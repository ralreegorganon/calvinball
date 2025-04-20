import dcs
import pydcs_extensions
import calvinball

class BalloonFight(calvinball.mission.Mission):
    def __init__(self) -> None:
        t = dcs.terrain.GermanyColdWar()
        miz_name = "BalloonFight"
        ctld = BalloonFightCtld()
        clients = BalloonFightClients()
        red_airwings = BalloonFightRedAirwings()
        blue_airwings = BalloonFightBlueAirwings()
        carriers = BalloonFightCarriers()
        qrf = BalloonFightQrf()
        reinforcement = BalloonFightReinforcement()
        red_brigades = BalloonFightRedBrigades()
        blue_brigades = BalloonFightBlueBrigades()

        super().__init__(t, miz_name, ctld, clients, red_airwings, blue_airwings, carriers, qrf, reinforcement, red_brigades, blue_brigades)

        self.m.coalition["blue"].set_bullseye({"x": -147009 , "y": -396554})
        self.m.coalition["red"].set_bullseye({"x": -147009 , "y": -396554})

class BalloonFightCtld(calvinball.ctld.Ctld):
    def __init__(self) -> None:
        super().__init__()

    def build(self, m: dcs.Mission):
        super().build(m)

class BalloonFightQrf(calvinball.qrf.Qrf):
    def __init__(self) -> None:
        super().__init__()

    def build(self, m: dcs.Mission):
        super().build(m)

        p = dcs.mapping.Point(m.coalition["blue"].bullseye["x"], m.coalition["blue"].bullseye["y"], m.terrain)

class BalloonFightReinforcement(calvinball.reinforcement.Reinforcement):
    def __init__(self) -> None:
        super().__init__()

    def build(self, m: dcs.Mission):
        super().build(m)

        p = dcs.mapping.Point(m.coalition["blue"].bullseye["x"], m.coalition["blue"].bullseye["y"], m.terrain)

class BalloonFightCarriers(calvinball.carriers.Carriers):
        def __init__(self) -> None:
            super().__init__()

