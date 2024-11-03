_SETTINGS:SetPlayerMenuOff()
--_SETTINGS:SetPlayerMenuOn()
_SETTINGS:SetEraModern()
_SETTINGS:SetA2A_BRAA()
_SETTINGS:SetA2G_LL_DDM()

-- BASE:TraceOn()
-- BASE:TraceClass("CTLD_HERCULES")
-- BASE:TraceClass("CTLD")

MESSAGE:New("CALVINBALL BEGIN!", 5):ToAll()

local defaultDrive = lfs.writedir() .. string.format("Missions\\%s\\missionstate", MissionDb.missionName)

local function loadState()
    local states = {}
    local objectivevehiclegroupstates = {}
    local objectiveshipgroupstates = {}
    local objectivestaticgroupstates = {}
    local unitstates = {}
    local nodestates = {}
    local taskstates = {}
    local qrfstates = {}
    local qrfvehiclegroupstates = {}
    local qrfshipgroupstates = {}
    local qrfstaticgroupstates = {}
    local reinforcementstates = {}
    local reinforcementvehiclegroupstates = {}
    local reinforcementshipgroupstates = {}
    local reinforcementstaticgroupstates = {}
    local taskvehiclegroupstates = {}
    local taskshipgroupstates = {}
    local taskstaticgroupstates = {}
    local redairwingstates = {}
    local blueairwingstates = {}
    local redbrigadestates = {}
    local bluebrigadestates = {}
    local counters = {}

    if io then
        if UTILS.CheckFileExists(defaultDrive,"progress.csv") then
            local _, loadeddata = UTILS.LoadFromFile(defaultDrive, "progress.csv")
            for _, _entry in pairs (loadeddata) do
                local dataset = UTILS.Split(_entry,",")
                -- name,state
                local name = dataset[1]
                local state = dataset[2]
                states[name] = state
            end
        end

        if UTILS.CheckFileExists(defaultDrive,"objectivevehiclegroups.csv") then
            local _, loadeddata = UTILS.LoadFromFile(defaultDrive, "objectivevehiclegroups.csv")
            for _, _entry in pairs (loadeddata) do
                local dataset = UTILS.Split(_entry,",")
                -- name,state
                local name = dataset[1]
                local state = dataset[2]
                objectivevehiclegroupstates[name] = state
            end
        end

        if UTILS.CheckFileExists(defaultDrive,"objectiveshipgroups.csv") then
            local _, loadeddata = UTILS.LoadFromFile(defaultDrive, "objectiveshipgroups.csv")
            for _, _entry in pairs (loadeddata) do
                local dataset = UTILS.Split(_entry,",")
                -- name,state
                local name = dataset[1]
                local state = dataset[2]
                objectiveshipgroupstates[name] = state
            end
        end

        if UTILS.CheckFileExists(defaultDrive,"objectivestaticgroups.csv") then
            local _, loadeddata = UTILS.LoadFromFile(defaultDrive, "objectivestaticgroups.csv")
            for _, _entry in pairs (loadeddata) do
                local dataset = UTILS.Split(_entry,",")
                -- name,state
                local name = dataset[1]
                local state = dataset[2]
                objectivestaticgroupstates[name] = state
            end
        end

        if UTILS.CheckFileExists(defaultDrive,"taskvehiclegroups.csv") then
            local _, loadeddata = UTILS.LoadFromFile(defaultDrive, "taskvehiclegroups.csv")
            for _, _entry in pairs (loadeddata) do
                local dataset = UTILS.Split(_entry,",")
                -- name,state
                local name = dataset[1]
                local state = dataset[2]
                taskvehiclegroupstates[name] = state
            end
        end

        if UTILS.CheckFileExists(defaultDrive,"taskshipgroups.csv") then
            local _, loadeddata = UTILS.LoadFromFile(defaultDrive, "taskshipgroups.csv")
            for _, _entry in pairs (loadeddata) do
                local dataset = UTILS.Split(_entry,",")
                -- name,state
                local name = dataset[1]
                local state = dataset[2]
                taskshipgroupstates[name] = state
            end
        end

        if UTILS.CheckFileExists(defaultDrive,"taskstaticgroups.csv") then
            local _, loadeddata = UTILS.LoadFromFile(defaultDrive, "taskstaticgroups.csv")
            for _, _entry in pairs (loadeddata) do
                local dataset = UTILS.Split(_entry,",")
                -- name,state
                local name = dataset[1]
                local state = dataset[2]
                taskstaticgroupstates[name] = state
            end
        end

        if UTILS.CheckFileExists(defaultDrive,"objectiveunits.csv") then
            local _, loadeddata = UTILS.LoadFromFile(defaultDrive, "objectiveunits.csv")
            for _, _entry in pairs (loadeddata) do
                local dataset = UTILS.Split(_entry,",")
                -- name,state
                local name = dataset[1]
                local state = dataset[2]
                unitstates[name] = state
            end
        end

        if UTILS.CheckFileExists(defaultDrive,"nodes.csv") then
            local _, loadeddata = UTILS.LoadFromFile(defaultDrive, "nodes.csv")
            for _, _entry in pairs (loadeddata) do
                local dataset = UTILS.Split(_entry,",")
                -- name,state
                local name = dataset[1]
                local state = dataset[2]
                nodestates[name] = state
            end
        end

        if UTILS.CheckFileExists(defaultDrive,"tasks.csv") then
            local _, loadeddata = UTILS.LoadFromFile(defaultDrive, "tasks.csv")
            for _, _entry in pairs (loadeddata) do
                local dataset = UTILS.Split(_entry,",")
                -- name,state
                local name = dataset[1]
                local state = dataset[2]
                taskstates[name] = state
            end
        end

        if UTILS.CheckFileExists(defaultDrive,"qrfs.csv") then
            local _, loadeddata = UTILS.LoadFromFile(defaultDrive, "qrfs.csv")
            for _, _entry in pairs (loadeddata) do
                local dataset = UTILS.Split(_entry,",")
                -- name,state
                local name = dataset[1]
                local state = dataset[2]
                qrfstates[name] = state
            end
        end

        if UTILS.CheckFileExists(defaultDrive,"qrfvehiclegroups.csv") then
            local _, loadeddata = UTILS.LoadFromFile(defaultDrive, "qrfvehiclegroups.csv")
            for _, _entry in pairs (loadeddata) do
                local dataset = UTILS.Split(_entry,",")
                -- name,state
                local name = dataset[1]
                local state = dataset[2]
                qrfvehiclegroupstates[name] = state
            end
        end

        if UTILS.CheckFileExists(defaultDrive,"qrfshipgroups.csv") then
            local _, loadeddata = UTILS.LoadFromFile(defaultDrive, "qrfshipgroups.csv")
            for _, _entry in pairs (loadeddata) do
                local dataset = UTILS.Split(_entry,",")
                -- name,state
                local name = dataset[1]
                local state = dataset[2]
                qrfshipgroupstates[name] = state
            end
        end

        if UTILS.CheckFileExists(defaultDrive,"qrfstaticgroups.csv") then
            local _, loadeddata = UTILS.LoadFromFile(defaultDrive, "qrfstaticgroups.csv")
            for _, _entry in pairs (loadeddata) do
                local dataset = UTILS.Split(_entry,",")
                -- name,state
                local name = dataset[1]
                local state = dataset[2]
                qrfstaticgroupstates[name] = state
            end
        end

        if UTILS.CheckFileExists(defaultDrive,"reinforcements.csv") then
            local _, loadeddata = UTILS.LoadFromFile(defaultDrive, "reinforcements.csv")
            for _, _entry in pairs (loadeddata) do
                local dataset = UTILS.Split(_entry,",")
                -- name,state
                local name = dataset[1]
                local state = dataset[2]
                reinforcementstates[name] = state
            end
        end

        if UTILS.CheckFileExists(defaultDrive,"reinforcementvehiclegroups.csv") then
            local _, loadeddata = UTILS.LoadFromFile(defaultDrive, "reinforcementvehiclegroups.csv")
            for _, _entry in pairs (loadeddata) do
                local dataset = UTILS.Split(_entry,",")
                -- name,state
                local name = dataset[1]
                local state = dataset[2]
                reinforcementvehiclegroupstates[name] = state
            end
        end

        if UTILS.CheckFileExists(defaultDrive,"reinforcementshipgroups.csv") then
            local _, loadeddata = UTILS.LoadFromFile(defaultDrive, "reinforcementshipgroups.csv")
            for _, _entry in pairs (loadeddata) do
                local dataset = UTILS.Split(_entry,",")
                -- name,state
                local name = dataset[1]
                local state = dataset[2]
                reinforcementshipgroupstates[name] = state
            end
        end

        if UTILS.CheckFileExists(defaultDrive,"reinforcementstaticgroups.csv") then
            local _, loadeddata = UTILS.LoadFromFile(defaultDrive, "reinforcementstaticgroups.csv")
            for _, _entry in pairs (loadeddata) do
                local dataset = UTILS.Split(_entry,",")
                -- name,state
                local name = dataset[1]
                local state = dataset[2]
                reinforcementstaticgroupstates[name] = state
            end
        end

        if UTILS.CheckFileExists(defaultDrive,"redairwings.csv") then
            local _, loadeddata = UTILS.LoadFromFile(defaultDrive, "redairwings.csv")
            for _, _entry in pairs (loadeddata) do
                local dataset = UTILS.Split(_entry,",")
                -- name,state
                local name = dataset[1]
                local state = dataset[2]
                redairwingstates[name] = state
            end
        end

        if UTILS.CheckFileExists(defaultDrive,"blueairwings.csv") then
            local _, loadeddata = UTILS.LoadFromFile(defaultDrive, "blueairwings.csv")
            for _, _entry in pairs (loadeddata) do
                local dataset = UTILS.Split(_entry,",")
                -- name,state
                local name = dataset[1]
                local state = dataset[2]
                blueairwingstates[name] = state
            end
        end

        if UTILS.CheckFileExists(defaultDrive,"redbrigades.csv") then
            local _, loadeddata = UTILS.LoadFromFile(defaultDrive, "redbrigades.csv")
            for _, _entry in pairs (loadeddata) do
                local dataset = UTILS.Split(_entry,",")
                -- name,state
                local name = dataset[1]
                local state = dataset[2]
                redbrigadestates[name] = state
            end
        end

        if UTILS.CheckFileExists(defaultDrive,"bluebrigades.csv") then
            local _, loadeddata = UTILS.LoadFromFile(defaultDrive, "bluebrigades.csv")
            for _, _entry in pairs (loadeddata) do
                local dataset = UTILS.Split(_entry,",")
                -- name,state
                local name = dataset[1]
                local state = dataset[2]
                bluebrigadestates[name] = state
            end
        end

        if UTILS.CheckFileExists(defaultDrive,"counters.csv") then
            local _, loadeddata = UTILS.LoadFromFile(defaultDrive, "counters.csv")
            for _, _entry in pairs (loadeddata) do
                local dataset = UTILS.Split(_entry,",")
                -- name,state
                local name = dataset[1]
                local state = dataset[2]
                counters[name] = state
            end
        end
    end

    for _, objective in ipairs(MissionDb.objectives) do
        if states[objective.name] ~= nil then
            objective.state = states[objective.name]
        else
            objective.state = "unstarted"
        end
        for _, node in ipairs(objective.nodes) do
            if nodestates[node.name] ~= nil then
                node.state = nodestates[node.name]
            else
                node.state = "unstarted"
            end
        end
        for _, group in ipairs(objective.vehicleGroups) do
            if objectivevehiclegroupstates[group.name] ~= nil then
                group.state = objectivevehiclegroupstates[group.name]
            else
                group.state = "unactivated"
            end
        end
        for _, group in ipairs(objective.shipGroups) do
            if objectiveshipgroupstates[group.name] ~= nil then
                group.state = objectiveshipgroupstates[group.name]
            else
                group.state = "unactivated"
            end
        end
        for _, group in ipairs(objective.staticGroups) do
            if objectivestaticgroupstates[group.name] ~= nil then
                group.state = objectivestaticgroupstates[group.name]
            else
                group.state = "unactivated"
            end
        end
        for _, qrf in ipairs(objective.qrfs) do
            if qrfstates[qrf.name] ~= nil then
                qrf.state = qrfstates[qrf.name]
            else
                qrf.state = "unactivated"
            end
            for _, group in ipairs(qrf.vehicleGroups) do
                if qrfvehiclegroupstates[group.name] ~= nil then
                    group.state = qrfvehiclegroupstates[group.name]
                else
                    group.state = "unactivated"
                end
            end
            for _, group in ipairs(qrf.shipGroups) do
                if qrfshipgroupstates[group.name] ~= nil then
                    group.state = qrfshipgroupstates[group.name]
                else
                    group.state = "unactivated"
                end
            end
            for _, group in ipairs(qrf.staticGroups) do
                if qrfstaticgroupstates[group.name] ~= nil then
                    group.state = qrfstaticgroupstates[group.name]
                else
                    group.state = "unactivated"
                end
            end
        end
        for _, reinforcement in ipairs(objective.reinforcements) do
            if reinforcementstates[reinforcement.name] ~= nil then
                reinforcement.state = reinforcementstates[reinforcement.name]
            else
                reinforcement.state = "unactivated"
            end
            for _, group in ipairs(reinforcement.vehicleGroups) do
                if reinforcementvehiclegroupstates[group.name] ~= nil then
                    group.state = reinforcementvehiclegroupstates[group.name]
                else
                    group.state = "unactivated"
                end
            end
            for _, group in ipairs(reinforcement.shipGroups) do
                if reinforcementshipgroupstates[group.name] ~= nil then
                    group.state = reinforcementshipgroupstates[group.name]
                else
                    group.state = "unactivated"
                end
            end
            for _, group in ipairs(reinforcement.staticGroups) do
                if reinforcementstaticgroupstates[group.name] ~= nil then
                    group.state = reinforcementstaticgroupstates[group.name]
                else
                    group.state = "unactivated"
                end
            end
        end
        for _, task in ipairs(objective.tasks) do
            if taskstates[task.name] ~= nil then
                task.state = taskstates[task.name]
            else
                task.state = "unstarted"
            end
            for _, group in ipairs(task.vehicleGroups) do
                if taskvehiclegroupstates[group.name] ~= nil then
                    group.state = taskvehiclegroupstates[group.name]
                else
                    group.state = "unactivated"
                end
            end
            for _, group in ipairs(task.shipGroups) do
                if taskshipgroupstates[group.name] ~= nil then
                    group.state = taskshipgroupstates[group.name]
                else
                    group.state = "unactivated"
                end
            end
            for _, group in ipairs(task.staticGroups) do
                if taskstaticgroupstates[group.name] ~= nil then
                    group.state = taskstaticgroupstates[group.name]
                else
                    group.state = "unactivated"
                end
            end
        end
    end

    for name, state in pairs(unitstates) do
        MissionDb.units[name] = state
    end

    for _, airwing in ipairs(MissionDb.redchief.airwings) do
        if redairwingstates[airwing.name] ~= nil then
            airwing.state = redairwingstates[airwing.name]
        else
            airwing.state = "unactivated"
        end
    end

    for _, airwing in ipairs(MissionDb.bluechief.airwings) do
        if blueairwingstates[airwing.name] ~= nil then
            airwing.state = blueairwingstates[airwing.name]
        else
            airwing.state = "unactivated"
        end
    end

    for _, brigade in ipairs(MissionDb.redchief.brigades) do
        if redbrigadestates[brigade.name] ~= nil then
            brigade.state = redbrigadestates[brigade.name]
        else
            brigade.state = "unactivated"
        end
    end

    for _, brigade in ipairs(MissionDb.bluechief.brigades) do
        if bluebrigadestates[brigade.name] ~= nil then
            brigade.state = bluebrigadestates[brigade.name]
        else
            brigade.state = "unactivated"
        end
    end

    for name, state in pairs(counters) do
        MissionDb.counters[name] = tonumber(state)
    end

    if MissionDb.counters.opstokens == nil then
        MissionDb.counters.opstokens = 0
    end

    -- todo, some sort of culling of the unit states from groups who are dead, since if they're dead we won't be spawning them again
end

