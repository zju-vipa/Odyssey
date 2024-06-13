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

