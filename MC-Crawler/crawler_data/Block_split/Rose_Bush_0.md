# Rose Bush
A rose bush is a tall flower that can be crafted into red dye.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Post-generation
- 2 Usage
	- 2.1 Crafting ingredient
	- 2.2 Bees
	- 2.3 Breeding
	- 2.4 Bee nests
	- 2.5 Composting
- 3 Sounds
- 4 Data values
	- 4.1 IDs
	- 4.2 Block states
- 5 History
	- 5.1 Data history
- 6 Issues
- 7 Trivia
- 8 References

## Obtaining
### Breaking
A rose bush can be broken instantly with any item or by hand, dropping itself.

A rose bush also breaks if water or lava runs over its location, if a piston extends or pushes a block into its location, or if a block under the plant is moved or destroyed.

| Block    | Rose Bush           |
|----------|---------------------|
| Hardness | 0                   |
|          | Breakingtime (secs) |
| Default  | 0.05                |

### Natural generation
Rose bushes generate naturally on dirt and grass blocks in  forest,  flower forest,  birch forest,  old growth birch forest, and  dark forest biomes as part of vegetation features.


### Post-generation
Main article: Flower § Post-generation
When bone meal is applied to a rose bush, the flower drops a copy of itself.

## Usage
Main article: Flower § Usage
Like other flowers, rose bushes can be used as decoration and planted on grass blocks, dirt, coarse dirt, rooted dirt, farmland, podzol, mycelium, moss blocks, mud, or muddy mangrove roots. Like other tall flowers, rose bushes cannot be placed inside flower pots. 

### Crafting ingredient
| Name    | Ingredients | Crafting recipe |
|---------|-------------|-----------------|
| Red Dye | Rose Bush   | 2               |

### Bees
Bees engage in a pollinating behavior with rose bushes, increasing the honey level in beehives and bee nests by 1.

### Breeding
Rose bushes can be used to breed, grow, and lead bees.

### Bee nests
Oak, birch, and cherry trees grown from saplings that are within 2 blocks of a rose bush have a 5% chance to grow with a bee nest and 1-3 bees in it.

### Composting
Placing a rose bush into a composter has a 65% chance of raising the compost level by 1. A stack of rose bushes yields an average of 5.94 bone meal.

## Data values
### IDs
Java Edition:

| Name      | Identifier | Form         | Block tags          | Item tags           | Translation key           |
|-----------|------------|--------------|---------------------|---------------------|---------------------------|
| Rose Bush | rose_bush  | Block & Item | flowerstall_flowers | flowerstall_flowers | block.minecraft.rose_bush |

Bedrock Edition:

| Name      | Identifier   | Numeric ID | Form                       | Item ID[i 1]   | Translation key             |
|-----------|--------------|------------|----------------------------|----------------|-----------------------------|
| Rose Bush | double_plant | 175        | Block & Giveable Item[i 2] | Identical[i 3] | tile.double_plant.rose.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block states

Java Edition:

| Name | Default value | Allowed values | Description                                    |
|------|---------------|----------------|------------------------------------------------|
| half | lower         | lowerupper     | The half of the plant contained in this block. |

Bedrock Edition:

| Name              | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                               |
|-------------------|---------------|---------------|----------------|-------------------------|-----------------------------------------------------------|
| double_plant_type | 0x10x20x4     | sunflower     | sunflower      | 0                       | Sunflower                                                 |
|                   |               |               | syringa        | 1                       | Lilac                                                     |
|                   |               |               | grass          | 2                       | Double Tallgrass                                          |
|                   |               |               | fern           | 3                       | Large Fern                                                |
|                   |               |               | rose           | 4                       | Rose Bush                                                 |
|                   |               |               | paeonia        | 5                       | Peony                                                     |
| upper_block_bit   | 0x8           | false         | falsetrue      | 01                      | If it is the upper half of the plant. For items, it is 0. |


