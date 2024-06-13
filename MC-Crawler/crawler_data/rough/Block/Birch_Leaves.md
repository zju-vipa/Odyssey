# Leaves
Leaves are transparent natural blocks that generate as part of trees. They decay when not attached to a tree trunk, but persist when placed by a player.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Post-generation
- 2 Usage
	- 2.1 Redstone component
	- 2.2 Piston interactivity
	- 2.3 Composting
	- 2.4 Bees
	- 2.5 Bee nests
	- 2.6 Color
		- 2.6.1 Biome colors
		- 2.6.2 Snowy leaves
- 3 Sounds
	- 3.1 Other leaves
	- 3.2 Azalea leaves
	- 3.3 Cherry leaves
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
	- 5.1 Data history
- 6 Issues
- 7 Trivia
- 8 Gallery
	- 8.1 Renders
	- 8.2 Screenshots
- 9 References
- 10 External links

## Obtaining
### Breaking
See also: Fortune § Tabulated probabilities

Hoes are the default tools for breaking leaves, but leaves can be obtained only with shears or Silk Touch enchanted tools.

| Block     | Leaves                |
|-----------|-----------------------|
| Hardness  | 0.2                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 0.3                   |
| Wooden    | 0.15                  |
| Stone     | 0.1                   |
| Iron      | 0.05                  |
| Diamond   | 0.05                  |
| Netherite | 0.05                  |
| Golden    | 0.05                  |
| Shears    | 0.05                  |
| Sword     | 0.2                   |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

| Drop                   | Source                       | No Fortune             | Fortune I                | Fortune II               | Fortune III              |
|------------------------|------------------------------|------------------------|--------------------------|--------------------------|--------------------------|
| Jungle Saplings        | Jungle Leaves                | $2.5% (\frac{1}{40}$)  | $2.78% (\frac{1}{36}$)   | $3.125% (\frac{1}{32}$)  | $4.17% (\frac{1}{24}$)   |
| Azaleaor otherSaplings | Azalea Leaves or otherLeaves | $5% (\frac{1}{20}$)    | $6.25% (\frac{1}{16}$)   | $8.33% (\frac{1}{12)}$   | $10% (\frac{1}{10}$)     |
| 1-2Sticks              | All Leaves                   | $2% (\frac{1}{50}$)    | $2.22% (\frac{1}{45}$)   | $2.5% (\frac{1}{40}$)    | $3.33% (\frac{1}{30}$)   |
| Apples                 | Oak andDark Oak Leaves       | $0.5% (\frac{1}{200}$) | $0.556% (\frac{1}{180}$) | $0.625% (\frac{1}{160}$) | $0.833% (\frac{1}{120}$) |

### Natural generation
Leaves occur naturally on trees and azaleas throughout the Overworld. Specially, oak leaves‌[Java Edition  only] or jungle leaves‌[Bedrock Edition  only] generate in jungle bushes. Oak leaves also generate in the tree at meeting points in plains villages. Dark oak leaves also generate in woodland mansions.


### Post-generation
See also: Tutorials/Tree farming

Leaves generate as part of trees grown from saplings, azaleas, or mangrove propagules.

## Usage
Leaves from trees spontaneously decay (disappear) when they receive a block tick if they are not connected to a block with the logs tag (log or wood block), either directly or via other leaf blocks, with a maximum distance of 6 blocks‌[Java Edition  only] or 4 blocks‌[Bedrock Edition  only]. Leaves placed by players never decay.

Leaves that decay, or are destroyed without using Silk Touch or shears, yield saplings 5% (1⁄20) of the time, sticks 2% of the time, and otherwise drop nothing. Jungle leaves drop saplings 2.5% (1⁄40) of the time. Oak and dark oak leaves also have a separate but additional 0.5% (1⁄200) chance of dropping an apple, making it extremely rare but possible for a single leaf to drop a sapling, a stick and an apple at the same time. Rates are increased by the Fortune enchantment. Leaves that are burned do not yield saplings or apples.

Leaves take on a different shade of green depending on the biome in which they are placed.

Leaves are always transparent to light, but cannot be seen through when the graphics mode is set to "Fast"; the transparent regions are instead black‌[JE  only]/dark green‌[BE  only]. They diffuse sky light, causing the shadows they cast under trees.

Leaves can be waterlogged, despite being a full block. Water does not spread out‌[Java Edition  only] and waterlogged leaves follow the same rules as any other waterlogged block. When concrete powder is placed on any side of the waterlogged leaves it turns into concrete, without the danger of the water running out of the block.

Applying bone meal to mangrove leaves with a space beneath produces a hanging mangrove propagule with age=0.

### Redstone component

  

This feature is exclusive to  Java Edition. 


