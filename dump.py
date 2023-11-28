import dcs
import argparse
import json
from shapely.geometry import Point, Polygon
from pathlib import Path
from collections import defaultdict
import csv
from prettytable import PrettyTable


def get_vehicle_groups(m: dcs.Mission):
    coalitions = {
        "red": {},
        "blue": {},
        "neutrals": {}
    }
    for c1 in m.coalition.values():
        for c2 in c1.countries.values():
            for vg in c2.vehicle_group:
                units = []
                for u in vg.units:
                    units.append({"type": u.type, "x": u.position.x, "y": u.position.y, "heading": u.heading})
                coalitions[c1.name][vg.name] = units
    return coalitions

def get_ship_groups(m: dcs.Mission):
    coalitions = {
        "red": {},
        "blue": {},
        "neutrals": {}
    }
    for c1 in m.coalition.values():
        for c2 in c1.countries.values():
            for sg in c2.ship_group:
                units = []
                for u in sg.units:
                    units.append({"type": u.type, "x": u.position.x, "y": u.position.y, "heading": u.heading})
                coalitions[c1.name][sg.name] = units
    return coalitions

def get_static_groups(m: dcs.Mission):
    coalitions = {
        "red": {},
        "blue": {},
        "neutrals": {}
    }
    for c1 in m.coalition.values():
        for c2 in c1.countries.values():
            for sg in c2.static_group:
                u = sg.units[0]
                coalitions[c1.name][sg.name] = u.dict()
                coalitions[c1.name][sg.name]["name"] = sg.name
                del coalitions[c1.name][sg.name]["unitId"]

    return coalitions


def get_objective_zones(m: dcs.Mission):
    objective_zones = {}
    objective_nodes = {}
    for z in m.triggers.zones():
        label = None
        component = None
        completeSound = None
        borderZones = None
        capZones = None
        redAwacsZones = None
        blueAwacsZones = None
        carriers = None
        qrfKillOnComplete = ""
        redSurrenderThreshold = "1"
        blueCaptureThreshold = "0"
        for v in z.properties.values():
            if(v["key"] == "label"):
                label = v["value"]
            if(v["key"] == "component"):
                component = v["value"]
            if(v["key"] == "completeSound"):
                completeSound = v.get("value", "")
            if(v["key"] == "borderZones"):
                borderZones = v.get("value", "")
            if(v["key"] == "capZones"):
                capZones = v.get("value", "")
            if(v["key"] == "redAwacsZones"):
                redAwacsZones = v.get("value", "")
            if(v["key"] == "blueAwacsZones"):
                blueAwacsZones = v.get("value", "")
            if(v["key"] == "carriers"):
                carriers = v.get("value", "")
            if(v["key"] == "redSurrenderThreshold"):
                redSurrenderThreshold = v.get("value", "1")
            if(v["key"] == "blueCaptureThreshold"):
                blueCaptureThreshold = v.get("value", "")
            if(v["key"] == "qrfKillOnComplete"):
                qrfKillOnComplete = v.get("value", "")
        
        if(component == None):
            continue

        if(component == "objective" and isinstance(z, dcs.triggers.TriggerZoneQuadPoint)):
            objective_zones[z.name] = {
                "label": label,
                "x": z.position.x,
                "y": z.position.y,
                "vertices": [{"x": v.x, "y": v.y } for v in z.verticies],
                "completeSound": completeSound,
                "borderZones": [x.strip() for x in borderZones.split(',') if x],
                "capZones": [x.strip() for x in capZones.split(',') if x],
                "redAwacsZones": [x.strip() for x in redAwacsZones.split(',') if x],
                "blueAwacsZones": [x.strip() for x in blueAwacsZones.split(',') if x],
                "carriers": [x.strip() for x in carriers.split(',') if x],
                "qrfKillOnComplete": [x.strip() for x in qrfKillOnComplete.split(',') if x],
                "nodes": {},
                "tasks": [],
                "farps": [],
                "roadbases": [],
                "airbases": [],
                "qrfs": [],
                "reinforcements": [],
                "vehicle_groups": [],
                "ship_groups": [],
                "static_groups": [],
                "component": "objective"
            }
        
        if(component == "node"):
            objective_nodes[z.name] = {"label": label, "x": z.position.x, "y": z.position.y, "radius": z.radius, "redSurrenderThreshold": redSurrenderThreshold, "blueCaptureThreshold": blueCaptureThreshold }

    for objective_zone in objective_zones.values():
        objective_poly = Polygon([(v["x"], v["y"]) for v in objective_zone["vertices"]])
        for node_name, node in objective_nodes.items():
            node_point = Point(node["x"], node["y"])
            if objective_poly.contains(node_point):
                objective_zone["nodes"][node_name] = node

    return objective_zones

