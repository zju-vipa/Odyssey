# Gold Ore
Gold ore is a rare mineral block found underground.

Deepslate gold ore is a variant of gold ore that can generate in deepslate and tuff.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
- 2 Usage
	- 2.1 Smelting ingredient
	- 2.2 Piglins
	- 2.3 Note Blocks
- 3 Sounds
	- 3.1 Gold ore
	- 3.2 Deepslate gold ore
- 4 Data values
	- 4.1 ID
- 5 Achievements
- 6 Advancements
- 7 History
	- 7.1 Data history
- 8 Issues
- 9 Gallery
	- 9.1 Screenshots
	- 9.2 In other media
- 10 See also
- 11 References
- 12 External links

## Obtaining
### Breaking
Gold ore drops as raw gold if mined by an iron pickaxe or higher. If mined by any other tool, it drops nothing. Mining with a Silk Touch pickaxe drops itself. It is affected by Fortune enchantment, dropping 1–2, 1–3, or 1–4 raw gold respectively with Fortune I, II, and III.

| Block     | Gold Ore | Deepslate Gold Ore    |
|-----------|----------|-----------------------|
| Hardness  | 3        | 4.5                   |
| Tool      |          |                       |
|           |          | Breakingtime (sec)[A] |
| Default   | 15       | 22.5                  |
| Wooden    | 7.5      | 11.25                 |
| Stone     | 3.75     | 5.65                  |
| Iron      | 0.75     | 1.15                  |
| Diamond   | 0.6      | 0.85                  |
| Netherite | 0.5      | 0.75                  |
| Golden    | 1.25     | 1.9                   |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
See also: Ore (feature)

Gold ore can generate in the Overworld in the form of ore features. 

Gold ore attempts to generate in two batches. The first batch generates 4 times per chunk in blobs of 0—13 blocks, from levels -64 to 32. It is most likely to be found around layer -16, becoming less common toward either end of the range. The second batch has a probability of 1/2 per chunks to generate in blobs of 0—13 blocks that generate uniformly between -64 and -48. There is also an extra batch of gold ore in badlands biome that generates 50 times per chunk in blobs of 0—13 blocks, from 32 to 256 uniformly. Gold ore is also less likely to be exposed to air: 50% of ore blocks from the first and second batch do not generate. The extra batch in badlands generate regardless of exposure to air. 

Gold ore can replace stone, andesite, diorite, granite, tuff, and deepslate. Any gold ore that replaces tuff or deepslate becomes deepslate gold ore.


## Usage
### Smelting ingredient
| Name       | Ingredients                                    | Smelting recipe |
|------------|------------------------------------------------|-----------------|
| Gold Ingot | Gold Oreor<br/>Deepslate Gold Ore+<br/>Anyfuel | 1               |

### Piglins
Piglins become hostile toward players who mine gold ore, even if the player is wearing golden armor. Piglins also run toward any gold ores on the ground, and inspect it for 6 to 8 seconds before putting it in their inventory.

### Note Blocks
Gold ore can be placed under note blocks to produce "bass drum" sounds.

## Data values
### ID
Java Edition:

| Name               | Identifier           | Form         | Block tags                                                                        | Item tags                      | Translation key                      |
|--------------------|----------------------|--------------|-----------------------------------------------------------------------------------|--------------------------------|--------------------------------------|
| Gold Ore           | `gold_ore`           | Block & Item | `gold_ores`<br/>`guarded_by_piglins`<br/>`mineable/pickaxe`<br/>`needs_iron_tool` | `gold_ores`<br/>`piglin_loved` | `block.minecraft.gold_ore`           |
| Deepslate Gold Ore | `deepslate_gold_ore` | Block & Item | `gold_ores`<br/>`guarded_by_piglins`<br/>`mineable/pickaxe`<br/>`needs_iron_tool` | `gold_ores`<br/>`piglin_loved` | `block.minecraft.deepslate_gold_ore` |

Bedrock Edition:

| Name               | Identifier           | Numeric ID | Form                       | Item ID[i 1]   | Translation key                |
|--------------------|----------------------|------------|----------------------------|----------------|--------------------------------|
| Gold Ore           | `gold_ore`           | `14`       | Block & Giveable Item[i 2] | Identical[i 3] | `tile.gold_ore.name`           |
| Deepslate Gold Ore | `deepslate_gold_ore` | `657`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.deepslate_gold_ore.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑ a bAvailable with /give command.
3. ↑ a bThe block's direct item form has the same id as the block.


