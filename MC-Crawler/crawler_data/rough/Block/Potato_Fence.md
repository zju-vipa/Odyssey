# Potato Fence
A potato fence is a potato variant of a fence, crafted from the respective potato planks.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
- 2 Usage
	- 2.1 Note blocks
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History

## Obtaining
### Breaking
Potato fences can be broken with anything, but axes are faster.

| Block     | Potato Fence          |
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

### Natural generation
Potato fences generate naturally as part of potato villages, potato mineshafts, and in fields biome.

### Crafting
| Ingredients              | Crafting recipe |
|--------------------------|-----------------|
| Potato Planks+<br/>Stick | 3               |

## Usage
For information about all fences, see Fence § Usage.

### Note blocks
Potato stairs can be placed under note blocks to produce "bass" sounds.

## Data values
### ID
| Name         | Identifier     | Block tags                                      | Translation key                |
|--------------|----------------|-------------------------------------------------|--------------------------------|
| Potato Fence | `potato_fence` | `mineable/axe`<br/>`wooden_fences`<br/>`fences` | `block.minecraft.potato_fence` |

### Block states
See also: Block states

| Name        | Default value | Allowed values     | Description                                                     |
|-------------|---------------|--------------------|-----------------------------------------------------------------|
| east        | `false`       | `false`<br/>`true` | When true, the fence extends from the center post to the east.  |
| north       | `false`       | `false`<br/>`true` | When true, the fence extends from the center post to the north. |
| south       | `false`       | `false`<br/>`true` | When true, the fence extends from the center post to the south. |
| waterlogged | `false`       | `false`<br/>`true` | Whether or not there's water in the same place as this fence.   |
| west        | `false`       | `false`<br/>`true` | When true, the fence extends from the center post to the west.  |

