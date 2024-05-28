import dcs
import pydcs_extensions
import calvinball

class RockTheCasbah(calvinball.mission.Mission):
    def __init__(self) -> None:
        t = dcs.terrain.PersianGulf()
        miz_name = "RockTheCasbah"
        ctld = RockTheCasbahCtld()
        clients = RockTheCasbahClients()
        red_airwings = RockTheCasbahRedAirwings()
        blue_airwings = RockTheCasbahBlueAirwings()
        carriers = RockTheCasbahCarriers()
        qrf = RockTheCasbahQrf()
        reinforcement = RockTheCasbahReinforcement()
        red_brigades = RockTheCasbahRedBrigades()
        blue_brigades = RockTheCasbahBlueBrigades()

        super().__init__(t, miz_name, ctld, clients, red_airwings, blue_airwings, carriers, qrf, reinforcement, red_brigades, blue_brigades)

        self.m.coalition["blue"].set_bullseye({"x": -147009 , "y": -396554})
        self.m.coalition["red"].set_bullseye({"x": -147009 , "y": -396554})

class RockTheCasbahCtld(calvinball.ctld.Ctld):
    def __init__(self) -> None:
        super().__init__()

    def build(self, m: dcs.Mission):
        super().build(m)

class RockTheCasbahQrf(calvinball.qrf.Qrf):
    def __init__(self) -> None:
        super().__init__()

    def build(self, m: dcs.Mission):
        super().build(m)

        p = dcs.mapping.Point(m.coalition["blue"].bullseye["x"], m.coalition["blue"].bullseye["y"], m.terrain)

        m.vehicle_group_platoon(m.country(dcs.countries.CombinedJointTaskForcesRed.name), "RED QRF 1", [
            dcs.vehicles.Armor.BRDM_2,
            dcs.vehicles.Unarmed.Ural_375,
            dcs.vehicles.Armor.BRDM_2,
            dcs.vehicles.Unarmed.Ural_375,
            dcs.vehicles.Unarmed.Ural_375,
            dcs.vehicles.AirDefence.ZSU_23_4_Shilka,
            dcs.vehicles.Armor.BMP_1,
            dcs.vehicles.Armor.BMP_1,
            dcs.vehicles.Armor.BMP_1,
        ], p, formation=dcs.unitgroup.VehicleGroup.Formation.Scattered).late_activation = True

        m.vehicle_group_platoon(m.country(dcs.countries.CombinedJointTaskForcesRed.name), "RED QRF 2", [
            dcs.vehicles.Armor.Cobra,
            dcs.vehicles.Armor.TYPE_59,
            dcs.vehicles.Armor.BRDM_2,
            dcs.vehicles.Armor.TYPE_59,
            dcs.vehicles.Armor.BTR_80,
            dcs.vehicles.Armor.BTR_80,
            dcs.vehicles.Unarmed.Ural_375,
            dcs.vehicles.AirDefence.ZSU_23_4_Shilka,
        ], p, formation=dcs.unitgroup.VehicleGroup.Formation.Scattered).late_activation = True

        m.vehicle_group_platoon(m.country(dcs.countries.CombinedJointTaskForcesRed.name), "RED QRF 3", [
            dcs.vehicles.Unarmed.Land_Rover_109_S3,
            dcs.vehicles.Unarmed.ZIL_135,
            dcs.vehicles.Unarmed.Ural_4320T,
            dcs.vehicles.Armor.HL_KORD,
            dcs.vehicles.Unarmed.KAMAZ_Truck,
            dcs.vehicles.Unarmed.ZiL_131_APA_80,
        ], p, formation=dcs.unitgroup.VehicleGroup.Formation.Scattered).late_activation = True

        m.vehicle_group_platoon(m.country(dcs.countries.CombinedJointTaskForcesRed.name), "RED QRF 4", [
            dcs.vehicles.Unarmed.Tigr_233036,
            dcs.vehicles.Unarmed.ATZ_10,
            dcs.vehicles.Unarmed.UAZ_469,
            dcs.vehicles.Unarmed.ATZ_10,
            dcs.vehicles.Unarmed.ATZ_10,
            dcs.vehicles.Unarmed.ATMZ_5,
            dcs.vehicles.Armor.BTR_80,
        ], p, formation=dcs.unitgroup.VehicleGroup.Formation.Scattered).late_activation = True

        m.vehicle_group_platoon(m.country(dcs.countries.CombinedJointTaskForcesRed.name), "RED QRF 5", [
            dcs.vehicles.MissilesSS.Scud_B,
            dcs.vehicles.Unarmed.Ural_375,
            dcs.vehicles.MissilesSS.Scud_B,
            dcs.vehicles.MissilesSS.Scud_B,
            dcs.vehicles.MissilesSS.Scud_B,
            dcs.vehicles.Unarmed.Ural_375,
            dcs.vehicles.Unarmed.Ural_375,
        ], p, formation=dcs.unitgroup.VehicleGroup.Formation.Scattered).late_activation = True

