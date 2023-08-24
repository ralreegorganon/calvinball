import dcs

class BlueBrigades:
    def define(self, m: dcs.mission):
        return {}

    def build(self, m: dcs.Mission):
        blue_brigades = self.define(m)

        country = m.country(dcs.countries.CombinedJointTaskForcesBlue.name)
        p = dcs.mapping.Point(m.terrain.bullseye_blue["x"], m.terrain.bullseye_blue["y"], m.terrain)
        for brigade_name, brigade in blue_brigades.items():
            for platoon_name, platoon in brigade["platoons"].items():
                platoon["groupName"] = f"BLUE {brigade_name} {platoon_name}"
                m.vehicle_group_platoon(country, platoon["groupName"], platoon["units"], p, formation=dcs.unitgroup.VehicleGroup.Formation.Scattered).late_activation = True

        return blue_brigades