class BalloonFightClients(calvinball.clients.Clients):
    def __init__(self) -> None:
        super().__init__()

    def define(self, m: dcs.Mission, edit: bool):
        m.groundControl.blue_game_masters = 1
        m.groundControl.blue_tactical_commander = 1
        m.groundControl.blue_jtac = 2
        m.groundControl.red_game_masters = 1

        airport_set = [
            {
                "country": m.country(dcs.countries.CombinedJointTaskForcesBlue.name),
                "airport": m.terrain.airports["Ramstein"],
                "start_type": dcs.mission.StartType.Warm,
                "airframes": [
                    { "airframe": dcs.planes.A_10C_2, "count": 4, "parking": [57, 58, 59, 60], "fuel": 0.6, "loadout": "Empty", "livery": "355th fs eielson afb, alaska (ak)" },
                ]
            }
        ]

        comms_plan = {
            "uhf": { 1: 250, 2: 251, 3: 252, 4: 253, 5: 254 },
            "vhf_am": { 1: 135, 2: 136, 3: 137, 4: 138, 5: 139 },
            "vhf_fm": { 1: 31, 2: 32, 3: 33, 4: 34, 5: 35 }
        }

        radio_override = {
            dcs.helicopters.Ka_50_3: { "radio": 2, "frequency": 250 },
            dcs.helicopters.SA342L: { "radio": 1, "frequency": 135 },
            dcs.helicopters.SA342M: { "radio": 1, "frequency": 135 },
            dcs.helicopters.SA342M: { "radio": 1, "frequency": 135 },
        }

        radios = {
            dcs.helicopters.AH_64D_BLK_II: ["vhf_am", "uhf", "vhf_fm", "vhf_fm"],
            dcs.helicopters.Ka_50_3: ["vhf_fm"],
            dcs.helicopters.Mi_24P: ["uhf", "vhf_fm"],
            dcs.helicopters.Mi_8MT: ["uhf", "vhf_fm"],
            dcs.helicopters.SA342L: ["vhf_fm"],
            dcs.helicopters.SA342M: ["vhf_fm"],
            dcs.helicopters.UH_1H: ["uhf"],
            dcs.helicopters.OH58D: ["uhf", "vhf_am", "vhf_fm", "vhf_fm"],
            dcs.planes.A_10A: ["vhf_am"],
            dcs.planes.A_10C_2: ["vhf_am", "uhf", "vhf_fm"],
            dcs.planes.AJS37: ["uhf"],
            dcs.planes.AV8BNA: ["vhf_am", "uhf", "vhf_fm"],
            dcs.planes.C_101CC: ["uhf"],
            dcs.planes.F_5E_3: ["uhf"],
            dcs.planes.F_86F_Sabre: ["uhf"],
            dcs.planes.L_39ZA: ["uhf"],
            dcs.planes.M_2000C: ["uhf", "vhf_am"],
            dcs.planes.MB_339A: ["uhf"],
            dcs.planes.MiG_19P: ["vhf_am"],
            dcs.planes.MiG_21Bis: ["uhf"],
            dcs.planes.MiG_29S: ["uhf"],
            dcs.planes.Mirage_F1EE: ["vhf_am", "uhf"],
            dcs.planes.Mirage_F1BE: ["vhf_am", "uhf"],
            dcs.planes.P_51D_30_NA: ["vhf_am"],
            dcs.planes.Su_25: ["vhf_am"],
            dcs.planes.Su_25T: ["vhf_am"],
            dcs.planes.F_14B: ["uhf", "vhf_am"],
            dcs.planes.FA_18C_hornet: ["vhf_am", "uhf"],
            dcs.planes.F_15ESE: ["uhf", "vhf_am"],
            dcs.planes.F_16C_50: ["uhf", "vhf_am"],
            dcs.planes.JF_17: ["uhf"],
            dcs.planes.F_15C: ["uhf"],
            dcs.planes.F_4E_45MC: ["uhf"],
        }

        if not edit:
            # airport_set[0]["airframes"].append({ "airframe": pydcs_extensions.A_4E_C, "count": 7, "parking": [244, 243, 242, 241, 240, 239, 238], "fuel": 0.75, "loadout": "Empty", "livery": "Aggressor USN VF-126 Bandits" })
            # airport_set[0]["airframes"].append({ "airframe": pydcs_extensions.Bronco_OV_10A, "count": 4, "parking": [253, 106, 105, 102], "fuel": 1, "loadout": "Empty", "livery": "colombian 2221" })
            # airport_set[0]["airframes"].append({ "airframe": pydcs_extensions.Hercules, "count": 2, "parking": [100, 104], "fuel": 0.6, "loadout": "Empty" })

            radios[pydcs_extensions.A_4E_C] = ["uhf"]
            radios[pydcs_extensions.Bronco_OV_10A] = ["vhf_fm"]
            radios[pydcs_extensions.Hercules] = ["uhf"]

            radio_override[pydcs_extensions.Bronco_OV_10A] = { "radio": 1, "frequency": 135 }

        for airport in airport_set:
            for airframe in airport["airframes"]:
                airframe["radios"] = {}
                if airframe["airframe"] in radio_override:
                    airframe["radio_override"] = radio_override[airframe["airframe"]]
                for i, template in enumerate(radios[airframe["airframe"]]):
                    airframe["radios"][i+1] = comms_plan[template]

        return airport_set