class RockTheCasbahReinforcement(calvinball.reinforcement.Reinforcement):
    def __init__(self) -> None:
        super().__init__()

    def build(self, m: dcs.Mission):
        super().build(m)

        p = dcs.mapping.Point(m.coalition["blue"].bullseye["x"], m.coalition["blue"].bullseye["y"], m.terrain)

        m.vehicle_group_platoon(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "BLUE REINFORCEMENT 1", [
            dcs.vehicles.Armor.M1128_Stryker_MGS,
            dcs.vehicles.Unarmed.M_818,
            dcs.vehicles.Armor.M1126_Stryker_ICV,
            dcs.vehicles.Armor.M1045_HMMWV_TOW,
            dcs.vehicles.AirDefence.Vulcan,
        ], p, formation=dcs.unitgroup.VehicleGroup.Formation.Scattered).late_activation = True


class RockTheCasbahCarriers(calvinball.carriers.Carriers):
        def __init__(self) -> None:
            super().__init__()

class RockTheCasbahClients(calvinball.clients.Clients):
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
                "airport": m.terrain.airports["Al Dhafra AFB"],
                "start_type": dcs.mission.StartType.Warm,
                "airframes": [
                    {
                        "airframe": dcs.helicopters.AH_64D_BLK_II, "fuel": 0.6, "loadout": "Empty", "livery": "JGSDF——1st_Combat_Helicopter_Unit",
                        "positions": [{"heading": 30, "x": -211045.51557317, "y": -174022.30478844}, {"heading": 45, "x": -211007.06703823, "y": -174071.62696548}, {"heading": 63, "x": -210982.75519683, "y": -174087.43755014}, {"heading": 40, "x": -211030.20290403, "y": -174050.55774136}]
                    },
                    {
                        "airframe": dcs.helicopters.Ka_50_3, "fuel": 0.6, "loadout": "Empty", "livery": "Ka-50_desert_werewolf", "properties": { dcs.helicopters.Ka_50_3.Properties.Realistic_INS.id: dcs.helicopters.Ka_50_3.Properties.Realistic_INS.Values.No_alignment_and_fixtaking_needed },
                        "positions": [{"heading": 208, "x": -210810.23768625, "y": -173945.4081324}, {"heading": 212, "x": -210819.25667192, "y": -173922.86066824}]
                    },
                    {
                        "airframe": dcs.helicopters.Mi_24P, "fuel": 0.6, "loadout": "Empty", "livery": "Ukrainian Army Aviation",
                        "positions": [{"heading": 135, "x": -210838.27496778, "y": -174063.04707586}, {"heading": 162, "x": -210810.82588097, "y": -174005.20792866}, {"heading": 182, "x": -210809.25736172, "y": -173976.38638751}, {"heading": 141, "x": -210820.96120277, "y": -174037.68335753}]
                    },
                    {
                        "airframe": dcs.helicopters.Mi_8MT, "fuel": 0.6, "loadout": "Empty", "livery": "Algerian AF Green EVSAN",
                        "positions": [{"heading": 116, "x": -210860.96353045, "y": -174080.18264709}, {"heading": 106, "x": -210920.64005228, "y": -174097.89315684}, {"heading": 72, "x": -210955.0405312, "y": -174095.39778531}, {"heading": 119, "x": -210890.15661837, "y": -174090.66377074}]
                    },
                    {
                        "airframe": dcs.helicopters.SA342L, "fuel": 0.6, "loadout": "Empty", "livery": "Tiger Meet 2",
                        "positions": [{"heading": 225, "x": -210831.21663117, "y": -173903.05811276}]
                    },
                    {
                        "airframe": dcs.helicopters.SA342M, "fuel": 0.6, "loadout": "Empty", "livery": "Tiger Meet",
                        "positions": [{"heading": 234, "x": -210847.29395344, "y": -173887.76505011}]
                    },
                    {
                        "airframe": dcs.helicopters.UH_1H, "fuel": 0.6, "loadout": "Empty", "livery": "US ARMY 1972",
                        "positions": [{"heading": 247, "x": -210881.95485597, "y": -173865.38806377}, {"heading": 251, "x": -210915.41911798, "y": -173857.7139285}, {"heading": 257, "x": -210935.46075016, "y": -173857.96553949}, {"heading": 255, "x": -210897.93215399, "y": -173859.34939995}]
                    },
                    { "airframe": dcs.planes.A_10C_2, "count": 4, "parking": [57, 58, 59, 60], "fuel": 0.6, "loadout": "Empty", "livery": "355th fs eielson afb, alaska (ak)" },
                    { "airframe": dcs.planes.AJS37, "count": 2, "parking": [231, 230], "fuel": 1, "loadout": "Empty", "livery": "SF-37 Akktu Stakki - F21" },
                    { "airframe": dcs.planes.AV8BNA, "count": 4, "parking": [192, 191, 190, 189], "fuel": 1, "loadout": "Empty", "livery": "vma-214" },
                    { "airframe": dcs.planes.C_101CC, "count": 2, "parking": [225, 226], "fuel": 1, "loadout": "Empty", "livery": "usaf agressor fictional" },
                    { "airframe": dcs.planes.F_5E_3, "count": 4, "parking": [252, 251, 250, 249], "fuel": 1, "loadout": "Empty", "livery": "BR FAB 4846" },
                    { "airframe": dcs.planes.F_86F_Sabre, "count": 2, "parking": [208, 229], "fuel": 1, "loadout": "Empty", "livery": "Royal Saudi Air Force" },
                    { "airframe": dcs.planes.L_39ZA, "count": 2, "parking": [227, 228], "fuel": 1, "loadout": "Empty", "livery": "algerian af tiger nl-36" },
                    { "airframe": dcs.planes.M_2000C, "count": 4, "parking": [235, 234, 233, 232], "fuel": 1, "loadout": "Empty", "livery": "2003 Tigermeet" },
                    { "airframe": dcs.planes.MB_339A, "count": 2, "parking": [223, 224], "fuel": 1, "loadout": "Empty", "livery": "MB339AN 'NIGERIA'" },
                    { "airframe": dcs.planes.MiG_19P, "count": 2, "parking": [214, 213], "fuel": 1, "loadout": "Empty", "livery": "DDR - Fictional" },
                    { "airframe": dcs.planes.MiG_21Bis, "count": 4, "parking": [212, 211, 210, 209], "fuel": 1, "loadout": "Empty", "livery": "HuAF 31st AB (Turul Sqn)" },
                    { "airframe": dcs.planes.Mirage_F1EE, "count": 4, "parking": [248, 247, 246, 245], "fuel": 1, "loadout": "Empty", "livery": "USA AGGRESSOR Colour (CE)" },
                    { "airframe": dcs.planes.Mirage_F1BE, "count": 2, "parking": [237, 236], "fuel": 1, "loadout": "Empty", "livery": "USA AGGRESSOR Colour (CE)" },
                    { "airframe": dcs.planes.Su_25, "count": 4, "parking": [219, 220, 221, 222], "fuel": 1, "loadout": "Empty", "livery": "petal camo scheme #1 (native). 299th brigade", "start_type": dcs.mission.StartType.Cold },
                    { "airframe": dcs.planes.Su_25T, "count": 4, "parking": [218, 217, 216, 215], "fuel": 1, "loadout": "Empty", "livery": "Algerian AF Desert KU-03", "start_type": dcs.mission.StartType.Cold },
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
        }

        if not edit:
            airport_set[0]["airframes"].append({ "airframe": pydcs_extensions.A_4E_C, "count": 7, "parking": [244, 243, 242, 241, 240, 239, 238], "fuel": 0.75, "loadout": "Empty", "livery": "Aggressor USN VF-126 Bandits" })
            airport_set[0]["airframes"].append({ "airframe": pydcs_extensions.Bronco_OV_10A, "count": 4, "parking": [253, 106, 105, 102], "fuel": 1, "loadout": "Empty", "livery": "colombian 2221" })
            airport_set[0]["airframes"].append({ "airframe": pydcs_extensions.Hercules, "count": 2, "parking": [100, 104], "fuel": 0.6, "loadout": "Empty" })

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

