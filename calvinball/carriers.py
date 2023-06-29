import dcs

class Carriers:
    def define(self, m: dcs.mission):
        return {}

    def build(self, m: dcs.Mission, edit: bool):
        blue_carriers = self.define(m)

        country = m.country(dcs.countries.CombinedJointTaskForcesBlue.name)
        for carrier_name, carrier in blue_carriers.items():
            sg = m.ship_group(country, carrier_name, carrier["ship"], dcs.mapping.Point(carrier["position"]["x"], carrier["position"]["y"], m.terrain), heading=90)
            if edit:
                if "waypoints" in carrier:
                    for wp in carrier["waypoints"]:
                        sg.add_waypoint(dcs.mapping.Point(wp["x"], wp["y"], m.terrain), speed=wp["speed"])

        return blue_carriers