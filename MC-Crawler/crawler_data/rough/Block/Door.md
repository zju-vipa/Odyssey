# Door
A door is a block that serves as a switchable barrier to entity movement.

## Contents
- 1 Variants
- 2 Usage
	- 2.1 Placement
		- 2.1.1 Facing direction
		- 2.1.2 Hinge placement
	- 2.2 Behavior
	- 2.3 Barrier
- 3 Block states
- 4 History
- 5 References

## Variants
- Wooden Door
	- Oak Door
	- Spruce Door
	- Birch Door
	- Jungle Door
	- Acacia Door
	- Dark Oak Door
	- Mangrove Door
	- Cherry Door
	- Bamboo Door
	- Crimson Door
	- Warped Door
- Iron Door
- Copper Door‌[upcoming: JE 1.21 & BE 1.21.0]
	- Unoxidized Copper Door(Waxed)
	- Exposed Copper Door(Waxed)
	- Weathered Copper Door(Waxed)
	- Oxidized Copper Door(Waxed)

## Usage
### Placement
Doors must be supported by a full solid block face beneath them. The bottom half of the door is placed where the player is aiming, with the top half extending one block above. If there is not enough space for the door, or not an appropriate supporting block underneath the base, no action is performed.

#### Facing direction
When placed, a door occupies the side of the block closest to the player, or behind the player if placed in the player's own space.

#### Hinge placement
When placed, a door checks the blocks to its immediate left and right and uses the following rules to determine hinge placement:

- If another matching door is adjacent, with its handle side touching the newly placed door, a double door forms. This causes the new door to have its handle touching the existing doors handle, with hinges opposite.
- If there is no other other matching door present, the hinge is placed the side with the highest number of adjacent solid block faces.
- If there are no blocks adjacent, or both sides fulfill a single other rule, the hinge is placed on the side closest to the players aim.

### Behavior
Water and lava flow around doors. 

Mobs can spawn in a space occupied by a door.

The sound of opening and closing of a door can be heard up to 16 blocks away, like most mob sounds.

When placed using the /setblock command, only one half of a door is placed, because doors are actually two separate blocks. The lower half still works, but with graphical bugs, and the upper half does not. Redstone cannot be used because it updates the half, breaking it. The upper half does not drop anything when broken, the lower half drops a normal door. This implies that the upper half is dependent on the lower.

### Barrier
A door can be used as a switchable barrier to entity movement. Although primarily used to block movement by mobs and players, a door can also be used to control the movement of boats (for example, a door placed in a two-wide water flow stops a boat when perpendicular to the flow, but allow it to move again when parallel), items and minecarts (a door can stop a falling item or minecart, then allow it to drop again when the door moves), etc.

In Java Edition, doors provide a breathable space if placed underwater. In Bedrock Edition, doors in water source blocks are waterlogged and do not displace water source blocks.

Doors are 0.1875 (3⁄16) blocks thick (0.1825 in Bedrock Edition). The rest of a door's space can be moved through freely. A door occupies two block spaces and both halves normally act as a single barrier, although doors can be opened or closed with a player or mob occupying the bottom block of the door,[1] in which case the player can jump up to land on the bottom half of the door and then again to land on top of the door.

## Block states
See also: Block states

Java Edition:

| Name    | Default value | Allowed values                            | Description                                                                                                                                                                                  |
|---------|---------------|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing  | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the door's "inside" is facing.<br/>The direction the player faces while placing the door.<br/>For example, a door facing east occupies the west part of its block when closed. |
| half    | `lower`       | `lower`<br/>`upper`                       | Identifies which part of the door the block is.                                                                                                                                              |
| hinge   | `left`        | `left`<br/>`right`                        | Identifies the side the hinge is on (when facing the same direction as the door's inside).                                                                                                   |
| open    | `false`       | `false`<br/>`true`                        | True if the door is currently open.                                                                                                                                                          |
| powered | `false`       | `false`<br/>`true`                        | True if the door is currently powered by redstone.                                                                                                                                           |

Bedrock Edition:
Lower Door Block:

| Name            | Metadata Bits   | Default value | Allowed values              | Values forMetadata Bits     | Description                                                                                                                                                                                                                                                                |
|-----------------|-----------------|---------------|-----------------------------|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| direction       | `0x1`<br/>`0x2` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3` | `0`<br/>`1`<br/>`2`<br/>`3` | The direction the door's "inside" is facing.<br/>The direction the player faces while placing the door.<br/>For example, a door facing east occupies the west part of its block when closed.0: Facing east<br/>1: Facing south<br/>2: Facing west<br/>3: Facing north<br/> |
| door_hinge_bit  | `— [sic]`       | `false`       | `false`<br/>`true`          | `0`<br/>`0 [sic]`           | Identifies the side the hinge is on (when facing the same direction as the door's inside). false if hinge is on the left (the default), true if on the right.<br/>Lower door block has the same aux value when it is opened and closed.                                    |
| open_bit        | `0x4`           | `false`       | `false`<br/>`true`          | `0`<br/>`1`                 | True if the door is currently open.                                                                                                                                                                                                                                        |
| upper_block_bit | `0x8`           | `false`       | `false`<br/>`true`          | `0`<br/>`1`                 | Always false for the lower part of a door.                                                                                                                                                                                                                                 |

Upper Door Block:

| Name            | Metadata Bits | Default value | Allowed values              | Values forMetadata Bits           | Description                                                                                                                                                                                                                                                                                                                                |
|-----------------|---------------|---------------|-----------------------------|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| direction       | `— [sic]`     | `0`           | `0`<br/>`1`<br/>`2`<br/>`3` | `0`<br/>`0`<br/>`0`<br/>`0 [sic]` | The direction the door's "inside" is facing.<br/>The direction the player faces while placing the door.<br/>For example, a door facing east occupies the west part of its block when closed.0: Facing east<br/>1: Facing south<br/>2: Facing west<br/>3: Facing north<br/>Upper door block has the same aux value no matter what it faces. |
| door_hinge_bit  | `— [sic]`     | `false`       | `false`<br/>`true`          | `0`<br/>`Unsupported`             | Identifies the side the hinge is on (when facing the same direction as the door's inside). false if hinge is on the left (the default), true if on the right.<br/>Upper door block doesn't support aux value when its hinge is on theright.                                                                                                |
| open_bit        | `— [sic]`     | `false`       | `false`<br/>`true`          | `0`<br/>`0 [sic]`                 | True if the door is currently open.<br/>Lower door block has the same aux value when it is opened and closed.                                                                                                                                                                                                                              |
| upper_block_bit | `0x8`         | `false`       | `false`<br/>`true`          | `0`<br/>`1`                       | Always true for the upper part of a door.                                                                                                                                                                                                                                                                                                  |

