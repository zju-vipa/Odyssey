# Single biome
Single Biome (also known as Buffet) is a world type in which the entire Overworld consists of one biome. It is simple to customize, albeit very limited.

## Contents
- 1 Generation
	- 1.1 Custom biome
- 2 Bedrock Edition (unused)
- 3 History
- 4 Trivia
- 5 Gallery
	- 5.1 Screenshots
- 6 See also
- 7 References

## Generation
Single Biome uses a single fixed biome source for generating the Overworld with noise generator. Similar to the Default world type, this configuration will generate a world with a bedrock floor at the Y=-64 lower height limit, and the rest of the terrain is generated on top of it. However, in contrast to the Default world type, the Overworld in a Single Biome world consists of only one biome.

The Nether and the End are unchanged from their Default world type counterpart. They use multi-noise biome source for the Nether and minecraft:the_end biome source for the End.

Additionally, players can override any dimension with the same fixed biome source generation like Single Biome using custom dimension data pack.

### Custom biome
Single Biome world type allows players to choose a biome that the world generates in the terrain of the Overworld. Biome choice determines things such as terrain, vegetation, generated structures, and to some extent, mob spawning. Single Biome worlds can be customized to use any one of the available biomes, using only that particular biome for the entire world. The player can choose any of the existing biomes, including the Nether and the End biomes, and custom biomes from data packs.

This customization is available in the "Buffet world customization" menu, accessible by clicking "Customize" button beside the world type selector in the world creation settings.

Using the Nether or End biome to generate the Overworld results in a world with their structures and characteristics, albeit very incomplete. For example, warped forest will not generate any trees, but will still generate nether fortress and their fog and particles. This is caused by a bug, the biome surface and terrain being different from their own dimension.[1]

## 
The code for Single Biome world is inside of Bedrock Edition, but inaccessible through the game's UI. They can only be accessed by editing a world's code or via a third-party site. This code supports every biome within Bedrock Edition, including removed biomes.

In Bedrock Edition, Single Biome has few quirks such as:

- Mineshaftsandstrongholdsgenerate in every biome.
- Single Biome affects theEndbut notNether.
- Nonland biomesdo not generate their terrain.
- Oceansandriverswhen inside of aNether biomehave a checkerboard-like pattern of water and lava.
- Structuregeneration cuts off at y-level 256 when in a Nether or End biome.

This feature is neither widely known nor is it fully developed, and is unlikely to be fully implemented into the game, but it can still be accessed.

