# Potato Stem
A potato stem is a joke log-type block, added in 24w14potato.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
- 2 Usage
	- 2.1 Crafting ingredient
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues

## Obtaining
### Breaking
Potato stems can be broken using any tool, but an axe is the fastest. Additionally, swords speed up the breaking time.

| Block     | Potato Stem           |
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
| Sword     | 2                     |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
Potato stems generate naturally as part of potato trees, as well as in potato villages and potato mineshafts.

## Usage
### Crafting ingredient
| Name                | Ingredients            | Crafting recipe |
|---------------------|------------------------|-----------------|
| Potato Planks       | Potato Stem            | 4               |
| Potato Hanging Sign | Chain+<br/>Potato Stem |                 |

Potato stems can't be stripped or crafted into wood blocks.

## Data values
### ID
| Name        | Identifier    | Block tags                                                                                                                                         | Translation key               |
|-------------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
| Potato Stem | `potato_stem` | `parrots_spawnable_on`<br/>`completes_find_tree_tutorial`<br/>`logs`<br/>`mineable/axe`<br/>`sword_efficient`<br/>`lava_pool_stone_cannot_replace` | `block.minecraft.potato_stem` |

### Block states
See also: Block States

| Name | Default value | Allowed values | Description                              |
|------|---------------|----------------|------------------------------------------|
| axis | `y`           | `x`            | The potato stem is oriented east–west.   |
|      |               | `y`            | The potato stem is oriented vertically.  |
|      |               | `z`            | The potato stem is oriented north–south. |


