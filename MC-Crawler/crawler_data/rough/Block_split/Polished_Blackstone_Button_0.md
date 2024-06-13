# Polished Blackstone Button
A polished blackstone button is a variant of the button that shares many common properties with stone buttons. Like stone buttons, a polished blackstone button is a non-solid block that produces a temporary redstone signal when pressed.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Crafting
- 2 Usage
	- 2.1 Placement
	- 2.2 Redstone power
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History

## Obtaining
### Breaking
Polished blackstone buttons can be mined using any pickaxe.

| Block     | Polished Blackstone Button |
|-----------|----------------------------|
| Hardness  | 0.5                        |
| Tool      |                            |
|           | Breakingtime (sec)[A]      |
| Default   | 2.5                        |
| Wooden    | 0.4                        |
| Stone     | 0.2                        |
| Iron      | 0.15                       |
| Diamond   | 0.1                        |
| Netherite | 0.1                        |
| Golden    | 0.1                        |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

A button is removed and drops as an item if:

- its attachment block is moved, removed, or destroyed.
- waterorlavaflows into its space.‌[Java Edition  only]
- apistontries to push it or moves a block into its space.

### Crafting
| Ingredients         | Crafting recipe |
|---------------------|-----------------|
| Polished Blackstone |                 |

## Usage
See also: Redstone circuit

### Placement
Buttons can be placed by using it on a surface.

They can be attached to the side, bottom and top of any full opaque block.

If placed on the top or bottom of a block, the button can face any direction.‌[Java Edition  only]

It can also be attached to the top of a fence in Bedrock Edition.

More information about placement on transparent blocks can be found at Opacity/Placement.

### Redstone power
A button can be used as a monostable redstone power source (it automatically deactivates shortly after being activated).

Buttons are usually in an inactive state, but can be temporarily activated by players. A polished blackstone button can be activated by a player using it. Mobs cannot activate buttons directly.

When activated, a polished blackstone button remains active for exactly 1 second (10 redstone ticks; 20 game ticks).

While active, a button:

- powers any adjacentredstone dusttopower level15, including beneath the button
- powers any adjacentredstone comparatorsorredstone repeatersfacing away from the button to power level 15
- strongly powers its attachment block to power level 15
- activates any adjacentmechanism components, including above or below, such aspistons,redstone lamps, etc.

When a button changes state it provides a redstone update to all redstone components adjacent to itself (including above and below), and to all redstone components adjacent to its attachment block.

## Data values
### ID
Java Edition:

| Name                       | Identifier                   | Form         | Block tags | Item tags | Translation key                              |
|----------------------------|------------------------------|--------------|------------|-----------|----------------------------------------------|
| Polished Blackstone Button | `polished_blackstone_button` | Block & Item | `buttons`  | `buttons` | `block.minecraft.polished_blackstone_button` |

Bedrock Edition:

| Name                       | Identifier                   | Numeric ID | Form                       | Item ID[i 1]   | Translation key                        |
|----------------------------|------------------------------|------------|----------------------------|----------------|----------------------------------------|
| Polished Blackstone Button | `polished_blackstone_button` | `551`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.polished_blackstone_button.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:

| Name    | Default value | Allowed values                            | Description                                                                                                                      |
|---------|---------------|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| face    | `wall`        | `ceiling`<br/>`floor`<br/>`wall`          | The face of the block it's placed on.<br/>Floor is on top of a block, ceiling is on the bottom, and wall is on one of its sides. |
| facing  | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction it's facing.<br/>Opposite to the direction the player is facing if placed on the side of a block.                  |
| powered | `false`       | `false`<br/>`true`                        | If true, the button is currently activated.                                                                                      |

Bedrock Edition:

| Name               | Metadata Bits             | Default value | Allowed values                              | Values forMetadata Bits                     | Description                                                                                                                                                                                                                                                                 |
|--------------------|---------------------------|---------------|---------------------------------------------|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| button_pressed_bit | `0x8`                     | `false`       | `false`<br/>`true`                          | `0`<br/>`1`                                 | If the button is currently activated.                                                                                                                                                                                                                                       |
| facing_direction   | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | The direction it's facing.0: Button on block bottom facing down<br/>1: Button on block top facing up<br/>2: Button on block side facing north<br/>3: Button on block side facing south<br/>4: Button on block side facing west<br/>5: Button on block side facing east<br/> |




