# Moss Block
A moss block is a natural block that can be spread to other blocks by using bone meal.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Chest loot
	- 1.4 Trading
	- 1.5 Post–generation
		- 1.5.1 Spreading specifics
- 2 Usage
	- 2.1 Crafting ingredient
	- 2.2 Composting
	- 2.3 Hatching
	- 2.4 Piston interactivity
- 3 Sounds
- 4 Data values
	- 4.1 ID
- 5 History
- 6 Issues
- 7 Gallery
	- 7.1 Screenshots
	- 7.2 In other media
- 8 References
- 9 External links

## Obtaining
Farthest range moss spreads from a central moss block in Java Edition. In Bedrock Edition, the source block would be a few blocks above the center.
### Breaking
Moss blocks can be mined using any tool or by hand, but a hoe is the fastest way to break it.

| Block     | Moss Block            |
|-----------|-----------------------|
| Hardness  | 0.1                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 0.15                  |
| Wooden    | 0.1                   |
| Stone     | 0.05                  |
| Iron      | 0.05                  |
| Diamond   | 0.05                  |
| Netherite | 0.05                  |
| Golden    | 0.05                  |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
Moss generates on the floor and ceiling within the lush caves biome.


### Chest loot
| Item       | Structure      | Container    | Quantity | Chance                         |
|------------|----------------|--------------|----------|--------------------------------|
|            |                |              |          | Java EditionandBedrock Edition |
| Moss Block | Shipwreck      | Supply chest | 1–4      | 42.1%                          |
|            | Trial Chambers | Supply chest | 2–5      | 20.4%                          |

### Trading
Moss blocks can be obtained by trading with a wandering trader, who may sell 2 moss blocks for 1 emerald.

### 
When bone meal is used on a moss block, moss spreads to any of the blocks listed below, if they have air blocks above them, in a corner-less 7×11×7 volume centered on the original moss block. Foliage can replace air on any of these blocks.

The following blocks can be replaced with moss blocks:

- Andesite
- Coarse Dirt
- Deepslate
- Diorite
- Dirt
- Granite
- Grass Block
- Mud‌[JE  only]
- Muddy Mangrove Roots‌[JE  only]
- Mycelium
- Podzol
- Polished Andesite‌[BE  only]
- Polished Diorite‌[BE  only]
- Polished Granite‌[BE  only]
- Rooted Dirt
- Stone
- Tuff

When a moss block generates with air above it, it has a chance to have grass, an azalea, or a moss carpet growing on it.

| Block            | Chance |
|------------------|--------|
| Short Grass      | 52.08% |
| Moss Carpet      | 26.04% |
| Tall Grass       | 10.42% |
| Azalea           | 7.29%  |
| Flowering Azalea | 4.17%  |

#### Spreading specifics
In Java Edition, when bone meal is used on a moss block, first it is checked that the block directly above the moss block is air. If successful, maximum X and Z distances are chosen (independently from each other) with a 50% chance of being either 2 or 3. Then, in a rectangular area centered on the moss block restricted to those maximum distances, it is decided independently for each vertical column whether a block is converted to moss. Each corner has a 0% to be selected, each edge has a 75% chance, and the rest of the blocks are always selected. If this check succeeds, a scan is started at a Y level one above the moss block to find a block with air above it. If the scan starts in an air block, it searches up to 6 blocks downward. If it starts in a non-air block, it searches up to 4 blocks upward. Both scans stop on the first block with air above it, even if it can not be converted to moss. The chosen block is converted to moss if it can be, and if it can (or already was a moss block) there is a 60% chance vegetation generates above it.

Each piece of bone meal, used on a flat 7×7 grid of convertible blocks, yields an average of 27 moss blocks, with a standard deviation of only 2.4 moss blocks. Those give about 2.5 bone meal in return when used in a composter.

| 0%     | 18.75% | 37.5% | 37.5% | 37.5% | 18.75% | 0%     |
|--------|--------|-------|-------|-------|--------|--------|
| 18.75% | 62.5%  | 87.5% | 87.5% | 87.5% | 62.5%  | 18.75% |
| 37.5%  | 87.5%  | 100%  | 100%  | 100%  | 87.5%  | 37.5%  |
| 37.5%  | 87.5%  | 100%  |       | 100%  | 87.5%  | 37.5%  |
| 37.5%  | 87.5%  | 100%  | 100%  | 100%  | 87.5%  | 37.5%  |
| 18.75% | 62.5%  | 87.5% | 87.5% | 87.5% | 62.5%  | 18.75% |
| 0%     | 18.75% | 37.5% | 37.5% | 37.5% | 18.75% | 0%     |

In Java Edition, blocks that can be replaced by moss are listed in the moss_replaceable block tag, which includes blocks with the base_stone_overworld, cave_vines and dirt tags. This theoretically also includes blocks such as cave vines and dirt path, which cannot be converted because they do not have a solid top surface aligned with the block grid.[more information needed for Bedrock Edition]

## Usage
All plants can be placed on moss except for cacti. Nether fungi can also be placed on moss, but mushrooms can be placed only at light level 12 or below.

### Crafting ingredient
| Name               | Ingredients                  | Crafting recipe |
|--------------------|------------------------------|-----------------|
| Moss Carpet        | Moss Block                   | 3               |
| Mossy Cobblestone  | Cobblestone+<br/>Moss Block  |                 |
| Mossy Stone Bricks | Stone Bricks+<br/>Moss Block |                 |

### Composting
Placing a moss block into a composter has a 65% chance of raising the compost level by 1.

### Hatching
A sniffer egg hatches twice as fast as normal when on top of a moss block.

### Piston interactivity
Moss blocks are destroyed and dropped as items when pushed by pistons. They do not stick to sticky pistons, slime blocks or honey blocks.

## Data values
### ID
Java Edition:

| Name       | Identifier   | Form         | Block tags                                                                                         | Translation key              |
|------------|--------------|--------------|----------------------------------------------------------------------------------------------------|------------------------------|
| Moss Block | `moss_block` | Block & Item | `dirt`<br/>`lush_plants_replaceable`<br/>`small_dripleaf_placeable‌`<br/>`#sniffer_diggable_block` | `block.minecraft.moss_block` |

Bedrock Edition:

| Name       | Identifier   | Numeric ID | Form                       | Item ID[i 1]   | Translation key        |
|------------|--------------|------------|----------------------------|----------------|------------------------|
| Moss Block | `moss_block` | `575`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.moss_block.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

