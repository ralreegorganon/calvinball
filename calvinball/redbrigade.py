import dcs

class RedBrigades:
    def define(self, m: dcs.mission):
        return {}

    def build(self, m: dcs.Mission):
        red_brigades = self.define(m)

        country = m.country(dcs.countries.CombinedJointTaskForcesRed.name)
        p = dcs.mapping.Point(m.terrain.bullseye_blue["x"], m.terrain.bullseye_blue["y"], m.terrain)
        for brigade_name, brigade in red_brigades.items():
            for platoon_name, platoon in brigade["platoons"].items():
                platoon["groupName"] = f"RED {brigade_name} {platoon_name}"
                m.vehicle_group_platoon(country, platoon["groupName"], platoon["units"], p, formation=dcs.unitgroup.VehicleGroup.Formation.Scattered).late_activation = True

        return red_brigades