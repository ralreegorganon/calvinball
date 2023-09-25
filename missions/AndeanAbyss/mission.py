import dcs
import pydcs_extensions
import calvinball

class AndeanAbyss(calvinball.mission.Mission):
    def __init__(self) -> None:
        t = dcs.terrain.Falklands()
        miz_name = "AndeanAbyss"
        ctld = AndeanAbyssCtld()
        clients = AndeanAbyssClients()
        red_airwings = AndeanAbyssRedAirwings()
        blue_airwings = AndeanAbyssBlueAirwings()
        carriers = AndeanAbyssCarriers()
        qrf = AndeanAbyssQrf()
        reinforcement = AndeanAbyssReinforcement()
        red_brigades = AndeanAbyssRedBrigades()
        blue_brigades = AndeanAbyssBlueBrigades()

        super().__init__(t, miz_name, ctld, clients, red_airwings, blue_airwings, carriers, qrf, reinforcement, red_brigades, blue_brigades)

        self.m.coalition["blue"].set_bullseye({"x": 0 , "y": 0})
        self.m.coalition["red"].set_bullseye({"x": 0 , "y": 0})

class AndeanAbyssCtld(calvinball.ctld.Ctld):
    def __init__(self) -> None:
        super().__init__()

    def build(self, m: dcs.Mission):
        super().build(m)

class AndeanAbyssQrf(calvinball.qrf.Qrf):
    def __init__(self) -> None:
        super().__init__()

    def build(self, m: dcs.Mission):
        super().build(m)

class AndeanAbyssReinforcement(calvinball.reinforcement.Reinforcement):
    def __init__(self) -> None:
        super().__init__()

    def build(self, m: dcs.Mission):
        super().build(m)

class AndeanAbyssCarriers(calvinball.carriers.Carriers):
        def __init__(self) -> None:
            super().__init__()
    
class AndeanAbyssClients(calvinball.clients.Clients):
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
                "airport": m.terrain.airports["El Calafate"],
                "start_type": dcs.mission.StartType.Warm,
                "airframes": [
                    { 
                        "airframe": dcs.planes.F_16C_50, "fuel": 1, "loadout": "Empty", "livery": "Chile Air Force 746",
                        "parking": [5]
                    },
                ]
            },
            {
                "country": m.country(dcs.countries.CombinedJointTaskForcesBlue.name),
                "airport": m.terrain.airports["Rio Gallegos"],
                "start_type": dcs.mission.StartType.Warm,
                "airframes": [
                    { 
                        "airframe": dcs.planes.F_5E_3, "fuel": 1, "loadout": "Empty", "livery": "BR FAB 4834",
                        "parking": [5]
                    },
                ]
            },
            {
                "country": m.country(dcs.countries.CombinedJointTaskForcesBlue.name),
                "airport": m.terrain.airports["Puerto Natales"],
                "start_type": dcs.mission.StartType.Warm,
                "airframes": [
                    { 
                        "airframe": dcs.planes.M_2000C, "fuel": 1, "loadout": "Empty", "livery": "Peru052",
                        "positions": [{"heading": 323, "x": -23888.474940716, "y": -923031.00338003}]
                    },
                    { "airframe": dcs.planes.MiG_29S, "parking": [3], "fuel": 1, "loadout": "Empty", "livery": "MB339AN 'NIGERIA'" },
                    { "airframe": dcs.planes.Su_25T, "parking": [4], "fuel": 1, "loadout": "Empty", "livery": "MB339AN 'NIGERIA'" },
                    { "airframe": dcs.planes.MB_339A, "parking": [5], "fuel": 1, "loadout": "Empty", "livery": "MB339AP 'PERU'" },
                ]
            },
            {
                "country": m.country(dcs.countries.CombinedJointTaskForcesBlue.name),
                "airport": m.terrain.airports["Rio Turbio"],
                "start_type": dcs.mission.StartType.Warm,
                "airframes": [
                    { 
                        "airframe": dcs.planes.Mirage_F1EE, "fuel": 1, "loadout": "Empty", "livery": "Aerges Camo",
                        "parking": [2]
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
            dcs.planes.MiG_29S: ["uhf"],
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
            radios[pydcs_extensions.A_4E_C] = ["uhf"]

        for airport in airport_set:
            for airframe in airport["airframes"]:
                airframe["radios"] = {}
                if airframe["airframe"] in radio_override:
                    airframe["radio_override"] = radio_override[airframe["airframe"]]
                for i, template in enumerate(radios[airframe["airframe"]]):
                    airframe["radios"][i+1] = comms_plan[template]

        return airport_set

class AndeanAbyssRedAirwings(calvinball.redairwing.RedAirwings):
    def __init__(self) -> None:
        super().__init__()

    def define(self, m: dcs.Mission):
        red_airwings = {
        }
        return red_airwings

class AndeanAbyssBlueAirwings(calvinball.blueairwing.BlueAirwings):
    def __init__(self) -> None:
        super().__init__()

    def define(self, m: dcs.Mission):
        blue_airwings = {
        }
        return blue_airwings

class AndeanAbyssRedBrigades(calvinball.redbrigade.RedBrigades):
    def __init__(self) -> None:
        super().__init__()

    def define(self, m: dcs.Mission):
        red_brigades = {
        }
        return red_brigades

class AndeanAbyssBlueBrigades(calvinball.bluebrigade.BlueBrigades):
    def __init__(self) -> None:
        super().__init__()

    def define(self, m: dcs.Mission):
        blue_brigades = {
        }
        return blue_brigades
