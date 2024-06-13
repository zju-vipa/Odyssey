# Button
A button is a non-solid block that produces a temporary redstone signal when pressed.

## Contents
- 1 Variants
- 2 Obtaining
	- 2.1 Crafting
- 3 Usage
	- 3.1 Redstone power
		- 3.1.1 Placement
		- 3.1.2 Behavior
	- 3.2 Breaking
- 4 Data values
	- 4.1 Block states
- 5 Video
- 6 History
- 7 Gallery
	- 7.1 Renders

## Variants
- Wooden button
	- Oak Button
	- Birch Button
	- Spruce Button
	- Jungle Button
	- Acacia Button
	- Dark Oak Button
	- Mangrove Button
	- Cherry Button
	- Bamboo Button
	- Crimson Button
	- Warped Button
- Stone Button
- Polished Blackstone Button
- Potato Button- April Fool's variant

## Obtaining
### Crafting
The crafting recipe is the same for all types and variants of buttons, using a single matching plank, stone, or polished blackstone block to craft the matching button.

| Name                                          | Ingredients                     | Crafting recipe |
|-----------------------------------------------|---------------------------------|-----------------|
| Wooden button                                 | MatchingPlanks                  |                 |
| Stone Buttonor<br/>Polished Blackstone Button | Stoneor<br/>Polished Blackstone |                 |

## Usage
For more specific usage, see the individual button pages.
### Redstone power
See also: Redstone circuit

A button can be used as a monostable power source (it automatically deactivates shortly after being activated).
A stone button stays ON for 10 ticks (1 second), while a wooden button stays ON for 15 ticks (1.5 seconds).

#### Placement
Buttons can be placed by using it on a surface.

They can be attached to the side, bottom and top of any full opaque block.

#### Behavior
Buttons are usually in an inactive state, but can be temporarily activated by players. A button can be activated by using it.

While active, a button:

- powers any adjacentredstone dusttopower level15, including beneath the button
- powers any adjacentredstone comparatorsorredstone repeatersfacing away from the button to power level 15
- strongly powers its attachment block to power level 15
- activates any adjacentmechanism components, including above or below, such aspistons,redstone lamps, etc.

When a button changes state it provides a redstone update to all redstone components adjacent to itself (including above and below), and to all redstone components adjacent to its attachment block.

### Breaking
A button is removed and drops as an item if:

- its attachment block is moved, removed, or destroyed.
- waterorlavaflows into its space.‌[Java Edition  only]
- apistontries to push it or moves a block into its space.

## Data values
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




