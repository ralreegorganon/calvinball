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
			},
			nodes = {
				{ name = "NODE-1", redSurrenderThreshold = 1, blueCaptureThreshold = 0 },
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
						{ name = "FARP MASH 1-1" },
						{ name = "FARP MASH 1-4" },
						{ name = "FARP MASH 1-2" },
						{ name = "FARP MASH 1-3" },
					},
					shipGroups = {
					},
					staticGroups = {
					},
					clients = {
							"Tbilisi-Lochini F-16C_50 Warm 1",
							"Tbilisi-Lochini F-16C_50 Warm 2",
							"Tbilisi-Lochini F-16C_50 Warm 3",
							"Tbilisi-Lochini F-16C_50 Warm 4",
					}
				},
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
	elint = {},
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
	enableElint = false,
	missionName = "GeorgianOffensive",
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