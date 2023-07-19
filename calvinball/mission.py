import dcs
import json
import os
import shutil
import sys
from jinja2 import Template
from pathlib import Path

import calvinball

class Mission:
    def __init__(self, terrain: dcs.terrain, miz_name: str, ctld: calvinball.ctld.Ctld, clients: calvinball.clients.Clients, red_airwings: calvinball.redairwing.RedAirwings, blue_airwings: calvinball.blueairwing.BlueAirwings, carriers: calvinball.carriers.Carriers, qrf: calvinball.qrf.Qrf, reinforcement: calvinball.reinforcement.Reinforcement, red_brigades: calvinball.redbrigade.RedBrigades, blue_brigades: calvinball.bluebrigade.BlueBrigades) -> None:
        self.m = dcs.Mission(terrain=terrain)
        self.miz_name = miz_name
        self.ctld = ctld
        self.qrf = qrf
        self.reinforcement = reinforcement
        self.clients = clients
        self.red_airwings = red_airwings
        self.blue_airwings = blue_airwings
        self.carriers = carriers
        self.red_brigades = red_brigades
        self.blue_brigades = blue_brigades
        self.json_root = os.path.realpath(os.path.join(sys.modules[self.__module__].__file__, '../' 'json'))
        self.mission_resource_path = os.path.realpath(os.path.join(sys.modules[self.__module__].__file__, '../' 'resources'))
        self.common_resource_path = os.path.realpath(os.path.join(sys.modules[self.__module__].__file__, '../../../' 'resources'))
        self.objectives_json_path = os.path.join(self.json_root, "objectives.json")
        self.tasks_json_path = os.path.join(self.json_root, "tasks.json")
        self.airbases_json_path = os.path.join(self.json_root, "airbases.json")
        self.statics_json_path = os.path.join(self.json_root, "statics.json")
        self.qrfs_json_path = os.path.join(self.json_root, "qrf.json")
        self.reinforcements_json_path = os.path.join(self.json_root, "reinforcement.json")
        self.farps_json_path = os.path.join(self.json_root, "farps.json")
        self.roadbases_json_path = os.path.join(self.json_root, "roadbases.json")
        self.vehicle_groups_path = os.path.join(self.json_root, "vehicle-groups.json")
        self.ship_groups_path = os.path.join(self.json_root, "ship-groups.json")
        self.unclassified_zones_path = os.path.join(self.json_root, "unclassified.json")
        self.mission_root_path = os.path.join(
            str(Path.home()), "Saved Games", "DCS.openbeta", "Missions", self.miz_name
        )
        self.miz_export_path = os.path.join(
            self.mission_root_path, f"{self.miz_name}.miz"
        )

    def build(self, edit: bool, package: bool):
        self.__configure_settings()
        self.__build_vehicle_groups()
        self.__build_ship_groups()
        if edit:
            self.__build_static_groups()
        self.ctld.build(self.m)
        self.qrf.build(self.m)
        self.reinforcement.build(self.m)
        self.__tasks()
        self.__farps()
        self.__roadbases()
        self.__airbases()
        self.__qrfs()
        self.__reinforcements()
        self.__objectives()
        self.__unclassified()
        carriers = self.carriers.build(self.m, edit)
        ctld_groups, csar_groups, farp_groups, roadbase_groups, airbase_groups, carrier_groups = self.clients.build(self.m, edit)
        red_airwings = self.red_airwings.build(self.m)
        blue_airwings = self.blue_airwings.build(self.m)
        red_brigades = self.red_brigades.build(self.m)
        blue_brigades = self.blue_brigades.build(self.m)
        self.__write_db(ctld_groups, csar_groups, farp_groups, roadbase_groups, airbase_groups, red_airwings, blue_airwings, carriers, carrier_groups, red_brigades, blue_brigades, edit, True)
        self.__save_mission(package, edit)

        print("Make sure to manually add a late activated `Downed Pilot`")

    def __configure_settings(self):
        self.m.coalition["blue"].countries.clear()
        self.m.coalition["blue"].add_country(dcs.countries.CombinedJointTaskForcesBlue())
        self.m.coalition["red"].countries.clear()
        self.m.coalition["red"].add_country(dcs.countries.CombinedJointTaskForcesRed())

        self.m.groundControl.pilot_can_control_vehicles = True

        # in the same order as the ME, everything is forced, leave nothing to chance
        self.m.forced_options.permit_crash = False
        self.m.forced_options.external_views = True
        self.m.forced_options.options_view = dcs.forcedoptions.ForcedOptions.Views.OnlyAllies
        self.m.forced_options.labels = dcs.forcedoptions.ForcedOptions.Labels.NeutralDot
        self.m.forced_options.easy_flight = False
        self.m.forced_options.easy_radar = False
        self.m.forced_options.immortal = False
        self.m.forced_options.fuel = False
        self.m.forced_options.weapons = False
        self.m.forced_options.easy_communication = True
        self.m.forced_options.radio = False
        self.m.forced_options.unrestricted_satnav = True
        self.m.forced_options.padlock = False
        self.m.forced_options.wake_turbulence = False
        self.m.forced_options.geffect = dcs.forcedoptions.ForcedOptions.GEffect.Realistic
        self.m.forced_options.accidental_failures = False
        self.m.forced_options.mini_hud = False
        self.m.forced_options.cockpit_visual_recon_mode = False
        self.m.forced_options.user_marks = True
        self.m.forced_options.civil_traffic = dcs.forcedoptions.ForcedOptions.CivilTraffic.Off
        self.m.forced_options.birds = 0
        self.m.forced_options.cockpit_status_bar = False
        self.m.forced_options.battle_damage_assessment = False

    def __add_sound_resource(self, resource: str):
        triggerOnce = dcs.triggers.TriggerOnce()
        triggerOnce.actions.append(dcs.action.SoundToCountry(dcs.countries.Australia.name, self.m.map_resource.add_resource_file(resource)))
        self.m.triggerrules.triggers.append(triggerOnce)

    def __common_resource(self, resource: str) -> str:
        return os.path.join(self.common_resource_path, resource)

    def __mission_resource(self, resource: str) -> str:
        return os.path.join(self.mission_resource_path, resource)

    def __save_mission(self, package: bool, configure_for_editor: bool) -> str:
        os.makedirs(self.mission_root_path, exist_ok=True)

        if not configure_for_editor:
            load_trigger = dcs.triggers.TriggerStart()
            load_trigger.actions.append(dcs.action.DoScriptFile(self.m.map_resource.add_resource_file(self.__common_resource("Moose.lua"))))
            load_trigger.actions.append(dcs.action.DoScriptFile(self.m.map_resource.add_resource_file(self.__common_resource("SplashDamage.lua"))))
            load_trigger.actions.append(dcs.action.DoScriptFile(self.m.map_resource.add_resource_file(self.__common_resource("Hercules_Cargo.lua"))))
            load_trigger.actions.append(dcs.action.DoScript(dcs.translation.String(f"trigger.action.setUserFlag(\"SSB\",100)")))

            # hacks and workarounds
            if self.m.terrain.name == "Syria":
                load_trigger.actions.append(dcs.action.DoScriptFile(self.m.map_resource.add_resource_file(self.__common_resource("larnaca-hotfix.lua"))))
            load_trigger.actions.append(dcs.action.DoScriptFile(self.m.map_resource.add_resource_file(self.__common_resource("kill-ai-helo-hotfix.lua"))))

            local_db_script_path = self.__mission_resource(f"{self.miz_name}_db.lua")
            local_config_path = self.__mission_resource(f"config.lua")
            local_script_path = self.__common_resource("calvinball.lua")

            if package:
                load_trigger.actions.append(dcs.action.DoScriptFile(self.m.map_resource.add_resource_file(local_db_script_path)))
                load_trigger.actions.append(dcs.action.DoScriptFile(self.m.map_resource.add_resource_file(local_config_path)))
                load_trigger.actions.append(dcs.action.DoScriptFile(self.m.map_resource.add_resource_file(local_script_path)))
            else:
                hot_db_script_path = os.path.join(self.mission_root_path, f"{self.miz_name}_db.lua")
                hot_config_script_path = os.path.join(self.mission_root_path, "calvinball.lua")
                hot_script_path = os.path.join(self.mission_root_path, "config.lua")
                load_trigger.actions.append(dcs.action.DoScript(dcs.translation.String(f"dofile([[{hot_db_script_path}]])")))
                load_trigger.actions.append(dcs.action.DoScript(dcs.translation.String(f"dofile([[{hot_config_script_path}]])")))
                load_trigger.actions.append(dcs.action.DoScript(dcs.translation.String(f"dofile([[{hot_script_path}]])")))
                shutil.copy(local_db_script_path, self.mission_root_path)
                shutil.copy(local_config_path, self.mission_root_path)
                shutil.copy(local_script_path, self.mission_root_path)

            self.m.triggerrules.triggers.append(load_trigger)

            self.__add_sound_resource(self.__common_resource("beacon.ogg"))

        self.m.save(self.miz_export_path)


    def __write_db(self, ctld_groups, csar_groups, farp_groups, roadbase_groups, airbase_groups, red_airwings, blue_airwings, carriers, carrier_groups, red_brigades, blue_brigades, configure_for_editor, devmode):
        with open(self.objectives_json_path) as json_file:
            obj = json.load(json_file)
        with open(self.tasks_json_path) as json_file:
            tasks = json.load(json_file)
        with open(self.airbases_json_path) as json_file:
            airbases = json.load(json_file)
        with open(self.statics_json_path) as json_file:
            statics = json.load(json_file)
        with open(self.qrfs_json_path) as json_file:
            qrfs = json.load(json_file)
        with open(self.reinforcements_json_path) as json_file:
            reinforcements = json.load(json_file)
        with open(self.farps_json_path) as json_file:
            farps = json.load(json_file)
        with open(self.roadbases_json_path) as json_file:
            roadbases = json.load(json_file)
        with open(self.__mission_resource(f"{self.miz_name}_db.lua"), "w") as lua_file:
            with open(self.__common_resource("calvinball_db.jinja2")) as jinja_file:
                template = Template(jinja_file.read(), trim_blocks=True, lstrip_blocks=True)
                lua_file.write(template.render(obj=obj, ctld_groups=ctld_groups, csar_groups=csar_groups, airbases=airbases, tasks=tasks, statics=statics, qrfs=qrfs, reinforcements=reinforcements, farps=farps, farp_groups=farp_groups, roadbases=roadbases, roadbase_groups=roadbase_groups, airbase_groups=airbase_groups, red_airwings=red_airwings, blue_airwings=blue_airwings, carriers=carriers, carrier_groups=carrier_groups, red_brigades=red_brigades, blue_brigades=blue_brigades, late_activate_statics=not configure_for_editor, devmode=devmode, missionName=self.miz_name))

    def __build_vehicle_groups(self):
        with open(self.vehicle_groups_path) as json_file:
            coalitions = json.load(json_file)
            for coalition_name, groups in coalitions.items():
                if coalition_name == "red":
                    country = self.m.country(dcs.countries.CombinedJointTaskForcesRed.name)
                if coalition_name == "blue":
                    country = self.m.country(dcs.countries.CombinedJointTaskForcesBlue.name)

                for group_name, units in groups.items():
                    vg = self.m.vehicle_group(country, group_name, dcs.vehicles.vehicle_map[units[0]["type"]], dcs.mapping.Point(units[0]["x"], units[0]["y"], self.m.terrain), units[0]["heading"], group_size=1)
                    vg.late_activation = True
                    for i, u in enumerate(units, start=1):
                        if i == 1:
                            continue
                        v = self.m.vehicle(group_name + f" Unit #{i+1}", dcs.vehicles.vehicle_map[u["type"]])
                        v.position.x = u["x"]
                        v.position.y = u["y"]
                        v.heading = u["heading"]
                        vg.add_unit(v)

    def __build_ship_groups(self):
        with open(self.ship_groups_path) as json_file:
            coalitions = json.load(json_file)
            for coalition_name, groups in coalitions.items():
                if coalition_name == "red":
                    country = self.m.country(dcs.countries.CombinedJointTaskForcesRed.name)
                if coalition_name == "blue":
                    country = self.m.country(dcs.countries.CombinedJointTaskForcesBlue.name)

                for group_name, units in groups.items():
                    sg = self.m.ship_group(country, group_name, dcs.ships.ship_map[units[0]["type"]], dcs.mapping.Point(units[0]["x"], units[0]["y"], self.m.terrain), units[0]["heading"], group_size=1)
                    sg.late_activation = True
                    for i, u in enumerate(units, start=1):
                        if i == 1:
                            continue
                        s = self.m.ship(group_name + f" Unit #{i+1}", dcs.ships.ship_map[u["type"]])
                        s.position.x = u["x"]
                        s.position.y = u["y"]
                        s.heading = u["heading"]
                        sg.add_unit(s)

    def __build_static_groups(self):
        with open(self.statics_json_path) as json_file:
            coalitions = json.load(json_file)
            for coalition_name, groups in coalitions.items():
                if coalition_name == "red":
                    country = self.m.country(dcs.countries.CombinedJointTaskForcesRed.name)
                if coalition_name == "blue":
                    country = self.m.country(dcs.countries.CombinedJointTaskForcesBlue.name)
                for group_name, unit in groups.items():
                    sg = dcs.unitgroup.StaticGroup(self.m.next_group_id(), group_name)
                    s = dcs.unit.Static(self.m.next_unit_id(), group_name, unit["type"], self.m.terrain)
                    s.load_from_dict(unit)

                    sg.add_unit(s)
                    sg.hidden = False
                    sg.dead = False

                    sp = dcs.point.StaticPoint(s.position)
                    sg.add_point(sp)

                    country.add_static_group(sg)
            
    def __add_prop(self, props, dict, key):
        if key in dict:
            props.append({"key": key, "value": dict[key]})

    def __objectives(self):
        with open(self.objectives_json_path) as json_file:
            obj = json.load(json_file)

            objective_centers = {}
            objective_zones = {}
            strand_colors = [
                {1: 0.5, 2: 0, 3: 0, 4: 0.38},
                {1: 0.0, 2: 0, 3: .75, 4: 0.38},
                {1: 0, 2: .5, 3: 1, 4: 0.38},
                {1: 0, 2: 0.5, 3: 0, 4: 0.38},
            ]

            for objective_name, objective in obj["objectives"].items():
                props_a = [
                    {"key": "label", "value": objective["label"]},
                    {"key": "component", "value": "objective"},
                    {"key": "completeSound", "value": objective["completeSound"]},
                    {"key": "borderZones", "value": ",".join(objective["borderZones"])},
                    {"key": "capZones", "value": ",".join(objective["capZones"])},
                    {"key": "carriers", "value": ",".join(objective["carriers"])},
                    {"key": "qrfKillOnComplete", "value": ",".join(objective["qrfKillOnComplete"])},
                ]

                props = {k+1: v for k, v in enumerate(props_a)}

                p = dcs.mapping.Point(objective["x"], objective["y"], self.m.terrain)
                oz = self.m.triggers.add_triggerzone_quad(p, [dcs.mapping.Point(v["x"], v["y"], self.m.terrain) for v in objective["vertices"]], name=objective_name, properties=props)
                objective_zones[oz.name] = oz
                for node_name, node in objective["nodes"].items():
                    props_a = [
                        {"key": "label", "value": node["label"]},
                        {"key": "component", "value": "node"},
                        {"key": "redSurrenderThreshold", "value": node["redSurrenderThreshold"]},
                        {"key": "blueCaptureThreshold", "value": node["blueCaptureThreshold"]},
                    ]
                    props = {k+1: v for k, v in enumerate(props_a)}
                    self.m.triggers.add_triggerzone(dcs.mapping.Point(node["x"], node["y"], self.m.terrain), node["radius"], name=node_name, properties=props)
                objective_centers[objective_name] = p

                if len(objective["tasks"]) > 0:
                    fg = self.m.flight_group_inflight(self.m.country(dcs.countries.CombinedJointTaskForcesBlue.name), f"OBJTASKLINK-{oz.name}", dcs.planes.F_16C_50, dcs.mapping.Point(p.x+50, p.y+50, self.m.terrain), 420, group_size=1)
                    fg.late_activation = True
                    for task_name in objective["tasks"]:
                        for zone in self.m.triggers.zones():
                            if zone.name == task_name:
                                fg.add_waypoint(zone.position, 420)

                if len(objective["farps"]) > 0:
                    fg = self.m.flight_group_inflight(self.m.country(dcs.countries.CombinedJointTaskForcesBlue.name), f"OBJFARPLINK-{oz.name}", dcs.planes.F_16C_50, dcs.mapping.Point(p.x+50, p.y+50, self.m.terrain), 420, group_size=1)
                    fg.late_activation = True
                    for farp_name in objective["farps"]:
                        for zone in self.m.triggers.zones():
                            if zone.name == farp_name:
                                fg.add_waypoint(zone.position, 420)

                if len(objective["roadbases"]) > 0:
                    fg = self.m.flight_group_inflight(self.m.country(dcs.countries.CombinedJointTaskForcesBlue.name), f"OBJROADBASELINK-{oz.name}", dcs.planes.F_16C_50, dcs.mapping.Point(p.x+50, p.y+50, self.m.terrain), 420, group_size=1)
                    fg.late_activation = True
                    for roadbase_name in objective["roadbases"]:
                        for zone in self.m.triggers.zones():
                            if zone.name == roadbase_name:
                                fg.add_waypoint(zone.position, 420)
                
                if len(objective["airbases"]) > 0:
                    fg = self.m.flight_group_inflight(self.m.country(dcs.countries.CombinedJointTaskForcesBlue.name), f"OBJAIRBASELINK-{oz.name}", dcs.planes.F_16C_50, dcs.mapping.Point(p.x+50, p.y+50, self.m.terrain), 420, group_size=1)
                    fg.late_activation = True
                    for airbase_name in objective["airbases"]:
                        for zone in self.m.triggers.zones():
                            if zone.name == airbase_name:
                                fg.add_waypoint(zone.position, 420)

                if len(objective["qrfs"]) > 0:
                    fg = self.m.flight_group_inflight(self.m.country(dcs.countries.CombinedJointTaskForcesBlue.name), f"OBJQRFLINK-{oz.name}", dcs.planes.F_16C_50, dcs.mapping.Point(p.x+50, p.y+50, self.m.terrain), 420, group_size=1)
                    fg.late_activation = True
                    for qrf_name in objective["qrfs"]:
                        for zone in self.m.triggers.zones():
                            if zone.name == qrf_name:
                                fg.add_waypoint(zone.position, 420)
                
                if len(objective["reinforcements"]) > 0:
                    fg = self.m.flight_group_inflight(self.m.country(dcs.countries.CombinedJointTaskForcesBlue.name), f"OBJREINFORCEMENTLINK-{oz.name}", dcs.planes.F_16C_50, dcs.mapping.Point(p.x+50, p.y+50, self.m.terrain), 420, group_size=1)
                    fg.late_activation = True
                    for reinforcement_name in objective["reinforcements"]:
                        for zone in self.m.triggers.zones():
                            if zone.name == reinforcement_name:
                                fg.add_waypoint(zone.position, 420)

            si = 0
            for strand_name, sequence in obj["strands"].items():
                fg = self.m.flight_group_inflight(self.m.country(dcs.countries.CombinedJointTaskForcesBlue.name), strand_name, dcs.planes.F_16C_50, dcs.mapping.Point(self.m.terrain.bullseye_blue["x"], self.m.terrain.bullseye_blue["y"], self.m.terrain), 420, group_size=1)
                fg.late_activation = True
                for obj in sequence:
                    fg.add_waypoint(objective_centers[obj], 420)
                    objective_zones[obj].color = strand_colors[si]
                si = si + 1

    def __tasks(self):
        with open(self.tasks_json_path) as json_file:
            tasks = json.load(json_file)
            for task_name, task in tasks.items():
                p = dcs.mapping.Point(task["x"], task["y"], self.m.terrain)

                props_a = [
                    {"key": "label", "value": task["label"]},
                    {"key": "component", "value": "task"},
                    {"key": "completeSound", "value": task["completeSound"]},
                ]

                self.__add_prop(props_a, task, "auftrag")
                if task["auftrag"] in ["SEAD", "BOMBING", "ANTISHIP"]:
                    self.__add_prop(props_a, task, "staticTargetNameContains")
                    self.__add_prop(props_a, task, "groupTargetNameContains")
                    props_a.append({"key": "targetUnitTypes", "value": ",".join(task["targetUnitTypes"])})
                if task["auftrag"] in ["BOMBING"]:
                    props_a.append({"key": "sceneryTargetZoneNames", "value": ",".join(task["sceneryTargetZoneNames"])})
                if task["auftrag"] in ["CSAR"]:
                    self.__add_prop(props_a, task, "targetZone")
                    self.__add_prop(props_a, task, "targetName")
                self.__add_prop(props_a, task, "description")

                props = {k+1: v for k, v in enumerate(props_a)}

                self.m.triggers.add_triggerzone_quad(p, [dcs.mapping.Point(v["x"], v["y"], self.m.terrain) for v in task["vertices"]], name=task_name, properties=props)

    def __airbases(self):
        with open(self.airbases_json_path) as json_file:
            airbases = json.load(json_file)
            for airbase_name, airbase in airbases.items():
                p = dcs.mapping.Point(airbase["x"], airbase["y"], self.m.terrain)
                self.m.triggers.add_triggerzone(p, airbase["radius"], name=airbase_name, properties={1: {"key": "label", "value": airbase["label"]}, 2: {"key": "component", "value": "airbase"}})

    def __unclassified(self):
        with open(self.unclassified_zones_path) as json_file:
            unclassified = json.load(json_file)
            for unclassified_name, unclassified in unclassified.items():
                p = dcs.mapping.Point(unclassified["x"], unclassified["y"], self.m.terrain)
                if "radius" in unclassified:
                    self.m.triggers.add_triggerzone(p, unclassified["radius"], name=unclassified_name)
                if "vertices" in unclassified:
                    self.m.triggers.add_triggerzone_quad(p, [dcs.mapping.Point(v["x"], v["y"], self.m.terrain) for v in unclassified["vertices"]], name=unclassified_name)

    def __qrfs(self):
        with open(self.qrfs_json_path) as json_file:
            qrfs = json.load(json_file)
            for qrf_name, qrf in qrfs.items():
                p = dcs.mapping.Point(qrf["x"], qrf["y"], self.m.terrain)

                props_a = [
                    {"key": "label", "value": qrf["label"]},
                    {"key": "component", "value": "qrf"},
                    {"key": "vehicleQrfTemplates", "value": ",".join(qrf["vehicleQrfTemplates"])},
                ]

                props = {k+1: v for k, v in enumerate(props_a)}

                self.m.triggers.add_triggerzone_quad(p, [dcs.mapping.Point(v["x"], v["y"], self.m.terrain) for v in qrf["vertices"]], name=qrf_name, properties=props)

    def __reinforcements(self):
        with open(self.reinforcements_json_path) as json_file:
            reinforcements = json.load(json_file)
            for reinforcement_name, reinforcement in reinforcements.items():
                p = dcs.mapping.Point(reinforcement["x"], reinforcement["y"], self.m.terrain)

                props_a = [
                    {"key": "label", "value": reinforcement["label"]},
                    {"key": "component", "value": "reinforcement"},
                    {"key": "vehicleReinforcementTemplates", "value": ",".join(reinforcement["vehicleReinforcementTemplates"])},
                ]

                props = {k+1: v for k, v in enumerate(props_a)}

                self.m.triggers.add_triggerzone_quad(p, [dcs.mapping.Point(v["x"], v["y"], self.m.terrain) for v in reinforcement["vertices"]], name=reinforcement_name, properties=props)

    def __farps(self):
        with open(self.farps_json_path) as json_file:
            farps = json.load(json_file)
            for farp_name, farp in farps.items():
                props_a = [
                    {"key": "label", "value": farp["label"]},
                    {"key": "component", "value": "farp"},
                    {"key": "clearScenery", "value": farp["clearScenery"]},
                ]

                props = {k+1: v for k, v in enumerate(props_a)}

                z = self.m.triggers.add_triggerzone(dcs.mapping.Point(farp["x"], farp["y"], self.m.terrain), farp["radius"], name=farp_name, properties=props)

                removeType = None
                match farp["clearScenery"]:
                    case "all":
                        removeType = dcs.action.RemoveSceneObjectsMask.ALL
                    case "trees":
                        removeType = dcs.action.RemoveSceneObjectsMask.TREES_ONLY
                    case "objects":
                        removeType = dcs.action.RemoveSceneObjectsMask.OBJECTS_ONLY

                if removeType is not None:
                    load_trigger = dcs.triggers.TriggerStart()
                    load_trigger.actions.append(dcs.action.RemoveSceneObjects(removeType, z.id))
                    self.m.triggerrules.triggers.append(load_trigger)

    def __roadbases(self):
        with open(self.roadbases_json_path) as json_file:
            roadbases = json.load(json_file)
            for roadbase_name, roadbase in roadbases.items():
                p = dcs.mapping.Point(roadbase["x"], roadbase["y"], self.m.terrain)

                props_a = [
                    {"key": "label", "value": roadbase["label"]},
                    {"key": "component", "value": "roadbase"},
                    {"key": "clearScenery", "value": roadbase["clearScenery"]},
                ]

                props = {k+1: v for k, v in enumerate(props_a)}

                z = self.m.triggers.add_triggerzone_quad(p, [dcs.mapping.Point(v["x"], v["y"], self.m.terrain) for v in roadbase["vertices"]], name=roadbase_name, properties=props)

                removeType = None
                match roadbase["clearScenery"]:
                    case "all":
                        removeType = dcs.action.RemoveSceneObjectsMask.ALL
                    case "trees":
                        removeType = dcs.action.RemoveSceneObjectsMask.TREES_ONLY
                    case "objects":
                        removeType = dcs.action.RemoveSceneObjectsMask.OBJECTS_ONLY

                if removeType is not None:
                    load_trigger = dcs.triggers.TriggerStart()
                    load_trigger.actions.append(dcs.action.RemoveSceneObjects(removeType, z.id))
                    self.m.triggerrules.triggers.append(load_trigger)