The state of a leaves block—including a player-placed block—changes after 1 game tick (half a redstone tick) when the distance to the nearest log or wood block changes, up to 6 blocks of leaves away. Observers facing away from the leaves detect this change and transmit a redstone signal in the same game tick, making leaves useful for redstone signal transmission. This has been called "Leafstone" by the Minecraft Community.

### Piston interactivity
Leaves are destroyed when pushed by pistons. They do not stick to sticky pistons, slime blocks or honey blocks.

### Composting
Leaves have a 30% chance of increasing the compost level in a composter by 1. A stack of leaves yields an average of 2.74 bone meal.

### Bees
Flowering azaleas leaves and cherry leaves function like any other flowers in their interaction and uses with bees.

### Bee nests
Oak, birch, and cherry trees grown from saplings that are within 2 blocks of flowering azalea leaves or cherry leaves have a 5% chance to grow with bee nest and 1-3 bees in it.

### Color
Main articles: Color § Biome colors and Block colors § Foliage colors
- In the inventory,oak,jungle,acacia, anddark oak leaves are colored#48b518.
- In the inventory,mangrove leaves are colored#92c648.
- Spruce leaves are colored#619961, and are not affected by biome or inventory color.[1]
- Birch leaves are colored#80a755, and are not affected by biome or inventory color.[1]
- Azalea,flowering azalea, andcherry leaves are not colored.

##### Biome colors
These values are generated by the biome dyeing algorithm.

| Biome                                                                                                                                                                                                                                                                                                         | Temperature | Downfall | Foliage Color | Block |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|----------|---------------|-------|
| (Default values)<br/>The Void<br/>River<br/>Warm Ocean<br/>Lukewarm Ocean<br/>Deep Lukewarm Ocean<br/>Ocean<br/>Deep Ocean<br/>Cold Ocean<br/>Deep Cold Ocean<br/>Deep Frozen Ocean‌[JE  only]<br/>Lush Caves‌[JE  only]<br/>The End<br/>End Highlands<br/>End Midlands<br/>Small End Islands<br/>End Barrens | 0.5         | 0.5      | #71a74d       |       |
| Lush Caves‌[BE  only]                                                                                                                                                                                                                                                                                         | 0.9         | 0.0      | #a6a432       |       |
| Plains<br/>Beach<br/>Sunflower Plains<br/>Dripstone Caves‌[JE  only]<br/>Deep Dark                                                                                                                                                                                                                            | 0.8         | 0.4      | #77ab2f       |       |
| Dripstone Caves‌[BE  only]                                                                                                                                                                                                                                                                                    | 0.2         | 0.0      | #70a26c       |       |
| Snowy Plains<br/>Ice Spikes<br/>Snowy Taiga<br/>Frozen Ocean<br/>Deep Frozen Ocean‌[BE  only]<br/>Frozen River                                                                                                                                                                                                | 0.0         | 0.5      | #60a17b       |       |
| Grove                                                                                                                                                                                                                                                                                                         | -0.2        | 0.8      |               |       |
| Snowy Slopes                                                                                                                                                                                                                                                                                                  | -0.3        | 0.9      |               |       |
| Frozen Peaks<br/>Jagged Peaks                                                                                                                                                                                                                                                                                 | -0.7        | 0.9      |               |       |
| Desert<br/>Savanna‌[JE  only]<br/>Savanna Plateau‌[JE  only]<br/>Windswept Savanna<br/>Nether Wastes<br/>Warped Forest<br/>Crimson Forest<br/>Soul Sand Valley<br/>Basalt Deltas                                                                                                                              | 2.0         | 0.0      | #aea42a       |       |
| Savanna‌[BE  only]                                                                                                                                                                                                                                                                                            | 1.2         | 0.0      |               |       |
| Savanna Plateau‌[BE  only]                                                                                                                                                                                                                                                                                    | 1.0         | 0.0      |               |       |
| Badlands<br/>Wooded Badlands<br/>Eroded Badlands                                                                                                                                                                                                                                                              | 2.0         | 0.0      | #9e814d[n 1]  |       |
| Swamp                                                                                                                                                                                                                                                                                                         | 0.8         | 0.9      | #6a7039[n 1]  |       |
| Mangrove Swamp                                                                                                                                                                                                                                                                                                | 0.8         | 0.9      | #8db127[n 1]  |       |
| Forest<br/>Dark Forest<br/>Flower Forest                                                                                                                                                                                                                                                                      | 0.7         | 0.8      | #59ae30       |       |
| Birch Forest<br/>Old Growth Birch Forest                                                                                                                                                                                                                                                                      | 0.6         | 0.6      | #6ba941       |       |
| Old Growth Pine Taiga                                                                                                                                                                                                                                                                                         | 0.3         | 0.8      | #68a55f       |       |
| Old Growth Spruce Taiga<br/>Taiga                                                                                                                                                                                                                                                                             | 0.25        | 0.8      | #68a464       |       |
| Windswept Hills<br/>Windswept Gravelly Hills<br/>Windswept Forest<br/>Stony Shore                                                                                                                                                                                                                             | 0.2         | 0.3      | #6da36b       |       |
| Jungle<br/>Bamboo Jungle                                                                                                                                                                                                                                                                                      | 0.95        | 0.9      | #30bb0b       |       |
| Sparse Jungle                                                                                                                                                                                                                                                                                                 | 0.95        | 0.8      | #3eb80f       |       |
| Meadow                                                                                                                                                                                                                                                                                                        | 0.5         | 0.8      | #63a948       |       |
| Cherry Grove                                                                                                                                                                                                                                                                                                  | 0.5         | 0.8      | #b6db61[n 1]  |       |
| Stony Peaks                                                                                                                                                                                                                                                                                                   | 1.0         | 0.3      | #82ac1e       |       |
| Snowy Beach                                                                                                                                                                                                                                                                                                   | 0.05        | 0.3      | #64a278       |       |
| Mushroom Fields                                                                                                                                                                                                                                                                                               | 0.9         | 1.0      | #2bbb0f       |       |