class BalloonFightRedAirwings(calvinball.redairwing.RedAirwings):
    def __init__(self) -> None:
        super().__init__()

    def define(self, m: dcs.Mission):
        red_airwings = {
            "Pferdsfeld": {
                "airbase": "Pferdsfeld",
                "warehouse": "Pferdsfeld Airwing Warehouse#00001",
                "squadrons": {
                    "Pferdsfeld AW 1": {
                        "airframe": dcs.planes.JF_17,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "PLAAF 125th AB (Fictional)",
                        "loadouts": {
                            "PL-5Ex2, 2*SD-10x2, 800L Tank": "{ AUFTRAG.Type.CAP, AUFTRAG.Type.INTERCEPT, AUFTRAG.Type.ESCORT }",
                            "PL-5Ex2, 2*MK-82x2, MK-83x2, MK-84": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.BOMBCARPET, AUFTRAG.Type.CASENHANCED }",
                            "PL-5Ex2, 2*LD-10x2, GB-6-HEx2, SPJ": "{ AUFTRAG.Type.SEAD }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.CAP": 50,
                            "AUFTRAG.Type.INTERCEPT": 50,
                            "AUFTRAG.Type.ESCORT": 50,
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.BOMBCARPET": 50,
                            "AUFTRAG.Type.SEAD": 50,
                            "AUFTRAG.Type.CASENHANCED": 50
                        }
                    },
                    "Pferdsfeld AW 2": {
                        "airframe": dcs.helicopters.UH_60A,
                        "groupSize": 1,
                        "initialInventory": 99,
                        "takeoffCold": "true",
                        "livery": "Russia_VVS_Grey",
                        "loadouts": {
                            "Empty": "{ AUFTRAG.Type.OPSTRANSPORT }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.OPSTRANSPORT": 50
                        }
                    },
                }
            },
            "Hahn": {
                "airbase": "Hahn",
                "warehouse": "Hahn Airwing Warehouse#00001",
                "squadrons": {
                    "Hahn AW 1": {
                        "airframe": dcs.planes.JF_17,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "PLAAF 125th AB (Fictional)",
                        "loadouts": {
                            "PL-5Ex2, 2*SD-10x2, 800L Tank": "{ AUFTRAG.Type.CAP, AUFTRAG.Type.INTERCEPT, AUFTRAG.Type.ESCORT }",
                            "PL-5Ex2, 2*MK-82x2, MK-83x2, MK-84": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.BOMBCARPET, AUFTRAG.Type.CASENHANCED }",
                            "PL-5Ex2, 2*LD-10x2, GB-6-HEx2, SPJ": "{ AUFTRAG.Type.SEAD }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.CAP": 50,
                            "AUFTRAG.Type.INTERCEPT": 50,
                            "AUFTRAG.Type.ESCORT": 50,
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.BOMBCARPET": 50,
                            "AUFTRAG.Type.SEAD": 50,
                            "AUFTRAG.Type.CASENHANCED": 50
                        }
                    },
                    "Hahn AW 2": {
                        "airframe": dcs.helicopters.UH_60A,
                        "groupSize": 1,
                        "initialInventory": 99,
                        "takeoffCold": "true",
                        "livery": "Russia_VVS_Grey",
                        "loadouts": {
                            "Empty": "{ AUFTRAG.Type.OPSTRANSPORT }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.OPSTRANSPORT": 50
                        }
                    },
                }
            },
            "Buchel": {
                "airbase": "Buchel",
                "warehouse": "Buchel Airwing Warehouse#00001",
                "squadrons": {
                    "Buchel AW 1": {
                        "airframe": dcs.planes.JF_17,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "PLAAF 125th AB (Fictional)",
                        "loadouts": {
                            "PL-5Ex2, 2*SD-10x2, 800L Tank": "{ AUFTRAG.Type.CAP, AUFTRAG.Type.INTERCEPT, AUFTRAG.Type.ESCORT }",
                            "PL-5Ex2, 2*MK-82x2, MK-83x2, MK-84": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.BOMBCARPET, AUFTRAG.Type.CASENHANCED }",
                            "PL-5Ex2, 2*LD-10x2, GB-6-HEx2, SPJ": "{ AUFTRAG.Type.SEAD }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.CAP": 50,
                            "AUFTRAG.Type.INTERCEPT": 50,
                            "AUFTRAG.Type.ESCORT": 50,
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.BOMBCARPET": 50,
                            "AUFTRAG.Type.SEAD": 50,
                            "AUFTRAG.Type.CASENHANCED": 50
                        }
                    },
                    "Buchel AW 2": {
                        "airframe": dcs.helicopters.UH_60A,
                        "groupSize": 1,
                        "initialInventory": 99,
                        "takeoffCold": "true",
                        "livery": "Russia_VVS_Grey",
                        "loadouts": {
                            "Empty": "{ AUFTRAG.Type.OPSTRANSPORT }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.OPSTRANSPORT": 50
                        }
                    },
                }
            },
            "Spangdahlem": {
                "airbase": "Spangdahlem",
                "warehouse": "Spangdahlem Airwing Warehouse#00001",
                "squadrons": {
                    "Spangdahlem AW 1": {
                        "airframe": dcs.planes.JF_17,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "PLAAF 125th AB (Fictional)",
                        "loadouts": {
                            "PL-5Ex2, 2*SD-10x2, 800L Tank": "{ AUFTRAG.Type.CAP, AUFTRAG.Type.INTERCEPT, AUFTRAG.Type.ESCORT }",
                            "PL-5Ex2, 2*MK-82x2, MK-83x2, MK-84": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.BOMBCARPET, AUFTRAG.Type.CASENHANCED }",
                            "PL-5Ex2, 2*LD-10x2, GB-6-HEx2, SPJ": "{ AUFTRAG.Type.SEAD }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.CAP": 50,
                            "AUFTRAG.Type.INTERCEPT": 50,
                            "AUFTRAG.Type.ESCORT": 50,
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.BOMBCARPET": 50,
                            "AUFTRAG.Type.SEAD": 50,
                            "AUFTRAG.Type.CASENHANCED": 50
                        }
                    },
                     "Shangdahlem AW 2": {
                        "airframe": dcs.helicopters.UH_60A,
                        "groupSize": 1,
                        "initialInventory": 99,
                        "takeoffCold": "true",
                        "livery": "Russia_VVS_Grey",
                        "loadouts": {
                            "Empty": "{ AUFTRAG.Type.OPSTRANSPORT }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.OPSTRANSPORT": 50
                        }
                    },
                }
            },
            "Bitburg": {
                "airbase": "Bitburg",
                "warehouse": "Bitburg Airwing Warehouse#00001",
                "squadrons": {
                    "Bitburg AW 1": {
                        "airframe": dcs.planes.JF_17,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "PLAAF 125th AB (Fictional)",
                        "loadouts": {
                            "PL-5Ex2, 2*SD-10x2, 800L Tank": "{ AUFTRAG.Type.CAP, AUFTRAG.Type.INTERCEPT, AUFTRAG.Type.ESCORT }",
                            "PL-5Ex2, 2*MK-82x2, MK-83x2, MK-84": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.BOMBCARPET, AUFTRAG.Type.CASENHANCED }",
                            "PL-5Ex2, 2*LD-10x2, GB-6-HEx2, SPJ": "{ AUFTRAG.Type.SEAD }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.CAP": 50,
                            "AUFTRAG.Type.INTERCEPT": 50,
                            "AUFTRAG.Type.ESCORT": 50,
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.BOMBCARPET": 50,
                            "AUFTRAG.Type.SEAD": 50,
                            "AUFTRAG.Type.CASENHANCED": 50
                        }
                    },
                    "Bitburg AW 2": {
                        "airframe": dcs.helicopters.UH_60A,
                        "groupSize": 1,
                        "initialInventory": 99,
                        "takeoffCold": "true",
                        "livery": "Russia_VVS_Grey",
                        "loadouts": {
                            "Empty": "{ AUFTRAG.Type.OPSTRANSPORT }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.OPSTRANSPORT": 50
                        }
                    },
                }
            },
            "Pottschutthohe": {
                "airbase": "Pottschutthohe",
                "warehouse": "Pottschutthohe Airwing Warehouse#00001",
                "squadrons": {
                    "Pottschutthohe AW 1": {
                        "airframe": dcs.planes.JF_17,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "PLAAF 125th AB (Fictional)",
                        "loadouts": {
                            "PL-5Ex2, 2*SD-10x2, 800L Tank": "{ AUFTRAG.Type.CAP, AUFTRAG.Type.INTERCEPT, AUFTRAG.Type.ESCORT }",
                            "PL-5Ex2, 2*MK-82x2, MK-83x2, MK-84": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.BOMBCARPET, AUFTRAG.Type.CASENHANCED }",
                            "PL-5Ex2, 2*LD-10x2, GB-6-HEx2, SPJ": "{ AUFTRAG.Type.SEAD }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.CAP": 50,
                            "AUFTRAG.Type.INTERCEPT": 50,
                            "AUFTRAG.Type.ESCORT": 50,
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.BOMBCARPET": 50,
                            "AUFTRAG.Type.SEAD": 50,
                            "AUFTRAG.Type.CASENHANCED": 50
                        }
                    },
                    "Pottschutthohe AW 2": {
                        "airframe": dcs.helicopters.UH_60A,
                        "groupSize": 1,
                        "initialInventory": 99,
                        "takeoffCold": "true",
                        "livery": "Russia_VVS_Grey",
                        "loadouts": {
                            "Empty": "{ AUFTRAG.Type.OPSTRANSPORT }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.OPSTRANSPORT": 50
                        }
                    },
                }
            },
            "Zweibrucken": {
                "airbase": "Zweibrucken",
                "warehouse": "Zweibrucken Airwing Warehouse#00001",
                "squadrons": {
                    "Zweibrucken AW 1": {
                        "airframe": dcs.planes.JF_17,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "PLAAF 125th AB (Fictional)",
                        "loadouts": {
                            "PL-5Ex2, 2*SD-10x2, 800L Tank": "{ AUFTRAG.Type.CAP, AUFTRAG.Type.INTERCEPT, AUFTRAG.Type.ESCORT }",
                            "PL-5Ex2, 2*MK-82x2, MK-83x2, MK-84": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.BOMBCARPET, AUFTRAG.Type.CASENHANCED }",
                            "PL-5Ex2, 2*LD-10x2, GB-6-HEx2, SPJ": "{ AUFTRAG.Type.SEAD }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.CAP": 50,
                            "AUFTRAG.Type.INTERCEPT": 50,
                            "AUFTRAG.Type.ESCORT": 50,
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.BOMBCARPET": 50,
                            "AUFTRAG.Type.SEAD": 50,
                            "AUFTRAG.Type.CASENHANCED": 50
                        }
                    },
                    "Zweibrucken AW 2": {
                        "airframe": dcs.helicopters.UH_60A,
                        "groupSize": 1,
                        "initialInventory": 99,
                        "takeoffCold": "true",
                        "livery": "Russia_VVS_Grey",
                        "loadouts": {
                            "Empty": "{ AUFTRAG.Type.OPSTRANSPORT }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.OPSTRANSPORT": 50
                        }
                    },
                }
            },
        }
        return red_airwings