local function saveState()
    if not lfs then
        return
    else
        lfs.mkdir(defaultDrive)
    end

    local objectivedata = ""
    local objectivevehiclegroupdata = ""
    local objectiveshipgroupdata = ""
    local objectivestaticgroupdata = ""
    local objectiveunitdata = ""
    local nodedata = ""
    local taskdata = ""
    local qrfdata = ""
    local qrfvehiclegroupdata = ""
    local qrfshipgroupdata = ""
    local qrfstaticgroupdata = ""
    local reinforcementdata = ""
    local reinforcementvehiclegroupdata = ""
    local reinforcementshipgroupdata = ""
    local reinforcementstaticgroupdata = ""
    local taskvehiclegroupdata = ""
    local taskshipgroupdata = ""
    local taskstaticgroupdata = ""
    local redairwingdata = ""
    local blueairwingdata = ""
    local redbrigadedata = ""
    local bluebrigadedata = ""
    local countersdata = ""
    for _, objective in ipairs(MissionDb.objectives) do
        objectivedata = string.format("%s%s,%s\n",objectivedata, objective.name, objective.state)
        for _, group in ipairs(objective.vehicleGroups) do
            objectivevehiclegroupdata = string.format("%s%s,%s\n",objectivevehiclegroupdata, group.name, group.state)
        end
        for _, group in ipairs(objective.shipGroups) do
            objectiveshipgroupdata = string.format("%s%s,%s\n",objectiveshipgroupdata, group.name, group.state)
        end
        for _, group in ipairs(objective.staticGroups) do
            objectivestaticgroupdata = string.format("%s%s,%s\n",objectivestaticgroupdata, group.name, group.state)
        end
        for _, node in ipairs(objective.nodes) do
            nodedata = string.format("%s%s,%s\n",nodedata, node.name, node.state)
        end
        for _, task in ipairs(objective.tasks) do
            taskdata = string.format("%s%s,%s\n",taskdata, task.name, task.state)
            for _, group in ipairs(task.vehicleGroups) do
                taskvehiclegroupdata = string.format("%s%s,%s\n",taskvehiclegroupdata, group.name, group.state)
            end
            for _, group in ipairs(task.shipGroups) do
                taskshipgroupdata = string.format("%s%s,%s\n",taskshipgroupdata, group.name, group.state)
            end
            for _, group in ipairs(task.staticGroups) do
                taskstaticgroupdata = string.format("%s%s,%s\n",taskstaticgroupdata, group.name, group.state)
            end
        end
        for _, qrf in pairs(objective.qrfs) do
            qrfdata = string.format("%s%s,%s\n",qrfdata, qrf.name, qrf.state)
            for _, group in ipairs(qrf.vehicleGroups) do
                qrfvehiclegroupdata = string.format("%s%s,%s\n",qrfvehiclegroupdata, group.name, group.state)
            end
            for _, group in ipairs(qrf.shipGroups) do
                qrfshipgroupdata = string.format("%s%s,%s\n",qrfshipgroupdata, group.name, group.state)
            end
            for _, group in ipairs(qrf.staticGroups) do
                qrfstaticgroupdata = string.format("%s%s,%s\n",qrfstaticgroupdata, group.name, group.state)
            end
        end
        for _, reinforcement in pairs(objective.reinforcements) do
            reinforcementdata = string.format("%s%s,%s\n",reinforcementdata, reinforcement.name, reinforcement.state)
            for _, group in ipairs(reinforcement.vehicleGroups) do
                reinforcementvehiclegroupdata = string.format("%s%s,%s\n",reinforcementvehiclegroupdata, group.name, group.state)
            end
            for _, group in ipairs(reinforcement.shipGroups) do
                reinforcementshipgroupdata = string.format("%s%s,%s\n",reinforcementshipgroupdata, group.name, group.state)
            end
            for _, group in ipairs(reinforcement.staticGroups) do
                reinforcementstaticgroupdata = string.format("%s%s,%s\n",reinforcementstaticgroupdata, group.name, group.state)
            end
        end
    end
    for name, state in pairs(MissionDb.units) do
        objectiveunitdata = string.format("%s%s,%s\n",objectiveunitdata, name, state)
    end
    for _, airwing in pairs(MissionDb.redchief.airwings) do
        redairwingdata = string.format("%s%s,%s\n",redairwingdata, airwing.name, airwing.state)
    end
    for _, airwing in pairs(MissionDb.bluechief.airwings) do
        blueairwingdata = string.format("%s%s,%s\n",blueairwingdata, airwing.name, airwing.state)
    end
    for _, brigade in pairs(MissionDb.redchief.brigades) do
        redbrigadedata = string.format("%s%s,%s\n",redbrigadedata, brigade.name, brigade.state)
    end
    for _, brigade in pairs(MissionDb.bluechief.brigades) do
        bluebrigadedata = string.format("%s%s,%s\n",bluebrigadedata, brigade.name, brigade.state)
    end
    for name, state in pairs(MissionDb.counters) do
        countersdata = string.format("%s%s,%s\n",countersdata, name, state)
    end

    UTILS.SaveToFile(defaultDrive,"progress.csv", objectivedata)
    UTILS.SaveToFile(defaultDrive,"objectivevehiclegroups.csv", objectivevehiclegroupdata)
    UTILS.SaveToFile(defaultDrive,"objectiveshipgroups.csv", objectiveshipgroupdata)
    UTILS.SaveToFile(defaultDrive,"objectivestaticgroups.csv", objectivestaticgroupdata)
    UTILS.SaveToFile(defaultDrive,"objectiveunits.csv", objectiveunitdata)
    UTILS.SaveToFile(defaultDrive,"nodes.csv", nodedata)
    UTILS.SaveToFile(defaultDrive,"tasks.csv", taskdata)
    UTILS.SaveToFile(defaultDrive,"qrfs.csv", qrfdata)
    UTILS.SaveToFile(defaultDrive,"qrfvehiclegroups.csv", qrfvehiclegroupdata)
    UTILS.SaveToFile(defaultDrive,"qrfshipgroups.csv", qrfshipgroupdata)
    UTILS.SaveToFile(defaultDrive,"qrfstaticgroups.csv", qrfstaticgroupdata)
    UTILS.SaveToFile(defaultDrive,"reinforcements.csv", reinforcementdata)
    UTILS.SaveToFile(defaultDrive,"reinforcementvehiclegroups.csv", reinforcementvehiclegroupdata)
    UTILS.SaveToFile(defaultDrive,"reinforcementshipgroups.csv", reinforcementshipgroupdata)
    UTILS.SaveToFile(defaultDrive,"reinforcementstaticgroups.csv", reinforcementstaticgroupdata)
    UTILS.SaveToFile(defaultDrive,"taskvehiclegroups.csv", taskvehiclegroupdata)
    UTILS.SaveToFile(defaultDrive,"taskshipgroups.csv", taskshipgroupdata)
    UTILS.SaveToFile(defaultDrive,"taskstaticgroups.csv", taskstaticgroupdata)
    UTILS.SaveToFile(defaultDrive,"redairwings.csv", redairwingdata)
    UTILS.SaveToFile(defaultDrive,"blueairwings.csv", blueairwingdata)
    UTILS.SaveToFile(defaultDrive,"redbrigades.csv", redbrigadedata)
    UTILS.SaveToFile(defaultDrive,"bluebrigades.csv", bluebrigadedata)
    UTILS.SaveToFile(defaultDrive,"counters.csv", countersdata)
end

-- stupid forward declaration shit
local completeObjective

local function checkObjectiveCapture(objective)
    local isCaptured = true
    local tasksComplete = true
    for _, node in ipairs(objective.nodes) do
        node.opsZone:EvaluateZone()
        if node.opsZone:IsContested() then
            isCaptured = false
            break
        end
        if not (node.opsZone:IsGuarded() and node.opsZone:IsBlue()) then
            isCaptured = false
            break
        end
    end

    for _, task in ipairs(objective.tasks) do
        if not task.instance or not task.instance:IsDone() then
            tasksComplete = false
            break
        end
    end

    if isCaptured and tasksComplete then
        completeObjective(objective, true)
    end
end

local function buildStrandObjectiveStateMap()
    local strandObjectiveStateMap = {}
    for _, strand in ipairs(MissionDb.strands) do
        strandObjectiveStateMap[strand.name] = {
            unstarted = 0,
            active = 0,
            finished = 0,
            total = 0,
            activeObjective = {
                name = "",
                displayName = "",
                nodes = {},
                totalNodes = 0,
                capturedNodes = 0,
                tasks = {},
                totalTasks = 0,
                completedTasks = 0
            }
        }
        for _, objectiveName in ipairs(strand.sequence) do
            for _, objective in ipairs(MissionDb.objectives) do
                if objective.name == objectiveName then
                    strandObjectiveStateMap[strand.name].total = strandObjectiveStateMap[strand.name].total + 1
                    strandObjectiveStateMap[strand.name][objective.state] = strandObjectiveStateMap[strand.name][objective.state] + 1
                    if objective.state == "active" then
                        local objectiveZone = ZONE:FindByName(objective.name)
                        strandObjectiveStateMap[strand.name].activeObjective.displayName = objectiveZone:GetProperty("label")

                        for _, node in ipairs(objective.nodes) do
                            local nodeZone = ZONE:FindByName(node.name)
                            local nodeStatus = {
                                name  = nodeZone:GetProperty("label"),
                                captured = node.opsZone:IsGuarded() and node.opsZone:IsBlue(),
                                contested =  node.opsZone:IsContested(),
                                redUnitsCount = node.opsZone.Nred
                            }
                            strandObjectiveStateMap[strand.name].activeObjective.totalNodes = strandObjectiveStateMap[strand.name].activeObjective.totalNodes + 1
                            if nodeStatus.captured then
                                strandObjectiveStateMap[strand.name].activeObjective.capturedNodes = strandObjectiveStateMap[strand.name].activeObjective.capturedNodes + 1
                            end
                            table.insert(strandObjectiveStateMap[strand.name].activeObjective.nodes, nodeStatus)
                        end

                        for _, task in ipairs(objective.tasks) do
                            local taskZone = ZONE:FindByName(task.name)
                            local taskStatus = {
                                name = taskZone:GetProperty("label"),
                                complete = task.state == "finished",
                                auftrag = taskZone:GetProperty("auftrag")
                            }
                            strandObjectiveStateMap[strand.name].activeObjective.totalTasks = strandObjectiveStateMap[strand.name].activeObjective.totalTasks + 1
                            if taskStatus.complete then
                                strandObjectiveStateMap[strand.name].activeObjective.completedTasks = strandObjectiveStateMap[strand.name].activeObjective.completedTasks + 1
                            end
                            table.insert(strandObjectiveStateMap[strand.name].activeObjective.tasks, taskStatus)
                        end
                    end
                end
            end
        end
    end
    return strandObjectiveStateMap
end

local function showNodeSurrenderUpdate(objective, node)
    local objectiveZone = ZONE:FindByName(objective.name)
    local objectiveLabelText = objectiveZone:GetProperty("label")
    local nodeZone = ZONE:FindByName(node.name)
    local nodeLabelText = nodeZone:GetProperty("label")

    local r = {}
    table.insert(r, "OBJECTIVE UPDATE")
    table.insert(r, "")
    table.insert(r, string.format("Enemy units at %s have surrendered in objective %s", nodeLabelText, objectiveLabelText))
    local m = table.concat(r, "\n")
    MESSAGE:New(m, 30):ToAll()
end

local function showNodeCapturedUpdate(objective, node, captureOrLost)
    local objectiveZone = ZONE:FindByName(objective.name)
    local objectiveLabelText = objectiveZone:GetProperty("label")
    local nodeZone = ZONE:FindByName(node.name)
    local nodeLabelText = nodeZone:GetProperty("label")

    local strandObjectiveStateMap = buildStrandObjectiveStateMap()

    local strandName
    local props

    for sn, p in pairs(strandObjectiveStateMap) do
        if p.activeObjective.displayName == objectiveLabelText then
            strandName = sn
            props = p
            break
        end
    end

    local r = {}
    table.insert(r, "OBJECTIVE UPDATE")
    table.insert(r, "")
    table.insert(r, string.format("%s has been %s at objective %s", nodeLabelText, captureOrLost, objectiveLabelText))
    local m = table.concat(r, "\n")
    MESSAGE:New(m, 30):ToAll()
end

local function showObjectiveStartedUpdate(objective)
    local objectiveZone = ZONE:FindByName(objective.name)
    local objectiveLabelText = objectiveZone:GetProperty("label")

    local strandObjectiveStateMap = buildStrandObjectiveStateMap()

    local strandName
    local props

    for sn, p in pairs(strandObjectiveStateMap) do
        if p.activeObjective.displayName == objectiveLabelText then
            strandName = sn
            props = p
            break
        end
    end

    local r = {}
    table.insert(r, "OBJECTIVE UPDATE")
    table.insert(r, "")
    table.insert(r, string.format("Objective %s is now active in %s", objectiveLabelText, strandName))
    local m = table.concat(r, "\n")
    MESSAGE:New(m, 30):ToAll()
end

local function showObjectiveCompletedUpdate(completedObjective, strandName, casevacCount)
    local objectiveZone = ZONE:FindByName(completedObjective.name)
    local objectiveLabelText = objectiveZone:GetProperty("label")

    local r = {}
    table.insert(r, "OBJECTIVE UPDATE")
    table.insert(r, "")
    table.insert(r, string.format("Objective %s has been completed in %s", objectiveLabelText, strandName))
    table.insert(r, "")
    table.insert(r, "CASEVAC UPDATE")
    table.insert(r, "")
    table.insert(r, string.format("%i new CASEVAC requests in the objective area", casevacCount))
    local m = table.concat(r, "\n")
    MESSAGE:New(m, 30):ToAll()
end

local function showFarpUnlockedUpdate(farp, strandName)
    local zone = ZONE:FindByName(farp.name)
    local labelText = zone:GetProperty("label")

    local r = {}
    table.insert(r, "FARP UPDATE")
    table.insert(r, "")
    table.insert(r, string.format("%s is now unlocked in %s", labelText, strandName))
    local m = table.concat(r, "\n")
    MESSAGE:New(m, 30):ToAll()
end

local function showRoadbaseUnlockedUpdate(roadbase, strandName)
    local zone = ZONE:FindByName(roadbase.name)
    local labelText = zone:GetProperty("label")

    local r = {}
    table.insert(r, "ROADBASE UPDATE")
    table.insert(r, "")
    table.insert(r, string.format("%s is now unlocked in %s", labelText, strandName))
    local m = table.concat(r, "\n")
    MESSAGE:New(m, 30):ToAll()
end

local function showCarrierUnlockedUpdate(carrier, strandName)
    local labelText = carrier.name

    local r = {}
    table.insert(r, "CARRIER UPDATE")
    table.insert(r, "")
    table.insert(r, string.format("%s is now unlocked in %s", labelText, strandName))
    local m = table.concat(r, "\n")
    MESSAGE:New(m, 30):ToAll()
end

local function showAirbaseUnlockedUpdate(airbase, strandName)
    local zone = ZONE:FindByName(airbase.name)
    local labelText = zone:GetProperty("label")

    local r = {}
    table.insert(r, "AIRBASE UPDATE")
    table.insert(r, "")
    table.insert(r, string.format("%s is now unlocked in %s", labelText, strandName))
    local m = table.concat(r, "\n")
    MESSAGE:New(m, 30):ToAll()
end

local function showIndustryPercentageUpdate()
    if(not MissionDb.industry.enabled) then
        return
    end

    local r = {}
    table.insert(r, "INDUSTRY UPDATE")
    table.insert(r, "")
    table.insert(r, string.format("Enemy industry is at %.f%% capacity, with %i active industry targets", MissionDb.industry.redPercentage, MissionDb.industry.redAlive))
    table.insert(r, "")
    table.insert(r, string.format("Friendly industry is at %.f%% capacity, with %i active industry structures", MissionDb.industry.bluePercentage, MissionDb.industry.blueAlive))
    local m = table.concat(r, "\n")
    MESSAGE:New(m, 30):ToAll()
end

