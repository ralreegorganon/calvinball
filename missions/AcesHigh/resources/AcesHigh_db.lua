MissionDb = {
	objectives = {
		{
			name = "OBJ-1",
			strand = "STRAND-1",
			completeSound = "",
			borderZones = {
			},
			capZones = {
				"CAP-1",
			},
			redAwacsZones = {
			},
			blueAwacsZones = {
			},
			nodes = {
				{ name = "NODE-1", redSurrenderThreshold = 1, blueCaptureThreshold = 0 },
				{ name = "NODE-2", redSurrenderThreshold = 1, blueCaptureThreshold = 0 },
				{ name = "NODE-3", redSurrenderThreshold = 1, blueCaptureThreshold = 0 },
			},
			tasks = {
			},
			farps = {
			},
			roadbases = {
			},
			airbases = {
				{
					name = "AIRBASE-1",
					vehicleGroups = {
					},
					shipGroups = {
					},
					staticGroups = {
						{
							name = "Lymington Airwing Warehouse#00001",
							template = {
								name = "Lymington Airwing Warehouse",
								type = "Warehouse",
								x = 139783.14802252,
								y = -90321.914661723,
								heading = 5.6897733615015,
								category = "Warehouses",
								canCargo = false,
								shape_name = "sklad",
								rate = 100,
								dead = false
							}
						},
					},
					clients = {
							"Lymington P-51D-30-NA Warm 1",
							"Lymington P-51D-30-NA Warm 2",
							"Lymington P-51D-30-NA Warm 3",
							"Lymington P-51D-30-NA Warm 4",
							"Lymington P-47D-30 Warm 1",
							"Lymington P-47D-30 Warm 2",
							"Lymington P-47D-30 Warm 3",
							"Lymington P-47D-30 Warm 4",
							"Lymington FW-190D9 Warm 1",
							"Lymington FW-190D9 Warm 2",
							"Lymington FW-190D9 Warm 3",
							"Lymington FW-190D9 Warm 4",
							"Lymington FW-190A8 Warm 1",
							"Lymington FW-190A8 Warm 2",
							"Lymington FW-190A8 Warm 3",
							"Lymington FW-190A8 Warm 4",
							"Lymington Bf-109K-4 Warm 1",
							"Lymington Bf-109K-4 Warm 2",
							"Lymington Bf-109K-4 Warm 3",
							"Lymington Bf-109K-4 Warm 4",
							"Lymington SpitfireLFMkIXCW Warm 1",
							"Lymington SpitfireLFMkIXCW Warm 2",
							"Lymington SpitfireLFMkIXCW Warm 3",
							"Lymington SpitfireLFMkIXCW Warm 4",
							"Lymington I-16 Warm 1",
							"Lymington I-16 Warm 2",
							"Lymington I-16 Warm 3",
							"Lymington I-16 Warm 4",
							"Lymington MosquitoFBMkVI Warm 1",
							"Lymington MosquitoFBMkVI Warm 2",
							"Lymington MosquitoFBMkVI Warm 3",
							"Lymington MosquitoFBMkVI Warm 4",
					}
				},
			},
			carriers = {
			},
			qrfs = {
				{
					name = "QRF-1",
					spawnGroups = {
						{ name = "RED QRF 1" },
						{ name = "RED QRF 2" },
					},
					vehicleGroups = {
					},
					shipGroups = {
					},
					staticGroups = {
					},
				},
				{
					name = "QRF-2",
					spawnGroups = {
					},
					vehicleGroups = {
						{ name = "RED RG Gound 1" },
					},
					shipGroups = {
					},
					staticGroups = {
						{
							name = "Funtington Airwing Warehouse#00001",
							template = {
								name = "Funtington Airwing Warehouse",
								type = "Warehouse",
								x = 152946.39092364,
								y = -46156.327299636,
								heading = 5.8119464091411,
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
				{
					name = "REINFORCEMENT-1",
					spawnGroups = {
						{ name = "BLUE REINFORCEMENT 1" },
					},
					vehicleGroups = {
					},
					shipGroups = {
					},
					staticGroups = {
					},
				},
			},
			vehicleGroups = {
				{ name = "RED RG Ground 1" },
				{ name = "RED RG Ground 2" },
				{ name = "RED RG Ground 4" },
				{ name = "RED RG Ground 5" },
				{ name = "RED RG Ground 6" },
				{ name = "RED RG Ground 3" },
			},
			shipGroups = {
			},
			staticGroups = {
			}
		},
		{
			name = "OBJ-2",
			strand = "STRAND-1",
			completeSound = "",
			borderZones = {
			},
			capZones = {
			},
			redAwacsZones = {
			},
			blueAwacsZones = {
			},
			nodes = {
			},
			tasks = {
			},
			farps = {
			},
			roadbases = {
			},
			airbases = {
			},
			carriers = {
			},
			qrfs = {
			},
			reinforcements = {
			},
			vehicleGroups = {
			},
			shipGroups = {
			},
			staticGroups = {
			}
		},
	},
	strands = {
		{
			name = "STRAND-1",
			sequence = {
				"OBJ-1",
				"OBJ-2",
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
	markerops = {},
	redchief = {
	    airwings = {
			{
				name = "Funtington",
				warehouse = "Funtington Airwing Warehouse#00001",
				airbase = "Funtington",
				squadrons = {
					{
						name = "Funtington 1",
						templateGroupName = "RED Funtington Funtington 1 Bf-109K-4",
						initialInventory = 1,
						takeoffCold = false,
						parking = nil,
						capabilities = {
							{ mission = AUFTRAG.Type.CAP, performance = 50 },
							{ mission = AUFTRAG.Type.INTERCEPT, performance = 50 },
							{ mission = AUFTRAG.Type.ESCORT, performance = 50 },
						},
						livery = "Bf-109 K4 Jagdgeschwader 53",
						payloads = {
							{
								templateGroupName = "RED Funtington Funtington 1 Bf-109K-4 LOADOUT 0",
								missionTypes = { AUFTRAG.Type.CAP, AUFTRAG.Type.INTERCEPT, AUFTRAG.Type.ESCORT }
							},
						}
					},
				}
			},
		},
		brigades = {
		},
		strategicZoneResources = {
			defaultOccupied = nil,
			defaultEmpty = nil,
			nodeOccupied = {},
			nodeEmpty = {},
		},
	},
	bluechief = {
	    airwings = {
			{
				name = "Lymington",
				warehouse = "Lymington Airwing Warehouse#00001",
				airbase = "Lymington",
				squadrons = {
					{
						name = "G-01",
						templateGroupName = "BLUE Lymington G-01 SpitfireLFMkIXCW",
						initialInventory = 99,
						takeoffCold = false,
						parking = nil,
						capabilities = {
							{ mission = AUFTRAG.Type.CAP, performance = 50 },
						},
						livery = "RAF, No. 145 Squadron",
						payloads = {
							{
								templateGroupName = "BLUE Lymington G-01 SpitfireLFMkIXCW LOADOUT 0",
								missionTypes = { AUFTRAG.Type.CAP }
							},
						}
					},
				}
			},
		},
		brigades = {
		},
		strategicZoneResources = {
			defaultOccupied = nil,
			defaultEmpty = nil,
			nodeOccupied = {},
			nodeEmpty = {},
		},
	},
	units = {},
	industry = {
		percentage = 100,
		active = 0
	},
	devmode = true,
	lateActivateStatics = false,
	enableConvoys = true,
	missionName = "AcesHigh",
	settings = {
		blueCasevacChance = 10,
		blueConvoyMission = {
			minStart = 1800,
			maxStart = 3600,
			repeatAfter = 3600
		},
		redQrfMission = {
			minStart = 1800,
			maxStart = 3600,
			repeatAfter = 3600,
			industryDelay = 1800
		},
		redChiefAirMission = {
			minStart = 300,
			maxStart = 600,
			repeatAfter = 2700
		},
		redAirwingReinforcement = {
			minStart = 120,
			maxStart = 120,
			repeatAfter = 3600,
			industryDelay = 1800
		},
		redBrigadeReinforcement = {
			minStart = 120,
			maxStart = 120,
			repeatAfter = 3600,
			industryDelay = 1800
		},
	},
	invokeOnActivate = {},
	counters = {},
}