import dcs

class RedAirwings:
    def define(self, m: dcs.mission):
        return {}

    def build(self, m: dcs.Mission):
        red_airwings = self.define(m)

        country = m.country(dcs.countries.CombinedJointTaskForcesRed.name)
        p = dcs.mapping.Point(m.coalition["blue"].bullseye["x"], m.coalition["blue"].bullseye["y"], m.terrain)
        for airwing_name, airwing in red_airwings.items():
            if "airbase" in airwing:
                if airwing["airbase"] in m.terrain.airports:
                    m.terrain.airports[airwing["airbase"]].set_red()
            for squadron_name, squadron in airwing["squadrons"].items():
                airframe = squadron["airframe"]
                squadron["groupName"] = f"RED {airwing_name} {squadron_name} {airframe.id}"
                m.flight_group_inflight(country, squadron["groupName"], airframe, p, 42000, group_size=squadron["groupSize"]).late_activation = True
                squadron["loadoutGroups"] = {}
                for i, (loadout, capability) in enumerate(squadron["loadouts"].items()):
                    loadout_group_name = f"RED {airwing_name} {squadron_name} {airframe.id} LOADOUT {i}"
                    fg = m.flight_group_inflight(country, loadout_group_name, airframe, p, 42000)
                    fg.late_activation = True
                    if "loadoutFuncs" in squadron and loadout in squadron["loadoutFuncs"]:
                        squadron["loadoutFuncs"][loadout](fg)
                    else:
                        fg.load_loadout(loadout)
                    squadron["loadoutGroups"][loadout_group_name] = capability

        return red_airwings