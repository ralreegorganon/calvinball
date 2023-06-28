import dcs
import pydcs_extensions
import calvinball

class DangerZone(calvinball.mission.Mission):
    def __init__(self) -> None:
        t = dcs.terrain.Normandy()
        miz_name = "DangerZone"
        ctld = DangerZoneCtld()
        clients = DangerZoneClients()
        red_airwings = DangerZoneRedAirwings()
        blue_airwings = DangerZoneBlueAirwings()
        carriers = DangerZoneCarriers()
        qrf = DangerZoneQrf()
        reinforcement = DangerZoneReinforcement()
        red_brigades = DangerZoneRedBrigades()
        blue_brigades = DangerZoneBlueBrigades()

        super().__init__(t, miz_name, ctld, clients, red_airwings, blue_airwings, carriers, qrf, reinforcement, red_brigades, blue_brigades)

class DangerZoneCtld(calvinball.ctld.Ctld):
    def __init__(self) -> None:
        super().__init__()

    def build(self, m: dcs.Mission):
        super().build(m)

class DangerZoneQrf(calvinball.qrf.Qrf):
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
            dcs.vehicles.Unarmed.Land_Rover_109_S3,
            dcs.vehicles.Armor.Chieftain_mk3,
            dcs.vehicles.Armor.Chieftain_mk3,
            dcs.vehicles.Armor.Marder,
            dcs.vehicles.AirDefence.ZSU_23_4_Shilka,
            dcs.vehicles.Armor.MCV_80,
            dcs.vehicles.Armor.PT_76,
        ], p, formation=dcs.unitgroup.VehicleGroup.Formation.Scattered).late_activation = True

        m.vehicle_group_platoon(m.country(dcs.countries.CombinedJointTaskForcesRed.name), "RED QRF 3", [
            dcs.vehicles.Armor.Cobra,
            dcs.vehicles.Armor.TYPE_59,
            dcs.vehicles.Armor.BRDM_2,
            dcs.vehicles.Armor.TYPE_59,
            dcs.vehicles.Armor.BTR_80,
            dcs.vehicles.Armor.BTR_80,
            dcs.vehicles.Unarmed.Ural_375,
            dcs.vehicles.AirDefence.ZSU_23_4_Shilka,
        ], p, formation=dcs.unitgroup.VehicleGroup.Formation.Scattered).late_activation = True

        m.vehicle_group_platoon(m.country(dcs.countries.CombinedJointTaskForcesRed.name), "RED QRF 4", [
            dcs.vehicles.Armor.BTR_80,
            dcs.vehicles.Armor.BMD_1,
            dcs.vehicles.Armor.VAB_Mephisto,
            dcs.vehicles.Armor.BTR_80,
            dcs.vehicles.Armor.PT_76,
            dcs.vehicles.Armor.M_113,
        ], p, formation=dcs.unitgroup.VehicleGroup.Formation.Scattered).late_activation = True

        m.vehicle_group_platoon(m.country(dcs.countries.CombinedJointTaskForcesRed.name), "RED QRF 5", [
            dcs.vehicles.Unarmed.Land_Rover_109_S3,
            dcs.vehicles.Unarmed.ZIL_135,
            dcs.vehicles.Unarmed.Ural_4320T,
            dcs.vehicles.Armor.HL_KORD,
            dcs.vehicles.Unarmed.KAMAZ_Truck,
            dcs.vehicles.Unarmed.ZiL_131_APA_80,
        ], p, formation=dcs.unitgroup.VehicleGroup.Formation.Scattered).late_activation = True

        m.vehicle_group_platoon(m.country(dcs.countries.CombinedJointTaskForcesRed.name), "RED QRF 6", [
            dcs.vehicles.Unarmed.Tigr_233036,
            dcs.vehicles.Unarmed.ATZ_10,
            dcs.vehicles.Unarmed.UAZ_469,
            dcs.vehicles.Unarmed.ATZ_10,
            dcs.vehicles.Unarmed.ATZ_10,
            dcs.vehicles.Unarmed.ATMZ_5,
            dcs.vehicles.Armor.BTR_80,
        ], p, formation=dcs.unitgroup.VehicleGroup.Formation.Scattered).late_activation = True

        m.vehicle_group_platoon(m.country(dcs.countries.CombinedJointTaskForcesRed.name), "RED QRF 7", [
            dcs.vehicles.MissilesSS.Scud_B,
            dcs.vehicles.Unarmed.Ural_375,
            dcs.vehicles.MissilesSS.Scud_B,
            dcs.vehicles.MissilesSS.Scud_B,
            dcs.vehicles.MissilesSS.Scud_B,
            dcs.vehicles.Unarmed.Ural_375,
            dcs.vehicles.Unarmed.Ural_375,
        ], p, formation=dcs.unitgroup.VehicleGroup.Formation.Scattered).late_activation = True

        m.vehicle_group_platoon(m.country(dcs.countries.CombinedJointTaskForcesRed.name), "RED QRF 8", [
            dcs.vehicles.Armor.BTR_80,
            dcs.vehicles.Unarmed.ZIL_131_KUNG,
            dcs.vehicles.Artillery.SAU_Gvozdika,
            dcs.vehicles.Artillery.SAU_Gvozdika,
            dcs.vehicles.Unarmed.Ural_375,
            dcs.vehicles.Artillery.SAU_Gvozdika,
            dcs.vehicles.Artillery.SAU_Gvozdika,
        ], p, formation=dcs.unitgroup.VehicleGroup.Formation.Scattered).late_activation = True

