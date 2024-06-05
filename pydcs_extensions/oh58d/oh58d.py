from typing import Any, Dict, Set, List

from dcs import task
from dcs.helicopters import HelicopterType
from dcs.weapons_data import Weapons

from pydcs_extensions.modsupport import helicoptermod
from pydcs_extensions.weapon_injector import inject_weapons

class WeaponsOH58D:
        M260___7_x_Laser_Guided_Rkts__70_mm_Hydra_70_M151_HE_APKWS = {"clsid": "{M260_APKWS_M151}", "name": "M260 - 7 x Laser Guided Rkts, 70 mm Hydra 70 M151 HE APKWS", "weight": 120.9}
        M260___7_x_UnGd_Rkts__70_mm_Hydra_70__Pod_Zones_A___M151__B___M156 = {"clsid": "{M260_A_M151_B_M156}", "name": "M260 - 7 x UnGd Rkts, 70 mm Hydra 70, Pod Zones: A - M151; B - M156", "weight": 89.24}
        M260___7_x_UnGd_Rkts__70_mm_Hydra_70__Pod_Zones_A___M151__B___M257 = {"clsid": "{M260_A_M151_B_M257}", "name": "M260 - 7 x UnGd Rkts, 70 mm Hydra 70, Pod Zones: A - M151; B - M257", "weight": 91.1}
        M260___7_x_UnGd_Rkts__70_mm_Hydra_70__Pod_Zones_A___M151__B___M259 = {"clsid": "{M260_A_M151_B_M259}", "name": "M260 - 7 x UnGd Rkts, 70 mm Hydra 70, Pod Zones: A - M151; B - M259", "weight": 87.68}
        M260___7_x_UnGd_Rkts__70_mm_Hydra_70__Pod_Zones_A___M229__B___M156 = {"clsid": "{M260_A_M229_B_M156}", "name": "M260 - 7 x UnGd Rkts, 70 mm Hydra 70, Pod Zones: A - M229; B - M156", "weight": 103.12}
        M260___7_x_UnGd_Rkts__70_mm_Hydra_70__Pod_Zones_A___M229__B___M257 = {"clsid": "{M260_A_M229_B_M257}", "name": "M260 - 7 x UnGd Rkts, 70 mm Hydra 70, Pod Zones: A - M229; B - M257", "weight": 104.98}
        M260___7_x_UnGd_Rkts__70_mm_Hydra_70__Pod_Zones_A___M229__B___M259 = {"clsid": "{M260_A_M229_B_M259}", "name": "M260 - 7 x UnGd Rkts, 70 mm Hydra 70, Pod Zones: A - M229; B - M259", "weight": 101.56}
        M260___7_x_UnGd_Rkts__70_mm_Hydra_70_M151_HE = {"clsid": "{M260_M151}", "name": "M260 - 7 x UnGd Rkts, 70 mm Hydra 70 M151 HE", "weight": 88.7}
        M260___7_x_UnGd_Rkts__70_mm_Hydra_70_M156_SM = {"clsid": "{M260_M156}", "name": "M260 - 7 x UnGd Rkts, 70 mm Hydra 70 M156 SM", "weight": 89.96}
        M260___7_x_UnGd_Rkts__70_mm_Hydra_70_M229_HE = {"clsid": "{M260_M229}", "name": "M260 - 7 x UnGd Rkts, 70 mm Hydra 70 M229 HE", "weight": 112.99}
        M260___7_x_UnGd_Rkts__70_mm_Hydra_70_M257_IL = {"clsid": "{M260_M257}", "name": "M260 - 7 x UnGd Rkts, 70 mm Hydra 70 M257 IL", "weight": 94.3}
        M260___7_x_UnGd_Rkts__70_mm_Hydra_70_M259_SM = {"clsid": "{M260_M259}", "name": "M260 - 7 x UnGd Rkts, 70 mm Hydra 70 M259 SM", "weight": 86.32}
        M260___7_x_UnGd_Rkts__70_mm_Hydra_70_M274_TP_SM = {"clsid": "{M260_M274}", "name": "M260 - 7 x UnGd Rkts, 70 mm Hydra 70 M274 TP-SM", "weight": 88.7}
        OH58D_AGM_114_L = {"clsid": "OH58D_AGM_114_L", "name": "2xAGM-114K", "weight": 138.23}
        OH58D_AGM_114_L1 = {"clsid": "OH58D_AGM_114_L1", "name": "1xAGM-114K", "weight": 93.05}
        OH58D_AGM_114_R = {"clsid": "OH58D_AGM_114_R", "name": "2xAGM-114K", "weight": 138.23}
        OH58D_AGM_114_R1 = {"clsid": "OH58D_AGM_114_R1", "name": "1xAGM-114K", "weight": 93.05}
        OH58D_Blue_Smoke_Grenade = {"clsid": "OH58D_Blue_Smoke_Grenade", "name": "1xBlue Smoke Grenade", "weight": 0.5}
        OH58D_FIM_92_L = {"clsid": "OH58D_FIM_92_L", "name": "2xFIM-92", "weight": 42.8}
        OH58D_FIM_92_R = {"clsid": "OH58D_FIM_92_R", "name": "2xFIM-92", "weight": 42.8}
        OH58D_Green_Smoke_Grenade = {"clsid": "OH58D_Green_Smoke_Grenade", "name": "1xGreen Smoke Grenade", "weight": 0.5}
        OH58D_M3P_L100 = {"clsid": "OH58D_M3P_L100", "name": "M3P100", "weight": 85.868}
        OH58D_M3P_L200 = {"clsid": "OH58D_M3P_L200", "name": "M3P200", "weight": 99.186}
        OH58D_M3P_L300 = {"clsid": "OH58D_M3P_L300", "name": "M3P300", "weight": 112.504}
        OH58D_M3P_L400 = {"clsid": "OH58D_M3P_L400", "name": "M3P400", "weight": 125.822}
        OH58D_M3P_L500 = {"clsid": "OH58D_M3P_L500", "name": "M3P500", "weight": 139.14}
        OH58D_Red_Smoke_Grenade = {"clsid": "OH58D_Red_Smoke_Grenade", "name": "1xRed Smoke Grenade", "weight": 0.5}
        OH58D_Violet_Smoke_Grenade = {"clsid": "OH58D_Violet_Smoke_Grenade", "name": "1xViolet Smoke Grenade", "weight": 0.5}
        OH58D_White_Smoke_Grenade = {"clsid": "OH58D_White_Smoke_Grenade", "name": "1xWhite Smoke Grenade", "weight": 0.5}
        OH58D_Yellow_Smoke_Grenade = {"clsid": "OH58D_Yellow_Smoke_Grenade", "name": "1xYellow Smoke Grenade", "weight": 0.5}

