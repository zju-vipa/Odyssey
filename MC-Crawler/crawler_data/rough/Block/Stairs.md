# Stairs
Stairs are blocks that allow mobs and players to change elevation without jumping.

## Contents
- 1 Variants
- 2 Obtaining
	- 2.1 Crafting
	- 2.2 Stonecutting
- 3 Usage
	- 3.1 Placement
	- 3.2 Walking
	- 3.3 Behavior
- 4 Block states
- 5 History
- 6 Issues
- 7 Trivia
- 8 References

## Variants
There are 53 (56‌[upcoming: JE 1.21 & BE 1.21.0]) variants of stairs:

- Wooden Stairs
	- Oak Stairs
	- Spruce Stairs
	- Birch Stairs
	- Jungle Stairs
	- Acacia Stairs
	- Dark Oak Stairs
	- Mangrove Stairs
	- Cherry Stairs
	- Bamboo Stairs
	- Crimson Stairs
	- Warped Stairs
- Bamboo Mosaic Stairs
- Stone Stairs
- Cobblestone Stairs
- Mossy Cobblestone Stairs
- Stone Brick Stairs
- Mossy Stone Brick Stairs
- Granite Stairs
- Polished Granite Stairs
- Diorite Stairs
- Polished Diorite Stairs
- Andesite Stairs
- Polished Andesite Stairs
- Cobbled Deepslate Stairs
- Polished Deepslate Stairs
- Deepslate Brick Stairs
- Deepslate Tile Stairs
- Tuff Stairs‌[upcoming: JE 1.21 & BE 1.21.0]
- Polished Tuff Stairs‌[upcoming: JE 1.21 & BE 1.21.0]
- Tuff Brick Stairs‌[upcoming: JE 1.21 & BE 1.21.0]
- Brick Stairs
- Mud Brick Stairs
- Sandstone Stairs
- Smooth Sandstone Stairs
- Red Sandstone Stairs
- Smooth Red Sandstone Stairs
- Prismarine Stairs
- Prismarine Brick Stairs
- Dark Prismarine Stairs
- Nether Brick Stairs
- Red Nether Brick Stairs
- Blackstone Stairs
- Polished Blackstone Stairs
- Polished Blackstone Brick Stairs
- End Stone Brick Stairs
- Purpur Stairs
- Quartz Stairs
- Smooth Quartz Stairs
- Cut Copper Stairs
	- Unoxidized Cut Copper Stairs(Waxed)
	- Exposed Cut Copper Stairs(Waxed)
	- Weathered Cut Copper Stairs(Waxed)
	- Oxidized Cut Copper Stairs(Waxed)

## Obtaining
### Crafting
All stairs have the same crafting recipe format, where six blocks result in four stairs of the same type.

| Ingredients                                                                                            | Crafting recipe                                          |
|--------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| Planks,Bamboo Mosaic,<br/>stone blocks, brick blocks,<br/>Quartz Block,Smooth Quartz,<br/>orCut Copper | 44444444444444444444444444444444444444444444444444444444 |

### Stonecutting
All stairs except wooden stairs and bamboo mosaic stairs can be obtained by stonecutting. This is more efficient than crafting them, since each block directly results in one stair of the same type.

| Ingredients                                                                | Cutting recipe |
|----------------------------------------------------------------------------|----------------|
| Stone block, brick block,<br/>Quartz Block,Smooth Quartz,<br/>orCut Copper |                |

## Usage
### Placement
Stairs Reconfiguration — Left: Original facing when separate. Right: Changed shape when adjacent (top: inner corner; bottom: outer corner).
To place stairs, use a stairs item while pointing at a surface facing the space the stairs should occupy. When placed, a stair orients itself with the half-block side closest to the player.

Stairs can be placed either right side up or upside-down:

- Pointing at ablocktop or the bottom half of a block side places the stairs right side up.
- Pointing at a block bottom or the top half of a block side places the stairs upside-down.

Stairs change their shape to join with adjacent stairs (of any material):

- When a stairs' half-block side is adjacent to the side of another stairs, the stairs' full-block side wraps into an "L" shape to join the other stairs (it creates an "inner corner").
- When a stairs' full-block side is adjacent to the side of another stairs, the stairs' full-block side shortens to join the other stairs' full-block side (it creates an "outer corner").

Right side up stairs do not join with upside-down stairs and vice versa.

### Walking
Walking up stairs is faster than jumping up the same distance. Walking up a stairway doesn't cost any exhaustion from the player's hunger bar, compared to 0.2 exhaustion per jump. Therefore, walking up stairs doesn't make the player hungry at all.

### Behavior
Generally, the solid faces of stairs are handled as solid blocks. Due to this, transparent blocks that need to placed on an opaque surface can be placed on these faces.

## Block states
See also: Block states

Java Edition:

| Name        | Default value | Allowed values                                                                   | Description                                                                                                                                                                                                                                                                                                                        |
|-------------|---------------|----------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing      | `north`       | `east`<br/>`north`<br/>`south`<br/>`west`                                        | The direction the stairs' full-block side faces.<br/>When placed in-game by a player, this matches the direction the player faces.                                                                                                                                                                                                 |
| half        | `bottom`      | `bottom`<br/>`top`                                                               | Top if the stairs are upside-down.                                                                                                                                                                                                                                                                                                 |
| shape       | `straight`    | `inner_left`<br/>`inner_right`<br/>`outer_left`<br/>`outer_right`<br/>`straight` | "straight" is the default stairs shape.<br/>"inner" is an "inside corner" stair shape, with two full-block and two stair-shaped side faces.<br/>"outer" is an "outside corner" stair shape, with two stair-shaped and two half-block side faces.<br/>"left" and "right" specify in which direction is the higher part of the step. |
| waterlogged | `false`       | `false`<br/>`true`                                                               | Whether or not there's water in the same place as these stairs.                                                                                                                                                                                                                                                                    |

Bedrock Edition:

| Name             | Metadata Bits   | Default value | Allowed values              | Values forMetadata Bits     | Description                                                                                        |
|------------------|-----------------|---------------|-----------------------------|-----------------------------|----------------------------------------------------------------------------------------------------|
| upside_down_bit  | `0x4`           | `false`       | `false`<br/>`true`          | `0`<br/>`1`                 | True if the stairs are upside-down.                                                                |
| weirdo_direction | `0x1`<br/>`0x2` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3` | `0`<br/>`1`<br/>`2`<br/>`3` | The direction the stairs' full-block side faces.0: East<br/>1: West<br/>2: South<br/>3: North<br/> |