def get_task_zones(m: dcs.Mission):
    task_zones = {}
    for z in m.triggers.zones():
        label = None
        component = None
        completeSound = ""
        auftrag = ""
        staticTargetNameContains = ""
        groupTargetNameContains = ""
        targetUnitTypes = ""
        sceneryTargetZoneNames = ""
        targetZone = ""
        targetName = ""
        description = ""
        for v in z.properties.values():
            if(v["key"] == "label"):
                label = v["value"]
            if(v["key"] == "component"):
                component = v["value"]
            if(v["key"] == "completeSound"):
                completeSound = v.get("value", "")
            if(v["key"] == "auftrag"):
                auftrag =  v.get("value", "")
            if auftrag in ["SEAD", "BOMBING", "ANTISHIP"]:
                if(v["key"] == "staticTargetNameContains"):
                    staticTargetNameContains =  v.get("value", "")
                if(v["key"] == "groupTargetNameContains"):
                    groupTargetNameContains =  v.get("value", "")
                if(v["key"] == "targetUnitTypes"):
                    targetUnitTypes =  v.get("value", "")
            if auftrag in ["BOMBING"]:
                if(v["key"] == "sceneryTargetZoneNames"):
                    sceneryTargetZoneNames =  v.get("value", "")
            if auftrag in ["CSAR"]:
                if(v["key"] == "targetZone"):
                    targetZone =  v.get("value", "")
                if(v["key"] == "targetName"):
                    targetName =  v.get("value", "")
            if(v["key"] == "description"):
                description =  v.get("value", "")
        
        if(component == None):
            continue

        if(component == "task" and isinstance(z, dcs.triggers.TriggerZoneQuadPoint)):
            task_zones[z.name] = {
                "label": label,
                "x": z.position.x,
                "y": z.position.y,
                "vertices": [{"x": v.x, "y": v.y } for v in z.verticies],
                "completeSound": completeSound,
                "auftrag": auftrag,
                "description": description,
                "vehicle_groups": [],
                "ship_groups": [],
                "static_groups": [],
                "component": "task"
            }

            if auftrag in ["SEAD", "BOMBING", "ANTISHIP"]:
                task_zones[z.name]["staticTargetNameContains"] = staticTargetNameContains
                task_zones[z.name]["groupTargetNameContains"] = groupTargetNameContains
                task_zones[z.name]["targetUnitTypes"] = *[x.strip() for x in targetUnitTypes.split(',') if x],
            if auftrag in ["BOMBING"]:
                task_zones[z.name]["sceneryTargetZoneNames"] = *[x.strip() for x in sceneryTargetZoneNames.split(',') if x],
            if auftrag in ["CSAR"]:
                task_zones[z.name]["targetZone"] = targetZone
                task_zones[z.name]["targetName"] = targetName

    return task_zones

def get_farp_zones(m: dcs.Mission):
    zones = {}
    for z in m.triggers.zones():
        label = None
        component = None
        clearScenery = None
        for v in z.properties.values():
            if(v["key"] == "label"):
                label = v["value"]
            if(v["key"] == "component"):
                component = v["value"]
            if(v["key"] == "clearScenery"):
                clearScenery =  v.get("value", "")
        
        if(component == None):
            continue

        if(component == "farp" and isinstance(z, dcs.triggers.TriggerZoneCircular)):
            zones[z.name] = {
                "label": label,
                "x": z.position.x,
                "y": z.position.y,
                "radius": z.radius,
                "clearScenery": clearScenery,
                "vehicle_groups": [],
                "ship_groups": [],
                "static_groups": [],
                "component": "farp"
            }
    return zones