class BalloonFightBlueAirwings(calvinball.blueairwing.BlueAirwings):
    def __init__(self) -> None:
        super().__init__()

    def define(self, m: dcs.Mission):
        blue_airwings = {
        }
        return blue_airwings

class BalloonFightRedBrigades(calvinball.redbrigade.RedBrigades):
    def __init__(self) -> None:
        super().__init__()

    def define(self, m: dcs.Mission):
        red_brigades = {
            "Pferdsfeld": {
                "warehouse": "Pferdsfeld Brigade Warehouse#00001",
                "platoons": {
                    "Pferdsfeld B 1": {
                        "units": [
                            dcs.vehicles.Infantry.Paratrooper_AKS_74,
                            dcs.vehicles.Infantry.Paratrooper_AKS_74,
                            dcs.vehicles.Infantry.Paratrooper_RPG_16,
                            dcs.vehicles.Infantry.Paratrooper_RPG_16,
                        ],
                        "initialInventory": 3,
                        "capabilities": {
                            "AUFTRAG.Type.ONGUARD": 50
                        }
                    },
                    "Pferdsfeld B 2": {
                        "units": [
                            dcs.vehicles.Artillery.Uragan_BM_27,
                            dcs.vehicles.Artillery.Uragan_BM_27,
                            dcs.vehicles.Artillery.Uragan_BM_27,
                            dcs.vehicles.Artillery.Uragan_BM_27,
                            dcs.vehicles.Artillery.Uragan_BM_27,
                            dcs.vehicles.Unarmed.Ural_375,
                            dcs.vehicles.Unarmed.Ural_375
                        ],
                        "initialInventory": 1,
                        "capabilities": {
                            "AUFTRAG.Type.ARTY": 50
                        }
                    }
                }
            },
            "Hahn": {
                "warehouse": "Hahn Brigade Warehouse#00001",
                "platoons": {
                    "Hahn B 1": {
                        "units": [
                            dcs.vehicles.Infantry.Paratrooper_AKS_74,
                            dcs.vehicles.Infantry.Paratrooper_AKS_74,
                            dcs.vehicles.Infantry.Paratrooper_RPG_16,
                            dcs.vehicles.Infantry.Paratrooper_RPG_16,
                        ],
                        "initialInventory": 3,
                        "capabilities": {
                            "AUFTRAG.Type.ONGUARD": 50
                        }
                    },
                    "Hahn B 2": {
                        "units": [
                            dcs.vehicles.Artillery.Uragan_BM_27,
                            dcs.vehicles.Artillery.Uragan_BM_27,
                            dcs.vehicles.Artillery.Uragan_BM_27,
                            dcs.vehicles.Artillery.Uragan_BM_27,
                            dcs.vehicles.Artillery.Uragan_BM_27,
                            dcs.vehicles.Unarmed.Ural_375,
                            dcs.vehicles.Unarmed.Ural_375
                        ],
                        "initialInventory": 1,
                        "capabilities": {
                            "AUFTRAG.Type.ARTY": 50
                        }
                    }
                }
            },
            "Buchel": {
                "warehouse": "Buchel Brigade Warehouse#00001",
                "platoons": {
                    "Buchel B 1": {
                        "units": [
                            dcs.vehicles.Infantry.Paratrooper_AKS_74,
                            dcs.vehicles.Infantry.Paratrooper_AKS_74,
                            dcs.vehicles.Infantry.Paratrooper_RPG_16,
                            dcs.vehicles.Infantry.Paratrooper_RPG_16,
                        ],
                        "initialInventory": 3,
                        "capabilities": {
                            "AUFTRAG.Type.ONGUARD": 50
                        }
                    },
                    "Buchel B 2": {
                        "units": [
                            dcs.vehicles.Artillery.Uragan_BM_27,
                            dcs.vehicles.Artillery.Uragan_BM_27,
                            dcs.vehicles.Artillery.Uragan_BM_27,
                            dcs.vehicles.Artillery.Uragan_BM_27,
                            dcs.vehicles.Artillery.Uragan_BM_27,
                            dcs.vehicles.Unarmed.Ural_375,
                            dcs.vehicles.Unarmed.Ural_375
                        ],
                        "initialInventory": 1,
                        "capabilities": {
                            "AUFTRAG.Type.ARTY": 50
                        }
                    }
                }
            },
            "Spangdahlem": {
                "warehouse": "Spangdahlem Brigade Warehouse#00001",
                "platoons": {
                    "Spangdahlem B 1": {
                        "units": [
                            dcs.vehicles.Infantry.Paratrooper_AKS_74,
                            dcs.vehicles.Infantry.Paratrooper_AKS_74,
                            dcs.vehicles.Infantry.Paratrooper_RPG_16,
                            dcs.vehicles.Infantry.Paratrooper_RPG_16,
                        ],
                        "initialInventory": 3,
                        "capabilities": {
                            "AUFTRAG.Type.ONGUARD": 50
                        }
                    },
                    "Spangdahlem B 2": {
                        "units": [
                            dcs.vehicles.Artillery.Uragan_BM_27,
                            dcs.vehicles.Artillery.Uragan_BM_27,
                            dcs.vehicles.Artillery.Uragan_BM_27,
                            dcs.vehicles.Artillery.Uragan_BM_27,
                            dcs.vehicles.Artillery.Uragan_BM_27,
                            dcs.vehicles.Unarmed.Ural_375,
                            dcs.vehicles.Unarmed.Ural_375
                        ],
                        "initialInventory": 1,
                        "capabilities": {
                            "AUFTRAG.Type.ARTY": 50
                        }
                    }
                }
            },
            "Pottschutthohe": {
                "warehouse": "Pottschutthohe Brigade Warehouse#00001",
                "platoons": {
                    "Pottschutthohe B 1": {
                        "units": [
                            dcs.vehicles.Infantry.Paratrooper_AKS_74,
                            dcs.vehicles.Infantry.Paratrooper_AKS_74,
                            dcs.vehicles.Infantry.Paratrooper_RPG_16,
                            dcs.vehicles.Infantry.Paratrooper_RPG_16,
                        ],
                        "initialInventory": 3,
                        "capabilities": {
                            "AUFTRAG.Type.ONGUARD": 50
                        }
                    },
                    "Pottschutthohe B 2": {
                        "units": [
                            dcs.vehicles.Artillery.Uragan_BM_27,
                            dcs.vehicles.Artillery.Uragan_BM_27,
                            dcs.vehicles.Artillery.Uragan_BM_27,
                            dcs.vehicles.Artillery.Uragan_BM_27,
                            dcs.vehicles.Artillery.Uragan_BM_27,
                            dcs.vehicles.Unarmed.Ural_375,
                            dcs.vehicles.Unarmed.Ural_375
                        ],
                        "initialInventory": 1,
                        "capabilities": {
                            "AUFTRAG.Type.ARTY": 50
                        }
                    }
                }
            },
            "Bitburg": {
                "warehouse": "Bitburg Brigade Warehouse#00001",
                "platoons": {
                    "Bitburg B 1": {
                        "units": [
                            dcs.vehicles.Infantry.Paratrooper_AKS_74,
                            dcs.vehicles.Infantry.Paratrooper_AKS_74,
                            dcs.vehicles.Infantry.Paratrooper_RPG_16,
                            dcs.vehicles.Infantry.Paratrooper_RPG_16,
                        ],
                        "initialInventory": 3,
                        "capabilities": {
                            "AUFTRAG.Type.ONGUARD": 50
                        }
                    },
                    "Bitburg B 2": {
                        "units": [
                            dcs.vehicles.Artillery.Uragan_BM_27,
                            dcs.vehicles.Artillery.Uragan_BM_27,
                            dcs.vehicles.Artillery.Uragan_BM_27,
                            dcs.vehicles.Artillery.Uragan_BM_27,
                            dcs.vehicles.Artillery.Uragan_BM_27,
                            dcs.vehicles.Unarmed.Ural_375,
                            dcs.vehicles.Unarmed.Ural_375
                        ],
                        "initialInventory": 1,
                        "capabilities": {
                            "AUFTRAG.Type.ARTY": 50
                        }
                    }
                }
            },
        }
        return red_brigades

class BalloonFightBlueBrigades(calvinball.bluebrigade.BlueBrigades):
    def __init__(self) -> None:
        super().__init__()

    def define(self, m: dcs.Mission):
        blue_brigades = {
        }
        return blue_brigades
