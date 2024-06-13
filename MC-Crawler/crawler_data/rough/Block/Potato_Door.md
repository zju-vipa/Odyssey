# Potato Door
A potato door is a variant of the door made of potato planks that can be opened and closed by the player without redstone.

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
Potato doors can be broken with anything, but axes are faster. Potato doors drop themselves if they no longer have a block beneath them that can support them.

| Block     | Potato Door           |
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
Potato doors generate naturally as part of potato villages.

### Crafting
| Ingredients   | Crafting recipe |
|---------------|-----------------|
| Potato Planks | 3               |

## Usage
For information about all doors, see Door § Usage.

### Note blocks
Potato doors can be placed under note blocks to produce "bass" sounds.

## Data values
### ID
| Name        | Identifier    | Block tags                                    | Translation key               |
|-------------|---------------|-----------------------------------------------|-------------------------------|
| Potato Door | `potato_door` | `doors`<br/>`mineable/axe`<br/>`wooden_doors` | `block.minecraft.potato_door` |

### Block states
See also: Block states

| Name    | Default value | Allowed values                            | Description                                                                                                                                                                                  |
|---------|---------------|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing  | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the door's "inside" is facing.<br/>The direction the player faces while placing the door.<br/>For example, a door facing east occupies the west part of its block when closed. |
| half    | `lower`       | `lower`<br/>`upper`                       | Identifies which part of the door the block is.                                                                                                                                              |
| hinge   | `left`        | `left`<br/>`right`                        | Identifies the side the hinge is on (when facing the same direction as the door's inside).                                                                                                   |
| open    | `false`       | `false`<br/>`true`                        | True if the door is currently open.                                                                                                                                                          |
| powered | `false`       | `false`<br/>`true`                        | True if the door is currently powered by redstone.                                                                                                                                           |

