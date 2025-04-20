MissionDb = {
	objectives = {
		{
			name = "OBJ-1",
			strand = "STRAND-1",
			completeSound = "",
			borderZones = {
			},
			capZones = {
			},
			redAwacsZones = {
			},
			blueAwacsZones = {
				"BLUE-AWACS-1",
			},
			nodes = {
				{ name = "NODE-4", redSurrenderThreshold = 1, blueCaptureThreshold = 0 },
				{ name = "NODE-5", redSurrenderThreshold = 1, blueCaptureThreshold = 0 },
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
		{
			name = "OBJ-2",
			strand = "STRAND-2",
			completeSound = "",
			borderZones = {
			},
			capZones = {
			},
			redAwacsZones = {
			},
			blueAwacsZones = {
				"BLUE-AWACS-1",
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
		{
			name = "OBJ-3",
			strand = "STRAND-2",
			completeSound = "",
			borderZones = {
			},
			capZones = {
			},
			redAwacsZones = {
			},
			blueAwacsZones = {
				"BLUE-AWACS-1",
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
				{
					name = "QRF-2",
					spawnGroups = {
					},
					vehicleGroups = {
					},
					shipGroups = {
					},
					staticGroups = {
					},
				},
				{
					name = "QRF-4",
					spawnGroups = {
					},
					vehicleGroups = {
					},
					shipGroups = {
					},
					staticGroups = {
					},
				},
				{
					name = "QRF-5",
					spawnGroups = {
					},
					vehicleGroups = {
					},
					shipGroups = {
					},
					staticGroups = {
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
			}
		},
		{
			name = "OBJ-4",
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
			},
			carriers = {
			},
			qrfs = {
				{
					name = "QRF-3",
					spawnGroups = {
					},
					vehicleGroups = {
					},
					shipGroups = {
					},
					staticGroups = {
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
			}
		},
	},
	strands = {
		{
			name = "STRAND-1",
			sequence = {
				"OBJ-4",
				"OBJ-1",
				},
			},
		{
			name = "STRAND-2",
			sequence = {
				"OBJ-3",
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
	markerops = {
		hintOptions = {},
		enableBomb = true,
		enableStrike = true,
		enableSead = true,
		enableCas = true,
		enableCarpetbomb = true
	},
	redchief = {
	    airwings = {
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
		redPercentage = 100,
		redAlive = 0,
		bluePercentage = 100,
		blueAlive = 0
	},
	devmode = true,
	lateActivateStatics = false,
	enableConvoys = true,
	enableAutolase = true,
	missionName = "BalloonFight",
	settings = {
		blueCasevacChance = 10,
		nodeCaptureBlueCasevacChance = 50,
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
		airBombingEscortChance = 25,
		blueIndustryTokenSupply = {
			minStart = 1800,
			maxStart = 1800,
			repeatAfter = 3600,
			industryDelay = 3600
		},
	},
	invokeOnActivate = {},
	counters = {}
}