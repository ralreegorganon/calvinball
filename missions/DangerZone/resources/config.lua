MissionDb.enableConvoys = false

MissionDb.invokeOnActivate["OBJ-6"] = function()
    local g = GROUP:FindByName("RED RG Neustrashimy")
    if not g then
        return
    end
    local ng = NAVYGROUP:New(g)
    ng:ClearWaypoints()
    ng:SetPatrolAdInfinitum(true)
    ng:AddWaypoint(COORDINATE:New(123806, 0, -96831), 30, nil, 0, true)
    ng:AddWaypoint(COORDINATE:New(127880, 0, -107679), 30, nil, 0, true)
    ng:AddWaypoint(g:GetCoordinate(), 30, nil, 0, true)
end

MissionDb.invokeOnActivate["OBJ-8"] = function()
    local g = GROUP:FindByName("RED RG 8-1 FK")
    if not g then
        return
    end
    local ng = NAVYGROUP:New(g)
    ng:ClearWaypoints()
    ng:SetPatrolAdInfinitum(true)
    ng:AddWaypoint(COORDINATE:New(128614, 0, -57619), 30, nil, 0, true)
    ng:AddWaypoint(COORDINATE:New(128546, 0, -57709), 30, nil, 0, true)
    ng:AddWaypoint(g:GetCoordinate(), 30, nil, 0, true)
end


MissionDb.invokeOnActivate["REINFORCEMENT-3"] = function()
    local g = GROUP:FindByName("BLUE Naval Escort RG 1")
    if not g then
        return
    end
    local ng = NAVYGROUP:New(g)
    ng:ClearWaypoints()
    ng:SetPatrolAdInfinitum(true)
    ng:AddWaypoint(COORDINATE:New(78902, 0, -67792), 25, nil, 0, true)
    ng:AddWaypoint(g:GetCoordinate(), 25, nil, 0, true)
    ng:SwitchROE(ENUMS.ROE.WeaponFree)
end

MissionDb.invokeOnActivate["OBJ-13"] = function()
    SCHEDULER:New(nil, function()
        local g = GROUP:FindByName("RED RG Kuznetsov")
        if not g then
            MESSAGE:New("Couldn't find the Kuz to set it up...", 30):ToAll()
            return
        end
        local ng = NAVYGROUP:New(g)
        ng:ClearWaypoints()
        ng:SetPatrolAdInfinitum(true)
        ng:AddWaypoint(COORDINATE:New(220160, 0, 140163), 25, nil, 0, true)
        ng:AddWaypoint(g:GetCoordinate(), 25, nil, 0, true)
    end, {}, 60)
end

MissionDb.invokeOnActivate["OBJ-14"] = function()
    SCHEDULER:New(nil, function()
        local g = GROUP:FindByName("RED RG Neustrashimy FR 1")
        if not g then
            return
        end
        local ng = NAVYGROUP:New(g)
        ng:ClearWaypoints()
        ng:SetPatrolAdInfinitum(true)
        ng:AddWaypoint(COORDINATE:New(181993, 0, 138421), 25, nil, 0, true)
        ng:AddWaypoint(g:GetCoordinate(), 25, nil, 0, true)
        ng:SetDefaultROE(ENUMS.ROE.WeaponFree)
    end, {}, 60)

    SCHEDULER:New(nil, function()
        local g = GROUP:FindByName("RED RG Grisha FR 1")
        if not g then
            return
        end
        local ng = NAVYGROUP:New(g)
        ng:ClearWaypoints()
        ng:SetPatrolAdInfinitum(true)
        ng:AddWaypoint(COORDINATE:New(184302, 0, 164083), 25, nil, 0, true)
        ng:AddWaypoint(g:GetCoordinate(), 25, nil, 0, true)
        ng:SetDefaultROE(ENUMS.ROE.WeaponFree)
    end, {}, 60)

    SCHEDULER:New(nil, function()
        local g = GROUP:FindByName("RED RG Moskva FR 1")
        if not g then
            return
        end
        local ng = NAVYGROUP:New(g)
        ng:ClearWaypoints()
        ng:SetPatrolAdInfinitum(true)
        ng:AddWaypoint(COORDINATE:New(198587, 0, 138472), 25, nil, 0, true)
        ng:AddWaypoint(g:GetCoordinate(), 25, nil, 0, true)
        ng:SetDefaultROE(ENUMS.ROE.WeaponFree)
    end, {}, 60)
end