def get_roadbase_zones(m: dcs.Mission):
    zones = {}
    for z in m.triggers.zones():
        label = None
        component = None
        clearScenery = None
        for v in z.properties.values():
            if(v["key"] == "label"):
                label = v["value"]
            if(v["key"] == "component"):
                component = v["value"]
            if(v["key"] == "clearScenery"):
                clearScenery =  v.get("value", "")
        
        if(component == None):
            continue

        if(component == "roadbase" and isinstance(z, dcs.triggers.TriggerZoneQuadPoint)):
            zones[z.name] = {
                "label": label,
                "x": z.position.x,
                "y": z.position.y,
                "vertices": [{"x": v.x, "y": v.y } for v in z.verticies],
                "clearScenery": clearScenery,
                "vehicle_groups": [],
                "ship_groups": [],
                "static_groups": [],
                "component": "roadbase"
            }
    return zones

def get_airbase_zones(m: dcs.Mission):
    zones = {}
    for z in m.triggers.zones():
        label = None
        component = None
        for v in z.properties.values():
            if(v["key"] == "label"):
                label = v["value"]
            if(v["key"] == "component"):
                component = v["value"]
        
        if(component == None):
            continue

        if(component == "airbase" and isinstance(z, dcs.triggers.TriggerZoneCircular)):
            zones[z.name] = {
                "label": label,
                "x": z.position.x,
                "y": z.position.y,
                "radius": z.radius,
                "vehicle_groups": [],
                "ship_groups": [],
                "static_groups": [],
                "component": "airbase"
            }
    return zones

def get_unclassified_zones(m: dcs.Mission):
    zones = {}
    for z in m.triggers.zones():
        label = None
        component = None
        for v in z.properties.values():
            if(v["key"] == "label"):
                label = v["value"]
            if(v["key"] == "component"):
                component = v["value"]
        
        if(component == None and isinstance(z, dcs.triggers.TriggerZoneCircular)):
            zones[z.name] = { "x": z.position.x, "y": z.position.y, "radius": z.radius }

        if(component == None and isinstance(z, dcs.triggers.TriggerZoneQuadPoint)):
            zones[z.name] = { 
                "x": z.position.x,
                "y": z.position.y,
                "vertices": [{"x": v.x, "y": v.y } for v in z.verticies]
            }

    return zones

def get_qrf_zones(m: dcs.Mission):
    zones = {}
    for z in m.triggers.zones():
        label = None
        component = None
        vehicleQrfTemplates = None
        for v in z.properties.values():
            if(v["key"] == "label"):
                label = v["value"]
            if(v["key"] == "component"):
                component = v["value"]
            if(v["key"] == "vehicleQrfTemplates"):
                vehicleQrfTemplates =  v.get("value", "")
        
        if(component == None):
            continue

        if(component == "qrf" and isinstance(z, dcs.triggers.TriggerZoneQuadPoint)):
            zones[z.name] = {
                "label": label,
                "x": z.position.x,
                "y": z.position.y,
                "vertices": [{"x": v.x, "y": v.y } for v in z.verticies],
                "vehicleQrfTemplates": [x.strip() for x in vehicleQrfTemplates.split(',') if x],
                "vehicle_groups": [],
                "ship_groups": [],
                "static_groups": [],
                "component": "qrf"
            }

    return zones

def get_reinforcement_zones(m: dcs.Mission):
    zones = {}
    for z in m.triggers.zones():
        label = None
        component = None
        vehicleReinforcementTemplates = None
        for v in z.properties.values():
            if(v["key"] == "label"):
                label = v["value"]
            if(v["key"] == "component"):
                component = v["value"]
            if(v["key"] == "vehicleReinforcementTemplates"):
                vehicleReinforcementTemplates =  v.get("value", "")
        
        if(component == None):
            continue

        if(component == "reinforcement" and isinstance(z, dcs.triggers.TriggerZoneQuadPoint)):
            zones[z.name] = {
                "label": label,
                "x": z.position.x,
                "y": z.position.y,
                "vertices": [{"x": v.x, "y": v.y } for v in z.verticies],
                "vehicleReinforcementTemplates": [x.strip() for x in vehicleReinforcementTemplates.split(',') if x],
                "vehicle_groups": [],
                "ship_groups": [],
                "static_groups": [],
                "component": "reinforcement"
            }

    return zones

