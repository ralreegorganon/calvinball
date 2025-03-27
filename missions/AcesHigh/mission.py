import dcs
import dcs.cloud_presets
import pydcs_extensions
import datetime
import random
import calvinball

class AcesHigh(calvinball.mission.Mission):
    def __init__(self) -> None:
        t = dcs.terrain.Normandy()
        miz_name = "AcesHigh"
        ctld = AcesHighCtld()
        clients = AcesHighClients()
        red_airwings = AcesHighRedAirwings()
        blue_airwings = AcesHighBlueAirwings()
        carriers = AcesHighCarriers()
        qrf = AcesHighQrf()
        reinforcement = AcesHighReinforcement()
        red_brigades = AcesHighRedBrigades()
        blue_brigades = AcesHighBlueBrigades()

        super().__init__(t, miz_name, ctld, clients, red_airwings, blue_airwings, carriers, qrf, reinforcement, red_brigades, blue_brigades)

        self.m.coalition["blue"].set_bullseye({"x": 57597, "y": -72593})
        self.m.coalition["red"].set_bullseye({"x": 57597, "y": -72593})

        max = len(dcs.cloud_presets.CLOUD_PRESETS) - 1
        preset_name = list(dcs.cloud_presets.CLOUD_PRESETS)[random.randint(0, max)]
        cloud_preset = dcs.weather.CloudPreset.by_name(preset_name)
        self.m.weather.clouds_base = random.randrange(int(cloud_preset.min_base), int(cloud_preset.max_base))
        self.m.weather.clouds_preset = cloud_preset
        wind_dir = random.randrange(0, 359) + 180
        wind_speed = random.randrange(5, 10)
        self.m.weather.wind_at_ground.direction = (wind_dir + random.randrange(-90, 90) - 180) % 360
        self.m.weather.wind_at_ground.speed = wind_speed + random.randrange(-4, -1)
        self.m.weather.wind_at_2000.direction = (wind_dir + random.randrange(-90, 90) - 180) % 360
        self.m.weather.wind_at_2000.speed = wind_speed + random.randrange(-2, 2)
        self.m.weather.wind_at_8000.direction = (wind_dir + random.randrange(-90, 90) - 180) % 360
        self.m.weather.wind_at_8000.speed = wind_speed + random.randrange(-1, 10)

        self.m.weather.halo.preset = dcs.weather.Halo.Preset.Auto
        self.m.weather.halo.crystals = None

        self.m.start_time = datetime.datetime(1944, 6, 6)
        self.m.random_daytime("day")

class AcesHighCtld(calvinball.ctld.Ctld):
    def __init__(self) -> None:
        super().__init__()

    def build(self, m: dcs.Mission):
        super().build(m)

class AcesHighQrf(calvinball.qrf.Qrf):
    def __init__(self) -> None:
        super().__init__()

    def build(self, m: dcs.Mission):
        super().build(m)

        p = dcs.mapping.Point(m.coalition["blue"].bullseye["x"], m.coalition["blue"].bullseye["y"], m.terrain)

        m.vehicle_group_platoon(m.country(dcs.countries.CombinedJointTaskForcesRed.name), "RED QRF 1", [
            dcs.vehicles.Unarmed.Kubelwagen_82,
            dcs.vehicles.Unarmed.Kubelwagen_82,
            dcs.vehicles.Unarmed.Blitz_36_6700A,
            dcs.vehicles.Unarmed.Blitz_36_6700A,
            dcs.vehicles.Unarmed.Horch_901_typ_40_kfz_21,
            dcs.vehicles.Unarmed.Horch_901_typ_40_kfz_21,
            dcs.vehicles.Unarmed.Sd_Kfz_2,
            dcs.vehicles.Unarmed.Sd_Kfz_2,
            dcs.vehicles.Unarmed.Sd_Kfz_2,
            dcs.vehicles.Unarmed.Sd_Kfz_7,
            dcs.vehicles.Unarmed.Sd_Kfz_7,
            dcs.vehicles.Unarmed.Sd_Kfz_7
        ], p, formation=dcs.unitgroup.VehicleGroup.Formation.Scattered).late_activation = True

        m.vehicle_group_platoon(m.country(dcs.countries.CombinedJointTaskForcesRed.name), "RED QRF 2", [
            dcs.vehicles.Armor.Pz_V_Panther_G,
            dcs.vehicles.Armor.Pz_V_Panther_G,
            dcs.vehicles.Armor.Pz_V_Panther_G,
            dcs.vehicles.Armor.Pz_V_Panther_G,
            dcs.vehicles.Unarmed.Sd_Kfz_2,
            dcs.vehicles.Unarmed.Sd_Kfz_2
        ], p, formation=dcs.unitgroup.VehicleGroup.Formation.Scattered).late_activation = True


