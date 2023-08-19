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
    local g = GROUP:FindByName("RED RG Kuznetsov")
    if not g then
        return
    end
    local ng = NAVYGROUP:New(g)
    ng:ClearWaypoints()
    ng:SetPatrolAdInfinitum(true)
    ng:AddWaypoint(COORDINATE:New(220160, 0, 140163), 25, nil, 0, true)
    ng:AddWaypoint(g:GetCoordinate(), 25, nil, 0, true)
end
