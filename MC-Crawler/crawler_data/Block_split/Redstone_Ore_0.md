# Redstone Ore
Redstone ore is the ore block from which redstone is obtained.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
- 2 Usage
	- 2.1 Light
	- 2.2 Smelting ingredient
	- 2.3 Note Blocks
- 3 Sounds
	- 3.1 Redstone ore
	- 3.2 Deepslate redstone ore
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 Video
- 6 History
	- 6.1 Lit redstone ore "item"
		- 6.1.1 Appearances
		- 6.1.2 Names
- 7 Issues
- 8 Gallery
	- 8.1 Screenshots
	- 8.2 In other media
- 9 See also
- 10 References
- 11 External links

## Obtaining
### Breaking
Redstone ore must be mined with an iron pickaxe or higher to drop redstone dust. When mined, it drops 4–5 redstone dust. It is affected by the Fortune enchantment, dropping 4-6, 4-7, or 4-8 redstone respectively with Fortune I, II, and III (averaging at 6 redstone dust with Fortune level 3[1][2]). If mined with Silk Touch, it drops itself instead of redstone dust.

| Block     | Redstone Ore | Deepslate Redstone Ore |
|-----------|--------------|------------------------|
| Hardness  | 3            | 4.5                    |
| Tool      |              |                        |
|           |              | Breakingtime (sec)[A]  |
| Default   | 15           | 22.5                   |
| Wooden    | 7.5          | 11.25                  |
| Stone     | 3.75         | 5.65                   |
| Iron      | 0.75         | 1.15                   |
| Diamond   | 0.6          | 0.85                   |
| Netherite | 0.5          | 0.75                   |
| Golden    | 1.25         | 1.9                    |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


### Natural generation
See also: Ore (feature)

Redstone ore can generate in the Overworld in the form of ore features. Redstone ore generates in two batches per chunk. The first batch attempts to generate 4 times per chunk, in blobs of 0–10, evenly from levels -64 to 15. The second batch attempts to generate 8 times per chunk, in blobs of 0–10, from levels -63 to -32, being more common the lower the elevation.

Redstone ore can replace stone, andesite, diorite, granite, tuff, and deepslate. Any redstone ore that replaces tuff or deepslate becomes deepslate redstone ore.


## Usage
### Light
Redstone ore produces the light level of 9 and emits bright red powered redstone particle when clicked, updated, or contacted by almost any entity (among some of the exceptions are a sneaking player, fired arrows, fired fire charges, shulkers, shulker bullets, and the ender dragon). This effect continues until the redstone ore block receives a random block tick (averaging 68.27 seconds). This effect does not actually produce redstone power, but the block changes can be detected with an observer or a block update detector.

Subsequent clickings on a redstone ore block causes it to emit an extra burst of particles per click.

### Smelting ingredient
| Name          | Ingredients                                  | Smelting recipe |
|---------------|----------------------------------------------|-----------------|
| Redstone Dust | Redstone OreorDeepslate Redstone Ore+Anyfuel | 0.7             |

### Note Blocks
Redstone ore can be placed under note blocks to produce "bass drum" sounds.

## Data values
A redstone ore that glows and emits particles in the dark.
### ID
Java Edition:

| Name                   | Identifier             | Form         | Block tags                                   | Translation key                        |
|------------------------|------------------------|--------------|----------------------------------------------|----------------------------------------|
| Redstone Ore           | redstone_ore           | Block & Item | redstone_oresmineable/pickaxeneeds_iron_tool | block.minecraft.redstone_ore           |
| Deepslate Redstone Ore | deepslate_redstone_ore | Block & Item | redstone_oresmineable/pickaxeneeds_iron_tool | block.minecraft.deepslate_redstone_ore |

Bedrock Edition:

| Name                       | Identifier                 | Numeric ID | Form                         | Item ID[i 1]   | Translation key                  |
|----------------------------|----------------------------|------------|------------------------------|----------------|----------------------------------|
| Redstone Ore               | redstone_ore               | 73         | Block & Giveable Item[i 2]   | Identical[i 3] | tile.redstone_ore.name           |
| Lit Redstone Ore           | lit_redstone_ore           | 74         | Block & Ungiveable Item[i 4] | Identical[i 3] | —                                |
| Deepslate Redstone Ore     | deepslate_redstone_ore     | 658        | Block & Giveable Item[i 2]   | Identical[i 3] | tile.deepslate_redstone_ore.name |
| Lit Deepslate Redstone Ore | lit_deepslate_redstone_ore | 659        | Block & Ungiveable Item[i 4] | Identical[i 3] | —                                |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ a b Available with /give command.

↑ a b c d The block's direct item form has the same id as the block.

↑ a b Unavailable with /give command


### Block states
See also: Block states

Java Edition:

| Name | Default value | Allowed values | Description                 |
|------|---------------|----------------|-----------------------------|
| lit  | false         | falsetrue      | If the redstone ore is lit. |



## See also
- Mechanisms
- Traps


