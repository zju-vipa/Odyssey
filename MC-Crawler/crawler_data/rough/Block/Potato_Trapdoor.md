# Potato Trapdoor
A potato trapdoor is a variant of a trapdoor made of potato planks in 24w14potato.

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
| Block     | Potato Trapdoor       |
|-----------|-----------------------|
| Hardness  | 3                     |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 4.5                   |
| Wooden    | 2.25                  |
| Stone     | 1.15                  |
| Iron      | 0.75                  |
| Diamond   | 0.6                   |
| Netherite | 0.5                   |
| Golden    | 0.4                   |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
Potato trapdoors generate naturally as part of potato villages.

Two potato trapdoors generate in every colosseum, one at each end of the maze beneath the arena.

### Crafting
| Ingredients   | Crafting recipe |
|---------------|-----------------|
| Potato Planks | 2               |

## Usage
For information mechanics of all trapdoors, see Trapdoor § Usage.

### Note blocks
Potato trapdoors can be placed under note blocks to produce "bass" sounds.

## Data values
### ID
| Name            | Identifier        | Block tags                                            | Translation key                   |
|-----------------|-------------------|-------------------------------------------------------|-----------------------------------|
| Potato Trapdoor | `potato_trapdoor` | `mineable/axe`<br/>`trapdoors`<br/>`wooden_trapdoors` | `block.minecraft.potato_trapdoor` |

### Block states
See also: Block states

| Name        | Default value | Allowed values                            | Description                                                                                      |
|-------------|---------------|-------------------------------------------|--------------------------------------------------------------------------------------------------|
| facing      | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the trapdoor swings open.<br/>The opposite from the side its hinge is attached to. |
| half        | `bottom`      | `bottom`<br/>`top`                        | Whether the trapdoor occupies the top or bottom part of a block.                                 |
| open        | `false`       | `false`<br/>`true`                        | True if the trapdoor is currently open (may differ from`powered`).                               |
| powered     | `false`       | `false`<br/>`true`                        | True if the trapdoor is currently powered (may differ from`open`).                               |
| waterlogged | `false`       | `false`<br/>`true`                        | Whether or not there's water in the same place as this trapdoor.                                 |

