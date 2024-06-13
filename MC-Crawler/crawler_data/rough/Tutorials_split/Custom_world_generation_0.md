# Tutorials/Custom world generation
Custom world generation is very complex and difficult for most data pack or mod creators. To create a more complete world, it is necessary to refer to how the world is generated in the vanilla version.

This tutorial roughly explains some of the vanilla world generation files in 1.20.1, making it easy for creators to read and understand the vanilla world generation.

## Contents
- 1 How to obtain vanilla world generation files
- 2 Final density function of the overworld
- 3 Surface rules of the overworld
	- 3.1 Notes
		- 3.1.1 Basin
		- 3.1.2 Carver
- 4 Biome source parameter list presets
- 5 See also

## How to obtain vanilla world generation files
After 22w42a, most of world generation files can be found in the data/minecraft/worldgen directory in client.jar or server.jar. However, multi-noise biome source parameter list files do not contain details of biome parameter list presets of the vanilla overworld and nether.

Through running the data generator, you can directly generate all vanilla data pack files, as well as biome source parameter list presets of the overworld and the nether.

The vanilla world generation files before 22w42a can be obtained on Slicedlime's github, located at examples repository. Missing versions in the repository commit history mean that the world generation files have not changed in these versions.

## Final density function of the overworld
Final density function of the overworld is the final_density field in worldgen/noise_settings/overworld.json.

{  //Final density function of the overworld
"type": "minecraft:min",
"argument1":
{  //Brings its value closer to 0, which affects the generation of barriers between different liquid bodies in the aquifer. The smaller the negative value of final_density, the less likely it is to generate barriers

"type": "minecraft:squeeze",
"argument": {
"type": "minecraft:mul",
"argument1": 0.64,
"argument2":
{  //Interpolating

"type": "minecraft:interpolated",
"argument":
{  //Transition to legacy 256-block-high chunks generated in old versions

"type": "minecraft:blend_density",
"argument":
{  //From Y=-40 to Y=-64, the density function value gradually changes to a fixed value of 0.1171875 to avoid too deep caves that expose or even penetrate the bedrock layer

"type": "minecraft:add",
"argument1": 0.1171875,
"argument2": {
"type": "minecraft:mul",
"argument1": {
"type": "minecraft:y_clamped_gradient",
"from_y": -64,
"to_y": -40,
"from_value": 0,
"to_value": 1
},
"argument2": {
"type": "minecraft:add",
"argument1": -0.1171875,
"argument2":
{  //From Y=-40 to Y=-64, the density function value gradually changes to a fixed value of -0.078125 to avoid too high terrain

"type": "minecraft:add",
"argument1": -0.078125,
"argument2": {
"type": "minecraft:mul",
"argument1": {
"type": "minecraft:y_clamped_gradient",
"from_y": 240,
"to_y": 256,
"from_value": 1,
"to_value": 0
},
"argument2": {
"type": "minecraft:add",
"argument1": 0.078125,
"argument2":
{  //Using sloped_cheese's 1.5625 as the boundary, divides the world into surface and underground parts

"type": "minecraft:range_choice",
"input": "minecraft:overworld/sloped_cheese",
"min_inclusive": -1000000,
"max_exclusive": 1.5625,
"when_in_range":
{  //Surface part

"type": "minecraft:min",
"argument1": "minecraft:overworld/sloped_cheese",  //Determines the height and shape of the surface terrain
"argument2":
{  //Noise cave entrances, i.e., some caves that connect the surface and underground caves

"type": "minecraft:mul",
"argument1": 5,
"argument2": "minecraft:overworld/caves/entrances"
}

},
"when_out_of_range":
{  //Underground part

"type": "minecraft:max",
"argument1":
{  //Spaghetti, cheese caves, and cave entrances. Takes the minimum value of the three. It is necessary to call the cave entrance again here, otherwise the cave entrance would only be generated in the surface part and cut off at the underground part

"type": "minecraft:min",
"argument1":
{  //Cheese caves and cave entrances

"type": "minecraft:min",
"argument1":
{  //Cheese caves

"type": "minecraft:add",
"argument1":
{  //Make caves smaller and more irregular in shape. The value of this field is always positive

"type": "minecraft:mul",
"argument1": 4,
"argument2": {
"type": "minecraft:square",
"argument": {
"type": "minecraft:noise",
"noise": "minecraft:cave_layer",
"xz_scale": 1,
"y_scale": 8
}
}

},
"argument2":
{

"type": "minecraft:add",
"argument1":
{  //Cheese caves. Cheese caves generate only at places where this field is less than zero

"type": "minecraft:clamp",
"input": {
"type": "minecraft:add",
"argument1": 0.27,
"argument2": {
"type": "minecraft:noise",
"noise": "minecraft:cave_cheese",
"xz_scale": 1,
"y_scale": 0.6666666666666666
}
},
"min": -1,
"max": 1

},
"argument2":
{  //Increases density near the surface to reduce the generation of cheese caves near the surface. This field is 0 when the value of slope_cheese is greater than 2.34375, gradually increasing to 0.5 until the slope_cheese reaches 1.5625

"type": "minecraft:clamp",
"input": {
"type": "minecraft:add",
"argument1": 1.5,
"argument2": {
"type": "minecraft:mul",
"argument1": -0.64,
"argument2": "minecraft:overworld/sloped_cheese"
}
},
"min": 0,
"max": 0.5

}

}

},
"argument2": "minecraft:overworld/caves/entrances"  //Cave entrances

},
"argument2":
{  //Spaghetti caves

"type": "minecraft:add",
"argument1": "minecraft:overworld/caves/spaghetti_2d",
"argument2": "minecraft:overworld/caves/spaghetti_roughness_function"
}

},
"argument2":
{  //Noise pillars in noise caves

"type": "minecraft:range_choice",
"input": "minecraft:overworld/caves/pillars",
"min_inclusive": -1000000,
"max_exclusive": 0.03,
"when_in_range": -1000000,
"when_out_of_range": "minecraft:overworld/caves/pillars"
}

}

}
}
}

}
}
}

}

}

}
}
},
"argument2": "minecraft:overworld/caves/noodle"  //Noodle caves
}

