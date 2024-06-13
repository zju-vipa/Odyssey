# Potato Fence Gate
A potato fence gate is a potato variant of a fence gate, crafted from the respective potato planks.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
- 2 Usage
	- 2.1 Note blocks
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History

## Obtaining
### Breaking
Potato fence gate can be broken with anything, but axes are faster.

| Block     | Potato Fence Gate     |
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
Potato fence gates generate naturally as part of potato villages.

### Crafting
| Ingredients              | Crafting recipe |
|--------------------------|-----------------|
| Stick+<br/>Potato Planks |                 |

## Usage
For information about the mechanics of all fence gates, see Fence Gate § Usage.

### Note blocks
Potato fence gatescan be placed under note blocks to produce "bass" sounds.

## Data values
### ID
| Name              | Identifier          | Block tags                                                    | Translation key                     |
|-------------------|---------------------|---------------------------------------------------------------|-------------------------------------|
| Potato Fence Gate | `potato_fence_gate` | `mineable/axe`<br/>`unstable_bottom_center`<br/>`fence_gates` | `block.minecraft.potato_fence_gate` |

### Block states
See also: Block states

| Name    | Default value | Allowed values                            | Description                                                                                                                                                                            |
|---------|---------------|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing  | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | For an open gate, the direction the gates swing open.<br/>For a closed gate, the direction the player was facing when the gate was placed, or the last direction the gates have swung. |
| in_wall | `false`       | `false`<br/>`true`                        | If true, the gate is lowered by three pixels, to accommodate attaching more cleanly withwalls.                                                                                         |
| open    | `false`       | `false`<br/>`true`                        | If true, the gate is opened.                                                                                                                                                           |
| powered | `false`       | `false`<br/>`true`                        | If true, the gate is receiving redstone power.                                                                                                                                         |


