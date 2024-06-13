# Diamond Ore
Diamond ore is a rare ore that generates deep underground, and is the most abundant and reliable source of diamonds.

Deepslate diamond ore is a variant of diamond ore that can generate in deepslate and tuff blobs.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
- 2 Usage
	- 2.1 Smelting ingredient
	- 2.2 Note blocks
- 3 Sounds
	- 3.1 Diamond ore
	- 3.2 Deepslate diamond ore
- 4 Data values
	- 4.1 ID
- 5 History
- 6 Issues
- 7 Trivia
- 8 Gallery
	- 8.1 Screenshots
	- 8.2 In other media
- 9 See also
- 10 References
- 11 External links

## Obtaining
### Breaking
The diamond ore block itself (rather than its diamond drops) can be obtained by mining it with an iron pickaxe or better, with the Silk Touch enchantment. When mined without Silk Touch, diamond ore drops a single diamond. The maximum amount of diamonds dropped can be increased with Fortune. Fortune I gives a 1⁄3 chance for 2 diamonds, averaging 1.33 diamonds, Fortune II gives a 25% chance (each) to give 2 or 3 diamonds, averaging 1.75 diamonds, and Fortune III gives a 20% chance (each) to give 2, 3, or 4 diamonds, averaging 2.2 diamonds.

| Block     | Diamond Ore | Deepslate Diamond Ore |
|-----------|-------------|-----------------------|
| Hardness  | 3           | 4.5                   |
| Tool      |             |                       |
|           |             | Breakingtime (sec)[A] |
| Default   | 15          | 22.5                  |
| Wooden    | 7.5         | 11.25                 |
| Stone     | 3.75        | 5.65                  |
| Iron      | 0.75        | 1.15                  |
| Diamond   | 0.6         | 0.85                  |
| Netherite | 0.5         | 0.75                  |
| Golden    | 1.25        | 1.9                   |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
See also: Ore (feature)

Ore feature of diamond ore.
Diamond ore generates in the Overworld in the form of ore features, and is more common as the altitude decreases. Diamond ore blocks have a chance to not generate if they are exposed to air; however, they do not have a reduced chance to generate if exposed to water or lava, making them appear more commonly on the walls of aquifers.

Diamond ore generation occurs in four batches:

- 7 blobs of 1-5 ores perchunk, from Y=14 to Y=-63. There is a 50% chance to not generate an ore block if it is next to air.
- 1 blob of 1-23 ores every1⁄9chunks, from Y=14 to Y=-63. There is a 70% chance to not generate an ore block if it is next to air.
- 4 blobs of 1-10 ores per chunk, from Y=14 to Y=-63. Ore blocks do not generate if they are next to air.
- 2 blobs of 1-10 ores per chunk, from Y=-4 to Y=-63. There is a 50% chance to not generate an ore block if it is next to air.

Diamond ore can replace stone, andesite, diorite, granite, tuff, and deepslate. Diamond ore that replaces tuff or deepslate becomes deepslate diamond ore.

Deepslate diamond ore also generates as part of fossils that generate below Y=0, replacing some of the bone blocks.


## Usage
### Smelting ingredient
| Name    | Ingredients                                          | Smelting recipe |
|---------|------------------------------------------------------|-----------------|
| Diamond | Diamond Oreor<br/>Deepslate Diamond Ore+<br/>Anyfuel | 1               |

### Note blocks
Diamond ore can be placed under note blocks to produce "bass drum" sounds.

## Data values
### ID
Java Edition:

| Name                  | Identifier              | Form         | Block tags                                                  | Translation key                         |
|-----------------------|-------------------------|--------------|-------------------------------------------------------------|-----------------------------------------|
| Diamond Ore           | `diamond_ore`           | Block & Item | `diamond_ores`<br/>`mineable/pickaxe`<br/>`needs_iron_tool` | `block.minecraft.diamond_ore`           |
| Deepslate Diamond Ore | `deepslate_diamond_ore` | Block & Item | `diamond_ores`<br/>`mineable/pickaxe`<br/>`needs_iron_tool` | `block.minecraft.deepslate_diamond_ore` |

Bedrock Edition:

| Name                  | Identifier              | Numeric ID | Form                       | Item ID[i 1]   | Translation key                   |
|-----------------------|-------------------------|------------|----------------------------|----------------|-----------------------------------|
| Diamond Ore           | `diamond_ore`           | `56`       | Block & Giveable Item[i 2] | Identical[i 3] | `tile.diamond_ore.name`           |
| Deepslate Diamond Ore | `deepslate_diamond_ore` | `660`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.deepslate_diamond_ore.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑ a bAvailable with /give command.
3. ↑ a bThe block's direct item form has the same id as the block.