def assign_groups_to_zones(objective_zones, task_zones, qrf_zones, farp_zones, roadbase_zones, airbase_zones, reinforcement_zones, vehicle_groups, ship_groups, static_groups):
    # We only want to track these in a single zone, in order of preference.
    # Generally the issue is a objective zone overlapping one of the others)
    handled_vehicles = {}
    handled_ships = {}
    handled_statics = {}

    zone_sequence = [airbase_zones, farp_zones, roadbase_zones, task_zones, qrf_zones, objective_zones, reinforcement_zones]
    for zone_set in zone_sequence:
        for zone in zone_set.values():
            if "vertices" in zone:
                geometry = Polygon([(v["x"], v["y"]) for v in zone["vertices"]])
            else: 
                geometry = Point(zone["x"], zone["y"]).buffer(zone["radius"])

            is_blue_only = zone["component"] == "farp" or zone["component"] == "airbase" or zone["component"] == "reinforcement" or zone["component"] == "roadbase"

            for coalition, groups in vehicle_groups.items():
                for group_name, group in groups.items():
                    group_point = Point(group[0]["x"], group[0]["y"])
                    if group_name not in handled_vehicles and geometry.contains(group_point):
                        if (is_blue_only and coalition == "blue") or not is_blue_only:
                            zone["vehicle_groups"].append(group_name)
                            handled_vehicles[group_name] = True
            for coalition, groups in ship_groups.items():
                for group_name, group in groups.items():
                    group_point = Point(group[0]["x"], group[0]["y"])
                    if group_name not in handled_ships and geometry.contains(group_point):
                        if (is_blue_only and coalition == "blue") or not is_blue_only:
                            zone["ship_groups"].append(group_name)
                            handled_ships[group_name] = True
            for coalition, groups in static_groups.items():
                for group_name, group in groups.items():
                    group_point = Point(group["x"], group["y"])
                    if group_name not in handled_statics and geometry.contains(group_point):
                        if (is_blue_only and coalition == "blue") or not is_blue_only:
                            zone["static_groups"].append(group_name)
                            handled_statics[group_name] = True

    # purge the unhandled...
    for groups in vehicle_groups.values():
        delete = [group_name for group_name in groups.keys() if group_name not in handled_vehicles]
        for group_name in delete:
            del groups[group_name]
    for groups in ship_groups.values():
        delete = [group_name for group_name in groups.keys() if group_name not in handled_ships]
        for group_name in delete:
            del groups[group_name]
    for groups in static_groups.values():
        delete = [group_name for group_name in groups.keys() if group_name not in handled_statics]
        for group_name in delete:
            del groups[group_name]

def get_strands(m: dcs.Mission):
    strands = {}
    for c1 in m.coalition.values():
        for c2 in c1.countries.values():
            for pg in c2.plane_group:
                if(pg.name.startswith("STRAND")):
                    strands[pg.name] = []
                    for p in pg.points:
                        strands[pg.name].append(Point(p.position.x, p.position.y))
    return strands

def get_objective_task_links(m: dcs.Mission):
    objective_task_links = {}
    for c1 in m.coalition.values():
        for c2 in c1.countries.values():
            for pg in c2.plane_group:
                if(pg.name.startswith("OBJTASKLINK")):
                    objective_task_links[pg.name] = { "x": pg.position.x, "y": pg.position.y, "points": []}
                    for p in pg.points:
                        objective_task_links[pg.name]["points"].append(Point(p.position.x, p.position.y))
    return objective_task_links

