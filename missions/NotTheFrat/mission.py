import dcs
import calvinball

class NotTheFrat(calvinball.mission.Mission):
    def __init__(self) -> None:
        t = dcs.terrain.Caucasus()
        miz_name = "NotTheFrat"
        ctld = NotTheFratCtld()
        clients = NotTheFratClients()
        red_airwings = NotTheFratRedAirwings()
        blue_airwings = NotTheFratBlueAirwings()

        super().__init__(t, miz_name, ctld, clients, red_airwings, blue_airwings)

class NotTheFratCtld(calvinball.ctld.Ctld):
    def build(self, m: dcs.Mission):
        super().build(m)

class NotTheFratClients(calvinball.clients.Clients):
    def define(self, m: dcs.Mission, edit: bool):
        m.groundControl.blue_game_masters = 1
        m.groundControl.blue_tactical_commander = 1
        m.groundControl.blue_jtac = 2
        m.groundControl.red_game_masters = 1

        m.coalition["blue"].set_bullseye({"x": -32691, "y": -270357})

        airport_set = [
            {
                "country": m.country(dcs.countries.CombinedJointTaskForcesBlue.name),
                "airport": m.terrain.airports["Batumi"],
                "start_type": dcs.mission.StartType.Cold,
                "airframes": [
                    { "airframe": dcs.planes.F_16C_50, "count": 4, "parking": [6, 8, 9, 10], "fuel": 1, "loadout": "Empty", "livery": "18th AGRS Arctic Splinter" }
                ]
            }
        ]

        return airport_set

class NotTheFratRedAirwings(calvinball.redairwing.RedAirwings):
    def define(self, m: dcs.Mission):
        red_airwings = {
            "1st Goon Wing - Kobuleti": {
                "airbase": "Kobuleti",
                "warehouse": "Kobuleti Airwing Warehouse#00001",
                "squadrons": {
                    "1GW-Kobuleti-1": {
                        "airframe": dcs.planes.JF_17,
                        "groupSize": 2,
                        "initialInventory": 2,
                        "livery": "PLAAF 125th AB (Fictional)",
                        "loadouts": {
                            "PL-5Ex2, 2*SD-10x2, 800L Tank": "{ AUFTRAG.Type.CAP, AUFTRAG.Type.INTERCEPT }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.CAP": 50,
                            "AUFTRAG.Type.INTERCEPT": 50
                        }
                    },
                    "1GW-Kobuleti-1": {
                        "airframe": dcs.planes.A_50,
                        "groupSize": 1,
                        "initialInventory": 1,
                        "livery": "RF Air Force new",
                        "loadouts": {
                            "Empty": "{ AUFTRAG.Type.AWACS }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.AWACS": 50
                        }
                    }
                }
            },
        }
        return red_airwings

class NotTheFratBlueAirwings(calvinball.blueairwing.BlueAirwings):
    def define(self, m: dcs.Mission):
        blue_airwings = {
            "1st - Batumi": {
                "airbase": "Batumi",
                "warehouse": "Batumi Airwing Warehouse#00001",
                "squadrons": {
                    "GGD-01": {
                        "airframe": dcs.planes.E_2C,
                        "groupSize": 1,
                        "initialInventory": 1,
                        "livery": "VAW-125 Tigertails",
                        "loadouts": {
                            "Empty": "{ AUFTRAG.Type.AWACS }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.AWACS": 50
                        }
                    }
                }
            }
        }
        return blue_airwings