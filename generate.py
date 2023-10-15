from missions.CyprusInvasion.mission import CyprusInvasion
from missions.DangerZone.mission import DangerZone
from missions.GeorgianOffensive.mission import GeorgianOffensive
from missions.AndeanAbyss.mission import AndeanAbyss
from missions.RockTheCasbah.mission import RockTheCasbah

missions = [CyprusInvasion(), DangerZone(), GeorgianOffensive(), AndeanAbyss(), RockTheCasbah()]
for m in missions:
    m.build(True, False, True)
