# Potato Slab
A potato slab is a potato variant of a wooden slab crafted from the respective potato planks in 24w14potato.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Crafting
- 2 Usage
	- 2.1 Crafting ingredient
	- 2.2 Note blocks
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History

## Obtaining
### Breaking
A potato slab can be broken using anything, but an axe is the fastest.

| Block     | Potato Slab           |
|-----------|-----------------------|
| Hardness  | 2                     |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 3                     |
| Wooden    | 1.5                   |
| Stone     | 0.75                  |
| Iron      | 0.5                   |
| Diamond   | 0.4                   |
| Netherite | 0.35                  |
| Golden    | 0.25                  |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Crafting
| Ingredients   | Crafting recipe |
|---------------|-----------------|
| Potato Planks | 6               |

## Usage
For information about the placement mechanics of all slabs, see Slab § Usage.

### Crafting ingredient
| Name               | Ingredients                               | Crafting recipe |
|--------------------|-------------------------------------------|-----------------|
| Composter          | Potato Slab                               |                 |
| Barrel             | Potato Planks+<br/>Potato Slab            |                 |
| Chiseled Bookshelf | Potato Planks+<br/>Potato Slab            |                 |
| Daylight Detector  | Glass+<br/>Nether Quartz+<br/>Potato Slab |                 |
| Lectern            | Potato Slab+<br/>Bookshelf                |                 |

### Note blocks
Potato stairs can be placed under note blocks to produce "bass" sounds.

## Data values
### ID
| Name        | Identifier    | Block tags                                    | Translation key               |
|-------------|---------------|-----------------------------------------------|-------------------------------|
| Potato Slab | `potato_slab` | `slabs`<br/>`mineable/axe`<br/>`wooden_slabs` | `block.minecraft.potato_slab` |

### Block states
See also: Block states

| Name        | Default value | Allowed values     | Description                                                  |
|-------------|---------------|--------------------|--------------------------------------------------------------|
| type        | `bottom`      | `bottom`<br/>`top` | Where the slab is within its block.                          |
|             |               | `double`           | The block is a double slab.                                  |
| waterlogged | `false`       | `false`<br/>`true` | Whether or not there's water in the same place as this slab. |


