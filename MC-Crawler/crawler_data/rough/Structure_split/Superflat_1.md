### Preset code format
The preset code is a string of numbers, semicolons(;), colons(:), commas(,), and asterisks(*). Each code has three main parts, divided by semicolons. They are:

- a list of one or moreblock IDs;
	- The block list is a comma-separated list of block IDs, ordered fromlayer -64 up; if the entry for a given block has an "*", the number before the "*" is the number of layers to be generated, and the string after is the block ID.
	- A block can also be repeated over multiple layers simply by repeating the block's ID, e.g.minecraft:glass,minecraft:glass,minecraft:glass,minecraft:glasswould give the same result as4*minecraft:glass.
- a validbiome ID;
- (optional,not after 1.16) a list offeature generation options.
	- Feature generation options (described below) may have additional parameters, for examplevillage(size=0 distance=9)(in 1.13+ they have no effect).
	- It is important to remember that multiple parameters are separated by spaces, rather than commas or semicolons.

#### Feature generation options

  

This section describes content that exists only in outdated versions of Java Edition. 
This feature used to be in the game but has since been removed.



Feature generation options



Feature generation option

Parameters

Description

Biome


village

sizedistance

Generates villages, provided they exist in that biome type. Extremely large size values and low distance values generate many villages tightly grouped togethersize determines the size of the village (default is 1, normal worlds have this set to 0, maximum is 65535).distance is the maximum distance between villages (minimum is 9, default is 32).

Plains,Desert, Savanna, Taiga, Snowy Tundra, Snowy Taiga


mineshaft

chance

Generates abandoned mineshafts. Note that they generate in midair if no terrain is present to cover them.chance determines how common mineshafts are (from 0.0 to 1.0, default is 0.01). Higher number, more common.

All


stronghold

distancecountspread

Generates strongholds.distance determines how far strongholds are from the spawn and other strongholds (minimum is 1.0, default is 32.0).count is the number of strongholds that exist per world (default is 3).spread determines how concentrated strongholds are around the spawn (minimum is 1, default is 3). Lower number, lower concentration.

All


biome_1

distance

Generates biome-specific features. This enables igloos, jungle temples, desert pyramids, or witch huts.distance for the maximum distance between features (minimum is 9, default is 32).NOTE: desert pyramids (and potentially other structures) are not generated solely by biome_1, and "desert_pyramid" must be added to the syntax. Both "biome_1" AND "desert_pyramid" must be added to the syntax for pyramids to generate. Putting "desert_pyramid" in your syntax without "biome_1" causes issues, and attempting to /locate a desert pyramid without biome_1 enabled effectively breaks your world. This applies to 1.14+ and potentially earlier game versions. This option may also be necessary with igloos, jungle temples, ocean monuments or witch huts, requires testing.

varies


dungeon

None

Dungeons are generated, if possible.

All


decoration

None

Causes plants, ores, and similar features to be generated according to the biome type. Stone, dirt, grass, sand, or mycelium are required for most features.

All


desert_pyramid

None

Generates desert pyramids.

Desert (Hills)


lake

None

Generates water lakes, sometimes with sand and sugar cane depending on biome.

All


lava_lake

None

Generates lava lakes, with stone surrounding them. If all stone layers are removed in a preset that enables lava lakes, ores can generate in the stone around lava lakes, given the proper altitude.

All


fortress

None

Generates nether fortresses.

Nether


mansion

distance

Generates woodland mansions.

Dark Forest,Dark Forest Hills


oceanmonument

spacingseparation

Generates ocean monuments in the water.spacing determines the size of the grid, in chunks, on which monuments are generated (minimum is 1, default is 32).separation determines the minimum distance, in chunks, between monuments. (minimum is 1, default is 5).WARNING: spacing must be greater than separation, otherwise the game crashes.

Deep Ocean,Deep Warm Ocean,Deep Lukewarm Ocean,Deep Cold Ocean,Deep Frozen Ocean


endcity

distance

Generates end cities.

End Highlands


pillager_outpost

None

Generates Pillager outposts.

Plains Desert,Savanna,Taiga,Snowy Taiga,Snowy Tundra


ruined_portal

None

Generates ruined portals.

All


bastion_remnant

None

Generates bastion remnants.

Nether Wastes, Crimson Forest, Warped Forest, Soul Sand Valley

Note that several criteria must be satisfied before some features can appear:

The biome ID must be correct. For example, at present villages can appear only in biome IDs plains, desert, taiga, savanna, snowy_taiga, and snowy_tundra.
Structures must be turned on when creating new world. (This does not affect normal features such as trees, flowers, mushrooms, and giant mushrooms.)
There must be suitable terrain for the structure to appear on or in. This applies to most features except for mineshafts and strongholds.
Villages are a partial exception; they do not form in mid-air, but can form provided there is at least one solid block layer.
Villages always spawn at least 2 blocks above the void.
For example, to have an 'End' superflat world with obsidian pillars, the biome ID must be the_end, and the top surface block must be End Stone. In this particular case 'Structures' does not need to be turned on in the world options.
Attempting to use an incorrectly formatted preset code causes the game to default to the Classic preset.



#### Preset code example
Consider the following preset code: 

minecraft:mossy_cobblestone,250*minecraft:air,minecraft:obsidian,minecraft:snow;minecraft:plains
It consists of the following elements:

- minecraft:mossy_cobblestone,250*minecraft:air,minecraft:obsidian,minecraft:snow— comma-separated list ofblock IDs.
	- minecraft:mossy_cobblestone— one layer ofmossy cobblestoneon layer -64.
	- 250*minecraft:air— 250 layers ofair, from layer -63 to layer 186.
	- minecraft:obsidian— one layer ofobsidian, on layer 187.
	- minecraft:snow— one layer ofsnow, on layer 188.
- minecraft:plains—biome ID, in this case Plains.

## Notes



