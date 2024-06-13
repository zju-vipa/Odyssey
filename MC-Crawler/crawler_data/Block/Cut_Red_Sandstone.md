# Cut Red Sandstone
Cut red sandstone is a variant of red sandstone, obtained through crafting.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Crafting
	- 1.3 Stonecutting
- 2 Usage
	- 2.1 Crafting ingredient
	- 2.2 Stonecutting
	- 2.3 Note blocks
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
	- 5.1 Data history
- 6 Issues
- 7 References

## Obtaining
### Breaking
Cut red sandstone can be mined with any pickaxe. If mined without a pickaxe, the block drops nothing.

| Block     | Cut Red Sandstone     |
|-----------|-----------------------|
| Hardness  | 0.8                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 4                     |
| Wooden    | 0.6                   |
| Stone     | 0.3                   |
| Iron      | 0.2                   |
| Diamond   | 0.15                  |
| Netherite | 0.15                  |
| Golden    | 0.1                   |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


### Crafting
| Ingredients   | Crafting recipe |
|---------------|-----------------|
| Red Sandstone | 4               |

### Stonecutting
| Ingredients   | Cutting recipe |
|---------------|----------------|
| Red Sandstone |                |

## Usage
Unlike red sand, cut red sandstone is never affected by gravity.

### Crafting ingredient
| Name                   | Ingredients       | Crafting recipe |
|------------------------|-------------------|-----------------|
| Cut Red Sandstone Slab | Cut Red Sandstone | 6               |

### Stonecutting
| Ingredients       | Cutting recipe |
|-------------------|----------------|
| Cut Red Sandstone | 2              |

### Note blocks
Cut red sandstone can be placed under note blocks to produce "bass drum" sounds.

## Data values
### ID
Java Edition:

| Name              | Identifier        | Form         | Translation key                   |
|-------------------|-------------------|--------------|-----------------------------------|
| Cut Red Sandstone | cut_red_sandstone | Block & Item | block.minecraft.cut_red_sandstone |

Bedrock Edition:

| Name              | Identifier    | Numeric ID | Form                       | Item ID[i 1]   | Translation key             |
|-------------------|---------------|------------|----------------------------|----------------|-----------------------------|
| Cut Red Sandstone | red_sandstone | 179        | Block & Giveable Item[i 2] | Identical[i 3] | tile.red_sandstone.cut.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block states

In Bedrock Edition, cut red sandstone use the following block states:

Bedrock Edition:

| Name            | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description        |
|-----------------|---------------|---------------|----------------|-------------------------|--------------------|
| sand_stone_type | 0x10x2        | default       | default        | 0                       | Sandstone          |
|                 |               |               | heiroglyphs    | 1                       | Chiseled Sandstone |
|                 |               |               | cut            | 2                       | Cut Sandstone      |
|                 |               |               | smooth         | 3                       | Smooth Sandstone   |



