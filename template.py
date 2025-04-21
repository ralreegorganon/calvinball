from missions.CyprusInvasion.mission import CyprusInvasion
from missions.DangerZone.mission import DangerZone
from missions.RockTheCasbah.mission import RockTheCasbah
from missions.BalloonFight.mission import BalloonFight
from calvinball.utility import build_sam_templates, build_copypasta_templates
import dcs

c = BalloonFight()
c.build(True, False, True, None)

m = dcs.mission.Mission()
m.load_file(c.miz_export_path)
build_sam_templates(m)
build_copypasta_templates(m)
m.save()