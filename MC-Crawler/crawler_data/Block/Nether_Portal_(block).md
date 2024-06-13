# Nether Portal (block)
The nether portal block is the translucent part of the nether portal that teleports the player to and from the Nether.

## Contents
- 1 Obtaining
- 2 Usage
	- 2.1 Piston interactivity
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
	- 5.1 History of the block itself
	- 5.2 History of the block's effects
	- 5.3 Nether portal "item"
		- 5.3.1 Appearances
		- 5.3.2 Names
	- 5.4 Texture generation prior to Java Edition 13w02a and Bedrock Edition v0.15.0
- 6 Issues
- 7 References

## Obtaining
The nether portal block cannot be obtained as an item even by using the /give command. The item form is completely nonexistent in Java Edition, but it can be obtained through add-ons, external editors or by using bugs in Bedrock Edition. 

The nether portal block can be placed using commands such as /fill or /setblock and is generated when lighting a nether portal.

## Usage
See also: Nether portal

Nether portal blocks can stably exist only within a nether portal structure, unlike end portal blocks. When the block is updated and detects it is not part of such a structure, it is destroyed. However, using update suppression glitches, it is possible to obtain a standalone portal block without a frame, but the portal will be destroyed once it receives an update, i.e. placing a block next to the portal or moving a piston next to or into the portal.

Nether portal blocks can be used to teleport entities between the Nether and the Overworld. When a player in the Overworld or the Nether stands in a nether portal block for 4 seconds, the player is taken to the other dimension. While in the nether portal block, the player can neither open their inventory nor interact with blocks with GUI. The player can step out of a portal before it completes its animation to abort the teleport. However, in Creative mode there is no wait time—the player immediately transfers between dimensions. If there is already an active portal within range (125 blocks) in the other world, the player appears in that portal. Otherwise, a portal is created at or near the corresponding coordinates. If a single portal block is placed using commands, it can still be used to travel to the Nether.

Nether portal blocks make distinctive sounds, and emit the same purple particles produced by endermen, endermites, and ender chests. Portal blocks emit a light level of 11, dimmer than a torch.

Falling block entities can be teleported through a portal, but a piston cannot push a block through.

Much like water or lava, portal blocks cannot be broken by tools except in Creative. However, portal blocks can be destroyed by explosions (even weak ones) and can be replaced by placing water or lava sources in the same block (can also be done by dispensers). If any portal block is destroyed, the whole portal is deactivated as adjacent portal blocks are updated and detect that the portal structure is no longer complete.

While nether portals themselves cannot be lit in the End, a portal block set in the End and in custom dimensions behave exactly like in the Overworld, calculating coordinates in the Nether with the same 1:8 ratio. They teleport players to the Nether in Java Edition, and to the Overworld in Bedrock Edition.

### Piston interactivity
Nether portal blocks cannot be pushed by pistons. They also cannot be pushed or pulled by sticky pistons.

## Data values
### ID
Java Edition:

| Name          | Identifier    | Form  | Block tags               | Translation key               |
|---------------|---------------|-------|--------------------------|-------------------------------|
| Nether Portal | nether_portal | Block | hoglin_repellentsportals | block.minecraft.nether_portal |

Bedrock Edition:

| Name          | Identifier | Numeric ID | Form                         | Item ID[i 1]   | Translation key  |
|---------------|------------|------------|------------------------------|----------------|------------------|
| Nether Portal | portal     | 90         | Block & Ungiveable Item[i 2] | Identical[i 3] | tile.portal.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Unavailable with /give command

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block states

Java Edition:

| Name | Default value | Allowed values | Description                              |
|------|---------------|----------------|------------------------------------------|
| axis | x             | x              | The portal's long edge runs east–west.   |
|      |               | z              | The portal's long edge runs north–south. |

Bedrock Edition:

| Name        | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                                                                                                               |
|-------------|---------------|---------------|----------------|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| portal_axis | 0x10x2        | unknown       | unknown        | 0                       | If placed with this state, the portal's long edge runs north–south. If set to it, its direction will be tied to that of adjacent portals. |
|             |               |               | x              | 1                       | The portal's long edge runs east–west.                                                                                                    |
|             |               |               | z              | 2                       | The portal's long edge runs north–south.                                                                                                  |