class DangerZoneReinforcement(calvinball.reinforcement.Reinforcement):
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

class DangerZoneCarriers(calvinball.carriers.Carriers):
    def __init__(self) -> None:
        super().__init__()

    def define(self, m: dcs.mission):
        return {
            "Teddy": {
                "ship": dcs.ships.CVN_71,
                "position": {"x":80500,"y":-202400},
                "waypoints": [
                    {"x": 91500, "y": -76000, "speed": 25},
                    {"x": 89000, "y": -76000, "speed": 25},
                    {"x": 78000, "y": -202400, "speed": 25},
                ],
                "tacan_channel": 51,
                "icls_channel": 1,
                "radio": 301,
                "link4": 336
            },
            "Forrestal": {
                "ship": dcs.ships.Forrestal,
                "position": {"x":88000 ,"y":-195000},
                "waypoints": [
                    {"x": 99000, "y": -68600, "speed": 25},
                    {"x": 96500, "y": -68600, "speed": 25},
                    {"x": 85500, "y": -195000, "speed": 25},
                ],
                "tacan_channel": 52,
                "icls_channel": 2,
                "radio": 302,
                "link4": 337
            },
            "Invincible": {
                "ship": dcs.ships.Hms_invincible,
                "position": {"x":74000,"y":-199000},
                "waypoints": [
                    {"x": 85000, "y": -72600, "speed": 25},
                    {"x": 82500, "y": -72600, "speed": 25},
                    {"x": 71500, "y": -199000, "speed": 25},
                ],
                "tacan_channel": 53,
                "radio": 303
            },
            "Tarawa": {
                "ship": dcs.ships.LHA_Tarawa,
                "position": {"x":95000 ,"y":-165000},
                "waypoints": [
                    {"x": 96700, "y": -145500, "speed": 25},
                    {"x": 94200, "y": -145500, "speed": 25},
                    {"x": 92500, "y": -165000, "speed": 25},
                ],
                "tacan_channel": 54,
                "radio": 304
            },
            "Peleliu": {
                "ship": dcs.ships.LHA_Tarawa,
                "position": {"x":99500 ,"y":-165500},
                "waypoints": [
                    {"x": 101300, "y": -145500, "speed": 25},
                    {"x": 98800, "y": -145500, "speed": 25},
                    {"x": 97000, "y": -165500, "speed": 25},
                ],
                "tacan_channel": 55,
                "radio": 305
            },
        }
    
