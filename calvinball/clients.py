import dcs
import pydcs_extensions

class Clients:
    def __park(self, slots, airport):
        if slots == None:
            return None
        return [airport.parking_slot(s) for s in slots]

    def define(self, m: dcs.mission, edit: bool):
        return []

    def __doittoit(self, m: dcs.Mission, edit: bool, fg: dcs.unitgroup.FlyingGroup, group_name, a, ctld_groups, csar_groups):
        fg.set_client()

        if "loadout" in a:
            if a["loadout"] == "Empty":
                fg.reset_loadout()
            else:
                fg.load_loadout(a["loadout"])

        setFreq = False

        if "radio_override" in a:
            fg.set_frequency(a["radio_override"]["frequency"], a["radio_override"]["radio"])
            setFreq = True

        for u in fg.units:
            u.fuel = a.get("fuel", 1) * a["airframe"].fuel_max
            if "livery" in a:
                u.livery_id = a["livery"]

            if "racks" in a:
                u.hardpoint_racks = a["racks"]

            if "radios" in a:
                for radio, channels in a["radios"].items():
                    for channel, frequency in channels.items():
                        if not setFreq:
                            fg.set_frequency(frequency, radio)
                            setFreq = True
                        if channel <= u.num_radio_channels(radio):
                            u.set_radio_channel_preset(radio, channel, frequency)

            if "properties" in a:
                for key, value in a["properties"].items():
                        u.set_property(key, value)

        if a["airframe"].helicopter:
            ctld_groups.append(group_name)

        if a["airframe"].helicopter or a["airframe"] == pydcs_extensions.Bronco_OV_10A:
            csar_groups.append(group_name)

        if "waypoints" in a:
            for w in a["waypoints"]:
                fg.add_waypoint(dcs.mapping.Point(w["x"], w["y"], m.terrain), 0)


    def build(self, m: dcs.Mission, edit: bool):
        airport_set = self.define(m, edit)

        ctld_groups = []
        csar_groups = []
        farp_groups = {}
        roadbase_groups = {}
        airbase_groups = {}
        carrier_groups = {}

        for p in airport_set:
            for a in p["airframes"]:
                start_type = a.get("start_type", p["start_type"])

                if "airport" in p:
                    airport_name = p["airport"].name

                    if airport_name not in airbase_groups:
                        airbase_groups[airport_name] = []

                    airframe_name = a["airframe"].id
                    parking = self.__park(a["parking"], p["airport"])
                    for i in range(a["count"]):
                        group_name = f"{airport_name} {airframe_name} {start_type.name} {str(i+1)}"
                        airbase_groups[airport_name].append(group_name)
                        fg = m.flight_group_from_airport(
                            p["country"], group_name, a["airframe"], p["airport"], group_size=1, start_type=start_type, parking_slots=parking
                        )

                        self.__doittoit(m, edit, fg, group_name, a, ctld_groups, csar_groups)

                if "farp" in p:
                    if p["farp_zone"] not in farp_groups:
                        farp_groups[p["farp_zone"]] = []

                    airport_name = p["farp"]
                    airframe_name = a["airframe"].id
                    for i, pos in enumerate(a["positions"]):
                        group_name = f"{airport_name} {airframe_name} {start_type.name} {str(i+1)}"
                        farp_groups[p["farp_zone"]].append(group_name)

                        fg = m.flight_group(p["country"], group_name, a["airframe"], None,  position=dcs.mapping.Point(pos["x"], pos["y"], m.terrain),  group_size=1, start_type=start_type)

                        if start_type == dcs.mission.StartType.Warm:
                            fg.points[0].type = "TakeOffGroundHot"
                            fg.points[0].action = dcs.point.PointAction.FromGroundAreaHot
                        else:
                            fg.points[0].type = "TakeOffGround"
                            fg.points[0].action = dcs.point.PointAction.FromGroundArea
                        fg.units[0].heading = pos["heading"]

                        self.__doittoit(m, edit, fg, group_name, a, ctld_groups, csar_groups)

                if "roadbase" in p:
                    if p["roadbase_zone"] not in roadbase_groups:
                        roadbase_groups[p["roadbase_zone"]] = []

                    airport_name = p["roadbase"]
                    airframe_name = a["airframe"].id
                    for i, pos in enumerate(a["positions"]):
                        group_name = f"{airport_name} {airframe_name} {start_type.name} {str(i+1)}"
                        roadbase_groups[p["roadbase_zone"]].append(group_name)

                        fg = m.flight_group(p["country"], group_name, a["airframe"], None,  position=dcs.mapping.Point(pos["x"], pos["y"], m.terrain),  group_size=1, start_type=start_type)

                        if start_type == dcs.mission.StartType.Warm:
                            fg.points[0].type = "TakeOffGroundHot"
                            fg.points[0].action = dcs.point.PointAction.FromGroundAreaHot
                        else:
                            fg.points[0].type = "TakeOffGround"
                            fg.points[0].action = dcs.point.PointAction.FromGroundArea
                        fg.units[0].heading = pos["heading"]

                        self.__doittoit(m, edit, fg, group_name, a, ctld_groups, csar_groups)


                if "carrier" in p:
                    if p["carrier"] not in carrier_groups:
                        carrier_groups[p["carrier"]] = []

                    airport_name = p["carrier"]

                    sg = p["country"].find_ship_group(airport_name)

                    airframe_name = a["airframe"].id
                    for i in range(a["count"]):
                        group_name = f"{airport_name} {airframe_name} {start_type.name} {str(i+1)}"
                        carrier_groups[airport_name].append(group_name)
                        fg = m.flight_group_from_unit(
                            p["country"], group_name, a["airframe"], sg, group_size=1, start_type=start_type
                        )

                        self.__doittoit(m, edit, fg, group_name, a, ctld_groups, csar_groups) 

        return ctld_groups, csar_groups, farp_groups, roadbase_groups, airbase_groups, carrier_groups