inject_weapons(WeaponsOH58D)

@helicoptermod
class OH58D(HelicopterType):
    id = "OH58D"
    flyable = True
    height = 2.77
    width = 10.668
    length = 10.2
    fuel_max = 333.69
    max_speed = 230
    chaff = 0
    flare = 30
    charge_total = 30
    chaff_charge_size = 1
    flare_charge_size = 1
    eplrs = True
    radio_frequency = 116

    panel_radio = {
        1: {
            "channels": {
                1: 260,
                2: 225,
                4: 240,
                8: 280,
                16: 360,
                17: 370,
                9: 290,
                18: 380,
                5: 250,
                10: 300,
                20: 395,
                11: 310,
                3: 230,
                6: 260,
                12: 320,
                13: 330,
                7: 270,
                14: 340,
                19: 390,
                15: 350
            },
        },
        2: {
            "channels": {
                1: 131,
                2: 116,
                4: 120,
                8: 128,
                16: 144,
                17: 146,
                9: 130,
                18: 148,
                5: 122,
                10: 132,
                20: 151,
                11: 134,
                3: 118,
                6: 124,
                12: 136,
                13: 138,
                7: 126,
                14: 140,
                19: 150,
                15: 142
            },
        },
        4: {
            "channels": {
                1: 30,
                2: 40.4,
                4: 32,
                8: 44,
                16: 68,
                17: 72,
                9: 48,
                18: 74,
                5: 36,
                10: 50,
                20: 80,
                21: 84,
                11: 54,
                3: 30,
                6: 38,
                12: 56,
                13: 60,
                7: 42,
                14: 62,
                19: 78,
                15: 66
            },
        },
        3: {
            "channels": {
                1: 30,
                2: 40.4,
                4: 32,
                8: 44,
                16: 68,
                17: 72,
                9: 48,
                18: 74,
                5: 36,
                10: 50,
                20: 80,
                21: 84,
                11: 54,
                3: 30,
                6: 38,
                12: 56,
                13: 60,
                7: 42,
                14: 62,
                19: 78,
                15: 66
            },
        },
    }

    callnames: Dict[str, List[str]] = {
        "USA": [
            "Anvil",
            "Azrael",
            "Bam-Bam",
            "Blackjack",
            "Bootleg",
            "Burnin' Stogie",
            "Chaos",
            "Crazyhorse",
            "Crusader",
            "Darkhorse",
            "Eagle",
            "Lighthorse",
            "Mustang",
            "Outcast",
            "Palehorse",
            "Pegasus",
            "Pistol",
            "Roughneck",
            "Saber",
            "Shamus",
            "Spur",
            "Stetson",
            "Wrath",
        ]
    }

    property_defaults: Dict[str, Any] = {
        "NetCrewControlPriority": 0,
        "Remove_doors": True,
        "PDU": False,
        "Rifles": True,
        "MMS_removal": False,
        "Rapid_Deployment_Gear": False,
        "ALQ144": False,
        "importDrawings": True,
        "tacNet": 1,
    }

    class Properties:

        class NetCrewControlPriority:
            id = "NetCrewControlPriority"

            class Values:
                Pilot = 0
                Copilot = 1
                Ask_Always = -1
                Equally_Responsible = -2

        class Remove_doors:
            id = "Remove doors"

        class PDU:
            id = "PDU"

        class Rifles:
            id = "Rifles"

        class MMS_removal:
            id = "MMS removal"

        class Rapid_Deployment_Gear:
            id = "Rapid Deployment Gear"

        class ALQ144:
            id = "ALQ144"

        class importDrawings:
            id = "importDrawings"

        class tacNet:
            id = "tacNet"

    livery_name = "OH58D"  # from type

    class Pylon1:
        OH58D_AGM_114_L1 = (1, Weapons.OH58D_AGM_114_L1)
        OH58D_AGM_114_L = (1, Weapons.OH58D_AGM_114_L)
        OH58D_FIM_92_L = (1, Weapons.OH58D_FIM_92_L)
        OH58D_M3P_L100 = (1, Weapons.OH58D_M3P_L100)
        OH58D_M3P_L200 = (1, Weapons.OH58D_M3P_L200)
        OH58D_M3P_L300 = (1, Weapons.OH58D_M3P_L300)
        OH58D_M3P_L400 = (1, Weapons.OH58D_M3P_L400)
        OH58D_M3P_L500 = (1, Weapons.OH58D_M3P_L500)
        M260___7_x_UnGd_Rkts__70_mm_Hydra_70_M151_HE = (1, Weapons.M260___7_x_UnGd_Rkts__70_mm_Hydra_70_M151_HE)
        M260___7_x_UnGd_Rkts__70_mm_Hydra_70_M156_SM = (1, Weapons.M260___7_x_UnGd_Rkts__70_mm_Hydra_70_M156_SM)
        M260___7_x_UnGd_Rkts__70_mm_Hydra_70_M229_HE = (1, Weapons.M260___7_x_UnGd_Rkts__70_mm_Hydra_70_M229_HE)
        M260___7_x_UnGd_Rkts__70_mm_Hydra_70_M257_IL = (1, Weapons.M260___7_x_UnGd_Rkts__70_mm_Hydra_70_M257_IL)
        M260___7_x_UnGd_Rkts__70_mm_Hydra_70_M259_SM = (1, Weapons.M260___7_x_UnGd_Rkts__70_mm_Hydra_70_M259_SM)
        M260___7_x_UnGd_Rkts__70_mm_Hydra_70_M274_TP_SM = (1, Weapons.M260___7_x_UnGd_Rkts__70_mm_Hydra_70_M274_TP_SM)
        M260___7_x_UnGd_Rkts__70_mm_Hydra_70__Pod_Zones_A___M151__B___M156 = (1, Weapons.M260___7_x_UnGd_Rkts__70_mm_Hydra_70__Pod_Zones_A___M151__B___M156)
        M260___7_x_UnGd_Rkts__70_mm_Hydra_70__Pod_Zones_A___M151__B___M257 = (1, Weapons.M260___7_x_UnGd_Rkts__70_mm_Hydra_70__Pod_Zones_A___M151__B___M257)
        M260___7_x_UnGd_Rkts__70_mm_Hydra_70__Pod_Zones_A___M151__B___M259 = (1, Weapons.M260___7_x_UnGd_Rkts__70_mm_Hydra_70__Pod_Zones_A___M151__B___M259)
        M260___7_x_UnGd_Rkts__70_mm_Hydra_70__Pod_Zones_A___M229__B___M156 = (1, Weapons.M260___7_x_UnGd_Rkts__70_mm_Hydra_70__Pod_Zones_A___M229__B___M156)
        M260___7_x_UnGd_Rkts__70_mm_Hydra_70__Pod_Zones_A___M229__B___M257 = (1, Weapons.M260___7_x_UnGd_Rkts__70_mm_Hydra_70__Pod_Zones_A___M229__B___M257)
        M260___7_x_UnGd_Rkts__70_mm_Hydra_70__Pod_Zones_A___M229__B___M259 = (1, Weapons.M260___7_x_UnGd_Rkts__70_mm_Hydra_70__Pod_Zones_A___M229__B___M259)
        M260___7_x_Laser_Guided_Rkts__70_mm_Hydra_70_M151_HE_APKWS = (1, Weapons.M260___7_x_Laser_Guided_Rkts__70_mm_Hydra_70_M151_HE_APKWS)

    class Pylon2:
        OH58D_Red_Smoke_Grenade = (2, Weapons.OH58D_Red_Smoke_Grenade)
        OH58D_Blue_Smoke_Grenade = (2, Weapons.OH58D_Blue_Smoke_Grenade)
        OH58D_Green_Smoke_Grenade = (2, Weapons.OH58D_Green_Smoke_Grenade)
        OH58D_Yellow_Smoke_Grenade = (2, Weapons.OH58D_Yellow_Smoke_Grenade)
        OH58D_Violet_Smoke_Grenade = (2, Weapons.OH58D_Violet_Smoke_Grenade)
        OH58D_White_Smoke_Grenade = (2, Weapons.OH58D_White_Smoke_Grenade)

    class Pylon3:
        OH58D_Red_Smoke_Grenade = (3, Weapons.OH58D_Red_Smoke_Grenade)
        OH58D_Blue_Smoke_Grenade = (3, Weapons.OH58D_Blue_Smoke_Grenade)
        OH58D_Green_Smoke_Grenade = (3, Weapons.OH58D_Green_Smoke_Grenade)
        OH58D_Yellow_Smoke_Grenade = (3, Weapons.OH58D_Yellow_Smoke_Grenade)
        OH58D_Violet_Smoke_Grenade = (3, Weapons.OH58D_Violet_Smoke_Grenade)
        OH58D_White_Smoke_Grenade = (3, Weapons.OH58D_White_Smoke_Grenade)

    class Pylon4:
        OH58D_Red_Smoke_Grenade = (4, Weapons.OH58D_Red_Smoke_Grenade)
        OH58D_Blue_Smoke_Grenade = (4, Weapons.OH58D_Blue_Smoke_Grenade)
        OH58D_Green_Smoke_Grenade = (4, Weapons.OH58D_Green_Smoke_Grenade)
        OH58D_Yellow_Smoke_Grenade = (4, Weapons.OH58D_Yellow_Smoke_Grenade)
        OH58D_Violet_Smoke_Grenade = (4, Weapons.OH58D_Violet_Smoke_Grenade)
        OH58D_White_Smoke_Grenade = (4, Weapons.OH58D_White_Smoke_Grenade)

    class Pylon5:
        OH58D_AGM_114_R1 = (5, Weapons.OH58D_AGM_114_R1)
        OH58D_AGM_114_R = (5, Weapons.OH58D_AGM_114_R)
        OH58D_FIM_92_R = (5, Weapons.OH58D_FIM_92_R)
        M260___7_x_UnGd_Rkts__70_mm_Hydra_70_M151_HE = (5, Weapons.M260___7_x_UnGd_Rkts__70_mm_Hydra_70_M151_HE)
        M260___7_x_UnGd_Rkts__70_mm_Hydra_70_M156_SM = (5, Weapons.M260___7_x_UnGd_Rkts__70_mm_Hydra_70_M156_SM)
        M260___7_x_UnGd_Rkts__70_mm_Hydra_70_M229_HE = (5, Weapons.M260___7_x_UnGd_Rkts__70_mm_Hydra_70_M229_HE)
        M260___7_x_UnGd_Rkts__70_mm_Hydra_70_M257_IL = (5, Weapons.M260___7_x_UnGd_Rkts__70_mm_Hydra_70_M257_IL)
        M260___7_x_UnGd_Rkts__70_mm_Hydra_70_M259_SM = (5, Weapons.M260___7_x_UnGd_Rkts__70_mm_Hydra_70_M259_SM)
        M260___7_x_UnGd_Rkts__70_mm_Hydra_70_M274_TP_SM = (5, Weapons.M260___7_x_UnGd_Rkts__70_mm_Hydra_70_M274_TP_SM)
        M260___7_x_UnGd_Rkts__70_mm_Hydra_70__Pod_Zones_A___M151__B___M156 = (5, Weapons.M260___7_x_UnGd_Rkts__70_mm_Hydra_70__Pod_Zones_A___M151__B___M156)
        M260___7_x_UnGd_Rkts__70_mm_Hydra_70__Pod_Zones_A___M151__B___M257 = (5, Weapons.M260___7_x_UnGd_Rkts__70_mm_Hydra_70__Pod_Zones_A___M151__B___M257)
        M260___7_x_UnGd_Rkts__70_mm_Hydra_70__Pod_Zones_A___M151__B___M259 = (5, Weapons.M260___7_x_UnGd_Rkts__70_mm_Hydra_70__Pod_Zones_A___M151__B___M259)
        M260___7_x_UnGd_Rkts__70_mm_Hydra_70__Pod_Zones_A___M229__B___M156 = (5, Weapons.M260___7_x_UnGd_Rkts__70_mm_Hydra_70__Pod_Zones_A___M229__B___M156)
        M260___7_x_UnGd_Rkts__70_mm_Hydra_70__Pod_Zones_A___M229__B___M257 = (5, Weapons.M260___7_x_UnGd_Rkts__70_mm_Hydra_70__Pod_Zones_A___M229__B___M257)
        M260___7_x_UnGd_Rkts__70_mm_Hydra_70__Pod_Zones_A___M229__B___M259 = (5, Weapons.M260___7_x_UnGd_Rkts__70_mm_Hydra_70__Pod_Zones_A___M229__B___M259)
        M260___7_x_Laser_Guided_Rkts__70_mm_Hydra_70_M151_HE_APKWS = (5, Weapons.M260___7_x_Laser_Guided_Rkts__70_mm_Hydra_70_M151_HE_APKWS)

    pylons: Set[int] = {1, 2, 3, 4, 5}

    tasks = [task.CAP, task.CAS, task.GroundAttack, task.AFAC, task.Escort, task.Transport, task.AntishipStrike, task.Reconnaissance]
    task_default = task.AFAC