def get_objective_farp_links(m: dcs.Mission):
    objective_farp_links = {}
    for c1 in m.coalition.values():
        for c2 in c1.countries.values():
            for pg in c2.plane_group:
                if(pg.name.startswith("OBJFARPLINK")):
                    objective_farp_links[pg.name] = { "x": pg.position.x, "y": pg.position.y, "points": []}
                    for p in pg.points:
                        objective_farp_links[pg.name]["points"].append(Point(p.position.x, p.position.y))
    return objective_farp_links

def get_objective_roadbase_links(m: dcs.Mission):
    objective_roadbase_links = {}
    for c1 in m.coalition.values():
        for c2 in c1.countries.values():
            for pg in c2.plane_group:
                if(pg.name.startswith("OBJROADBASELINK")):
                    objective_roadbase_links[pg.name] = { "x": pg.position.x, "y": pg.position.y, "points": []}
                    for p in pg.points:
                        objective_roadbase_links[pg.name]["points"].append(Point(p.position.x, p.position.y))
    return objective_roadbase_links

def get_objective_airbase_links(m: dcs.Mission):
    objective_airbase_links = {}
    for c1 in m.coalition.values():
        for c2 in c1.countries.values():
            for pg in c2.plane_group:
                if(pg.name.startswith("OBJAIRBASELINK")):
                    objective_airbase_links[pg.name] = { "x": pg.position.x, "y": pg.position.y, "points": []}
                    for p in pg.points:
                        objective_airbase_links[pg.name]["points"].append(Point(p.position.x, p.position.y))
    return objective_airbase_links

def get_objective_qrf_links(m: dcs.Mission):
    objective_qrf_links = {}
    for c1 in m.coalition.values():
        for c2 in c1.countries.values():
            for pg in c2.plane_group:
                if(pg.name.startswith("OBJQRFLINK")):
                    objective_qrf_links[pg.name] = { "x": pg.position.x, "y": pg.position.y, "points": []}
                    for p in pg.points:
                        objective_qrf_links[pg.name]["points"].append(Point(p.position.x, p.position.y))
    return objective_qrf_links

def get_objective_reinforcement_links(m: dcs.Mission):
    objective_reinforcement_links = {}
    for c1 in m.coalition.values():
        for c2 in c1.countries.values():
            for pg in c2.plane_group:
                if(pg.name.startswith("OBJREINFORCEMENTLINK")):
                    objective_reinforcement_links[pg.name] = { "x": pg.position.x, "y": pg.position.y, "points": []}
                    for p in pg.points:
                        objective_reinforcement_links[pg.name]["points"].append(Point(p.position.x, p.position.y))
    return objective_reinforcement_links

def assign_objective_zones_to_strands(zones, strands):
    merged = { "strands": {}, "objectives": zones }
    for strand_name, strand_points in strands.items():
        merged["strands"][strand_name] = []
        for strand_point in strand_points:
            for objective_name, objective_zone in zones.items():
                zone_poly = Polygon([(v["x"], v["y"]) for v in objective_zone["vertices"]])
                if zone_poly.contains(strand_point):
                    merged["strands"][strand_name].append(objective_name)
                    objective_zone["strand"] = strand_name
    return merged

def assign_task_zones_to_objectives(objective_zones, task_zones, objective_task_links):
     for name, link in objective_task_links.items():
        for objective_name, objective_zone in objective_zones.items():
                objective_zone_poly = Polygon([(v["x"], v["y"]) for v in objective_zone["vertices"]])
                if objective_zone_poly.contains(Point(link["x"], link["y"])):
                    for link_point in link["points"]:
                        for task_name, task_zone in task_zones.items():
                            task_zone_poly = Polygon([(v["x"], v["y"]) for v in task_zone["vertices"]])
                            if task_zone_poly.contains(link_point):
                                objective_zone["tasks"].append(task_name)

