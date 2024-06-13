# Superflat
Superflat‌[Java Edition  only] or Flat‌[Bedrock Edition  only] is a world type or a vanilla world preset replacing the normal varied terrain of the Overworld, with customizable layers.

In Java Edition, superflat can also refer to a dimension's generator type, with which the completely flat terrain can be generated in a specific dimension. See also Custom dimension and Custom world preset.

## Contents
- 1 Structure
- 2 Multiplayer
- 3 Customization
	- 3.1 Vanilla superflat level generation presets
	- 3.2 Preset code format
		- 3.2.1 Feature generation options
		- 3.2.2 Preset code example
- 4 History
- 5 Issues
- 6 Trivia
- 7 Gallery
	- 7.1 Screenshots
	- 7.2 Development images
- 8 See also
- 9 Notes
- 10 References

## Structure
In the default Superflat world, the terrain consists of one layer of bedrock, two layers of dirt, and one layer of grass blocks. Because the entire world is a plains biome by default, in Java Edition, villages generate relatively frequently; strongholds are also generated. While in Bedrock Edition no feature or structure generate in Flat worlds.

In the default Superflat world, the surface of the world is completely flat and at Y=-60, except for villages and other structures if they are enabled. Mobs still spawn normally. Because of the low altitude of the world, slimes spawn frequently.

Superflat worlds allow the player to access the Nether and the End in the usual ways, which generate as normal.[1]

## Multiplayer
In Java Edition, in order to create a Superflat world in a multiplayer server, the level-type flag in server.properties must be flat, instead of default. To alter the layers, biome and structures define generator-settings, which is a string of a JSON object:

- : The root object.
	- 
	- Flat generation settings

In Bedrock Edition, level-type in server.properties must be "FLAT" to generate a flat world.

## Customization

  

This feature is exclusive to  Java Edition. 


The Superflat world type button in Java Edition.
In Java Edition, superflat generator defaults to one layer of grass block, two layers of dirt, and one layer of bedrock, in "plains" biome and generating villages and strongholds. This content can be customized.

Upon selecting "Superflat" in the "World Type" box, a new button becomes clickable labeled "Customize". In the customize menu, there are two buttons available to customize Superflat worlds, which include the "Remove Layer" button, used for removing unwanted types of layers, and the "Presets" button, used for preset code string or "superflat level generation presets". There are nine original presets, and you can also use data packs to customize presets, see Custom world preset#Superflat Level Generation Preset.

Note that the default superflat is different from the "Classic" preset, where the default superflat (without using any preset) can generate strongholds, while the "Classic" preset has no stronghold.

If the player can understand the preset code syntax, they can create presets of their own by entering valid information into the preset code box, where these changes can be previewed and applied. Preset code is shareable, which is highlightable and copyable. Similar to how new worlds are shared through seeds, preset code can be entered into this box to use it.

Note that the preset code currently cannot fully describe a superflat level generation preset. Settings related to features and structures are inaccessible in the preset code. Using the preset code and the "Remove Layer" function to recreate world can only ensure that the blocks on each layer are the same, but cannot guarantee the same settings of features or structures. When using preset code, the settings for features and structures are based on what preset is selected. If no preset is selected, only villages and strongholds are generated. For example, if typing preset code with the Classic Flat preset selected, only villages are generated. If typing it with the Overworld preset selected, features in Plains biome (except monster rooms) and Pillager Outpost, Village, Stronghold, Mineshaft, Dungeon, and Ruined Portal are generated.

In Bedrock Edition there is no interface for customizing flat worlds. It always uses the default configuration (one layer of bedrock, two layers of dirt, and a layer of grass blocks) even when the Seed Picker is used. However, custom flat worlds are possible internally, and can be used by modifying FlatWorldLayers in the world's level.dat file using an external editor. This was used for converting Legacy Console Edition custom superflat worlds over to Bedrock Edition.

### Vanilla superflat level generation presets
| Preset           | Layers                                                   | Biome           | Structures                                                                              | Generating features | Forced to generate lava lakes | Notes                                                                                                                                                                                     |
|------------------|----------------------------------------------------------|-----------------|-----------------------------------------------------------------------------------------|---------------------|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Classic Flat     | Grass Block x1Dirt x2Bedrock x1                          | Plains          | Village                                                                                 | No                  | No                            | Note that this is different from the default superflat world, where the default superflat (without using any preset) can generatestrongholds, while the classic preset has no stronghold. |
| Tunnelers' Dream | Grass Block x1Dirt x5Stone x230Bedrock x1                | Windswept Hills | Stronghold<br/>Mineshaft<br/>Dungeon                                                    | Yes                 | No                            |                                                                                                                                                                                           |
| Water World      | Water x90Gravel x5Dirt x5Stone x5Deepslate x64Bedrock x1 | Deep Ocean      | Ocean Monument<br/>Ocean Ruin<br/>Shipwreck                                             | No                  | No                            |                                                                                                                                                                                           |
| Overworld        | Grass Block x1Dirt x3Stone x59Bedrock x1                 | Plains          | Pillager Outpost<br/>Village<br/>Stronghold<br/>Mineshaft<br/>Dungeon<br/>Ruined Portal | Yes                 | Yes                           | Mimics the height of default world generation. Ores can also be found.                                                                                                                    |
| Snowy Kingdom    | Snow x1Grass Block x1Dirt x3Stone x59Bedrock x1          | Snowy Plains    | Village<br/>Igloo                                                                       | No                  | No                            |                                                                                                                                                                                           |
| Bottomless Pit   | Grass Block x1Dirt x3Cobblestone x2                      | Plains          | Village                                                                                 | No                  | No                            | Allows easySurvivalaccess to theVoid, due to the replacement of bedrock with cobblestone.                                                                                                 |
| Desert           | Sand x8Sandstone x52Stone x3Bedrock x1                   | Desert          | Village<br/>Desert pyramid<br/>Stronghold<br/>Mineshaft<br/>Dungeon                     | Yes                 | No                            | Sandstone and stone layer amounts are reversed from Default worlds.                                                                                                                       |
| Redstone Ready   | Sandstone x116Stone x3Bedrock x1                         | Desert          | None                                                                                    | No                  | No                            |                                                                                                                                                                                           |
| The Void         | Air x1                                                   | The Void        | None                                                                                    | Yes                 | No                            | Spawns the player on a stone platform with a single cobblestone block at the center of the platform.                                                                                      |

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


