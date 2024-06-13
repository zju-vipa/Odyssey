# Dirt
Dirt is a block found abundantly in most biomes under a layer of grass blocks at the top of the Overworld.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Mob loot
	- 1.4 Post-generation
	- 1.5 Renewability
- 2 Usage
	- 2.1 Crafting ingredient
	- 2.2 Farming
	- 2.3 Dirt path
	- 2.4 Grass and mycelium spreading
	- 2.5 Mud
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
	- 5.1 Data history
- 6 Issues
- 7 Gallery
	- 7.1 Screenshots
- 8 References
- 9 External links

## Obtaining
### Breaking
Dirt drops as an item when broken with any tool or by hand, but a shovel is the quickest way to break it.

| Block     | Dirt                  |
|-----------|-----------------------|
| Hardness  | 0.5                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 0.75                  |
| Wooden    | 0.4                   |
| Stone     | 0.2                   |
| Iron      | 0.15                  |
| Diamond   | 0.1                   |
| Netherite | 0.1                   |
| Golden    | 0.1                   |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

Farmland, dirt paths, grass blocks, mycelium, and podzol drop dirt if broken without Silk Touch. Farmland and dirt paths‌[JE  only] drop dirt even if broken with Silk Touch.

### Natural generation
Dirt comprises the majority of the upper terrain layers in most Overworld biomes, bridging the gap between stone and grass blocks in various thicknesses.

There are approximately 1,850 dirt blocks per chunk in plains, forest, snowy plains, jungle, and windswept hills biomes. In villages, dirt generates naturally as part of several different structures. In woodland mansions, dirt generates in several types of rooms. Four blocks of dirt also generates as part of each ancient city and they also generate in trail ruins.

Dirt can generate in the Overworld in the form of ore blobs. Dirt attempts to generate 7 times per chunk in blobs of size 0-160 at Y=0—160, in all biomes. It can replace stone, granite, andesite, diorite, polished granite‌[BE  only], polished andesite‌[BE  only], polished diorite‌[BE  only], tuff‌[JE  only], and deepslate‌[JE  only].


### Mob loot
An enderman drops a dirt block upon death, if holding one.

### Post-generation
Farmland turns into dirt if either a mob jumps on it, a solid block is placed over it, or if nothing is planted on it and it is not within four blocks of water.

Dirt paths immediately turns into dirt if a solid block is placed over it.

Coarse dirt can be tilled with a hoe to become dirt.

Tilling rooted dirt with a hoe turns it into normal dirt, and yields a hanging roots item.

Grass blocks and mycelium can die under various circumstances. When they die, they turn into dirt.

### Renewability
See also: Tutorials/Dirt farming

By tilling coarse dirt, the player can convert gravel into dirt. Two blocks each of gravel and dirt become four blocks of coarse dirt, which can then be placed and tilled. Since gravel is renewable through bartering with piglins, this makes a renewable source of dirt.

Another way to obtain renewable dirt makes use of moss blocks. Azalea converts the moss block below it into rooted dirt when grown into a tree. In Java Edition, Large spruce trees convert up to about 100 moss blocks into podzol when grown. Since moss can be converted from stone using bone meal, and stone can be renewably generated with water and lava, dirt can be renewably created as long as there is access to water, lava and moss blocks.

A third way to obtain renewable dirt is by buying podzol or rooted dirt from wandering traders. However, only 18 blocks of podzol or 10 blocks of rooted dirt can be purchased from each trader, so this method cannot be performed on a large scale.

## Usage
Dirt's primary use is for farming, but due to its abundancy, it can also be used as a highly available building block.

### Crafting ingredient
| Name        | Ingredients      | Crafting recipe |
|-------------|------------------|-----------------|
| Coarse Dirt | Dirt+<br/>Gravel | 4               |

### Farming
Dirt has the ability to grow saplings, sugar cane, mushrooms, sweet berries, and bamboo, which can be planted directly in dirt under appropriate conditions.

Using a hoe on dirt turns it into farmland, enabling wheat seeds, pumpkin seeds, melon seeds, potatoes, carrots, beetroot seeds, pitcher pods, and torchflower seeds to be planted on it.

### Dirt path
Using a shovel on dirt turns it into a dirt path.

### Grass and mycelium spreading
See also: Grass Block

When a dirt block is adjacent to a grass block and is exposed to a light level of at least 4, it is eventually converted into a grass block at random intervals.

Mycelium spreads in a similar fashion, but requires a light level of at least 9.

### Mud
Using a water bottle, splash water bottle or lingering water bottle will convert the dirt into mud.

## Data values
### ID
Java Edition:

| Name | Identifier | Form         | Block tags                                                                                                                                                                                           | Translation key        |
|------|------------|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|
| Dirt | `dirt`     | Block & Item | `bamboo_plantable_on`<br/>`enderman_holdable`<br/>`dripstone_replaceable_blocks`<br/>`moss_replaceable`<br/>`lush_ground_replaceable`<br/>`mineable/shovel`<br/>`dirt`<br/>`#sniffer_diggable_block` | `block.minecraft.dirt` |

Bedrock Edition:

| Name | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key          |
|------|------------|------------|----------------------------|----------------|--------------------------|
| Dirt | `dirt`     | `3`        | Block & Giveable Item[i 2] | Identical[i 3] | `tile.dirt.default.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

In Bedrock Edition, dirt uses the following block states:

Bedrock Edition:

| Name      | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description |
|-----------|---------------|---------------|----------------|-------------------------|-------------|
| dirt_type | `0x1`         | `normal`      | `normal`       | `0`                     | Dirt        |
|           |               |               | `coarse`       | `1`                     | Coarse Dirt |



