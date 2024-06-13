# Pitcher Plant
A pitcher plant is a tall flower that grows from a pitcher pod.

## Contents
- 1 Obtaining
	- 1.1 Breaking
- 2 Usage
	- 2.1 Crafting ingredient
	- 2.2 Bees
	- 2.3 Breeding
	- 2.4 Bee nests
	- 2.5 Composting
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Trivia
- 8 References

## Obtaining
Pitcher plants do not generate naturally and are obtained by growing a pitcher pod. Breaking a fully grown pitcher crop drops one pitcher plant. 

Unlike the other tall flowers, it is not possible to duplicate pitcher plants by applying bone meal on them.

### Breaking
Pitcher plants can be broken instantly with any item or by hand.

A pitcher plant also breaks if water or lava runs over its location, if a piston extends or pushes a block into its location, or if a block under the plant is moved or destroyed.

| Block    | Pitcher Plant       |
|----------|---------------------|
| Hardness | 0                   |
|          | Breakingtime (secs) |
| Default  | 0.05                |

## Usage
Like most flowers, pitcher plants can be used as decoration and planted on grass blocks, dirt, coarse dirt, rooted dirt, farmland, podzol, mycelium, moss blocks, mud, or muddy mangrove roots. Like other tall flowers, pitcher plants cannot be placed inside flower pots.

### Crafting ingredient
A pitcher plant can be crafted into 2 cyan dye.

| Name     | Ingredients   | Crafting recipe |
|----------|---------------|-----------------|
| Cyan Dye | Pitcher Plant | 2               |

### Bees
Bees engage in a pollinating behavior with pitcher plants, increasing the honey level in beehives and bee nests by 1.

### Breeding
Pitcher plants can be used to breed, grow, and lead bees.

### Bee nests
Oak, birch, and cherry trees grown from saplings that are within 2 blocks of a pitcher plant have a 5% chance to grow with a bee nest and 1-3 bees in it.

### Composting
Placing a pitcher plant into a composter has an 85% chance of raising the compost level by 1.

## Data values
### ID
Java Edition:

| Name          | Identifier    | Form         | Block tags          | Item tags           | Translation key               |
|---------------|---------------|--------------|---------------------|---------------------|-------------------------------|
| Pitcher Plant | pitcher_plant | Block & Item | flowerstall_flowers | flowerstall_flowers | block.minecraft.pitcher_plant |

Bedrock Edition:

| Name          | Identifier    | Numeric ID | Form                       | Item ID[i 1]   | Translation key         |
|---------------|---------------|------------|----------------------------|----------------|-------------------------|
| Pitcher Plant | pitcher_plant | -612       | Block & Giveable Item[i 2] | Identical[i 3] | tile.pitcher_plant.name |


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

| Name            | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                           |
|-----------------|---------------|---------------|----------------|-------------------------|---------------------------------------|
| upper_block_bit | Not Supported | false         | falsetrue      | Unsupported             | If it is the upper half of the plant. |