def assign_farp_zones_to_objectives(objective_zones, farp_zones, objective_farp_links):
     for name, link in objective_farp_links.items():
        for objective_name, objective_zone in objective_zones.items():
                objective_zone_poly = Polygon([(v["x"], v["y"]) for v in objective_zone["vertices"]])
                if objective_zone_poly.contains(Point(link["x"], link["y"])):
                    for link_point in link["points"]:
                        for farp_name, farp_zone in farp_zones.items():
                            farp_zone_circle = Point(farp_zone["x"], farp_zone["y"]).buffer(farp_zone["radius"])
                            if farp_zone_circle.contains(link_point):
                                objective_zone["farps"].append(farp_name)

def assign_roadbase_zones_to_objectives(objective_zones, roadbase_zones, objective_roadbase_links):
     for name, link in objective_roadbase_links.items():
        for objective_name, objective_zone in objective_zones.items():
                objective_zone_poly = Polygon([(v["x"], v["y"]) for v in objective_zone["vertices"]])
                if objective_zone_poly.contains(Point(link["x"], link["y"])):
                    for link_point in link["points"]:
                        for roadbase_name, roadbase_zone in roadbase_zones.items():
                            roadbase_zone_poly = Polygon([(v["x"], v["y"]) for v in roadbase_zone["vertices"]])
                            if roadbase_zone_poly.contains(link_point):
                                objective_zone["roadbases"].append(roadbase_name)

def assign_airbase_zones_to_objectives(objective_zones, airbase_zones, objective_airbase_links):
     for name, link in objective_airbase_links.items():
        for objective_name, objective_zone in objective_zones.items():
                objective_zone_poly = Polygon([(v["x"], v["y"]) for v in objective_zone["vertices"]])
                if objective_zone_poly.contains(Point(link["x"], link["y"])):
                    for link_point in link["points"]:
                        for airbase_name, airbase_zone in airbase_zones.items():
                            airbase_zone_circle = Point(airbase_zone["x"], airbase_zone["y"]).buffer(airbase_zone["radius"])
                            if airbase_zone_circle.contains(link_point):
                                objective_zone["airbases"].append(airbase_name)

def assign_qrf_zones_to_objectives(objective_zones, qrf_zones, objective_qrf_links):
     for name, link in objective_qrf_links.items():
        for objective_name, objective_zone in objective_zones.items():
                objective_zone_poly = Polygon([(v["x"], v["y"]) for v in objective_zone["vertices"]])
                if objective_zone_poly.contains(Point(link["x"], link["y"])):
                    for link_point in link["points"]:
                        for qrf_name, qrf_zone in qrf_zones.items():
                            qrf_zone_poly = Polygon([(v["x"], v["y"]) for v in qrf_zone["vertices"]])
                            if qrf_zone_poly.contains(link_point):
                                objective_zone["qrfs"].append(qrf_name)

def assign_reinforcement_zones_to_objectives(objective_zones, reinforcement_zones, objective_reinforcement_links):
     for name, link in objective_reinforcement_links.items():
        for objective_name, objective_zone in objective_zones.items():
                objective_zone_poly = Polygon([(v["x"], v["y"]) for v in objective_zone["vertices"]])
                if objective_zone_poly.contains(Point(link["x"], link["y"])):
                    for link_point in link["points"]:
                        for reinforcement_name, reinforcement_zone in reinforcement_zones.items():
                            reinforcement_zone_poly = Polygon([(v["x"], v["y"]) for v in reinforcement_zone["vertices"]])
                            if reinforcement_zone_poly.contains(link_point):
                                objective_zone["reinforcements"].append(reinforcement_name)

def debug_aircraft_farp(m: dcs.Mission, farp_zones):
    farp = {}
    for farp_name, farp_zone in farp_zones.items():
        farp[farp_name] = {}
        farp_zone_circle = Point(farp_zone["x"], farp_zone["y"]).buffer(farp_zone["radius"])
        for c1 in m.coalition.values():
            for c2 in c1.countries.values():
                for pg in c2.helicopter_group:
                    if farp_zone_circle.contains(Point(pg.position.x, pg.position.y)):
                        for u in pg.units:
                            if u.type not in farp[farp_name]:
                                farp[farp_name][u.type] = [{"x": u.position.x, "y": u.position.y, "heading": round(u.heading)}]
                            else:
                                farp[farp_name][u.type].append({"x": u.position.x, "y": u.position.y, "heading": round(u.heading)})
            
    print(json.dumps(farp,sort_keys=True))

