from missions.CyprusInvasion.mission import CyprusInvasion
from missions.DangerZone.mission import DangerZone
from missions.GeorgianOffensive.mission import GeorgianOffensive

missions = [CyprusInvasion(), DangerZone(), GeorgianOffensive()]
for m in missions:
    m.build(True, False, True)