class RockTheCasbahRedAirwings(calvinball.redairwing.RedAirwings):
    def __init__(self) -> None:
        super().__init__()

    def define(self, m: dcs.Mission):
        red_airwings = {
            "Liwa AFB": {
                "airbase": "Liwa AFB",
                "warehouse": "Liwa AFB Airwing Warehouse#00001",
                "squadrons": {
                    "Liwa-AFB-1": {
                        "airframe": dcs.planes.Mirage_F1EE,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "USA Company Skin (M-EE)",
                        "loadouts": {
                            "2*R550 Magic I, 2*R530IR, 1*Fuel Tank": "{ AUFTRAG.Type.CAP, AUFTRAG.Type.INTERCEPT, AUFTRAG.Type.ESCORT }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.CAP": 50,
                            "AUFTRAG.Type.INTERCEPT": 50,
                            "AUFTRAG.Type.ESCORT": 50
                        }
                    },
                    "Liwa-AFB-2": {
                        "airframe": dcs.helicopters.Mi_26,
                        "groupSize": 1,
                        "initialInventory": 1,
                        "takeoffCold": "true",
                        "parking": "{14, 15, 16}",
                        "livery": "Russia_VVS_Grey",
                        "loadouts": {
                            "Empty": "{ AUFTRAG.Type.OPSTRANSPORT }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.OPSTRANSPORT": 50
                        }
                    },
                    "Liwa-AFB-3": {
                        "airframe": dcs.helicopters.Mi_24P,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "Russian Air Force",
                        "loadouts": {
                            "GoonsSuck": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.CASENHANCED }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.CASENHANCED": 50
                        }
                    },
                    "Liwa-AFB-4": {
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

class RockTheCasbahBlueAirwings(calvinball.blueairwing.BlueAirwings):
    def __init__(self) -> None:
        super().__init__()

    def define(self, m: dcs.Mission):
        blue_airwings = {
             "Al Dhafra AFB": {
                "airbase": "Al Dhafra AFB",
                "warehouse": "Al Dhafra AFB Airwing Warehouse#00001",
                "squadrons": {
                    "G-01": {
                        "airframe": dcs.planes.E_2C,
                        "groupSize": 1,
                        "initialInventory": 99,
                        "livery": "VAW-125 Tigertails",
                        "loadouts": {
                            "Empty": "{ AUFTRAG.Type.AWACS }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.AWACS": 50
                        }
                    },
                    "G-02 JTAC": {
                        "airframe": dcs.planes.MQ_9_Reaper,
                        "groupSize": 1,
                        "initialInventory": 99,
                        "livery": "usaf standard",
                        "loadouts": {
                            "Empty": "{ AUFTRAG.Type.RECON }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.RECON": 50
                        }
                    },
                    "G-03": {
                        "airframe": dcs.helicopters.CH_47D,
                        "groupSize": 1,
                        "initialInventory": 99,
                        "livery": "standard",
                        "takeoffCold": "true",
                        "parking": "{14, 15, 16}",
                        "loadouts": {
                            "Empty": "{ AUFTRAG.Type.OPSTRANSPORT }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.OPSTRANSPORT": 50
                        }
                    }
                }
            },
        }
        return blue_airwings

class RockTheCasbahRedBrigades(calvinball.redbrigade.RedBrigades):
    def __init__(self) -> None:
        super().__init__()

    def define(self, m: dcs.Mission):
        red_brigades = {
            "Liwa AFB": {
                "warehouse": "Liwa AFB Brigade Warehouse#00001",
                "platoons": {
                    "Liwa-AFB-P-1": {
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
                    "Liwa-AFB-P-2": {
                        "units": [
                            dcs.vehicles.Armor.TPZ,
                            dcs.vehicles.Armor.TPZ,
                            dcs.vehicles.Armor.TPZ,
                            dcs.vehicles.Armor.TPZ,
                            dcs.vehicles.Unarmed.Ural_375,
                            dcs.vehicles.Unarmed.Ural_375
                        ],
                        "initialInventory": 1,
                        "capabilities": {
                            "AUFTRAG.Type.OPSTRANSPORT": 50
                        }
                    }
                }
            },
        }
        return red_brigades

class RockTheCasbahBlueBrigades(calvinball.bluebrigade.BlueBrigades):
    def __init__(self) -> None:
        super().__init__()

    def define(self, m: dcs.Mission):
        blue_brigades = {
            "Al Dhafra AFB": {
                "warehouse": "Al Dhafra AFB Brigade Warehouse#00001",
                "platoons": {
                    "GP-01": {
                        "units": [
                            dcs.vehicles.Infantry.Soldier_M4,
                            dcs.vehicles.Infantry.Soldier_M4,
                            dcs.vehicles.Infantry.Soldier_RPG,
                            dcs.vehicles.Infantry.Soldier_RPG,
                        ],
                        "initialInventory": 99,
                        "capabilities": {
                            "AUFTRAG.Type.ONGUARD": 50
                        }
                    },
                    "GP-02": {
                        "units": [
                            dcs.vehicles.Armor.AAV7,
                            dcs.vehicles.Armor.AAV7,
                            dcs.vehicles.Armor.AAV7,
                            dcs.vehicles.Armor.AAV7,
                            dcs.vehicles.Unarmed.M_818,
                            dcs.vehicles.Unarmed.M_818
                        ],
                        "initialInventory": 99,
                        "capabilities": {
                            "AUFTRAG.Type.OPSTRANSPORT": 50
                        }
                    }
                }
            },
        }
        return blue_brigades