class DangerZoneClients(calvinball.clients.Clients):
    def __init__(self) -> None:
        super().__init__()

    def define(self, m: dcs.Mission, edit: bool):
        m.groundControl.blue_game_masters = 1
        m.groundControl.blue_tactical_commander = 1
        m.groundControl.blue_jtac = 2
        m.groundControl.red_game_masters = 1

        # m.coalition["blue"].set_bullseye({"x": -32691, "y": -270357})

        airport_set = [
            {
                "country": m.country(dcs.countries.CombinedJointTaskForcesBlue.name),
                "carrier": "Teddy",
                "start_type": dcs.mission.StartType.Cold,
                "airframes": [
                    { "airframe": dcs.planes.F_14B, "count": 4, "fuel": 1, "loadout": "Empty", "livery": "Santa", "properties": { dcs.planes.F_14B.Properties.INSAlignmentStored.id: True }  },
                    { "airframe": dcs.planes.FA_18C_hornet, "count": 4, "fuel": 1, "loadout": "Empty", "livery": "Santa" },
                ]
            },
            {
                "country": m.country(dcs.countries.CombinedJointTaskForcesBlue.name),
                "carrier": "Forrestal",
                "start_type": dcs.mission.StartType.Cold,
                "airframes": [
                    { "airframe": dcs.planes.F_14B, "count": 2, "fuel": 1, "loadout": "Empty", "livery": "Santa", "properties": { dcs.planes.F_14B.Properties.INSAlignmentStored.id: True } },
                    { "airframe": dcs.planes.FA_18C_hornet, "count": 2, "fuel": 1, "loadout": "Empty", "livery": "Santa" },
                ]
            },
            {
                "country": m.country(dcs.countries.CombinedJointTaskForcesBlue.name),
                "carrier": "Invincible",
                "start_type": dcs.mission.StartType.Cold,
                "airframes": [
                    { "airframe": dcs.planes.AV8BNA, "count": 3, "fuel": 1, "loadout": "Empty", "livery": "vma-214" },
                ]
            },
            {
                "country": m.country(dcs.countries.CombinedJointTaskForcesBlue.name),
                "carrier": "Tarawa",
                "start_type": dcs.mission.StartType.Cold,
                "airframes": [
                    { "airframe": dcs.helicopters.Mi_24P, "count": 3, "fuel": 0.6, "loadout": "Empty", "livery": "Ukrainian Army Aviation" },
                    { "airframe": dcs.helicopters.Mi_8MT, "count": 3, "fuel": 0.6, "loadout": "Empty", "livery": "Algerian AF Green EVSAN" },
                    { "airframe": dcs.helicopters.SA342L, "count": 1, "fuel": 0.6, "loadout": "Empty", "livery": "Tiger Meet 2" },
                    { "airframe": dcs.helicopters.SA342M, "count": 1, "fuel": 0.6, "loadout": "Empty", "livery": "Tiger Meet" },
                ]
            },
            {
                "country": m.country(dcs.countries.CombinedJointTaskForcesBlue.name),
                "carrier": "Peleliu",
                "start_type": dcs.mission.StartType.Cold,
                "airframes": [
                    { "airframe": dcs.helicopters.UH_1H, "count": 3, "fuel": 0.6, "loadout": "Empty", "livery": "US ARMY 1972" },
                    { "airframe": dcs.helicopters.AH_64D_BLK_II, "count": 3, "fuel": 0.6, "loadout": "Empty", "livery": "JGSDF——1st_Combat_Helicopter_Unit" },
                    { "airframe": dcs.helicopters.Ka_50_3, "count": 2, "fuel": 0.6, "loadout": "Empty", "livery": "Ka-50_desert_werewolf", "properties": { dcs.helicopters.Ka_50_3.Properties.Realistic_INS.id: dcs.helicopters.Ka_50_3.Properties.Realistic_INS.Values.No_alignment_and_fixtaking_needed } },
                ]
            },
            {
                "country": m.country(dcs.countries.CombinedJointTaskForcesBlue.name),
                "farp": "FARP Portland Bill",
                "farp_zone": "FARP-1",
                "start_type": dcs.mission.StartType.Cold,
                "airframes": [
                    {
                        "airframe": dcs.helicopters.Mi_24P, "fuel": 0.6, "loadout": "Empty", "livery": "Ukrainian Army Aviation",
                        "positions": [{"heading": 162, "x": 111649.07192207, "y": -157093.62475887}, {"heading": 182, "x": 111650.64044132, "y": -157064.80321772}, {"heading": 135, "x": 111621.62283526, "y": -157151.46390607}, {"heading": 141, "x": 111638.93660027, "y": -157126.10018774}]
                    },
                    {
                        "airframe": dcs.helicopters.Mi_8MT, "fuel": 0.6, "loadout": "Empty", "livery": "Algerian AF Green EVSAN",
                        "positions": [{"heading": 106, "x": 111539.25775076, "y": -157186.30998705}, {"heading": 72, "x": 111504.85727184, "y": -157183.81461552}, {"heading": 116, "x": 111598.93427259, "y": -157168.5994773}, {"heading": 119, "x": 111569.74118467, "y": -157179.08060095}]
                    },
                    {
                        "airframe": dcs.helicopters.UH_1H, "fuel": 0.6, "loadout": "Empty", "livery": "US ARMY 1972",
                        "positions": [{"heading": 251, "x": 111544.47868506, "y": -156946.13075871}, {"heading": 257, "x": 111524.43705288, "y": -156946.3823697}, {"heading": 247, "x": 111577.94294707, "y": -156953.80489398}, {"heading": 255, "x": 111561.96564905, "y": -156947.76623016}]
                    },
                    {
                        "airframe": dcs.helicopters.AH_64D_BLK_II, "fuel": 0.6, "loadout": "Empty", "livery": "JGSDF——1st_Combat_Helicopter_Unit",
                        "positions": [{"heading": 40, "x": 111429.69489901, "y": -157138.97457157}, {"heading": 30, "x": 111414.38222987, "y": -157110.72161865}, {"heading": 63, "x": 111477.14260621, "y": -157175.85438035}, {"heading": 45, "x": 111452.83076481, "y": -157160.04379569}]
                    },
                    {
                        "airframe": dcs.helicopters.SA342L, "fuel": 0.6, "loadout": "Empty", "livery": "Tiger Meet 2",
                        "positions": [{"heading": 225, "x": 111628.68117187, "y": -156991.47494297}]
                    },
                    {
                        "airframe": dcs.helicopters.SA342M, "fuel": 0.6, "loadout": "Empty", "livery": "Tiger Meet",
                        "positions": [{"heading": 234, "x": 111612.6038496, "y": -156976.18188032}]
                    },
                    {
                        "airframe": dcs.helicopters.Ka_50_3, "fuel": 0.6, "loadout": "Empty", "livery": "Ka-50_desert_werewolf",
                        "positions": [{"heading": 208, "x": 111649.66011679, "y": -157033.82496261}, {"heading": 212, "x": 111640.64113112, "y": -157011.27749845}],
                        "properties": { dcs.helicopters.Ka_50_3.Properties.Realistic_INS.id: dcs.helicopters.Ka_50_3.Properties.Realistic_INS.Values.No_alignment_and_fixtaking_needed }
                    },
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
            dcs.planes.Mirage_F1EE: ["vhf_am", "uhf"],
            dcs.planes.P_51D_30_NA: ["vhf_am"],
            dcs.planes.Su_25: ["vhf_am"],
            dcs.planes.Su_25T: ["vhf_am"],
            dcs.planes.F_14B: ["uhf", "vhf_am"],
            dcs.planes.FA_18C_hornet: ["vhf_am", "uhf"],
        }

        if not edit:
            airport_set[0]["airframes"].append({ "airframe": pydcs_extensions.A_4E_C, "count": 4, "loadout": "Empty", "livery": "Aggressor USN VF-126 Bandits" })
            airport_set[1]["airframes"].append({ "airframe": pydcs_extensions.A_4E_C, "count": 4, "loadout": "Empty", "livery": "Aggressor USN VF-126 Bandits" })

            radios[pydcs_extensions.A_4E_C] = ["uhf"]

        for airport in airport_set:
            for airframe in airport["airframes"]:
                airframe["radios"] = {}
                if airframe["airframe"] in radio_override:
                    airframe["radio_override"] = radio_override[airframe["airframe"]]
                for i, template in enumerate(radios[airframe["airframe"]]):
                    airframe["radios"][i+1] = comms_plan[template]

        return airport_set

class DangerZoneRedAirwings(calvinball.redairwing.RedAirwings):
    def __init__(self) -> None:
        super().__init__()

    def define(self, m: dcs.Mission):
        red_airwings = {
            "1st Goon Wing - Evreux": {
                "airbase": "Evreux",
                "warehouse": "Evreux Airwing Warehouse#00001",
                "squadrons": {
                    "1GW-Evreux-1": {
                        "airframe": dcs.planes.JF_17,
                        "groupSize": 2,
                        "initialInventory": 2,
                        "livery": "PLAAF 125th AB (Fictional)",
                        "loadouts": {
                            "PL-5Ex2, 2*SD-10x2, 800L Tank": "{ AUFTRAG.Type.CAP, AUFTRAG.Type.INTERCEPT }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.CAP": 50,
                            "AUFTRAG.Type.INTERCEPT": 50,
                            "AUFTRAG.Type.ESCORT": 50,
                        }
                    },
                    "1GW-Evreux-2": {
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
            "1st Goon Wing - Funtington": {
                "airbase": "Funtington",
                "warehouse": "Funtington Airwing Warehouse#00001",
                "squadrons": {
                    "1GW-Funtington-1": {
                        "airframe": dcs.planes.JF_17,
                        "groupSize": 2,
                        "initialInventory": 2,
                        "livery": "PLAAF 125th AB (Fictional)",
                        "loadouts": {
                            "PL-5Ex2, 2*SD-10x2, 800L Tank": "{ AUFTRAG.Type.CAP, AUFTRAG.Type.INTERCEPT }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.CAP": 50,
                            "AUFTRAG.Type.INTERCEPT": 50,
                            "AUFTRAG.Type.ESCORT": 50
                        }
                    },
                }
            },
            "2nd Goon Wing - Stoney Cross": {
                "airbase": "Stoney Cross",
                "warehouse": "Stoney Cross Airwing Warehouse#00001",
                "squadrons": {
                    "2GW-Stoney Cross-2": {
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
                    "2GW-Stoney Cross-3": {
                        "airframe": dcs.planes.F_16C_50,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "18th AGRS BDU Splinter",
                        "loadouts": {
                            "AIM-120C*4, AIM-9X*2, FUEL*2, ECM": "{ AUFTRAG.Type.CAP, AUFTRAG.Type.INTERCEPT, AUFTRAG.Type.ESCORT }",
                            "AIM-120C*2, AIM-9X*2, AGM-65D*4, FUEL*2, ECM, TGP": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.CASENHANCED }",
                            "AIM-120C*2, AIM-9X*2, CBU-105*4, FUEL*2, ECM, TGP": "{ AUFTRAG.Type.BOMBCARPET}",
                            "AIM-120C*4, AGM-88C*4, ECM, TGP, HTS": "{ AUFTRAG.Type.SEAD }"
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
                    "2GW-Stoney Cross-4": {
                        "airframe": dcs.planes.F_5E_3,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "black 'Mig-28'",
                        "loadouts": {
                            "AIM-9P5*2, Fuel 150*3": "{ AUFTRAG.Type.CAP, AUFTRAG.Type.INTERCEPT, AUFTRAG.Type.ESCORT }",
                            "Mk-82SE*5,AIM-9*2": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.BOMBCARPET, AUFTRAG.Type.CASENHANCED }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.CAP": 50,
                            "AUFTRAG.Type.INTERCEPT": 50,
                            "AUFTRAG.Type.ESCORT": 50,
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.BOMBCARPET": 50,
                            "AUFTRAG.Type.CASENHANCED": 50
                        }
                    },
                    "2GW-Stoney Cross-5": {
                        "airframe": dcs.planes.Mirage_F1EE,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "USA Company Skin (M-EE)",
                        "loadouts": {
                            "2*R550 Magic I, 2*R530IR, 1*Fuel Tank": "{ AUFTRAG.Type.CAP, AUFTRAG.Type.INTERCEPT, AUFTRAG.Type.ESCORT }",
                            "2*AIM-9JULI, 8*SAMP 400 LD": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.BOMBCARPET, AUFTRAG.Type.CASENHANCED }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.CAP": 50,
                            "AUFTRAG.Type.INTERCEPT": 50,
                            "AUFTRAG.Type.ESCORT": 50,
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.BOMBCARPET": 50,
                            "AUFTRAG.Type.CASENHANCED": 50
                        }
                    },
                    "2GW-Stoney Cross-6": {
                        "airframe": dcs.planes.MiG_21Bis,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "Draken International",
                        "loadouts": {
                            "Patrol, short range": "{ AUFTRAG.Type.CAP, AUFTRAG.Type.INTERCEPT, AUFTRAG.Type.ESCORT }",
                            "Few big targets, GROM + BOMBS": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.BOMBCARPET, AUFTRAG.Type.CASENHANCED }",
                        },
                        "capabilities": {
                            "AUFTRAG.Type.CAP": 50,
                            "AUFTRAG.Type.INTERCEPT": 50,
                            "AUFTRAG.Type.ESCORT": 50,
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.BOMBCARPET": 50,
                            "AUFTRAG.Type.CASENHANCED": 50
                        }
                    },
                }
            },
            "1st Goon Wing - Anglo": {
                "airbase": "Anglo Farp#00001",
                "warehouse": "Anglo Airwing Warehouse#00001",
                "squadrons": {
                    "1GW-Anglo-1": {
                        "airframe": dcs.helicopters.Mi_26,
                        "groupSize": 1,
                        "initialInventory": 99,
                        "livery": "Russia_VVS_Grey",
                        "loadouts": {
                            "Empty": "{ AUFTRAG.Type.OPSTRANSPORT }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.OPSTRANSPORT": 50
                        }
                    },
                    "1GW-Anglo-2": {
                        "airframe": dcs.helicopters.Mi_24P,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "Russian Air Force",
                        "loadouts": {
                            "2xB8V20 (S-8KOM)+8xATGM 9M114": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.CASENHANCED }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.CASENHANCED": 50
                        }
                    },
                }
            },
        }
        return red_airwings

class DangerZoneBlueAirwings(calvinball.blueairwing.BlueAirwings):
    def __init__(self) -> None:
        super().__init__()

    def define(self, m: dcs.Mission):
        blue_airwings = {
            "1st CAW - Teddy": {
                "airbase": "Teddy",
                "warehouse": "Teddy Unit #1",
                "squadrons": {
                    "GGD-01": {
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
                    "GGD-02 JTAC": {
                        "airframe": dcs.planes.S_3B,
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
                    "GGD-02": {
                        "airframe": dcs.helicopters.CH_53E,
                        "groupSize": 1,
                        "initialInventory": 99,
                        "livery": "standard",
                        "loadouts": {
                            "Empty": "{ AUFTRAG.Type.OPSTRANSPORT }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.OPSTRANSPORT": 50
                        }
                    }
                }
            },
            "2nd CAW - Teddy": {
                "airbase": "Teddy",
                "warehouse": "Teddy Unit #1",
                "squadrons": {
                    "GGD-03": {
                        "airframe": dcs.planes.FA_18C_hornet,
                        "groupSize": 2,
                        "initialInventory": 99,
                        "livery": "Canada 150 Demo Jet",
                        "loadouts": {
                            "AIM-9X*2, AIM-120C-5*6, FUEL*3": "{ AUFTRAG.Type.CAP }",
                           #"AIM-9X*2, AIM-120C-5*1, GBU-38*4, GBU-12*4, ATFLIR, FUEL": "{ AUFTRAG.Type.CASENHANCED }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.CAP": 50,
                            #"AUFTRAG.Type.CASENHANCED": 50,
                        }
                    }
                }
            },
        }
        return blue_airwings

class DangerZoneRedBrigades(calvinball.redbrigade.RedBrigades):
    def __init__(self) -> None:
        super().__init__()

    def define(self, m: dcs.Mission):
        red_brigades = {
            "1st Anglo": {
                "warehouse": "Anglo Brigade Warehouse#00001",
                "platoons": {
                    "1GW-Anglo-2": {
                        "units": [
                            dcs.vehicles.Infantry.Paratrooper_AKS_74,
                            dcs.vehicles.Infantry.Paratrooper_AKS_74,
                            dcs.vehicles.Infantry.Paratrooper_AKS_74,
                            dcs.vehicles.Infantry.Paratrooper_AKS_74,
                            dcs.vehicles.Infantry.Paratrooper_AKS_74,
                            dcs.vehicles.Infantry.Paratrooper_AKS_74,
                            dcs.vehicles.Infantry.Paratrooper_AKS_74,
                            dcs.vehicles.Infantry.Paratrooper_AKS_74,
                            dcs.vehicles.Infantry.Paratrooper_RPG_16,
                            dcs.vehicles.Infantry.Paratrooper_RPG_16,
                            dcs.vehicles.Infantry.Paratrooper_RPG_16,
                            dcs.vehicles.Infantry.Paratrooper_RPG_16,
                        ],
                        "initialInventory": 3,
                        "capabilities": {
                            "AUFTRAG.Type.ONGUARD": 50
                        }
                    },
                    "1GW-Anglo-3": {
                        "units": [
                            dcs.vehicles.Artillery.Grad_URAL,
                            dcs.vehicles.Artillery.Grad_URAL,
                            dcs.vehicles.Artillery.Grad_URAL,
                            dcs.vehicles.Artillery.Grad_URAL,
                            dcs.vehicles.Artillery.Grad_URAL,
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
            # "2nd Goonwalker": {
            #     "warehouse": "Anglo Brigade Warehouse#00001",
            #     "platoons": {
            #         "1GW-Anglo-1": {
            #             "units": [
            #                 dcs.vehicles.Armor.T_55,
            #                 dcs.vehicles.Armor.T_55,
            #                 dcs.vehicles.Armor.T_55,
            #                 dcs.vehicles.Armor.T_55,
            #                 dcs.vehicles.Armor.T_55,
            #                 dcs.vehicles.Armor.T_55,
            #                 dcs.vehicles.Armor.T_55,
            #                 dcs.vehicles.Unarmed.Ural_375,
            #                 dcs.vehicles.Unarmed.Ural_375,
            #                 dcs.vehicles.Unarmed.ATZ_5
            #             ],
            #             "initialInventory": 1,
            #             "capabilities": {
            #                 "AUFTRAG.Type.ONGUARD": 50
            #             }
            #         }
            #     }
            # },
        }
        return red_brigades

class DangerZoneBlueBrigades(calvinball.bluebrigade.BlueBrigades):
    def __init__(self) -> None:
        super().__init__()

    def define(self, m: dcs.Mission):
        blue_brigades = {
            "1st Teddy": {
                "warehouse": "Teddy Unit #1",
                "platoons": {
                    "Teddy-01": {
                        "units": [
                            dcs.vehicles.Infantry.Soldier_M4,
                            dcs.vehicles.Infantry.Soldier_M4,
                            dcs.vehicles.Infantry.Soldier_M4,
                            dcs.vehicles.Infantry.Soldier_M4,
                            dcs.vehicles.Infantry.Soldier_M4,
                            dcs.vehicles.Infantry.Soldier_M4,
                            dcs.vehicles.Infantry.Soldier_M4,
                            dcs.vehicles.Infantry.Soldier_M4,
                            dcs.vehicles.Infantry.Soldier_RPG,
                            dcs.vehicles.Infantry.Soldier_RPG,
                            dcs.vehicles.Infantry.Soldier_RPG,
                            dcs.vehicles.Infantry.Soldier_RPG,
                        ],
                        "initialInventory": 1,
                        "capabilities": {
                            "AUFTRAG.Type.ONGUARD": 50
                        }
                    }
                }
            }
        }
        return blue_brigades
