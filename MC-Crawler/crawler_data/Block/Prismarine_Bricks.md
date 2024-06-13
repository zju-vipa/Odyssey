# Prismarine Bricks
Prismarine bricks are a variant of prismarine, appearing as cyan bricks with chiseled patterns. 

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
- 2 Usage
	- 2.1 Conduit power
	- 2.2 Crafting ingredient
	- 2.3 Stonecutting
	- 2.4 Note Blocks
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 Achievements
- 6 History
- 7 Issues
- 8 Trivia
- 9 References

## Obtaining
### Breaking
Prismarine bricks only drops itself when mined with a pickaxe. If mined by any other tool, it drops nothing.

| Block     | Prismarine Bricks     |
|-----------|-----------------------|
| Hardness  | 1.5                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 7.5                   |
| Wooden    | 1.15                  |
| Stone     | 0.6                   |
| Iron      | 0.4                   |
| Diamond   | 0.3                   |
| Netherite | 0.25                  |
| Golden    | 0.2                   |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


### Natural generation
Prismarine bricks naturally generate as the main blocks making up ocean monuments. Prismarine bricks are found in large amounts due to the size of the structure. Prismarine bricks make up the 23 pillars below the monument, and appear decoratively throughout the structure.

### Crafting
| Ingredients      | Crafting recipe |
|------------------|-----------------|
| Prismarine Shard |                 |

## Usage
### Conduit power
Main article: Conduit
Prismarine bricks can be used to activate a conduit by building a structure around it. By doing this, the conduit emits the "Conduit Power" effect in a certain radius, depending on how many blocks are used to power it. Sea lanterns can also be used for this purpose.

### Crafting ingredient
| Name                    | Ingredients       | Crafting recipe |
|-------------------------|-------------------|-----------------|
| Prismarine Brick Slab   | Prismarine Bricks | 6               |
| Prismarine Brick Stairs | Prismarine Bricks | 4               |

### Stonecutting
| Name                    | Ingredients       | Cutting recipe |
|-------------------------|-------------------|----------------|
| Prismarine Brick Slab   | Prismarine Bricks | 2              |
| Prismarine Brick Stairs | Prismarine Bricks |                |

### Note Blocks
Prismarine bricks can be placed under note blocks to produce "bass drum" sound.

## Data values
### ID
Java Edition:

| Name              | Identifier        | Form         | Translation key                   |
|-------------------|-------------------|--------------|-----------------------------------|
| Prismarine Bricks | prismarine_bricks | Block & Item | block.minecraft.prismarine_bricks |

Bedrock Edition:

| Name              | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key             |
|-------------------|------------|------------|----------------------------|----------------|-----------------------------|
| Prismarine Bricks | prismarine | 168        | Block & Giveable Item[i 2] | Identical[i 3] | tile.prismarine.bricks.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block states

Bedrock Edition:

| Name                  | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description       |
|-----------------------|---------------|---------------|----------------|-------------------------|-------------------|
| prismarine_block_type | 0x10x2        | default       | bricks         | 2                       | Prismarine Bricks |
|                       |               |               | dark           | 1                       | Dark Prismarine   |
|                       |               |               | default        | 0                       | Prismarine        |



