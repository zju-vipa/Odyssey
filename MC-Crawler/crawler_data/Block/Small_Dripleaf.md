# Small Dripleaf
A  small dripleaf is a plant which generates in lush caves, and is used to grow big dripleaves, a platforming block.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Trading
- 2 Usage
	- 2.1 Placement
	- 2.2 Bone meal
	- 2.3 Composting
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Gallery
	- 7.1 Screenshots
	- 7.2 Concept artwork

## Obtaining
### Breaking
A small dripleaf can be obtained by mining it using shears. A small dripleaf drops nothing when mined using any other tool, pushed with a piston or sticky piston, or broken by destroying or moving the block under it. It breaks instantly in all cases.

| Block    | Small Dripleaf      |
|----------|---------------------|
| Hardness | 0                   |
|          | Breakingtime (secs) |
| Default  | 0.05                |
| Shears   | 0.05                |

### Natural generation
Small dripleaves naturally generate within the lush caves biome.


### Trading
Small dripleaves can be obtained by trading with a wandering trader, who sometimes may sell 2 small dripleaves for 1 emerald. Note that small dripleaves cannot be farmed as such:  Bone meal converts them to a big dripleaf, which can be grown/duplicated with bone meal, but that does not produce small dripleaves.

## Usage
### Placement
Small dripleaf can be placed on top of clay and moss blocks. They can also be placed on dirt, coarse dirt, farmland, grass blocks, podzol, rooted dirt, mycelium, and mud if these blocks are underwater.

### Bone meal
Using bone meal on a small dripleaf causes it to grow into a big dripleaf, from two to five blocks tall. The small dripleaf is consumed in the process, and cannot be retrieved.

Small dripleaves do not grow on their own.

### Composting
Small dripleaves can be placed into a composter, with a 30% chance to increase its compost level.

## Data values
### ID
Java Edition:

| Name           | Identifier     | Form         | Block tags                                    | Translation key                |
|----------------|----------------|--------------|-----------------------------------------------|--------------------------------|
| Small Dripleaf | small_dripleaf | Block & Item | lush_plants_replaceableazalea_log_replaceable | block.minecraft.small_dripleaf |

Bedrock Edition:

| Name           | Identifier           | Numeric ID | Form                       | Item ID[i 1]   | Translation key                |
|----------------|----------------------|------------|----------------------------|----------------|--------------------------------|
| Small Dripleaf | small_dripleaf_block | 591        | Block & Giveable Item[i 2] | Identical[i 3] | tile.small_dripleaf_block.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block states

Java Edition:

| Name        | Default value | Allowed values     | Description                                                                                                                   |
|-------------|---------------|--------------------|-------------------------------------------------------------------------------------------------------------------------------|
| facing      | north         | eastnorthsouthwest | The direction the small dripleaf is facing.The opposite from the direction the player faces while placing the small dripleaf. |
| half        | lower         | lowerupper         | What half of the small dripleaf this block is.                                                                                |
| waterlogged | false         | falsetrue          | Whether or not there's water in the same place as this small dripleaf.                                                        |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values     | Values forMetadata Bits | Description                                                                                                                   |
|------------------------------|---------------|---------------|--------------------|-------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| minecraft:cardinal_direction | Not Supported | south         | eastnorthsouthwest | Unsupported             | The direction the small dripleaf is facing.The opposite from the direction the player faces while placing the small dripleaf. |
| upper_block_bit              | Not Supported | true          | falsetrue          | Unsupported             | What half of the small dripleaf this block is.                                                                                |



