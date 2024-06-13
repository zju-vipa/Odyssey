# Border
Border blocks are unbreakable blocks that prohibit movement through, over or under them. They are exclusive to Minecraft Education and Bedrock Edition.[1]

## Contents
- 1 Obtaining
- 2 Usage
	- 2.1 Piston interactivity
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Trivia
- 7 Gallery
	- 7.1 Screenshots
- 8 References

## Obtaining
Border blocks can be obtained only by using commands, or using pick block in Creative mode. No tool or explosion can damage them (they act as if they have no collision box when you try).

## Usage
Border blocks are generally used to surround an area to prevent students (or players) and mobs from entering it, or to confine them within the surrounded area. They create an invisible, impassable barrier of infinite height above and below themselves (but not sideways). They prevent players who lack the worldbuilder ability from doing any of the following:

- Jumping, climbing, tunneling, or swimming over or under them,
- Walking through them,
- Building (placing or destroying blocks) over or under them,
- Destroying the border block.

Most mobs cannot pass over or under border blocks and cannot target a player or other mob through them. However, they do not stop the Ender Dragon. Weapons, projectiles, and explosions interact with them as if they were regular walls. Because of this, it is possible to use an ender pearl to cross one.

Placing or breaking a border block requires the worldbuilder or operator‌[Bedrock Edition  only] ability, which can be granted to the player by an operator or host.
Border blocks continuously emit red particles.

When used in Bedrock Edition without Education Edition features enabled, border blocks are indestructible, with a height of 1.5 blocks and a width of 1 block.

### Piston interactivity
Border cannot be pushed by pistons. It also cannot be pushed nor pulled by sticky pistons.

## Data values
### ID
| Name   | Identifier   | Numeric ID | Form                       | Item ID[i 1]   | Translation key        |
|--------|--------------|------------|----------------------------|----------------|------------------------|
| Border | border_block | 212        | Block & Giveable Item[i 2] | Identical[i 3] | tile.border_block.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


### Block states
Bedrock Edition and Minecraft Education:

| Name                       | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                             |
|----------------------------|---------------|---------------|----------------|-------------------------|---------------------------------------------------------|
| wall_connection_type_east  | Not Supported | none          | noneshorttall  | Unsupported             | How the wall extends from the center post to the east.  |
| wall_connection_type_north | Not Supported | none          | noneshorttall  | Unsupported             | How the wall extends from the center post to the north. |
| wall_connection_type_south | Not Supported | none          | noneshorttall  | Unsupported             | How the wall extends from the center post to the south. |
| wall_connection_type_west  | Not Supported | none          | noneshorttall  | Unsupported             | How the wall extends from the center post to the west.  |
| wall_post_bit              | Not Supported | true          | falsetrue      | Unsupported             | Whether or not the wall has a center post.              |



