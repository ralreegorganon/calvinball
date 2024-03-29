-- Label parameters
-- Copyright (C) 2018, Eagle Dynamics.



-- labels =  0  -- NONE
-- labels =  1  -- FULL
-- labels =  2  -- ABBREVIATED
-- labels =  3  -- DOT ONLY

-- Off: No labels are used
-- Full: As we have now
-- Abbreviated: Only red or blue dot and unit type name based on side
-- Dot Only: Only red or blue dot based on unit side

AirOn			 		= true
GroundOn 		 		= true
NavyOn		 	 		= true
WeaponOn 		 		= true
labels_format_version 	= 3 -- labels format vesrion
---------------------------------
-- Label text format symbols
-- %N - name of object
-- %D - distance to object
-- %P - pilot name
-- %n - new line 
-- %% - symbol '%'
-- %x, where x is not NDPn% - symbol 'x'
-- %C - extended info for vehicle's and ship's weapon systems
------------------------------------------
-- Example
-- labelFormat[5000] = {"Name: %N%nDistance: %D%n Pilot: %P","LeftBottom",0,0}
-- up to 5km label is:
--       Name: Su-33
--       Distance: 30km
--       Pilot: Pilot1


-- alignment options 
--"RightBottom"
--"LeftTop"
--"RightTop"
--"LeftCenter"
--"RightCenter"
--"CenterBottom"
--"CenterTop"
--"CenterCenter"
--"LeftBottom"

local aircraft_symbol_near  =  "˄" --U+02C4
local aircraft_symbol_far   =  "˄" --U+02C4

local ground_symbol_near    = "ˉ"  --U+02C9
local ground_symbol_far     = "ˉ"  --U+02C9

local navy_symbol_near      = "˜"  --U+02DC
local navy_symbol_far       = "˜"  --U+02DC

local weapon_symbol_near    = "ˈ"  --U+02C8
local weapon_symbol_far     = "ˈ"  --U+02C8

local function dot_symbol(blending,opacity)
    return {"˙","CenterBottom", blending or 1.0 , opacity  or 0.1}
end

local DISTANCE             = "%D"
local NAME 				   = "%n  %N"
local DISTANCE_NAME        = DISTANCE..NAME
local DISTANCE_NAME_PLAYER = DISTANCE_NAME.."%n  %P"
local ABB_NAME 			   = "%N"

-- Text shadow color in {red, green, blue, alpha} format, volume from 0 up to 255
-- alpha will by multiplied by opacity value for corresponding distance
local text_shadow_color = {128, 128, 128, 255}
local text_blur_color 	= {0, 0, 255, 255}

local EMPTY = {"", "LeftBottom", 1, 1, 0, 0}



-- Colors in {red, green, blue} format, volume from 0 up to 255

ColorAliesSide   		= {249, 69,38}
ColorEnemiesSide 		= {0, 82,  199}
ColorUnknown     		= {50, 50, 50} -- will be blend at distance with coalition color

ShadowColorNeutralSide 	= {255,255,255,32}
ShadowColorAliesSide	= {255,255,255,32}
ShadowColorEnemiesSide 	= {255,255,255,32}
ShadowColorUnknown 	= {255,255,255,32}

BlurColorNeutralSide 	= {255,255,255,32}
BlurColorAliesSide	= {255,255,255,32}
BlurColorEnemiesSide	= {255,255,255,32}
BlurColorUnknown	= {255,255,255,32}

local function NEUTRAL_DOT(hundred_percent_dist,five_percent_dist,cutoff_dist)

	local res = {
		[500]	= EMPTY,
	}
	local points = (five_percent_dist - hundred_percent_dist)/2000
	local last_x = 0
	for i = 1,points,1 do 
		last_x 		= hundred_percent_dist + (i - 1) * 2000
		local opacity 	= 0.95 * (1 - math.sqrt(last_x/five_percent_dist)) + 0.05
		res[last_x] 	= {"·","CenterCenter",0,opacity,0,2}
	end
	
	res[last_x + 2000] = EMPTY
	return res
	
end

local baseNeutralDotColor = {0,0,0} 

LEVEL_NEUTRAL_DOT = {
	AirFormat 	 = NEUTRAL_DOT(1000,30000),
	GroundFormat = NEUTRAL_DOT(1000,20000),
	NavyFormat 	 = NEUTRAL_DOT(1000,40000),
	WeaponFormat = NEUTRAL_DOT(1000,20000),
	--------------------------------------------------------
	ColorAliesSide   		= baseNeutralDotColor,
	ColorEnemiesSide 		= baseNeutralDotColor,
	ColorUnknown     		= baseNeutralDotColor,
	--------------------------------------------------
	font_properties 		= {"DejaVuLGCSans.ttf",4},
}

LEVEL_DOT = {
	AirFormat 	 = NEUTRAL_DOT(1000,30000),
	GroundFormat = NEUTRAL_DOT(1000,20000),
	NavyFormat 	 = NEUTRAL_DOT(1000,40000),
	WeaponFormat = NEUTRAL_DOT(1000,20000),
	--------------------------------------------------------
	ColorAliesSide   		= baseNeutralDotColor,
	ColorEnemiesSide 		= baseNeutralDotColor,
	ColorUnknown     		= baseNeutralDotColor,
	--------------------------------------------------
	font_properties 		= {"DejaVuLGCSans.ttf",11},
}

LEVEL_ABBREVIATED = {
	AirFormat 	 = NEUTRAL_DOT(1000,30000),
	GroundFormat = NEUTRAL_DOT(1000,20000),
	NavyFormat 	 = NEUTRAL_DOT(1000,40000),
	WeaponFormat = NEUTRAL_DOT(1000,20000),
	--------------------------------------------------------
	ColorAliesSide   		= baseNeutralDotColor,
	ColorEnemiesSide 		= baseNeutralDotColor,
	ColorUnknown     		= baseNeutralDotColor,
	--------------------------------------------------
	font_properties 		= {"DejaVuLGCSans.ttf",18},
}

LEVEL_FULL = {
	AirFormat 	 = NEUTRAL_DOT(1000,30000),
	GroundFormat = NEUTRAL_DOT(1000,20000),
	NavyFormat 	 = NEUTRAL_DOT(1000,40000),
	WeaponFormat = NEUTRAL_DOT(1000,20000),
	--------------------------------------------------------
	ColorAliesSide   		= baseNeutralDotColor,
	ColorEnemiesSide 		= baseNeutralDotColor,
	ColorUnknown     		= baseNeutralDotColor,
	--------------------------------------------------
	font_properties 		= {"DejaVuLGCSans.ttf",24},
}