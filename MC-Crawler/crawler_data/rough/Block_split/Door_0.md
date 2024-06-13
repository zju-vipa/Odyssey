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