Unused biomes in Bedrock Edition.

| Biome                                                                               | Temperature | Downfall | Foliage Color | Block |
|-------------------------------------------------------------------------------------|-------------|----------|---------------|-------|
| (Default values)<br/>Deep Warm Ocean                                                | 0.5         | 0.5      | #71a74d       |       |
| Snowy Mountains<br/>Legacy Frozen Ocean                                             | 0.0         | 0.5      | #60a17b       |       |
| Snowy Taiga Hills<br/>Snowy Taiga Mountains                                         | -0.5        | 0.4      |               |       |
| Taiga Hills<br/>Taiga Mountains                                                     | 0.25        | 0.8      | #68a464       |       |
| Desert Hills<br/>Desert Lakes                                                       | 2.0         | 0.0      | #aea42a       |       |
| Badlands Plateau<br/>Modified Badlands Plateau<br/>Modified Wooded Badlands Plateau | 2.0         | 0.0      | #9e814d[n 1]  |       |
| Shattered Savanna Plateau                                                           | 1.0         | 0.5      | #64b216       |       |
| Swamp Hills                                                                         | 0.8         | 0.5      | #6a7039[n 1]  |       |
| Wooded Hills<br/>Tall Birch Hills<br/>Dark Forest Hills                             | 0.7         | 0.8      | #59ae30       |       |
| Birch Forest Hills                                                                  | 0.6         | 0.6      | #6ba941       |       |
| Giant Tree Taiga Hills<br/>Giant Spruce Taiga Hills                                 | 0.3         | 0.8      | #68a55f       |       |
| Gravelly Mountains+<br/>Mountain Edge                                               | 0.2         | 0.3      | #6da36b       |       |
| Jungle Hills<br/>Modified Jungle<br/>Bamboo Jungle Hills                            | 0.95        | 0.9      | #30bb0b       |       |
| Modified Jungle Edge                                                                | 0.95        | 0.8      | #3eb80f       |       |
| Mushroom Field Shore                                                                | 0.9         | 1.0      | #2bbb0f       |       |

1. ↑ a b c d e fColor is preset

#### Snowy leaves

  

This feature is exclusive to  Bedrock Edition. 


Trees in a snowy biome during snowfall.
In any biome with a base temperature of below 0.15, all leaves exposed to the sky gradually fade to white once snowfall begins, giving them a frosted appearance for the storm's duration. Cherry, azalea, and flowering azalea leaves are not affected, and the change is entirely invisible to the client if the fancy graphics option is disabled (though it still takes place, and leaves are the correct color phase for the time if the option is reenabled). After snowfall ends, leaves gradually fade back to their normal coloration.

## Data values
### ID
Java Edition:

