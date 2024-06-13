### On blocks
Players cannot normally place and destroy blocks, nor interact with objects outside of the world border, as there are no hitboxes. It is possible to place blocks outside of the world border, either by placing the block against one that is inside the world border or by using commands.

Most blocks still function outside the world border, and most redstone contraptions still function as well. Exceptions include falling blocks (such as sand and gravel), which drop as an item, and pistons or hoppers, which simply don't function. Explosions from TNT and other sources also work normally, destroying terrain outside of the border. Light from torches and other sources also remain unaffected.

Liquids flow through the world border, so long as they are placed inside the border.
Liquids can flow through the border and continue flowing until reaching their flow limit. Liquids cannot be placed on the outside of the border.[3] Liquids placed via a dispenser flow as normal. Mixing water and lava with a dispenser results in the flow of each liquid abruptly ending, presumably because the stone, cobblestone, or obsidian that would normally generate does not.

### When set to invalid values
The world border size can be changed by manually editing the level.dat file. In any case, there remains a world boundary at 30 million blocks on both the X and Z axes. 

- When set to 0 or a negative number, the entire world is treated as outside the world border, and the border warning overlay appears throughout the world. No blocks can be mined and entities take damage unless they are within the border safe zone.
- When set to NaN (Not a Number), the entire world is treated as outside the world border, but no border warning appears. No blocks can be mined, even in Creative mode, although entities do not take damage.
- When set to infinity, the border occurs normally.

## Commands
Main article: Commands/worldborder
** Set **
/worldborder set <sizeInBlocks> [timeInSeconds]
Sets the border to a square region with the specified size in blocks as the width and length. Optionally, atimeInSecondsmay be specified such that the border grows or shrinks from the previous width to that being set over the specified time in seconds. IftimeInSecondsis not specified, the world border changes immediately. To reset the world border size, setsizeInBlocksto 59,999,968. The border still grows or shrinks and the animation displays even if the game is paused.
** Center **
/worldborder center <x> <z>
Sets the center of the area inside the world border to the specified<x>and<z>coordinates. Tilde (~) can be used as a relative coordinate. To reset the world border center, set both<x>and<z>to 0 (zero).
** Add **
/worldborder add <sizeInBlocks> [timeInSeconds]
Adds or subtractssizeInBlocksto/from the current world border width and length.sizeInBlocksmay be a positive or negative number. Optionally, atimeInSecondsmay be specified such that the border grows or shrinks from the current width to that being set over the specified time in seconds.
** Damage **
/worldborder damage buffer <sizeInBlocks>
Sets the number of blocks a player may safely be outside the world border before taking damage.  The default is 5 blocks.
/worldborder damage amount <damagePerBlock>
Sets the amount of damage a player takes when outside the world border plus the world border buffer.  The default is 0.2 damage per second per block.
** Warning **
/worldborder warning time <timeInSeconds>
Causes the screen to be tinted red when a contracting world border reaches the player within the specified time. The default is 15 seconds. The tint does not display if the user is using fast graphics.
/worldborder warning distance <sizeInBlocks>
Causes the screen to be tinted red when the player is within the specified number of blocks from the world border. The default is 5 blocks. The tint does not display if the user is using fast graphics.
** Get **
/worldborder get
Returns the current width of the world border.
## Data values
### World data
Java Edition:

- level.dat
	- Data
		- BorderCenterX: Center of the world border (X-axis).
		- BorderCenterZ: Center of the world border (Z-axis).
		- BorderDamagePerBlock: Damage taken per block moved outside the world border,
		- BorderSafeZone: Distance in blocks of the buffer zone where damage is not taken when outside the world border.
		- BorderSize: World border diameter.
		- BorderSizeLerpTarget: The border size after it has been changed. "Lerp" stands forLinear Interpolation, as the border changes its size in a linear fashion.
		- BorderSizeLerpTime:[more information needed]
		- BorderWarningBlocks: Maximum distance away from the border until the border warning overlay appears on the player's HUD.
		- BorderWarningTime: Time in seconds[verify]until the border warning overlay appears.


