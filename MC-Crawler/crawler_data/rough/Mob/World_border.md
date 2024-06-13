# World border
The world border is the current edge of a Minecraft dimension.

## Contents
- 1 General information
	- 1.1 Size
	- 1.2 Walking to the border
- 2 Effects
	- 2.1 On entities
	- 2.2 On blocks
	- 2.3 When set to invalid values
- 3 Commands
- 4 Data values
	- 4.1 World data
- 5 History
- 6 Issues
- 7 Trivia
- 8 Gallery
	- 8.1 Screenshots
- 9 References
- 10 See also

## General information
The world border from the outside using the /tp command.
The world border appears as a series of animated, diagonal, narrow stripes at 29,999,984 blocks out of the center of the world.

The world border is tinted depending on how and if its size is changing. By default, when the border is not changing, the stripes are a translucent aqua color. If the border is expanding, the stripes appear green; if the border is shrinking, they appear red.

The world border appears different depending on the current graphics setting, which is likely not intended;[1] on Fast and Fancy it appears as light and translucent, but on Fabulous! it appears considerably darker.

### Size
The world border is essentially a giant bounding box; by default, its center lies at coordinates above Y=255.

With commands, the size and position of the border can be modified. The world border always behaves in full block increments, even if it is set to a partial block. Its size and location remain the same across all dimensions.

### Walking to the border
A terrestrial journey to the border through legitimate means, without using a Nether shortcut, has been done by a single player, Figonometry between 2021–22, as of October 2023.[2]

Others have completed the journey through means such as glitches, elytra flying on the Nether roof, or otherwise.

Time-wise, the walking (not sprinting) speed is 4.3 blocks per second. Walking for 6 hours per day is equal to 21,600 seconds, giving a travelled distance of 92,880 blocks every day. Walking to the Far Lands, 12.5 million blocks away, would take just under 136 days at this pace. The border is almost three times further out.

## Effects
### On entities
Most entities, with exception to some projectiles, are unable to move through the world border.

If a dispenser or dropper is placed so that it directly faces the edge of the border, then items, projectiles, TNT, etc. can be fired outside of the edge of the border. Any items fired out of a dispenser float in midair; if an item is dropped from the player inventory, the item falls normally.

If a mob is spawned from a dispenser via a spawn egg, the mob behaves normally. Spiders can climb the world border, and endermen can teleport outside of it and Pillagers can walk through it.

Any players on the outside of the world border (with exception to those in Creative or Spectator mode) take constant damage as long as they are outside the border. The amount of damage depends on the distance to the border, with damage being inflicted when the player is outside an area that is 5 blocks wider than the world border on each side. Players typically cannot interact with blocks or entities outside the world border.

Additionally, while sneaking if they are less than one block outside the world border, some of the effects that occur while sneaking or changed or removed. These are:

- Being prevented from walking off edges
- Having movement slowed
- Decreased eye level andthird-person view, character model bending over slightly
- Shorter hitbox
- Fainter name tag inmultiplayer[verify]
- Moving throughscaffolding: the player instead falls through it as if it were air

If the player was already sneaking before entering this area, their eye level and third-person view remains decreased.

While players themselves cannot move through the world border, even if they manage to go ahead of chunk loading, they can reach the other side of the world border through other means, including: 

- Letting the world border pass them as it is shrinking
- Throwing an ender pearl through the world border
- Consumingchorus fruitnear the world border and being teleported beyond it
- Dying and respawning, if the spawn point is outside the world border

Oddly, while standing inside the world border while close to it and looking at it at a negative angle, trying to use item (such as throwing projectiles, eating food, or shooting a bow) results in nothing happening.

Entities cannot spawn naturally outside the world border. They persist without taking damage if they spawned before the world border gets shrunk by a command.

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

