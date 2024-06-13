# Mangrove Propagule
A mangrove propagule is a block that can be grown into a mangrove tree, similar to a sapling.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Trading
	- 1.4 Post-generation
- 2 Usage
	- 2.1 Growing trees
	- 2.2 Bees
	- 2.3 Breeding
	- 2.4 Bee nests
	- 2.5 Decoration
	- 2.6 Fuel
	- 2.7 Composting
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Gallery
	- 7.1 Renders
- 8 References

## Obtaining
### Breaking
Mangrove propagules can be broken instantly using any tool, including the player's fist. Only blocks with block states hanging=false or with age=4 drop themselves.

### Natural generation
Hanging mangrove propagules generate under leaf blocks of mangrove trees that spawn in mangrove swamps.

### Trading
A mangrove propagule is sold by the wandering trader for 5 emeralds.

### Post-generation
Applying bone meal to a block of mangrove leaves with a space underneath produces a hanging mangrove propagule with age=0. Bone meal can then be applied to the propagule itself to increase its age by 1.

## Usage
### Growing trees
See also: Tree

A hanging mangrove propagule cannot grow into a tree.

Like saplings, mangrove propagules can grow only if a player is within a certain radius, even in loaded chunks. 

Also as with saplings, mangrove propagules have two growth stages (with no visible difference between them) before growing into trees. When a tree is to be grown, a height is chosen and then the ground and space are checked; if the ground is bad or there is not space for the chosen height, the tree does not grow. Bone meal can be used to speed up the growth of the sapling, even to grow the tree without sufficient light.

Mangrove propagules can be placed on all variants of dirt (except dirt paths), moss blocks, and mud. It requires a light level of at least 9 to grow. A mangrove also requires at least 6 empty spaces above the propagule. The height of the tree depends on how far the roots can spread horizontally. The roots can spread up to 5 blocks away from the propagule. It requires at least one solid block within the 9×9×9 cube directly underneath and centered on the sapling outside the column where the sapling is, and solid blocks for the bottoms of the roots to land on within 11 blocks below the sapling in a 9×9 area. The farther the solid blocks are below the sapling, the more attempts it takes to generate a suitable tree shape. Mud does not count as a solid block.

Dirt blocks in the space above the propagule are an exception. Dirt blocks do not stop the tree from growing. The dirt remains in place and the rest of the tree generates normally around it (it is possible to grow a tree that contains only one log block at the original sapling location, with a column of dirt above where the rest of the trunk should be and leaves spreading out from it). In Java Edition, all types of log block and wood block and their stripped versions are also treated like dirt blocks (they don't stop growth). In Bedrock Edition, log and wood blocks are treated like other block types and stop the tree from growing if they are above it.

When a propagule on a grass block grows into a tree, the grass block becomes a dirt block.

Mangrove propagules can also be placed underwater.  These can grow from at least 3 blocks of water deep.

### Bees
Bees engage in a pollinating behavior with mangrove propagules, increasing the honey level in beehives and bee nests by 1.

### Breeding
Mangrove propagules can be fed to bees for breeding, and reduce the remaining growth duration of baby bees by 10%. Bees also follow a player holding a mangrove propagule.

### Bee nests
Oak, birch, and cherry trees grown from saplings that are within 2 blocks of a mangrove propagule have a 5% chance to grow with a bee nest and 1-3 bees in it.

### Decoration
Mangrove propagules can be placed in a flower pot.

### Fuel
Mangrove propagules can be used as a fuel in furnaces, smelting 0.5 items per sapling.

### Composting
Placing a mangrove propagule into a composter has a 30% chance of raising the compost level by 1. A stack of saplings yields an average of 2.74 bone meal.

## Data values
### ID
Java Edition:

| Name               | Identifier         | Form         | Translation key                    |
|--------------------|--------------------|--------------|------------------------------------|
| Mangrove Propagule | mangrove_propagule | Block & Item | block.minecraft.mangrove_propagule |

Bedrock Edition:

| Name               | Identifier         | Numeric ID | Form                       | Item ID[i 1]   | Translation key              |
|--------------------|--------------------|------------|----------------------------|----------------|------------------------------|
| Mangrove Propagule | mangrove_propagule | -474       | Block & Giveable Item[i 2] | Identical[i 3] | tile.mangrove_propagule.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block states

Java Edition:

| Name        | Default value | Allowed values | Description                                                                |
|-------------|---------------|----------------|----------------------------------------------------------------------------|
| age         | 0             | 0123           | [more information needed]                                                  |
| hanging     | false         | falsetrue      | If the mangrove propagule is hanging from a mangrove leaves.               |
| stage       | 0             | 01             | Specifies the sapling's growth stage.                                      |
| waterlogged | false         | falsetrue      | Whether or not there's water in the same place as this mangrove propagule. |

