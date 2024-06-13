# Potato Stairs
Potato stairs are a potato variant of wooden stairs, crafted from the respective potato planks in 24w14potato.

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
Potato stairs can be broken using anything, but an axe is the fastest.

| Block     | Potato Stairs         |
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
Potato stairs generate naturally as part of potato villages.

### Crafting
| Ingredients   | Crafting recipe |
|---------------|-----------------|
| Potato Planks | 4               |

## Usage
For information about the placement mechanics of all stairs, see Stairs § Usage.

### Note blocks
Potato stairs can be placed under note blocks to produce "bass" sounds.

## Data values
### ID
| Name          | Identifier      | Block tags                                      | Translation key                 |
|---------------|-----------------|-------------------------------------------------|---------------------------------|
| Potato Stairs | `potato_stairs` | `stairs`<br/>`wooden_stairs`<br/>`mineable/axe` | `block.minecraft.potato_stairs` |

### Block states
See also: Block states

| Name        | Default value | Allowed values                                                                   | Description                                                                                                                                                                                                                                                                                                                        |
|-------------|---------------|----------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing      | `north`       | `east`<br/>`north`<br/>`south`<br/>`west`                                        | The direction the stairs' full-block side faces.<br/>When placed in-game by a player, this matches the direction the player faces.                                                                                                                                                                                                 |
| half        | `bottom`      | `bottom`<br/>`top`                                                               | Top if the stairs are upside-down.                                                                                                                                                                                                                                                                                                 |
| shape       | `straight`    | `inner_left`<br/>`inner_right`<br/>`outer_left`<br/>`outer_right`<br/>`straight` | "straight" is the default stairs shape.<br/>"inner" is an "inside corner" stair shape, with two full-block and two stair-shaped side faces.<br/>"outer" is an "outside corner" stair shape, with two stair-shaped and two half-block side faces.<br/>"left" and "right" specify in which direction is the higher part of the step. |
| waterlogged | `false`       | `false`<br/>`true`                                                               | Whether or not there's water in the same place as these stairs.                                                                                                                                                                                                                                                                    |

