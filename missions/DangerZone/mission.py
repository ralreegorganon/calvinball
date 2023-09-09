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
            "Abe": {
                "ship": dcs.ships.CVN_72,
                "position": {"x":105300 ,"y":-10200},
                "waypoints": [
                    {"x": 151200, "y": 97400, "speed": 25},
                    {"x": 148700, "y": 97400, "speed": 25},
                    {"x": 102800, "y": -10200, "speed": 25},
                ],
                "tacan_channel": 56,
                "icls_channel": 3,
                "radio": 306,
                "link4": 338
            },
            "Saratoga": {
                "ship": dcs.ships.Forrestal,
                "position": {"x":111300 ,"y":-13200},
                "waypoints": [
                    {"x": 157200, "y": 94400, "speed": 25},
                    {"x": 154700, "y": 94400, "speed": 25},
                    {"x": 108800, "y": -13200, "speed": 25},
                ],
                "tacan_channel": 57,
                "icls_channel": 4,
                "radio": 307,
                "link4": 339
            },
            "Illustrious": {
                "ship": dcs.ships.Hms_invincible,
                "position": {"x":96300 ,"y":-14200},
                "waypoints": [
                    {"x": 142200, "y": 93400, "speed": 25},
                    {"x": 139700, "y": 93400, "speed": 25},
                    {"x": 93800, "y": -14200, "speed": 25},
                ],
                "tacan_channel": 58,
                "radio": 308
            },
            "Nassau": {
                "ship": dcs.ships.LHA_Tarawa,
                "position": {"x":129400 ,"y":-24200},
                "waypoints": [
                    {"x": 131100, "y": -4700, "speed": 25},
                    {"x": 128600, "y": -4700, "speed": 25},
                    {"x": 126900, "y": -24200, "speed": 25},
                ],
                "tacan_channel": 59,
                "radio": 309
            },
            "Saipan": {
                "ship": dcs.ships.LHA_Tarawa,
                "position": {"x":133900 ,"y":-24700},
                "waypoints": [
                    {"x": 135700, "y": -4700, "speed": 25},
                    {"x": 133200, "y": -4700, "speed": 25},
                    {"x": 131400, "y": -24700, "speed": 25},
                ],
                "tacan_channel": 60,
                "radio": 310
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
                "start_type": dcs.mission.StartType.Warm,
                "airframes": [
                    { "airframe": dcs.planes.F_14B, "count": 4, "fuel": 1, "loadout": "Empty", "livery": "Santa", "properties": { dcs.planes.F_14B.Properties.INSAlignmentStored.id: True }  },
                    { "airframe": dcs.planes.FA_18C_hornet, "count": 4, "fuel": 1, "loadout": "Empty", "livery": "VX-31 CoNA" },
                ]
            },
            {
                "country": m.country(dcs.countries.CombinedJointTaskForcesBlue.name),
                "carrier": "Forrestal",
                "start_type": dcs.mission.StartType.Warm,
                "airframes": [
                    { "airframe": dcs.planes.F_14B, "count": 2, "fuel": 1, "loadout": "Empty", "livery": "Santa", "properties": { dcs.planes.F_14B.Properties.INSAlignmentStored.id: True } },
                    { "airframe": dcs.planes.FA_18C_hornet, "count": 2, "fuel": 1, "loadout": "Empty", "livery": "VX-31 CoNA" },
                ]
            },
            {
                "country": m.country(dcs.countries.CombinedJointTaskForcesBlue.name),
                "carrier": "Invincible",
                "start_type": dcs.mission.StartType.Warm,
                "airframes": [
                    { "airframe": dcs.planes.AV8BNA, "count": 3, "fuel": 1, "loadout": "Empty", "livery": "vma-214" },
                ]
            },
            {
                "country": m.country(dcs.countries.CombinedJointTaskForcesBlue.name),
                "carrier": "Tarawa",
                "start_type": dcs.mission.StartType.Warm,
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
                "start_type": dcs.mission.StartType.Warm,
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
                "start_type": dcs.mission.StartType.Warm,
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
            },
            {
                "country": m.country(dcs.countries.CombinedJointTaskForcesBlue.name),
                "farp": "FARP Morden Bog",
                "farp_zone": "FARP-2",
                "start_type": dcs.mission.StartType.Warm,
                "airframes": [
                    {
                        "airframe": dcs.helicopters.Mi_24P, "fuel": 0.6, "loadout": "Empty", "livery": "Ukrainian Army Aviation",
                        "positions": [{"heading": 182, "x": 134272.27649971, "y": -133813.2056198}, {"heading": 135, "x": 134243.25889365, "y": -133899.86630815}, {"heading": 141, "x": 134260.57265866, "y": -133874.50258982}, {"heading": 162, "x": 134270.70798046, "y": -133842.02716095}]
                    },
                    {
                        "airframe": dcs.helicopters.Mi_8MT, "fuel": 0.6, "loadout": "Empty", "livery": "Algerian AF Green EVSAN",
                        "positions": [{"heading": 72, "x": 134126.49333023, "y": -133932.2170176}, {"heading": 116, "x": 134220.57033098, "y": -133917.00187938}, {"heading": 119, "x": 134191.37724306, "y": -133927.48300303}, {"heading": 106, "x": 134160.89380915, "y": -133934.71238913}]
                    },
                    {
                        "airframe": dcs.helicopters.UH_1H, "fuel": 0.6, "loadout": "Empty", "livery": "US ARMY 1972",
                        "positions": [{"heading": 257, "x": 134146.07311127, "y": -133694.78477178}, {"heading": 247, "x": 134199.57900546, "y": -133702.20729606}, {"heading": 255, "x": 134183.60170744, "y": -133696.16863224}, {"heading": 251, "x": 134166.11474345, "y": -133694.53316079}]
                    },
                    {
                        "airframe": dcs.helicopters.AH_64D_BLK_II, "fuel": 0.6, "loadout": "Empty", "livery": "JGSDF——1st_Combat_Helicopter_Unit",
                        "positions": [{"heading": 30, "x": 134036.01828826, "y": -133859.12402073}, {"heading": 63, "x": 134098.7786646, "y": -133924.25678243}, {"heading": 45, "x": 134074.4668232, "y": -133908.44619777}, {"heading": 40, "x": 134051.3309574, "y": -133887.37697365}]
                    },
                    {
                        "airframe": dcs.helicopters.SA342L, "fuel": 0.6, "loadout": "Empty", "livery": "Tiger Meet 2",
                        "positions": [{"heading": 225, "x": 134250.31723026, "y": -133739.87734505}]
                    },
                    {
                        "airframe": dcs.helicopters.SA342M, "fuel": 0.6, "loadout": "Empty", "livery": "Tiger Meet",
                        "positions": [{"heading": 234, "x": 134234.23990799, "y": -133724.5842824}]
                    },
                    {
                        "airframe": dcs.helicopters.Ka_50_3, "fuel": 0.6, "loadout": "Empty", "livery": "Ka-50_desert_werewolf",
                        "positions": [{"heading": 208, "x": 134271.29617518, "y": -133782.22736469}, {"heading": 212, "x": 134262.27718951, "y": -133759.67990053}],
                        "properties": { dcs.helicopters.Ka_50_3.Properties.Realistic_INS.id: dcs.helicopters.Ka_50_3.Properties.Realistic_INS.Values.No_alignment_and_fixtaking_needed }
                    },
                ]
            },
            {
                "country": m.country(dcs.countries.CombinedJointTaskForcesBlue.name),
                "airport": m.terrain.airports["Stoney Cross"],
                "start_type": dcs.mission.StartType.Warm,
                "airframes": [
                    { "airframe": dcs.planes.A_10C_2, "count": 4, "parking": [21, 37, 39, 20], "fuel": 0.6, "loadout": "Empty", "livery": "355th fs eielson afb, alaska (ak)" },
                    { "airframe": dcs.planes.AJS37, "count": 2, "parking": [40, 19], "fuel": 1, "loadout": "Empty", "livery": "SF-37 Akktu Stakki - F21" },
                    { "airframe": dcs.planes.AV8BNA, "count": 2, "parking": [36, 38], "fuel": 1, "loadout": "Empty", "livery": "vma-214" },
                    { "airframe": dcs.planes.F_14B, "count": 4, "parking": [1, 7, 2, 9], "fuel": 1, "loadout": "Empty", "livery": "Santa", "properties": { dcs.planes.F_14B.Properties.INSAlignmentStored.id: True } },
                    { "airframe": dcs.planes.F_15ESE, "count": 4, "parking": [8, 24, 11, 10], "fuel": 1, "loadout": "Empty", "livery": "USAF 494th Panthers FS 91-603 75th D-Day Anniversary", "properties": { dcs.planes.F_15ESE.Properties.NetCrewControlPriority.id: dcs.planes.F_15ESE.Properties.NetCrewControlPriority.Values.Equally_Responsible } },
                    { "airframe": dcs.planes.F_16C_50, "count": 6, "parking": [22, 14, 13, 16, 28, 25], "fuel": 1, "loadout": "Empty", "livery": "18th AGRS Arctic Splinter" },
                    { "airframe": dcs.planes.FA_18C_hornet, "count": 4, "parking": [12, 17, 15, 0], "fuel": 1, "loadout": "Empty", "livery": "VX-31 CoNA" },
                    { "airframe": dcs.planes.JF_17, "count": 4, "parking": [27, 23, 26, 32], "fuel": 1, "loadout": "Empty", "livery": "PAF Black Panthers 07-101" },
                    { "airframe": dcs.planes.Mirage_F1EE, "count": 2, "parking": [30, 18], "fuel": 1, "loadout": "Empty", "livery": "USA AGGRESSOR Colour (CE)" },
                    { "airframe": dcs.planes.Su_25T, "count": 4, "parking": [41, 31, 42, 34], "fuel": 1, "loadout": "Empty", "livery": "Algerian AF Desert KU-03" },
                ]
            },
            {
                "country": m.country(dcs.countries.CombinedJointTaskForcesBlue.name),
                "airport": m.terrain.airports["Lymington"],
                "start_type": dcs.mission.StartType.Warm,
                "airframes": [
                    { "airframe": dcs.helicopters.AH_64D_BLK_II, "count": 4, "parking": [55, 56, 50, 48], "fuel": 0.6, "loadout": "Empty", "livery": "JGSDF——1st_Combat_Helicopter_Unit" },
                    { "airframe": dcs.helicopters.Ka_50_3, "count": 4, "parking": [49, 52, 51, 53], "fuel": 0.6, "loadout": "Empty", "livery": "Ka-50_desert_werewolf", "properties": { dcs.helicopters.Ka_50_3.Properties.Realistic_INS.id: dcs.helicopters.Ka_50_3.Properties.Realistic_INS.Values.No_alignment_and_fixtaking_needed } },
                    { "airframe": dcs.helicopters.Mi_24P, "count": 4, "parking": [4, 5, 6, 7], "fuel": 0.6, "loadout": "Empty", "livery": "Ukrainian Army Aviation" },
                    { "airframe": dcs.helicopters.Mi_8MT, "count": 4, "parking": [8, 9, 12, 10], "fuel": 0.6, "loadout": "Empty", "livery": "Algerian AF Green EVSAN" },
                    { "airframe": dcs.helicopters.SA342L, "count": 4, "parking": [11, 13, 14, 15], "fuel": 0.6, "loadout": "Empty", "livery": "Tiger Meet 2" },
                    { "airframe": dcs.helicopters.SA342M, "count": 4, "parking": [16, 17, 19, 18], "fuel": 0.6, "loadout": "Empty", "livery": "Tiger Meet" },
                    { "airframe": dcs.helicopters.UH_1H, "count": 4, "parking": [20, 23, 21, 22], "fuel": 0.6, "loadout": "Empty", "livery": "US ARMY 1972" },
                ]
            },
            {
                "country": m.country(dcs.countries.CombinedJointTaskForcesBlue.name),
                "airport": m.terrain.airports["Needs Oar Point"],
                "start_type": dcs.mission.StartType.Warm,
                "airframes": [
                    { "airframe": dcs.planes.A_10A, "count": 2, "parking": [26, 24], "fuel": 1, "loadout": "Empty", "livery": "355th fs eielson afb, alaska (ak)", "start_type": dcs.mission.StartType.Cold },
                    { "airframe": dcs.planes.C_101CC, "count": 2, "parking": [25, 27], "fuel": 1, "loadout": "Empty", "livery": "usaf agressor fictional" },
                    { "airframe": dcs.planes.F_5E_3, "count": 2, "parking": [28, 29], "fuel": 1, "loadout": "Empty", "livery": "BR FAB 4846" },
                    { "airframe": dcs.planes.F_86F_Sabre, "count": 2, "parking": [30, 32], "fuel": 1, "loadout": "Empty", "livery": "Royal Saudi Air Force" },
                    { "airframe": dcs.planes.L_39ZA, "count": 2, "parking": [31, 33], "fuel": 1, "loadout": "Empty", "livery": "algerian af tiger nl-36" },
                    { "airframe": dcs.planes.MB_339A, "count": 2, "parking": [34, 35], "fuel": 1, "loadout": "Empty", "livery": "MB339AN 'NIGERIA'" },
                    { "airframe": dcs.planes.MiG_19P, "count": 2, "parking": [42, 36], "fuel": 1, "loadout": "Empty", "livery": "DDR - Fictional" },
                    { "airframe": dcs.planes.P_51D_30_NA, "count": 2, "parking": [41, 37], "fuel": 1, "loadout": "Empty", "livery": "Ukraine Modern" },
                    { "airframe": dcs.planes.F_15C, "count": 2, "parking": [40, 38], "fuel": 1, "loadout": "Empty", "livery": "12th Fighter SQN (AK)", "start_type": dcs.mission.StartType.Cold },
                    { "airframe": dcs.planes.Su_25, "count": 2, "parking": [39, 43], "fuel": 1, "loadout": "Empty", "livery": "petal camo scheme #1 (native). 299th brigade", "start_type": dcs.mission.StartType.Cold },
                    { "airframe": dcs.planes.MiG_21Bis, "count": 2, "parking": [45, 44], "fuel": 1, "loadout": "Empty", "livery": "HuAF 31st AB (Turul Sqn)" },
                    { "airframe": dcs.planes.M_2000C, "count": 2, "parking": [46, 47], "fuel": 1, "loadout": "Empty", "livery": "2003 Tigermeet" },
                ]
            },
            {
                "country": m.country(dcs.countries.CombinedJointTaskForcesBlue.name),
                "carrier": "Abe",
                "start_type": dcs.mission.StartType.Warm,
                "airframes": [
                    { "airframe": dcs.planes.F_14B, "count": 4, "fuel": 1, "loadout": "Empty", "livery": "Santa", "properties": { dcs.planes.F_14B.Properties.INSAlignmentStored.id: True }  },
                    { "airframe": dcs.planes.FA_18C_hornet, "count": 4, "fuel": 1, "loadout": "Empty", "livery": "VX-31 CoNA" },
                ]
            },
            {
                "country": m.country(dcs.countries.CombinedJointTaskForcesBlue.name),
                "carrier": "Saratoga",
                "start_type": dcs.mission.StartType.Warm,
                "airframes": [
                    { "airframe": dcs.planes.F_14B, "count": 2, "fuel": 1, "loadout": "Empty", "livery": "Santa", "properties": { dcs.planes.F_14B.Properties.INSAlignmentStored.id: True } },
                    { "airframe": dcs.planes.FA_18C_hornet, "count": 2, "fuel": 1, "loadout": "Empty", "livery": "VX-31 CoNA" },
                ]
            },
            {
                "country": m.country(dcs.countries.CombinedJointTaskForcesBlue.name),
                "carrier": "Illustrious",
                "start_type": dcs.mission.StartType.Warm,
                "airframes": [
                    { "airframe": dcs.planes.AV8BNA, "count": 3, "fuel": 1, "loadout": "Empty", "livery": "vma-214" },
                ]
            },
            {
                "country": m.country(dcs.countries.CombinedJointTaskForcesBlue.name),
                "carrier": "Nassau",
                "start_type": dcs.mission.StartType.Warm,
                "airframes": [
                    { "airframe": dcs.helicopters.Mi_24P, "count": 3, "fuel": 0.6, "loadout": "Empty", "livery": "Ukrainian Army Aviation" },
                    { "airframe": dcs.helicopters.Mi_8MT, "count": 3, "fuel": 0.6, "loadout": "Empty", "livery": "Algerian AF Green EVSAN" },
                    { "airframe": dcs.helicopters.SA342L, "count": 1, "fuel": 0.6, "loadout": "Empty", "livery": "Tiger Meet 2" },
                    { "airframe": dcs.helicopters.SA342M, "count": 1, "fuel": 0.6, "loadout": "Empty", "livery": "Tiger Meet" },
                ]
            },
            {
                "country": m.country(dcs.countries.CombinedJointTaskForcesBlue.name),
                "carrier": "Saipan",
                "start_type": dcs.mission.StartType.Warm,
                "airframes": [
                    { "airframe": dcs.helicopters.UH_1H, "count": 3, "fuel": 0.6, "loadout": "Empty", "livery": "US ARMY 1972" },
                    { "airframe": dcs.helicopters.AH_64D_BLK_II, "count": 3, "fuel": 0.6, "loadout": "Empty", "livery": "JGSDF——1st_Combat_Helicopter_Unit" },
                    { "airframe": dcs.helicopters.Ka_50_3, "count": 2, "fuel": 0.6, "loadout": "Empty", "livery": "Ka-50_desert_werewolf", "properties": { dcs.helicopters.Ka_50_3.Properties.Realistic_INS.id: dcs.helicopters.Ka_50_3.Properties.Realistic_INS.Values.No_alignment_and_fixtaking_needed } },
                ]
            },
            {
                "country": m.country(dcs.countries.CombinedJointTaskForcesBlue.name),
                "farp": "FARP Timmy",
                "farp_zone": "FARP-3",
                "start_type": dcs.mission.StartType.Warm,
                "airframes": [
                    {
                        "airframe": dcs.helicopters.Mi_24P, "fuel": 0.6, "loadout": "Empty", "livery": "Ukrainian Army Aviation",
                        "positions": [{"heading": 135, "x": 225314.38913892, "y": 26864.114781482}, {"heading": 141, "x": 225331.70290393, "y": 26889.478499812}, {"heading": 162, "x": 225341.83822573, "y": 26921.953928682}, {"heading": 182, "x": 225343.40674498, "y": 26950.775469832}]
                    },
                    {
                        "airframe": dcs.helicopters.Mi_8MT, "fuel": 0.6, "loadout": "Empty", "livery": "Algerian AF Green EVSAN",
                        "positions": [{"heading": 116, "x": 225291.70057625, "y": 26846.979210252}, {"heading": 119, "x": 225262.50748833, "y": 26836.498086602}, {"heading": 106, "x": 225232.02405442, "y": 26829.268700502}, {"heading": 72, "x": 225197.6235755, "y": 26831.764072032}]
                    },
                    {
                        "airframe": dcs.helicopters.UH_1H, "fuel": 0.6, "loadout": "Empty", "livery": "US ARMY 1972",
                        "positions": [{"heading": 247, "x": 225270.70925073, "y": 27061.773793572}, {"heading": 255, "x": 225254.73195271, "y": 27067.812457392}, {"heading": 251, "x": 225237.24498872, "y": 27069.447928842}, {"heading": 257, "x": 225217.20335654, "y": 27069.196317852}]
                    },
                    {
                        "airframe": dcs.helicopters.AH_64D_BLK_II, "fuel": 0.6, "loadout": "Empty", "livery": "JGSDF——1st_Combat_Helicopter_Unit",
                        "positions": [{"heading": 63, "x": 225169.90890987, "y": 26839.724307202}, {"heading": 45, "x": 225145.59706847, "y": 26855.534891862}, {"heading": 40, "x": 225122.46120267, "y": 26876.604115982}, {"heading": 30, "x": 225107.14853353, "y": 26904.857068902}]
                    },
                    {
                        "airframe": dcs.helicopters.SA342L, "fuel": 0.6, "loadout": "Empty", "livery": "Tiger Meet 2",
                        "positions": [{"heading": 225, "x": 225321.44747553, "y": 27024.103744582}]
                    },
                    {
                        "airframe": dcs.helicopters.SA342M, "fuel": 0.6, "loadout": "Empty", "livery": "Tiger Meet",
                        "positions": [{"heading": 234, "x": 225305.37015326, "y": 27039.396807232}]
                    },
                    {
                        "airframe": dcs.helicopters.Ka_50_3, "fuel": 0.6, "loadout": "Empty", "livery": "Ka-50_desert_werewolf",
                        "positions": [{"heading": 208, "x": 225342.42642045, "y": 26981.753724942}, {"heading": 212, "x": 225333.40743478, "y": 27004.301189102}],
                        "properties": { dcs.helicopters.Ka_50_3.Properties.Realistic_INS.id: dcs.helicopters.Ka_50_3.Properties.Realistic_INS.Values.No_alignment_and_fixtaking_needed }
                    },
                ]
            },
            {
                "country": m.country(dcs.countries.CombinedJointTaskForcesBlue.name),
                "farp": "FARP Bewl Water",
                "farp_zone": "FARP-4",
                "start_type": dcs.mission.StartType.Warm,
                "airframes": [
                    {
                        "airframe": dcs.helicopters.Mi_24P, "fuel": 0.6, "loadout": "Empty", "livery": "Ukrainian Army Aviation",
                        "positions": [{"heading": 141, "x": 177971.08504576, "y": 42545.814319969}, {"heading": 135, "x": 177953.77128075, "y": 42520.450601639}, {"heading": 182, "x": 177982.78888681, "y": 42607.111289989}, {"heading": 162, "x": 177981.22036756, "y": 42578.289748839}]
                    },
                    {
                        "airframe": dcs.helicopters.Mi_8MT, "fuel": 0.6, "loadout": "Empty", "livery": "Algerian AF Green EVSAN",
                        "positions": [{"heading": 119, "x": 177901.88963016, "y": 42492.833906759}, {"heading": 72, "x": 177837.00571733, "y": 42488.099892189}, {"heading": 116, "x": 177931.08271808, "y": 42503.315030409}, {"heading": 106, "x": 177871.40619625, "y": 42485.604520659}]
                    },
                    {
                        "airframe": dcs.helicopters.UH_1H, "fuel": 0.6, "loadout": "Empty", "livery": "US ARMY 1972",
                        "positions": [{"heading": 255, "x": 177894.11409454, "y": 42724.148277549}, {"heading": 247, "x": 177910.09139256, "y": 42718.109613729}, {"heading": 251, "x": 177876.62713055, "y": 42725.783748999}, {"heading": 257, "x": 177856.58549837, "y": 42725.532138009}]
                    },
                    {
                        "airframe": dcs.helicopters.AH_64D_BLK_II, "fuel": 0.6, "loadout": "Empty", "livery": "JGSDF——1st_Combat_Helicopter_Unit",
                        "positions": [{"heading": 45, "x": 177784.9792103, "y": 42511.870712019}, {"heading": 40, "x": 177761.8433445, "y": 42532.939936139}, {"heading": 30, "x": 177746.53067536, "y": 42561.192889059}, {"heading": 63, "x": 177809.2910517, "y": 42496.060127359}]
                    },
                    {
                        "airframe": dcs.helicopters.SA342L, "fuel": 0.6, "loadout": "Empty", "livery": "Tiger Meet 2",
                        "positions": [{"heading": 225, "x": 177960.82961736, "y": 42680.439564739}]
                    },
                    {
                        "airframe": dcs.helicopters.SA342M, "fuel": 0.6, "loadout": "Empty", "livery": "Tiger Meet",
                        "positions": [{"heading": 234, "x": 177944.75229509, "y": 42695.732627389}]
                    },
                    {
                        "airframe": dcs.helicopters.Ka_50_3, "fuel": 0.6, "loadout": "Empty", "livery": "Ka-50_desert_werewolf",
                        "positions": [{"heading": 208, "x": 177981.80856228, "y": 42638.089545099}, {"heading": 212, "x": 177972.78957661, "y": 42660.637009259}],
                        "properties": { dcs.helicopters.Ka_50_3.Properties.Realistic_INS.id: dcs.helicopters.Ka_50_3.Properties.Realistic_INS.Values.No_alignment_and_fixtaking_needed }
                    },
                ]
            },
            {
                "country": m.country(dcs.countries.CombinedJointTaskForcesBlue.name),
                "roadbase": "ROADBASE Send It",
                "roadbase_zone": "ROADBASE-1",
                "start_type": dcs.mission.StartType.Warm,
                "airframes": [
                    { 
                        "airframe": dcs.planes.A_10C_2, "fuel": 0.6, "loadout": "Empty", "livery": "355th fs eielson afb, alaska (ak)",
                        "positions": [{"heading": 211, "x": 127490.33400494, "y": -168766.15351086}, {"heading": 211, "x": 127509.4216532, "y": -168754.48007308}]
                    },
                    { 
                        "airframe": dcs.planes.AJS37, "fuel": 1, "loadout": "Empty", "livery": "SF-37 Akktu Stakki - F21",
                        "positions": [{"heading": 211, "x": 127528.14796083, "y": -168742.03988248}]
                    },
                    { 
                        "airframe": dcs.planes.F_16C_50, "fuel": 1, "loadout": "Empty", "livery": "18th AGRS Arctic Splinter",
                        "positions": [{"heading": 218, "x": 127382.21199551, "y": -168832.95995519}, {"heading": 213, "x": 127401.20573, "y": -168821.52346574}, {"heading": 211, "x": 127419.18913415, "y": -168810.16552627}, {"heading": 211, "x": 127437.96128409, "y": -168798.64983765}, {"heading": 211, "x": 127456.41793572, "y": -168787.29189819}, {"heading": 211, "x": 127473.92809239, "y": -168776.56495537}],
                        "waypoints": [{"x": 127850.86824241467, "y": -169993.8939761349}]
                    },
                    { 
                        "airframe": dcs.planes.F_15ESE, "fuel": 1, "loadout": "Empty", "livery": "USAF 494th Panthers FS 91-603 75th D-Day Anniversary", "properties": { dcs.planes.F_15ESE.Properties.NetCrewControlPriority.id: dcs.planes.F_15ESE.Properties.NetCrewControlPriority.Values.Equally_Responsible },
                        "positions": [{"heading": 211, "x": 127545.3005247, "y": -168731.35467876}, {"heading": 211, "x": 127564, "y": -168716}]
                    },
                ]
            },
            {
                "country": m.country(dcs.countries.CombinedJointTaskForcesBlue.name),
                "roadbase": "ROADBASE Watch This",
                "roadbase_zone": "ROADBASE-2",
                "start_type": dcs.mission.StartType.Warm,
                "airframes": [
                    { 
                        "airframe": dcs.planes.A_10C_2, "fuel": 0.6, "loadout": "Empty", "livery": "355th fs eielson afb, alaska (ak)",
                        "positions": [{"heading": 204, "x": 172966.33826149, "y": 75162.49934103}, {"heading": 204, "x": 172984.84658479, "y": 75169.461995988}]
                    },
                    { 
                        "airframe": dcs.planes.F_16C_50, "fuel": 1, "loadout": "Empty", "livery": "18th AGRS Arctic Splinter",
                        "positions": [{"heading": 224, "x": 172906.31841306, "y": 75119.930197431}, {"heading": 224, "x": 172919.80304861, "y": 75132.709753998}, {"heading": 212, "x": 172933.99276314, "y": 75144.167287472}, {"heading": 204, "x": 172948.97569153, "y": 75154.743472217}]
                    },
                    { 
                        "airframe": dcs.planes.F_15ESE, "fuel": 1, "loadout": "Empty", "livery": "USAF 494th Panthers FS 91-603 75th D-Day Anniversary", "properties": { dcs.planes.F_15ESE.Properties.NetCrewControlPriority.id: dcs.planes.F_15ESE.Properties.NetCrewControlPriority.Values.Equally_Responsible },
                        "positions": [{"heading": 198, "x": 173007.16297902, "y": 75177.49832118}, {"heading": 205, "x": 173027.18632185, "y": 75186.670304026}]
                    },
                ]
            },
            {
                "country": m.country(dcs.countries.CombinedJointTaskForcesBlue.name),
                "farp": "FARP Bluebird",
                "farp_zone": "FARP-5",
                "start_type": dcs.mission.StartType.Warm,
                "airframes": [
                    {
                        "airframe": dcs.helicopters.Mi_24P, "fuel": 0.6, "loadout": "Empty", "livery": "Ukrainian Army Aviation",
                        "positions": [{"heading": 182, "x": 182952.41382148, "y": 98497.198602195}, {"heading": 141, "x": 182940.70998043, "y": 98435.901632175}, {"heading": 135, "x": 182923.39621542, "y": 98410.537913845}, {"heading": 162, "x": 182950.84530223, "y": 98468.377061045}]
                    },
                    {
                        "airframe": dcs.helicopters.Mi_8MT, "fuel": 0.6, "loadout": "Empty", "livery": "Algerian AF Green EVSAN",
                        "positions": [{"heading": 72, "x": 182806.630652, "y": 98378.187204395}, {"heading": 116, "x": 182900.70765275, "y": 98393.402342615}, {"heading": 119, "x": 182871.51456483, "y": 98382.921218965}, {"heading": 106, "x": 182841.03113092, "y": 98375.691832865}]
                    },
                    {
                        "airframe": dcs.helicopters.UH_1H, "fuel": 0.6, "loadout": "Empty", "livery": "US ARMY 1972",
                        "positions": [{"heading": 257, "x": 182826.21043304, "y": 98615.619450215}, {"heading": 251, "x": 182846.25206522, "y": 98615.871061205}, {"heading": 247, "x": 182879.71632723, "y": 98608.196925935}, {"heading": 255, "x": 182863.73902921, "y": 98614.235589755}]
                    },
                    {
                        "airframe": dcs.helicopters.AH_64D_BLK_II, "fuel": 0.6, "loadout": "Empty", "livery": "JGSDF——1st_Combat_Helicopter_Unit",
                        "positions": [{"heading": 30, "x": 182716.15561003, "y": 98451.280201265}, {"heading": 45, "x": 182754.60414497, "y": 98401.958024225}, {"heading": 40, "x": 182731.46827917, "y": 98423.027248345}, {"heading": 63, "x": 182778.91598637, "y": 98386.147439565}]
                    },
                    {
                        "airframe": dcs.helicopters.SA342L, "fuel": 0.6, "loadout": "Empty", "livery": "Tiger Meet 2",
                        "positions": [{"heading": 225, "x": 182930.45455203, "y": 98570.526876945}]
                    },
                    {
                        "airframe": dcs.helicopters.SA342M, "fuel": 0.6, "loadout": "Empty", "livery": "Tiger Meet",
                        "positions": [{"heading": 234, "x": 182914.37722976, "y": 98585.819939595}]
                    },
                    {
                        "airframe": dcs.helicopters.Ka_50_3, "fuel": 0.6, "loadout": "Empty", "livery": "Ka-50_desert_werewolf",
                        "positions": [{"heading": 212, "x": 182942.41451128, "y": 98550.724321465}, {"heading": 208, "x": 182951.43349695, "y": 98528.176857305}],
                        "properties": { dcs.helicopters.Ka_50_3.Properties.Realistic_INS.id: dcs.helicopters.Ka_50_3.Properties.Realistic_INS.Values.No_alignment_and_fixtaking_needed }
                    },
                ]
            },
            {
                "country": m.country(dcs.countries.CombinedJointTaskForcesBlue.name),
                "roadbase": "ROADBASE Hold My Beer",
                "roadbase_zone": "ROADBASE-3",
                "start_type": dcs.mission.StartType.Warm,
                "airframes": [
                    { 
                        "airframe": dcs.planes.A_10C_2, "fuel": 0.6, "loadout": "Empty", "livery": "355th fs eielson afb, alaska (ak)",
                        "positions": [{"heading": 111, "x": 160587.59171745, "y": 146183.1854019}, {"heading": 118, "x": 160575.10929448, "y": 146208.83370479}]
                    },
                    { 
                        "airframe": dcs.planes.AV8BNA, "fuel": 1, "loadout": "Empty", "livery": "355th fs eielson afb, alaska (ak)",
                        "positions": [{"heading": 126, "x": 160620.67236022, "y": 146108.81733247}, {"heading": 126, "x": 160631.19011748, "y": 146090.81396419}, {"heading": 126, "x": 160642.4659113, "y": 146073.28436876}]
                    },
                    { 
                        "airframe": dcs.planes.F_16C_50, "fuel": 1, "loadout": "Empty", "livery": "18th AGRS Arctic Splinter",
                        "positions": [{"heading": 294, "x": 160530.45132613, "y": 146284.61167889}, {"heading": 289, "x": 160516.13887338, "y": 146315.91591161}, {"heading": 305, "x": 160549.19157798, "y": 146248.87445442}, {"heading": 292, "x": 160507.31884031, "y": 146335.59517102}, {"heading": 298, "x": 160539.31299561, "y": 146266.45252012}, {"heading": 296, "x": 160498.6407579, "y": 146355.57113429}]
                    },
                    { 
                        "airframe": dcs.planes.F_15ESE, "fuel": 1, "loadout": "Empty", "livery": "USAF 494th Panthers FS 91-603 75th D-Day Anniversary", "properties": { dcs.planes.F_15ESE.Properties.NetCrewControlPriority.id: dcs.planes.F_15ESE.Properties.NetCrewControlPriority.Values.Equally_Responsible },
                        "positions": [{"heading": 111, "x": 160597.03326698, "y": 146157.62413366}, {"heading": 112, "x": 160608.08678838, "y": 146133.44455559}]
                    },
                ]
            },
            {
                "country": m.country(dcs.countries.CombinedJointTaskForcesBlue.name),
                "farp": "FARP Guines",
                "farp_zone": "FARP-6",
                "start_type": dcs.mission.StartType.Warm,
                "airframes": [
                    {
                        "airframe": dcs.helicopters.Mi_24P, "fuel": 0.6, "loadout": "Empty", "livery": "Ukrainian Army Aviation",
                        "positions": [{"heading": 135, "x": 160297.63757879, "y": 146319.14918679}, {"heading": 162, "x": 160325.0866656, "y": 146376.98833399}, {"heading": 182, "x": 160326.65518485, "y": 146405.80987514}, {"heading": 141, "x": 160314.9513438, "y": 146344.51290512}]
                    },
                    {
                        "airframe": dcs.helicopters.Mi_8MT, "fuel": 0.6, "loadout": "Empty", "livery": "Algerian AF Green EVSAN",
                        "positions": [{"heading": 119, "x": 160245.7559282, "y": 146291.53249191}, {"heading": 106, "x": 160215.27249429, "y": 146284.30310581}, {"heading": 72, "x": 160180.87201537, "y": 146286.79847734}, {"heading": 116, "x": 160274.94901612, "y": 146302.01361556}], "SA342L": [{"heading": 225, "x": 160304.6959154, "y": 146479.13814989}]
                    },
                    {
                        "airframe": dcs.helicopters.UH_1H, "fuel": 0.6, "loadout": "Empty", "livery": "US ARMY 1972",
                        "positions": [{"heading": 247, "x": 160253.9576906, "y": 146516.80819888}, {"heading": 255, "x": 160236.43630341, "y": 146522.5334687}, {"heading": 257, "x": 160200.45179641, "y": 146524.23072316}, {"heading": 251, "x": 160219.74055521, "y": 146524.73027767}]
                    },
                    {
                        "airframe": dcs.helicopters.AH_64D_BLK_II, "fuel": 0.6, "loadout": "Empty", "livery": "JGSDF——1st_Combat_Helicopter_Unit",
                        "positions": [{"heading": 40, "x": 160105.70964254, "y": 146331.63852129}, {"heading": 30, "x": 160090.3969734, "y": 146359.89147421}, {"heading": 63, "x": 160153.15734974, "y": 146294.75871251}, {"heading": 45, "x": 160128.84550834, "y": 146310.56929717}]
                    },
                    {
                        "airframe": dcs.helicopters.SA342L, "fuel": 0.6, "loadout": "Empty", "livery": "Tiger Meet 2",
                        "positions": [{"heading": 225, "x": 160304.6959154, "y": 146479.13814989}]
                    },
                    {
                        "airframe": dcs.helicopters.SA342M, "fuel": 0.6, "loadout": "Empty", "livery": "Tiger Meet",
                        "positions": [{"heading": 234, "x": 160288.61859313, "y": 146494.43121254}]
                    },
                    {
                        "airframe": dcs.helicopters.Ka_50_3, "fuel": 0.6, "loadout": "Empty", "livery": "Ka-50_desert_werewolf",
                        "positions": [{"heading": 212, "x": 160316.65587465, "y": 146459.33559441}, {"heading": 208, "x": 160325.67486032, "y": 146436.78813025}],
                        "properties": { dcs.helicopters.Ka_50_3.Properties.Realistic_INS.id: dcs.helicopters.Ka_50_3.Properties.Realistic_INS.Values.No_alignment_and_fixtaking_needed }
                    },
                ]
            },
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
            dcs.planes.F_15ESE: ["uhf", "vhf_am"],
            dcs.planes.F_16C_50: ["uhf", "vhf_am"],
            dcs.planes.JF_17: ["uhf"],
            dcs.planes.F_15C: ["uhf"],
        }

        if not edit:
            airport_set[0]["airframes"].append({ "airframe": pydcs_extensions.A_4E_C, "count": 4, "loadout": "Empty", "livery": "Aggressor USN VF-126 Bandits" })
            airport_set[1]["airframes"].append({ "airframe": pydcs_extensions.A_4E_C, "count": 4, "loadout": "Empty", "livery": "Aggressor USN VF-126 Bandits" })
            airport_set[9]["airframes"].append({ "airframe": pydcs_extensions.A_4E_C, "count": 4, "parking": [45, 44, 46, 47], "loadout": "Empty", "livery": "Aggressor USN VF-126 Bandits" })
            airport_set[10]["airframes"].append({ "airframe": pydcs_extensions.A_4E_C, "count": 4, "parking": [45, 44, 46, 47], "loadout": "Empty", "livery": "Aggressor USN VF-126 Bandits" })
            airport_set[11]["airframes"].append({ "airframe": pydcs_extensions.A_4E_C, "count": 4, "parking": [45, 44, 46, 47], "loadout": "Empty", "livery": "Aggressor USN VF-126 Bandits" })

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
                    # "1GW-Evreux-1": {
                    #     "airframe": dcs.planes.JF_17,
                    #     "groupSize": 2,
                    #     "initialInventory": 2,
                    #     "livery": "PLAAF 125th AB (Fictional)",
                    #     "loadouts": {
                    #         "PL-5Ex2, 2*SD-10x2, 800L Tank": "{ AUFTRAG.Type.CAP, AUFTRAG.Type.INTERCEPT }"
                    #     },
                    #     "capabilities": {
                    #         "AUFTRAG.Type.CAP": 50,
                    #         "AUFTRAG.Type.INTERCEPT": 50,
                    #         "AUFTRAG.Type.ESCORT": 50,
                    #     }
                    # },
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
            # "1st Goon Wing - Conches": {
            #     "airbase": "Conches",
            #     "warehouse": "Conches Airwing Warehouse#00001",
            #     "squadrons": {
            #         "1GW-Conches-1": {
            #             "airframe": dcs.planes.JF_17,
            #             "groupSize": 2,
            #             "initialInventory": 2,
            #             "livery": "PLAAF 125th AB (Fictional)",
            #             "loadouts": {
            #                 "PL-5Ex2, 2*SD-10x2, 800L Tank": "{ AUFTRAG.Type.CAP, AUFTRAG.Type.INTERCEPT }"
            #             },
            #             "capabilities": {
            #                 "AUFTRAG.Type.CAP": 50,
            #                 "AUFTRAG.Type.INTERCEPT": 50,
            #                 "AUFTRAG.Type.ESCORT": 50
            #             }
            #         },
            #     }
            # },
            "Stoney Cross": {
                "airbase": "Stoney Cross",
                "warehouse": "Stoney Cross Airwing Warehouse#00001",
                "squadrons": {
                    "Stoney Cross 1": {
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
                    "Stoney Cross 2": {
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
                    }
                }
            },
            "Lymington": {
                "airbase": "Lymington",
                "warehouse": "Lymington Airwing Warehouse#00001",
                "squadrons": {
                    "Lymington 1": {
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
                            "AUFTRAG.Type.BAI": 40,
                            "AUFTRAG.Type.CAS": 40,
                            "AUFTRAG.Type.BOMBCARPET": 40,
                            "AUFTRAG.Type.CASENHANCED": 40
                        }
                    },
                    "Lymington 2": {
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
                    }
                }
            },
            "Needs Oar Point": {
                "airbase": "Needs Oar Point",
                "warehouse": "Needs Oar Point Airwing Warehouse#00001",
                "squadrons": {
                    "Needs Oar Point 1": {
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
                            "AUFTRAG.Type.BAI": 40,
                            "AUFTRAG.Type.CAS": 40,
                            "AUFTRAG.Type.BOMBCARPET": 40,
                            "AUFTRAG.Type.CASENHANCED": 40
                        }
                    },
                    "Needs Oar Point 2": {
                        "airframe": dcs.planes.Su_25TM,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "Flight Research Institute  VVS",
                        "loadouts": {
                            "Kh-58*2,Kh-25MPU*4,R-73*2,ECM": "{ AUFTRAG.Type.SEAD }",
                            "APU-8 Vikhr-M*2,R-60M*2,R-73*2,SPPU-22*2,Mercury LLTV Pod": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.CASENHANCED }",
                            "FAB-500*6,R-60M*2,Fuel*2": "{ AUFTRAG.Type.BOMBCARPET }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.BOMBCARPET": 50,
                            "AUFTRAG.Type.CASENHANCED": 50,
                            "AUFTRAG.Type.SEAD": 50
                        }
                    }
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
                        "takeoffCold": "true",
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
                            "GoonsSuck": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.CASENHANCED }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.CASENHANCED": 50
                        }
                    },
                }
            },
            "FOB Yes Minister": {
                "airbase": "FOB Yes Minister Farp#00001",
                "warehouse": "FOB Yes Minister Airwing Warehouse#00001",
                "squadrons": {
                    "Yes Minister 1": {
                        "airframe": dcs.helicopters.Mi_26,
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
                    "Yes Minister 2": {
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
                }
            },
            "FOB Murray": {
                "airbase": "FOB Murray Farp#00001",
                "warehouse": "FOB Murray Airwing Warehouse#00001",
                "squadrons": {
                    "Murray 1": {
                        "airframe": dcs.helicopters.Mi_26,
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
                    "Murray 2": {
                        "airframe": dcs.helicopters.Mi_28N,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "night",
                        "loadouts": {
                            "16x9M114, 40xS-8": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.CASENHANCED }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.CASENHANCED": 50
                        }
                    },
                }
            },
            "FOB Smith": {
                "airbase": "FOB Smith Farp#00001",
                "warehouse": "FOB Smith Airwing Warehouse#00001",
                "squadrons": {
                    "Smith 1": {
                        "airframe": dcs.helicopters.Mi_26,
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
                    "Smith 2": {
                        "airframe": dcs.helicopters.Ka_50_3,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "Ka-50_standart_black_RussianAirForce",
                        "loadouts": {
                            "12x9A4172, 40xS-13, 4xIgla": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.CASENHANCED }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.CASENHANCED": 50
                        }
                    },
                }
            },
            "Funtington": {
                "airbase": "Funtington",
                "warehouse": "Funtington Airwing Warehouse#00001",
                "squadrons": {
                    "Funtington 1": {
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
                            "AUFTRAG.Type.BAI": 40,
                            "AUFTRAG.Type.CAS": 40,
                            "AUFTRAG.Type.BOMBCARPET": 40,
                            "AUFTRAG.Type.CASENHANCED": 40
                        }
                    },
                    "Funtington 2": {
                        "airframe": dcs.planes.Su_25TM,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "Flight Research Institute  VVS",
                        "loadouts": {
                            "Kh-58*2,Kh-25MPU*4,R-73*2,ECM": "{ AUFTRAG.Type.SEAD }",
                            "APU-8 Vikhr-M*2,R-60M*2,R-73*2,SPPU-22*2,Mercury LLTV Pod": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.CASENHANCED }",
                            "FAB-500*6,R-60M*2,Fuel*2": "{ AUFTRAG.Type.BOMBCARPET }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.BOMBCARPET": 50,
                            "AUFTRAG.Type.CASENHANCED": 50,
                            "AUFTRAG.Type.SEAD": 50
                        }
                    }
                }
            },
            "Tangmere": {
                "airbase": "Tangmere",
                "warehouse": "Tangmere Airwing Warehouse#00001",
                "squadrons": {
                    "Tangmere 1": {
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
                    "Tangmere 2": {
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
                    }
                }
            },
            "Ford": {
                "airbase": "Ford",
                "warehouse": "Ford Airwing Warehouse#00001",
                "squadrons": {
                    "Ford 1": {
                        "airframe": dcs.planes.Su_27,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "Lypetsk AFB (Shark)",
                        "loadouts": {
                            "R-73*4,R-27ER*4,R-27ET*2": "{ AUFTRAG.Type.CAP, AUFTRAG.Type.INTERCEPT, AUFTRAG.Type.ESCORT }",
                            "FAB-500*6,R-73*2,ECM": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.BOMBCARPET, AUFTRAG.Type.CASENHANCED }"
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
                    "Ford 2": {
                        "airframe": dcs.planes.MiG_29A,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "Strizhi (W)",
                        "loadouts": {
                            "R-73*2,R-60M*2,R-27R*2,Fuel-1500": "{ AUFTRAG.Type.CAP, AUFTRAG.Type.INTERCEPT, AUFTRAG.Type.ESCORT }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.CAP": 50,
                            "AUFTRAG.Type.INTERCEPT": 50,
                            "AUFTRAG.Type.ESCORT": 50,
                        }
                    }
                }
            },
            "West Malling": {
                "airbase": "West Malling",
                "warehouse": "West Malling Airwing Warehouse#00001",
                "squadrons": {
                    "West Malling 1": {
                        "airframe": dcs.planes.Su_27,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "Lypetsk AFB (Shark)",
                        "loadouts": {
                            "R-73*4,R-27ER*4,R-27ET*2": "{ AUFTRAG.Type.CAP, AUFTRAG.Type.INTERCEPT, AUFTRAG.Type.ESCORT }",
                            "FAB-500*6,R-73*2,ECM": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.BOMBCARPET, AUFTRAG.Type.CASENHANCED }"
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
                    "West Malling 2": {
                        "airframe": dcs.planes.MiG_29A,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "Strizhi (W)",
                        "loadouts": {
                            "R-73*2,R-60M*2,R-27R*2,Fuel-1500": "{ AUFTRAG.Type.CAP, AUFTRAG.Type.INTERCEPT, AUFTRAG.Type.ESCORT }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.CAP": 60,
                            "AUFTRAG.Type.INTERCEPT": 50,
                            "AUFTRAG.Type.ESCORT": 50,
                        }
                    },
                    "West Malling 3": {
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
                    "West Malling 4": {
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
                            "AUFTRAG.Type.CAP": 40,
                            "AUFTRAG.Type.INTERCEPT": 50,
                            "AUFTRAG.Type.ESCORT": 50,
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.BOMBCARPET": 50,
                            "AUFTRAG.Type.SEAD": 50,
                            "AUFTRAG.Type.CASENHANCED": 50
                        }
                    },
                    "West Malling 5": {
                        "airframe": dcs.planes.Su_25TM,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "Flight Research Institute  VVS",
                        "loadouts": {
                            "Kh-58*2,Kh-25MPU*4,R-73*2,ECM": "{ AUFTRAG.Type.SEAD }",
                            "APU-8 Vikhr-M*2,R-60M*2,R-73*2,SPPU-22*2,Mercury LLTV Pod": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.CASENHANCED }",
                            "FAB-500*6,R-60M*2,Fuel*2": "{ AUFTRAG.Type.BOMBCARPET }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.BOMBCARPET": 50,
                            "AUFTRAG.Type.CASENHANCED": 50,
                            "AUFTRAG.Type.SEAD": 50
                        }
                    }
                }
            },
            "Chailey": {
                "airbase": "Chailey",
                "warehouse": "Chailey Airwing Warehouse#00001",
                "squadrons": {
                    "Chailey 1": {
                        "airframe": dcs.planes.Su_27,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "Lypetsk AFB (Shark)",
                        "loadouts": {
                            "R-73*4,R-27ER*4,R-27ET*2": "{ AUFTRAG.Type.CAP, AUFTRAG.Type.INTERCEPT, AUFTRAG.Type.ESCORT }",
                            "FAB-500*6,R-73*2,ECM": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.BOMBCARPET, AUFTRAG.Type.CASENHANCED }"
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
                    "Chailey 2": {
                        "airframe": dcs.planes.MiG_29A,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "Strizhi (W)",
                        "loadouts": {
                            "R-73*2,R-60M*2,R-27R*2,Fuel-1500": "{ AUFTRAG.Type.CAP, AUFTRAG.Type.INTERCEPT, AUFTRAG.Type.ESCORT }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.CAP": 60,
                            "AUFTRAG.Type.INTERCEPT": 50,
                            "AUFTRAG.Type.ESCORT": 50,
                        }
                    },
                    "Chailey 3": {
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
                    "Chailey 4": {
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
                            "AUFTRAG.Type.CAP": 40,
                            "AUFTRAG.Type.INTERCEPT": 50,
                            "AUFTRAG.Type.ESCORT": 50,
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.BOMBCARPET": 50,
                            "AUFTRAG.Type.SEAD": 50,
                            "AUFTRAG.Type.CASENHANCED": 50
                        }
                    },
                    "Chailey 5": {
                        "airframe": dcs.planes.Su_25TM,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "Flight Research Institute  VVS",
                        "loadouts": {
                            "Kh-58*2,Kh-25MPU*4,R-73*2,ECM": "{ AUFTRAG.Type.SEAD }",
                            "APU-8 Vikhr-M*2,R-60M*2,R-73*2,SPPU-22*2,Mercury LLTV Pod": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.CASENHANCED }",
                            "FAB-500*6,R-60M*2,Fuel*2": "{ AUFTRAG.Type.BOMBCARPET }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.BOMBCARPET": 50,
                            "AUFTRAG.Type.CASENHANCED": 50,
                            "AUFTRAG.Type.SEAD": 50
                        }
                    }
                }
            },
            "FOB Bo'ohw'o'wo'er": {
                "airbase": "FOB Bo'ohw'o'wo'er Farp#00001",
                "warehouse": "FOB Bo'ohw'o'wo'er Airwing Warehouse#00001",
                "squadrons": {
                    "Bo'ohw'o'wo'er 1": {
                        "airframe": dcs.helicopters.Mi_26,
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
                    "Bo'ohw'o'wo'er 2": {
                        "airframe": dcs.helicopters.Mi_28N,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "night",
                        "loadouts": {
                            "16x9M114, 40xS-8": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.CASENHANCED }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.CASENHANCED": 50
                        }
                    },
                }
            },
            "FOB Innit": {
                "airbase": "FOB Innit Farp#00001",
                "warehouse": "FOB Innit Airwing Warehouse#00001",
                "squadrons": {
                    "Innit 1": {
                        "airframe": dcs.helicopters.Mi_26,
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
                    "Innit 2": {
                        "airframe": dcs.helicopters.Ka_50_3,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "Ka-50_standart_black_RussianAirForce",
                        "loadouts": {
                            "12x9A4172, 40xS-13, 4xIgla": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.CASENHANCED }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.CASENHANCED": 50
                        }
                    },
                }
            },
            "Kuz": {
                "airbase": "RED RG Kuznetsov Unit #1",
                "warehouse": "RED RG Kuznetsov Unit #1",
                "squadrons": {
                    "Kuz 1": {
                        "airframe": dcs.planes.Su_33,
                        "groupSize": 2,
                        "initialInventory": 2,
                        "livery": "279th kiap 1st squad navy",
                        "loadouts": {
                            "R-73*4,R-27ET*2,R-27ER*6": "{ AUFTRAG.Type.CAP, AUFTRAG.Type.INTERCEPT, AUFTRAG.Type.ESCORT }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.CAP": 50,
                            "AUFTRAG.Type.INTERCEPT": 50,
                            "AUFTRAG.Type.ESCORT": 50
                        }
                    },
                    "Kuz 2": {
                        "airframe": dcs.helicopters.Ka_27,
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
                    }
                }
            },
            "Amiens-Glisy Alpha": {
                "airbase": "Amiens-Glisy",
                "warehouse": "Amiens-Glisy Airwing Warehouse-1#00001",
                "squadrons": {
                    "Amiens-Glisy Alpha 1": {
                        "airframe": dcs.planes.JF_17,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "PLAAF 125th AB (Fictional)",
                        "loadouts": {
                            "PL-5Ex2, 2*SD-10x2, 1100L Tankx2, 800L Tank": "{ AUFTRAG.Type.CAP, AUFTRAG.Type.INTERCEPT, AUFTRAG.Type.ESCORT }",
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
                    "Amiens-Glisy Alpha 2": {
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
                    }
                }
            },
            "Amiens-Glisy Beta": {
                "airbase": "Amiens-Glisy",
                "warehouse": "Amiens-Glisy Airwing Warehouse-2#00001",
                "squadrons": {
                    "Amiens-Glisy Beta 1": {
                        "airframe": dcs.planes.JF_17,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "PLAAF 125th AB (Fictional)",
                        "loadouts": {
                            "PL-5Ex2, 2*SD-10x2, 1100L Tankx2, 800L Tank": "{ AUFTRAG.Type.CAP, AUFTRAG.Type.INTERCEPT, AUFTRAG.Type.ESCORT }",
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
                    "Amiens-Glisy Beta 2": {
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
                    }
                }
            },
            "Amiens-Glisy Gamma": {
                "airbase": "Amiens-Glisy",
                "warehouse": "Amiens-Glisy Airwing Warehouse-3#00001",
                "squadrons": {
                    "Amiens-Glisy Gamma 1": {
                        "airframe": dcs.planes.JF_17,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "PLAAF 125th AB (Fictional)",
                        "loadouts": {
                            "PL-5Ex2, 2*SD-10x2, 1100L Tankx2, 800L Tank": "{ AUFTRAG.Type.CAP, AUFTRAG.Type.INTERCEPT, AUFTRAG.Type.ESCORT }",
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
                    "Amiens-Glisy Gamma 2": {
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
                    }
                }
            },
            "Poix Alpha": {
                "airbase": "Poix",
                "warehouse": "Poix Airwing Warehouse-1#00001",
                "squadrons": {
                    "Poix Alpha 1": {
                        "airframe": dcs.planes.JF_17,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "PLAAF 125th AB (Fictional)",
                        "loadouts": {
                            "PL-5Ex2, 2*SD-10x2, 1100L Tankx2, 800L Tank": "{ AUFTRAG.Type.CAP, AUFTRAG.Type.INTERCEPT, AUFTRAG.Type.ESCORT }",
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
                    "Poix Alpha 2": {
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
                    }
                }
            },
            "Poix Beta": {
                "airbase": "Poix",
                "warehouse": "Poix Airwing Warehouse-2#00001",
                "squadrons": {
                    "Poix Beta 1": {
                        "airframe": dcs.planes.JF_17,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "PLAAF 125th AB (Fictional)",
                        "loadouts": {
                            "PL-5Ex2, 2*SD-10x2, 1100L Tankx2, 800L Tank": "{ AUFTRAG.Type.CAP, AUFTRAG.Type.INTERCEPT, AUFTRAG.Type.ESCORT }",
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
                    "Poix Beta 2": {
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
                    }
                }
            },
            "Poix Gamma": {
                "airbase": "Poix",
                "warehouse": "Poix Airwing Warehouse-3#00001",
                "squadrons": {
                    "Poix Gamma 1": {
                        "airframe": dcs.planes.JF_17,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "PLAAF 125th AB (Fictional)",
                        "loadouts": {
                            "PL-5Ex2, 2*SD-10x2, 1100L Tankx2, 800L Tank": "{ AUFTRAG.Type.CAP, AUFTRAG.Type.INTERCEPT, AUFTRAG.Type.ESCORT }",
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
                    "Poix Gamma 2": {
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
                    }
                }
            },
            "Poix Delta": {
                "airbase": "Poix",
                "warehouse": "Poix Airwing Warehouse-4#00001",
                "squadrons": {
                    "Poix Delta 1": {
                        "airframe": dcs.planes.JF_17,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "PLAAF 125th AB (Fictional)",
                        "loadouts": {
                            "PL-5Ex2, 2*SD-10x2, 1100L Tankx2, 800L Tank": "{ AUFTRAG.Type.CAP, AUFTRAG.Type.INTERCEPT, AUFTRAG.Type.ESCORT }",
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
                    "Poix Delta 2": {
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
                    }
                }
            },
            "FOB Amiens-Glisy": {
                "airbase": "FOB Amiens-Glisy Farp#00001",
                "warehouse": "FOB Amiens-Glisy Airwing Warehouse#00001",
                "squadrons": {
                    "Amiens-Glisy 1": {
                        "airframe": dcs.helicopters.Mi_26,
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
                    "Amiens-Glisy 2": {
                        "airframe": dcs.helicopters.AH_64D_BLK_II,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "IAF 113th Hornet Squadron",
                        "loadouts": {
                            "4 * Hellfire station: 4*AGM-114K": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.CASENHANCED }"
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
                "airbase": "Teddy Unit #1",
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
                    }
                }
            },
            "2nd CAW - Teddy": {
                "airbase": "Teddy Unit #1",
                "warehouse": "Teddy Unit #1",
                "squadrons": {
                    "GGD-03": {
                        "airframe": dcs.planes.FA_18C_hornet,
                        "groupSize": 2,
                        "initialInventory": 99,
                        "livery": "Canada 150 Demo Jet",
                        "loadouts": {
                            "AIM-9X*2, AIM-120C-5*6, FUEL*3": "{ AUFTRAG.Type.CAP }",
                        },
                        "capabilities": {
                            "AUFTRAG.Type.CAP": 50,
                        }
                    }
                }
            },
            "GOON OPS - Teddy": {
                "airbase": "Teddy Unit #1",
                "warehouse": "Teddy Unit #1",
                "squadrons": {
                    "GOON OPS TEDDY": {
                        "airframe": dcs.planes.FA_18C_hornet,
                        "groupSize": 2,
                        "initialInventory": 99,
                        "livery": "NSAWC blue",
                        "loadouts": {
                            "AIM-9M*2, MK-84*2, FUEL*2": "{ AUFTRAG.Type.BOMBING }",
                            "AIM-9X*2, AIM-120C-5*1, GBU-38*4, GBU-12*4, ATFLIR, FUEL": "{ AUFTRAG.Type.STRIKE }",
                            "AIM-9X*2, AIM-120C-5*2, AGM-88C*2, FUEL": "{ AUFTRAG.Type.SEAD }",
                            "AIM-9X*2, AIM-120C-5*1, AGM-65D*4, ATFLIR, FUEL": "{ AUFTRAG.Type.CAS }",
                        },
                        "capabilities": {
                            "AUFTRAG.Type.BOMBING": 50,
                            "AUFTRAG.Type.STRIKE": 50,
                            "AUFTRAG.Type.SEAD": 50,
                            "AUFTRAG.Type.CAS": 50,
                        }
                    },
                }
            },
            "3rd CAW - Abe": {
                "airbase": "Abe Unit #1",
                "warehouse": "Abe Unit #1",
                "squadrons": {
                    "GGD-04": {
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
                    "GGD-05 JTAC": {
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
                    "GGD-06": {
                        "airframe": dcs.helicopters.CH_47D,
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
            "4th CAW - Abe": {
                "airbase": "Abe Unit #1",
                "warehouse": "Abe Unit #1",
                "squadrons": {
                    "GGD-07": {
                        "airframe": dcs.planes.FA_18C_hornet,
                        "groupSize": 2,
                        "initialInventory": 99,
                        "livery": "Canada 150 Demo Jet",
                        "loadouts": {
                            "AIM-9X*2, AIM-120C-5*6, FUEL*3": "{ AUFTRAG.Type.CAP }",
                        },
                        "capabilities": {
                            "AUFTRAG.Type.CAP": 50,
                        }
                    }
                }
            },
            "GOON OPS - Abe": {
                "airbase": "Abe Unit #1",
                "warehouse": "Abe Unit #1",
                "squadrons": {
                    "GOON OPS ABE": {
                        "airframe": dcs.planes.FA_18C_hornet,
                        "groupSize": 2,
                        "initialInventory": 99,
                        "livery": "NSAWC blue",
                        "loadouts": {
                            "AIM-9M*2, MK-84*2, FUEL*2": "{ AUFTRAG.Type.BOMBING }",
                            "AIM-9X*2, AIM-120C-5*1, GBU-38*4, GBU-12*4, ATFLIR, FUEL": "{ AUFTRAG.Type.STRIKE }",
                            "AIM-9X*2, AIM-120C-5*2, AGM-88C*2, FUEL": "{ AUFTRAG.Type.SEAD }",
                            "AIM-9X*2, AIM-120C-5*1, AGM-65D*4, ATFLIR, FUEL": "{ AUFTRAG.Type.CAS }",
                        },
                        "capabilities": {
                            "AUFTRAG.Type.BOMBING": 50,
                            "AUFTRAG.Type.STRIKE": 50,
                            "AUFTRAG.Type.SEAD": 50,
                            "AUFTRAG.Type.CAS": 50,
                        }
                    },
                }
            },
            "1st Lymington Goonwing": {
                "airbase": "Lymington Goon Farp#00001",
                "warehouse": "Lymington Goon Airwing Warehouse#00001",
                "squadrons": {
                    "LG-01": {
                        "airframe": dcs.helicopters.CH_47D,
                        "groupSize": 1,
                        "initialInventory": 99,
                        "takeoffCold": "true",
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
            "1st Needs Oar Point Goonwing": {
                "airbase": "Needs Oar Point",
                "warehouse": "Needs Oar Point Goon Airwing Warehouse#00001",
                "squadrons": {
                    "NOPG-01": {
                        "airframe": dcs.planes.FA_18C_hornet,
                        "groupSize": 2,
                        "initialInventory": 99,
                        "livery": "Canada 150 Demo Jet",
                        "loadouts": {
                            "AIM-9X*2, AIM-120C-5*6, FUEL*3": "{ AUFTRAG.Type.CAP }",
                        },
                        "capabilities": {
                            "AUFTRAG.Type.CAP": 50,
                        }
                    }
                }
            },
            "5th CAW - Forrestal": {
                "airbase": "Forrestal Unit #1",
                "warehouse": "Forrestal Unit #1",
                "squadrons": {
                    "5S-01": {
                        "airframe": dcs.helicopters.CH_47D,
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
            "6th CAW - Saratoga": {
                "airbase": "Saratoga Unit #1",
                "warehouse": "Saratoga Unit #1",
                "squadrons": {
                    "6S-01": {
                        "airframe": dcs.helicopters.CH_47D,
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
            "1st Guines Goonwing": {
                "airbase": "Guines Goon Farp#00001",
                "warehouse": "Guines Goon Airwing Warehouse#00001",
                "squadrons": {
                    "LG-01": {
                        "airframe": dcs.helicopters.CH_47D,
                        "groupSize": 1,
                        "initialInventory": 99,
                        "takeoffCold": "true",
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
            "FOB Yes Minister": {
                "warehouse": "FOB Yes Minister Brigade Warehouse#00001",
                "platoons": {
                    "FOB Yes Minister 1": {
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
                    "FOB Yes Minister 2": {
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
            "FOB Murray": {
                "warehouse": "FOB Murray Brigade Warehouse#00001",
                "platoons": {
                    "FOB Murray 1": {
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
                    "FOB Murray 2": {
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
            "FOB Smith": {
                "warehouse": "FOB Smith Brigade Warehouse#00001",
                "platoons": {
                    "FOB Smith 1": {
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
                    "FOB Smith 2": {
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
            "FOB Bo'ohw'o'wo'er": {
                "warehouse": "FOB Bo'ohw'o'wo'er Brigade Warehouse#00001",
                "platoons": {
                    "FOB Bo'ohw'o'wo'er 1": {
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
                    "FOB Bo'ohw'o'wo'er 2": {
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
            "FOB Innit": {
                "warehouse": "FOB Innit Brigade Warehouse#00001",
                "platoons": {
                    "FOB Innit 1": {
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
                    "FOB Innit 2": {
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
            "1st Kuz": {
                "warehouse": "RED RG Kuznetsov Unit #1",
                "platoons": {
                    "Kuz-01": {
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
                    }
                }
            },
            "FOB Amiens-Glisy": {
                "warehouse": "FOB Amiens-Glisy Brigade Warehouse#00001",
                "platoons": {
                    "FOB Amiens-Glisy 1": {
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
                    "FOB Amiens-Glisy 2": {
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

class DangerZoneBlueBrigades(calvinball.bluebrigade.BlueBrigades):
    def __init__(self) -> None:
        super().__init__()

    def define(self, m: dcs.Mission):
        blue_brigades = {
            "1st Forrestal": {
                "warehouse": "Forrestal Unit #1",
                "platoons": {
                    "Forrestal-01": {
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
                    }
                }
            },
            "1st Saratoga": {
                "warehouse": "Saratoga Unit #1",
                "platoons": {
                    "Saratoga-01": {
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
                    }
                }
            },
            "1st Lymington": {
                "warehouse": "Lymington Goon Brigade Warehouse#00001",
                "platoons": {
                    "Lymington-01": {
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
                    }
                }
            },
            "1st Guines": {
                "warehouse": "Guines Goon Brigade Warehouse#00001",
                "platoons": {
                    "Guines-01": {
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
                    }
                }
            }
        }
        return blue_brigades