In which, the sloped_cheese used to determine the height and shape of the surface terrain is located in data/minecraft/worldgen/density_function/overworld/sloped_cheese.json.

{  //sloped_cheese
"type": "minecraft:add",
"argument1":
{  //Multiplies the factor minecraft:overworld/factor to determine the distribution of 3D terrain. Then multiplies positive values by 4 to avoid deep underground region being affected by base_3d_noise

"type": "minecraft:mul",
"argument1": 4.0,
"argument2": {
"type": "minecraft:quarter_negative",
"argument": {
"type": "minecraft:mul",
"argument1":
{

"type": "minecraft:add",
"argument1": "minecraft:overworld/depth",  //Determines the height of the surface terrain in general, with negative values above the surface and positive values below the surface
"argument2":
{  //Increases or decreases density in high mountainous areas to obtain jagged small peaks. This field is a two-dimensional density function

"type": "minecraft:mul",
"argument1": "minecraft:overworld/jaggedness",  // Using a spline function, obtains the distribution of mountain ranges based on continentalness, erosion, PV value, and weirdness value. It is 0 in most places, but positive in areas with high continentalness, low erosion, and high PV values, and larger in areas with negative weirdness
"argument2": {  //Noise factor to convert mountain ranges into small peaks
"type": "minecraft:half_negative",
"argument": {
"type": "minecraft:noise",
"noise": "minecraft:jagged",
"xz_scale": 1500.0,
"y_scale": 0.0
}
}

}

},
"argument2": "minecraft:overworld/factor"  //This factor uses spline function to determine the distribution of 3D terrain according to continentalness, erosion, weirdness and PV value. It is always positive. Values are smaller at the positions where windswept savannas or shattered biomes should be generated, and higher at other places to reduce the impact of base_3d_noise
}
}

},
"argument2": "minecraft:overworld/base_3d_noise"  //A 3D noise used to create 3D surface terrain shape
}
In which, the depth to determine the height of general surface terrain is located in data/minecraft/worldgen/density_function/overworld/depth.json.

{  //depth
"type": "minecraft:add",
"argument1":
{  //For each block down, the depth decreases by 1⁄128 (0.0078125), and it is 0 at Y=128

"type": "minecraft:y_clamped_gradient",
"from_value": 1.5,
"from_y": -64,
"to_value": -1.5,
"to_y": 320

},
"argument2": "minecraft:overworld/offset"  //The terrain height offset using a spline function based on continentalness, erosion, and PV values
}
