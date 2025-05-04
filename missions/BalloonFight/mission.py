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
                    { "airframe": dcs.helicopters.AH_64D_BLK_II, "count": 6, "parking": [175, 111, 85, 186, 148, 36], "fuel": 0.6, "loadout": "Empty", "livery": "JGSDF——1st_Combat_Helicopter_Unit" },
                    { "airframe": dcs.helicopters.CH_47Fbl1, "count": 4, "parking": [95, 195, 34, 185], "fuel": 0.6, "loadout": "Empty", "livery": "Turkish Land Forces" },
                    { "airframe": dcs.helicopters.Ka_50_3, "count": 4, "parking": [130, 163, 70, 149], "fuel": 0.6, "loadout": "Empty", "livery": "Ka-50_desert_werewolf", "properties": { dcs.helicopters.Ka_50_3.Properties.Realistic_INS.id: dcs.helicopters.Ka_50_3.Properties.Realistic_INS.Values.No_alignment_and_fixtaking_needed } },
                    { "airframe": dcs.helicopters.Mi_24P, "count": 6, "parking": [170, 188, 44, 162, 83, 152], "fuel": 0.6, "loadout": "Empty", "livery": "Ukrainian Army Aviation" },
                    { "airframe": dcs.helicopters.Mi_8MT, "count": 4, "parking": [40, 14, 37, 7], "fuel": 0.6, "loadout": "Empty", "livery": "Algerian AF Green EVSAN" },
                    { "airframe": dcs.helicopters.OH58D, "count": 6, "parking": [77, 69, 177, 78, 106, 127], "fuel": 0.6, "loadout": "Empty", "livery": "AUS Army Fictional" },
                    { "airframe": dcs.helicopters.SA342L, "count": 2, "parking": [46, 61], "fuel": 0.6, "loadout": "Empty", "livery": "Tiger Meet 2" },
                    { "airframe": dcs.helicopters.SA342M, "count": 2, "parking": [147, 38], "fuel": 0.6, "loadout": "Empty", "livery": "Tiger Meet" },
                    { "airframe": dcs.helicopters.UH_1H, "count": 6, "parking": [135, 137, 154, 42, 176, 50], "fuel": 0.6, "loadout": "Empty", "livery": "US ARMY 1972" },
                    { "airframe": dcs.planes.A_10A, "count": 2, "parking": [33, 145], "fuel": 1, "loadout": "Empty", "livery": "355th fs eielson afb, alaska (ak)", "start_type": dcs.mission.StartType.Cold },
                    { "airframe": dcs.planes.A_10C_2, "count": 6, "parking": [51, 112, 56, 84, 126, 107], "fuel": 0.6, "loadout": "Empty", "livery": "355th fs eielson afb, alaska (ak)" },
                    { "airframe": dcs.planes.AJS37, "count": 2, "parking": [65, 15], "fuel": 1, "loadout": "Empty", "livery": "SF-37 Akktu Stakki - F21" },
                    { "airframe": dcs.planes.AV8BNA, "count": 4, "parking": [60, 131, 1, 159], "fuel": 1, "loadout": "Empty", "livery": "vma-214" },
                    { "airframe": dcs.planes.C_101CC, "count": 2, "parking": [142, 53], "fuel": 1, "loadout": "Empty", "livery": "usaf agressor fictional" },
                    { "airframe": dcs.planes.F_14B, "count": 4, "parking": [113, 121, 160, 191], "fuel": 1, "loadout": "Empty", "livery": "Santa", "properties": { dcs.planes.F_14B.Properties.INSAlignmentStored.id: True } },
                    { "airframe": dcs.planes.F_15C, "count": 4, "parking": [49, 110, 134, 153], "fuel": 1, "loadout": "Empty", "livery": "12th Fighter SQN (AK)", "start_type": dcs.mission.StartType.Cold },
                    { "airframe": dcs.planes.F_15ESE, "count": 2, "parking": [123, 196], "fuel": 1, "loadout": "Empty", "livery": "USAF 494th Panthers FS 91-603 75th D-Day Anniversary", "properties": { dcs.planes.F_15ESE.Properties.NetCrewControlPriority.id: dcs.planes.F_15ESE.Properties.NetCrewControlPriority.Values.Equally_Responsible } },
                    { "airframe": dcs.planes.F_16C_50, "count": 8, "parking": [104, 174, 101, 62, 192, 115, 57, 13], "fuel": 1, "loadout": "Empty", "livery": "18th AGRS Arctic Splinter" },
                    { "airframe": dcs.planes.F_4E_45MC, "count": 8, "parking": [150, 93, 118, 161, 19, 139, 199, 45], "fuel": 1, "loadout": "Empty", "livery": "RS68-517_SEA_526TFS", "properties": { dcs.planes.F_4E_45MC.Properties.INSAlignmentStored.id: True } },
                    { "airframe": dcs.planes.F_5E_3, "count": 4, "parking": [4, 108, 138, 173], "fuel": 1, "loadout": "Empty", "livery": "BR FAB 4846" },
                    { "airframe": dcs.planes.F_86F_Sabre, "count": 2, "parking": [109, 39], "fuel": 1, "loadout": "Empty", "livery": "Royal Saudi Air Force" },
                    { "airframe": dcs.planes.FA_18C_hornet, "count": 8, "parking": [179, 98, 31, 97, 119, 164, 122, 180], "fuel": 1, "loadout": "Empty", "livery": "VX-31 CoNA" },
                    { "airframe": dcs.planes.J_11A, "count": 2, "parking": [6, 172], "fuel": 1, "loadout": "Empty", "livery": "USN Aggressor VFC-13 'Ferris' (Fictional)", "start_type": dcs.mission.StartType.Cold },
                    { "airframe": dcs.planes.JF_17, "count": 4, "parking": [198, 102, 24, 169], "fuel": 1, "loadout": "Empty", "livery": "PAF Black Panthers 07-101" },
                    { "airframe": dcs.planes.L_39ZA, "count": 2, "parking": [189, 32], "fuel": 1, "loadout": "Empty", "livery": "algerian af tiger nl-36" },
                    { "airframe": dcs.planes.M_2000C, "count": 2, "parking": [120, 30], "fuel": 1, "loadout": "Empty", "livery": "2003 Tigermeet" },
                    { "airframe": dcs.planes.MB_339A, "count": 2, "parking": [23, 128], "fuel": 1, "loadout": "Empty", "livery": "MB339AN 'NIGERIA'" },
                    { "airframe": dcs.planes.MiG_19P, "count": 2, "parking": [79, 75], "fuel": 1, "loadout": "Empty", "livery": "DDR - Fictional" },
                    { "airframe": dcs.planes.MiG_21Bis, "count": 6, "parking": [74, 72, 82, 184, 90, 183], "fuel": 1, "loadout": "Empty", "livery": "HuAF 31st AB (Turul Sqn)" },
                    { "airframe": dcs.planes.MiG_29S, "count": 2, "parking": [52, 171], "fuel": 1, "loadout": "Empty", "livery": "MB339AN 'NIGERIA'", "start_type": dcs.mission.StartType.Cold  },
                    { "airframe": dcs.planes.Mirage_F1EE, "count": 4, "parking": [25, 129, 27, 136], "fuel": 1, "loadout": "Empty", "livery": "USA AGGRESSOR Colour (CE)" },
                    { "airframe": dcs.planes.P_51D_30_NA, "count": 2, "parking": [96, 66], "fuel": 1, "loadout": "Empty", "livery": "Ukraine Modern" },
                    { "airframe": dcs.planes.Su_25, "count": 4, "parking": [114, 103, 35, 140], "fuel": 1, "loadout": "Empty", "livery": "petal camo scheme #1 (native). 299th brigade", "start_type": dcs.mission.StartType.Cold },
                    { "airframe": dcs.planes.Su_25T, "count": 4, "parking": [157, 197, 117, 67], "fuel": 1, "loadout": "Empty", "livery": "Algerian AF Desert KU-03", "start_type": dcs.mission.StartType.Cold },
                    { "airframe": dcs.planes.Su_27, "count": 2, "parking": [132, 55], "fuel": 1, "loadout": "Empty", "livery": "Air Force Standard old", "start_type": dcs.mission.StartType.Cold },
                    { "airframe": dcs.planes.Su_33, "count": 2, "parking": [181, 26], "fuel": 1, "loadout": "Empty", "livery": "t-10k-9 test paint scheme", "start_type": dcs.mission.StartType.Cold }
                ]
            },
            {
                "country": m.country(dcs.countries.CombinedJointTaskForcesBlue.name),
                "farp": "FARP Puhdys",
                "farp_zone": "FARP-1",
                "start_type": dcs.mission.StartType.Warm,
                "airframes": [
                    {
                        "airframe": dcs.helicopters.Mi_24P, "fuel": 0.6, "loadout": "Empty", "livery": "Ukrainian Army Aviation",
                        "positions": [{"heading": 135, "x": -525096.28686341, "y": -879182.91853331}, {"heading": 141, "x": -525079.22921661, "y": -879158.01829028}, {"heading": 162, "x": -525068.8377766, "y": -879125.07938611}, {"heading": 182, "x": -525067.26925735, "y": -879096.25784496}]
                    },
                    {
                        "airframe": dcs.helicopters.Mi_8MT, "fuel": 0.6, "loadout": "Empty", "livery": "Algerian AF Green EVSAN",
                        "positions": [{"heading": 116, "x": -525118.97542608, "y": -879200.05410454}, {"heading": 119, "x": -525148.168514, "y": -879210.53522819}, {"heading": 106, "x": -525178.65194791, "y": -879217.76461429}, {"heading": 72, "x": -525213.05242683, "y": -879215.26924276}]
                    },
                    {
                        "airframe": dcs.helicopters.UH_1H, "fuel": 0.6, "loadout": "Empty", "livery": "US ARMY 1972",
                        "positions": [{"heading": 247, "x": -525139.9667516, "y": -878985.25952122}, {"heading": 255, "x": -525155.94404962, "y": -878979.2208574}, {"heading": 251, "x": -525173.4310136, "y": -878977.58538595}, {"heading": 257, "x": -525193.47264579, "y": -878977.83699694}]
                    },
                    {
                        "airframe": dcs.helicopters.AH_64D_BLK_II, "fuel": 0.6, "loadout": "Empty", "livery": "JGSDF——1st_Combat_Helicopter_Unit",
                        "positions": [{"heading": 63, "x": -525240.76709246, "y": -879207.30900759}, {"heading": 45, "x": -525265.07893386, "y": -879191.49842293}, {"heading": 40, "x": -525288.21479966, "y": -879170.42919881}, {"heading": 30, "x": -525303.5274688, "y": -879142.17624589}]
                    },
                    {
                        "airframe": dcs.helicopters.SA342L, "fuel": 0.6, "loadout": "Empty", "livery": "Tiger Meet 2",
                        "positions": [{"heading": 225, "x": -525089.2285268, "y": -879022.92957021}]
                    },
                    {
                        "airframe": dcs.helicopters.SA342M, "fuel": 0.6, "loadout": "Empty", "livery": "Tiger Meet",
                        "positions": [{"heading": 234, "x": -525105.30584907, "y": -879007.63650756}]
                    },
                    {
                        "airframe": dcs.helicopters.Ka_50_3, "fuel": 0.6, "loadout": "Empty", "livery": "Ka-50_desert_werewolf",
                        "positions": [{"heading": 208, "x": -525068.24958188, "y": -879065.27958985}, {"heading": 212, "x": -525077.26856755, "y": -879042.73212569}],
                        "properties": { dcs.helicopters.Ka_50_3.Properties.Realistic_INS.id: dcs.helicopters.Ka_50_3.Properties.Realistic_INS.Values.No_alignment_and_fixtaking_needed }
                    },
                    {
                        "airframe": dcs.helicopters.OH58D, "fuel": 0.6, "loadout": "Empty", "livery": "AUS Army Fictional", "start_type": dcs.mission.StartType.Warm,
                        "positions": [{"heading": 10, "x": -525312.21450729, "y": -879111.56083862}, {"heading": 333, "x": -525309.89967444, "y": -879081.52583691}, {"heading": 324, "x": -525302.08020687, "y": -879055.52610725}, {"heading": 322, "x": -525288.00516525, "y": -879028.54894415}]
                    },
                    {
                        "airframe": dcs.helicopters.CH_47Fbl1, "fuel": 0.6, "loadout": "Empty", "livery": "Turkish Land Forces", "start_type": dcs.mission.StartType.Warm,
                        "positions": [{"heading": 314, "x": -525272.97047051, "y": -879017.06610045}, {"heading": 305, "x": -525252.82872594, "y": -879001.51108979}, {"heading": 299, "x": -525233.39254605, "y": -878990.50619517}, {"heading": 289, "x": -525211.72644286, "y": -878981.93195008}]
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
            dcs.helicopters.CH_47Fbl1: ["vhf_fm"],
            dcs.helicopters.Ka_50_3: ["vhf_fm"],
            dcs.helicopters.Mi_24P: ["uhf", "vhf_fm"],
            dcs.helicopters.Mi_8MT: ["uhf", "vhf_fm"],
            dcs.helicopters.OH58D: ["uhf", "vhf_am", "vhf_fm", "vhf_fm"],
            dcs.helicopters.SA342L: ["vhf_fm"],
            dcs.helicopters.SA342M: ["vhf_fm"],
            dcs.helicopters.UH_1H: ["uhf"],
            dcs.planes.A_10A: ["vhf_am"],
            dcs.planes.A_10C_2: ["vhf_am", "uhf", "vhf_fm"],
            dcs.planes.AJS37: ["uhf"],
            dcs.planes.AV8BNA: ["vhf_am", "uhf", "vhf_fm"],
            dcs.planes.C_101CC: ["uhf"],
            dcs.planes.F_14B: ["uhf", "vhf_am"],
            dcs.planes.F_15C: ["uhf"],
            dcs.planes.F_15ESE: ["uhf", "vhf_am"],
            dcs.planes.F_16C_50: ["uhf", "vhf_am"],
            dcs.planes.F_4E_45MC: ["uhf"],
            dcs.planes.F_5E_3: ["uhf"],
            dcs.planes.F_86F_Sabre: ["uhf"],
            dcs.planes.FA_18C_hornet: ["vhf_am", "uhf"],
            dcs.planes.J_11A: ["vhf_am"],
            dcs.planes.JF_17: ["uhf"],
            dcs.planes.L_39ZA: ["uhf"],
            dcs.planes.M_2000C: ["uhf", "vhf_am"],
            dcs.planes.MB_339A: ["uhf"],
            dcs.planes.MiG_19P: ["vhf_am"],
            dcs.planes.MiG_21Bis: ["uhf"],
            dcs.planes.MiG_29S: ["uhf"],
            dcs.planes.Mirage_F1BE: ["vhf_am", "uhf"],
            dcs.planes.Mirage_F1EE: ["vhf_am", "uhf"],
            dcs.planes.P_51D_30_NA: ["vhf_am"],
            dcs.planes.Su_25: ["vhf_am"],
            dcs.planes.Su_25T: ["vhf_am"],
            dcs.planes.Su_27: ["vhf_am"],
            dcs.planes.Su_33: ["vhf_am"],
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
                        "airframe": dcs.planes.F_4E_45MC,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "38+10_N72_JG71",
                        "loadouts": {
                            "A2A MEDIUM RANGE: Aim-7M*4, Aim-9M*4, ALE-40 (30-60)*1, Sargent Fletcher Fuel Tank 370 GAL*2": "{ AUFTRAG.Type.CAP, AUFTRAG.Type.INTERCEPT, AUFTRAG.Type.ESCORT }",
                            "IRON: Mk-82 Snakeye*24, Aim-7E2*3, ALQ-131 ECM*1, ALE-40 (30-60)*1": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.BOMBCARPET, AUFTRAG.Type.CASENHANCED }",
                            "SEAD + ATGM: AGM-45A*2, AGM-65D*2, Aim-7F*3, Aim-9L*4, ALQ-131*1, ALE-40 (30-60)*1, Sargent Fl. Fuel Tank 600 Gal*1": "{ AUFTRAG.Type.SEAD }"
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
            "Hahn": {
                "airbase": "Hahn",
                "warehouse": "Hahn Airwing Warehouse#00001",
                "squadrons": {
                    "Hahn AW 1": {
                        "airframe": dcs.planes.F_4E_45MC,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "38+10_N72_JG71",
                        "loadouts": {
                            "A2A MEDIUM RANGE: Aim-7M*4, Aim-9M*4, ALE-40 (30-60)*1, Sargent Fletcher Fuel Tank 370 GAL*2": "{ AUFTRAG.Type.CAP, AUFTRAG.Type.INTERCEPT, AUFTRAG.Type.ESCORT }",
                            "IRON: Mk-82 Snakeye*24, Aim-7E2*3, ALQ-131 ECM*1, ALE-40 (30-60)*1": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.BOMBCARPET, AUFTRAG.Type.CASENHANCED }",
                            "SEAD + ATGM: AGM-45A*2, AGM-65D*2, Aim-7F*3, Aim-9L*4, ALQ-131*1, ALE-40 (30-60)*1, Sargent Fl. Fuel Tank 600 Gal*1": "{ AUFTRAG.Type.SEAD }"
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
                    "Hahn AW 3": {
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
                },
            },
            "Buchel": {
                "airbase": "Buchel",
                "warehouse": "Buchel Airwing Warehouse#00001",
                "squadrons": {
                    "Buchel AW 1": {
                        "airframe": dcs.planes.Tornado_IDS,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "jagdbombergeschwader 33 buchel ab no. 43+19 experimental scheme",
                        "loadouts": {
                            "Mk-82*4,AIM-9*2,Fuel*2": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.BOMBCARPET }",
                            "AGM-88*4,AIM-9*2,ECM": "{ AUFTRAG.Type.SEAD }"
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
            "Spangdahlem": {
                "airbase": "Spangdahlem",
                "warehouse": "Spangdahlem Airwing Warehouse#00001",
                "squadrons": {
                    "Spangdahlem AW 1": {
                        "airframe": dcs.planes.A_10A,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "Canada RCAF 442 Snow Scheme",
                        "loadouts": {
                            "MK-84*2 , LAU-68*2 , AGM-65K*2": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.BOMBCARPET, AUFTRAG.Type.CASENHANCED }",
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
            "Bitburg": {
                "airbase": "Bitburg",
                "warehouse": "Bitburg Airwing Warehouse#00001",
                "squadrons": {
                    "Bitburg AW 1": {
                        "airframe": dcs.planes.F_15C,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "65th Aggressor SQN (WA) MiG",
                        "loadouts": {
                            "AIM-120B*4, AIM-7M*2, AIM-9M*2, Fuel*3": "{ AUFTRAG.Type.CAP, AUFTRAG.Type.INTERCEPT, AUFTRAG.Type.ESCORT }",
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
                }
            },
            "Pottschutthohe": {
                "airbase": "Pottschutthohe",
                "warehouse": "Pottschutthohe Airwing Warehouse#00001",
                "squadrons": {
                    "Pottschutthohe AW 1": {
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
                    "Pottschutthohe AW 2": {
                        "airframe": dcs.helicopters.AH_64D_BLK_II,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "UAE Armed Forces - OD",
                        "loadouts": {
                            "2 * M261: C - M274 (6SK), D/E - M151 (6PD), 2 * Hellfire station: 4*AGM-114K": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.CASENHANCED }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.CASENHANCED": 50
                        }
                    },
                    "Pottschutthohe AW 3": {
                        "airframe": dcs.helicopters.AH_1W,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "Standard",
                        "loadouts": {
                            "8xAGM-114, 38xHYDRA-70": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.CASENHANCED }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.CASENHANCED": 50
                        }
                    },
                    "Pottschutthohe AW 4": {
                        "airframe": dcs.helicopters.OH58D,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "DE Army Fictional",
                        "loadouts": {
                            "2x Hellfire, APKWS": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.CASENHANCED }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.CASENHANCED": 50
                        }
                    },
                }
            },
            "Zweibrucken": {
                "airbase": "Zweibrucken",
                "warehouse": "Zweibrucken Airwing Warehouse#00001",
                "squadrons": {
                    "Zweibrucken AW 1": {
                        "airframe": dcs.planes.F_4E_45MC,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "38+10_N72_JG71",
                        "loadouts": {
                            "A2A MEDIUM RANGE: Aim-7M*4, Aim-9M*4, ALE-40 (30-60)*1, Sargent Fletcher Fuel Tank 370 GAL*2": "{ AUFTRAG.Type.CAP, AUFTRAG.Type.INTERCEPT, AUFTRAG.Type.ESCORT }",
                            "IRON: Mk-82 Snakeye*24, Aim-7E2*3, ALQ-131 ECM*1, ALE-40 (30-60)*1": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.BOMBCARPET, AUFTRAG.Type.CASENHANCED }",
                            "SEAD + ATGM: AGM-45A*2, AGM-65D*2, Aim-7F*3, Aim-9L*4, ALQ-131*1, ALE-40 (30-60)*1, Sargent Fl. Fuel Tank 600 Gal*1": "{ AUFTRAG.Type.SEAD }"
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
                }
            },
            "FOB Roth": {
                "airbase": "H FRG 30",
                "warehouse": "FOB Roth Airwing Warehouse#00001",
                "squadrons": {
                    "FOB Roth AW 1": {
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
                    "FOB Roth AW 2": {
                        "airframe": dcs.helicopters.AH_64D_BLK_II,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "UAE Armed Forces - OD",
                        "loadouts": {
                            "2 * M261: C - M274 (6SK), D/E - M151 (6PD), 2 * Hellfire station: 4*AGM-114K": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.CASENHANCED }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.CASENHANCED": 50
                        }
                    },
                    "FOB Roth AW 3": {
                        "airframe": dcs.helicopters.AH_1W,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "Standard",
                        "loadouts": {
                            "8xAGM-114, 38xHYDRA-70": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.CASENHANCED }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.CASENHANCED": 50
                        }
                    },
                    "FOB Roth AW 4": {
                        "airframe": dcs.helicopters.OH58D,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "DE Army Fictional",
                        "loadouts": {
                            "2x Hellfire, APKWS": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.CASENHANCED }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.CASENHANCED": 50
                        }
                    },
                }
            },
            "FOB Schenker": {
                "airbase": "FOB Schenker FARP#00001",
                "warehouse": "FOB Schenker Airwing Warehouse#00001",
                "squadrons": {
                    "FOB Schenker AW 1": {
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
                    "FOB Schenker AW 2": {
                        "airframe": dcs.helicopters.AH_64D_BLK_II,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "UAE Armed Forces - OD",
                        "loadouts": {
                            "2 * M261: C - M274 (6SK), D/E - M151 (6PD), 2 * Hellfire station: 4*AGM-114K": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.CASENHANCED }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.CASENHANCED": 50
                        }
                    },
                    "FOB Schenker AW 3": {
                        "airframe": dcs.helicopters.AH_1W,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "Standard",
                        "loadouts": {
                            "8xAGM-114, 38xHYDRA-70": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.CASENHANCED }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.BAI": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.CASENHANCED": 50
                        }
                    },
                    "FOB Schenker AW 4": {
                        "airframe": dcs.helicopters.OH58D,
                        "groupSize": 2,
                        "initialInventory": 1,
                        "livery": "DE Army Fictional",
                        "loadouts": {
                            "2x Hellfire, APKWS": "{ AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.CASENHANCED }"
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

class BalloonFightBlueAirwings(calvinball.blueairwing.BlueAirwings):
    def __init__(self) -> None:
        super().__init__()

    def define(self, m: dcs.Mission):
        blue_airwings = {
            "Ramstein": {
                "airbase": "Ramstein",
                "warehouse": "Ramstein Airwing Warehouse#00001",
                "squadrons": {
                    "Ramstein AW 1": {
                        "airframe": dcs.planes.F_16C_50,
                        "groupSize": 2,
                        "initialInventory": 99,
                        "livery": "18th AGRS Arctic Splinter",
                        "loadouts": {
                            "AIM-120C*2, AIM-9X*2, MK-84*2, FUEL*2, ECM, TGP": "{ AUFTRAG.Type.BOMBING }",
                            "AIM-120C*2, AIM-9X*2, GBU-38*4, FUEL*2, ECM, TGP": "{ AUFTRAG.Type.STRIKE }",
                            "AIM-120C*4, AIM-9X*2, FUEL*2, ECM": "{ AUFTRAG.Type.CAP }",
                            "AIM-120C*2, AIM-9X*2, AGM-65D*4, FUEL*2, ECM, TGP": "{ AUFTRAG.Type.CAS }",
                            "AIM-120C*4, AGM-88C*4, ECM, TGP, HTS": "{ AUFTRAG.Type.SEAD }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.BOMBING": 50,
                            "AUFTRAG.Type.STRIKE": 50,
                            "AUFTRAG.Type.SEAD": 50,
                            "AUFTRAG.Type.CAS": 50,
                            "AUFTRAG.Type.CAP": 50,
                        }
                    },
                    "Ramstein AW 2": {
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
                    "Ramstein AW 3": {
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
                    "Ramstein AW 4 JTAC ELINT": {
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
                            dcs.vehicles.Infantry.Soldier_M4,
                            dcs.vehicles.Infantry.Soldier_M4,
                            dcs.vehicles.Infantry.Soldier_RPG,
                            dcs.vehicles.Infantry.Soldier_RPG,
                        ],
                        "initialInventory": 3,
                        "capabilities": {
                            "AUFTRAG.Type.ONGUARD": 50
                        }
                    }
                }
            },
            "FOB Schenker": {
                "warehouse": "FOB Schenker Brigade Warehouse#00001",
                "platoons": {
                    "Hahn B 1": {
                        "units": [
                            dcs.vehicles.Infantry.Soldier_M4,
                            dcs.vehicles.Infantry.Soldier_M4,
                            dcs.vehicles.Infantry.Soldier_RPG,
                            dcs.vehicles.Infantry.Soldier_RPG,
                        ],
                        "initialInventory": 3,
                        "capabilities": {
                            "AUFTRAG.Type.ONGUARD": 50
                        }
                    },
                }
            },
            "FOB Roth": {
                "warehouse": "FOB Roth Brigade Warehouse#00001",
                "platoons": {
                    "FOB Roth B 1": {
                        "units": [
                            dcs.vehicles.Infantry.Soldier_M4,
                            dcs.vehicles.Infantry.Soldier_M4,
                            dcs.vehicles.Infantry.Soldier_RPG,
                            dcs.vehicles.Infantry.Soldier_RPG,
                        ],
                        "initialInventory": 3,
                        "capabilities": {
                            "AUFTRAG.Type.ONGUARD": 50
                        }
                    },
                }
            },
        }
        return red_brigades

class BalloonFightBlueBrigades(calvinball.bluebrigade.BlueBrigades):
    def __init__(self) -> None:
        super().__init__()

    def define(self, m: dcs.Mission):
        blue_brigades = {
            "Ramstein": {
                "warehouse": "Ramstein Brigade Warehouse#00001",
                "platoons": {
                    "Ramstein B 1": {
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
        }
        return blue_brigades
