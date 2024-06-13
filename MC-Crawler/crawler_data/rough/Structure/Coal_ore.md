# Coal Ore
Coal ore is a mineral block that drops coal when mined.

Deepslate coal ore is a variant of coal ore that rarely generates at the top of the deepslate layer.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
- 2 Usage
	- 2.1 Smelting ingredient
	- 2.2 Note blocks
- 3 Sounds
	- 3.1 Coal ore
	- 3.2 Deepslate coal ore
- 4 Data values
	- 4.1 ID
- 5 History
	- 5.1 Data history
- 6 Issues
- 7 Gallery
	- 7.1 Screenshots
	- 7.2 In other media
- 8 External links

## Obtaining
### Breaking
Coal ore itself can be obtained by mining it with any pickaxe enchanted with Silk Touch. When mined without Silk Touch, it drops one coal. It is affected by the Fortune enchantment, dropping 1–2, 1–3, or 1–4 coal respectively with Fortune I, II, and III.  It also drops 0–2 when mined. Fortune does not affect the amount of experience dropped.

| Block     | Coal Ore | Deepslate Coal Ore    |
|-----------|----------|-----------------------|
| Hardness  | 3        | 4.5                   |
| Tool      |          |                       |
|           |          | Breakingtime (sec)[A] |
| Default   | 15       | 22.5                  |
| Wooden    | 2.25     | 3.4                   |
| Stone     | 1.15     | 1.7                   |
| Iron      | 0.75     | 1.15                  |
| Diamond   | 0.6      | 0.85                  |
| Netherite | 0.5      | 0.75                  |
| Golden    | 0.4      | 0.6                   |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
See also: Ore (feature)

Coal ore can generate in the Overworld in the form of ore blobs. It generates in two batches per chunk. The first batch attempts to generate 30 times per chunk in blobs of 0-37, evenly from levels 136 to 320. The second batch attempts to generate 20 times per chunk in blobs of 0-37, from levels 0 to 192, being most common at Y=96, and being less common toward either end of the range. Coal ore in this second batch is also less likely to be exposed to air: 50% of ore blocks that would generate exposed do not generate. In Bedrock Edition, coal ore also has the third batches, which attempts to generate 20 times per chunk in blobs of size 0-37, evenly from levels 128 to 256, within any type of mountains biomes.

Coal ore can replace stone, andesite, diorite, granite, tuff, and deepslate. Deepslate coal ore generates when replacing tuff or deepslate, which is a rare occurrence due to the rarity of coal blobs below Y=8 where deepslate generates.

Coal ore is also found in small amounts alongside underground fossils.


## Usage
### Smelting ingredient
| Name | Ingredients           | Smelting recipe |
|------|-----------------------|-----------------|
| Coal | Coal Ore+<br/>Anyfuel | 0.1             |

### Note blocks
Coal ore can be placed under note blocks to produce "bass drum" sounds.

## Data values
### ID
Java Edition:

| Name               | Identifier           | Form         | Block tags                         | Translation key                      |
|--------------------|----------------------|--------------|------------------------------------|--------------------------------------|
| Coal Ore           | `coal_ore`           | Block & Item | `coal_ores`<br/>`mineable/pickaxe` | `block.minecraft.coal_ore`           |
| Deepslate Coal Ore | `deepslate_coal_ore` | Block & Item | `coal_ores`<br/>`mineable/pickaxe` | `block.minecraft.deepslate_coal_ore` |

Bedrock Edition:

| Name               | Identifier           | Numeric ID | Form                       | Item ID[i 1]   | Translation key                |
|--------------------|----------------------|------------|----------------------------|----------------|--------------------------------|
| Coal Ore           | `coal_ore`           | `16`       | Block & Giveable Item[i 2] | Identical[i 3] | `tile.coal_ore.name`           |
| Deepslate Coal Ore | `deepslate_coal_ore` | `661`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.deepslate_coal_ore.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑ a bAvailable with /give command.
3. ↑ a bThe block's direct item form has the same id as the block.