| Name                    | Identifier                | Form         | Block tags                                                                     | Item tags              | Translation key                           |
|-------------------------|---------------------------|--------------|--------------------------------------------------------------------------------|------------------------|-------------------------------------------|
| Oak Leaves              | `oak_leaves`              | Block & Item | `lava_pool_stone_cannot_replace`<br/>`leaves`<br/>`mineable/hoe`               | `leaves`               | `block.minecraft.oak_leaves`              |
| Spruce Leaves           | `spruce_leaves`           | Block & Item | `lava_pool_stone_cannot_replace`<br/>`leaves`<br/>`mineable/hoe`               | `leaves`               | `block.minecraft.spruce_leaves`           |
| Birch Leaves            | `birch_leaves`            | Block & Item | `lava_pool_stone_cannot_replace`<br/>`leaves`<br/>`mineable/hoe`               | `leaves`               | `block.minecraft.birch_leaves`            |
| Jungle Leaves           | `jungle_leaves`           | Block & Item | `lava_pool_stone_cannot_replace`<br/>`leaves`<br/>`mineable/hoe`               | `leaves`               | `block.minecraft.jungle_leaves`           |
| Acacia Leaves           | `acacia_leaves`           | Block & Item | `lava_pool_stone_cannot_replace`<br/>`leaves`<br/>`mineable/hoe`               | `leaves`               | `block.minecraft.acacia_leaves`           |
| Dark Oak Leaves         | `dark_oak_leaves`         | Block & Item | `lava_pool_stone_cannot_replace`<br/>`leaves`<br/>`mineable/hoe`               | `leaves`               | `block.minecraft.dark_oak_leaves`         |
| Mangrove Leaves         | `mangrove_leaves`         | Block & Item | `lava_pool_stone_cannot_replace`<br/>`leaves`<br/>`mineable/hoe`               | `leaves`               | `block.minecraft.mangrove_leaves`         |
| Cherry Leaves           | `cherry_leaves`           | Block & Item | `lava_pool_stone_cannot_replace`<br/>`leaves`<br/>`mineable/hoe`               | `leaves`               | `block.minecraft.cherry_leaves`           |
| Azalea Leaves           | `azalea_leaves`           | Block & Item | `lava_pool_stone_cannot_replace`<br/>`leaves`<br/>`mineable/hoe`               | `leaves`               | `block.minecraft.azalea_leaves`           |
| Flowering Azalea Leaves | `flowering_azalea_leaves` | Block & Item | `flowers`<br/>`lava_pool_stone_cannot_replace`<br/>`leaves`<br/>`mineable/hoe` | `flowers`<br/>`leaves` | `block.minecraft.flowering_azalea_leaves` |

Bedrock Edition:

| Name                   | Identifier               | Alias ID      | Numeric ID | Form                       | Item ID[i 1]   | Translation key                                            |
|------------------------|--------------------------|---------------|------------|----------------------------|----------------|------------------------------------------------------------|
| Oak Leaves             | `oak_leaves`             | `leaves / 0`  | `18`       | Block & Giveable Item[i 2] | Identical[i 3] | `tile.leaves.oak.name`                                     |
| Spruce Leaves          | `spruce_leaves`          | `leaves / 1`  | `-800`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.leaves.spruce.name`                                  |
| Birch Leaves           | `birch_leaves`           | `leaves / 2`  | `-801`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.leaves.birch.name`                                   |
| Jungle Leaves          | `jungle_leaves`          | `leaves / 3`  | `-802`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.leaves.jungle.name`                                  |
| Acacia Leaves          | `acacia_leaves`          | `leaves2 / 0` | `161`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.leaves2.acacia.name`<br/>`tile.leaves.acacia.name`   |
| Dark Oak Leaves        | `dark_oak_leaves`        | `leaves2 / 1` | `-803`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.leaves2.big_oak.name`<br/>`tile.leaves.big_oak.name` |
| Mangrove Leaves        | `mangrove_leaves`        | None          | `-472`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.mangrove_leaves.name`                                |
| Cherry Leaves          | `cherry_leaves`          | None          | `-548`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.cherry_leaves.name`                                  |
| Azalea Leaves          | `azalea_leaves`          | None          | `579`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.azalea_leaves.name`                                  |
| Flowered Azalea Leaves | `azalea_leaves_flowered` | None          | `580`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.azalea_leaves_flowered.name`                         |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑ a b c d e f g h i jAvailable with /give command.
3. ↑ a b c d e f g h i jThe block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:

| Name        | Default value | Allowed values                                      | Description                                                                                    |
|-------------|---------------|-----------------------------------------------------|------------------------------------------------------------------------------------------------|
| distance    | `7`           | `1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7` | How far away this block is from the nearest log or wood, intaxicab distance.                   |
| persistent  | `false`       | `false`<br/>`true`                                  | If the block persists regardless of having no wood nearby.<br/>`true`for player-placed leaves. |
| waterlogged | `false`       | `false`<br/>`true`                                  | Whether or not there's water in the same place as this leaves.                                 |

Bedrock Edition:

| Name           | Metadata Bits | Default value | Allowed values     | Values forMetadata Bits | Description                                                |
|----------------|---------------|---------------|--------------------|-------------------------|------------------------------------------------------------|
| persistent_bit | Not Supported | `false`       | `false`<br/>`true` | `Unsupported`           | If the block persists regardless of having no wood nearby. |
| update_bit     | Not Supported | `false`       | `false`<br/>`true` | `Unsupported`           | If the block checks for nearby wood and decays.            |



