MissionDb.enableConvoys = true

MissionDb.redchief.strategicZoneResources.defaultEmptyFunc = function(chief)
    local resourceEmpty, resourceInfantry = chief:CreateResource(AUFTRAG.Type.ONGUARD, 1, 1, GROUP.Attribute.GROUND_INFANTRY)
    -- chief:AddToResource(resourceEmpty, AUFTRAG.Type.ONGUARD, 0, 1, GROUP.Attribute.GROUND_TANK)
    -- chief:AddToResource(resourceEmpty, AUFTRAG.Type.ONGUARD, 0, 1, GROUP.Attribute.GROUND_IFV)
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
    -- chief:AddToResource(resourceEmpty, AUFTRAG.Type.ONGUARD, 0, 1, GROUP.Attribute.GROUND_TANK)
    -- chief:AddToResource(resourceEmpty, AUFTRAG.Type.ONGUARD, 0, 1, GROUP.Attribute.GROUND_IFV)
    chief:AddTransportToResource(resourceInfantry, 1, 1, {GROUP.Attribute.AIR_TRANSPORTHELO, GROUP.Attribute.GROUND_APC})
    return resourceEmpty
end

MissionDb.bluechief.strategicZoneResources.defaultOccupiedFunc = function(chief)
    local resourceOccupied = chief:CreateResource(AUFTRAG.Type.ARTY, 1, 2)
    chief:AddToResource(resourceOccupied, AUFTRAG.Type.CASENHANCED, 1, 2)
    return resourceOccupied
end