class AcesHighReinforcement(calvinball.reinforcement.Reinforcement):
    def __init__(self) -> None:
        super().__init__()

    def build(self, m: dcs.Mission):
        super().build(m)

        p = dcs.mapping.Point(m.coalition["blue"].bullseye["x"], m.coalition["blue"].bullseye["y"], m.terrain)

        m.vehicle_group_platoon(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "BLUE REINFORCEMENT 1", [
            dcs.vehicles.Armor.M4_Sherman,
            dcs.vehicles.Armor.M4_Sherman,
            dcs.vehicles.Armor.M4_Sherman,
            dcs.vehicles.Armor.M4_Sherman,
            dcs.vehicles.Unarmed.M30_CC,
            dcs.vehicles.Unarmed.M30_CC,
            dcs.vehicles.Unarmed.M30_CC

        ], p, formation=dcs.unitgroup.VehicleGroup.Formation.Scattered).late_activation = True

class AcesHighCarriers(calvinball.carriers.Carriers):
    def __init__(self) -> None:
        super().__init__()

    def define(self, m: dcs.mission):
        return {}

class AcesHighClients(calvinball.clients.Clients):
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
                "airport": m.terrain.airports["Lymington"],
                "start_type": dcs.mission.StartType.Warm,
                "airframes": [
                    { "airframe": dcs.planes.P_51D_30_NA, "count": 4, "parking": [55, 56, 50, 48], "fuel": 1, "loadout": "Empty", "livery": "USAF 363rd FS, 357th FG DESERT RAT" },
                    { "airframe": dcs.planes.P_47D_30, "count": 4, "parking": [49, 52, 51, 53], "fuel": 1, "loadout": "Empty", "livery": "Maj_Howard_Park_1945"},
                    { "airframe": dcs.planes.FW_190D9, "count": 4, "parking": [4, 5, 6, 7], "fuel": 1, "loadout": "Empty", "livery": "FW-190D9_GB" },
                    { "airframe": dcs.planes.FW_190A8, "count": 4, "parking": [8, 9, 12, 10], "fuel": 1, "loadout": "Empty", "livery": "FW-190A8_RAF" },
                    { "airframe": dcs.planes.Bf_109K_4, "count": 4, "parking": [11, 13, 14, 15], "fuel": 1, "loadout": "Empty", "livery": "Bf-109 K4 Irmgard" },
                    { "airframe": dcs.planes.SpitfireLFMkIXCW, "count": 4, "parking": [16, 17, 19, 18], "fuel": 1, "loadout": "Empty", "livery": "RAF, No. 145 Squadron" },
                    { "airframe": dcs.planes.I_16, "count": 4, "parking": [20, 23, 21, 22], "fuel": 1, "loadout": "Empty", "livery": "Red Army Standard" },
                    { "airframe": dcs.planes.MosquitoFBMkVI, "count": 4, "parking": [36, 37, 38, 39], "fuel": 1, "loadout": "Empty", "livery": "605 Sqn" },
                ]
            },
        ]

        comms_plan = {
            "uhf": { 1: 250, 2: 251, 3: 252, 4: 253, 5: 254 },
            "vhf_am": { 1: 135, 2: 136, 3: 137, 4: 138, 5: 139 },
            "vhf_fm": { 1: 31, 2: 32, 3: 33, 4: 34, 5: 35 },
            "vhf_am_de": { 1: 39, 2: 40, 3: 41, 4: 42 }
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
            dcs.planes.P_47D_30: ["vhf_am"],
            dcs.planes.FW_190D9: ["vhf_am_de"],
            dcs.planes.FW_190A8: ["vhf_am_de"],
            dcs.planes.Bf_109K_4: ["vhf_am_de"],
            dcs.planes.SpitfireLFMkIX: ["vhf_am"],
            dcs.planes.SpitfireLFMkIXCW: ["vhf_am"],
            dcs.planes.I_16: ["vhf_am"],
            dcs.planes.MosquitoFBMkVI: ["vhf_am"],

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
            radios[pydcs_extensions.A_4E_C] = ["uhf"]

        for airport in airport_set:
            for airframe in airport["airframes"]:
                airframe["radios"] = {}
                if airframe["airframe"] in radio_override:
                    airframe["radio_override"] = radio_override[airframe["airframe"]]
                for i, template in enumerate(radios[airframe["airframe"]]):
                    airframe["radios"][i+1] = comms_plan[template]

        return airport_set

class AcesHighRedAirwings(calvinball.redairwing.RedAirwings):
    def __init__(self) -> None:
        super().__init__()

    def ju88loadout(self, fg: dcs.unitgroup.FlyingGroup):
        for p in fg.units:
            p.pylons.clear()
            p.load_pylon(dcs.planes.Ju_88A4.Pylon2._10_x_SC_50___50kg_GP_Bomb_LD)

    def define(self, m: dcs.Mission):
        red_airwings = {
            "Funtington": {
                "airbase": "Funtington",
                "warehouse": "Funtington Airwing Warehouse#00001",
                "squadrons": {
                    "Funtington 1": {
                        "airframe": dcs.planes.Bf_109K_4,
                        "groupSize": 2,
                        "initialInventory": 0,
                        "livery": "Bf-109 K4 Jagdgeschwader 53",
                        "loadouts": {
                            "Empty": "{ AUFTRAG.Type.CAP, AUFTRAG.Type.INTERCEPT }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.CAP": 50,
                            "AUFTRAG.Type.INTERCEPT": 50
                        }
                    }
                }
            },
            "Fecamp-Benouville": {
                "airbase": "Fecamp-Benouville",
                "warehouse": "Fecamp-Benouville Airwing Warehouse#00001",
                "squadrons": {
                    "Fecamp-Benouville 1": {
                        "airframe": dcs.planes.Bf_109K_4,
                        "groupSize": 2,
                        "initialInventory": 0,
                        "livery": "Bf-109 K4 Jagdgeschwader 53",
                        "loadouts": {
                            "Empty": "{ AUFTRAG.Type.ESCORT }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.ESCORT": 50
                        }
                    },
                    "Fecamp-Benouville 2": {
                        "airframe": dcs.planes.Ju_88A4,
                        "groupSize": 4,
                        "initialInventory": 0,
                        "livery": "Ju-88",
                        "loadouts": {
                            "FuncBomb": "{ AUFTRAG.Type.BOMBCARPET }"
                        },
                        "loadoutFuncs": {
                            "FuncBomb": self.ju88loadout
                        },
                        "capabilities": {
                            "AUFTRAG.Type.BOMBCARPET": 50
                        }
                    }
                }
            },
        }
        return red_airwings

class AcesHighBlueAirwings(calvinball.blueairwing.BlueAirwings):
    def __init__(self) -> None:
        super().__init__()

    def b17loadout(self, fg: dcs.unitgroup.FlyingGroup):
        for p in fg.units:
            p.pylons.clear()
            p.load_pylon(dcs.planes.B_17G.Pylon1._12_AN_M64___500lb_GP_Bomb_LD)

    def define(self, m: dcs.Mission):
        blue_airwings = {
            "Lymington": {
                "airbase": "Lymington",
                "warehouse": "Lymington Airwing Warehouse#00001",
                "squadrons": {
                    "G-01": {
                        "airframe": dcs.planes.SpitfireLFMkIXCW,
                        "groupSize": 2,
                        "initialInventory": 99,
                        "livery": "RAF, No. 145 Squadron",
                        "loadouts": {
                            "Empty": "{ AUFTRAG.Type.CAP }"
                        },
                        "capabilities": {
                            "AUFTRAG.Type.CAP": 50
                        }
                    }
                }
            },
            "GOON OPS - Stoney Cross": {
                "airbase": "Stoney Cross",
                "warehouse": "Stoney Cross Airwing Warehouse#00001",
                "squadrons": {
                    "GOON OPS STONEY CROSS": {
                        "airframe": dcs.planes.B_17G,
                        "groupSize": 4,
                        "initialInventory": 99,
                        "livery": "91st BG, 323rd BS, 'Out House Mouse",
                        "loadouts": {
                            "FuncBomb": "{ AUFTRAG.Type.BOMBCARPET }"
                        },
                        "loadoutFuncs": {
                            "FuncBomb": self.b17loadout
                        },
                        "capabilities": {
                            "AUFTRAG.Type.BOMBCARPET": 50
                        }
                    },
                }
            },
        }
        return blue_airwings

class AcesHighRedBrigades(calvinball.redbrigade.RedBrigades):
    def __init__(self) -> None:
        super().__init__()

    def define(self, m: dcs.Mission):
        red_brigades = {}
        return red_brigades

class AcesHighBlueBrigades(calvinball.bluebrigade.BlueBrigades):
    def __init__(self) -> None:
        super().__init__()

    def define(self, m: dcs.Mission):
        blue_brigades = {}
        return blue_brigades