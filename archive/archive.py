## BLUE
m.triggers.add_triggerzone(dcs.mapping.Point(22143, -73423, m.terrain), 67056, name="Zone Alpha")
m.terrain.airports["Larnaca"].set_blue()
m.static_group(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "Larnaca Warehouse", dcs.statics.Warehouse.Warehouse,  dcs.mapping.Point(-7746,-209595, m.terrain))
fg = m.flight_group_inflight(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "BLUE F-16 Group", dcs.planes.F_16C_50, m.terrain.airports["Larnaca"].position, 42000, group_size=4)
fg.late_activation = True
fg = m.flight_group_inflight(m.country(dcs.countries.CombinedJointTaskForcesBlue.name), "BLUE F-16 Payload", dcs.planes.F_16C_50, m.terrain.airports["Larnaca"].position, 42000)
fg.late_activation = True


## RED
m.terrain.airports["Bassel Al-Assad"].set_red()
m.static_group(m.country(dcs.countries.CombinedJointTaskForcesRed.name), "Bassel Al-Assad Warehouse", dcs.statics.Warehouse.Warehouse,  dcs.mapping.Point(42585, 6308, m.terrain))
fg = m.flight_group_inflight(m.country(dcs.countries.CombinedJointTaskForcesRed.name), "RED F-16 Group", dcs.planes.F_16C_50, m.terrain.airports["Bassel Al-Assad"].position, 42000, group_size=4)
fg.late_activation = True
fg = m.flight_group_inflight(m.country(dcs.countries.CombinedJointTaskForcesRed.name), "RED F-16 Payload", dcs.planes.F_16C_50, m.terrain.airports["Bassel Al-Assad"].position, 42000)
fg.late_activation = True