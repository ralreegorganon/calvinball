import dcs
import random

def build_copypasta_templates(m: dcs.Mission):
    templates = {
        "loose infantry": [
            { "unit": dcs.vehicles.Infantry.Infantry_AK_Ins, "min": 6, "max": 6},
            { "unit": dcs.vehicles.Infantry.Soldier_RPG, "min": 2, "max": 2}
        ],
        "bmp-1 squad": [
            { "unit": dcs.vehicles.Armor.BMP_1, "min": 1, "max": 1},
            { "unit": dcs.vehicles.Infantry.Infantry_AK_Ins, "min": 6, "max": 6},
            { "unit": dcs.vehicles.Infantry.Soldier_RPG, "min": 2, "max": 2},
        ],
        "btr-80 squad": [
            { "unit": dcs.vehicles.Armor.BTR_80, "min": 1, "max": 1},
            { "unit": dcs.vehicles.Infantry.Infantry_AK_Ins, "min": 6, "max": 6},
            { "unit": dcs.vehicles.Infantry.Soldier_RPG, "min": 1, "max": 1}
        ],
        "brdm-2 squad": [
            { "unit": dcs.vehicles.Armor.BRDM_2, "min": 3, "max": 3}
        ],
        "uaz-469 squad": [
            { "unit": dcs.vehicles.Unarmed.UAZ_469, "min": 1, "max": 1},
            { "unit": dcs.vehicles.Infantry.Infantry_AK_Ins, "min": 4, "max": 4},
        ],
        "ural-375 squad": [
            { "unit": dcs.vehicles.Unarmed.Ural_375, "min": 1, "max": 1},
            { "unit": dcs.vehicles.Infantry.Infantry_AK_Ins, "min": 4, "max": 4},
        ],
        "t-55 squad": [
            { "unit": dcs.vehicles.Armor.T_55, "min": 3, "max": 3},
            { "unit": dcs.vehicles.Infantry.Infantry_AK_Ins, "min": 12, "max": 12},
        ],
        "bmp-2 squad": [
            { "unit": dcs.vehicles.Armor.BMP_1, "min": 1, "max": 3},
            { "unit": dcs.vehicles.Armor.BMP_2, "min": 2, "max": 3},
            { "unit": dcs.vehicles.Infantry.Infantry_AK_ver3, "min": 8, "max": 16},
            { "unit": dcs.vehicles.AirDefence.SA_18_Igla_manpad, "min": 1, "max": 2},
            { "unit": dcs.vehicles.AirDefence.ZSU_23_4_Shilka, "min": 0, "max": 1},
            { "unit": dcs.vehicles.Unarmed.Ural_375, "min": 1, "max": 1},
        ],
        "t-72 squad": [
            { "unit": dcs.vehicles.Armor.T_72B, "min": 6, "max": 9},
            { "unit": dcs.vehicles.AirDefence.ZSU_23_4_Shilka, "min": 1, "max": 2},
            { "unit": dcs.vehicles.AirDefence.Strela_10M3, "min": 0, "max": 1},
            { "unit": dcs.vehicles.AirDefence.SA_18_Igla_manpad, "min": 1, "max": 2},
            { "unit": dcs.vehicles.Armor.BRDM_2, "min": 0, "max": 2},
        ],
        "artillery group": [
            { "unit": dcs.vehicles.Artillery.SAU_Akatsia, "min": 4, "max": 6},
            { "unit": dcs.vehicles.Unarmed.Ural_375, "min": 2, "max": 4},
            { "unit": dcs.vehicles.AirDefence.Strela_1_9P31, "min": 1, "max": 2},
            { "unit": dcs.vehicles.Infantry.Infantry_AK_ver3, "min": 8, "max": 16},
        ],
        "rocket artillery group": [
            { "unit": dcs.vehicles.Artillery.Grad_URAL, "min": 4, "max": 6},
            { "unit": dcs.vehicles.Unarmed.Ural_375, "min": 2, "max": 4},
            { "unit": dcs.vehicles.AirDefence.Strela_1_9P31, "min": 1, "max": 2},
            { "unit": dcs.vehicles.Infantry.Infantry_AK_ver3, "min": 8, "max": 8},
        ],
        "elite bmp": [
            { "unit": dcs.vehicles.Armor.BMP_3, "min": 4, "max": 4},
            { "unit": dcs.vehicles.AirDefence.x_2S6_Tunguska, "min": 1, "max": 1},
            { "unit": dcs.vehicles.Unarmed.Ural_375, "min": 2, "max": 2},
            { "unit": dcs.vehicles.AirDefence.SA_18_Igla_manpad, "min": 2, "max": 2},
        ],
        "elite tank": [
            { "unit": dcs.vehicles.Armor.T_90, "min": 4, "max": 6},
            { "unit": dcs.vehicles.AirDefence.x_2S6_Tunguska, "min": 1, "max": 1},
            { "unit": dcs.vehicles.Armor.BMP_3, "min": 1, "max": 2},
            { "unit": dcs.vehicles.Infantry.Infantry_AK_ver3, "min": 8, "max": 12},
            { "unit": dcs.vehicles.AirDefence.SA_18_Igla_manpad, "min": 2, "max": 2},
            { "unit": dcs.vehicles.Unarmed.Ural_375, "min": 1, "max": 1},
        ],
        "elite sam": [
            { "unit": dcs.vehicles.AirDefence.Tor_9A331, "min": 2, "max": 3},
            { "unit": dcs.vehicles.AirDefence.x_2S6_Tunguska, "min": 1, "max": 2},
            { "unit": dcs.vehicles.AirDefence.SA_18_Igla_manpad, "min": 2, "max": 3},
            { "unit": dcs.vehicles.Unarmed.Ural_375, "min": 2, "max": 2},
        ],
        "flak party": [
            { "unit": dcs.vehicles.AirDefence.S_60_Type59_Artillery, "min": 2, "max": 3},
            { "unit": dcs.vehicles.AirDefence.KS_19, "min": 2, "max": 3},
            { "unit": dcs.vehicles.AirDefence.ZU_23_Emplacement_Closed, "min": 2, "max": 3},
            { "unit": dcs.vehicles.Infantry.Infantry_AK_ver3, "min": 3, "max": 9},
            { "unit": dcs.vehicles.AirDefence.SA_18_Igla_manpad, "min": 0, "max": 1},
            { "unit": dcs.vehicles.Unarmed.Ural_375, "min": 2, "max": 2},
        ],
        "supply convoy": [
            { "unit": dcs.vehicles.Unarmed.Ural_375, "min": 4, "max": 6},
            { "unit": dcs.vehicles.Unarmed.ATZ_10, "min": 4, "max": 6},
            { "unit": dcs.vehicles.Armor.BRDM_2, "min": 2, "max": 3},
            { "unit": dcs.vehicles.AirDefence.Strela_10M3, "min": 2, "max": 3},
            { "unit": dcs.vehicles.AirDefence.Ural_375_ZU_23, "min": 2, "max": 2},
        ],
        "btr group": [
            { "unit": dcs.vehicles.Armor.BTR_80, "min": 6, "max": 9},
            { "unit": dcs.vehicles.AirDefence.Ural_375_ZU_23_Insurgent, "min": 0, "max": 2},
            { "unit": dcs.vehicles.Infantry.Infantry_AK_Ins, "min": 8, "max": 12},
            { "unit": dcs.vehicles.Infantry.Soldier_RPG, "min": 1, "max": 3},
            { "unit": dcs.vehicles.AirDefence.SA_18_Igla_manpad, "min": 0, "max": 1},
            { "unit": dcs.vehicles.AirDefence.SA_18_Igla_comm, "min": 0, "max": 1}
        ],
        "qrf group": [
            { "unit": dcs.vehicles.Armor.BRDM_2, "min": 2, "max": 4},
            { "unit": dcs.vehicles.AirDefence.ZSU_23_4_Shilka, "min": 1, "max": 1},
            { "unit": dcs.vehicles.Unarmed.Ural_375, "min": 1, "max": 1},
            { "unit": dcs.vehicles.AirDefence.ZSU_23_4_Shilka, "min": 1, "max": 1},
            { "unit": dcs.vehicles.Armor.BMP_2, "min": 2, "max": 4},
        ],
        "blue mobile 1": [
             { "unit": dcs.vehicles.Armor.leopard_2A4, "min": 4, "max": 8},
             { "unit": dcs.vehicles.Unarmed.M_818, "min": 1, "max": 3},
             { "unit": dcs.vehicles.Unarmed.Hummer, "min": 1, "max": 2},
             { "unit": dcs.vehicles.Infantry.Soldier_M4, "min": 4, "max": 8},
             { "unit": dcs.vehicles.AirDefence.Vulcan, "min": 1, "max": 2},
        ],
        "blue mobile 2": [
             { "unit": dcs.vehicles.Armor.MCV_80, "min": 4, "max": 8},
             { "unit": dcs.vehicles.Unarmed.M_818, "min": 1, "max": 3},
             { "unit": dcs.vehicles.Unarmed.Hummer, "min": 1, "max": 2},
             { "unit": dcs.vehicles.Infantry.Soldier_M4, "min": 4, "max": 8},
             { "unit": dcs.vehicles.AirDefence.Vulcan, "min": 1, "max": 2},
        ],
        "blue mobile 3": [
             { "unit": dcs.vehicles.Armor.M_2_Bradley, "min": 4, "max": 8},
             { "unit": dcs.vehicles.Unarmed.M_818, "min": 1, "max": 3},
             { "unit": dcs.vehicles.Unarmed.Hummer, "min": 1, "max": 2},
             { "unit": dcs.vehicles.Infantry.Soldier_M4, "min": 4, "max": 8},
             { "unit": dcs.vehicles.AirDefence.Vulcan, "min": 1, "max": 2},
        ],
        "blue mobile 4": [
             { "unit": dcs.vehicles.Artillery.M_109, "min": 4, "max": 8},
             { "unit": dcs.vehicles.Unarmed.M_818, "min": 2, "max": 4},
             { "unit": dcs.vehicles.Unarmed.Hummer, "min": 1, "max": 2},
             { "unit": dcs.vehicles.Infantry.Soldier_M4, "min": 4, "max": 8},
             { "unit": dcs.vehicles.AirDefence.Vulcan, "min": 1, "max": 2},
        ],
    }

    compositions = {
        "qrf": {
            "qty": 0,
            "templates": [
                { "id": "qrf group", "min": 1, "max": 1},
            ]
        },
        "midgame": {
            "qty": 0,
            "templates": [
                { "id": "btr group", "min": 1, "max": 1},
                { "id": "bmp-2 squad", "min": 1, "max": 1},
                { "id": "t-72 squad", "min": 1, "max": 1},
                { "id": "artillery group", "min": 1, "max": 1},
                { "id": "rocket artillery group", "min": 1, "max": 1},
                { "id": "elite bmp", "min": 1, "max": 1},
                { "id": "elite tank", "min": 1, "max": 1},
                { "id": "elite sam", "min": 1, "max": 1},
                { "id": "flak party", "min": 1, "max": 1},
                { "id": "supply convoy", "min": 1, "max": 1},
            ]
        },
        "low intensity": {
            "qty": 0,
            "templates": [
                { "id": "loose infantry", "min": 1, "max": 2},
                { "id": "bmp-1 squad", "min": 1, "max": 3},
                { "id": "btr-80 squad", "min": 1, "max": 3},
                { "id": "brdm-2 squad", "min": 1, "max": 2},
                { "id": "uaz-469 squad", "min": 1, "max": 4},
                { "id": "ural-375 squad", "min": 1, "max": 4},
                { "id": "t-55 squad", "min": 1, "max": 1},
            ]
        },
        "light defense": {
            "qty": 0,
            "templates": [
                { "id": "supply convoy", "min": 1, "max": 1},
            ]
        },
        "blue": {
            "qty": 1,
            "templates": [
                { "id": "blue mobile 1", "min": 1, "max": 3},
                { "id": "blue mobile 2", "min": 1, "max": 3},
                { "id": "blue mobile 3", "min": 1, "max": 3},
                { "id": "blue mobile 4", "min": 1, "max": 3},
            ]
        }
    }

    anchorx = -577817
    anchory = -1074749
    goffset = 0
    gc = m.next_group_id()
    prefix = "RED RG"

    for c in compositions.values():
        for i in range(c["qty"]):
            uc = 2
            catshift = 0
            for template in c["templates"]:
                template_iterations = random.randint(template["min"], template["max"])
                if template_iterations == 0:
                    continue

                once = True
                first_type = templates[template["id"]][0]["unit"]
                group_name = f"{prefix} {gc}"
                vg = m.vehicle_group(m.country(dcs.countries.CombinedJointTaskForcesRed.name), group_name , first_type, dcs.mapping.Point(anchorx + catshift, anchory + goffset, m.terrain), group_size=1)
                vg.late_activation = True
                for ti in range(template_iterations):
                    instance = templates[template["id"]]
                    ushift = 50
                    for unit in instance:
                        unit_iterations = random.randint(unit["min"], unit["max"])
                        for ui in range(unit_iterations):
                            if once:
                                ushift = ushift + 50
                                once = False
                                continue
                            v = m.vehicle(group_name + f" Unit #{uc}", unit["unit"])
                            v.position.x = anchorx + catshift
                            v.position.y = anchory + goffset + ushift
                            v.heading = random.randint(0, 359)
                            vg.add_unit(v)
                            uc = uc + 1
                            ushift = ushift + 50
                    catshift = catshift + 50
                catshift = catshift + 50
            goffset = goffset + 1300 



