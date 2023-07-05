MissionDb = {
	objectives = {
		{
			name = "OBJ-1",
			strand = "STRAND-3",
			completeSound = "",
			borderZones = {
				"BORDER-1",
				"BORDER-2",
				"BORDER-3",
				"BORDER-4",
			},
			capZones = {
				"CAP-3",
			},
			nodes = {
			},
			tasks = {
			},
			farps = {
			},
			airbases = {
			},
			carriers = {
				{
					name = "Teddy",
					clients = {
							"Teddy F-14B Warm 1",
							"Teddy F-14B Warm 2",
							"Teddy F-14B Warm 3",
							"Teddy F-14B Warm 4",
							"Teddy FA-18C_hornet Warm 1",
							"Teddy FA-18C_hornet Warm 2",
							"Teddy FA-18C_hornet Warm 3",
							"Teddy FA-18C_hornet Warm 4",
					},
					waypoints = {
						{ 
							x = 91500,
							y = -76000,
							speed = 25,
						},
						{ 
							x = 89000,
							y = -76000,
							speed = 25,
						},
						{ 
							x = 78000,
							y = -202400,
							speed = 25,
						},
					},
					tacan_channel = 51,
					radio = 301,
					link4 = 336,
					icls_channel = 1,
				},
				{
					name = "Forrestal",
					clients = {
							"Forrestal F-14B Warm 1",
							"Forrestal F-14B Warm 2",
							"Forrestal FA-18C_hornet Warm 1",
							"Forrestal FA-18C_hornet Warm 2",
					},
					waypoints = {
						{ 
							x = 99000,
							y = -68600,
							speed = 25,
						},
						{ 
							x = 96500,
							y = -68600,
							speed = 25,
						},
						{ 
							x = 85500,
							y = -195000,
							speed = 25,
						},
					},
					tacan_channel = 52,
					radio = 302,
					link4 = 337,
					icls_channel = 2,
				},
				{
					name = "Invincible",
					clients = {
							"Invincible AV8BNA Warm 1",
							"Invincible AV8BNA Warm 2",
							"Invincible AV8BNA Warm 3",
					},
					waypoints = {
						{ 
							x = 85000,
							y = -72600,
							speed = 25,
						},
						{ 
							x = 82500,
							y = -72600,
							speed = 25,
						},
						{ 
							x = 71500,
							y = -199000,
							speed = 25,
						},
					},
					tacan_channel = 53,
					radio = 303,
					link4 = nil,
					icls_channel = nil,
				},
				{
					name = "Tarawa",
					clients = {
							"Tarawa Mi-24P Warm 1",
							"Tarawa Mi-24P Warm 2",
							"Tarawa Mi-24P Warm 3",
							"Tarawa Mi-8MT Warm 1",
							"Tarawa Mi-8MT Warm 2",
							"Tarawa Mi-8MT Warm 3",
							"Tarawa SA342L Warm 1",
							"Tarawa SA342M Warm 1",
					},
					waypoints = {
						{ 
							x = 96700,
							y = -145500,
							speed = 25,
						},
						{ 
							x = 94200,
							y = -145500,
							speed = 25,
						},
						{ 
							x = 92500,
							y = -165000,
							speed = 25,
						},
					},
					tacan_channel = 54,
					radio = 304,
					link4 = nil,
					icls_channel = nil,
				},
				{
					name = "Peleliu",
					clients = {
							"Peleliu UH-1H Warm 1",
							"Peleliu UH-1H Warm 2",
							"Peleliu UH-1H Warm 3",
							"Peleliu AH-64D_BLK_II Warm 1",
							"Peleliu AH-64D_BLK_II Warm 2",
							"Peleliu AH-64D_BLK_II Warm 3",
							"Peleliu Ka-50_3 Warm 1",
							"Peleliu Ka-50_3 Warm 2",
					},
					waypoints = {
						{ 
							x = 101300,
							y = -145500,
							speed = 25,
						},
						{ 
							x = 98800,
							y = -145500,
							speed = 25,
						},
						{ 
							x = 97000,
							y = -165500,
							speed = 25,
						},
					},
					tacan_channel = 55,
					radio = 305,
					link4 = nil,
					icls_channel = nil,
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
							name = "Evreux Airwing Warehouse#00001",
							template = {
								name = "Evreux Airwing Warehouse",
								type = "Warehouse",
								x = -45937.516753441,
								y = 113150.41067526,
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
				{
					name = "QRF-2",
					spawnGroups = {
					},
					vehicleGroups = {
					},
					shipGroups = {
					},
					staticGroups = {
						{
							name = "Funtington Airwing Warehouse#00001",
							template = {
								name = "Funtington Airwing Warehouse",
								type = "Warehouse",
								x = -56913.781104768,
								y = 95359.246478193,
								heading = 6.2308254296198,
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
			}
		},
		{
			name = "OBJ-2",
			strand = "STRAND-1",
			completeSound = "",
			borderZones = {
			},
			capZones = {
				"CAP-4",
			},
			nodes = {
				{ name = "NODE-1" },
				{ name = "NODE-2" },
				{ name = "NODE-4" },
			},
			tasks = {
			},
			farps = {
			},
			airbases = {
			},
			carriers = {
			},
			qrfs = {
				{
					name = "QRF-3",
					spawnGroups = {
						{ name = "RED QRF 1" },
						{ name = "RED QRF 2" },
						{ name = "RED QRF 3" },
						{ name = "RED QRF 4" },
						{ name = "RED QRF 5" },
						{ name = "RED QRF 6" },
						{ name = "RED QRF 7" },
						{ name = "RED QRF 8" },
					},
					vehicleGroups = {
					},
					shipGroups = {
					},
					staticGroups = {
					},
				},
				{
					name = "QRF-7",
					spawnGroups = {
					},
					vehicleGroups = {
						{ name = "RED EWR 1" },
					},
					shipGroups = {
					},
					staticGroups = {
					},
				},
				{
					name = "QRF-10",
					spawnGroups = {
					},
					vehicleGroups = {
						{ name = "RED AIR DEFENSE BATTERY A 242-1" },
						{ name = "RED AIR DEFENSE BATTERY C RG 246-1" },
						{ name = "RED RG 152-1" },
						{ name = "RED RG 152-2" },
						{ name = "RED RG 152-3" },
						{ name = "RED RG 152-4" },
						{ name = "RED RG 152-5" },
						{ name = "RED RG 152-6" },
						{ name = "RED RG 152-7" },
						{ name = "RED SAM SA-2 RG 234-1" },
						{ name = "RED SAM SA-3 236-1" },
						{ name = "RED SAM SA-6 238-1" },
						{ name = "RED SAM SA-6 238-2" },
						{ name = "RED SAM SA-8 RG 240-1" },
						{ name = "RED SAM SA-8 RG 240-2" },
					},
					shipGroups = {
					},
					staticGroups = {
						{
							name = "Anglo Airwing Warehouse#00001",
							template = {
								name = "Anglo Airwing Warehouse",
								type = ".Ammunition depot",
								x = 136514.38099047,
								y = -172813.49896681,
								heading = 3.1415926535898,
								category = "Warehouses",
								canCargo = false,
								shape_name = "SkladC",
								rate = 100,
								dead = false
							}
						},
						{
							name = "Anglo Brigade Warehouse#00001",
							template = {
								name = "Anglo Brigade Warehouse",
								type = ".Ammunition depot",
								x = 136256.5321952,
								y = -173105.39931373,
								heading = 1.5707963267949,
								category = "Warehouses",
								canCargo = false,
								shape_name = "SkladC",
								rate = 100,
								dead = false
							}
						},
						{
							name = "Anglo Farp#00001",
							template = {
								name = "Anglo Farp",
								type = "FARP",
								x = 136246.57713557,
								y = -172820.38632655,
								heading = 2.2863813201126,
								category = "Heliports",
								canCargo = false,
								shape_name = "FARPS",
								rate = 50,
								dead = false
							}
						},
						{
							name = "Static Container 40ft-1#00001",
							template = {
								name = "Static Container 40ft-1",
								type = "container_40ft",
								x = 135932.2369729,
								y = -173001.67910306,
								heading = 1.2566370614359,
								category = "Fortifications",
								canCargo = false,
								shape_name = "container_40ft",
								rate = 1,
								dead = false
							}
						},
						{
							name = "Static Container 40ft-2#00001",
							template = {
								name = "Static Container 40ft-2",
								type = "container_40ft",
								x = 135934.28315346,
								y = -172993.72173424,
								heading = 1.2566370614359,
								category = "Fortifications",
								canCargo = false,
								shape_name = "container_40ft",
								rate = 1,
								dead = false
							}
						},
						{
							name = "Static Container 40ft-3#00001",
							template = {
								name = "Static Container 40ft-3",
								type = "container_40ft",
								x = 135937.69345438,
								y = -172984.40024505,
								heading = 1.2566370614359,
								category = "Fortifications",
								canCargo = false,
								shape_name = "container_40ft",
								rate = 1,
								dead = false
							}
						},
						{
							name = "Static Container 40ft-4#00001",
							template = {
								name = "Static Container 40ft-4",
								type = "container_40ft",
								x = 135939.96698833,
								y = -172975.07875586,
								heading = 1.2566370614359,
								category = "Fortifications",
								canCargo = false,
								shape_name = "container_40ft",
								rate = 1,
								dead = false
							}
						},
						{
							name = "Static Container 40ft-5#00001",
							template = {
								name = "Static Container 40ft-5",
								type = "container_40ft",
								x = 135942.92258246,
								y = -172964.3931463,
								heading = 1.2566370614359,
								category = "Fortifications",
								canCargo = false,
								shape_name = "container_40ft",
								rate = 1,
								dead = false
							}
						},
						{
							name = "Static Excavator-1#00001",
							template = {
								name = "Static Excavator-1",
								type = "345 Excavator",
								x = 136274.08264341,
								y = -172419.23747142,
								heading = 2.146754979953,
								category = "Fortifications",
								canCargo = false,
								shape_name = "cat_345l",
								rate = 3,
								dead = false
							}
						},
						{
							name = "Static Excavator-2#00001",
							template = {
								name = "Static Excavator-2",
								type = "345 Excavator",
								x = 136262.82653521,
								y = -172433.16452055,
								heading = 2.146754979953,
								category = "Fortifications",
								canCargo = false,
								shape_name = "cat_345l",
								rate = 3,
								dead = false
							}
						},
						{
							name = "Static Excavator-3#00001",
							template = {
								name = "Static Excavator-3",
								type = "345 Excavator",
								x = 136251.37964551,
								y = -172446.51922519,
								heading = 2.146754979953,
								category = "Fortifications",
								canCargo = false,
								shape_name = "cat_345l",
								rate = 3,
								dead = false
							}
						},
						{
							name = "Static FARP Tent-1#00001",
							template = {
								name = "Static FARP Tent-1",
								type = "FARP Tent",
								x = 136378.77530188,
								y = -173394.22567928,
								heading = 2.146754979953,
								category = "Fortifications",
								canCargo = false,
								shape_name = "PalatkaB",
								rate = 50,
								dead = false
							}
						},
						{
							name = "Static FARP Tent-10#00001",
							template = {
								name = "Static FARP Tent-10",
								type = "FARP Tent",
								x = 136377.36420432,
								y = -173431.40251587,
								heading = 2.146754979953,
								category = "Fortifications",
								canCargo = false,
								shape_name = "PalatkaB",
								rate = 50,
								dead = false
							}
						},
						{
							name = "Static FARP Tent-11#00001",
							template = {
								name = "Static FARP Tent-11",
								type = "FARP Tent",
								x = 136358.98540743,
								y = -173443.74256522,
								heading = 2.146754979953,
								category = "Fortifications",
								canCargo = false,
								shape_name = "PalatkaB",
								rate = 50,
								dead = false
							}
						},
						{
							name = "Static FARP Tent-12#00001",
							template = {
								name = "Static FARP Tent-12",
								type = "FARP Tent",
								x = 136339.29383933,
								y = -173456.60772304,
								heading = 2.146754979953,
								category = "Fortifications",
								canCargo = false,
								shape_name = "PalatkaB",
								rate = 50,
								dead = false
							}
						},
						{
							name = "Static FARP Tent-2#00001",
							template = {
								name = "Static FARP Tent-2",
								type = "FARP Tent",
								x = 136359.77307015,
								y = -173405.40964598,
								heading = 2.146754979953,
								category = "Fortifications",
								canCargo = false,
								shape_name = "PalatkaB",
								rate = 50,
								dead = false
							}
						},
						{
							name = "Static FARP Tent-3#00001",
							template = {
								name = "Static FARP Tent-3",
								type = "FARP Tent",
								x = 136344.01981567,
								y = -173419.32502077,
								heading = 2.146754979953,
								category = "Fortifications",
								canCargo = false,
								shape_name = "PalatkaB",
								rate = 50,
								dead = false
							}
						},
						{
							name = "Static FARP Tent-4#00001",
							template = {
								name = "Static FARP Tent-4",
								type = "FARP Tent",
								x = 136326.16612726,
								y = -173431.92762436,
								heading = 2.146754979953,
								category = "Fortifications",
								canCargo = false,
								shape_name = "PalatkaB",
								rate = 50,
								dead = false
							}
						},
						{
							name = "Static FARP Tent-9#00001",
							template = {
								name = "Static FARP Tent-9",
								type = "FARP Tent",
								x = 136396.53066394,
								y = -173423.26333439,
								heading = 2.146754979953,
								category = "Fortifications",
								canCargo = false,
								shape_name = "PalatkaB",
								rate = 50,
								dead = false
							}
						},
						{
							name = "Static Fuel tank-1#00001",
							template = {
								name = "Static Fuel tank-1",
								type = "Fuel tank",
								x = 136060.56853948,
								y = -173167.43080463,
								heading = 2.146754979953,
								category = "Fortifications",
								canCargo = false,
								shape_name = "toplivo-bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "Static Fuel tank-2#00001",
							template = {
								name = "Static Fuel tank-2",
								type = "Fuel tank",
								x = 136057.02370525,
								y = -173160.34113618,
								heading = 2.146754979953,
								category = "Fortifications",
								canCargo = false,
								shape_name = "toplivo-bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "Static Mi-24P-1#00001",
							template = {
								name = "Static Mi-24P-1",
								type = "Mi-24P",
								x = 136395.75812255,
								y = -173072.47809543,
								heading = 0.4363323129986,
								category = "Helicopters",
								canCargo = false,
								shape_name = "",
								rate = 20,
								dead = false
							}
						},
						{
							name = "Static Mi-24P-2#00001",
							template = {
								name = "Static Mi-24P-2",
								type = "Mi-24P",
								x = 136425.04175849,
								y = -173021.54852512,
								heading = 0.4363323129986,
								category = "Helicopters",
								canCargo = false,
								shape_name = "",
								rate = 20,
								dead = false
							}
						},
						{
							name = "Static Mi-26-1#00001",
							template = {
								name = "Static Mi-26-1",
								type = "Mi-26",
								x = 136553.63231979,
								y = -172904.83997071,
								heading = 6.0737457969403,
								category = "Helicopters",
								canCargo = false,
								shape_name = "",
								rate = 30,
								dead = false
							}
						},
						{
							name = "Static Mi-26-2#00001",
							template = {
								name = "Static Mi-26-2",
								type = "Mi-26",
								x = 136554.32827129,
								y = -172956.34038149,
								heading = 6.0737457969403,
								category = "Helicopters",
								canCargo = false,
								shape_name = "",
								rate = 30,
								dead = false
							}
						},
						{
							name = "Static Mi-26-3#00001",
							template = {
								name = "Static Mi-26-3",
								type = "Mi-26",
								x = 136552.9363683,
								y = -173008.18876801,
								heading = 6.0737457969403,
								category = "Helicopters",
								canCargo = false,
								shape_name = "",
								rate = 30,
								dead = false
							}
						},
						{
							name = "Static Military staff-1#00001",
							template = {
								name = "Static Military staff-1",
								type = "Military staff",
								x = 136518.9066223,
								y = -172618.37235653,
								heading = 2.146754979953,
								category = "Fortifications",
								canCargo = false,
								shape_name = "aviashtab",
								rate = 100,
								dead = false
							}
						},
						{
							name = "Static Military staff-2#00001",
							template = {
								name = "Static Military staff-2",
								type = "Military staff",
								x = 136504.81734576,
								y = -172598.32223223,
								heading = 2.146754979953,
								category = "Fortifications",
								canCargo = false,
								shape_name = "aviashtab",
								rate = 100,
								dead = false
							}
						},
						{
							name = "Static Military staff-3#00001",
							template = {
								name = "Static Military staff-3",
								type = "Military staff",
								x = 136491.26996448,
								y = -172580.98158419,
								heading = 2.146754979953,
								category = "Fortifications",
								canCargo = false,
								shape_name = "aviashtab",
								rate = 100,
								dead = false
							}
						},
						{
							name = "Static Small warehouse 3-1#00001",
							template = {
								name = "Static Small warehouse 3-1",
								type = "Small werehouse 3",
								x = 136106.85378166,
								y = -173041.19421853,
								heading = 3.1066860685499,
								category = "Fortifications",
								canCargo = false,
								shape_name = "s3",
								rate = 100,
								dead = false
							}
						},
						{
							name = "Static Small warehouse 3-2#00001",
							template = {
								name = "Static Small warehouse 3-2",
								type = "Small werehouse 3",
								x = 136129.50951197,
								y = -173047.26271771,
								heading = 3.1415926535898,
								category = "Fortifications",
								canCargo = false,
								shape_name = "s3",
								rate = 100,
								dead = false
							}
						},
						{
							name = "Static Tank 1-1#00001",
							template = {
								name = "Static Tank 1-1",
								type = "Tank",
								x = 136518.00255572,
								y = -173108.87028796,
								heading = 0.0645788929948,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "Static Tank 1-2#00001",
							template = {
								name = "Static Tank 1-2",
								type = "Tank",
								x = 136520.06938404,
								y = -173167.77489501,
								heading = 0.0645788929948,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "Static Tank 1-3#00001",
							template = {
								name = "Static Tank 1-3",
								type = "Tank",
								x = 136520.75832681,
								y = -173227.02397344,
								heading = 0.0645788929948,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
					},
				},
				{
					name = "QRF-8",
					spawnGroups = {
					},
					vehicleGroups = {
						{ name = "RED EWR 2" },
					},
					shipGroups = {
					},
					staticGroups = {
					},
				},
				{
					name = "QRF-11",
					spawnGroups = {
					},
					vehicleGroups = {
						{ name = "RED RG 1-1" },
						{ name = "RED RG 1-162" },
					},
					shipGroups = {
					},
					staticGroups = {
						{
							name = "INDUSTRYTARGET-1#00001",
							template = {
								name = "INDUSTRYTARGET-1",
								type = "Warehouse",
								x = 164605.4838359,
								y = -144273.32307957,
								heading = 3.1415926535898,
								category = "Warehouses",
								canCargo = false,
								shape_name = "sklad",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-11#00001",
							template = {
								name = "INDUSTRYTARGET-11",
								type = "Tank",
								x = 164504.91441029,
								y = -144249.53307059,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-12#00001",
							template = {
								name = "INDUSTRYTARGET-12",
								type = "Workshop A",
								x = 164508.98172624,
								y = -144137.29253737,
								heading = 1.5707963267949,
								category = "Fortifications",
								canCargo = false,
								shape_name = "tec_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-13#00001",
							template = {
								name = "INDUSTRYTARGET-13",
								type = "Tech hangar A",
								x = 164457.65757337,
								y = -144250.28352559,
								heading = 5.9341194567807,
								category = "Fortifications",
								canCargo = false,
								shape_name = "ceh_ang_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-14#00001",
							template = {
								name = "INDUSTRYTARGET-14",
								type = "Tech hangar A",
								x = 164398.48748824,
								y = -144242.58330904,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "ceh_ang_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-15#00001",
							template = {
								name = "INDUSTRYTARGET-15",
								type = "Repair workshop",
								x = 164343.63595538,
								y = -144256.06761686,
								heading = 1.535889741755,
								category = "Fortifications",
								canCargo = false,
								shape_name = "tech",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-16#00001",
							template = {
								name = "INDUSTRYTARGET-16",
								type = "Chemical tank A",
								x = 164378.74105165,
								y = -144183.59935028,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-17#00001",
							template = {
								name = "INDUSTRYTARGET-17",
								type = "Chemical tank A",
								x = 164342.13834426,
								y = -144172.84730498,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-18#00001",
							template = {
								name = "INDUSTRYTARGET-18",
								type = "Chemical tank A",
								x = 164374.39448015,
								y = -144142.65007139,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-19#00001",
							template = {
								name = "INDUSTRYTARGET-19",
								type = "Chemical tank A",
								x = 164335.73287047,
								y = -144129.15282304,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-2#00001",
							template = {
								name = "INDUSTRYTARGET-2",
								type = "Boiler-house A",
								x = 164587.77622174,
								y = -144182.42865565,
								heading = 1.5882496193148,
								category = "Fortifications",
								canCargo = false,
								shape_name = "kotelnaya_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-20#00001",
							template = {
								name = "INDUSTRYTARGET-20",
								type = "Chemical tank A",
								x = 164370.50544249,
								y = -144102.15832634,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-21#00001",
							template = {
								name = "INDUSTRYTARGET-21",
								type = "Chemical tank A",
								x = 164333.21643434,
								y = -144092.09258181,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-22#00001",
							template = {
								name = "INDUSTRYTARGET-22",
								type = "Tech combine",
								x = 164253.84871285,
								y = -144164.25490365,
								heading = 3.08923277603,
								category = "Fortifications",
								canCargo = false,
								shape_name = "kombinat",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-23#00001",
							template = {
								name = "INDUSTRYTARGET-23",
								type = "Comms tower M",
								x = 164499.9426178,
								y = -143978.68025377,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "tele_bash_m",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-3#00001",
							template = {
								name = "INDUSTRYTARGET-3",
								type = "Boiler-house A",
								x = 164587.77622174,
								y = -144128.67194259,
								heading = 1.5882496193148,
								category = "Fortifications",
								canCargo = false,
								shape_name = "kotelnaya_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-4#00001",
							template = {
								name = "INDUSTRYTARGET-4",
								type = "Boiler-house A",
								x = 164584.54179892,
								y = -144072.87786851,
								heading = 1.5882496193148,
								category = "Fortifications",
								canCargo = false,
								shape_name = "kotelnaya_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-5#00001",
							template = {
								name = "INDUSTRYTARGET-5",
								type = "Tank",
								x = 164546.15559893,
								y = -144348.39492705,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-6#00001",
							template = {
								name = "INDUSTRYTARGET-6",
								type = "Tank",
								x = 164545.86310823,
								y = -144305.10630351,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-7#00001",
							template = {
								name = "INDUSTRYTARGET-7",
								type = "Tank",
								x = 164543.81567333,
								y = -144259.18526368,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-8#00001",
							template = {
								name = "INDUSTRYTARGET-8",
								type = "Tank",
								x = 164507.83931729,
								y = -144341.08265956,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-9#00001",
							template = {
								name = "INDUSTRYTARGET-9",
								type = "Tank",
								x = 164506.37686379,
								y = -144292.52920343,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
					},
				},
				{
					name = "QRF-9",
					spawnGroups = {
					},
					vehicleGroups = {
						{ name = "RED EWR 3" },
					},
					shipGroups = {
					},
					staticGroups = {
					},
				},
				{
					name = "QRF-6",
					spawnGroups = {
					},
					vehicleGroups = {
						{ name = "RED AIR DEFENSE BATTERY A RG 690" },
						{ name = "RED AIR DEFENSE BATTERY A RG 690-1" },
						{ name = "RED SAM SA-15 RG 686" },
						{ name = "RED SAM SA-15 RG 686-1" },
						{ name = "RED SAM SA-15 RG 686-2" },
						{ name = "RED SAM SA-3 RG 674" },
						{ name = "RED SAM SA-3 RG 674-1" },
						{ name = "RED SAM SA-3 RG 674-2" },
					},
					shipGroups = {
					},
					staticGroups = {
						{
							name = "Stoney Cross Airwing Warehouse#00001",
							template = {
								name = "Stoney Cross Airwing Warehouse",
								type = ".Ammunition depot",
								x = 155591.78112467,
								y = -101442.96449276,
								heading = 5.9864793343406,
								category = "Warehouses",
								canCargo = false,
								shape_name = "SkladC",
								rate = 100,
								dead = false
							}
						},
					},
				},
				{
					name = "QRF-13",
					spawnGroups = {
					},
					vehicleGroups = {
						{ name = "RED AIR DEFENSE BATTERY A RG 691" },
						{ name = "RED AIR DEFENSE BATTERY A RG 692" },
						{ name = "RED SAM SA-15 RG 686-3" },
						{ name = "RED SAM SA-15 RG 686-4" },
						{ name = "RED SAM SA-15 RG 686-5" },
						{ name = "RED SAM SA-3 RG 674-3" },
						{ name = "RED SAM SA-3 RG 674-4" },
						{ name = "RED SAM SA-3 RG 674-5" },
					},
					shipGroups = {
					},
					staticGroups = {
						{
							name = "Lymington Airwing Warehouse#00001",
							template = {
								name = "Lymington Airwing Warehouse",
								type = ".Ammunition depot",
								x = 139345.40388958,
								y = -90788.699777832,
								heading = 0.2617993877992,
								category = "Warehouses",
								canCargo = false,
								shape_name = "SkladC",
								rate = 100,
								dead = false
							}
						},
					},
				},
				{
					name = "QRF-14",
					spawnGroups = {
					},
					vehicleGroups = {
						{ name = "RED AIR DEFENSE BATTERY A RG 693" },
						{ name = "RED AIR DEFENSE BATTERY A RG 694" },
						{ name = "RED SAM SA-15 RG 686-6" },
						{ name = "RED SAM SA-15 RG 686-7" },
						{ name = "RED SAM SA-15 RG 686-8" },
						{ name = "RED SAM SA-3 RG 674-6" },
						{ name = "RED SAM SA-3 RG 674-7" },
						{ name = "RED SAM SA-3 RG 674-8" },
					},
					shipGroups = {
					},
					staticGroups = {
						{
							name = "Needs Oar Point Airwing Warehouse#00001",
							template = {
								name = "Needs Oar Point Airwing Warehouse",
								type = ".Ammunition depot",
								x = 140314.3410004,
								y = -85524.362236823,
								heading = 5.8992128717408,
								category = "Warehouses",
								canCargo = false,
								shape_name = "SkladC",
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
				{ name = "RED AIR DEFENSE BATTERY A RG 1" },
				{ name = "RED AIR DEFENSE BATTERY B RG 1" },
				{ name = "RED AIR DEFENSE BATTERY C RG 1" },
				{ name = "RED SAM SA-2 RG 1" },
				{ name = "RED SAM SA-3 RG 1" },
			},
			shipGroups = {
				{ name = "RED RG 1" },
			},
			staticGroups = {
				{
					name = "Static Fueltank-1#00001",
					template = {
						name = "Static Fueltank-1",
						type = "fueltank_cargo",
						x = 113071.93369221,
						y = -156495.96330617,
						heading = 3.9269908169872,
						category = "Cargos",
						canCargo = true,
						shape_name = "fueltank_cargo",
						rate = 100,
						dead = false
					}
				},
				{
					name = "Static Fueltank-2#00001",
					template = {
						name = "Static Fueltank-2",
						type = "fueltank_cargo",
						x = 113069.36247038,
						y = -156488.4732252,
						heading = 4.014257279587,
						category = "Cargos",
						canCargo = true,
						shape_name = "fueltank_cargo",
						rate = 100,
						dead = false
					}
				},
				{
					name = "Static Oiltank-1#00001",
					template = {
						name = "Static Oiltank-1",
						type = "oiltank_cargo",
						x = 113089.02542811,
						y = -156518.81613372,
						heading = 3.8746309394274,
						category = "Cargos",
						canCargo = true,
						shape_name = "oiltank_cargo",
						rate = 100,
						dead = false
					}
				},
				{
					name = "Static Oiltank-2#00001",
					template = {
						name = "Static Oiltank-2",
						type = "oiltank_cargo",
						x = 113085.01338585,
						y = -156512.5644558,
						heading = 3.8222710618676,
						category = "Cargos",
						canCargo = true,
						shape_name = "oiltank_cargo",
						rate = 100,
						dead = false
					}
				},
			}
		},
		{
			name = "OBJ-3",
			strand = "STRAND-1",
			completeSound = "",
			borderZones = {
			},
			capZones = {
				"CAP-4",
			},
			nodes = {
				{ name = "NODE-10" },
				{ name = "NODE-11" },
				{ name = "NODE-12" },
				{ name = "NODE-13" },
				{ name = "NODE-5" },
			},
			tasks = {
			},
			farps = {
				{
					name = "FARP-1",
					vehicleGroups = {
						{ name = "FARP MASH 1-2" },
						{ name = "FARP Support 1-1" },
						{ name = "FARP Support 1-2" },
						{ name = "FARP Support 1-3" },
					},
					shipGroups = {
					},
					staticGroups = {
						{
							name = "MASH Tent 1#00001",
							template = {
								name = "MASH Tent 1",
								type = "FARP Tent",
								x = 111541.46810781,
								y = -157031.31691739,
								heading = 5.4803338512622,
								category = "Fortifications",
								canCargo = false,
								shape_name = "PalatkaB",
								rate = 50,
								dead = false
							}
						},
						{
							name = "MASH Tent 1-1#00001",
							template = {
								name = "MASH Tent 1-1",
								type = "FARP Tent",
								x = 111546.40324635,
								y = -157085.40888838,
								heading = 3.6302848441482,
								category = "Fortifications",
								canCargo = false,
								shape_name = "PalatkaB",
								rate = 50,
								dead = false
							}
						},
						{
							name = "Static Container 20ft-2#00001",
							template = {
								name = "Static Container 20ft-2",
								type = "container_20ft",
								x = 111545.91690155,
								y = -157077.30314177,
								heading = 5.0265482457437,
								category = "Fortifications",
								canCargo = false,
								shape_name = "container_20ft",
								rate = 1,
								dead = false
							}
						},
						{
							name = "Static Container 20ft-3#00001",
							template = {
								name = "Static Container 20ft-3",
								type = "container_20ft",
								x = 111553.21207351,
								y = -157091.56925581,
								heading = 5.0265482457437,
								category = "Fortifications",
								canCargo = false,
								shape_name = "container_20ft",
								rate = 1,
								dead = false
							}
						},
						{
							name = "Static Container 20ft-4#00001",
							template = {
								name = "Static Container 20ft-4",
								type = "container_20ft",
								x = 111546.24113142,
								y = -157095.13578432,
								heading = 5.0265482457437,
								category = "Fortifications",
								canCargo = false,
								shape_name = "container_20ft",
								rate = 1,
								dead = false
							}
						},
						{
							name = "Static FARP Tent-5#00001",
							template = {
								name = "Static FARP Tent-5",
								type = "FARP Tent",
								x = 111520.17454493,
								y = -157037.71621664,
								heading = 5.4803338512622,
								category = "Fortifications",
								canCargo = false,
								shape_name = "PalatkaB",
								rate = 50,
								dead = false
							}
						},
						{
							name = "Static FARP Tent-6#00001",
							template = {
								name = "Static FARP Tent-6",
								type = "FARP Tent",
								x = 111512.23463071,
								y = -157083.18034585,
								heading = 1.5707963267949,
								category = "Fortifications",
								canCargo = false,
								shape_name = "PalatkaB",
								rate = 50,
								dead = false
							}
						},
						{
							name = "Static FARP Tent-7#00001",
							template = {
								name = "Static FARP Tent-7",
								type = "FARP Tent",
								x = 111501.71590316,
								y = -157083.28524714,
								heading = 1.5707963267949,
								category = "Fortifications",
								canCargo = false,
								shape_name = "PalatkaB",
								rate = 50,
								dead = false
							}
						},
						{
							name = "Static FARP Tent-8#00001",
							template = {
								name = "Static FARP Tent-8",
								type = "FARP Tent",
								x = 111491.58525743,
								y = -157083.19144487,
								heading = 1.5707963267949,
								category = "Fortifications",
								canCargo = false,
								shape_name = "PalatkaB",
								rate = 50,
								dead = false
							}
						},
						{
							name = "Static Invisible FARP-1#00001",
							template = {
								name = "Static Invisible FARP-1",
								type = "Invisible FARP",
								x = 111530.31356466,
								y = -156970.70739986,
								heading = 0.0,
								category = "Heliports",
								canCargo = false,
								shape_name = "invisiblefarp",
								rate = 100,
								dead = false
							}
						},
						{
							name = "Static Invisible FARP-2#00001",
							template = {
								name = "Static Invisible FARP-2",
								type = "Invisible FARP",
								x = 111630.14032456,
								y = -157063.76473758,
								heading = 0.0,
								category = "Heliports",
								canCargo = false,
								shape_name = "invisiblefarp",
								rate = 100,
								dead = false
							}
						},
						{
							name = "Static Invisible FARP-3#00001",
							template = {
								name = "Static Invisible FARP-3",
								type = "Invisible FARP",
								x = 111532.3562611,
								y = -157160.31326234,
								heading = 0.0,
								category = "Heliports",
								canCargo = false,
								shape_name = "invisiblefarp",
								rate = 100,
								dead = false
							}
						},
						{
							name = "Static Invisible FARP-4#00001",
							template = {
								name = "Static Invisible FARP-4",
								type = "Invisible FARP",
								x = 111430.33606492,
								y = -157070.47194771,
								heading = 0.0,
								category = "Heliports",
								canCargo = false,
								shape_name = "invisiblefarp",
								rate = 100,
								dead = false
							}
						},
						{
							name = "Static Watch tower armed-3#00001",
							template = {
								name = "Static Watch tower armed-3",
								type = "house2arm",
								x = 111542.70155256,
								y = -157060.79717784,
								heading = 3.6302848441482,
								category = "Fortifications",
								canCargo = false,
								shape_name = "",
								rate = 10,
								dead = false
							}
						},
						{
							name = "Static Windsock-1#00001",
							template = {
								name = "Static Windsock-1",
								type = "Windsock",
								x = 111531.39553305,
								y = -157070.01490128,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "H-Windsock_RW",
								rate = 3,
								dead = false
							}
						},
					},
					clients = {
							"FARP Portland Bill Mi-24P Warm 1",
							"FARP Portland Bill Mi-24P Warm 2",
							"FARP Portland Bill Mi-24P Warm 3",
							"FARP Portland Bill Mi-24P Warm 4",
							"FARP Portland Bill Mi-8MT Warm 1",
							"FARP Portland Bill Mi-8MT Warm 2",
							"FARP Portland Bill Mi-8MT Warm 3",
							"FARP Portland Bill Mi-8MT Warm 4",
							"FARP Portland Bill UH-1H Warm 1",
							"FARP Portland Bill UH-1H Warm 2",
							"FARP Portland Bill UH-1H Warm 3",
							"FARP Portland Bill UH-1H Warm 4",
							"FARP Portland Bill AH-64D_BLK_II Warm 1",
							"FARP Portland Bill AH-64D_BLK_II Warm 2",
							"FARP Portland Bill AH-64D_BLK_II Warm 3",
							"FARP Portland Bill AH-64D_BLK_II Warm 4",
							"FARP Portland Bill SA342L Warm 1",
							"FARP Portland Bill SA342M Warm 1",
							"FARP Portland Bill Ka-50_3 Warm 1",
							"FARP Portland Bill Ka-50_3 Warm 2",
					}
				},
			},
			airbases = {
			},
			carriers = {
			},
			qrfs = {
				{
					name = "QRF-15",
					spawnGroups = {
					},
					vehicleGroups = {
						{ name = "RED RG 1-6" },
						{ name = "RED RG 1-7" },
					},
					shipGroups = {
					},
					staticGroups = {
						{
							name = "INDUSTRYTARGET-111#00001",
							template = {
								name = "INDUSTRYTARGET-111",
								type = "Tank",
								x = 144065.47410801,
								y = -170399.37894847,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-112#00001",
							template = {
								name = "INDUSTRYTARGET-112",
								type = "Tank",
								x = 144013.28666086,
								y = -170395.56035477,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-113#00001",
							template = {
								name = "INDUSTRYTARGET-113",
								type = "Tank",
								x = 144040.01681672,
								y = -170372.96700875,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-114#00001",
							template = {
								name = "INDUSTRYTARGET-114",
								type = "Tank",
								x = 143960.78099756,
								y = -170387.60495124,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-115#00001",
							template = {
								name = "INDUSTRYTARGET-115",
								type = "Tank",
								x = 143989.10223413,
								y = -170368.83019891,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-116#00001",
							template = {
								name = "INDUSTRYTARGET-116",
								type = "Tank",
								x = 144016.78703841,
								y = -170347.19150131,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-117#00001",
							template = {
								name = "INDUSTRYTARGET-117",
								type = "Chemical tank A",
								x = 144135.22216644,
								y = -170777.15748242,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-118#00001",
							template = {
								name = "INDUSTRYTARGET-118",
								type = "Chemical tank A",
								x = 144104.48381694,
								y = -170776.68458474,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-119#00001",
							template = {
								name = "INDUSTRYTARGET-119",
								type = "Chemical tank A",
								x = 144072.79967208,
								y = -170776.21168705,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-120#00001",
							template = {
								name = "INDUSTRYTARGET-120",
								type = "Chemical tank A",
								x = 144165.06582052,
								y = -170872.66076568,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-121#00001",
							template = {
								name = "INDUSTRYTARGET-121",
								type = "Chemical tank A",
								x = 144128.8147526,
								y = -170876.02426683,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-122#00001",
							template = {
								name = "INDUSTRYTARGET-122",
								type = "Chemical tank A",
								x = 144094.43229643,
								y = -170879.76149033,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-123#00001",
							template = {
								name = "INDUSTRYTARGET-123",
								type = "Chemical tank A",
								x = 144076.867346,
								y = -170841.64181066,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-124#00001",
							template = {
								name = "INDUSTRYTARGET-124",
								type = "Chemical tank A",
								x = 144061.91845201,
								y = -170809.12796624,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-125#00001",
							template = {
								name = "INDUSTRYTARGET-125",
								type = "Chemical tank A",
								x = 144039.86883338,
								y = -170777.73528887,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-126#00001",
							template = {
								name = "INDUSTRYTARGET-126",
								type = "Chemical tank A",
								x = 144147.87459243,
								y = -170902.932276,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-127#00001",
							template = {
								name = "INDUSTRYTARGET-127",
								type = "Chemical tank A",
								x = 144112.74469157,
								y = -170909.28555595,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-67#00001",
							template = {
								name = "INDUSTRYTARGET-67",
								type = "Boiler-house A",
								x = 143998.67260559,
								y = -170530.76461991,
								heading = 0.5061454830784,
								category = "Fortifications",
								canCargo = false,
								shape_name = "kotelnaya_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-68#00001",
							template = {
								name = "INDUSTRYTARGET-68",
								type = "Comms tower M",
								x = 144461.01934735,
								y = -170606.60526738,
								heading = 0.4363323129986,
								category = "Fortifications",
								canCargo = false,
								shape_name = "tele_bash_m",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-69#00001",
							template = {
								name = "INDUSTRYTARGET-69",
								type = "Tank",
								x = 144083.61242806,
								y = -170434.382724,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-70#00001",
							template = {
								name = "INDUSTRYTARGET-70",
								type = "Tech hangar A",
								x = 143866.89921772,
								y = -170343.39036785,
								heading = 5.235987755983,
								category = "Fortifications",
								canCargo = false,
								shape_name = "ceh_ang_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-71#00001",
							template = {
								name = "INDUSTRYTARGET-71",
								type = "Chemical tank A",
								x = 144093.13427251,
								y = -170808.3687296,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-72#00001",
							template = {
								name = "INDUSTRYTARGET-72",
								type = "Chemical tank A",
								x = 144110.50837119,
								y = -170840.25456214,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-73#00001",
							template = {
								name = "INDUSTRYTARGET-73",
								type = "Boiler-house A",
								x = 144025.66622944,
								y = -170586.86901458,
								heading = 0.4188790204786,
								category = "Fortifications",
								canCargo = false,
								shape_name = "kotelnaya_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-74#00001",
							template = {
								name = "INDUSTRYTARGET-74",
								type = "Tank",
								x = 144057.31600281,
								y = -170464.08514899,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-75#00001",
							template = {
								name = "INDUSTRYTARGET-75",
								type = "Warehouse",
								x = 144042.14563209,
								y = -170650.99432521,
								heading = 3.6128315516283,
								category = "Warehouses",
								canCargo = false,
								shape_name = "sklad",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-76#00001",
							template = {
								name = "INDUSTRYTARGET-76",
								type = "Tech hangar A",
								x = 143840.27041719,
								y = -170288.72164467,
								heading = 5.1836278784232,
								category = "Fortifications",
								canCargo = false,
								shape_name = "ceh_ang_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-77#00001",
							template = {
								name = "INDUSTRYTARGET-77",
								type = "Chemical tank A",
								x = 144138.53834453,
								y = -170841.05541852,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-78#00001",
							template = {
								name = "INDUSTRYTARGET-78",
								type = "Chemical tank A",
								x = 144150.82779003,
								y = -170809.31452497,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-79#00001",
							template = {
								name = "INDUSTRYTARGET-79",
								type = "Boiler-house A",
								x = 144013.66906329,
								y = -170558.2875305,
								heading = 0.4537856055185,
								category = "Fortifications",
								canCargo = false,
								shape_name = "kotelnaya_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-80#00001",
							template = {
								name = "INDUSTRYTARGET-80",
								type = "Tank",
								x = 144004.75644168,
								y = -170453.44017458,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-81#00001",
							template = {
								name = "INDUSTRYTARGET-81",
								type = "Tank",
								x = 143984.32899201,
								y = -170415.60797167,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-82#00001",
							template = {
								name = "INDUSTRYTARGET-82",
								type = "Repair workshop",
								x = 143867.41205692,
								y = -170175.47096059,
								heading = 0.5410520681182,
								category = "Fortifications",
								canCargo = false,
								shape_name = "tech",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-83#00001",
							template = {
								name = "INDUSTRYTARGET-83",
								type = "Chemical tank A",
								x = 144121.50813359,
								y = -170809.78742265,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-84#00001",
							template = {
								name = "INDUSTRYTARGET-84",
								type = "Tech combine",
								x = 143810.98808461,
								y = -170067.42815425,
								heading = 2.146754979953,
								category = "Fortifications",
								canCargo = false,
								shape_name = "kombinat",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-85#00001",
							template = {
								name = "INDUSTRYTARGET-85",
								type = "Tank",
								x = 144028.7076341,
								y = -170492.0282068,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-86#00001",
							template = {
								name = "INDUSTRYTARGET-86",
								type = "Tank",
								x = 144034.37944613,
								y = -170429.33227473,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-87#00001",
							template = {
								name = "INDUSTRYTARGET-87",
								type = "Workshop A",
								x = 143934.55357464,
								y = -170463.86542214,
								heading = 2.1293016874331,
								category = "Fortifications",
								canCargo = false,
								shape_name = "tec_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-88#00001",
							template = {
								name = "INDUSTRYTARGET-88",
								type = "Chemical tank A",
								x = 144170.57259978,
								y = -170840.25456214,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
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
				{ name = "RED AIR DEFENSE BATTERY A RG 145" },
				{ name = "RED AIR DEFENSE BATTERY B RG 147" },
				{ name = "RED AIR DEFENSE BATTERY C RG 149" },
				{ name = "RED RG 151" },
				{ name = "RED RG 151-1" },
				{ name = "RED RG 151-2" },
				{ name = "RED RG 151-3" },
				{ name = "RED RG 151-4" },
				{ name = "RED RG 151-5" },
				{ name = "RED RG 151-6" },
				{ name = "RED RG 152" },
				{ name = "RED RG 153" },
				{ name = "RED SAM SA-2 DW 2" },
				{ name = "RED SAM SA-2 RG 3" },
			},
			shipGroups = {
			},
			staticGroups = {
				{
					name = "Static Fueltank-3#00001",
					template = {
						name = "Static Fueltank-3",
						type = "fueltank_cargo",
						x = 123677.62877371,
						y = -163553.66215895,
						heading = 4.014257279587,
						category = "Cargos",
						canCargo = true,
						shape_name = "fueltank_cargo",
						rate = 100,
						dead = false
					}
				},
				{
					name = "Static Fueltank-4#00001",
					template = {
						name = "Static Fueltank-4",
						type = "fueltank_cargo",
						x = 123676.6254246,
						y = -163565.45151101,
						heading = 3.9269908169872,
						category = "Cargos",
						canCargo = true,
						shape_name = "fueltank_cargo",
						rate = 100,
						dead = false
					}
				},
				{
					name = "Static Fueltank-5#00001",
					template = {
						name = "Static Fueltank-5",
						type = "fueltank_cargo",
						x = 126101.10347056,
						y = -160987.3009249,
						heading = 3.9269908169872,
						category = "Cargos",
						canCargo = true,
						shape_name = "fueltank_cargo",
						rate = 100,
						dead = false
					}
				},
				{
					name = "Static Fueltank-6#00001",
					template = {
						name = "Static Fueltank-6",
						type = "fueltank_cargo",
						x = 126102.10681967,
						y = -160975.51157285,
						heading = 4.014257279587,
						category = "Cargos",
						canCargo = true,
						shape_name = "fueltank_cargo",
						rate = 100,
						dead = false
					}
				},
				{
					name = "Static Oiltank-6#00001",
					template = {
						name = "Static Oiltank-6",
						type = "oiltank_cargo",
						x = 126107.87607706,
						y = -160997.08357874,
						heading = 3.8222710618676,
						category = "Cargos",
						canCargo = true,
						shape_name = "oiltank_cargo",
						rate = 100,
						dead = false
					}
				},
				{
					name = "Static Oiltank-3#00001",
					template = {
						name = "Static Oiltank-3",
						type = "oiltank_cargo",
						x = 123681.64217015,
						y = -163586.77267962,
						heading = 3.8746309394274,
						category = "Cargos",
						canCargo = true,
						shape_name = "oiltank_cargo",
						rate = 100,
						dead = false
					}
				},
				{
					name = "Static Oiltank-4#00001",
					template = {
						name = "Static Oiltank-4",
						type = "oiltank_cargo",
						x = 123683.3980311,
						y = -163575.23416485,
						heading = 3.8222710618676,
						category = "Cargos",
						canCargo = true,
						shape_name = "oiltank_cargo",
						rate = 100,
						dead = false
					}
				},
				{
					name = "Static Oiltank-5#00001",
					template = {
						name = "Static Oiltank-5",
						type = "oiltank_cargo",
						x = 126106.12021611,
						y = -161008.62209352,
						heading = 3.8746309394274,
						category = "Cargos",
						canCargo = true,
						shape_name = "oiltank_cargo",
						rate = 100,
						dead = false
					}
				},
			}
		},
		{
			name = "OBJ-4",
			strand = "STRAND-1",
			completeSound = "",
			borderZones = {
			},
			capZones = {
				"CAP-4",
			},
			nodes = {
				{ name = "NODE-14" },
				{ name = "NODE-15" },
				{ name = "NODE-16" },
				{ name = "NODE-17" },
				{ name = "NODE-6" },
			},
			tasks = {
			},
			farps = {
			},
			airbases = {
			},
			carriers = {
			},
			qrfs = {
				{
					name = "QRF-5",
					spawnGroups = {
						{ name = "RED QRF 1" },
						{ name = "RED QRF 2" },
						{ name = "RED QRF 3" },
						{ name = "RED QRF 4" },
						{ name = "RED QRF 5" },
						{ name = "RED QRF 6" },
						{ name = "RED QRF 7" },
						{ name = "RED QRF 8" },
					},
					vehicleGroups = {
					},
					shipGroups = {
					},
					staticGroups = {
					},
				},
				{
					name = "QRF-16",
					spawnGroups = {
					},
					vehicleGroups = {
						{ name = "RED RG 1-4" },
						{ name = "RED RG 1-5" },
					},
					shipGroups = {
					},
					staticGroups = {
						{
							name = "INDUSTRYTARGET-45#00001",
							template = {
								name = "INDUSTRYTARGET-45",
								type = "Boiler-house A",
								x = 150437.85539745,
								y = -134612.88428984,
								heading = 1.5882496193148,
								category = "Fortifications",
								canCargo = false,
								shape_name = "kotelnaya_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-46#00001",
							template = {
								name = "INDUSTRYTARGET-46",
								type = "Comms tower M",
								x = 150514.57951381,
								y = -134461.54827617,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "tele_bash_m",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-47#00001",
							template = {
								name = "INDUSTRYTARGET-47",
								type = "Tank",
								x = 150362.30017819,
								y = -134525.55383042,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-48#00001",
							template = {
								name = "INDUSTRYTARGET-48",
								type = "Tech hangar A",
								x = 150294.09858508,
								y = -134828.67465984,
								heading = 6.0562925044203,
								category = "Fortifications",
								canCargo = false,
								shape_name = "ceh_ang_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-49#00001",
							template = {
								name = "INDUSTRYTARGET-49",
								type = "Chemical tank A",
								x = 150526.56079995,
								y = -134652.63967989,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-50#00001",
							template = {
								name = "INDUSTRYTARGET-50",
								type = "Chemical tank A",
								x = 150267.25955879,
								y = -134752.80984151,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-51#00001",
							template = {
								name = "INDUSTRYTARGET-51",
								type = "Boiler-house A",
								x = 150469.44295187,
								y = -134612.09950588,
								heading = 1.5882496193148,
								category = "Fortifications",
								canCargo = false,
								shape_name = "kotelnaya_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-52#00001",
							template = {
								name = "INDUSTRYTARGET-52",
								type = "Tank",
								x = 150380.36162252,
								y = -134477.44804726,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-53#00001",
							template = {
								name = "INDUSTRYTARGET-53",
								type = "Warehouse",
								x = 150398.69883964,
								y = -134589.2221163,
								heading = 2.6529004630314,
								category = "Warehouses",
								canCargo = false,
								shape_name = "sklad",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-54#00001",
							template = {
								name = "INDUSTRYTARGET-54",
								type = "Tech hangar A",
								x = 150315.6339316,
								y = -134763.55587391,
								heading = 5.9690260418206,
								category = "Fortifications",
								canCargo = false,
								shape_name = "ceh_ang_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-55#00001",
							template = {
								name = "INDUSTRYTARGET-55",
								type = "Chemical tank A",
								x = 150466.96589367,
								y = -134652.63967989,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-56#00001",
							template = {
								name = "INDUSTRYTARGET-56",
								type = "Chemical tank A",
								x = 150255.84776823,
								y = -134788.9471783,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-57#00001",
							template = {
								name = "INDUSTRYTARGET-57",
								type = "Boiler-house A",
								x = 150498.08756643,
								y = -134611.90330989,
								heading = 1.5882496193148,
								category = "Fortifications",
								canCargo = false,
								shape_name = "kotelnaya_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-58#00001",
							template = {
								name = "INDUSTRYTARGET-58",
								type = "Tank",
								x = 150441.12317836,
								y = -134352.69865828,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-59#00001",
							template = {
								name = "INDUSTRYTARGET-59",
								type = "Tank",
								x = 150420.1523759,
								y = -134395.71568896,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-60#00001",
							template = {
								name = "INDUSTRYTARGET-60",
								type = "Repair workshop",
								x = 150545.85704091,
								y = -134314.90282124,
								heading = 1.4835298641952,
								category = "Fortifications",
								canCargo = false,
								shape_name = "tech",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-61#00001",
							template = {
								name = "INDUSTRYTARGET-61",
								type = "Chemical tank A",
								x = 150496.76334681,
								y = -134651.37170316,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-62#00001",
							template = {
								name = "INDUSTRYTARGET-62",
								type = "Tech combine",
								x = 150272.33146571,
								y = -134650.73771479,
								heading = 4.4854961776254,
								category = "Fortifications",
								canCargo = false,
								shape_name = "kombinat",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-63#00001",
							template = {
								name = "INDUSTRYTARGET-63",
								type = "Tank",
								x = 150341.43619746,
								y = -134563.24732047,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-64#00001",
							template = {
								name = "INDUSTRYTARGET-64",
								type = "Tank",
								x = 150403.48327651,
								y = -134438.73271965,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-65#00001",
							template = {
								name = "INDUSTRYTARGET-65",
								type = "Workshop A",
								x = 150385.88018099,
								y = -134684.59293664,
								heading = 1.0122909661567,
								category = "Fortifications",
								canCargo = false,
								shape_name = "tec_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-66#00001",
							template = {
								name = "INDUSTRYTARGET-66",
								type = "Chemical tank A",
								x = 150555.09027636,
								y = -134651.37170316,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
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
				{ name = "RED EWR 1-1" },
				{ name = "RED GROUND 1-120" },
				{ name = "RED GROUND 1-121" },
				{ name = "RED GROUND 1-122" },
				{ name = "RED GROUND 1-123" },
				{ name = "RED GROUND 1-124" },
				{ name = "RED GROUND 1-125" },
				{ name = "RED GROUND 1-126" },
				{ name = "RED GROUND 1-127" },
				{ name = "RED GROUND 1-128" },
				{ name = "RED GROUND 1-78" },
				{ name = "RED GROUND 1-89" },
				{ name = "RED GROUND 1-91" },
				{ name = "RED GROUND 1-92" },
				{ name = "RED GROUND 1-94" },
				{ name = "RED GROUND 1-95" },
				{ name = "RED GROUND 1-96" },
				{ name = "RED GROUND 10-15" },
				{ name = "RED GROUND 10-16" },
				{ name = "RED GROUND 10-17" },
				{ name = "RED GROUND 10-18" },
				{ name = "RED SAM SA-8 379-1" },
			},
			shipGroups = {
			},
			staticGroups = {
			}
		},
		{
			name = "OBJ-5",
			strand = "STRAND-1",
			completeSound = "",
			borderZones = {
			},
			capZones = {
				"CAP-4",
			},
			nodes = {
				{ name = "NODE-18" },
				{ name = "NODE-19" },
				{ name = "NODE-20" },
				{ name = "NODE-3" },
			},
			tasks = {
			},
			farps = {
				{
					name = "FARP-2",
					vehicleGroups = {
						{ name = "FARP MASH 1-1" },
						{ name = "FARP Support 1-4" },
						{ name = "FARP Support 1-5" },
						{ name = "FARP Support 1-6" },
					},
					shipGroups = {
					},
					staticGroups = {
						{
							name = "MASH Tent 1-2#00001",
							template = {
								name = "MASH Tent 1-2",
								type = "FARP Tent",
								x = 134163.1041662,
								y = -133779.71931947,
								heading = 5.4803338512622,
								category = "Fortifications",
								canCargo = false,
								shape_name = "PalatkaB",
								rate = 50,
								dead = false
							}
						},
						{
							name = "MASH Tent 1-3#00001",
							template = {
								name = "MASH Tent 1-3",
								type = "FARP Tent",
								x = 134168.03930474,
								y = -133833.81129046,
								heading = 3.6302848441482,
								category = "Fortifications",
								canCargo = false,
								shape_name = "PalatkaB",
								rate = 50,
								dead = false
							}
						},
						{
							name = "Static Container 20ft-1#00001",
							template = {
								name = "Static Container 20ft-1",
								type = "container_20ft",
								x = 134167.55295994,
								y = -133825.70554385,
								heading = 5.0265482457437,
								category = "Fortifications",
								canCargo = false,
								shape_name = "container_20ft",
								rate = 1,
								dead = false
							}
						},
						{
							name = "Static Container 20ft-5#00001",
							template = {
								name = "Static Container 20ft-5",
								type = "container_20ft",
								x = 134174.8481319,
								y = -133839.97165789,
								heading = 5.0265482457437,
								category = "Fortifications",
								canCargo = false,
								shape_name = "container_20ft",
								rate = 1,
								dead = false
							}
						},
						{
							name = "Static Container 20ft-6#00001",
							template = {
								name = "Static Container 20ft-6",
								type = "container_20ft",
								x = 134167.87718981,
								y = -133843.5381864,
								heading = 5.0265482457437,
								category = "Fortifications",
								canCargo = false,
								shape_name = "container_20ft",
								rate = 1,
								dead = false
							}
						},
						{
							name = "Static FARP Tent-13#00001",
							template = {
								name = "Static FARP Tent-13",
								type = "FARP Tent",
								x = 134141.81060332,
								y = -133786.11861872,
								heading = 5.4803338512622,
								category = "Fortifications",
								canCargo = false,
								shape_name = "PalatkaB",
								rate = 50,
								dead = false
							}
						},
						{
							name = "Static FARP Tent-14#00001",
							template = {
								name = "Static FARP Tent-14",
								type = "FARP Tent",
								x = 134133.8706891,
								y = -133831.58274793,
								heading = 1.5707963267949,
								category = "Fortifications",
								canCargo = false,
								shape_name = "PalatkaB",
								rate = 50,
								dead = false
							}
						},
						{
							name = "Static FARP Tent-15#00001",
							template = {
								name = "Static FARP Tent-15",
								type = "FARP Tent",
								x = 134123.35196155,
								y = -133831.68764922,
								heading = 1.5707963267949,
								category = "Fortifications",
								canCargo = false,
								shape_name = "PalatkaB",
								rate = 50,
								dead = false
							}
						},
						{
							name = "Static FARP Tent-18#00001",
							template = {
								name = "Static FARP Tent-18",
								type = "FARP Tent",
								x = 134113.22131582,
								y = -133831.59384695,
								heading = 1.5707963267949,
								category = "Fortifications",
								canCargo = false,
								shape_name = "PalatkaB",
								rate = 50,
								dead = false
							}
						},
						{
							name = "Static Invisible FARP-5#00001",
							template = {
								name = "Static Invisible FARP-5",
								type = "Invisible FARP",
								x = 134151.94962305,
								y = -133719.10980194,
								heading = 0.0,
								category = "Heliports",
								canCargo = false,
								shape_name = "invisiblefarp",
								rate = 100,
								dead = false
							}
						},
						{
							name = "Static Invisible FARP-6#00001",
							template = {
								name = "Static Invisible FARP-6",
								type = "Invisible FARP",
								x = 134251.77638295,
								y = -133812.16713966,
								heading = 0.0,
								category = "Heliports",
								canCargo = false,
								shape_name = "invisiblefarp",
								rate = 100,
								dead = false
							}
						},
						{
							name = "Static Invisible FARP-7#00001",
							template = {
								name = "Static Invisible FARP-7",
								type = "Invisible FARP",
								x = 134153.99231949,
								y = -133908.71566442,
								heading = 0.0,
								category = "Heliports",
								canCargo = false,
								shape_name = "invisiblefarp",
								rate = 100,
								dead = false
							}
						},
						{
							name = "Static Invisible FARP-8#00001",
							template = {
								name = "Static Invisible FARP-8",
								type = "Invisible FARP",
								x = 134051.97212331,
								y = -133818.87434979,
								heading = 0.0,
								category = "Heliports",
								canCargo = false,
								shape_name = "invisiblefarp",
								rate = 100,
								dead = false
							}
						},
						{
							name = "Static Watch tower armed-1#00001",
							template = {
								name = "Static Watch tower armed-1",
								type = "house2arm",
								x = 134164.33761095,
								y = -133809.19957992,
								heading = 3.6302848441482,
								category = "Fortifications",
								canCargo = false,
								shape_name = "",
								rate = 10,
								dead = false
							}
						},
						{
							name = "Static Windsock-2#00001",
							template = {
								name = "Static Windsock-2",
								type = "Windsock",
								x = 134153.03159144,
								y = -133818.41730336,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "H-Windsock_RW",
								rate = 3,
								dead = false
							}
						},
					},
					clients = {
							"FARP Morden Bog Mi-24P Warm 1",
							"FARP Morden Bog Mi-24P Warm 2",
							"FARP Morden Bog Mi-24P Warm 3",
							"FARP Morden Bog Mi-24P Warm 4",
							"FARP Morden Bog Mi-8MT Warm 1",
							"FARP Morden Bog Mi-8MT Warm 2",
							"FARP Morden Bog Mi-8MT Warm 3",
							"FARP Morden Bog Mi-8MT Warm 4",
							"FARP Morden Bog UH-1H Warm 1",
							"FARP Morden Bog UH-1H Warm 2",
							"FARP Morden Bog UH-1H Warm 3",
							"FARP Morden Bog UH-1H Warm 4",
							"FARP Morden Bog AH-64D_BLK_II Warm 1",
							"FARP Morden Bog AH-64D_BLK_II Warm 2",
							"FARP Morden Bog AH-64D_BLK_II Warm 3",
							"FARP Morden Bog AH-64D_BLK_II Warm 4",
							"FARP Morden Bog SA342L Warm 1",
							"FARP Morden Bog SA342M Warm 1",
							"FARP Morden Bog Ka-50_3 Warm 1",
							"FARP Morden Bog Ka-50_3 Warm 2",
					}
				},
			},
			airbases = {
			},
			carriers = {
			},
			qrfs = {
				{
					name = "QRF-4",
					spawnGroups = {
						{ name = "RED QRF 1" },
						{ name = "RED QRF 2" },
						{ name = "RED QRF 3" },
						{ name = "RED QRF 4" },
						{ name = "RED QRF 5" },
						{ name = "RED QRF 6" },
						{ name = "RED QRF 7" },
						{ name = "RED QRF 8" },
					},
					vehicleGroups = {
					},
					shipGroups = {
					},
					staticGroups = {
					},
				},
				{
					name = "QRF-12",
					spawnGroups = {
					},
					vehicleGroups = {
						{ name = "RED AIR DEFENSE BATTERY A 242-2" },
						{ name = "RED AIR DEFENSE BATTERY C RG 246-2" },
						{ name = "RED RG 152-10" },
						{ name = "RED RG 152-11" },
						{ name = "RED RG 152-12" },
						{ name = "RED RG 152-13" },
						{ name = "RED RG 152-14" },
						{ name = "RED RG 152-8" },
						{ name = "RED RG 152-9" },
						{ name = "RED SAM SA-2 RG 234-2" },
						{ name = "RED SAM SA-3 236-2" },
						{ name = "RED SAM SA-6 238-3" },
						{ name = "RED SAM SA-6 238-4" },
						{ name = "RED SAM SA-8 RG 240-3" },
						{ name = "RED SAM SA-8 RG 240-4" },
					},
					shipGroups = {
					},
					staticGroups = {
						{
							name = "FOB Yes Minister Airwing Warehouse#00001",
							template = {
								name = "FOB Yes Minister Airwing Warehouse",
								type = ".Ammunition depot",
								x = 145949.80953861,
								y = -122099.55128433,
								heading = 3.5430183815485,
								category = "Warehouses",
								canCargo = false,
								shape_name = "SkladC",
								rate = 100,
								dead = false
							}
						},
						{
							name = "FOB Yes Minister Brigade Warehouse#00001",
							template = {
								name = "FOB Yes Minister Brigade Warehouse",
								type = ".Ammunition depot",
								x = 145436.07536451,
								y = -122436.8177019,
								heading = 2.3736477827123,
								category = "Warehouses",
								canCargo = false,
								shape_name = "SkladC",
								rate = 100,
								dead = false
							}
						},
						{
							name = "FOB Yes Minister Farp#00001",
							template = {
								name = "FOB Yes Minister Farp",
								type = "FARP",
								x = 145762.62294347,
								y = -122415.88361338,
								heading = 2.1118483949131,
								category = "Heliports",
								canCargo = false,
								shape_name = "FARPS",
								rate = 50,
								dead = false
							}
						},
						{
							name = "Static Container 40ft-10#00001",
							template = {
								name = "Static Container 40ft-10",
								type = "container_40ft",
								x = 145792.87252663,
								y = -122694.49581192,
								heading = 1.7278759594744,
								category = "Fortifications",
								canCargo = false,
								shape_name = "container_40ft",
								rate = 1,
								dead = false
							}
						},
						{
							name = "Static Container 40ft-6#00001",
							template = {
								name = "Static Container 40ft-6",
								type = "container_40ft",
								x = 145775.2019227,
								y = -122711.16619298,
								heading = 1.5009831567151,
								category = "Fortifications",
								canCargo = false,
								shape_name = "container_40ft",
								rate = 1,
								dead = false
							}
						},
						{
							name = "Static Container 40ft-7#00001",
							template = {
								name = "Static Container 40ft-7",
								type = "container_40ft",
								x = 145763.53265596,
								y = -122682.49313755,
								heading = 1.553343034275,
								category = "Fortifications",
								canCargo = false,
								shape_name = "container_40ft",
								rate = 1,
								dead = false
							}
						},
						{
							name = "Static Container 40ft-8#00001",
							template = {
								name = "Static Container 40ft-8",
								type = "container_40ft",
								x = 145765.53310168,
								y = -122696.49625765,
								heading = 1.6057029118348,
								category = "Fortifications",
								canCargo = false,
								shape_name = "container_40ft",
								rate = 1,
								dead = false
							}
						},
						{
							name = "Static Container 40ft-9#00001",
							template = {
								name = "Static Container 40ft-9",
								type = "container_40ft",
								x = 145794.87297236,
								y = -122705.83167104,
								heading = 1.7453292519943,
								category = "Fortifications",
								canCargo = false,
								shape_name = "container_40ft",
								rate = 1,
								dead = false
							}
						},
						{
							name = "Static Excavator-4#00001",
							template = {
								name = "Static Excavator-4",
								type = "345 Excavator",
								x = 145800.53506843,
								y = -122114.91228844,
								heading = 2.146754979953,
								category = "Fortifications",
								canCargo = false,
								shape_name = "cat_345l",
								rate = 3,
								dead = false
							}
						},
						{
							name = "Static Excavator-5#00001",
							template = {
								name = "Static Excavator-5",
								type = "345 Excavator",
								x = 146019.68374777,
								y = -122531.43745813,
								heading = 1.1344640137963,
								category = "Fortifications",
								canCargo = false,
								shape_name = "cat_345l",
								rate = 3,
								dead = false
							}
						},
						{
							name = "Static Excavator-6#00001",
							template = {
								name = "Static Excavator-6",
								type = "345 Excavator",
								x = 145726.03889405,
								y = -122734.79778515,
								heading = 2.146754979953,
								category = "Fortifications",
								canCargo = false,
								shape_name = "cat_345l",
								rate = 3,
								dead = false
							}
						},
						{
							name = "Static FARP Tent-19#00001",
							template = {
								name = "Static FARP Tent-19",
								type = "FARP Tent",
								x = 145531.02360096,
								y = -122672.95543604,
								heading = 2.146754979953,
								category = "Fortifications",
								canCargo = false,
								shape_name = "PalatkaB",
								rate = 50,
								dead = false
							}
						},
						{
							name = "Static FARP Tent-20#00001",
							template = {
								name = "Static FARP Tent-20",
								type = "FARP Tent",
								x = 145515.27034648,
								y = -122686.87081083,
								heading = 2.146754979953,
								category = "Fortifications",
								canCargo = false,
								shape_name = "PalatkaB",
								rate = 50,
								dead = false
							}
						},
						{
							name = "Static FARP Tent-21#00001",
							template = {
								name = "Static FARP Tent-21",
								type = "FARP Tent",
								x = 145550.02583269,
								y = -122661.77146934,
								heading = 2.146754979953,
								category = "Fortifications",
								canCargo = false,
								shape_name = "PalatkaB",
								rate = 50,
								dead = false
							}
						},
						{
							name = "Static FARP Tent-22#00001",
							template = {
								name = "Static FARP Tent-22",
								type = "FARP Tent",
								x = 145497.41665807,
								y = -122699.47341442,
								heading = 2.146754979953,
								category = "Fortifications",
								canCargo = false,
								shape_name = "PalatkaB",
								rate = 50,
								dead = false
							}
						},
						{
							name = "Static FARP Tent-23#00001",
							template = {
								name = "Static FARP Tent-23",
								type = "FARP Tent",
								x = 145548.61473513,
								y = -122698.94830593,
								heading = 2.146754979953,
								category = "Fortifications",
								canCargo = false,
								shape_name = "PalatkaB",
								rate = 50,
								dead = false
							}
						},
						{
							name = "Static FARP Tent-24#00001",
							template = {
								name = "Static FARP Tent-24",
								type = "FARP Tent",
								x = 145567.78119475,
								y = -122690.80912445,
								heading = 2.146754979953,
								category = "Fortifications",
								canCargo = false,
								shape_name = "PalatkaB",
								rate = 50,
								dead = false
							}
						},
						{
							name = "Static FARP Tent-25#00001",
							template = {
								name = "Static FARP Tent-25",
								type = "FARP Tent",
								x = 145530.23593824,
								y = -122711.28835528,
								heading = 2.146754979953,
								category = "Fortifications",
								canCargo = false,
								shape_name = "PalatkaB",
								rate = 50,
								dead = false
							}
						},
						{
							name = "Static FARP Tent-26#00001",
							template = {
								name = "Static FARP Tent-26",
								type = "FARP Tent",
								x = 145510.54437014,
								y = -122724.1535131,
								heading = 2.146754979953,
								category = "Fortifications",
								canCargo = false,
								shape_name = "PalatkaB",
								rate = 50,
								dead = false
							}
						},
						{
							name = "Static Mi-24P-3#00001",
							template = {
								name = "Static Mi-24P-3",
								type = "Mi-24P",
								x = 145946.29624674,
								y = -121980.50670623,
								heading = 1.5707963267949,
								category = "Helicopters",
								canCargo = false,
								shape_name = "",
								rate = 20,
								dead = false
							}
						},
						{
							name = "Static Mi-24P-4#00001",
							template = {
								name = "Static Mi-24P-4",
								type = "Mi-24P",
								x = 145973.30070409,
								y = -121955.89744547,
								heading = 1.553343034275,
								category = "Helicopters",
								canCargo = false,
								shape_name = "",
								rate = 20,
								dead = false
							}
						},
						{
							name = "Static Mi-24P-5#00001",
							template = {
								name = "Static Mi-24P-5",
								type = "Mi-24P",
								x = 145927.82948953,
								y = -121933.6018822,
								heading = 1.5707963267949,
								category = "Helicopters",
								canCargo = false,
								shape_name = "",
								rate = 20,
								dead = false
							}
						},
						{
							name = "Static Mi-24P-6#00001",
							template = {
								name = "Static Mi-24P-6",
								type = "Mi-24P",
								x = 145960.39274641,
								y = -121920.9872872,
								heading = 1.553343034275,
								category = "Helicopters",
								canCargo = false,
								shape_name = "",
								rate = 20,
								dead = false
							}
						},
						{
							name = "Static Mi-26-4#00001",
							template = {
								name = "Static Mi-26-4",
								type = "Mi-26",
								x = 145921.96441369,
								y = -122181.38185551,
								heading = 6.0737457969403,
								category = "Helicopters",
								canCargo = false,
								shape_name = "",
								rate = 30,
								dead = false
							}
						},
						{
							name = "Static Mi-26-5#00001",
							template = {
								name = "Static Mi-26-5",
								type = "Mi-26",
								x = 146000.86102405,
								y = -122222.87603766,
								heading = 6.0737457969403,
								category = "Helicopters",
								canCargo = false,
								shape_name = "",
								rate = 30,
								dead = false
							}
						},
						{
							name = "Static Mi-26-6#00001",
							template = {
								name = "Static Mi-26-6",
								type = "Mi-26",
								x = 145951.78494111,
								y = -122271.9521206,
								heading = 6.0737457969403,
								category = "Helicopters",
								canCargo = false,
								shape_name = "",
								rate = 30,
								dead = false
							}
						},
						{
							name = "Static Military staff-4#00001",
							template = {
								name = "Static Military staff-4",
								type = "Military staff",
								x = 145812.60804752,
								y = -121873.91206889,
								heading = 1.9896753472735,
								category = "Fortifications",
								canCargo = false,
								shape_name = "aviashtab",
								rate = 100,
								dead = false
							}
						},
						{
							name = "Static Military staff-5#00001",
							template = {
								name = "Static Military staff-5",
								type = "Military staff",
								x = 145738.98924137,
								y = -121909.72662323,
								heading = 2.0594885173533,
								category = "Fortifications",
								canCargo = false,
								shape_name = "aviashtab",
								rate = 100,
								dead = false
							}
						},
						{
							name = "Static Military staff-6#00001",
							template = {
								name = "Static Military staff-6",
								type = "Military staff",
								x = 145776.79349318,
								y = -121891.57063388,
								heading = 1.9722220547536,
								category = "Fortifications",
								canCargo = false,
								shape_name = "aviashtab",
								rate = 100,
								dead = false
							}
						},
						{
							name = "Static Tank 1-4#00001",
							template = {
								name = "Static Tank 1-4",
								type = "Tank",
								x = 145961.07516338,
								y = -122762.81585643,
								heading = 0.0645788929948,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "Static Tank 1-5#00001",
							template = {
								name = "Static Tank 1-5",
								type = "Tank",
								x = 145901.69916495,
								y = -122805.08351633,
								heading = 0.0645788929948,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "Static Tank 1-6#00001",
							template = {
								name = "Static Tank 1-6",
								type = "Tank",
								x = 145840.31042081,
								y = -122849.36392194,
								heading = 0.0645788929948,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "Static Small warehouse 3-3#00001",
							template = {
								name = "Static Small warehouse 3-3",
								type = "Small werehouse 3",
								x = 145514.5411652,
								y = -122277.80265483,
								heading = 3.9444441095072,
								category = "Fortifications",
								canCargo = false,
								shape_name = "s3",
								rate = 100,
								dead = false
							}
						},
						{
							name = "Static Tank 1-7#00001",
							template = {
								name = "Static Tank 1-7",
								type = "Tank",
								x = 145963.36617683,
								y = -122687.13134802,
								heading = 0.0645788929948,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "Static Small warehouse 3-4#00001",
							template = {
								name = "Static Small warehouse 3-4",
								type = "Small werehouse 3",
								x = 145493.37454114,
								y = -122300.11342074,
								heading = 3.9618974020271,
								category = "Fortifications",
								canCargo = false,
								shape_name = "s3",
								rate = 100,
								dead = false
							}
						},
						{
							name = "Static Tank 1-8#00001",
							template = {
								name = "Static Tank 1-8",
								type = "Tank",
								x = 145911.1362536,
								y = -122730.38425319,
								heading = 0.0645788929948,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "Static Tank 1-9#00001",
							template = {
								name = "Static Tank 1-9",
								type = "Tank",
								x = 145848.29712721,
								y = -122777.71762112,
								heading = 0.0645788929948,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
					},
				},
				{
					name = "QRF-17",
					spawnGroups = {
					},
					vehicleGroups = {
						{ name = "RED RG 1-2" },
						{ name = "RED RG 1-3" },
					},
					shipGroups = {
					},
					staticGroups = {
						{
							name = "INDUSTRYTARGET-10#00001",
							template = {
								name = "INDUSTRYTARGET-10",
								type = "Boiler-house A",
								x = 156793.25062599,
								y = -133095.50040538,
								heading = 1.7802358370342,
								category = "Fortifications",
								canCargo = false,
								shape_name = "kotelnaya_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-128#00001",
							template = {
								name = "INDUSTRYTARGET-128",
								type = "Chemical tank A",
								x = 156537.16744402,
								y = -133062.02156148,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-129#00001",
							template = {
								name = "INDUSTRYTARGET-129",
								type = "Chemical tank A",
								x = 156507.24078812,
								y = -133103.03216401,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-130#00001",
							template = {
								name = "INDUSTRYTARGET-130",
								type = "Tank",
								x = 156746.65869059,
								y = -132873.38398461,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-131#00001",
							template = {
								name = "INDUSTRYTARGET-131",
								type = "Tank",
								x = 156795.0007142,
								y = -132894.56756799,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-132#00001",
							template = {
								name = "INDUSTRYTARGET-132",
								type = "Tank",
								x = 156852.57660749,
								y = -132911.40580094,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-133#00001",
							template = {
								name = "INDUSTRYTARGET-133",
								type = "Tank",
								x = 156884.62356697,
								y = -132846.22554438,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-134#00001",
							template = {
								name = "INDUSTRYTARGET-134",
								type = "Tank",
								x = 156841.1700626,
								y = -132816.35126013,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-135#00001",
							template = {
								name = "INDUSTRYTARGET-135",
								type = "Tank",
								x = 156800.97557105,
								y = -132797.34035196,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-136#00001",
							template = {
								name = "INDUSTRYTARGET-136",
								type = "Tank",
								x = 156743.94284657,
								y = -132767.46606771,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-137#00001",
							template = {
								name = "INDUSTRYTARGET-137",
								type = "Tank",
								x = 156784.68050692,
								y = -132733.78960182,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-138#00001",
							template = {
								name = "INDUSTRYTARGET-138",
								type = "Tank",
								x = 156821.07281683,
								y = -132691.42243506,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-139#00001",
							template = {
								name = "INDUSTRYTARGET-139",
								type = "Tank",
								x = 156830.3066865,
								y = -132759.31853564,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-140#00001",
							template = {
								name = "INDUSTRYTARGET-140",
								type = "Tank",
								x = 156875.38969729,
								y = -132780.50211902,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-141#00001",
							template = {
								name = "INDUSTRYTARGET-141",
								type = "Tank",
								x = 156922.10221449,
								y = -132756.05952281,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-142#00001",
							template = {
								name = "INDUSTRYTARGET-142",
								type = "Tank",
								x = 156887.33941099,
								y = -132724.01256334,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-143#00001",
							template = {
								name = "INDUSTRYTARGET-143",
								type = "Tank",
								x = 156850.94710108,
								y = -132719.1240441,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-144#00001",
							template = {
								name = "INDUSTRYTARGET-144",
								type = "Tank",
								x = 156867.24216522,
								y = -132670.78202049,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-24#00001",
							template = {
								name = "INDUSTRYTARGET-24",
								type = "Comms tower M",
								x = 157028.7409032,
								y = -132809.49980781,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "tele_bash_m",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-25#00001",
							template = {
								name = "INDUSTRYTARGET-25",
								type = "Tank",
								x = 156806.95042791,
								y = -132963.55000618,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-26#00001",
							template = {
								name = "INDUSTRYTARGET-26",
								type = "Tech hangar A",
								x = 156794.31500585,
								y = -133139.05499056,
								heading = 1.8151424220741,
								category = "Fortifications",
								canCargo = false,
								shape_name = "ceh_ang_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-27#00001",
							template = {
								name = "INDUSTRYTARGET-27",
								type = "Chemical tank A",
								x = 156498.37363081,
								y = -133058.14218016,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-28#00001",
							template = {
								name = "INDUSTRYTARGET-28",
								type = "Chemical tank A",
								x = 156547.14299598,
								y = -133100.81537468,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-29#00001",
							template = {
								name = "INDUSTRYTARGET-29",
								type = "Boiler-house A",
								x = 156838.81681729,
								y = -133081.58703846,
								heading = 1.7802358370342,
								category = "Fortifications",
								canCargo = false,
								shape_name = "kotelnaya_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-30#00001",
							template = {
								name = "INDUSTRYTARGET-30",
								type = "Tank",
								x = 156680.93526523,
								y = -132894.02439919,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-31#00001",
							template = {
								name = "INDUSTRYTARGET-31",
								type = "Warehouse",
								x = 157061.00346696,
								y = -132984.82300413,
								heading = 3.4382986264288,
								category = "Warehouses",
								canCargo = false,
								shape_name = "sklad",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-32#00001",
							template = {
								name = "INDUSTRYTARGET-32",
								type = "Tech hangar A",
								x = 156724.48614207,
								y = -133160.66868649,
								heading = 1.7453292519943,
								category = "Fortifications",
								canCargo = false,
								shape_name = "ceh_ang_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-33#00001",
							template = {
								name = "INDUSTRYTARGET-33",
								type = "Chemical tank A",
								x = 156576.51545456,
								y = -133065.9009428,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-34#00001",
							template = {
								name = "INDUSTRYTARGET-34",
								type = "Chemical tank A",
								x = 156524.42090539,
								y = -133021.01095894,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-35#00001",
							template = {
								name = "INDUSTRYTARGET-35",
								type = "Boiler-house A",
								x = 156733.12373634,
								y = -133112.85457491,
								heading = 1.832595714594,
								category = "Fortifications",
								canCargo = false,
								shape_name = "kotelnaya_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-36#00001",
							template = {
								name = "INDUSTRYTARGET-36",
								type = "Tank",
								x = 156786.85318213,
								y = -133009.71935457,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-37#00001",
							template = {
								name = "INDUSTRYTARGET-37",
								type = "Tank",
								x = 156627.16155357,
								y = -132897.82658082,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-38#00001",
							template = {
								name = "INDUSTRYTARGET-38",
								type = "Repair workshop",
								x = 156908.34058001,
								y = -133121.1291532,
								heading = 3.4208453339089,
								category = "Fortifications",
								canCargo = false,
								shape_name = "tech",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-39#00001",
							template = {
								name = "INDUSTRYTARGET-39",
								type = "Chemical tank A",
								x = 156469.00117224,
								y = -133091.94821738,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-40#00001",
							template = {
								name = "INDUSTRYTARGET-40",
								type = "Tech combine",
								x = 156734.9213764,
								y = -132963.84184933,
								heading = 2.6529004630314,
								category = "Fortifications",
								canCargo = false,
								shape_name = "kombinat",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-41#00001",
							template = {
								name = "INDUSTRYTARGET-41",
								type = "Tank",
								x = 156661.38118827,
								y = -132941.82325399,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-42#00001",
							template = {
								name = "INDUSTRYTARGET-42",
								type = "Tank",
								x = 156703.74835503,
								y = -132847.31188199,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-43#00001",
							template = {
								name = "INDUSTRYTARGET-43",
								type = "Workshop A",
								x = 156951.66534581,
								y = -133006.97403991,
								heading = 5.0789081233035,
								category = "Fortifications",
								canCargo = false,
								shape_name = "tec_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-44#00001",
							template = {
								name = "INDUSTRYTARGET-44",
								type = "Chemical tank A",
								x = 156519.98732674,
								y = -133137.9465959,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
					},
				},
				{
					name = "QRF-18",
					spawnGroups = {
					},
					vehicleGroups = {
						{ name = "RED RG 1-8" },
						{ name = "RED RG 1-9" },
					},
					shipGroups = {
					},
					staticGroups = {
						{
							name = "INDUSTRYTARGET-100#00001",
							template = {
								name = "INDUSTRYTARGET-100",
								type = "Chemical tank A",
								x = 157341.72694874,
								y = -120252.84012458,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-101#00001",
							template = {
								name = "INDUSTRYTARGET-101",
								type = "Boiler-house A",
								x = 157075.68696701,
								y = -119931.08156161,
								heading = 2.0943951023932,
								category = "Fortifications",
								canCargo = false,
								shape_name = "kotelnaya_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-102#00001",
							template = {
								name = "INDUSTRYTARGET-102",
								type = "Tank",
								x = 157025.84333939,
								y = -120096.54092595,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-103#00001",
							template = {
								name = "INDUSTRYTARGET-103",
								type = "Tank",
								x = 156911.71894293,
								y = -120188.34579099,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-104#00001",
							template = {
								name = "INDUSTRYTARGET-104",
								type = "Repair workshop",
								x = 157304.25154856,
								y = -120097.76718569,
								heading = 1.4137166941154,
								category = "Fortifications",
								canCargo = false,
								shape_name = "tech",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-105#00001",
							template = {
								name = "INDUSTRYTARGET-105",
								type = "Chemical tank A",
								x = 157380.10221611,
								y = -120212.50693541,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-106#00001",
							template = {
								name = "INDUSTRYTARGET-106",
								type = "Tech combine",
								x = 157138.56683062,
								y = -119972.49416558,
								heading = 3.0194196059502,
								category = "Fortifications",
								canCargo = false,
								shape_name = "kombinat",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-107#00001",
							template = {
								name = "INDUSTRYTARGET-107",
								type = "Tank",
								x = 156972.36068865,
								y = -120203.08510419,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-108#00001",
							template = {
								name = "INDUSTRYTARGET-108",
								type = "Tank",
								x = 156986.25775538,
								y = -120124.3350594,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-109#00001",
							template = {
								name = "INDUSTRYTARGET-109",
								type = "Workshop A",
								x = 157235.33857932,
								y = -119988.51155847,
								heading = 1.2740903539559,
								category = "Fortifications",
								canCargo = false,
								shape_name = "tec_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-110#00001",
							template = {
								name = "INDUSTRYTARGET-110",
								type = "Chemical tank A",
								x = 157258.31947987,
								y = -120311.18619436,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-145#00001",
							template = {
								name = "INDUSTRYTARGET-145",
								type = "Tank",
								x = 156987.94224832,
								y = -120057.7975884,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-146#00001",
							template = {
								name = "INDUSTRYTARGET-146",
								type = "Tank",
								x = 156948.77778754,
								y = -120159.28828784,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-147#00001",
							template = {
								name = "INDUSTRYTARGET-147",
								type = "Tank",
								x = 156874.23897509,
								y = -120166.86850605,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-148#00001",
							template = {
								name = "INDUSTRYTARGET-148",
								type = "Tank",
								x = 156832.96889815,
								y = -120132.33640085,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-149#00001",
							template = {
								name = "INDUSTRYTARGET-149",
								type = "Tank",
								x = 156792.11994443,
								y = -120102.85777446,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-150#00001",
							template = {
								name = "INDUSTRYTARGET-150",
								type = "Tank",
								x = 156939.09195315,
								y = -120027.47671554,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-151#00001",
							template = {
								name = "INDUSTRYTARGET-151",
								type = "Tank",
								x = 156951.30452694,
								y = -120099.90991182,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-152#00001",
							template = {
								name = "INDUSTRYTARGET-152",
								type = "Tank",
								x = 156902.87535502,
								y = -120134.44201702,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-153#00001",
							template = {
								name = "INDUSTRYTARGET-153",
								type = "Tank",
								x = 156909.61332676,
								y = -120078.85375011,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-154#00001",
							template = {
								name = "INDUSTRYTARGET-154",
								type = "Tank",
								x = 156870.44886599,
								y = -120116.75484119,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-155#00001",
							template = {
								name = "INDUSTRYTARGET-155",
								type = "Tank",
								x = 156890.24165799,
								y = -120034.63581053,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-156#00001",
							template = {
								name = "INDUSTRYTARGET-156",
								type = "Tank",
								x = 156864.13201747,
								y = -120068.74679249,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-157#00001",
							template = {
								name = "INDUSTRYTARGET-157",
								type = "Tank",
								x = 156856.13067602,
								y = -120011.89515588,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-158#00001",
							template = {
								name = "INDUSTRYTARGET-158",
								type = "Tank",
								x = 156829.17878904,
								y = -120078.43262688,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-159#00001",
							template = {
								name = "INDUSTRYTARGET-159",
								type = "Chemical tank A",
								x = 157471.87484061,
								y = -120217.13265469,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-160#00001",
							template = {
								name = "INDUSTRYTARGET-160",
								type = "Chemical tank A",
								x = 157433.73589002,
								y = -120257.04550995,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-161#00001",
							template = {
								name = "INDUSTRYTARGET-161",
								type = "Chemical tank A",
								x = 157402.15457987,
								y = -120280.19466267,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-162#00001",
							template = {
								name = "INDUSTRYTARGET-162",
								type = "Chemical tank A",
								x = 157372.45872107,
								y = -120319.78914107,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-163#00001",
							template = {
								name = "INDUSTRYTARGET-163",
								type = "Chemical tank A",
								x = 157331.45015416,
								y = -120350.42772554,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-164#00001",
							template = {
								name = "INDUSTRYTARGET-164",
								type = "Chemical tank A",
								x = 157289.02749873,
								y = -120378.70949583,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-165#00001",
							template = {
								name = "INDUSTRYTARGET-165",
								type = "Chemical tank A",
								x = 157250.375746,
								y = -120404.16308909,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-166#00001",
							template = {
								name = "INDUSTRYTARGET-166",
								type = "Chemical tank A",
								x = 157214.08080747,
								y = -120432.44485937,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-167#00001",
							template = {
								name = "INDUSTRYTARGET-167",
								type = "Chemical tank A",
								x = 157172.12951488,
								y = -120375.40995596,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-168#00001",
							template = {
								name = "INDUSTRYTARGET-168",
								type = "Chemical tank A",
								x = 157307.95428632,
								y = -120021.34426591,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-169#00001",
							template = {
								name = "INDUSTRYTARGET-169",
								type = "Chemical tank A",
								x = 157359.57543669,
								y = -120016.78945852,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-170#00001",
							template = {
								name = "INDUSTRYTARGET-170",
								type = "Chemical tank A",
								x = 157413.47399076,
								y = -120033.49041894,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-171#00001",
							template = {
								name = "INDUSTRYTARGET-171",
								type = "Chemical tank A",
								x = 157474.96389048,
								y = -120052.46878305,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-172#00001",
							template = {
								name = "INDUSTRYTARGET-172",
								type = "Chemical tank A",
								x = 157534.1763865,
								y = -120069.16974346,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-89#00001",
							template = {
								name = "INDUSTRYTARGET-89",
								type = "Boiler-house A",
								x = 157160.69999303,
								y = -119893.08331513,
								heading = 1.7453292519943,
								category = "Fortifications",
								canCargo = false,
								shape_name = "kotelnaya_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-90#00001",
							template = {
								name = "INDUSTRYTARGET-90",
								type = "Comms tower M",
								x = 157264.50321754,
								y = -119812.6583424,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "tele_bash_m",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-91#00001",
							template = {
								name = "INDUSTRYTARGET-91",
								type = "Tank",
								x = 157023.31659999,
								y = -120161.81502724,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-92#00001",
							template = {
								name = "INDUSTRYTARGET-92",
								type = "Tech hangar A",
								x = 157322.60756334,
								y = -119887.62246471,
								heading = 6.16101225954,
								category = "Fortifications",
								canCargo = false,
								shape_name = "ceh_ang_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-93#00001",
							template = {
								name = "INDUSTRYTARGET-93",
								type = "Chemical tank A",
								x = 157218.76945942,
								y = -120346.03720248,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-94#00001",
							template = {
								name = "INDUSTRYTARGET-94",
								type = "Chemical tank A",
								x = 157413.38688679,
								y = -120165.5168121,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-95#00001",
							template = {
								name = "INDUSTRYTARGET-95",
								type = "Boiler-house A",
								x = 157197.41016335,
								y = -119887.28697245,
								heading = 1.6929693744345,
								category = "Fortifications",
								canCargo = false,
								shape_name = "kotelnaya_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-96#00001",
							template = {
								name = "INDUSTRYTARGET-96",
								type = "Tank",
								x = 157069.21903251,
								y = -120133.59977055,
								heading = 0.0,
								category = "Warehouses",
								canCargo = false,
								shape_name = "bak",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-97#00001",
							template = {
								name = "INDUSTRYTARGET-97",
								type = "Warehouse",
								x = 157045.26551705,
								y = -119979.10134015,
								heading = 4.5727626402251,
								category = "Warehouses",
								canCargo = false,
								shape_name = "sklad",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-98#00001",
							template = {
								name = "INDUSTRYTARGET-98",
								type = "Tech hangar A",
								x = 157224.49782915,
								y = -119895.85102306,
								heading = 0.1396263401595,
								category = "Fortifications",
								canCargo = false,
								shape_name = "ceh_ang_a",
								rate = 100,
								dead = false
							}
						},
						{
							name = "INDUSTRYTARGET-99#00001",
							template = {
								name = "INDUSTRYTARGET-99",
								type = "Chemical tank A",
								x = 157301.78534393,
								y = -120282.60053601,
								heading = 0.0,
								category = "Fortifications",
								canCargo = false,
								shape_name = "him_bak_a",
								rate = 100,
								dead = false
							}
						},
					},
				},
			},
			reinforcements = {
				{
					name = "REINFORCEMENT-2",
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
				{ name = "DW RED GROUND 1-1" },
				{ name = "DW RED GROUND 1-2" },
				{ name = "DW RED GROUND 1-3" },
				{ name = "DW RED GROUND 1-4" },
				{ name = "DW RED GROUND 1-5" },
				{ name = "DW RED GROUND 1-51" },
				{ name = "DW RED GROUND 1-7" },
				{ name = "DW RED GROUND 10-1" },
				{ name = "DW RED GROUND 10-2" },
				{ name = "DW RED GROUND 10-3" },
				{ name = "DW RED GROUND 10-4" },
				{ name = "DW RED GROUND 10-5" },
				{ name = "DW RED GROUND 2" },
				{ name = "DWRED GROUND 10-1" },
				{ name = "DWRED GROUND 10-2" },
				{ name = "RED AIR DEFENSE BATTERY C RG 149-1" },
				{ name = "RED EWR 2-1" },
				{ name = "RED EWR 2-2" },
				{ name = "RED EWR 2-3" },
				{ name = "RED EWR 2-4" },
				{ name = "RED GROUND 1-2" },
				{ name = "RED GROUND 1-3" },
				{ name = "RED GROUND 1-4" },
				{ name = "RED GROUND 1-6" },
				{ name = "RED SAM Rapier DW 3" },
				{ name = "RED SAM Rapier DW 3-1" },
			},
			shipGroups = {
				{ name = "Naval-1" },
				{ name = "Naval-2" },
			},
			staticGroups = {
				{
					name = "Static FARP Tent-16#00001",
					template = {
						name = "Static FARP Tent-16",
						type = "FARP Tent",
						x = 127114.74659466,
						y = -132010.77636887,
						heading = 2.0594885173533,
						category = "Fortifications",
						canCargo = false,
						shape_name = "PalatkaB",
						rate = 50,
						dead = false
					}
				},
				{
					name = "Static FARP Tent-17#00001",
					template = {
						name = "Static FARP Tent-17",
						type = "FARP Tent",
						x = 127093.56699148,
						y = -132024.03230612,
						heading = 2.0245819323134,
						category = "Fortifications",
						canCargo = false,
						shape_name = "PalatkaB",
						rate = 50,
						dead = false
					}
				},
			}
		},
		{
			name = "OBJ-6",
			strand = "STRAND-1",
			completeSound = "",
			borderZones = {
			},
			capZones = {
				"CAP-4",
			},
			nodes = {
				{ name = "NODE-24" },
				{ name = "NODE-25" },
				{ name = "NODE-8" },
			},
			tasks = {
			},
			farps = {
			},
			airbases = {
			},
			carriers = {
			},
			qrfs = {
				{
					name = "QRF-19",
					spawnGroups = {
						{ name = "RED QRF 1" },
						{ name = "RED QRF 2" },
						{ name = "RED QRF 3" },
						{ name = "RED QRF 4" },
						{ name = "RED QRF 5" },
						{ name = "RED QRF 6" },
						{ name = "RED QRF 7" },
						{ name = "RED QRF 8" },
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
				{ name = "RED SAM SA-2 RG 234-3" },
				{ name = "RED SAM SA-2 RG 234-4" },
				{ name = "RED SAM SA-2 RG 234-5" },
				{ name = "RED SAM SA-2 RG 234-6" },
				{ name = "RED SAM SA-8 RG 240-5" },
				{ name = "RED SAM SA-8 RG 240-6" },
				{ name = "RED SAM SA-8 RG 240-7" },
				{ name = "RED SAM SA-6 238-5" },
				{ name = "RED SAM SA-6 238-6" },
				{ name = "RED SAM SA-6 238-7" },
				{ name = "RED AIR DEFENSE BATTERY C RG 246-3" },
				{ name = "RED AIR DEFENSE BATTERY C RG 246-4" },
				{ name = "RED AIR DEFENSE BATTERY C RG 246-5" },
				{ name = "RED AIR DEFENSE BATTERY A 242-3" },
				{ name = "RED AIR DEFENSE BATTERY A 242-4" },
			},
			shipGroups = {
				{ name = "RED RG 8-2 FK-1" },
			},
			staticGroups = {
				{
					name = "Lymington Airwing Warehouse#00001",
					template = {
						name = "Lymington Airwing Warehouse",
						type = ".Ammunition depot",
						x = 139345.40388958,
						y = -90788.699777832,
						heading = 0.2617993877992,
						category = "Warehouses",
						canCargo = false,
						shape_name = "SkladC",
						rate = 100,
						dead = false
					}
				},
				{
					name = "Needs Oar Point Airwing Warehouse#00001",
					template = {
						name = "Needs Oar Point Airwing Warehouse",
						type = ".Ammunition depot",
						x = 140314.3410004,
						y = -85524.362236823,
						heading = 5.8992128717408,
						category = "Warehouses",
						canCargo = false,
						shape_name = "SkladC",
						rate = 100,
						dead = false
					}
				},
				{
					name = "Stoney Cross Airwing Warehouse#00001",
					template = {
						name = "Stoney Cross Airwing Warehouse",
						type = ".Ammunition depot",
						x = 155591.78112467,
						y = -101442.96449276,
						heading = 5.9864793343406,
						category = "Warehouses",
						canCargo = false,
						shape_name = "SkladC",
						rate = 100,
						dead = false
					}
				},
			}
		},
		{
			name = "OBJ-7",
			strand = "STRAND-1",
			completeSound = "",
			borderZones = {
			},
			capZones = {
				"CAP-4",
			},
			nodes = {
				{ name = "NODE-7" },
			},
			tasks = {
			},
			farps = {
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
				{ name = "DW RED GROUND 1-10" },
				{ name = "DW RED GROUND 1-11" },
				{ name = "DW RED GROUND 1-12" },
				{ name = "DW RED GROUND 1-13" },
				{ name = "DW RED GROUND 1-14" },
				{ name = "DW RED GROUND 1-15" },
				{ name = "DW RED GROUND 1-16" },
				{ name = "DW RED GROUND 1-19" },
				{ name = "DW RED GROUND 1-6" },
				{ name = "DW RED GROUND 1-9" },
				{ name = "DW RED GROUND 10-6" },
				{ name = "DW RED GROUND 10-7" },
				{ name = "DWRED GROUND 10-3" },
				{ name = "RED EWR 2-6" },
				{ name = "RED EWR 2-7" },
				{ name = "RED EWR 2-8" },
				{ name = "RED GROUND 1-1" },
				{ name = "RED GROUND 1-10" },
				{ name = "RED GROUND 1-11" },
				{ name = "RED GROUND 1-12" },
				{ name = "RED GROUND 1-13" },
				{ name = "RED GROUND 1-14" },
				{ name = "RED GROUND 1-5" },
				{ name = "RED GROUND 1-7" },
				{ name = "RED GROUND 1-8" },
				{ name = "RED GROUND 1-9" },
				{ name = "RED SAM Rapier DW 3-2" },
				{ name = "RED SAM Rapier DW 3-3" },
				{ name = "RED SAM Roland DW" },
			},
			shipGroups = {
				{ name = "Naval-3" },
				{ name = "Naval-4" },
			},
			staticGroups = {
				{
					name = "Static Bunker 1-1#00001",
					template = {
						name = "Static Bunker 1-1",
						type = "Sandbox",
						x = 138359.10618532,
						y = -127730.87990104,
						heading = 3.8222710618676,
						category = "Fortifications",
						canCargo = false,
						shape_name = "",
						rate = 5,
						dead = false
					}
				},
				{
					name = "Static Bunker 1-2#00001",
					template = {
						name = "Static Bunker 1-2",
						type = "Sandbox",
						x = 137151.65625846,
						y = -118755.04863081,
						heading = 3.4033920413889,
						category = "Fortifications",
						canCargo = false,
						shape_name = "",
						rate = 5,
						dead = false
					}
				},
				{
					name = "Static Bunker 1-3#00001",
					template = {
						name = "Static Bunker 1-3",
						type = "Sandbox",
						x = 141091.98377319,
						y = -108870.33616842,
						heading = 3.7699111843078,
						category = "Fortifications",
						canCargo = false,
						shape_name = "",
						rate = 5,
						dead = false
					}
				},
				{
					name = "Static Bunker 1-4#00001",
					template = {
						name = "Static Bunker 1-4",
						type = "Sandbox",
						x = 139692.42604539,
						y = -108410.80703919,
						heading = 4.6774823953448,
						category = "Fortifications",
						canCargo = false,
						shape_name = "",
						rate = 5,
						dead = false
					}
				},
				{
					name = "Static Coach Platform-1#00001",
					template = {
						name = "Static Coach Platform-1",
						type = "Coach a platform",
						x = 135460.82906206,
						y = -124991.1729347,
						heading = 1.4835298641952,
						category = "",
						canCargo = false,
						shape_name = "",
						rate = 4,
						dead = false
					}
				},
				{
					name = "Static Coach Platform-2#00001",
					template = {
						name = "Static Coach Platform-2",
						type = "Coach a platform",
						x = 135462.04815532,
						y = -124976.77825659,
						heading = 1.4835298641952,
						category = "",
						canCargo = false,
						shape_name = "",
						rate = 4,
						dead = false
					}
				},
				{
					name = "Static Coach Platform-3#00001",
					template = {
						name = "Static Coach Platform-3",
						type = "Coach a platform",
						x = 135463.16493837,
						y = -124962.78020704,
						heading = 1.4835298641952,
						category = "",
						canCargo = false,
						shape_name = "",
						rate = 4,
						dead = false
					}
				},
				{
					name = "Static Flatcar-1#00001",
					template = {
						name = "Static Flatcar-1",
						type = "Boxcartrinity",
						x = 135449.06012328,
						y = -125096.24939608,
						heading = 1.4660765716752,
						category = "",
						canCargo = false,
						shape_name = "",
						rate = 4,
						dead = false
					}
				},
				{
					name = "Static Flatcar-2#00001",
					template = {
						name = "Static Flatcar-2",
						type = "Boxcartrinity",
						x = 135447.09081878,
						y = -125112.84781969,
						heading = 1.4660765716752,
						category = "",
						canCargo = false,
						shape_name = "",
						rate = 4,
						dead = false
					}
				},
				{
					name = "Static Flatcar-3#00001",
					template = {
						name = "Static Flatcar-3",
						type = "Boxcartrinity",
						x = 135444.88707327,
						y = -125129.1649141,
						heading = 1.4311699866353,
						category = "",
						canCargo = false,
						shape_name = "",
						rate = 4,
						dead = false
					}
				},
				{
					name = "Static Freight Van-1#00001",
					template = {
						name = "Static Freight Van-1",
						type = "Coach cargo",
						x = 135442.68332777,
						y = -125144.59113266,
						heading = 1.4311699866353,
						category = "",
						canCargo = false,
						shape_name = "",
						rate = 4,
						dead = false
					}
				},
				{
					name = "Static Freight Van-2#00001",
					template = {
						name = "Static Freight Van-2",
						type = "Coach cargo",
						x = 135440.33891765,
						y = -125159.50158099,
						heading = 1.4311699866353,
						category = "",
						canCargo = false,
						shape_name = "",
						rate = 4,
						dead = false
					}
				},
				{
					name = "Static Loco ES44AH-1#00001",
					template = {
						name = "Static Loco ES44AH-1",
						type = "ES44AH",
						x = 135464.48309296,
						y = -124944.55528693,
						heading = 1.5184364492351,
						category = "",
						canCargo = false,
						shape_name = "",
						rate = 10,
						dead = false
					}
				},
				{
					name = "Static Loco ES44AH-2#00001",
					template = {
						name = "Static Loco ES44AH-2",
						type = "ES44AH",
						x = 135437.85384293,
						y = -125178.0224209,
						heading = 4.5902159327451,
						category = "",
						canCargo = false,
						shape_name = "",
						rate = 10,
						dead = false
					}
				},
				{
					name = "Static Tank Car blue-3#00001",
					template = {
						name = "Static Tank Car blue-3",
						type = "Coach a tank blue",
						x = 135452.06096823,
						y = -125071.16420784,
						heading = 1.4835298641952,
						category = "",
						canCargo = false,
						shape_name = "",
						rate = 4,
						dead = false
					}
				},
				{
					name = "Static Tank Car blue-4#00001",
					template = {
						name = "Static Tank Car blue-4",
						type = "Coach a tank blue",
						x = 135450.60743396,
						y = -125082.558041,
						heading = 1.4486232791553,
						category = "",
						canCargo = false,
						shape_name = "",
						rate = 4,
						dead = false
					}
				},
				{
					name = "Static Well Car-1#00001",
					template = {
						name = "Static Well Car-1",
						type = "Wellcarnsc",
						x = 135456.84356486,
						y = -125031.96567071,
						heading = 1.4660765716752,
						category = "",
						canCargo = false,
						shape_name = "",
						rate = 4,
						dead = false
					}
				},
				{
					name = "Static Well Car-2#00001",
					template = {
						name = "Static Well Car-2",
						type = "Wellcarnsc",
						x = 135459.18797498,
						y = -125009.5062218,
						heading = 1.4835298641952,
						category = "",
						canCargo = false,
						shape_name = "",
						rate = 4,
						dead = false
					}
				},
				{
					name = "Static Tank Car blue-1#00001",
					template = {
						name = "Static Tank Car blue-1",
						type = "Coach a tank blue",
						x = 135454.78048396,
						y = -125048.89231174,
						heading = 1.4835298641952,
						category = "",
						canCargo = false,
						shape_name = "",
						rate = 4,
						dead = false
					}
				},
				{
					name = "Static Tank Car blue-2#00001",
					template = {
						name = "Static Tank Car blue-2",
						type = "Coach a tank blue",
						x = 135453.37383789,
						y = -125060.00481569,
						heading = 1.4311699866353,
						category = "",
						canCargo = false,
						shape_name = "",
						rate = 4,
						dead = false
					}
				},
			}
		},
		{
			name = "OBJ-8",
			strand = "STRAND-1",
			completeSound = "",
			borderZones = {
			},
			capZones = {
			},
			nodes = {
				{ name = "NODE-21" },
				{ name = "NODE-22" },
				{ name = "NODE-23" },
				{ name = "NODE-9" },
			},
			tasks = {
			},
			farps = {
			},
			airbases = {
				{
					name = "AIRBASE-1",
					vehicleGroups = {
						{ name = "FARP MASH 1-6" },
						{ name = "FARP MASH 1-7" },
						{ name = "FARP MASH 1-8" },
						{ name = "FARP MASH 1-9" },
					},
					shipGroups = {
					},
					staticGroups = {
					},
					clients = {
							"Needs Oar Point A-10A Cold 1",
							"Needs Oar Point A-10A Cold 2",
							"Needs Oar Point C-101CC Warm 1",
							"Needs Oar Point C-101CC Warm 2",
							"Needs Oar Point F-5E-3 Warm 1",
							"Needs Oar Point F-5E-3 Warm 2",
							"Needs Oar Point F-86F Sabre Warm 1",
							"Needs Oar Point F-86F Sabre Warm 2",
							"Needs Oar Point L-39ZA Warm 1",
							"Needs Oar Point L-39ZA Warm 2",
							"Needs Oar Point MB-339A Warm 1",
							"Needs Oar Point MB-339A Warm 2",
							"Needs Oar Point MiG-19P Warm 1",
							"Needs Oar Point MiG-19P Warm 2",
							"Needs Oar Point P-51D-30-NA Warm 1",
							"Needs Oar Point P-51D-30-NA Warm 2",
							"Needs Oar Point F-15C Cold 1",
							"Needs Oar Point F-15C Cold 2",
							"Needs Oar Point Su-25 Cold 1",
							"Needs Oar Point Su-25 Cold 2",
					}
				},
				{
					name = "AIRBASE-3",
					vehicleGroups = {
						{ name = "FARP MASH 1-10" },
						{ name = "FARP MASH 1-11" },
						{ name = "FARP MASH 1-12" },
						{ name = "FARP MASH 1-13" },
					},
					shipGroups = {
					},
					staticGroups = {
					},
					clients = {
							"Stoney Cross A-10C_2 Warm 1",
							"Stoney Cross A-10C_2 Warm 2",
							"Stoney Cross A-10C_2 Warm 3",
							"Stoney Cross A-10C_2 Warm 4",
							"Stoney Cross AJS37 Warm 1",
							"Stoney Cross AJS37 Warm 2",
							"Stoney Cross AV8BNA Warm 1",
							"Stoney Cross AV8BNA Warm 2",
							"Stoney Cross F-14B Warm 1",
							"Stoney Cross F-14B Warm 2",
							"Stoney Cross F-14B Warm 3",
							"Stoney Cross F-14B Warm 4",
							"Stoney Cross F-15ESE Warm 1",
							"Stoney Cross F-15ESE Warm 2",
							"Stoney Cross F-15ESE Warm 3",
							"Stoney Cross F-15ESE Warm 4",
							"Stoney Cross F-16C_50 Warm 1",
							"Stoney Cross F-16C_50 Warm 2",
							"Stoney Cross F-16C_50 Warm 3",
							"Stoney Cross F-16C_50 Warm 4",
							"Stoney Cross FA-18C_hornet Warm 1",
							"Stoney Cross FA-18C_hornet Warm 2",
							"Stoney Cross FA-18C_hornet Warm 3",
							"Stoney Cross FA-18C_hornet Warm 4",
							"Stoney Cross JF-17 Warm 1",
							"Stoney Cross JF-17 Warm 2",
							"Stoney Cross JF-17 Warm 3",
							"Stoney Cross JF-17 Warm 4",
							"Stoney Cross M-2000C Warm 1",
							"Stoney Cross M-2000C Warm 2",
							"Stoney Cross MiG-21Bis Warm 1",
							"Stoney Cross MiG-21Bis Warm 2",
							"Stoney Cross Mirage-F1EE Warm 1",
							"Stoney Cross Mirage-F1EE Warm 2",
							"Stoney Cross Su-25T Warm 1",
							"Stoney Cross Su-25T Warm 2",
							"Stoney Cross Su-25T Warm 3",
							"Stoney Cross Su-25T Warm 4",
					}
				},
				{
					name = "AIRBASE-4",
					vehicleGroups = {
						{ name = "FARP MASH 1" },
						{ name = "FARP MASH 1-3" },
						{ name = "FARP MASH 1-4" },
						{ name = "FARP MASH 1-5" },
					},
					shipGroups = {
					},
					staticGroups = {
					},
					clients = {
							"Lymington AH-64D_BLK_II Warm 1",
							"Lymington AH-64D_BLK_II Warm 2",
							"Lymington AH-64D_BLK_II Warm 3",
							"Lymington AH-64D_BLK_II Warm 4",
							"Lymington Ka-50_3 Warm 1",
							"Lymington Ka-50_3 Warm 2",
							"Lymington Ka-50_3 Warm 3",
							"Lymington Ka-50_3 Warm 4",
							"Lymington Mi-24P Warm 1",
							"Lymington Mi-24P Warm 2",
							"Lymington Mi-24P Warm 3",
							"Lymington Mi-24P Warm 4",
							"Lymington Mi-8MT Warm 1",
							"Lymington Mi-8MT Warm 2",
							"Lymington Mi-8MT Warm 3",
							"Lymington Mi-8MT Warm 4",
							"Lymington SA342L Warm 1",
							"Lymington SA342L Warm 2",
							"Lymington SA342L Warm 3",
							"Lymington SA342L Warm 4",
							"Lymington SA342M Warm 1",
							"Lymington SA342M Warm 2",
							"Lymington SA342M Warm 3",
							"Lymington SA342M Warm 4",
							"Lymington UH-1H Warm 1",
							"Lymington UH-1H Warm 2",
							"Lymington UH-1H Warm 3",
							"Lymington UH-1H Warm 4",
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
				{ name = "RED EWR 8-1 FK" },
				{ name = "RED EWR 8-2 FK" },
				{ name = "RED EWR 8-3 FK" },
				{ name = "RED EWR 8-4 FK" },
				{ name = "RED GROUND 8-1 FK" },
				{ name = "RED GROUND 8-10 FK" },
				{ name = "RED GROUND 8-11 FK" },
				{ name = "RED GROUND 8-12 FK" },
				{ name = "RED GROUND 8-13 FK" },
				{ name = "RED GROUND 8-14 FK" },
				{ name = "RED GROUND 8-15 FK" },
				{ name = "RED GROUND 8-16 FK" },
				{ name = "RED GROUND 8-17 FK" },
				{ name = "RED GROUND 8-18 FK" },
				{ name = "RED GROUND 8-19 FK" },
				{ name = "RED GROUND 8-2 FK" },
				{ name = "RED GROUND 8-20 FK" },
				{ name = "RED GROUND 8-21 FK" },
				{ name = "RED GROUND 8-22 FK" },
				{ name = "RED GROUND 8-23 FK" },
				{ name = "RED GROUND 8-24 FK" },
				{ name = "RED GROUND 8-25 FK" },
				{ name = "RED GROUND 8-26 FK" },
				{ name = "RED GROUND 8-27 FK" },
				{ name = "RED GROUND 8-28 FK" },
				{ name = "RED GROUND 8-29 FK" },
				{ name = "RED GROUND 8-3 FK" },
				{ name = "RED GROUND 8-4 FK" },
				{ name = "RED GROUND 8-5 FK" },
				{ name = "RED GROUND 8-6 FK" },
				{ name = "RED GROUND 8-7 FK" },
				{ name = "RED GROUND 8-8 FK" },
				{ name = "RED GROUND 8-9 FK" },
				{ name = "RED GROUND 9-8 FK" },
				{ name = "RED SA-8 8-1 FK" },
				{ name = "RED SAM SA-3 8-1 FK" },
				{ name = "RED SAM SA-3 8-2 FK" },
				{ name = "RED SAM SA-3 8-3 FK" },
				{ name = "RED SAM SA-5 8-1 FK" },
				{ name = "RED SAM SA-9 8-1 FK" },
			},
			shipGroups = {
				{ name = "RED RG 8-1 FK" },
				{ name = "RED RG 8-2 FK" },
				{ name = "RED RG 8-3 FK" },
				{ name = "RED RG 8-4 FK" },
				{ name = "RED RG 8-5 FK" },
				{ name = "RED RG 8-6 FK" },
			},
			staticGroups = {
			}
		},
	},
	strands = {
		{
			name = "STRAND-1",
			sequence = {
				"OBJ-2",
				"OBJ-3",
				"OBJ-4",
				"OBJ-5",
				"OBJ-7",
				"OBJ-6",
				"OBJ-8",
				},
			},
		{
			name = "STRAND-3",
			sequence = {
				"OBJ-1",
				},
			},
	},
	ctld = {
		groups = {
			"Tarawa Mi-24P Warm 1",
			"Tarawa Mi-24P Warm 2",
			"Tarawa Mi-24P Warm 3",
			"Tarawa Mi-8MT Warm 1",
			"Tarawa Mi-8MT Warm 2",
			"Tarawa Mi-8MT Warm 3",
			"Tarawa SA342L Warm 1",
			"Tarawa SA342M Warm 1",
			"Peleliu UH-1H Warm 1",
			"Peleliu UH-1H Warm 2",
			"Peleliu UH-1H Warm 3",
			"Peleliu AH-64D_BLK_II Warm 1",
			"Peleliu AH-64D_BLK_II Warm 2",
			"Peleliu AH-64D_BLK_II Warm 3",
			"Peleliu Ka-50_3 Warm 1",
			"Peleliu Ka-50_3 Warm 2",
			"FARP Portland Bill Mi-24P Warm 1",
			"FARP Portland Bill Mi-24P Warm 2",
			"FARP Portland Bill Mi-24P Warm 3",
			"FARP Portland Bill Mi-24P Warm 4",
			"FARP Portland Bill Mi-8MT Warm 1",
			"FARP Portland Bill Mi-8MT Warm 2",
			"FARP Portland Bill Mi-8MT Warm 3",
			"FARP Portland Bill Mi-8MT Warm 4",
			"FARP Portland Bill UH-1H Warm 1",
			"FARP Portland Bill UH-1H Warm 2",
			"FARP Portland Bill UH-1H Warm 3",
			"FARP Portland Bill UH-1H Warm 4",
			"FARP Portland Bill AH-64D_BLK_II Warm 1",
			"FARP Portland Bill AH-64D_BLK_II Warm 2",
			"FARP Portland Bill AH-64D_BLK_II Warm 3",
			"FARP Portland Bill AH-64D_BLK_II Warm 4",
			"FARP Portland Bill SA342L Warm 1",
			"FARP Portland Bill SA342M Warm 1",
			"FARP Portland Bill Ka-50_3 Warm 1",
			"FARP Portland Bill Ka-50_3 Warm 2",
			"FARP Morden Bog Mi-24P Warm 1",
			"FARP Morden Bog Mi-24P Warm 2",
			"FARP Morden Bog Mi-24P Warm 3",
			"FARP Morden Bog Mi-24P Warm 4",
			"FARP Morden Bog Mi-8MT Warm 1",
			"FARP Morden Bog Mi-8MT Warm 2",
			"FARP Morden Bog Mi-8MT Warm 3",
			"FARP Morden Bog Mi-8MT Warm 4",
			"FARP Morden Bog UH-1H Warm 1",
			"FARP Morden Bog UH-1H Warm 2",
			"FARP Morden Bog UH-1H Warm 3",
			"FARP Morden Bog UH-1H Warm 4",
			"FARP Morden Bog AH-64D_BLK_II Warm 1",
			"FARP Morden Bog AH-64D_BLK_II Warm 2",
			"FARP Morden Bog AH-64D_BLK_II Warm 3",
			"FARP Morden Bog AH-64D_BLK_II Warm 4",
			"FARP Morden Bog SA342L Warm 1",
			"FARP Morden Bog SA342M Warm 1",
			"FARP Morden Bog Ka-50_3 Warm 1",
			"FARP Morden Bog Ka-50_3 Warm 2",
			"Lymington AH-64D_BLK_II Warm 1",
			"Lymington AH-64D_BLK_II Warm 2",
			"Lymington AH-64D_BLK_II Warm 3",
			"Lymington AH-64D_BLK_II Warm 4",
			"Lymington Ka-50_3 Warm 1",
			"Lymington Ka-50_3 Warm 2",
			"Lymington Ka-50_3 Warm 3",
			"Lymington Ka-50_3 Warm 4",
			"Lymington Mi-24P Warm 1",
			"Lymington Mi-24P Warm 2",
			"Lymington Mi-24P Warm 3",
			"Lymington Mi-24P Warm 4",
			"Lymington Mi-8MT Warm 1",
			"Lymington Mi-8MT Warm 2",
			"Lymington Mi-8MT Warm 3",
			"Lymington Mi-8MT Warm 4",
			"Lymington SA342L Warm 1",
			"Lymington SA342L Warm 2",
			"Lymington SA342L Warm 3",
			"Lymington SA342L Warm 4",
			"Lymington SA342M Warm 1",
			"Lymington SA342M Warm 2",
			"Lymington SA342M Warm 3",
			"Lymington SA342M Warm 4",
			"Lymington UH-1H Warm 1",
			"Lymington UH-1H Warm 2",
			"Lymington UH-1H Warm 3",
			"Lymington UH-1H Warm 4",
		}
	},
	csar = {
		groups = {
			"Tarawa Mi-24P Warm 1",
			"Tarawa Mi-24P Warm 2",
			"Tarawa Mi-24P Warm 3",
			"Tarawa Mi-8MT Warm 1",
			"Tarawa Mi-8MT Warm 2",
			"Tarawa Mi-8MT Warm 3",
			"Tarawa SA342L Warm 1",
			"Tarawa SA342M Warm 1",
			"Peleliu UH-1H Warm 1",
			"Peleliu UH-1H Warm 2",
			"Peleliu UH-1H Warm 3",
			"Peleliu AH-64D_BLK_II Warm 1",
			"Peleliu AH-64D_BLK_II Warm 2",
			"Peleliu AH-64D_BLK_II Warm 3",
			"Peleliu Ka-50_3 Warm 1",
			"Peleliu Ka-50_3 Warm 2",
			"FARP Portland Bill Mi-24P Warm 1",
			"FARP Portland Bill Mi-24P Warm 2",
			"FARP Portland Bill Mi-24P Warm 3",
			"FARP Portland Bill Mi-24P Warm 4",
			"FARP Portland Bill Mi-8MT Warm 1",
			"FARP Portland Bill Mi-8MT Warm 2",
			"FARP Portland Bill Mi-8MT Warm 3",
			"FARP Portland Bill Mi-8MT Warm 4",
			"FARP Portland Bill UH-1H Warm 1",
			"FARP Portland Bill UH-1H Warm 2",
			"FARP Portland Bill UH-1H Warm 3",
			"FARP Portland Bill UH-1H Warm 4",
			"FARP Portland Bill AH-64D_BLK_II Warm 1",
			"FARP Portland Bill AH-64D_BLK_II Warm 2",
			"FARP Portland Bill AH-64D_BLK_II Warm 3",
			"FARP Portland Bill AH-64D_BLK_II Warm 4",
			"FARP Portland Bill SA342L Warm 1",
			"FARP Portland Bill SA342M Warm 1",
			"FARP Portland Bill Ka-50_3 Warm 1",
			"FARP Portland Bill Ka-50_3 Warm 2",
			"FARP Morden Bog Mi-24P Warm 1",
			"FARP Morden Bog Mi-24P Warm 2",
			"FARP Morden Bog Mi-24P Warm 3",
			"FARP Morden Bog Mi-24P Warm 4",
			"FARP Morden Bog Mi-8MT Warm 1",
			"FARP Morden Bog Mi-8MT Warm 2",
			"FARP Morden Bog Mi-8MT Warm 3",
			"FARP Morden Bog Mi-8MT Warm 4",
			"FARP Morden Bog UH-1H Warm 1",
			"FARP Morden Bog UH-1H Warm 2",
			"FARP Morden Bog UH-1H Warm 3",
			"FARP Morden Bog UH-1H Warm 4",
			"FARP Morden Bog AH-64D_BLK_II Warm 1",
			"FARP Morden Bog AH-64D_BLK_II Warm 2",
			"FARP Morden Bog AH-64D_BLK_II Warm 3",
			"FARP Morden Bog AH-64D_BLK_II Warm 4",
			"FARP Morden Bog SA342L Warm 1",
			"FARP Morden Bog SA342M Warm 1",
			"FARP Morden Bog Ka-50_3 Warm 1",
			"FARP Morden Bog Ka-50_3 Warm 2",
			"Lymington AH-64D_BLK_II Warm 1",
			"Lymington AH-64D_BLK_II Warm 2",
			"Lymington AH-64D_BLK_II Warm 3",
			"Lymington AH-64D_BLK_II Warm 4",
			"Lymington Ka-50_3 Warm 1",
			"Lymington Ka-50_3 Warm 2",
			"Lymington Ka-50_3 Warm 3",
			"Lymington Ka-50_3 Warm 4",
			"Lymington Mi-24P Warm 1",
			"Lymington Mi-24P Warm 2",
			"Lymington Mi-24P Warm 3",
			"Lymington Mi-24P Warm 4",
			"Lymington Mi-8MT Warm 1",
			"Lymington Mi-8MT Warm 2",
			"Lymington Mi-8MT Warm 3",
			"Lymington Mi-8MT Warm 4",
			"Lymington SA342L Warm 1",
			"Lymington SA342L Warm 2",
			"Lymington SA342L Warm 3",
			"Lymington SA342L Warm 4",
			"Lymington SA342M Warm 1",
			"Lymington SA342M Warm 2",
			"Lymington SA342M Warm 3",
			"Lymington SA342M Warm 4",
			"Lymington UH-1H Warm 1",
			"Lymington UH-1H Warm 2",
			"Lymington UH-1H Warm 3",
			"Lymington UH-1H Warm 4",
		}
	},
	autolase = {},
	playerRecce = {},
	strandtasks = {},
	samnetwork = {},
	redchief = {
	    airwings = {
			{
				name = "1st Goon Wing - Evreux",
				warehouse = "Evreux Airwing Warehouse#00001",
				airbase = "Evreux",
				squadrons = {
					{
						name = "1GW-Evreux-1",
						templateGroupName = "RED 1st Goon Wing - Evreux 1GW-Evreux-1 JF-17",
						initialInventory = 2,
						capabilities = {
							{ mission = AUFTRAG.Type.CAP, performance = 50 },
							{ mission = AUFTRAG.Type.INTERCEPT, performance = 50 },
							{ mission = AUFTRAG.Type.ESCORT, performance = 50 },
						},
						livery = "PLAAF 125th AB (Fictional)",
						payloads = {
							{
								templateGroupName = "RED 1st Goon Wing - Evreux 1GW-Evreux-1 JF-17 LOADOUT 0",
								missionTypes = { AUFTRAG.Type.CAP, AUFTRAG.Type.INTERCEPT }
							},
						}
					},
					{
						name = "1GW-Evreux-2",
						templateGroupName = "RED 1st Goon Wing - Evreux 1GW-Evreux-2 A-50",
						initialInventory = 1,
						capabilities = {
							{ mission = AUFTRAG.Type.AWACS, performance = 50 },
						},
						livery = "RF Air Force new",
						payloads = {
							{
								templateGroupName = "RED 1st Goon Wing - Evreux 1GW-Evreux-2 A-50 LOADOUT 0",
								missionTypes = { AUFTRAG.Type.AWACS }
							},
						}
					},
				}
			},
			{
				name = "1st Goon Wing - Funtington",
				warehouse = "Funtington Airwing Warehouse#00001",
				airbase = "Funtington",
				squadrons = {
					{
						name = "1GW-Funtington-1",
						templateGroupName = "RED 1st Goon Wing - Funtington 1GW-Funtington-1 JF-17",
						initialInventory = 2,
						capabilities = {
							{ mission = AUFTRAG.Type.CAP, performance = 50 },
							{ mission = AUFTRAG.Type.INTERCEPT, performance = 50 },
							{ mission = AUFTRAG.Type.ESCORT, performance = 50 },
						},
						livery = "PLAAF 125th AB (Fictional)",
						payloads = {
							{
								templateGroupName = "RED 1st Goon Wing - Funtington 1GW-Funtington-1 JF-17 LOADOUT 0",
								missionTypes = { AUFTRAG.Type.CAP, AUFTRAG.Type.INTERCEPT }
							},
						}
					},
				}
			},
			{
				name = "Stoney Cross",
				warehouse = "Stoney Cross Airwing Warehouse#00001",
				airbase = "Stoney Cross",
				squadrons = {
					{
						name = "Stoney Cross 1",
						templateGroupName = "RED Stoney Cross Stoney Cross 1 JF-17",
						initialInventory = 1,
						capabilities = {
							{ mission = AUFTRAG.Type.CAP, performance = 50 },
							{ mission = AUFTRAG.Type.INTERCEPT, performance = 50 },
							{ mission = AUFTRAG.Type.ESCORT, performance = 50 },
							{ mission = AUFTRAG.Type.BAI, performance = 50 },
							{ mission = AUFTRAG.Type.CAS, performance = 50 },
							{ mission = AUFTRAG.Type.BOMBCARPET, performance = 50 },
							{ mission = AUFTRAG.Type.SEAD, performance = 50 },
							{ mission = AUFTRAG.Type.CASENHANCED, performance = 50 },
						},
						livery = "PLAAF 125th AB (Fictional)",
						payloads = {
							{
								templateGroupName = "RED Stoney Cross Stoney Cross 1 JF-17 LOADOUT 0",
								missionTypes = { AUFTRAG.Type.CAP, AUFTRAG.Type.INTERCEPT, AUFTRAG.Type.ESCORT }
							},
							{
								templateGroupName = "RED Stoney Cross Stoney Cross 1 JF-17 LOADOUT 1",
								missionTypes = { AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.BOMBCARPET, AUFTRAG.Type.CASENHANCED }
							},
							{
								templateGroupName = "RED Stoney Cross Stoney Cross 1 JF-17 LOADOUT 2",
								missionTypes = { AUFTRAG.Type.SEAD }
							},
						}
					},
					{
						name = "Stoney Cross 2",
						templateGroupName = "RED Stoney Cross Stoney Cross 2 F-16C_50",
						initialInventory = 1,
						capabilities = {
							{ mission = AUFTRAG.Type.CAP, performance = 50 },
							{ mission = AUFTRAG.Type.INTERCEPT, performance = 50 },
							{ mission = AUFTRAG.Type.ESCORT, performance = 50 },
							{ mission = AUFTRAG.Type.BAI, performance = 50 },
							{ mission = AUFTRAG.Type.CAS, performance = 50 },
							{ mission = AUFTRAG.Type.BOMBCARPET, performance = 50 },
							{ mission = AUFTRAG.Type.SEAD, performance = 50 },
							{ mission = AUFTRAG.Type.CASENHANCED, performance = 50 },
						},
						livery = "18th AGRS BDU Splinter",
						payloads = {
							{
								templateGroupName = "RED Stoney Cross Stoney Cross 2 F-16C_50 LOADOUT 0",
								missionTypes = { AUFTRAG.Type.CAP, AUFTRAG.Type.INTERCEPT, AUFTRAG.Type.ESCORT }
							},
							{
								templateGroupName = "RED Stoney Cross Stoney Cross 2 F-16C_50 LOADOUT 1",
								missionTypes = { AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.CASENHANCED }
							},
							{
								templateGroupName = "RED Stoney Cross Stoney Cross 2 F-16C_50 LOADOUT 2",
								missionTypes = { AUFTRAG.Type.BOMBCARPET}
							},
							{
								templateGroupName = "RED Stoney Cross Stoney Cross 2 F-16C_50 LOADOUT 3",
								missionTypes = { AUFTRAG.Type.SEAD }
							},
						}
					},
				}
			},
			{
				name = "Lymington",
				warehouse = "Lymington Airwing Warehouse#00001",
				airbase = "Lymington",
				squadrons = {
					{
						name = "Lymington 1",
						templateGroupName = "RED Lymington Lymington 1 F-5E-3",
						initialInventory = 1,
						capabilities = {
							{ mission = AUFTRAG.Type.CAP, performance = 50 },
							{ mission = AUFTRAG.Type.INTERCEPT, performance = 50 },
							{ mission = AUFTRAG.Type.ESCORT, performance = 50 },
							{ mission = AUFTRAG.Type.BAI, performance = 50 },
							{ mission = AUFTRAG.Type.CAS, performance = 50 },
							{ mission = AUFTRAG.Type.BOMBCARPET, performance = 50 },
							{ mission = AUFTRAG.Type.CASENHANCED, performance = 50 },
						},
						livery = "black 'Mig-28'",
						payloads = {
							{
								templateGroupName = "RED Lymington Lymington 1 F-5E-3 LOADOUT 0",
								missionTypes = { AUFTRAG.Type.CAP, AUFTRAG.Type.INTERCEPT, AUFTRAG.Type.ESCORT }
							},
							{
								templateGroupName = "RED Lymington Lymington 1 F-5E-3 LOADOUT 1",
								missionTypes = { AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.BOMBCARPET, AUFTRAG.Type.CASENHANCED }
							},
						}
					},
					{
						name = "Lymington 2",
						templateGroupName = "RED Lymington Lymington 2 MiG-21Bis",
						initialInventory = 1,
						capabilities = {
							{ mission = AUFTRAG.Type.CAP, performance = 50 },
							{ mission = AUFTRAG.Type.INTERCEPT, performance = 50 },
							{ mission = AUFTRAG.Type.ESCORT, performance = 50 },
							{ mission = AUFTRAG.Type.BAI, performance = 50 },
							{ mission = AUFTRAG.Type.CAS, performance = 50 },
							{ mission = AUFTRAG.Type.BOMBCARPET, performance = 50 },
							{ mission = AUFTRAG.Type.CASENHANCED, performance = 50 },
						},
						livery = "Draken International",
						payloads = {
							{
								templateGroupName = "RED Lymington Lymington 2 MiG-21Bis LOADOUT 0",
								missionTypes = { AUFTRAG.Type.CAP, AUFTRAG.Type.INTERCEPT, AUFTRAG.Type.ESCORT }
							},
							{
								templateGroupName = "RED Lymington Lymington 2 MiG-21Bis LOADOUT 1",
								missionTypes = { AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.BOMBCARPET, AUFTRAG.Type.CASENHANCED }
							},
						}
					},
				}
			},
			{
				name = "Needs Oar Point",
				warehouse = "Needs Oar Point Airwing Warehouse#00001",
				airbase = "Needs Oar Point",
				squadrons = {
					{
						name = "Needs Oar Point 1",
						templateGroupName = "RED Needs Oar Point Needs Oar Point 1 Mirage-F1EE",
						initialInventory = 1,
						capabilities = {
							{ mission = AUFTRAG.Type.CAP, performance = 50 },
							{ mission = AUFTRAG.Type.INTERCEPT, performance = 50 },
							{ mission = AUFTRAG.Type.ESCORT, performance = 50 },
							{ mission = AUFTRAG.Type.BAI, performance = 50 },
							{ mission = AUFTRAG.Type.CAS, performance = 50 },
							{ mission = AUFTRAG.Type.BOMBCARPET, performance = 50 },
							{ mission = AUFTRAG.Type.CASENHANCED, performance = 50 },
						},
						livery = "USA Company Skin (M-EE)",
						payloads = {
							{
								templateGroupName = "RED Needs Oar Point Needs Oar Point 1 Mirage-F1EE LOADOUT 0",
								missionTypes = { AUFTRAG.Type.CAP, AUFTRAG.Type.INTERCEPT, AUFTRAG.Type.ESCORT }
							},
							{
								templateGroupName = "RED Needs Oar Point Needs Oar Point 1 Mirage-F1EE LOADOUT 1",
								missionTypes = { AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.BOMBCARPET, AUFTRAG.Type.CASENHANCED }
							},
						}
					},
					{
						name = "Needs Oar Point 2",
						templateGroupName = "RED Needs Oar Point Needs Oar Point 2 Su-25TM",
						initialInventory = 1,
						capabilities = {
							{ mission = AUFTRAG.Type.BAI, performance = 50 },
							{ mission = AUFTRAG.Type.CAS, performance = 50 },
							{ mission = AUFTRAG.Type.BOMBCARPET, performance = 50 },
							{ mission = AUFTRAG.Type.CASENHANCED, performance = 50 },
							{ mission = AUFTRAG.Type.SEAD, performance = 50 },
						},
						livery = "Flight Research Institute  VVS",
						payloads = {
							{
								templateGroupName = "RED Needs Oar Point Needs Oar Point 2 Su-25TM LOADOUT 0",
								missionTypes = { AUFTRAG.Type.SEAD }
							},
							{
								templateGroupName = "RED Needs Oar Point Needs Oar Point 2 Su-25TM LOADOUT 1",
								missionTypes = { AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.CASENHANCED }
							},
							{
								templateGroupName = "RED Needs Oar Point Needs Oar Point 2 Su-25TM LOADOUT 2",
								missionTypes = { AUFTRAG.Type.BOMBCARPET }
							},
						}
					},
				}
			},
			{
				name = "1st Goon Wing - Anglo",
				warehouse = "Anglo Airwing Warehouse#00001",
				airbase = "Anglo Farp#00001",
				squadrons = {
					{
						name = "1GW-Anglo-1",
						templateGroupName = "RED 1st Goon Wing - Anglo 1GW-Anglo-1 Mi-26",
						initialInventory = 99,
						capabilities = {
							{ mission = AUFTRAG.Type.OPSTRANSPORT, performance = 50 },
						},
						livery = "Russia_VVS_Grey",
						payloads = {
							{
								templateGroupName = "RED 1st Goon Wing - Anglo 1GW-Anglo-1 Mi-26 LOADOUT 0",
								missionTypes = { AUFTRAG.Type.OPSTRANSPORT }
							},
						}
					},
					{
						name = "1GW-Anglo-2",
						templateGroupName = "RED 1st Goon Wing - Anglo 1GW-Anglo-2 Mi-24P",
						initialInventory = 1,
						capabilities = {
							{ mission = AUFTRAG.Type.BAI, performance = 50 },
							{ mission = AUFTRAG.Type.CAS, performance = 50 },
							{ mission = AUFTRAG.Type.CASENHANCED, performance = 50 },
						},
						livery = "Russian Air Force",
						payloads = {
							{
								templateGroupName = "RED 1st Goon Wing - Anglo 1GW-Anglo-2 Mi-24P LOADOUT 0",
								missionTypes = { AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.CASENHANCED }
							},
						}
					},
				}
			},
			{
				name = "FOB Yes Minister",
				warehouse = "FOB Yes Minister Airwing Warehouse#00001",
				airbase = "FOB Yes Minister Farp#00001",
				squadrons = {
					{
						name = "Yes Minister 1",
						templateGroupName = "RED FOB Yes Minister Yes Minister 1 Mi-26",
						initialInventory = 99,
						capabilities = {
							{ mission = AUFTRAG.Type.OPSTRANSPORT, performance = 50 },
						},
						livery = "Russia_VVS_Grey",
						payloads = {
							{
								templateGroupName = "RED FOB Yes Minister Yes Minister 1 Mi-26 LOADOUT 0",
								missionTypes = { AUFTRAG.Type.OPSTRANSPORT }
							},
						}
					},
					{
						name = "Yes Minister 2",
						templateGroupName = "RED FOB Yes Minister Yes Minister 2 Mi-24P",
						initialInventory = 1,
						capabilities = {
							{ mission = AUFTRAG.Type.BAI, performance = 50 },
							{ mission = AUFTRAG.Type.CAS, performance = 50 },
							{ mission = AUFTRAG.Type.CASENHANCED, performance = 50 },
						},
						livery = "Russian Air Force",
						payloads = {
							{
								templateGroupName = "RED FOB Yes Minister Yes Minister 2 Mi-24P LOADOUT 0",
								missionTypes = { AUFTRAG.Type.BAI, AUFTRAG.Type.CAS, AUFTRAG.Type.CASENHANCED }
							},
						}
					},
				}
			},
		},
		brigades = {
			{
				name = "1st Anglo",
				warehouse = "Anglo Brigade Warehouse#00001",
				platoons = {
					{
						name = "1GW-Anglo-2",
						templateGroupName = "RED 1st Anglo 1GW-Anglo-2",
						initialInventory = 3,
						capabilities = {
							{ mission = AUFTRAG.Type.ONGUARD, performance = 50 },
						},
					},
					{
						name = "1GW-Anglo-3",
						templateGroupName = "RED 1st Anglo 1GW-Anglo-3",
						initialInventory = 1,
						capabilities = {
							{ mission = AUFTRAG.Type.ARTY, performance = 50 },
						},
					},
				}
			},
			{
				name = "FOB Yes Minister",
				warehouse = "FOB Yes Minister Brigade Warehouse#00001",
				platoons = {
					{
						name = "FOB Yes Minister 1",
						templateGroupName = "RED FOB Yes Minister FOB Yes Minister 1",
						initialInventory = 3,
						capabilities = {
							{ mission = AUFTRAG.Type.ONGUARD, performance = 50 },
						},
					},
					{
						name = "FOB Yes Minister 2",
						templateGroupName = "RED FOB Yes Minister FOB Yes Minister 2",
						initialInventory = 1,
						capabilities = {
							{ mission = AUFTRAG.Type.ARTY, performance = 50 },
						},
					},
				}
			},
		}
	},
	bluechief = {
	    airwings = {
			{
				name = "1st CAW - Teddy",
				warehouse = "Teddy Unit #1",
				airbase = "Teddy",
				squadrons = {
					{
						name = "GGD-01",
						templateGroupName = "BLUE 1st CAW - Teddy GGD-01 E-2C",
						initialInventory = 99,
						capabilities = {
							{ mission = AUFTRAG.Type.AWACS, performance = 50 },
						},
						livery = "VAW-125 Tigertails",
						payloads = {
							{
								templateGroupName = "BLUE 1st CAW - Teddy GGD-01 E-2C LOADOUT 0",
								missionTypes = { AUFTRAG.Type.AWACS }
							},
						}
					},
					{
						name = "GGD-02 JTAC",
						templateGroupName = "BLUE 1st CAW - Teddy GGD-02 JTAC S-3B",
						initialInventory = 99,
						capabilities = {
							{ mission = AUFTRAG.Type.RECON, performance = 50 },
						},
						livery = "usaf standard",
						payloads = {
							{
								templateGroupName = "BLUE 1st CAW - Teddy GGD-02 JTAC S-3B LOADOUT 0",
								missionTypes = { AUFTRAG.Type.RECON }
							},
						}
					},
					{
						name = "GGD-02",
						templateGroupName = "BLUE 1st CAW - Teddy GGD-02 CH-47D",
						initialInventory = 99,
						capabilities = {
							{ mission = AUFTRAG.Type.OPSTRANSPORT, performance = 50 },
						},
						livery = "standard",
						payloads = {
							{
								templateGroupName = "BLUE 1st CAW - Teddy GGD-02 CH-47D LOADOUT 0",
								missionTypes = { AUFTRAG.Type.OPSTRANSPORT }
							},
						}
					},
				}
			},
			{
				name = "2nd CAW - Teddy",
				warehouse = "Teddy Unit #1",
				airbase = "Teddy",
				squadrons = {
					{
						name = "GGD-03",
						templateGroupName = "BLUE 2nd CAW - Teddy GGD-03 FA-18C_hornet",
						initialInventory = 99,
						capabilities = {
							{ mission = AUFTRAG.Type.CAP, performance = 50 },
						},
						livery = "Canada 150 Demo Jet",
						payloads = {
							{
								templateGroupName = "BLUE 2nd CAW - Teddy GGD-03 FA-18C_hornet LOADOUT 0",
								missionTypes = { AUFTRAG.Type.CAP }
							},
						}
					},
				}
			},
		},
		brigades = {
			{
				name = "1st Teddy",
				warehouse = "Teddy Unit #1",
				platoons = {
					{
						name = "Teddy-01",
						templateGroupName = "BLUE 1st Teddy Teddy-01",
						initialInventory = 99,
						capabilities = {
							{ mission = AUFTRAG.Type.ONGUARD, performance = 50 },
						},
					},
				}
			},
		}
	},
	units = {},
	industry = {
		percentage = 100,
		active = 0
	},
	devmode = true,
	lateActivateStatics = false,
	enableConvoys = true,
	missionName = "DangerZone",
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
	}
}