local function calculateIndustryPercentage()
    local redAlive = 0
    local redTotal = 0
    for _, objective in ipairs(MissionDb.objectives) do
        for _, qrf in ipairs(objective.qrfs) do
            if qrf.state == "active" and #qrf.staticGroups > 0 then
                for _, static in ipairs(qrf.staticGroups) do
                    if string.find(static.name, "INDUSTRYTARGET") then
                        redTotal = redTotal + 1
                        if static.state ~= "dead" then
                            redAlive = redAlive + 1
                        end
                    end
                end
            end
        end
    end

    local redPercent = 100
    if redTotal > 0 then
        redPercent = UTILS.Round((redAlive / redTotal) * 100, 2)
    end

    local blueAlive = 0
    local blueTotal = 0
    for _, objective in ipairs(MissionDb.objectives) do
        for _, reinforcement in ipairs(objective.reinforcements) do
            if reinforcement.state == "active" and #reinforcement.staticGroups > 0 then
                for _, static in ipairs(reinforcement.staticGroups) do
                    if string.find(static.name, "INDUSTRYTARGET") then
                        blueTotal = blueTotal + 1
                        if static.state ~= "dead" then
                            blueAlive = blueAlive + 1
                        end
                    end
                end
            end
        end
    end

    local bluePercent = 100
    if blueTotal > 0 then
        bluePercent = UTILS.Round((blueAlive / blueTotal) * 100, 2)
    end

    local changed = MissionDb.industry.redPercentage ~= redPercent or MissionDb.industry.redAlive ~= redAlive or MissionDb.industry.bluePercentage ~= bluePercent or MissionDb.industry.blueAlive ~= blueAlive

    MissionDb.industry.redPercentage = redPercent
    MissionDb.industry.redAlive = redAlive
    MissionDb.industry.bluePercentage = bluePercent
    MissionDb.industry.blueAlive = blueAlive
    MissionDb.industry.blueEnabled = not (bluePercent == 100 and blueAlive == 0)
    MissionDb.industry.redEnabled = not (redPercent == 100 and redAlive == 0)
    MissionDb.industry.enabled = MissionDb.industry.blueEnabled or MissionDb.industry.redEnabled

    if changed then
        showIndustryPercentageUpdate()
    end
end

