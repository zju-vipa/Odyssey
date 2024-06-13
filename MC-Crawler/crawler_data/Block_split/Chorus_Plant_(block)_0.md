# Chorus Plant
Chorus plants are blocks that naturally generate on the outer islands of the End. They can be grown using chorus flowers.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Post-generation
- 2 Usage
	- 2.1 Support
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Trivia
- 8 Gallery
	- 8.1 Screenshots
- 9 References

## Obtaining
The block form cannot be obtained in Survival mode, even with the Silk Touch enchantment; however, it is available in the Creative inventory.

### Breaking
Chorus plants can be broken using any tool, but an axe is the quickest. Breaking one block of a chorus tree generally causes all chorus plants and flowers above to break due to lack of support. Upon breaking, a chorus plant drops 0–1 chorus fruit. This is not affected by Fortune.[1]

| Block     | Chorus Plant          |
|-----------|-----------------------|
| Hardness  | 0.4                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 0.6                   |
| Wooden    | 0.3                   |
| Stone     | 0.15                  |
| Iron      | 0.1                   |
| Diamond   | 0.1                   |
| Netherite | 0.1                   |
| Golden    | 0.05                  |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


### Natural generation
Chorus plants make up most of the chorus trees that are naturally generated on the outer islands of the End. Chorus trees are typically 10–15 blocks in height, although a single plant can reach up to 22 blocks.


### Post-generation
Chorus plants are generated as chorus flowers grow.

## Usage
Chorus plants can be broken to obtain chorus fruit.

### Support
Chorus plant blocks break automatically (potentially dropping fruit), if the six surrounding blocks are not valid:

- a chorus plant with at least one other chorus plant horizontally adjacent breaks unless at least one of the vertically adjacent blocks is air
- a chorus plant breaks unless the block below is chorus plant orend stoneor any horizontally adjacent block is a chorus plant above chorus plant or end stone

## Data values
### ID
Java Edition:

| Name         | Identifier   | Form         | Translation key              |
|--------------|--------------|--------------|------------------------------|
| Chorus Plant | chorus_plant | Block & Item | block.minecraft.chorus_plant |

Bedrock Edition:

| Name         | Identifier   | Numeric ID | Form                       | Item ID[i 1]   | Translation key        |
|--------------|--------------|------------|----------------------------|----------------|------------------------|
| Chorus Plant | chorus_plant | 240        | Block & Giveable Item[i 2] | Identical[i 3] | tile.chorus_plant.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block states

Java Edition:

| Name  | Default value | Allowed values | Description                                                                       |
|-------|---------------|----------------|-----------------------------------------------------------------------------------|
| down  | false         | falsetrue      | When true, the plant extends out from the center of the plant-block down.         |
| east  | false         | falsetrue      | When true, the plant extends out from the center of the plant-block to the east.  |
| north | false         | falsetrue      | When true, the plant extends out from the center of the plant-block to the north. |
| south | false         | falsetrue      | When true, the plant extends out from the center of the plant-block to the south. |
| up    | false         | falsetrue      | When true, the plant extends out from the center of the plant-block up.           |
| west  | false         | falsetrue      | When true, the plant extends out from the center of the plant-block to the west.  |