def debug_aircraft_roadbase(m: dcs.Mission, roadbase_zones):
    roadbase = {}
    for roadbase_name, roadbase_zone in roadbase_zones.items():
        roadbase[roadbase_name] = {}
        roadbase_zone_poly = Polygon([(v["x"], v["y"]) for v in roadbase_zone["vertices"]])
        for c1 in m.coalition.values():
            for c2 in c1.countries.values():
                for pg in c2.plane_group:
                    if roadbase_zone_poly.contains(Point(pg.position.x, pg.position.y)):
                        for u in pg.units:
                            if u.type not in roadbase[roadbase_name]:
                                roadbase[roadbase_name][u.type] = [{"x": u.position.x, "y": u.position.y, "heading": round(u.heading)}]
                            else:
                                roadbase[roadbase_name][u.type].append({"x": u.position.x, "y": u.position.y, "heading": round(u.heading)})
            
    print(json.dumps(roadbase,sort_keys=True))

def debug_aircraft_airbase(m: dcs.Mission, airbase_zones):
    airbase = {}
    for airbase_name, airbase_zone in airbase_zones.items():
        airbase[airbase_name] = {}
        airbase_zone_circle = Point(airbase_zone["x"], airbase_zone["y"]).buffer(airbase_zone["radius"])
        for c1 in m.coalition.values():
            for c2 in c1.countries.values():
                for pg in c2.plane_group:
                    if airbase_zone_circle.contains(Point(pg.position.x, pg.position.y)):
                        for u in pg.units:
                            if u.type not in airbase[airbase_name]:
                                airbase[airbase_name][u.type] = [{"x": u.position.x, "y": u.position.y, "heading": round(u.heading)}]
                            else:
                                airbase[airbase_name][u.type].append({"x": u.position.x, "y": u.position.y, "heading": round(u.heading)})
                for pg in c2.helicopter_group:
                    if airbase_zone_circle.contains(Point(pg.position.x, pg.position.y)):
                        for u in pg.units:
                            if u.type not in airbase[airbase_name]:
                                airbase[airbase_name][u.type] = [{"x": u.position.x, "y": u.position.y, "heading": round(u.heading)}]
                            else:
                                airbase[airbase_name][u.type].append({"x": u.position.x, "y": u.position.y, "heading": round(u.heading)})
            
    print(json.dumps(airbase,sort_keys=True))

def report_units_in_obj(m: dcs.Mission, objective_zones):
    summary = {}
    for objective_zone in objective_zones.values():
        summary[objective_zone["label"]] = defaultdict(int)
        for vg in objective_zone["vehicle_groups"]:
            g = m.find_group(vg)
            for u in g.units:
                summary[objective_zone["label"]][u.type] += 1
        for sg in objective_zone["ship_groups"]:
            g = m.find_group(sg)
            for u in g.units:
                summary[objective_zone["label"]][u.type] += 1


    field_names = ["Objective", "Unit", "Count"]
    
    csv_rows = []

    for obj, units in summary.items():
        units_table = PrettyTable()
        units_table.field_names = field_names
        units_table.sortby = "Count"
        units_table.reversesort = True
        for unit, count in units.items():
            csv_rows.append([obj, unit, count])
            units_table.add_row([obj, unit, count])
        print(units_table)

    with open("objective-units.csv", "w", newline='') as outfile:
        w = csv.writer(outfile)
        w.writerow(field_names)
        w.writerows(csv_rows)

