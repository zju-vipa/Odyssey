# Iron Ore
Iron ore is a mineral block found underground. It is a source of raw iron, which can be smelted into iron ingots. 

Deepslate iron ore is the deepslate variant of iron ore.

Iron ore can be found at any elevation, but is most common at a Y level of 16. Additonally, large ore veins consisting of deepslate iron ore, raw iron blocks and tuff can be occasionally found in the deepslate layer.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
- 2 Usage
	- 2.1 Smelting ingredient
	- 2.2 Note blocks
- 3 Sounds
	- 3.1 Iron ore
	- 3.2 Deepslate iron ore
- 4 Data values
	- 4.1 ID
- 5 History
	- 5.1 Data history
- 6 Issues
- 7 Gallery
	- 7.1 Screenshots
	- 7.2 In other media
- 8 References
- 9 External links

## Obtaining
### Breaking
Iron ore itself can be obtained by mining it with a stone pickaxe or higher enchanted with Silk Touch. When mined without Silk Touch, iron ore drops raw iron. It is affected by the Fortune enchantment, dropping 1–2, 1–3, or 1–4 raw iron respectively with Fortune I, II, and III.

| Block     | Iron Ore | Deepslate Iron Ore    |
|-----------|----------|-----------------------|
| Hardness  | 3        | 4.5                   |
| Tool      |          |                       |
|           |          | Breakingtime (sec)[A] |
| Default   | 15       | 22.5                  |
| Wooden    | 7.5      | 11.25                 |
| Stone     | 1.15     | 1.7                   |
| Iron      | 0.75     | 1.15                  |
| Diamond   | 0.6      | 0.85                  |
| Netherite | 0.5      | 0.75                  |
| Golden    | 1.25     | 1.9                   |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
See also: Ore (feature)

Iron ore generates in three batches. The first batch attempts to generate 90 times per chunk in blobs of 0-13‌[JE  only] or 0-16‌[BE  only], from levels 80 to 384, being most common around level 232 and becoming less common toward either end of the range. The second batch attempts to generate 10 times per chunk in blobs of 0-13‌[JE  only] or 0-16‌[BE  only], from levels -24 to 56, being most common around level 16 and becoming less common toward either end of the range. The third batch attempts to generate 10 times per chunk in blobs of 0-5, evenly from levels -64 to 72.

Iron ore can replace stone, andesite, diorite, granite, tuff, and deepslate. Iron ore that replaces tuff or deepslate becomes deepslate iron ore.

Iron ore can generate as a large ore vein found in the deepslate layer, consisting of iron ore, blocks of raw iron, and tuff.


## Usage
The primary usage of iron ore is to obtain iron ingots.

### Smelting ingredient
| Ingredients                                    | Smelting recipe |
|------------------------------------------------|-----------------|
| Iron Oreor<br/>Deepslate Iron Ore+<br/>Anyfuel | 0.7             |

### Note blocks
Iron ore can be placed under note blocks to produce "bass drum" sounds.

## Data values
### ID
Java Edition:

| Name               | Identifier           | Form         | Block tags                                                | Item tags   | Translation key                      |
|--------------------|----------------------|--------------|-----------------------------------------------------------|-------------|--------------------------------------|
| Iron Ore           | `iron_ore`           | Block & Item | `iron_ores`<br/>`mineable/pickaxe`<br/>`needs_stone_tool` | `iron_ores` | `block.minecraft.iron_ore`           |
| Deepslate Iron Ore | `deepslate_iron_ore` | Block & Item | `iron_ores`<br/>`mineable/pickaxe`<br/>`needs_stone_tool` | `iron_ores` | `block.minecraft.deepslate_iron_ore` |

Bedrock Edition:

| Name               | Identifier           | Numeric ID | Form                       | Item ID[i 1]   | Translation key                |
|--------------------|----------------------|------------|----------------------------|----------------|--------------------------------|
| Iron Ore           | `iron_ore`           | `15`       | Block & Giveable Item[i 2] | Identical[i 3] | `tile.iron_ore.name`           |
| Deepslate Iron Ore | `deepslate_iron_ore` | `656`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.deepslate_iron_ore.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑ a bAvailable with /give command.
3. ↑ a bThe block's direct item form has the same id as the block.


