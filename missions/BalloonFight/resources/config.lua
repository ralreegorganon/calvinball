MissionDb.enableConvoys = true
MissionDb.enableElint = true

MissionDb.redchief.strategicZoneResources.defaultEmptyFunc = function(chief)
    local resourceEmpty, resourceInfantry = chief:CreateResource(AUFTRAG.Type.ONGUARD, 1, 1, GROUP.Attribute.GROUND_INFANTRY)
    chief:AddTransportToResource(resourceInfantry, 1, 1, {GROUP.Attribute.AIR_TRANSPORTHELO, GROUP.Attribute.GROUND_APC})
    return resourceEmpty
end

MissionDb.redchief.strategicZoneResources.defaultOccupiedFunc = function(chief)
    local resourceOccupied = chief:CreateResource(AUFTRAG.Type.ARTY, 1, 2)
    chief:AddToResource(resourceOccupied, AUFTRAG.Type.CASENHANCED, 1, 2)
    return resourceOccupied
end

MissionDb.bluechief.strategicZoneResources.defaultEmptyFunc = function(chief)
    local resourceEmpty, resourceInfantry = chief:CreateResource(AUFTRAG.Type.ONGUARD, 1, 1, GROUP.Attribute.GROUND_INFANTRY)
    chief:AddTransportToResource(resourceInfantry, 1, 1, {GROUP.Attribute.AIR_TRANSPORTHELO, GROUP.Attribute.GROUND_APC})
    return resourceEmpty
end

MissionDb.bluechief.strategicZoneResources.defaultOccupiedFunc = function(chief)
    local resourceOccupied = chief:CreateResource(AUFTRAG.Type.ARTY, 1, 2)
    chief:AddToResource(resourceOccupied, AUFTRAG.Type.CASENHANCED, 1, 2)
    return resourceOccupied
end

MissionDb.ctld.customCtldFunc = function(instance)
    instance:AddTroopsCargo("Infantry (8)", { "CTLD Inf M4 8" }, CTLD_CARGO.Enum.TROOPS, 8, 80)
    instance:AddTroopsCargo("Infantry - AA (6)", { "CTLD Infantry AA" }, CTLD_CARGO.Enum.TROOPS, 6, 80)
    instance:AddTroopsCargo("Infantry - AT (8)", { "CTLD Infantry AT" }, CTLD_CARGO.Enum.TROOPS, 8, 80)
    instance:AddTroopsCargo("JTAC (1)", { "CTLD BLUE RECCE JTAC" }, CTLD_CARGO.Enum.TROOPS, 1, 80)
    instance:AddTroopsCargo("MORTAR (5)", { "CTLD MORTAR" }, CTLD_CARGO.Enum.TROOPS, 5, 122)
    instance:AddTroopsCargo("SK Special - AT (2)", { "CTLD AT SK Special 2" }, CTLD_CARGO.Enum.TROOPS, 2, 80)
    instance:AddTroopsCargo("SK Special - AA (2)", { "CTLD AA SK Special 2" }, CTLD_CARGO.Enum.TROOPS, 2, 80)

    instance:AddCratesCargo("MRAP - JTAC", { "CTLD BLUE RECCE JTAC MRAP" }, CTLD_CARGO.Enum.VEHICLE, 1, 1350, nil, "Vehicles")
    instance:AddCratesCargo("M939 - AMMO", { "CTLD M818" }, CTLD_CARGO.Enum.VEHICLE, 1, 1350, nil, "Vehicles")
    instance:AddCratesCargo("Leclerc", { "CTLD Leclerc" }, CTLD_CARGO.Enum.VEHICLE, 2, 1350, nil, "Vehicles")
    instance:AddCratesCargo("ZBD-04A", { "CTLD ZBD-04A" }, CTLD_CARGO.Enum.VEHICLE, 1, 1350, nil, "Vehicles")
    instance:AddCratesCargo("MLRS", { "CTLD MLRS" }, CTLD_CARGO.Enum.VEHICLE, 1, 1350, nil, "Artillery")
    instance:AddCratesCargo("Dana", { "CTLD Dana" }, CTLD_CARGO.Enum.VEHICLE, 1, 1350, nil, "Artillery")
    instance:AddCratesCargo("L118", { "CTLD L118" }, CTLD_CARGO.Enum.VEHICLE, 1, 1350, nil, "Artillery")
    instance:AddCratesCargo("AVENGER", { "CTLD AVENGER" }, CTLD_CARGO.Enum.VEHICLE, 1, 1350, nil, "Air Defense")
    instance:AddCratesCargo("HAWK", { "CTLD HAWK" }, CTLD_CARGO.Enum.VEHICLE, 3, 1350, nil, "Air Defense")
    instance:AddCratesCargo("NASAM", { "CTLD NASAM" }, CTLD_CARGO.Enum.VEHICLE, 2, 1350, nil, "Air Defense")
end
