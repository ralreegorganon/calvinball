MissionDb = {
	objectives = {
		{
			name = "OBJ-1",
			strand = "STRAND-1",
			completeSound = "",
			nodes = {
				{ name = "NODE-1" },
				{ name = "NODE-2" },
				{ name = "NODE-3" },
			},
			tasks = {
			},
			farps = {
			},
			airbases = {
				{
					name = "AIRBASE-1",
					vehicleGroups = {
						{ name = "AIRBASE Support 1-1" },
						{ name = "MASH 1-1" },
						{ name = "MASH 1-2" },
						{ name = "MASH 1-3" },
					},
					shipGroups = {
					},
					staticGroups = {
						{
							name = "Batumi Airwing Warehouse#00001",
							template = {
								name = "Batumi Airwing Warehouse",
								type = "Warehouse",
								x = -355750.38193427,
								y = 617734.21158543,
								heading = 3.7873644768277,
								category = "Warehouses",
								canCargo = false,
								shape_name = "sklad",
								rate = 100,
								dead = false
							}
						},
					},
					clients = {
							"Batumi F-16C_50 1",
							"Batumi F-16C_50 2",
							"Batumi F-16C_50 3",
							"Batumi F-16C_50 4",
					}
				},
			},
			qrfs = {
				{
					name = "QRF-1",
					spawnGroups = {
					},
					vehicleGroups = {
					},
					shipGroups = {
					},
					staticGroups = {
						{
							name = "Kobuleti Airwing Warehouse#00001",
							template = {
								name = "Kobuleti Airwing Warehouse",
								type = "Warehouse",
								x = -317385.25525859,
								y = 636739.83277947,
								heading = 5.9341194567807,
								category = "Warehouses",
								canCargo = false,
								shape_name = "sklad",
								rate = 100,
								dead = false
							}
						},
					},
				},
			},
			reinforcements = {
			},
			vehicleGroups = {
			},
			shipGroups = {
			},
			staticGroups = {
				{
					name = "Kobuleti Airwing Warehouse#00001",
					template = {
						name = "Kobuleti Airwing Warehouse",
						type = "Warehouse",
						x = -317385.25525859,
						y = 636739.83277947,
						heading = 5.9341194567807,
						category = "Warehouses",
						canCargo = false,
						shape_name = "sklad",
						rate = 100,
						dead = false
					}
				},
			}
		},
	},
	strands = {
		{
			name = "STRAND-1",
			sequence = {
				"OBJ-1",
				},
			},
	},
	ctld = {
		groups = {
		}
	},
	csar = {
		groups = {
		}
	},
	autolase = {},
	playerRecce = {},
	strandtasks = {},
	samnetwork = {},
	redchief = {
	    airwings = {
			{
				name = "1st Goon Wing - Kobuleti",
				warehouse = "Kobuleti Airwing Warehouse#00001",
				airbase = "Kobuleti",
				squadrons = {
					{
						name = "1GW-Kobuleti-1",
						templateGroupName = "RED 1st Goon Wing - Kobuleti 1GW-Kobuleti-1 A-50",
						initialInventory = 1,
						capabilities = {
							{ mission = AUFTRAG.Type.AWACS, performance = 50 },
						},
						livery = "RF Air Force new",
						payloads = {
							{
								templateGroupName = "RED 1st Goon Wing - Kobuleti 1GW-Kobuleti-1 A-50 LOADOUT 0",
								missionTypes = { AUFTRAG.Type.AWACS }
							},
						}
					},
				}
			},
		}
	},
	bluechief = {
	    airwings = {
			{
				name = "1st - Batumi",
				warehouse = "Batumi Airwing Warehouse#00001",
				airbase = "Batumi",
				squadrons = {
					{
						name = "GGD-01",
						templateGroupName = "BLUE 1st - Batumi GGD-01 E-2C",
						initialInventory = 1,
						capabilities = {
							{ mission = AUFTRAG.Type.AWACS, performance = 50 },
						},
						livery = "VAW-125 Tigertails",
						payloads = {
							{
								templateGroupName = "BLUE 1st - Batumi GGD-01 E-2C LOADOUT 0",
								missionTypes = { AUFTRAG.Type.AWACS }
							},
						}
					},
				}
			},
		}
	},
	units = {},
	devmode = true,
	lateActivateStatics = false,
	missionName = "NotTheFrat",
	settings = {
		blueCasevacChance = 10
	}
}