local function enemyReinforceZone(targetZoneName)
    if not MissionDb.enableConvoys then
        return
    end

    local zone = ZONE:FindByName(targetZoneName)
    local label  = zone:GetProperty("label")
    local targetCoord = zone:GetCoordinate():GetClosestPointToRoad()

    local closestQrf = nil
    local closestQrfDistance = nil

    -- TODO: consider a max response distance, set as a property on the qrf zone
    for _, objective in ipairs(MissionDb.objectives) do
        for _, qrf in ipairs(objective.qrfs) do
            if qrf.state == "active" and #qrf.spawnGroups > 0 then
                local qrfZone = ZONE:FindByName(qrf.name)
                local qrfCoordinate = qrfZone:GetCoordinate()
                local distance = qrfCoordinate:DistanceFromPointVec2(targetCoord)
                if closestQrf == nil or distance < closestQrfDistance then
                    closestQrf = qrf
                    closestQrfDistance = distance
                end
            end
        end
    end

    if closestQrf ~= nil then
        local qrfZone = ZONE:FindByName(closestQrf.name)
        local sg = closestQrf.spawnGroups[math.random(#closestQrf.spawnGroups)]
        local g = SPAWN:NewWithAlias(sg.name, string.format("%s-%d", sg.name, math.random(1,100000))):SpawnInZone(qrfZone, true)

        g:OptionDisperseOnAttack(0)

        local ag = ARMYGROUP:New(g)
        ag:Activate()

        local gUnits = g:GetUnits()
        for _, gUnit in ipairs(gUnits) do
            if not gUnit:HasSEAD() then
                gUnit:OptionEngageRange(50)
            end
        end

        local guardMission = AUFTRAG:NewARMOREDGUARD(targetCoord)
        guardMission:SetEngageDetected()
        ag:AddMission(guardMission)

        function ag:OnAfterPassingWaypoint(From, Event, To, Waypoint)
            if ag:HasPassedFinalWaypoint() then
                MESSAGE:New(string.format("Enemy reinforcement convoy has arrived in %s.", label), 30):ToAll()
                guardMission:Cancel()
                local patrolMission = AUFTRAG:NewPATROLZONE(zone, ag:GetSpeedCruise())
                patrolMission:SetEngageDetected()
                ag:AddMission(patrolMission)

                -- Cancel the patrol mission after 5 minutes.
                SCHEDULER:New(nil, function()
                    patrolMission:Cancel()
                end, {}, 300)
            end
        end

        local sourceCoord =  ag:GetCoordinate()
        MESSAGE:New(string.format("Enemy reinforcement convoy enroute to %s from %s, traveling approximately %s km.", label, sourceCoord:ToStringMGRS(), UTILS.Round(closestQrfDistance/1000,0)), 30):ToAll()
    end

end

local function friendlyReinforceZone(targetZoneName)
    if not MissionDb.enableConvoys then
        return
    end

    local zone = ZONE:FindByName(targetZoneName)
    local label = zone:GetProperty("label")
    local targetCoord = zone:GetCoordinate():GetClosestPointToRoad()

    local closestReinforcement = nil
    local closestReinforcementDistance = nil

    -- TODO: consider a max response distance, set as a property on the reinforcement zone
    for _, objective in ipairs(MissionDb.objectives) do
        for _, reinforcement in ipairs(objective.reinforcements) do
            if reinforcement.state == "active" and #reinforcement.spawnGroups > 0  then
                local reinforcementZone = ZONE:FindByName(reinforcement.name)
                local reinforcementCoordinate = reinforcementZone:GetCoordinate()
                local distance = reinforcementCoordinate:DistanceFromPointVec2(targetCoord)
                if closestReinforcement == nil or distance < closestReinforcementDistance then
                    closestReinforcement = reinforcement
                    closestReinforcementDistance = distance
                end
            end
        end
    end

    if closestReinforcement ~= nil then
        local reinforcementZone = ZONE:FindByName(closestReinforcement.name)
        local sg = closestReinforcement.spawnGroups[math.random(#closestReinforcement.spawnGroups)]
        local g = SPAWN:NewWithAlias(sg.name, string.format("%s-%d", sg.name, math.random(1,100000))):SpawnInZone(reinforcementZone, true)

        g:OptionDisperseOnAttack(0)
        g:HandleEvent( EVENTS.Dead )
        function g:OnEventDead( EventData )
            -- 100% of the time...
            if math.random(1, 100) <= MissionDb.settings.blueCasevacChance then
                local c = EventData.IniGroup:GetCoordinate()
                if c then
                    MissionDb.csar.instance:SpawnCASEVAC(c:Translate(math.random(1, 10), math.random(0, 359)), coalition.side.BLUE, "CASEVAC", false, "CASEVAC", "CASEVAC", true)
                end
            end
        end

        local ag = ARMYGROUP:New(g)
        ag:Activate()

        local gUnits = g:GetUnits()
        for _, gUnit in ipairs(gUnits) do
            if not gUnit:HasSEAD() then
                gUnit:OptionEngageRange(50)
            end
        end

        local guardMission = AUFTRAG:NewARMOREDGUARD(targetCoord)
        guardMission:SetEngageDetected()
        ag:AddMission(guardMission)

        function ag:OnAfterPassingWaypoint(From, Event, To, Waypoint)
            if ag:HasPassedFinalWaypoint() then
                MESSAGE:New(string.format("Friendly reinforcement convoy has arrived in %s.", label), 30):ToAll()
                guardMission:Cancel()
                local patrolMission = AUFTRAG:NewPATROLZONE(zone, ag:GetSpeedCruise())
                patrolMission:SetEngageDetected()
                ag:AddMission(patrolMission)

                -- Cancel the patrol mission after 5 minutes.
                SCHEDULER:New(nil, function()
                    patrolMission:Cancel()
                end, {}, 300)
            end
        end

        local sourceCoord =  ag:GetCoordinate()
        MESSAGE:New(string.format("Friendly reinforcement convoy enroute to %s from %s, traveling approximately %s km.", label, sourceCoord:ToStringMGRS(), UTILS.Round(closestReinforcementDistance/1000,0)), 30):ToAll()
    end

end

local function randomEnemyReinforcement()
    if not MissionDb.enableConvoys then
        return
    end

    local potentials = {}
    for _, objective in ipairs(MissionDb.objectives) do
        if objective.state == "active" then
            for _, node in ipairs(objective.nodes) do
                if node.state ~= "unstarted" then
                    table.insert(potentials, node.name)
                end
            end
        end
    end

    if #potentials > 0 then
        local chosenNodeName = potentials[math.random(#potentials)]
        enemyReinforceZone(chosenNodeName)
    end
end

local function industryAwareRandomEnemyReinforcement()
    if not MissionDb.enableConvoys then
        return
    end

    if MissionDb.industry.redEnabled and MissionDb.industry.redPercentage < 100 then
        local delaySeconds = (100 - MissionDb.industry.redPercentage)/100 * MissionDb.settings.redQrfMission.industryDelay
        MESSAGE:New(string.format("Enemy reinforcement convoy delayed by %s due to industry capacity of %.f%%.", UTILS.SecondsToClock(delaySeconds, true), MissionDb.industry.redPercentage), 30):ToAll()
        SCHEDULER:New(nil, function()
            randomEnemyReinforcement()
        end, {}, delaySeconds)
    else
        randomEnemyReinforcement()
    end
end

local function randomFriendlyReinforcement()
    if not MissionDb.enableConvoys then
        return
    end

    local potentials = {}
    for _, objective in ipairs(MissionDb.objectives) do
        if objective.state == "active" then
            for _, node in ipairs(objective.nodes) do
                if node.state ~= "unstarted" then
                    table.insert(potentials, node.name)
                end
            end
        end
    end

    if #potentials > 0 then
        local chosenNodeName = potentials[math.random(#potentials)]
        friendlyReinforceZone(chosenNodeName)
    end
end

local function standardAirwingReinforcement()
    local didIt = false
    for _, airwing in ipairs(MissionDb.redchief.airwings) do
        if airwing.state ~= "dead" and airwing.instance ~= nil then
            for _, squadron in ipairs(airwing.squadrons) do
                if squadron.instance ~= nil then
                    local airwing = squadron.instance:GetAirwing()
                    airwing:AddAssetToSquadron(squadron.instance, 1)
                end
            end
            didIt = true
        end
    end
    if didIt then
        MESSAGE:New(string.format("New airframes have been delivered to the enemy warehouses"), 30):ToAll()
    end
end

local function standardBrigadeReinforcement()
    local didIt = false
    for _, brigade in ipairs(MissionDb.redchief.brigades) do
        if brigade.state ~= "dead" and brigade.instance ~= nil then
            for _, platoon in ipairs(brigade.platoons) do
                if platoon.instance ~= nil then
                    local brigade = platoon.instance:GetBrigade()
                    brigade:AddAssetToPlatoon(platoon.instance, 1)
                end
            end
            didIt = true
        end
    end
    if didIt then
        MESSAGE:New(string.format("New ground units have been delivered to the enemy warehouses"), 30):ToAll()
    end
end

local function blueBrigadeReinforcement()
    for _, brigade in ipairs(MissionDb.bluechief.brigades) do
        if brigade.state == "active" then
            for _, platoon in ipairs(brigade.platoons) do
                local brigade = platoon.instance:GetBrigade()
                brigade:AddAssetToPlatoon(platoon.instance, 1)
            end
        end
    end
end

local function addOpsToken()
    MissionDb.counters.opstokens = MissionDb.counters.opstokens + 1
end

local function industryAwareBlueTokenSupply()
    if MissionDb.industry.blueEnabled and MissionDb.industry.bluePercentage < 100 then
        local delaySeconds = (100 - MissionDb.industry.bluePercentage)/100 * MissionDb.settings.blueIndustryTokenSupply.industryDelay
        MESSAGE:New(string.format("Goon ops token resupply delayed by %s due to industry capacity of %.f%%.", UTILS.SecondsToClock(delaySeconds, true), MissionDb.industry.bluePercentage), 30):ToAll()
        SCHEDULER:New(nil, function()
            addOpsToken()
            MESSAGE:New(string.format("Goon ops token supplied"), 30):ToAll()
        end, {}, delaySeconds)
    else
        addOpsToken()
        MESSAGE:New(string.format("Goon ops token supplied"), 30):ToAll()
    end
end

local function industryAwareStandardAirwingReinforcement()
    if MissionDb.industry.redEnabled and MissionDb.industry.redPercentage < 100 then
        local delaySeconds = (100 - MissionDb.industry.redPercentage)/100 * MissionDb.settings.redAirwingReinforcement.industryDelay
        MESSAGE:New(string.format("Enemy airframe delivery delayed by %s due to industry capacity of %.f%%.", UTILS.SecondsToClock(delaySeconds, true), MissionDb.industry.redPercentage), 30):ToAll()
        SCHEDULER:New(nil, function()
            standardAirwingReinforcement()
        end, {}, delaySeconds)
    else
        standardAirwingReinforcement()
    end
end

local function industryAwareStandardBrigadeReinforcement()
    if MissionDb.industry.redEnabled and MissionDb.industry.redPercentage < 100 then
        local delaySeconds = (100 - MissionDb.industry.redPercentage)/100 * MissionDb.settings.redBrigadeReinforcement.industryDelay
        MESSAGE:New(string.format("Enemy ground unit delivery delayed by %s due to industry capacity of %.f%%.", UTILS.SecondsToClock(delaySeconds, true), MissionDb.industry.redPercentage), 30):ToAll()
        SCHEDULER:New(nil, function()
            standardBrigadeReinforcement()
        end, {}, delaySeconds)
    else
        standardBrigadeReinforcement()
    end
end

local function nodeCaptured(objective, node, previousCoalition, newCoalition)
    if newCoalition == coalition.side.BLUE or previousCoalition == coalition.side.BLUE then
        if newCoalition == coalition.side.BLUE then
            showNodeCapturedUpdate(objective, node, "captured")
            if math.random(1, 100) <= 25 then
                enemyReinforceZone(node.name)
            end
        elseif previousCoalition == coalition.side.BLUE then
            showNodeCapturedUpdate(objective, node, "lost")
        end

        if math.random(1, 100) <= MissionDb.settings.nodeCaptureBlueCasevacChance then
            local nodeZone = ZONE:FindByName(node.name)
            local nodeLabel = nodeZone:GetProperty("label")
            MissionDb.csar.instance:SpawnCASEVAC(nodeZone:GetRandomPointVec2(), coalition.side.BLUE, string.format("%s casualty", nodeLabel), true, 'absolute unit', string.format("%s casualty", nodeLabel), true)
        end

        saveState()
    end

    checkObjectiveCapture(objective)
end

local function nodeGuarded(objective)
    checkObjectiveCapture(objective)
end

local function determineNextObjectiveFrom(objective)
    local strand
    for _, s in ipairs(MissionDb.strands) do
        if s.name == objective.strand then
            strand = s
            break
        end
    end

    local toStartName = nil

    for i, objectiveName in ipairs(strand.sequence) do
        if objectiveName == objective.name then
            local nextIndex = i+1
            if nextIndex <= #strand.sequence then
                toStartName = strand.sequence[i+1]
                break
            end
        end
    end

    if toStartName == nil then
        return nil
    end

    for _, objective in ipairs(MissionDb.objectives) do
        if objective.name == toStartName then
            return objective
        end
    end

    -- shouldn't get here
    return nil
end

local function spawnGroupsAtThing(thing, staticCountry)
    local skipGroupName = {}

    if thing.spawnGroups ~= nil then
        for _, group in ipairs(thing.spawnGroups) do
            skipGroupName[group.name] = true
        end
    end

    for _, category in ipairs({thing.vehicleGroups, thing.shipGroups}) do
        for _, group in ipairs(category) do
            if group.state ~= "dead" then
                if skipGroupName[group.name] ~= true then
                    group.state = "active"
                    local g = GROUP:FindByName(group.name)
                    if g and not g:IsActive() then
                        local gUnits = g:GetUnits()
                        for _, gUnit in ipairs(gUnits) do
                            if MissionDb.units[gUnit:Name()] == "dead" then
                                gUnit:Destroy(false)
                            else
                                MissionDb.units[gUnit:Name()] = "active"
                                if not gUnit:HasSEAD() then
                                    gUnit:OptionEngageRange(50)
                                end
                            end
                        end

                        g:OptionDisperseOnAttack(0)
                        g:Activate(0)

                        g:HandleEvent( EVENTS.Dead )
                        function g:OnEventDead( EventData )
                            MissionDb.units[EventData.IniUnitName] = "dead"
                            if g:CountAliveUnits() == 0 then
                                group.state = "dead"
                            end

                            if staticCountry == country.id.CJTF_BLUE then
                                -- 100% of the time...
                                if math.random(1, 100) <= MissionDb.settings.blueCasevacChance then
                                    local c = EventData.IniGroup:GetCoordinate()
                                    if c then
                                        MissionDb.csar.instance:SpawnCASEVAC(c:Translate(math.random(1, 10), math.random(0, 359)), coalition.side.BLUE, "CASEVAC", false, "CASEVAC", "CASEVAC", true)
                                    end
                                end
                            end
                        end
                    end
                end
            end
        end
    end

    if MissionDb.lateActivateStatics then
        for _, static in ipairs(thing.staticGroups) do
            if static.state ~= "dead" then
                local ss = SPAWNSTATIC:NewFromTemplate(static.template, staticCountry)
                local s = ss:Spawn()
                -- For some reason, certain statics refuse to spawn.
                if s ~= nil then
                    s:HandleEvent( EVENTS.Dead )
                    function s:OnEventDead( EventData )
                        if EventData.IniUnitName == static.name then
                            static.state = "dead"
                        end
                    end
                end
                static.state = "active"
            end
        end
    end

    if MissionDb.invokeOnActivate[thing.name] then
        MissionDb.invokeOnActivate[thing.name]()
    end
end

local function syncWarehouseStorage()
    local delay = 1
    if MissionDb.lateActivateStatics then
        MESSAGE:New(string.format("Syncing warehouse storage, hope you're not rearming..."), 5):ToAll()
        for _, objective in ipairs(MissionDb.objectives) do
            for _, farp in ipairs(objective.farps) do
                for _, static in ipairs(farp.staticGroups) do
                    if static.state == "active" then
                        if static.template.type == ENUMS.FARPObjectTypeNamesAndShape[ENUMS.FARPType.INVISIBLE].TypeName then
                            SCHEDULER:New(nil, function()
                                --MESSAGE:New(string.format("Clearing warehouse storage for %s - %s.", farp.name, static.name), 5):ToAll()
                                local warehouse = STORAGE:New(static.name)
                                warehouse:SetLiquid(STORAGE.Liquid.DIESEL, 0)
                                warehouse:SetLiquid(STORAGE.Liquid.GASOLINE, 0)
                                warehouse:SetLiquid(STORAGE.Liquid.JETFUEL, 0)
                                warehouse:SetLiquid(STORAGE.Liquid.MW50, 0)
                                for _, nitem in pairs(ENUMS.Storage.weapons) do
                                    for _, item in pairs(nitem) do
                                        warehouse:SetItem(item, 0)
                                    end
                                end
                            end, {}, delay)
                            delay = delay + 1
                            SCHEDULER:New(nil, function()
                                --MESSAGE:New(string.format("Syncing warehouse storage for %s - %s.", farp.name, static.name), 5):ToAll()
                                local warehouse = STORAGE:New(static.name)
                                warehouse:SetLiquid(STORAGE.Liquid.DIESEL, 100000)
                                warehouse:SetLiquid(STORAGE.Liquid.GASOLINE, 100000)
                                warehouse:SetLiquid(STORAGE.Liquid.JETFUEL, 100000)
                                warehouse:SetLiquid(STORAGE.Liquid.MW50, 100000)
                                for _, nitem in pairs(ENUMS.Storage.weapons) do
                                    for _, item in pairs(nitem) do
                                        warehouse:SetItem(item, 9999)
                                    end
                                end
                            end, {}, delay)
                            delay = delay + 1
                        end
                    end
                end
            end
            for _, roadbase in ipairs(objective.roadbases) do
                for _, static in ipairs(roadbase.staticGroups) do
                    if static.state == "active" then
                        if static.template.type == ENUMS.FARPObjectTypeNamesAndShape[ENUMS.FARPType.INVISIBLE].TypeName then
                            SCHEDULER:New(nil, function()
                                --MESSAGE:New(string.format("Clearing warehouse storage for %s - %s.", farp.name, static.name), 5):ToAll()
                                local warehouse = STORAGE:New(static.name)
                                warehouse:SetLiquid(STORAGE.Liquid.DIESEL, 0)
                                warehouse:SetLiquid(STORAGE.Liquid.GASOLINE, 0)
                                warehouse:SetLiquid(STORAGE.Liquid.JETFUEL, 0)
                                warehouse:SetLiquid(STORAGE.Liquid.MW50, 0)
                                for _, nitem in pairs(ENUMS.Storage.weapons) do
                                    for _, item in pairs(nitem) do
                                        warehouse:SetItem(item, 0)
                                    end
                                end
                            end, {}, delay)
                            delay = delay + 1
                            SCHEDULER:New(nil, function()
                                --MESSAGE:New(string.format("Syncing warehouse storage for %s - %s.", farp.name, static.name), 5):ToAll()
                                local warehouse = STORAGE:New(static.name)
                                warehouse:SetLiquid(STORAGE.Liquid.DIESEL, 100000)
                                warehouse:SetLiquid(STORAGE.Liquid.GASOLINE, 100000)
                                warehouse:SetLiquid(STORAGE.Liquid.JETFUEL, 100000)
                                warehouse:SetLiquid(STORAGE.Liquid.MW50, 100000)
                                for _, nitem in pairs(ENUMS.Storage.weapons) do
                                    for _, item in pairs(nitem) do
                                        warehouse:SetItem(item, 9999)
                                    end
                                end
                            end, {}, delay)
                            delay = delay + 1
                        end
                    end
                end
            end
            for _, qrf in ipairs(objective.qrfs) do
                for _, static in ipairs(qrf.staticGroups) do
                    if static.state == "active" then
                        if static.template.type == ENUMS.FARPObjectTypeNamesAndShape[ENUMS.FARPType.INVISIBLE].TypeName or static.template.type == ENUMS.FARPObjectTypeNamesAndShape[ENUMS.FARPType.FARP].TypeName then
                            SCHEDULER:New(nil, function()
                                --MESSAGE:New(string.format("Clearing warehouse storage for %s - %s.", farp.name, static.name), 5):ToAll()
                                local warehouse = STORAGE:New(static.name)
                                warehouse:SetLiquid(STORAGE.Liquid.DIESEL, 0)
                                warehouse:SetLiquid(STORAGE.Liquid.GASOLINE, 0)
                                warehouse:SetLiquid(STORAGE.Liquid.JETFUEL, 0)
                                warehouse:SetLiquid(STORAGE.Liquid.MW50, 0)
                                for _, nitem in pairs(ENUMS.Storage.weapons) do
                                    for _, item in pairs(nitem) do
                                        warehouse:SetItem(item, 0)
                                    end
                                end
                                -- Bullshit hardcoding of the airframes for Chief spawned ops
                                warehouse:SetItem('Mi-24P', 0)
                                warehouse:SetItem('Mi-26', 0)
                                warehouse:SetItem('Mi-28N', 0)
                                warehouse:SetItem('Ka-50 III', 0)
                                warehouse:SetItem('CH-47D', 0)
                            end, {}, delay)
                            delay = delay + 1
                            SCHEDULER:New(nil, function()
                                --MESSAGE:New(string.format("Syncing warehouse storage for %s - %s.", farp.name, static.name), 5):ToAll()
                                local warehouse = STORAGE:New(static.name)
                                warehouse:SetLiquid(STORAGE.Liquid.DIESEL, 100000)
                                warehouse:SetLiquid(STORAGE.Liquid.GASOLINE, 100000)
                                warehouse:SetLiquid(STORAGE.Liquid.JETFUEL, 100000)
                                warehouse:SetLiquid(STORAGE.Liquid.MW50, 100000)
                                for _, nitem in pairs(ENUMS.Storage.weapons) do
                                    for _, item in pairs(nitem) do
                                        warehouse:SetItem(item, 9999)
                                    end
                                end
                                -- Bullshit hardcoding of the airframes for Chief spawned ops
                                warehouse:SetItem('Mi-24P', 100)
                                warehouse:SetItem('Mi-26', 100)
                                warehouse:SetItem('Mi-28N', 100)
                                warehouse:SetItem('Ka-50 III', 100)
                                warehouse:SetItem('CH-47D', 100)
                            end, {}, delay)
                            delay = delay + 1
                        end
                    end
                end
            end
        end
    end
end

local function activateBrigades(chief, side)
    for _, brigade in ipairs(chief.brigades) do
        if brigade.state ~= "dead" and brigade.instance == nil then

            local warehouse = UNIT:FindByName(brigade.warehouse)
            if warehouse ~= nil then
                local isAlive = warehouse:IsAlive()
                if(isAlive == nil or not isAlive) then
                    warehouse = nil
                end
            end
            if warehouse == nil then
                warehouse = STATIC:FindByName(brigade.warehouse, false)
            end

            if warehouse ~= nil then
                brigade.instance = BRIGADE:New(brigade.warehouse, brigade.name)

                function brigade.instance:onafterDestroyed(From, Event, To)
                    brigade.state = "dead"
                    MESSAGE:New(string.format("Brigade warehouse at %s has been destroyed.", brigade.name), 15):ToAll()
                end

                if side == coalition.side.BLUE then
                    function brigade.instance:OnAfterArmyOnMission(From, Event, To, ArmyGroup, Mission)
                        local text=string.format("BLUE has launched a new mission: %s.", Mission:GetType())
                        MESSAGE:New(text, 15):ToAll()
                    end
                else
                    function brigade.instance:OnAfterArmyOnMission(From, Event, To, ArmyGroup, Mission)
                        local text=string.format("RED has launched a new mission: %s.", Mission:GetType())
                        MESSAGE:New(text, 15):ToAll()
                    end
                end

                for _, platoon in ipairs(brigade.platoons) do
                    platoon.instance = PLATOON:New(platoon.templateGroupName, platoon.initialInventory, platoon.name)
                    platoon.instance:SetSkill(AI.Skill.EXCELLENT)

                    for _, capability in ipairs(platoon.capabilities) do
                        platoon.instance:AddMissionCapability({capability.mission}, capability.performance)
                    end

                    brigade.instance:AddPlatoon(platoon.instance)
                end
                chief.instance:AddBrigade(brigade.instance)
                brigade.state = "active"
            end
        end
    end
end

local function activateAirwings(chief, side)
    for _, airwing in ipairs(chief.airwings) do
        if airwing.state ~= "dead" and airwing.instance == nil then

            local warehouse = UNIT:FindByName(airwing.warehouse)
            if warehouse ~= nil then
                local isAlive = warehouse:IsAlive()
                if(isAlive == nil or not isAlive) then
                    warehouse = nil
                end
            end
            if warehouse == nil then
                warehouse = STATIC:FindByName(airwing.warehouse, false)
            end

            if warehouse ~= nil then
                airwing.instance = AIRWING:New(airwing.warehouse, airwing.name)

                local airbase = AIRBASE:FindByName(airwing.airbase)
                if airbase == nil then
                    MESSAGE:New(string.format("Couldn't find airbase %s", airwing.airbase), 15):ToAll()
                else
                    airwing.instance:SetAirbase(airbase)
                end

                function airwing.instance:onafterDestroyed(From, Event, To)
                    airwing.state = "dead"
                    MESSAGE:New(string.format("Airwing warehouse at %s has been destroyed.", airwing.airbase), 15):ToAll()
                end

                if side == coalition.side.BLUE then
                    function airwing.instance:OnAfterFlightOnMission(From, Event, To, Flightgroup, Mission)
                        if Mission:GetType() == AUFTRAG.Type.AWACS then
                            Mission:SetMissionAltitude(30000)
                        end

                        local text=string.format("BLUE has launched a new mission: %s.", Mission:GetType())
                        MESSAGE:New(text, 15):ToAll()
                    end
                else
                    function airwing.instance:OnAfterAirbaseCaptured(From, Event, To, Coalition)
                        MESSAGE:New("AIRBASE CAPTURED!", 15):ToAll()
                        if Coalition == coalition.side.BLUE then
                            -- SCHEDULER:New(nil, function()
                                if airwing.state ~= "dead" then
                                    airwing.state = "dead"
                                    local wh = STATIC:FindByName(airwing.warehouse)
                                    if wh then
                                        wh:GetCoordinate():Explosion(999)
                                        local text=string.format("Friendly forces have destroyed the enemy airwing at %s.", airwing.airbase)
                                        MESSAGE:New(text, 15):ToAll()
                                    end
                                end
                            -- end, {}, 1)
                        end
                    end

                    function airwing.instance:OnAfterFlightOnMission(From, Event, To, Flightgroup, Mission)
                        if Mission:GetType() == AUFTRAG.Type.BOMBCARPET or Mission:GetType() == AUFTRAG.Type.BAI then
                            if math.random(1, 100) <= MissionDb.settings.airBombingEscortChance then
                                local escortMission = AUFTRAG:NewESCORT(Flightgroup:GetGroup())
                                MissionDb.redchief.instance:AddMission(escortMission)
                            end
                        end

                        if Mission:GetType() == AUFTRAG.Type.BOMBCARPET then
                            Mission:SetMissionAltitude(25000)
                        end

                        if Mission:GetType() == AUFTRAG.Type.AWACS then
                            Mission:SetMissionAltitude(30000)
                            -- local escortMission = AUFTRAG:NewESCORT(Flightgroup:GetGroup())
                            -- MissionDb.redchief.instance:AddMission(escortMission)
                            --MissionDb.samnetwork.instance:SetAwacs(Flightgroup:GetName())
                        end

                        local text=string.format("RED has launched a new mission: %s.", Mission:GetType())
                        MESSAGE:New(text, 15):ToAll()
                    end
                end

                for _, squadron in ipairs(airwing.squadrons) do
                    squadron.instance = SQUADRON:New(squadron.templateGroupName, squadron.initialInventory, squadron.name)
                    squadron.instance:SetSkill(AI.Skill.EXCELLENT)
                    squadron.instance:SetTakeoffHot()

                    if squadron.takeoffCold then
                        squadron.instance:SetTakeoffCold()
                    end

                    if squadron.parking then
                        squadron.instance:SetParkingIDs(squadron.parking)
                    end

                    for _, capability in ipairs(squadron.capabilities) do
                        squadron.instance:AddMissionCapability({capability.mission}, capability.performance)
                    end
                    squadron.instance:SetLivery(squadron.livery)

                    airwing.instance:AddSquadron(squadron.instance)
                    for _, payload in ipairs(squadron.payloads) do
                        airwing.instance:NewPayload(GROUP:FindByName(payload.templateGroupName), -1, payload.missionTypes)
                    end
                end

                chief.instance:AddAirwing(airwing.instance)
                airwing.state = "active"
            end
        end
    end
end

local function unlockFarpsForObjective(objective)
    for _, farp in ipairs(objective.farps) do
        spawnGroupsAtThing(farp, country.id.CJTF_BLUE)
        MissionDb.ctld.instance:AddCTLDZone(farp.name, CTLD.CargoZoneType.LOAD, SMOKECOLOR.Blue, true, false)

        local farpZone = ZONE:FindByName(farp.name)
        local farpLabelText = farpZone:GetProperty("label")
        farp.labelMarkId = farpZone:GetCoordinate(0):Translate(farpZone.Radius + 50, 0, false, true):TextToAll(farpLabelText, -1, {0,0,1}, 1, {1,1,1}, 0.0, 20, true)
        farp.circleMarkId = farpZone:GetCoordinate(0):CircleToAll(farpZone.Radius, -1, {0,0,1}, 1, {0,0,1}, 0.15, 2, true)

        for _, client in ipairs(farp.clients) do
            local farpSlot = USERFLAG:New(client)
            farpSlot:Set(0)
        end

        showFarpUnlockedUpdate(farp, objective.strand)

        SCHEDULER:New(nil, function()
            farpZone:GetCoordinate(0):SmokeGreen()
        end, {}, 1, 300)

        SCHEDULER:New(nil, function()
            farpZone:GetCoordinate(500):IlluminationBomb()
        end, {}, 1, 150)
    end
end

local function unlockRoadbasesForObjective(objective)
    for _, roadbase in ipairs(objective.roadbases) do
        spawnGroupsAtThing(roadbase, country.id.CJTF_BLUE)

        local roadbaseZone = ZONE:FindByName(roadbase.name)
        local roadbaseLabelText = roadbaseZone:GetProperty("label")
        roadbase.labelMarkId = roadbaseZone:GetCoordinate(0):Translate(roadbaseZone:GetRadius() + 50, 0, false, true):TextToAll(roadbaseLabelText, -1, {0,0,1}, 1, {1,1,1}, 0.0, 20, true)

        for _, client in ipairs(roadbase.clients) do
            local roadbaseSlot = USERFLAG:New(client)
            roadbaseSlot:Set(0)
        end

        showRoadbaseUnlockedUpdate(roadbase, objective.strand)
    end
end

local function unlockCarriersForObjective(objective)
    for _, carrier in ipairs(objective.carriers) do
        local unitName = string.format("%s Unit #1", carrier.name)

        -- Hardcoded for now...
        if carrier.name == "Tarawa" or carrier.name == "Peleliu" or carrier.name == "Saipan" or carrier.name == "Nassau" then
            MissionDb.ctld.instance:AddCTLDZone(unitName, CTLD.CargoZoneType.SHIP, SMOKECOLOR.Blue, true, false, 240, 20)
        end

        local ng = NAVYGROUP:New(carrier.name)
        ng:SetDefaultInvisible(true)
        ng:SwitchInvisible(true)
        ng:ClearWaypoints()
        ng:SetPatrolAdInfinitum(true)

        for _, waypoint in ipairs(carrier.waypoints) do
            ng:AddWaypoint(COORDINATE:New(waypoint.x, 0, waypoint.y), waypoint.speed, nil, 0, true)
        end

        ng:SwitchTACAN(carrier.tacan_channel)
        ng:SwitchRadio(carrier.radio)

        if carrier.icls_channel ~= nil then
            ng:SwitchICLS(carrier.icls_channel)
        end

        if carrier.link4 ~= nil then
            local g = ng:GetGroup()
            g:CommandActivateLink4(carrier.link4)
            g:CommandActivateACLS()
        end

        for _, client in ipairs(carrier.clients) do
            local carrierSlot = USERFLAG:New(client)
            carrierSlot:Set(0)
        end

        showCarrierUnlockedUpdate(carrier, objective.strand)
    end
end

local function unlockAirbasesForObjective(objective)
    for _, airbase in ipairs(objective.airbases) do
        if airbase.unlocked == nil then
            spawnGroupsAtThing(airbase, country.id.CJTF_BLUE)
            MissionDb.ctld.instance:AddCTLDZone(airbase.name, CTLD.CargoZoneType.LOAD, SMOKECOLOR.Blue, true, false)

            local airbaseZone = ZONE:FindByName(airbase.name)
            MissionDb.bluechief.instance:AddBorderZone(airbaseZone)

            for _, client in ipairs(airbase.clients) do
                local airbaseSlot = USERFLAG:New(client)
                airbaseSlot:Set(0)
            end

            showAirbaseUnlockedUpdate(airbase, objective.strand)
            airbase.unlocked = true
        end
    end
end

local function unlockReinforcementsForObjective(objective)
    for _, reinforcement in ipairs(objective.reinforcements) do
        if reinforcement.state ~= "dead" then
            reinforcement.state = "active"
            spawnGroupsAtThing(reinforcement, country.id.CJTF_BLUE)
        
            local reinforcementZone = ZONE:FindByName(reinforcement.name)
            local reinforcementLabelText = reinforcementZone:GetProperty("label")
            if reinforcementLabelText ~= "" then
                reinforcement.labelMarkId = reinforcementZone:GetCoordinate(0):Translate(reinforcementZone:GetRadius() + 50, 0, false, true):TextToAll(reinforcementLabelText, -1, {0,0,0}, 1, {1,1,1}, 0.0, 20, true)
                reinforcement.circleMarkId = reinforcementZone:GetCoordinate(0):CircleToAll(reinforcementZone:GetRadius(), -1, {0,0,1}, 1, {0,0,1}, 0.15, 3, true)
            end
        end
    end
end

local function unlockQrfsForObjective(objective)
    for _, qrf in ipairs(objective.qrfs) do
        if qrf.state ~= "dead" then
            qrf.state = "active"
            spawnGroupsAtThing(qrf, country.id.CJTF_RED)

            local qrfZone = ZONE:FindByName(qrf.name)
            local qrfLabelText = qrfZone:GetProperty("label")
            if qrfLabelText ~= "" then
                qrf.labelMarkId = qrfZone:GetCoordinate(0):Translate(qrfZone:GetRadius() + 50, 0, false, true):TextToAll(qrfLabelText, -1, {0,0,0}, 1, {1,1,1}, 0.0, 20, true)
                qrf.circleMarkId = qrfZone:GetCoordinate(0):CircleToAll(qrfZone:GetRadius(), -1, {1,0,0}, 1, {1,0,0}, 0.15, 3, true)
            end
        end
    end
end

local function updateBorderZones()
    MissionDb.redchief.borderZones:Clear()
    for _, objective in ipairs(MissionDb.objectives) do
        if objective.state == "active" then
            for _, borderZoneName in ipairs(objective.borderZones) do
                local borderZone = ZONE:FindByName(borderZoneName)
                MissionDb.redchief.borderZones:AddZone(borderZone)
            end
        end
    end
end

local function updateRedAwacsZones()
    local intendedAwacsZones = {}
    for _, objective in ipairs(MissionDb.objectives) do
        if objective.state == "active" then
            for _, awacsZoneName in ipairs(objective.redAwacsZones) do
                table.insert(intendedAwacsZones, awacsZoneName)
            end
        end
    end

    local commander = MissionDb.redchief.instance:GetCommander()

    for i=#commander.awacsZones,1,-1 do
        local awacsZone = commander.awacsZones[i]
        local found = false
        for _, awacsZoneName in ipairs(intendedAwacsZones) do
            if awacsZoneName == awacsZone.zone:GetName() then
                found = true
                break
            end
        end
        if not found then
            table.remove(commander.awacsZones, i)
            MissionDb.redchief.instance:RemoveAwacsZone(awacsZone)
        end
    end

    for i=#intendedAwacsZones,1,-1 do
        local awacsZoneName = intendedAwacsZones[i]
        local found = false
        for _, awacsZone in ipairs(commander.awacsZones) do
            if awacsZoneName == awacsZone.zone:GetName() then
                found = true
                break
            end
        end
        if found then
            table.remove(intendedAwacsZones, i)
        end
    end

    for _, awacsZoneName in ipairs(intendedAwacsZones) do
        local awacsZone = ZONE:FindByName(awacsZoneName)
        MissionDb.redchief.instance:AddAwacsZone(awacsZone)
    end
end

local function updateBlueAwacsZones()
    local intendedAwacsZones = {}
    for _, objective in ipairs(MissionDb.objectives) do
        if objective.state == "active" then
            for _, awacsZoneName in ipairs(objective.blueAwacsZones) do
                table.insert(intendedAwacsZones, awacsZoneName)
            end
        end
    end

    local commander = MissionDb.bluechief.instance:GetCommander()

    for i=#commander.awacsZones,1,-1 do
        local awacsZone = commander.awacsZones[i]
        local found = false
        for _, awacsZoneName in ipairs(intendedAwacsZones) do
            if awacsZoneName == awacsZone.zone:GetName() then
                found = true
                break
            end
        end
        if not found then
            table.remove(commander.awacsZones, i)
            MissionDb.bluechief.instance:RemoveAwacsZone(awacsZone)
        end
    end

    for i=#intendedAwacsZones,1,-1 do
        local awacsZoneName = intendedAwacsZones[i]
        local found = false
        for _, awacsZone in ipairs(commander.awacsZones) do
            if awacsZoneName == awacsZone.zone:GetName() then
                found = true
                break
            end
        end
        if found then
            table.remove(intendedAwacsZones, i)
        end
    end

    for _, awacsZoneName in ipairs(intendedAwacsZones) do
        local awacsZone = ZONE:FindByName(awacsZoneName)
        MissionDb.bluechief.instance:AddAwacsZone(awacsZone)
    end
end

-- TODO: parameterize these
local function updateAwacsZones()
    updateRedAwacsZones()
    updateBlueAwacsZones()
end

local function updateCapZones()
    local intendedCapZones = {}
    for _, objective in ipairs(MissionDb.objectives) do
        if objective.state == "active" then
            for _, capZoneName in ipairs(objective.capZones) do
                table.insert(intendedCapZones, capZoneName)
            end
        end
    end

    local commander = MissionDb.redchief.instance:GetCommander()

    for i=#commander.capZones,1,-1 do
        local capZone = commander.capZones[i]
        local found = false
        for _, capZoneName in ipairs(intendedCapZones) do
            if capZoneName == capZone.zone:GetName() then
                found = true
                break
            end
        end
        if not found then
            table.remove(commander.capZones, i)
        end
    end

    for i=#intendedCapZones,1,-1 do
        local capZoneName = intendedCapZones[i]
        local found = false
        for _, capZone in ipairs(commander.capZones) do
            if capZoneName == capZone.zone:GetName() then
                found = true
                break
            end
        end
        if found then
            table.remove(intendedCapZones, i)
        end
    end

    for _, capZoneName in ipairs(intendedCapZones) do
        local capZone = ZONE:FindByName(capZoneName)
        MissionDb.redchief.instance:AddCapZone(capZone)
    end
end

local function startObjective(objective)
    local objectiveZone = ZONE:FindByName(objective.name)

    if #objective.nodes > 0 then
        local objectiveLabelText = objectiveZone:GetProperty("label")
        objective.labelMarkId = objectiveZone:GetCoordinate(0):TextToAll(objectiveLabelText, -1, {0,0,0}, 1, {1,1,1}, 0.0, 20, true)

        MissionDb.redchief.conflictZones:AddZone(objectiveZone)
        MissionDb.bluechief.conflictZones:AddZone(objectiveZone)
    end

    for _, node in ipairs(objective.nodes) do
        local initialOwner = coalition.side.NEUTRAL
        if(node.state == "red") then
            initialOwner = coalition.side.RED
        elseif node.state == "blue" then
            initialOwner = coalition.side.BLUE
        end

        local nodeZone = ZONE:FindByName(node.name)
        node.opsZone = OPSZONE:New(nodeZone, initialOwner)
        node.opsZone:SetObjectCategories({Object.Category.UNIT})
        node.opsZone:SetDrawZone(true)
        node.opsZone:SetMarkZone(false)
        function node.opsZone:OnAfterCaptured(From, Event, To, Coalition)
            if Coalition == coalition.side.BLUE then
                node.state = "blue"
            elseif Coalition == coalition.side.RED then
                node.state = "red"
            end
            nodeCaptured(objective, node, node.opsZone:GetPreviousOwner(), Coalition)
        end
        function node.opsZone:OnAfterGuarded(From, Event, To)
            nodeGuarded(objective)
        end
        function node.opsZone:OnAfterEvaluated(From, Event, To)
            local surrender = false
            if node.redSurrenderThreshold ~= "" and node.opsZone.Nred > 0 and node.opsZone.Nred <= node.redSurrenderThreshold then
                if node.blueCaptureThreshold ~= "" then
                    if node.opsZone.Nblu >= node.blueCaptureThreshold then
                        surrender = true
                    end
                else
                    surrender = true
                end
            end
            if surrender then
                node.opsZone:GetScannedUnitSet():ForEachUnit(function(unit)
                    if unit:GetCoalition() == coalition.side.RED then
                        unit:Destroy()
                    end
                end)
                showNodeSurrenderUpdate(objective, node)
            end
        end
        node.opsZone:Start()
        local nodeLabelText = nodeZone:GetProperty("label")
        node.labelMarkId = nodeZone:GetCoordinate(0):Translate(nodeZone.Radius + 50, 0, false, true):TextToAll(nodeLabelText, -1, {0,0,0}, 1, {1,1,1}, 0.0, 14, true)

        MissionDb.ctld.instance:AddCTLDZone(node.name, CTLD.CargoZoneType.MOVE, SMOKECOLOR.Blue, true, false)

        MissionDb.redchief.instance:AddStrategicZone(node.opsZone, 50, nil, MissionDb.redchief.strategicZoneResources.defaultOccupied, MissionDb.redchief.strategicZoneResources.defaultEmpty)
        MissionDb.bluechief.instance:AddStrategicZone(node.opsZone, 50, nil, MissionDb.bluechief.strategicZoneResources.defaultOccupied, MissionDb.bluechief.strategicZoneResources.defaultEmpty)
    end

    spawnGroupsAtThing(objective, country.id.CJTF_RED)

    for _, task in ipairs(objective.tasks) do
        if task.state ~= "finished" then
            spawnGroupsAtThing(task, country.id.CJTF_RED)

            local taskZone = ZONE:FindByName(task.name)
            local taskLabel = taskZone:GetProperty("label")
            local taskAuftrag = taskZone:GetProperty("auftrag")
            local taskDescription = taskZone:GetProperty("description")
            task.label = taskLabel

            -- Might consider FilterZones, but it only works for active units
            -- local targSet = SET_GROUP:New():FilterZones({taskZone}):FilterCoalitions("red"):FilterPrefixes(taskTargetNameContains):FilterOnce()
            if taskAuftrag == "ANTISHIP" then
                local taskGroupTargetNameContains = taskZone:GetProperty("groupTargetNameContains")
                local targSet = SET_GROUP:New():FilterCoalitions("red"):FilterPrefixes(taskGroupTargetNameContains):FilterOnce()
                local target = TARGET:New(targSet)
                task.instance = PLAYERTASK:New(AUFTRAG.Type.ANTISHIP, target, true , 99, "")
                task.instance:SetMenuName(taskLabel)
                task.instance:AddFreetext(taskDescription)

                local taskTargetUnitTypes = taskZone:GetProperty("targetUnitTypes")
                if taskTargetUnitTypes ~= "" then
                    task.instance:AddConditionSuccess(function()
                        local anyOfTypeAlive = true
                        targSet:ForEachGroup(function(g)
                            local gUnits = g:GetUnits()
                            for _, gUnit in ipairs(gUnits) do
                                if anyOfTypeAlive and gUnit:IsAlive() and string.match(taskTargetUnitTypes, gUnit:GetTypeName()) then
                                    anyOfTypeAlive = false
                                end
                            end
                        end)
                        return anyOfTypeAlive
                    end)
                end

                function task.instance:OnAfterSuccess(From, Event, To)
                    task.state = "finished"
                    checkObjectiveCapture(objective)
                    saveState()
                end

                MissionDb.strandtasks.instance:AddPlayerTaskToQueue(task.instance)
            elseif taskAuftrag == "SEAD" then
                local taskGroupTargetNameContains = taskZone:GetProperty("groupTargetNameContains")
                local targSet = SET_GROUP:New():FilterCoalitions("red"):FilterPrefixes(taskGroupTargetNameContains):FilterOnce()
                local target = TARGET:New(targSet)
                task.instance = PLAYERTASK:New(AUFTRAG.Type.SEAD, target, true , 99, "")
                task.instance:SetMenuName(taskLabel)
                task.instance:AddFreetext(taskDescription)

                local taskTargetUnitTypes = taskZone:GetProperty("targetUnitTypes")
                if taskTargetUnitTypes ~= "" then
                    task.instance:AddConditionSuccess(function()
                        local anyOfTypeAlive = true
                        targSet:ForEachGroup(function(g)
                            local gUnits = g:GetUnits()
                            for _, gUnit in ipairs(gUnits) do
                                if anyOfTypeAlive and gUnit:IsAlive() and string.match(taskTargetUnitTypes, gUnit:GetTypeName()) then
                                    anyOfTypeAlive = false
                                end
                            end
                        end)
                        return anyOfTypeAlive
                    end)
                end

                function task.instance:OnAfterSuccess(From, Event, To)
                    task.state = "finished"
                    checkObjectiveCapture(objective)
                    saveState()
                end

                MissionDb.strandtasks.instance:AddPlayerTaskToQueue(task.instance)
            elseif taskAuftrag == "BOMBING" then
                local taskGroupTargetNameContains = taskZone:GetProperty("groupTargetNameContains")
                local taskStaticTargetNameContains = taskZone:GetProperty("staticTargetNameContains")

                local possibleSets = {}

                if taskGroupTargetNameContains ~= "" then
                    local set = SET_GROUP:New():FilterCoalitions("red"):FilterPrefixes(taskGroupTargetNameContains):FilterStart()
                    table.insert(possibleSets, set)
                end

                if taskStaticTargetNameContains ~= "" then
                    local set = SET_STATIC:New():FilterCoalitions("red"):FilterPrefixes(taskStaticTargetNameContains):FilterStart()
                    table.insert(possibleSets, set)
                end

                local sceneryTargetZoneNames = taskZone:GetProperty("sceneryTargetZoneNames")
                if sceneryTargetZoneNames ~= "" then
                    local zones = UTILS.Split(sceneryTargetZoneNames, ",")
                    for _, zoneName in ipairs(zones) do
                        local set = SET_SCENERY:NewFromZone(zoneName)
                        table.insert(possibleSets, set)
                    end
                end

                local target = TARGET:New(possibleSets[1])

                for i, s in ipairs(possibleSets) do
                    if i > 1 then
                        target:AddObject(s)
                    end
                end

                task.instance = PLAYERTASK:New(AUFTRAG.Type.BOMBING, target, true , 99, "")
                task.instance:SetMenuName(taskLabel)
                task.instance:AddFreetext(taskDescription)

                -- todo, include the targetTypes stuff

                function task.instance:OnAfterSuccess(From, Event, To)
                    for _, s in ipairs(possibleSets) do
                        s:FilterStop()
                    end
                    task.state = "finished"
                    checkObjectiveCapture(objective)
                    saveState()
                end

                MissionDb.strandtasks.instance:AddPlayerTaskToQueue(task.instance)
            elseif taskAuftrag == "CSAR" then
                local targetZoneName = taskZone:GetProperty("targetZone")
                local targetName = taskZone:GetProperty("targetName")
                local targetZone = ZONE:FindByName(targetZoneName)

                local target = TARGET:New(targetZone)
                task.instance = PLAYERTASK:New(AUFTRAG.Type.CSAR, target, true , 99, "")
                task.instance:SetSubType("Boarded")
                task.instance:SetMenuName(taskLabel)
                task.instance:AddFreetext(taskDescription)
                task.instance.CSARPilotName = targetName
                task.instance.SmokeColor = SMOKECOLOR.Blue
                function task.instance:OnAfterSuccess(From, Event, To)
                    task.state = "finished"
                    checkObjectiveCapture(objective)
                    saveState()
                end
                MissionDb.strandtasks.instance:AddPlayerTaskToQueue(task.instance)
                MissionDb.csar.instance:AddPlayerTask(task.instance)

                MissionDb.csar.instance:SpawnCSARAtZone(targetZone, coalition.side.BLUE, targetName, true, true, nil, nil, true)
            end
        end
    end

    unlockFarpsForObjective(objective)
    unlockRoadbasesForObjective(objective)
    unlockCarriersForObjective(objective)
    unlockAirbasesForObjective(objective)
    unlockReinforcementsForObjective(objective)
    unlockQrfsForObjective(objective)

    objective.state = "active"

    saveState()

    SCHEDULER:New(nil, function()
        showObjectiveStartedUpdate(objective)
    end, {}, 5)

    SCHEDULER:New(nil, function()
        activateAirwings(MissionDb.bluechief, coalition.side.BLUE)
        activateAirwings(MissionDb.redchief, coalition.side.RED)
        activateBrigades(MissionDb.bluechief, coalition.side.BLUE)
        activateBrigades(MissionDb.redchief, coalition.side.RED)
        saveState()
    end, {}, 15)

    -- Not sure that I actually want this "prespwaning" going on anymore.
    --
    -- local nextObjective = determineNextObjectiveFrom(objective)
    -- if nextObjective ~= nil then
    --     local nextObjectiveZone = ZONE:FindByName(nextObjective.name)
    --     if nextObjectiveZone:Get2DDistance(objectiveZone:GetCoordinate(0)) > 37040 then
    --         SCHEDULER:New(nil, function()
    --             spawnGroupsAtThing(nextObjective, country.id.CJTF_RED)
    --         end, {}, 270)
    --     end
    -- end

    updateBorderZones()
    updateAwacsZones()
    updateCapZones()
end

local function spawnCasevacForCompletedObjective(objective)
    local objectiveZone = ZONE:FindByName(objective.name)
    local objectiveLabel = objectiveZone:GetProperty("label")
    local count = math.random(1, #objective.nodes)
    for i=1, count do
        MissionDb.csar.instance:SpawnCASEVAC(objectiveZone:GetRandomPointVec2(), coalition.side.BLUE, string.format("%s casualty", objectiveLabel), true, 'absolute unit', 'whatever', true)
    end
    return count
end

local function progressToNextObjectiveFrom(completedObjective, strandName)
    local strand
    for _, s in ipairs(MissionDb.strands) do
        if s.name == strandName then
            strand = s
            break
        end
    end

    local toStartName = nil
    local strandComplete = false
    local missionComplete = false

    if completedObjective == nil then
        -- we don't know which one, so figure it out...
        local strandStateMap = {}
        for _, objectiveName in ipairs(strand.sequence) do
            for _, objective in ipairs(MissionDb.objectives) do
                if objective.name == objectiveName then
                    strandStateMap[objectiveName] = objective.state
                end
            end
        end

        for _, objectiveName in ipairs(strand.sequence) do
            local state = strandStateMap[objectiveName]
            if state == "active" or state == "unstarted" then
                toStartName = objectiveName
                break
            end
        end

        if toStartName == nil then
            strandComplete = true
            -- this strand is done, but we need to check the others before we reset it
            local anyObjectiveNotFinished = false
            for _, objective in ipairs(MissionDb.objectives) do
                if objective.strand ~= strandName and state ~= "finished" then
                    anyObjectiveNotFinished = true
                    break
                end
            end
            if not anyObjectiveNotFinished then
                missionComplete = true
            end
        end
    else
        for i, objectiveName in ipairs(strand.sequence) do
            if objectiveName == completedObjective.name then
                local nextIndex = i+1
                if nextIndex <= #strand.sequence then
                    toStartName = strand.sequence[i+1]
                    break
                else
                    strandComplete = true
                    local anyObjectiveNotFinished = false
                    for _, objective in ipairs(MissionDb.objectives) do
                        if objective.state ~= "finished" then
                            anyObjectiveNotFinished = true
                            break
                        end
                    end

                    if not anyObjectiveNotFinished then
                        missionComplete = true
                    end
                end
            end
        end

        local casevacCount = spawnCasevacForCompletedObjective(completedObjective)

        showObjectiveCompletedUpdate(completedObjective, strandName, casevacCount)
    end

    if toStartName == nil then
        if missionComplete then
            -- Do end of mission stuff
            MESSAGE:New("MISSION COMPLETE -- NOBODY WINS!!!", 5):ToAll()
        elseif strandComplete then
            -- Do end of strand stuff
            MESSAGE:New(strandName .. " COMPLETE", 5):ToAll()
        end
    else
        for _, objective in ipairs(MissionDb.objectives) do
            if objective.name == toStartName then
                if completedObjective == nil then
                    startObjective(objective)
                else
                    local delay = 120
                    MESSAGE:New(string.format("STRAND UPDATE\n\n%s will be progressing to the next objective in %s seconds", strandName, delay), 30):ToAll()
                    SCHEDULER:New(nil, function()
                        startObjective(objective)
                    end, {}, delay)
                end
                break
            end
        end
    end
end

completeObjective = function(objective, killLinkedUnits)
    if #objective.nodes > 0 then
        UTILS.RemoveMark(objective.labelMarkId, 0)

        MissionDb.redchief.conflictZones:RemoveZonesByName(objective.name)
        MissionDb.bluechief.conflictZones:RemoveZonesByName(objective.name)
    end

    for _, node in ipairs(objective.nodes) do
        MissionDb.redchief.instance:RemoveStrategicZone(node.opsZone)
        MissionDb.bluechief.instance:RemoveStrategicZone(node.opsZone)
        node.opsZone:SetDrawZone(false)
        node.opsZone:GetZone():UndrawZone()
        node.opsZone:Stop()
        UTILS.RemoveMark(node.labelMarkId, 0)
        MissionDb.ctld.instance:DeactivateZone(node.name, CTLD.CargoZoneType.MOVE)
    end

    if killLinkedUnits then
        for _, category in ipairs({objective.vehicleGroups, objective.shipGroups}) do
            for _, group in ipairs(category) do
                local g = GROUP:FindByName(group.name)
                if g then
                    g:Destroy(true)
                end
            end
        end

        local objectiveZone = ZONE:FindByName(objective.name)
        local qrfsNamesToKill = objectiveZone:GetProperty("qrfKillOnComplete")
        if qrfsNamesToKill ~= "" then
            local qrfsToKill = UTILS.Split(qrfsNamesToKill, ",")
            for _, qrfName in ipairs(qrfsToKill) do
                for _, obj in ipairs(MissionDb.objectives) do
                    for _, qrf in ipairs(obj.qrfs) do
                        if qrfName == qrf.name then
                            qrf.state = "dead"
                            for _, category in ipairs({qrf.vehicleGroups, qrf.shipGroups}) do
                                for _, group in ipairs(category) do
                                    local g = GROUP:FindByName(group.name)
                                    if g then
                                        g:Destroy(true)
                                    end
                                end
                            end

                            for _, group in ipairs(qrf.staticGroups) do
                                local g = STATIC:FindByName(group.name, false)
                                if g then
                                    g:Destroy(true)
                                end
                            end

                            if qrf.labelMarkId then
                                UTILS.RemoveMark(qrf.labelMarkId, 0)
                            end
                            if qrf.circleMarkId then
                                UTILS.RemoveMark(qrf.circleMarkId, 0)
                            end
                        end
                    end
                end
            end
        end
    end

    for _, task in ipairs(objective.tasks) do
        task.state = "finished"
        if task.instance then
            task.instance:__Success(-1)
            if killLinkedUnits then
                for _, category in ipairs({task.vehicleGroups, task.shipGroups}) do
                    for _, group in ipairs(category) do
                        local group = GROUP:FindByName(group.name)
                        group:Destroy(true)
                    end
                end
            end
        end
    end

    objective.state = "finished"

    saveState()

    if(objective.completeSound ~= "") then
        SCHEDULER:New(nil, function()
            local playItAgainSam = USERSOUND:New(objective.completeSound)
            playItAgainSam:ToAll()
        end, {}, 5)
    end

    progressToNextObjectiveFrom(objective, objective.strand)
end

local function lockAllFarpSlots()
    for _, objective in ipairs(MissionDb.objectives) do
        for _, farp in ipairs(objective.farps) do
            for _, client in ipairs(farp.clients) do
                local farpSlot = USERFLAG:New(client)
                farpSlot:Set(100)
            end
        end
    end
end

local function lockAllRoadbaseSlots()
    for _, objective in ipairs(MissionDb.objectives) do
        for _, roadbase in ipairs(objective.roadbases) do
            for _, client in ipairs(roadbase.clients) do
                local roadbaseSlot = USERFLAG:New(client)
                roadbaseSlot:Set(100)
            end
        end
    end
end

local function lockAllCarrierSlots()
    for _, objective in ipairs(MissionDb.objectives) do
        for _, carrier in ipairs(objective.carriers) do
            for _, client in ipairs(carrier.clients) do
                local carrierSlot = USERFLAG:New(client)
                carrierSlot:Set(100)
            end
        end
    end
end

local function lockAllAirbaseSlots()
    for _, objective in ipairs(MissionDb.objectives) do
        for _, airbase in ipairs(objective.airbases) do
            for _, client in ipairs(airbase.clients) do
                local airbaseSlot = USERFLAG:New(client)
                airbaseSlot:Set(100)
            end
        end
    end
end

local function initializeRedChief()
    local redAgents = SET_GROUP:New():FilterCoalitions("red"):FilterStart()
    MissionDb.redchief.instance = CHIEF:New(coalition.side.RED, redAgents, "Red Chief")
    MissionDb.redchief.instance:SetTacticalOverviewOn()
    MissionDb.redchief.instance:SetStrategy(CHIEF.Strategy.AGGRESSIVE)
    MissionDb.redchief.conflictZones = SET_ZONE:New()
    MissionDb.redchief.borderZones = SET_ZONE:New()
    MissionDb.redchief.awacsZones = SET_ZONE:New()
    MissionDb.redchief.instance:SetConflictZones(MissionDb.redchief.conflictZones)

    if MissionDb.redchief.strategicZoneResources.defaultEmptyFunc then
        MissionDb.redchief.strategicZoneResources.defaultEmpty = MissionDb.redchief.strategicZoneResources.defaultEmptyFunc(MissionDb.redchief.instance)
    end

    if MissionDb.redchief.strategicZoneResources.defaultOccupiedFunc then
        MissionDb.redchief.strategicZoneResources.defaultOccupied = MissionDb.redchief.strategicZoneResources.defaultOccupiedFunc(MissionDb.redchief.instance)
    end
end

local function initializeBlueChief()
    local blueAgents = SET_GROUP:New():FilterCoalitions("blue"):FilterStart()
    MissionDb.bluechief.instance = CHIEF:New(coalition.side.BLUE, blueAgents, "Blue Chief")
    --MissionDb.bluechief.instance:SetTacticalOverviewOn()
    MissionDb.bluechief.instance:SetStrategy(CHIEF.Strategy.DEFENSIVE)
    MissionDb.bluechief.conflictZones = SET_ZONE:New()
    MissionDb.bluechief.awacsZones = SET_ZONE:New()
    MissionDb.bluechief.instance:SetConflictZones(MissionDb.bluechief.conflictZones)

    if MissionDb.bluechief.strategicZoneResources.defaultEmptyFunc then
        MissionDb.bluechief.strategicZoneResources.defaultEmpty = MissionDb.bluechief.strategicZoneResources.defaultEmptyFunc(MissionDb.bluechief.instance)
    end

    if MissionDb.bluechief.strategicZoneResources.defaultOccupiedFunc then
        MissionDb.bluechief.strategicZoneResources.defaultOccupied = MissionDb.bluechief.strategicZoneResources.defaultOccupiedFunc(MissionDb.bluechief.instance)
    end
end

local function initializeObjectives()
    loadState()
    saveState()

    lockAllFarpSlots()
    lockAllRoadbaseSlots()
    lockAllCarrierSlots()
    lockAllAirbaseSlots()
    initializeRedChief()
    initializeBlueChief()

    local strandInProgressCount = {}

    for _, strand in ipairs(MissionDb.strands) do
        strandInProgressCount[strand.name] = 0
    end

    local finishedCount = 0

    for _, objective in ipairs(MissionDb.objectives) do
        if objective.state == "active" then
            startObjective(objective)
            strandInProgressCount[objective.strand] = strandInProgressCount[objective.strand] + 1
        elseif objective.state == "finished" then
            finishedCount = finishedCount + 1
            unlockFarpsForObjective(objective)
            unlockRoadbasesForObjective(objective)
            unlockCarriersForObjective(objective)
            unlockAirbasesForObjective(objective)
            unlockReinforcementsForObjective(objective)
            unlockQrfsForObjective(objective)
        end
    end

    SCHEDULER:New(nil, function()
        activateAirwings(MissionDb.bluechief, coalition.side.BLUE)
        activateAirwings(MissionDb.redchief, coalition.side.RED)
        activateBrigades(MissionDb.bluechief, coalition.side.BLUE)
        activateBrigades(MissionDb.redchief, coalition.side.RED)
        saveState()
    end, {}, 15)

    MissionDb.bluechief.instance:__Start(75)
    MissionDb.redchief.instance:__Start(75)

    -- All finished so reset them so it can start over
    if(finishedCount == #MissionDb.objectives) then
        -- ALL DONE, go reset things...
    end

    for strandName, count in pairs(strandInProgressCount) do
        if count == 0 then
            progressToNextObjectiveFrom(nil, strandName)
        end
    end
end

local function debugCompleteObjective(menuArgs)
    for _, objective in ipairs(MissionDb.objectives) do
        if objective.state == "active" and objective.strand == menuArgs.strand then
            completeObjective(objective, menuArgs.killLinkedUnits)
            break
        end
    end
end

local function reportOverallMissionStatus()
    local strandObjectiveStateMap = buildStrandObjectiveStateMap()

    local r = {}
    table.insert(r, "MISSION STATUS")
    table.insert(r, "")
    for strandName, props in pairs(strandObjectiveStateMap) do
        table.insert(r,string.format("%s, %i/%i objectives complete", strandName, props.finished, props.total))
        if(props.active and props.finished ~= props.total) then
            table.insert(r,string.format("  %s", props.activeObjective.displayName))
            if props.activeObjective.totalNodes > 0 then
                table.insert(r,string.format("      %i/%i zones captured", props.activeObjective.capturedNodes, props.activeObjective.totalNodes))
                for _, node in ipairs(props.activeObjective.nodes) do
                    if node.captured then
                        table.insert(r,string.format("        - %s: captured", node.name))
                    else
                        table.insert(r,string.format("        - %s: %i enemy units", node.name, node.redUnitsCount))
                    end
                end
            end
            if props.activeObjective.totalTasks > 0 then
                table.insert(r,string.format("      %i/%i tasks completed", props.activeObjective.completedTasks, props.activeObjective.totalTasks))
                for _, task in ipairs(props.activeObjective.tasks) do
                    if task.complete then
                        table.insert(r,string.format("        - %s '%s': complete", task.auftrag, task.name))
                    else
                        table.insert(r,string.format("        - %s '%s': active", task.auftrag, task.name))
                    end
                end
            end
        end
        table.insert(r, "")
    end

    if(MissionDb.industry.enabled) then
        table.insert(r, string.format("Enemy industry is at %.f%% capacity, with %i active industry targets", MissionDb.industry.redPercentage, MissionDb.industry.redAlive))
        table.insert(r, "")
        table.insert(r, string.format("Friendly industry is at %.f%% capacity, with %i active industry structures", MissionDb.industry.bluePercentage, MissionDb.industry.blueAlive))
        table.insert(r, "")
    end

    table.insert(r, string.format("%i operation token(s) available", MissionDb.counters.opstokens))
    table.insert(r, string.format("  - %s", table.concat(MissionDb.markerops.hintOptions, ", ")))
    table.insert(r, "")

    local m = table.concat(r, "\n")
    MESSAGE:New(m, 30):ToAll()
end

local function debugResupplyAirwing(menuArgs)
    for _, airwing in ipairs(MissionDb.redchief.airwings) do
        if airwing.name == menuArgs.name and airwing.state == "active" then
            for _, squadron in ipairs(airwing.squadrons) do
                airwing.instance:AddAssetToSquadron(squadron.instance, 1)
            end
        end
    end
end

local function debugResupplyBrigade(menuArgs)
    if menuArgs.brigade.state == "active" then
        for _, platoon in ipairs(menuArgs.brigade.platoons) do
            menuArgs.brigade.instance:AddAssetToPlatoon(platoon.instance, 1)
        end
    end
end

local function randomChiefMissions()
    local bombingPotentials = {}
    local baiPotentials = {}

    for _, objective in ipairs(MissionDb.objectives) do
        if objective.state == "active" then
            for _, node in ipairs(objective.nodes) do
                if node.state ~= "unstarted" then
                    node.opsZone:EvaluateZone()
                    if node.opsZone:IsGuarded() and node.opsZone:IsBlue() then
                        table.insert(bombingPotentials, {coordinate = node.opsZone:GetCoordinate(), zone = node.opsZone:GetZone() })
                    end
                end
            end

            local objectiveZone = ZONE:FindByName(objective.name)
            local groupsInZone = SET_GROUP:New():FilterActive():FilterCoalitions("blue"):FilterZones({objectiveZone}):FilterOnce()
            groupsInZone:ForEachGroup(function(g)
                table.insert(baiPotentials, g)
            end)
        end
    end

    for _, objective in ipairs(MissionDb.objectives) do
        for _, reinforcement in ipairs(objective.reinforcements) do
            if reinforcement.state == "active" and #reinforcement.staticGroups > 0 then
                for _, static in ipairs(reinforcement.staticGroups) do
                    if string.find(static.name, "INDUSTRYTARGET") then
                        if static.state ~= "dead" then
                            table.insert(bombingPotentials, {coordinate = STATIC:FindByName(static.name):GetCoordinate()})
                        end
                    end
                end
            end
        end
    end
    
    if #bombingPotentials > 0 then
        local chosen = bombingPotentials[math.random(#bombingPotentials)]

        local bombingMission = AUFTRAG:NewBOMBCARPET(chosen.coordinate, 25000, 500)

        -- This is really WW2 specific, need to make it conditional.
        bombingMission:SetFormation(ENUMS.Formation.FixedWing.BomberElement.Close)
        bombingMission:SetMissionSpeed(225)

        MissionDb.redchief.instance:AddMission(bombingMission)
    end

    if #baiPotentials > 0 then
        local chosenGroundTargetGroup = baiPotentials[math.random(#baiPotentials)]
        local baiMission = AUFTRAG:NewBAI(chosenGroundTargetGroup)
        MissionDb.redchief.instance:AddMission(baiMission)
    end
end

local function requestReconFlight(menuArgs)
    for _, objective in ipairs(MissionDb.objectives) do
        if objective.state == "active" and objective.strand == menuArgs.strand then
            if #objective.nodes > 0 then
                local reconZones = SET_ZONE:New()
                for _, node in ipairs(objective.nodes) do
                    reconZones:AddZone(node.opsZone:GetZone())
                end
                local reconMission = AUFTRAG:NewRECON(reconZones, nil, 30000, true, true)
                MissionDb.bluechief.instance:AddMission(reconMission)

                local objectiveZone = ZONE:FindByName(objective.name)
                local objectiveLabelText = objectiveZone:GetProperty("label")
                local text=string.format("BLUE has requested a recon mission at %s. Units will be dispatched when available.", objectiveLabelText)
                MESSAGE:New(text, 15):ToAll()
            end
            break
        end
    end
end

local function requestCAP(menuArgs)
    for _, objective in ipairs(MissionDb.objectives) do
        if objective.state == "active" and objective.strand == menuArgs.strand then
            if #objective.nodes > 0 then
                local objectiveZone = ZONE:FindByName(objective.name)
                local capZone =  ZONE_RADIUS:New( string.format("BLUECAP-%d", math.random(1,100000)), objectiveZone:GetVec2(), objectiveZone:GetRadius())
                local capMission = AUFTRAG:NewCAP(capZone, 30000, 350)
                MissionDb.bluechief.instance:AddMission(capMission)

                local objectiveZone = ZONE:FindByName(objective.name)
                local objectiveLabelText = objectiveZone:GetProperty("label")
                local text=string.format("BLUE has requested a CAP mission at %s. Units will be dispatched when available.", objectiveLabelText)
                MESSAGE:New(text, 15):ToAll()
            end
            break
        end
    end
end

local function pruneCtldForInactiveObjectives()
    local finishedObjectiveZones = SET_ZONE:New()

    for _, objective in ipairs(MissionDb.objectives) do
        if objective.state == "finished" then
            finishedObjectiveZones:AddZone(ZONE:FindByName(objective.name))
        end
    end

    local ctldGroups = SET_GROUP:New():FilterCoalitions("blue"):FilterPrefixes("CTLD"):FilterActive():FilterZones(finishedObjectiveZones):FilterOnce()
    ctldGroups:ForEachGroup(function(g)
        -- MESSAGE:New(string.format("CTLD cleanup destroying %s.", g.GroupName), 5):ToAll()
        g:Destroy(false)
    end)
end

local function initializeStrandMenus()
    local menuMissionStatus = MENU_MISSION:New("Mission Status")
    MENU_MISSION_COMMAND:New("Overall Status", menuMissionStatus, reportOverallMissionStatus)

    if MissionDb.devmode then
        local menuDebug = MENU_MISSION:New("Debug", menuMissionStatus)
        local menuDebugStrands = MENU_MISSION:New("Strands", menuDebug)
        for _, strand in ipairs(MissionDb.strands) do
            local menuIndividualStrand = MENU_MISSION:New(strand.name, menuDebugStrands)
            MENU_MISSION_COMMAND:New("Complete (kill units)", menuIndividualStrand, debugCompleteObjective, {strand = strand.name, killLinkedUnits = true})
            MENU_MISSION_COMMAND:New("Complete (leave units)", menuIndividualStrand, debugCompleteObjective, {strand = strand.name, killLinkedUnits = false})
        end

        MENU_MISSION_COMMAND:New("Save", menuDebug, saveState)

        local menuSpawn = MENU_MISSION:New("Spawn", menuDebug)

        MENU_MISSION_COMMAND:New("Spawn QRF", menuSpawn, randomEnemyReinforcement)
        MENU_MISSION_COMMAND:New("Spawn Enemy Air Missions", menuSpawn, randomChiefMissions)
        MENU_MISSION_COMMAND:New("Spawn Friendly Reinforcement", menuSpawn, randomFriendlyReinforcement)

        local menuResupply = MENU_MISSION:New("Resupply", menuDebug)

        local menuDebugAirwingResupply = MENU_MISSION:New("Resupply Airwings", menuResupply)
        for _, airwing in ipairs(MissionDb.redchief.airwings) do
            MENU_MISSION_COMMAND:New(airwing.name, menuDebugAirwingResupply, debugResupplyAirwing, { name = airwing.name, state = airwing.state })
        end

        local menuDebugBrigadeResupply = MENU_MISSION:New("Resupply Brigades", menuResupply)
        local menuDebugBrigadeResupplyRed = MENU_MISSION:New("RED", menuDebugBrigadeResupply)
        for _, brigade in ipairs(MissionDb.redchief.brigades) do
            MENU_MISSION_COMMAND:New(brigade.name, menuDebugBrigadeResupplyRed, debugResupplyBrigade, { brigade = brigade })
        end
        local menuDebugBrigadeResupplyBlue = MENU_MISSION:New("BLUE", menuDebugBrigadeResupply)
        for _, brigade in ipairs(MissionDb.bluechief.brigades) do
            MENU_MISSION_COMMAND:New(brigade.name, menuDebugBrigadeResupplyBlue, debugResupplyBrigade, { brigade = brigade })
        end

        MENU_MISSION_COMMAND:New("CTLD Cleanup", menuDebug, pruneCtldForInactiveObjectives)
        MENU_MISSION_COMMAND:New("Add ops token", menuDebug, addOpsToken)
        MENU_MISSION_COMMAND:New("Sync Warehouse Storage", menuDebug, syncWarehouseStorage)
    end

    local menuRequest = MENU_MISSION:New("Request")
    for _, strand in ipairs(MissionDb.strands) do
        local menuIndividualStrand = MENU_MISSION:New(strand.name, menuRequest)
        MENU_MISSION_COMMAND:New("Request Recon Flight", menuIndividualStrand, requestReconFlight, {strand = strand.name})
        MENU_MISSION_COMMAND:New("Request CAP", menuIndividualStrand, requestCAP, {strand = strand.name})
    end
end

local function initializeCtld()
    MissionDb.ctld.instance = CTLD:New(coalition.side.BLUE, MissionDb.ctld.groups, "CTLD Rotary Gang")

    MissionDb.ctld.instance.dropcratesanywhere = true
    MissionDb.ctld.instance.forcehoverload = false
    MissionDb.ctld.instance.hoverautoloading = false
    MissionDb.ctld.instance.movetroopsdistance  = 1000
    MissionDb.ctld.instance.enableHercules = false
    MissionDb.ctld.instance.enableslingload = true
    MissionDb.ctld.instance.cratecountry = country.id.CJTF_BLUE
    MissionDb.ctld.instance.buildtime = 0
    MissionDb.ctld.instance.usesubcats = true
    MissionDb.ctld.instance.nobuildinloadzones = false
    MissionDb.ctld.instance.movecratesbeforebuild = false

    MissionDb.ctld.instance.enableLoadSave = true
    MissionDb.ctld.instance.saveinterval = 600
    MissionDb.ctld.instance.filename = "ctld.csv"
    MissionDb.ctld.instance.filepath = defaultDrive
    MissionDb.ctld.instance.eventoninject = true

    MissionDb.ctld.instance:SetUnitCapabilities("Ka-50", false, true, 0, 2, 15, 200)
    MissionDb.ctld.instance:SetUnitCapabilities("Ka-50_3", false, true, 0, 2, 15, 200)
    MissionDb.ctld.instance:SetUnitCapabilities("UH-1H", true, true, 1, 8, 15, 1350)
    MissionDb.ctld.instance:SetUnitCapabilities("UH-1H", true, true, 1, 8, 15, 1350)
    MissionDb.ctld.instance:SetUnitCapabilities("OH58D", false, true, 0, 2, 15, 200)

    MissionDb.ctld.instance:Start()
    MissionDb.ctld.instance:AddTroopsCargo("Infantry (8)", { "CTLD Inf M4 8" }, CTLD_CARGO.Enum.TROOPS, 8, 80)
    MissionDb.ctld.instance:AddTroopsCargo("Infantry - AA (6)", { "CTLD Infantry AA" }, CTLD_CARGO.Enum.TROOPS, 6, 80)
    MissionDb.ctld.instance:AddTroopsCargo("Infantry - AT (8)", { "CTLD Infantry AT" }, CTLD_CARGO.Enum.TROOPS, 8, 80)
    MissionDb.ctld.instance:AddTroopsCargo("JTAC (1)", { "CTLD BLUE RECCE JTAC" }, CTLD_CARGO.Enum.TROOPS, 1, 80)
    MissionDb.ctld.instance:AddTroopsCargo("MORTAR (5)", { "CTLD MORTAR" }, CTLD_CARGO.Enum.TROOPS, 5, 122)
    MissionDb.ctld.instance:AddTroopsCargo("SK Special - AT (2)", { "CTLD AT SK Special 2" }, CTLD_CARGO.Enum.TROOPS, 2, 80)
    MissionDb.ctld.instance:AddTroopsCargo("SK Special - AA (2)", { "CTLD AA SK Special 2" }, CTLD_CARGO.Enum.TROOPS, 2, 80)

    MissionDb.ctld.instance:AddCratesCargo("HMMWV - JTAC", { "CTLD BLUE RECCE JTAC HMMWV" }, CTLD_CARGO.Enum.VEHICLE, 1, 1350, nil, "Vehicles")
    MissionDb.ctld.instance:AddCratesCargo("HMMWV - MG", { "CTLD HMMWV MG" }, CTLD_CARGO.Enum.VEHICLE, 1, 1350, nil, "Vehicles")
    MissionDb.ctld.instance:AddCratesCargo("HMMWV - TOW", { "CTLD HMMWV TOW" }, CTLD_CARGO.Enum.VEHICLE, 1, 1350, nil, "Vehicles")
    MissionDb.ctld.instance:AddCratesCargo("AVENGER", { "CTLD AVENGER" }, CTLD_CARGO.Enum.VEHICLE, 1, 1350, nil, "Air Defense")
    MissionDb.ctld.instance:AddCratesCargo("M939 - AMMO", { "CTLD M818" }, CTLD_CARGO.Enum.VEHICLE, 1, 1350, nil, "Vehicles")
    MissionDb.ctld.instance:AddCratesCargo("M60A3", { "CTLD M60" }, CTLD_CARGO.Enum.VEHICLE, 2, 1350, nil, "Vehicles")
    MissionDb.ctld.instance:AddCratesCargo("STRYKER - MGS", { "CTLD STRYKER MGS" }, CTLD_CARGO.Enum.VEHICLE, 1, 1350, nil, "Vehicles")
    MissionDb.ctld.instance:AddCratesCargo("STRYKER - ICV", { "CTLD STRYKER ICV" }, CTLD_CARGO.Enum.VEHICLE, 1, 1350, nil, "Vehicles")
    MissionDb.ctld.instance:AddCratesCargo("MLRS", { "CTLD MLRS" }, CTLD_CARGO.Enum.VEHICLE, 1, 1350, nil, "Artillery")
    MissionDb.ctld.instance:AddCratesCargo("M-109", { "CTLD M-109" }, CTLD_CARGO.Enum.VEHICLE, 1, 1350, nil, "Artillery")
    MissionDb.ctld.instance:AddCratesCargo("HAWK", { "CTLD HAWK" }, CTLD_CARGO.Enum.VEHICLE, 3, 1350, nil, "Air Defense")
    MissionDb.ctld.instance:AddCratesCargo("NASAM", { "CTLD NASAM" }, CTLD_CARGO.Enum.VEHICLE, 2, 1350, nil, "Air Defense")

    CTLD_HERCULES:New(coalition.side.BLUE, "Jaelifter Fixed Wing", MissionDb.ctld.instance)

    function MissionDb.ctld.instance:OnAfterTroopsPickedUp(From, Event, To, Group, Unit, Cargo)
        MESSAGE:New(string.format("%s loaded '%s' into a %s.", Unit:GetPlayerName(), Cargo.Name, Unit:GetTypeName()), 5):ToAll()
    end

    function MissionDb.ctld.instance:OnAfterTroopsDeployed(From, Event, To, Group, Unit, Troops)
        if Unit then
            MESSAGE:New(string.format("%s deployed troops into the field from a %s.", Unit:GetPlayerName(), Unit:GetTypeName()), 5):ToAll()
        end

        local g = Troops
        g:HandleEvent( EVENTS.Dead )
        function g:OnEventDead( EventData )
            -- 100% of the time...
            if math.random(1, 100) <= MissionDb.settings.blueCasevacChance then
                local c = EventData.IniGroup:GetCoordinate()
                if c then
                    MissionDb.csar.instance:SpawnCASEVAC(c:Translate(math.random(1, 10), math.random(0, 359)), coalition.side.BLUE, "CASEVAC", false, "CASEVAC", "CASEVAC", true)
                end
            end
        end
    end

    function MissionDb.ctld.instance:OnAfterTroopsExtracted(From, Event, To, Group, Unit, Troops)
        MESSAGE:New(string.format("%s extracted troops from the field in a %s.", Unit:GetPlayerName(), Unit:GetTypeName()), 5):ToAll()
    end

    function MissionDb.ctld.instance:OnAfterCratesPickedUp(From, Event, To, Group, Unit, Cargo)
        MESSAGE:New(string.format("%s loaded a crate for '%s' into a %s.", Unit:GetPlayerName(), Cargo.Name, Unit:GetTypeName()), 5):ToAll()
    end

    function MissionDb.ctld.instance:OnAfterCratesDropped(From, Event, To, Group, Unit, Cargotable)
        MESSAGE:New(string.format("%s dropped crates into the field from a %s.", Unit:GetPlayerName(), Unit:GetTypeName()), 5):ToAll()
    end

    function MissionDb.ctld.instance:OnAfterCratesBuild(From, Event, To, Group, Unit, Vehicle)
        if Unit then
            MESSAGE:New(string.format("%s built crates into a %s.", Unit:GetPlayerName(), Vehicle:GetTypeName()), 5):ToAll()
        end

        local g = Vehicle
        g:HandleEvent( EVENTS.Dead )
        function g:OnEventDead( EventData )
            -- 100% of the time...
            if math.random(1, 100) <= MissionDb.settings.blueCasevacChance then
                local c = EventData.IniGroup:GetCoordinate()
                if c then
                    MissionDb.csar.instance:SpawnCASEVAC(c:Translate(math.random(1, 10), math.random(0, 359)), coalition.side.BLUE, "CASEVAC", false, "CASEVAC", "CASEVAC", true)
                end
            end
        end
    end

    MissionDb.ctld.instance:__Load(5)
end

local function initializeCsar()
    MissionDb.csar.instance = CSAR:New(coalition.side.BLUE, "Downed Pilot")

    MissionDb.csar.instance.csarPrefix = MissionDb.csar.groups
    MissionDb.csar.instance.allowDownedPilotCAcontrol  = true
    MissionDb.csar.instance.countryblue = country.id.UN_PEACEKEEPERS
    MissionDb.csar.instance.enableForAI = true
    MissionDb.csar.instance.csarUsePara = true
    MissionDb.csar.instance.allowbronco = true
    MissionDb.csar.instance.autosmoke = true
    MissionDb.csar.instance.immortalcrew = false
    MissionDb.csar.instance.rescuehoverheight  = 30
    MissionDb.csar.instance.rescuehoverdistance  = 30
    MissionDb.csar.instance.CreateRadioBeacons = false

    MissionDb.csar.instance.enableLoadSave = true
    MissionDb.csar.instance.saveinterval = 600
    MissionDb.csar.instance.filename = "csar.csv"
    MissionDb.csar.instance.filepath = defaultDrive

    function MissionDb.csar.instance:OnAfterRescued(from, event, to, heliunit, heliname, pilotssaved)
        local potentials = {}
        for _, objective in ipairs(MissionDb.objectives) do
            if objective.state == "active" then
                for _, group in ipairs(objective.vehicleGroups) do
                    if group.state == "active" then
                        table.insert(potentials, group.name)
                    end
                end
            end
        end

        MESSAGE:New(string.format("%i lives were saved! They'll be debriefed and any intel will be made available shortly.", pilotssaved), 5):ToAll()

        if #potentials > 0 then
            local count = math.random(1, pilotssaved)
            for i=1, count do
                local chosen = potentials[math.random(#potentials)]
                MissionDb.csar.taskControllerInstance:AddTarget(GROUP:FindByName(chosen):GetCoordinate())
            end

            randomFriendlyReinforcement()
        end

        MissionDb.counters.opstokens = MissionDb.counters.opstokens + pilotssaved
        MESSAGE:New(string.format("%i operation tokens available.", MissionDb.counters.opstokens), 5):ToAll()

    end

    MissionDb.csar.instance:Start()
    MissionDb.csar.instance:__Load(10)
end

local function initializeAutolase()
    SCHEDULER:New(nil, function()
        local players = SET_CLIENT:New():FilterCoalitions("blue"):FilterActive(true):FilterStart()
        local jtacs = SET_GROUP:New():FilterPrefixes("JTAC"):FilterCoalitions("blue"):FilterStart()
        MissionDb.autolase.instance = AUTOLASE:New(jtacs, coalition.side.BLUE, "AUTOLASE", players)
        MissionDb.autolase.instance:SetSmokeTargets(true, SMOKECOLOR.Orange)
        MissionDb.autolase.instance:SetMaxLasingTargets(1)
        MissionDb.autolase.instance:SetLasingParameters(10000, 14400)
        MissionDb.autolase.instance:SetLaserCodes({1688, 1113, 1511, 1522, 1533, 1611, 1622, 1633, 1711, 1722})
    end, {}, 60)
end

-- local function initializePlayerRecce()
--     local playerSet = SET_CLIENT:New():FilterCoalitions("blue"):FilterActive(true):FilterPrefixes({"SA342L", "SA342M", "Ka-50", "Bronco-OV-10A"}):FilterStart()
--     local attackers = SET_CLIENT:New():FilterCoalitions("blue"):FilterActive(true):FilterStart()
--     MissionDb.playerRecce.instance = PLAYERRECCE:New("PLAYER RECCE", coalition.side.BLUE, playerSet)
--     MissionDb.playerRecce.instance:SetAttackSet(attackers)
-- end

local function intializeStrandTaskController()
    MissionDb.strandtasks.instance = PLAYERTASKCONTROLLER:New("82nd Airborne", coalition.side.BLUE, PLAYERTASKCONTROLLER.Type.A2GS)
    MissionDb.strandtasks.instance:SetLocale("en")
    MissionDb.strandtasks.instance:SetMenuName("STRAND TASKS")
    MissionDb.strandtasks.instance:EnableTaskInfoMenu()
end

local function initializeCsarIntelTaskController()
    MissionDb.csar.taskControllerInstance = PLAYERTASKCONTROLLER:New("82nd Airborne", coalition.side.BLUE, PLAYERTASKCONTROLLER.Type.A2G)
    MissionDb.csar.taskControllerInstance:SetLocale("en")
    MissionDb.csar.taskControllerInstance:SetMenuName("CSAR INTEL TASKS")
    MissionDb.csar.taskControllerInstance:EnableTaskInfoMenu()
end

local function initializeMantis()
    MissionDb.samnetwork.instance = MANTIS:New("BlapBlap", "RED SAM", "RED EWR", nil, "red", true)
    --MissionDb.samnetwork.instance:Debug(true)
    MissionDb.samnetwork.instance:Start()
end

local function initializeMarkerOps()
    if MissionDb.markerops.enableBomb then
        table.insert(MissionDb.markerops.hintOptions, "GOON BOMB")
        MissionDb.markerops.bomb = MARKEROPS_BASE:New("GOON BOMB", {}, false)
        function MissionDb.markerops.bomb:OnAfterMarkChanged(From, Event, To, Text, Keywords, Coord, idx)
            if MissionDb.counters.opstokens > 0 then
                MissionDb.counters.opstokens = MissionDb.counters.opstokens - 1
                local mission = AUFTRAG:NewBOMBING(Coord)
                MissionDb.bluechief.instance:AddMission(mission)
                MESSAGE:New(string.format("GOON OPERATION: Bomb @ %s. %i tokens remaining.", Coord:ToStringMGRS(), MissionDb.counters.opstokens), 15):ToAll()
            else
                MESSAGE:New(string.format("GOON OPERATION: Aborted. No ops tokens available."), 15):ToAll()
            end
            UTILS.RemoveMark(idx, 0)
        end
    end

    if MissionDb.markerops.enableStrike then
        table.insert(MissionDb.markerops.hintOptions, "GOON STRIKE")
        MissionDb.markerops.strike = MARKEROPS_BASE:New("GOON STRIKE", {}, false)
        function MissionDb.markerops.strike:OnAfterMarkChanged(From, Event, To, Text, Keywords, Coord, idx)
            if MissionDb.counters.opstokens > 0 then
                MissionDb.counters.opstokens = MissionDb.counters.opstokens - 1
                local mission = AUFTRAG:NewSTRIKE(Coord)
                MissionDb.bluechief.instance:AddMission(mission)
                MESSAGE:New(string.format("GOON OPERATION: Strike @ %s. %i tokens remaining.", Coord:ToStringMGRS(), MissionDb.counters.opstokens), 15):ToAll()
            else
                MESSAGE:New(string.format("GOON OPERATION: Aborted. No ops tokens available."), 15):ToAll()
            end
            UTILS.RemoveMark(idx, 0)
        end
    end

    if MissionDb.markerops.enableSead then
        table.insert(MissionDb.markerops.hintOptions, "GOON SEAD")
        MissionDb.markerops.sead = MARKEROPS_BASE:New("GOON SEAD", {}, false)
        function MissionDb.markerops.sead:OnAfterMarkChanged(From, Event, To, Text, Keywords, Coord, idx)
            if MissionDb.counters.opstokens > 0 then
                MissionDb.counters.opstokens = MissionDb.counters.opstokens - 1
                local zone =  ZONE_RADIUS:New( string.format("BLUESEAD-%d", math.random(1,100000)), Coord:GetVec2(), 15000)
                local targSet = SET_GROUP:New():FilterCoalitions("red"):FilterPrefixes({"RED SAM", "RED EWR"}):FilterZones({zone}):FilterOnce()
                local target = TARGET:New(targSet)
                local mission = AUFTRAG:NewSEAD(target)
                MissionDb.bluechief.instance:AddMission(mission)
                MESSAGE:New(string.format("GOON OPERATION: SEAD @ %s. %i tokens remaining.", target:GetCoordinate():ToStringMGRS(), MissionDb.counters.opstokens), 15):ToAll()
            else
                MESSAGE:New(string.format("GOON OPERATION: Aborted. No ops tokens available."), 15):ToAll()
            end
            UTILS.RemoveMark(idx, 0)
        end
    end

    if MissionDb.markerops.enableCas then
        table.insert(MissionDb.markerops.hintOptions, "GOON CAS")
        MissionDb.markerops.cas = MARKEROPS_BASE:New("GOON CAS", {}, false)
        function MissionDb.markerops.cas:OnAfterMarkChanged(From, Event, To, Text, Keywords, Coord, idx)
            if MissionDb.counters.opstokens > 0 then
                MissionDb.counters.opstokens = MissionDb.counters.opstokens - 1
                local zone =  ZONE_RADIUS:New( string.format("BLUECAS-%d", math.random(1,100000)), Coord:GetVec2(), 15000)
                local mission = AUFTRAG:NewCAS(zone)
                MissionDb.bluechief.instance:AddMission(mission)
                MESSAGE:New(string.format("GOON OPERATION: CAS @ %s. %i tokens remaining.", Coord:ToStringMGRS(), MissionDb.counters.opstokens), 15):ToAll()
            else
                MESSAGE:New(string.format("GOON OPERATION: Aborted. No ops tokens available."), 15):ToAll()
            end
            UTILS.RemoveMark(idx, 0)
        end
    end

    if MissionDb.markerops.enableCarpetbomb then
        table.insert(MissionDb.markerops.hintOptions, "GOON CARPETBOMB")
        MissionDb.markerops.carpetbomb = MARKEROPS_BASE:New("GOON CARPETBOMB", {}, false)
        function MissionDb.markerops.carpetbomb:OnAfterMarkChanged(From, Event, To, Text, Keywords, Coord, idx)
            if MissionDb.counters.opstokens > 0 then
                MissionDb.counters.opstokens = MissionDb.counters.opstokens - 1
                local mission = AUFTRAG:NewBOMBCARPET(Coord, 25000, 500)
                -- This is really WW2 specific, need to make it conditional.
                mission:SetFormation(ENUMS.Formation.FixedWing.BomberElement.Close)
                mission:SetMissionSpeed(225)
                MissionDb.bluechief.instance:AddMission(mission)
                MESSAGE:New(string.format("GOON OPERATION: CARPETBOMB @ %s. %i tokens remaining.", Coord:ToStringMGRS(), MissionDb.counters.opstokens), 15):ToAll()
            else
                MESSAGE:New(string.format("GOON OPERATION: Aborted. No ops tokens available."), 15):ToAll()
            end
            UTILS.RemoveMark(idx, 0)
        end
    end
end

local function initializeSlotBlocker()
    local blocker = NET:New()
    function blocker:OnAfterPlayerJoined(From,Event,To,Client,Name)
        local client = CLIENT:FindByPlayerName(Name)
        if client then
            local group = Client:GetGroup()
            local flag = USERFLAG:New(group.GroupName)
            if flag:Get() == 100 then
                MESSAGE:New("Slot is locked.", 15, "ALERT"):ToClient(client)
                blocker:BlockPlayer(client, Name, 60, "Slot is locked.")
                if not blocker:ForceSlot(client, 0) then 
                    if group and group:IsAlive() then group:Destroy() end
                end
            end
        end
    end
end

initializeCtld()

initializeCsar()

initializeStrandMenus()

intializeStrandTaskController()

initializeCsarIntelTaskController()

if MissionDb.enableAutolase then
    initializeAutolase()
end

initializeMantis()

initializeMarkerOps()

-- initializePlayerRecce()

initializeSlotBlocker()

SCHEDULER:New(nil, initializeObjectives, {}, 30)

MESSAGE:New("CALVINBALL END!", 5):ToAll()

SCHEDULER:New(nil, saveState, {}, 600, 600)

SCHEDULER:New(nil, industryAwareRandomEnemyReinforcement, {}, math.random(MissionDb.settings.redQrfMission.minStart, MissionDb.settings.redQrfMission.maxStart), MissionDb.settings.redQrfMission.repeatAfter)

SCHEDULER:New(nil, randomFriendlyReinforcement, {}, math.random(MissionDb.settings.blueConvoyMission.minStart, MissionDb.settings.blueConvoyMission.maxStart), MissionDb.settings.blueConvoyMission.repeatAfter)

SCHEDULER:New(nil, randomChiefMissions, {}, math.random(MissionDb.settings.redChiefAirMission.minStart, MissionDb.settings.redChiefAirMission.maxStart), MissionDb.settings.redChiefAirMission.repeatAfter)

SCHEDULER:New(nil, industryAwareStandardAirwingReinforcement, {}, math.random(MissionDb.settings.redAirwingReinforcement.minStart, MissionDb.settings.redAirwingReinforcement.maxStart), MissionDb.settings.redAirwingReinforcement.repeatAfter)

SCHEDULER:New(nil, industryAwareStandardBrigadeReinforcement, {}, math.random(MissionDb.settings.redBrigadeReinforcement.minStart, MissionDb.settings.redBrigadeReinforcement.maxStart), MissionDb.settings.redBrigadeReinforcement.repeatAfter)

SCHEDULER:New(nil, blueBrigadeReinforcement, {}, math.random(120, 120), 3600)

SCHEDULER:New(nil, industryAwareBlueTokenSupply, {}, math.random(MissionDb.settings.blueIndustryTokenSupply.minStart, MissionDb.settings.blueIndustryTokenSupply.maxStart), MissionDb.settings.blueIndustryTokenSupply.repeatAfter)

SCHEDULER:New(nil, calculateIndustryPercentage, {}, 60, 60)

SCHEDULER:New(nil, syncWarehouseStorage, {}, 60, 300)

-- Global wrappers for local functions, to be called from discord bot
function DebugRandomEnemyReinforcement()
    randomEnemyReinforcement()
end


-- SCHEDULER:New(nil, function()
--     local c = STATIC:FindByName("Stoney Cross Airwing Warehouse#00001"):GetCoordinate()
--     c:Explosion(99999)
--     c:Explosion(99999)
--     c:Explosion(99999)
--     c:Explosion(99999)
-- end, {}, 500)