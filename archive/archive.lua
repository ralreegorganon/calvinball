
local function setupBlue()
    local airwing = AIRWING:New("Larnaca Warehouse object", "1st Derp")
    airwing:Start()
    local vipers = SQUADRON:New("BLUE F-16 Group", 8, "Good Guys")
    vipers:SetSkill(AI.Skill.AVERAGE)
    vipers:AddMissionCapability({ AUFTRAG.Type.CAP })
    vipers:SetTakeoffHot()
    airwing:AddSquadron(vipers)
    airwing:NewPayload(GROUP:FindByName("BLUE F-16 Payload"), -1, { AUFTRAG.Type.CAP })

    local zoneAlpha = ZONE:New("Zone Alpha")
    local missionCAP = AUFTRAG:NewCAP(zoneAlpha)
    missionCAP:SetRepeat(99)
    airwing:AddMission(missionCAP)
end

local function setupRed()
    local airwing = AIRWING:New("Bassel Al-Assad Warehouse object", "1st Derp")
    airwing:Start()
    local vipers = SQUADRON:New("RED F-16 Group", 8, "Bad Guys")
    vipers:SetSkill(AI.Skill.EXCELLENT)
    vipers:AddMissionCapability({ AUFTRAG.Type.CAP })
    vipers:SetTakeoffHot()
    airwing:AddSquadron(vipers)
    airwing:NewPayload(GROUP:FindByName("RED F-16 Payload"), -1, { AUFTRAG.Type.CAP })

    local zoneAlpha = ZONE:New("Zone Alpha")
    local missionCAP = AUFTRAG:NewCAP(zoneAlpha)
    missionCAP:SetRepeat(99)
    airwing:AddMission(missionCAP)
end

setupBlue()
setupRed()