def dumpit(miz_export_path):
    m = dcs.mission.Mission()
    m.load_file(miz_export_path)

    vehicle_groups = get_vehicle_groups(m)
    ship_groups = get_ship_groups(m)
    static_groups = get_static_groups(m)
    objective_zones = get_objective_zones(m)
    task_zones = get_task_zones(m)
    qrf_zones = get_qrf_zones(m)
    reinforcement_zones = get_reinforcement_zones(m)
    farp_zones = get_farp_zones(m)
    roadbase_zones = get_roadbase_zones(m)
    airbase_zones = get_airbase_zones(m)
    strands = get_strands(m)
    objective_task_links = get_objective_task_links(m)
    objective_farp_links = get_objective_farp_links(m)
    objective_roadbase_links = get_objective_roadbase_links(m)
    objective_airbase_links = get_objective_airbase_links(m)
    objective_qrf_links = get_objective_qrf_links(m)
    objective_reinforcement_links = get_objective_reinforcement_links(m)
    assign_task_zones_to_objectives(objective_zones, task_zones, objective_task_links)
    assign_farp_zones_to_objectives(objective_zones, farp_zones, objective_farp_links)
    assign_roadbase_zones_to_objectives(objective_zones, roadbase_zones, objective_roadbase_links)
    assign_airbase_zones_to_objectives(objective_zones, airbase_zones, objective_airbase_links)
    assign_qrf_zones_to_objectives(objective_zones, qrf_zones, objective_qrf_links)
    assign_reinforcement_zones_to_objectives(objective_zones, reinforcement_zones, objective_reinforcement_links)
    assign_groups_to_zones(objective_zones, task_zones, qrf_zones, farp_zones, roadbase_zones, airbase_zones, reinforcement_zones, vehicle_groups, ship_groups, static_groups)
    merged = assign_objective_zones_to_strands(objective_zones, strands)
    unclassified_zones = get_unclassified_zones(m)

    debug_aircraft_farp(m, farp_zones)
    debug_aircraft_roadbase(m, roadbase_zones)
    debug_aircraft_airbase(m, airbase_zones)
    report_units_in_obj(m, objective_zones)

    obj_filter = ["OBJ-6"]

    with open("temp/temp-objectives.json", "w") as outfile:
        json.dump(merged, outfile, sort_keys=True)

    with open("temp/temp-vehicle-groups.json", "w") as outfile:
        json.dump(vehicle_groups, outfile, sort_keys=True)

    with open("temp/temp-ship-groups.json", "w") as outfile:
        json.dump(ship_groups, outfile, sort_keys=True)

    with open("temp/temp-tasks.json", "w") as outfile:
        json.dump(task_zones, outfile, sort_keys=True)

    with open("temp/temp-qrf.json", "w") as outfile:
        json.dump(qrf_zones, outfile, sort_keys=True)

    with open("temp/temp-reinforcement.json", "w") as outfile:
        json.dump(reinforcement_zones, outfile, sort_keys=True)

    with open("temp/temp-statics.json", "w") as outfile:
        json.dump(static_groups, outfile, sort_keys=True)

    with open("temp/temp-airbases.json", "w") as outfile:
        json.dump(airbase_zones, outfile, sort_keys=True)

    with open("temp/temp-unclassified.json", "w") as outfile:
        json.dump(unclassified_zones, outfile, sort_keys=True)

    with open("temp/temp-farps.json", "w") as outfile:
        json.dump(farp_zones, outfile, sort_keys=True)

    with open("temp/temp-roadbases.json", "w") as outfile:
        json.dump(roadbase_zones, outfile, sort_keys=True)

from missions.CyprusInvasion.mission import CyprusInvasion
from missions.DangerZone.mission import DangerZone
from missions.GeorgianOffensive.mission import GeorgianOffensive
from missions.AndeanAbyss.mission import AndeanAbyss
from missions.RockTheCasbah.mission import RockTheCasbah
from missions.AcesHigh.mission import AcesHigh

parser = argparse.ArgumentParser()
parser.add_argument("--mission", action="store", dest="mission", required=True)
args = parser.parse_args()

m = None

match args.mission:
    case "CyprusInvasion":
        m = CyprusInvasion()
    case "DangerZone":
        m = DangerZone()
    case "GeorgianOffensive":
        m = GeorgianOffensive()
    case "AndeanAbyss":
        m = AndeanAbyss()
    case "RockTheCasbah":
        m = RockTheCasbah()
    case "AcesHigh":
        m = AcesHigh()

dumpit(m.miz_export_path)