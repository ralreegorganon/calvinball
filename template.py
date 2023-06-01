from missions.CyprusInvasion.mission import CyprusInvasion
from missions.DangerZone.mission import DangerZone
from calvinball.utility import build_sam_templates, build_copypasta_templates
import dcs

c = DangerZone()

m = dcs.mission.Mission()
m.load_file(c.miz_export_path)
build_sam_templates(m)
#build_copypasta_templates(m)
m.save()