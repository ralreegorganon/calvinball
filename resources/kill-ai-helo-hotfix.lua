local eventhit = {}
function eventhit:onEvent(event)
    if event.id ~= 2 then return false end -- exit on other event than "hit"
    if not event.weapon then return false end --exit if no weapon info (ex:collision)
    if not event.weapon:getDesc()["missileCategory"] then return false end -- exit if weapon is not a missile
    if not event.target:hasAttribute("Helicopters") then return false end --exit if target is not an helicopter
    event.target = Unit.getByName(event.target:getName())    --Transform Object class to Unit class
    if event.target == nil then return false end -- If target is destroy before get the unit class, return false
    if event.target:getPlayerName() ~= nil then return false end --exit if target is a player (no issue with the damage model for the players)
    trigger.action.explosion(event.target:getPoint(), 3) -- Explode volume 3 on the center of the helicopter, which destroy his engine.
end
world.addEventHandler(eventhit)