def build_sam_templates(m: dcs.Mission):
    templates = {
        # include 2 cargos -> oiltank, 2 cargos -> fuel tank
        # do the flower pattern w/ sensors and lgistics units in center and launchers in a circle, few 100 feet apart
        # include some AAA and manpads
        "RED SAM SA-2": [
            dcs.vehicles.AirDefence.p_19_s_125_sr,
            dcs.vehicles.AirDefence.SNR_75V,
            dcs.vehicles.AirDefence.S_75M_Volhov,
            dcs.vehicles.AirDefence.S_75M_Volhov,
            dcs.vehicles.AirDefence.S_75M_Volhov,
            dcs.vehicles.AirDefence.S_75M_Volhov,
            dcs.vehicles.AirDefence.S_75M_Volhov,
            dcs.vehicles.AirDefence.S_75M_Volhov,
            dcs.vehicles.Unarmed.SKP_11,
            dcs.vehicles.Unarmed.Ural_375_PBU,
            dcs.vehicles.Unarmed.Ural_375_PBU,
            dcs.vehicles.Unarmed.ZiL_131_APA_80,
            dcs.vehicles.Unarmed.Ural_375,
            dcs.vehicles.Unarmed.Ural_375,
            dcs.vehicles.Unarmed.Ural_375,
            dcs.vehicles.Unarmed.Ural_375,
            dcs.vehicles.Unarmed.Ural_375,
            dcs.vehicles.Unarmed.Ural_375,
        ],
        # include 1 cargos -> iso container small
        # place launchers within 70m of central guidance area
        # transports, containers, radio relay, position 100m away from central but no further than 200m away from launcher, other units should be part of central
        "RED SAM SA-3": [
            dcs.vehicles.AirDefence.p_19_s_125_sr,
            dcs.vehicles.AirDefence.snr_s_125_tr,
            dcs.vehicles.AirDefence.x_5p73_s_125_ln,
            dcs.vehicles.AirDefence.x_5p73_s_125_ln,
            dcs.vehicles.AirDefence.x_5p73_s_125_ln,
            dcs.vehicles.AirDefence.x_5p73_s_125_ln,
            dcs.vehicles.Unarmed.SKP_11,
            dcs.vehicles.Unarmed.Ural_375_PBU,
            dcs.vehicles.Unarmed.Ural_375_PBU,
            dcs.vehicles.Unarmed.Ural_375_PBU,
            dcs.vehicles.Unarmed.Ural_375_PBU,
            dcs.vehicles.Unarmed.ZiL_131_APA_80,
            dcs.vehicles.Unarmed.Ural_375,
        ],
        # include 8 cargos -> iso container small
        "RED SAM SA-6": [
            dcs.vehicles.AirDefence.Kub_1S91_str,
            dcs.vehicles.AirDefence.Kub_2P25_ln,
            dcs.vehicles.AirDefence.Kub_2P25_ln,
            dcs.vehicles.AirDefence.Kub_2P25_ln,
            dcs.vehicles.AirDefence.Kub_2P25_ln,
            dcs.vehicles.Armor.BTR_80,
            dcs.vehicles.Unarmed.SKP_11,
            dcs.vehicles.Unarmed.Ural_375_PBU,
            dcs.vehicles.Unarmed.GAZ_66,
            dcs.vehicles.Unarmed.KAMAZ_Truck,
            dcs.vehicles.Unarmed.KAMAZ_Truck,
            dcs.vehicles.Unarmed.ZIL_131_KUNG,
        ],
        "RED SAM SA-8": [
            dcs.vehicles.AirDefence.Osa_9A33_ln,
            dcs.vehicles.AirDefence.Osa_9A33_ln,
            dcs.vehicles.AirDefence.Osa_9A33_ln,
            dcs.vehicles.AirDefence.Osa_9A33_ln,
            dcs.vehicles.AirDefence.Dog_Ear_radar,
            dcs.vehicles.Unarmed.Ural_375_PBU,
            dcs.vehicles.Unarmed.ATZ_10,
            dcs.vehicles.Unarmed.KAMAZ_Truck,
            dcs.vehicles.Unarmed.Ural_375,
            dcs.vehicles.Unarmed.ZIL_131_KUNG,
        ],
        # include 8 cargos -> iso container small, 4 structures -> generatorf
        "RED SAM SA-10": [
            dcs.vehicles.AirDefence.S_300PS_54K6_cp,
            dcs.vehicles.AirDefence.S_300PS_40B6MD_sr,
            dcs.vehicles.AirDefence.S_300PS_64H6E_sr,
            dcs.vehicles.AirDefence.S_300PS_40B6M_tr,
            dcs.vehicles.AirDefence.S_300PS_5P85C_ln,
            dcs.vehicles.AirDefence.S_300PS_5P85C_ln,
            dcs.vehicles.AirDefence.S_300PS_5P85C_ln,
            dcs.vehicles.AirDefence.S_300PS_5P85C_ln,
            dcs.vehicles.AirDefence.S_300PS_5P85D_ln,
            dcs.vehicles.AirDefence.S_300PS_5P85D_ln,
            dcs.vehicles.AirDefence.S_300PS_5P85D_ln,
            dcs.vehicles.AirDefence.S_300PS_5P85D_ln,
            dcs.vehicles.AirDefence.S_300PS_5P85D_ln,
            dcs.vehicles.AirDefence.S_300PS_5P85D_ln,
            dcs.vehicles.AirDefence.S_300PS_5P85D_ln,
            dcs.vehicles.AirDefence.S_300PS_5P85D_ln,
            dcs.vehicles.AirDefence.S_300PS_5P85D_ln,
            dcs.vehicles.AirDefence.S_300PS_5P85D_ln,
            dcs.vehicles.AirDefence.S_300PS_5P85D_ln,
            dcs.vehicles.AirDefence.S_300PS_5P85D_ln,
            dcs.vehicles.Unarmed.KAMAZ_Truck,
            dcs.vehicles.Unarmed.KAMAZ_Truck,
            dcs.vehicles.Unarmed.KAMAZ_Truck,
            dcs.vehicles.Unarmed.KAMAZ_Truck,
            dcs.vehicles.Unarmed.KAMAZ_Truck,
            dcs.vehicles.Unarmed.KAMAZ_Truck,
            dcs.vehicles.Unarmed.KAMAZ_Truck,
            dcs.vehicles.Unarmed.KAMAZ_Truck,
            dcs.vehicles.Unarmed.KAMAZ_Truck,
            dcs.vehicles.Unarmed.KAMAZ_Truck,
            dcs.vehicles.Unarmed.KAMAZ_Truck,
            dcs.vehicles.Unarmed.KAMAZ_Truck,
            dcs.vehicles.Unarmed.Ural_375,
            dcs.vehicles.Unarmed.Ural_375,
            dcs.vehicles.Unarmed.Ural_375,
            dcs.vehicles.Unarmed.Ural_375,
            dcs.vehicles.Unarmed.Ural_375,
            dcs.vehicles.Unarmed.Ural_375,
            dcs.vehicles.Unarmed.Ural_375,
            dcs.vehicles.Unarmed.Ural_375,
            dcs.vehicles.Unarmed.Ural_4320T,
            dcs.vehicles.Unarmed.Ural_4320T,
            dcs.vehicles.Unarmed.Ural_4320T,
            dcs.vehicles.Unarmed.Ural_4320T,
        ],
        # include 2 cargos -> iso container small
        "RED SAM SA-11": [
            dcs.vehicles.AirDefence.SA_11_Buk_CC_9S470M1,
            dcs.vehicles.AirDefence.SA_11_Buk_SR_9S18M1,
            dcs.vehicles.AirDefence.SA_11_Buk_LN_9A310M1,
            dcs.vehicles.AirDefence.SA_11_Buk_LN_9A310M1,
            dcs.vehicles.AirDefence.SA_11_Buk_LN_9A310M1,
            dcs.vehicles.AirDefence.SA_11_Buk_LN_9A310M1,
            dcs.vehicles.AirDefence.SA_11_Buk_LN_9A310M1,
            dcs.vehicles.AirDefence.SA_11_Buk_LN_9A310M1,
            dcs.vehicles.Unarmed.Ural_4320_APA_5D,
            dcs.vehicles.Unarmed.KAMAZ_Truck,
            dcs.vehicles.Unarmed.KAMAZ_Truck,
            dcs.vehicles.Unarmed.Ural_375,
            dcs.vehicles.Unarmed.Ural_4320_31,
            dcs.vehicles.Unarmed.Ural_4320_31,
            dcs.vehicles.Unarmed.ZIL_131_KUNG,
        ],
        "RED SAM SA-13": [
            dcs.vehicles.AirDefence.Strela_10M3,
            dcs.vehicles.AirDefence.Strela_10M3,
            dcs.vehicles.AirDefence.Strela_10M3,
            dcs.vehicles.AirDefence.Strela_10M3,
            dcs.vehicles.AirDefence.Dog_Ear_radar,
            dcs.vehicles.Armor.BTR_80,
            dcs.vehicles.Unarmed.Ural_375_PBU,
            dcs.vehicles.Unarmed.GAZ_3308,
            dcs.vehicles.Unarmed.GAZ_3308,
            dcs.vehicles.Unarmed.Ural_4320T,
            dcs.vehicles.Unarmed.ZIL_131_KUNG,
        ],
        "RED SAM SA-15": [
            dcs.vehicles.AirDefence.Tor_9A331,
            dcs.vehicles.AirDefence.Tor_9A331,
            dcs.vehicles.AirDefence.Tor_9A331,
            dcs.vehicles.AirDefence.Tor_9A331,
            dcs.vehicles.AirDefence.Dog_Ear_radar,
            dcs.vehicles.Unarmed.Ural_4320_31,
            dcs.vehicles.Unarmed.Ural_4320_31,
        ],
        "RED SAM SA-19": [
            dcs.vehicles.AirDefence.x_2S6_Tunguska,
            dcs.vehicles.AirDefence.x_2S6_Tunguska,
            dcs.vehicles.AirDefence.x_2S6_Tunguska,
            dcs.vehicles.AirDefence.x_2S6_Tunguska,
            dcs.vehicles.AirDefence.x_2S6_Tunguska,
            dcs.vehicles.AirDefence.x_2S6_Tunguska,
            dcs.vehicles.AirDefence.Dog_Ear_radar,
            dcs.vehicles.Unarmed.GAZ_3308,
            dcs.vehicles.Unarmed.KAMAZ_Truck,
            dcs.vehicles.Unarmed.KAMAZ_Truck,
            dcs.vehicles.Unarmed.KAMAZ_Truck,
            dcs.vehicles.Unarmed.Ural_4320_31,
            dcs.vehicles.Unarmed.Ural_4320_31,
            dcs.vehicles.Unarmed.Ural_4320_31,
            dcs.vehicles.Unarmed.ZIL_131_KUNG,
        ],
        "RED AIR DEFENSE BATTERY A": [
            dcs.vehicles.AirDefence.ZSU_23_4_Shilka,
            dcs.vehicles.AirDefence.ZSU_23_4_Shilka,
            dcs.vehicles.AirDefence.ZSU_23_4_Shilka,
            dcs.vehicles.AirDefence.ZSU_23_4_Shilka,
            dcs.vehicles.AirDefence.Strela_1_9P31,
            dcs.vehicles.AirDefence.Strela_1_9P31,
            dcs.vehicles.AirDefence.Strela_1_9P31,
            dcs.vehicles.AirDefence.Strela_1_9P31,
            dcs.vehicles.AirDefence.SA_18_Igla_manpad,
            dcs.vehicles.AirDefence.SA_18_Igla_manpad,
            dcs.vehicles.AirDefence.SA_18_Igla_manpad,
            dcs.vehicles.AirDefence.ZSU_57_2,
            dcs.vehicles.AirDefence.ZSU_57_2,
            dcs.vehicles.AirDefence.ZSU_57_2,
            dcs.vehicles.AirDefence.ZSU_57_2,
        ],
        "RED AIR DEFENSE BATTERY B": [
            dcs.vehicles.AirDefence.Dog_Ear_radar,
            dcs.vehicles.AirDefence.ZU_23_Emplacement_Closed,
            dcs.vehicles.AirDefence.ZU_23_Emplacement_Closed,
            dcs.vehicles.AirDefence.ZU_23_Emplacement_Closed,
            dcs.vehicles.AirDefence.ZU_23_Emplacement,
            dcs.vehicles.AirDefence.ZU_23_Emplacement,
            dcs.vehicles.AirDefence.ZU_23_Emplacement,
            dcs.vehicles.AirDefence.ZSU_57_2,
            dcs.vehicles.AirDefence.ZSU_57_2,
            dcs.vehicles.AirDefence.ZSU_57_2,
            dcs.vehicles.AirDefence.ZSU_57_2,
        ],
        "RED AIR DEFENSE BATTERY C": [
            dcs.vehicles.AirDefence.Dog_Ear_radar,
            dcs.vehicles.AirDefence.Ural_375_ZU_23,
            dcs.vehicles.AirDefence.Ural_375_ZU_23,
            dcs.vehicles.AirDefence.Ural_375_ZU_23,
            dcs.vehicles.AirDefence.Ural_375_ZU_23,
            dcs.vehicles.AirDefence.Ural_375_ZU_23,
            dcs.vehicles.AirDefence.Ural_375_ZU_23,
            dcs.vehicles.AirDefence.ZSU_57_2,
            dcs.vehicles.AirDefence.ZSU_57_2,
            dcs.vehicles.AirDefence.ZSU_57_2,
            dcs.vehicles.AirDefence.ZSU_57_2,
        ],
        # NATO Variations
        "RED Avenger": [
            dcs.vehicles.AirDefence.M1097_Avenger,
            dcs.vehicles.AirDefence.M1097_Avenger,
            dcs.vehicles.AirDefence.M1097_Avenger,
            dcs.vehicles.AirDefence.M1097_Avenger,
            dcs.vehicles.Unarmed.M_818,
            dcs.vehicles.Unarmed.M_818,
        ],
        "RED Chaparral": [
            dcs.vehicles.AirDefence.M48_Chaparral,
            dcs.vehicles.AirDefence.M48_Chaparral,
            dcs.vehicles.AirDefence.M48_Chaparral,
            dcs.vehicles.AirDefence.M48_Chaparral,
            dcs.vehicles.Unarmed.M_818,
            dcs.vehicles.Unarmed.M_818,
        ],
        "RED Hawk": [
            dcs.vehicles.AirDefence.Hawk_sr,
            dcs.vehicles.AirDefence.Hawk_tr,
            dcs.vehicles.AirDefence.Hawk_tr,
            dcs.vehicles.AirDefence.Hawk_pcp,
            dcs.vehicles.AirDefence.Hawk_pcp,
            dcs.vehicles.AirDefence.Hawk_pcp,
            dcs.vehicles.AirDefence.Hawk_cwar,
            dcs.vehicles.AirDefence.Hawk_ln,
            dcs.vehicles.AirDefence.Hawk_ln,
            dcs.vehicles.AirDefence.Hawk_ln,
            dcs.vehicles.AirDefence.Hawk_ln,
            dcs.vehicles.AirDefence.Hawk_ln,
            dcs.vehicles.AirDefence.Hawk_ln,
            dcs.vehicles.Unarmed.M_818,
            dcs.vehicles.Unarmed.M_818,
            dcs.vehicles.Unarmed.M_818,
        ],
        "RED Linebacker": [
            dcs.vehicles.AirDefence.M6_Linebacker,
            dcs.vehicles.AirDefence.M6_Linebacker,
            dcs.vehicles.AirDefence.M6_Linebacker,
            dcs.vehicles.AirDefence.M6_Linebacker,
            dcs.vehicles.Unarmed.M_818,
            dcs.vehicles.Unarmed.M_818,
        ],
        "RED NASAMS": [
            dcs.vehicles.AirDefence.NASAMS_Command_Post,
            dcs.vehicles.AirDefence.NASAMS_Radar_MPQ64F1,
            dcs.vehicles.AirDefence.NASAMS_Radar_MPQ64F1,
            dcs.vehicles.AirDefence.NASAMS_Radar_MPQ64F1,
            dcs.vehicles.AirDefence.NASAMS_Radar_MPQ64F1,
            dcs.vehicles.AirDefence.NASAMS_Radar_MPQ64F1,
            dcs.vehicles.AirDefence.NASAMS_Radar_MPQ64F1,
            dcs.vehicles.AirDefence.NASAMS_Radar_MPQ64F1,
            dcs.vehicles.AirDefence.NASAMS_Radar_MPQ64F1,
            dcs.vehicles.AirDefence.NASAMS_LN_C,
            dcs.vehicles.AirDefence.NASAMS_LN_C,
            dcs.vehicles.AirDefence.NASAMS_LN_C,
            dcs.vehicles.AirDefence.NASAMS_LN_C,
            dcs.vehicles.AirDefence.NASAMS_LN_C,
            dcs.vehicles.AirDefence.NASAMS_LN_C,
            dcs.vehicles.AirDefence.NASAMS_LN_C,
            dcs.vehicles.AirDefence.NASAMS_LN_C,
            dcs.vehicles.AirDefence.NASAMS_LN_C,
            dcs.vehicles.AirDefence.NASAMS_LN_C,
            dcs.vehicles.AirDefence.NASAMS_LN_C,
            dcs.vehicles.AirDefence.NASAMS_LN_C,
            dcs.vehicles.Unarmed.M_818,
            dcs.vehicles.Unarmed.M_818,
            dcs.vehicles.Unarmed.M_818,
        ],
        "RED Patriot": [
            dcs.vehicles.AirDefence.Patriot_ECS,
            dcs.vehicles.AirDefence.Patriot_ECS,
            dcs.vehicles.AirDefence.Patriot_ECS,
            dcs.vehicles.AirDefence.Patriot_ECS,
            dcs.vehicles.AirDefence.Patriot_ECS,
            dcs.vehicles.AirDefence.Patriot_ECS,
            dcs.vehicles.AirDefence.Patriot_str,
            dcs.vehicles.AirDefence.Patriot_str,
            dcs.vehicles.AirDefence.Patriot_str,
            dcs.vehicles.AirDefence.Patriot_str,
            dcs.vehicles.AirDefence.Patriot_str,
            dcs.vehicles.AirDefence.Patriot_str,
            dcs.vehicles.AirDefence.Patriot_AMG,
            dcs.vehicles.AirDefence.Patriot_AMG,
            dcs.vehicles.AirDefence.Patriot_AMG,
            dcs.vehicles.AirDefence.Patriot_AMG,
            dcs.vehicles.AirDefence.Patriot_AMG,
            dcs.vehicles.AirDefence.Patriot_AMG,
            dcs.vehicles.AirDefence.Patriot_EPP,
            dcs.vehicles.AirDefence.Patriot_EPP,
            dcs.vehicles.AirDefence.Patriot_EPP,
            dcs.vehicles.AirDefence.Patriot_EPP,
            dcs.vehicles.AirDefence.Patriot_EPP,
            dcs.vehicles.AirDefence.Patriot_cp,
            dcs.vehicles.AirDefence.Patriot_ln,
            dcs.vehicles.AirDefence.Patriot_ln,
            dcs.vehicles.AirDefence.Patriot_ln,
            dcs.vehicles.AirDefence.Patriot_ln,
            dcs.vehicles.AirDefence.Patriot_ln,
            dcs.vehicles.AirDefence.Patriot_ln,
            dcs.vehicles.AirDefence.Patriot_ln,
            dcs.vehicles.AirDefence.Patriot_ln,
            dcs.vehicles.AirDefence.Patriot_ln,
            dcs.vehicles.AirDefence.Patriot_ln,
            dcs.vehicles.AirDefence.Patriot_ln,
            dcs.vehicles.AirDefence.Patriot_ln,
            dcs.vehicles.AirDefence.Patriot_ln,
            dcs.vehicles.AirDefence.Patriot_ln,
            dcs.vehicles.AirDefence.Patriot_ln,
            dcs.vehicles.AirDefence.Patriot_ln,
            dcs.vehicles.AirDefence.Patriot_ln,
            dcs.vehicles.AirDefence.Patriot_ln,
            dcs.vehicles.AirDefence.Patriot_ln,
            dcs.vehicles.AirDefence.Patriot_ln,
            dcs.vehicles.AirDefence.Patriot_ln,
            dcs.vehicles.AirDefence.Patriot_ln,
            dcs.vehicles.AirDefence.Patriot_ln,
            dcs.vehicles.AirDefence.Patriot_ln,
            dcs.vehicles.AirDefence.Patriot_ln,
            dcs.vehicles.AirDefence.Patriot_ln,
            dcs.vehicles.AirDefence.Patriot_ln,
            dcs.vehicles.AirDefence.Patriot_ln,
            dcs.vehicles.AirDefence.Patriot_ln,
            dcs.vehicles.AirDefence.Patriot_ln,
            dcs.vehicles.AirDefence.Patriot_ln,
            dcs.vehicles.AirDefence.Patriot_ln,
            dcs.vehicles.AirDefence.Patriot_ln,
            dcs.vehicles.AirDefence.Patriot_ln,
            dcs.vehicles.AirDefence.Patriot_ln,
            dcs.vehicles.AirDefence.Patriot_ln,
            dcs.vehicles.Unarmed.M_818,
            dcs.vehicles.Unarmed.M_818,
            dcs.vehicles.Unarmed.M_818,
            dcs.vehicles.Unarmed.M_818,
            dcs.vehicles.Unarmed.M_818,
            dcs.vehicles.Unarmed.M_818,
            dcs.vehicles.Unarmed.M_818,
            dcs.vehicles.Unarmed.M_818,
            dcs.vehicles.Unarmed.M_818,
            dcs.vehicles.Unarmed.M_818,
            dcs.vehicles.Unarmed.M_818,
            dcs.vehicles.Unarmed.M_818,
            dcs.vehicles.Unarmed.M_818,
            dcs.vehicles.Unarmed.HEMTT_TFFT,
            dcs.vehicles.Unarmed.HEMTT_TFFT,
            dcs.vehicles.Unarmed.HEMTT_TFFT,
            dcs.vehicles.Unarmed.HEMTT_TFFT,
            dcs.vehicles.Unarmed.HEMTT_TFFT,
            dcs.vehicles.Unarmed.HEMTT_TFFT,
            dcs.vehicles.Unarmed.HEMTT_TFFT,
            dcs.vehicles.Unarmed.HEMTT_TFFT,
            dcs.vehicles.Unarmed.HEMTT_TFFT,
            dcs.vehicles.Unarmed.HEMTT_TFFT,
            dcs.vehicles.Unarmed.HEMTT_TFFT,
            dcs.vehicles.Unarmed.HEMTT_TFFT,
        ],
        "RED Rapier": [
            dcs.vehicles.AirDefence.rapier_fsa_launcher,
            dcs.vehicles.AirDefence.rapier_fsa_blindfire_radar,
            dcs.vehicles.AirDefence.rapier_fsa_optical_tracker_unit,
            dcs.vehicles.Unarmed.Land_Rover_101_FC,
            dcs.vehicles.Unarmed.M_818,
        ],
        "RED Roland": [
            dcs.vehicles.AirDefence.Roland_ADS,
            dcs.vehicles.AirDefence.Roland_Radar,
            dcs.vehicles.Unarmed.M_818,
        ],
        "RED AIR DEFENSE BATTERY D": [
            dcs.vehicles.AirDefence.Gepard,
            dcs.vehicles.AirDefence.Gepard,
            dcs.vehicles.AirDefence.Gepard,
            dcs.vehicles.AirDefence.Gepard,
            dcs.vehicles.AirDefence.Gepard,
            dcs.vehicles.Unarmed.M_818,
            dcs.vehicles.Unarmed.M_818,
            dcs.vehicles.AirDefence.Soldier_stinger,
        ],
        "RED AIR DEFENSE BATTERY E": [
            dcs.vehicles.AirDefence.Vulcan,
            dcs.vehicles.AirDefence.Vulcan,
            dcs.vehicles.AirDefence.Vulcan,
            dcs.vehicles.AirDefence.Vulcan,
            dcs.vehicles.AirDefence.Vulcan,
            dcs.vehicles.Unarmed.M_818,
            dcs.vehicles.Unarmed.M_818,
            dcs.vehicles.AirDefence.Soldier_stinger,
        ]
    }

    for gname, units in templates.items():
        gid = m.next_group_id()
        group_name = f"{gname} {gid}"
        m.vehicle_group_platoon(m.country(dcs.countries.CombinedJointTaskForcesRed.name), group_name, units, dcs.mapping.Point(-577817, -1074749, m.terrain))
