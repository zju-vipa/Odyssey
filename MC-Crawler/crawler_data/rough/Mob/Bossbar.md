# Bossbar
A bossbar is a bar at the top of the screen that can track health of a boss mob or the total health of raid mobs.

The bossbar appears naturally in the game through three means: during a raid, after constructing a wither, and upon entering the End if the ender dragon has not yet been defeated.

## Contents
- 1 Creation
	- 1.1 Manual
	- 1.2 Natural
		- 1.2.1 Boss mobs
		- 1.2.2 Raids
- 2 Components
	- 2.1 Color
	- 2.2 Style
	- 2.3 ID system
- 3 Removal
- 4 History
- 5 Issues
- 6 Gallery
- 7 References

## Creation
### Manual

  

This section needs expansion. 
You can help by expanding it.


A bossbar can be created manually using the /bossbar command. ‌[Java Edition  only]

### Natural
#### Boss mobs
A bossbar appears in the top center of the screen when near a wither or ender dragon. For the ender dragon's bossbar to appear, the player must be within a Euclidean distance of 192 blocks from the coordinates (0.0, 192, 0.0) in the End dimension.[needs testing] For the wither's bossbar to appear, the player must be loading the chunk the wither is in and be within 24 chunks and 3.5 blocks of a chunk the wither is in. For the bossbar to update after taking damage, a mob has to have the NBT-Tag NoAI set to 0b. [1]

#### Raids
When a player is within a 93 block radius of the center of a raid, a raid bossbar appears, showing the total health of all raid mobs present during the current wave.

## Components
### Color
The bossbar has colors depending on which boss mob or event is active:

- the ender dragon has a color of pink,
- the wither has a light purple bossbar‌[Java Edition  only]or a dark purple bossbar‌[Bedrock Edition  only],
- the raid bossbar has a color of red.

### Style
A bossbar has a style attribute. It can be either "progress", "notched_6", "notched_10", "notched_12" or "notched_20". The value "progress" creates a clean bar, while the other ones create a notched bar with 6, 10, 12 or 20 segments.

The ender dragon and wither own a "progress" bossbar. During a raid, a "notched_10" ‌[Java Edition  only] or a "progress" ‌[Bedrock Edition  only] bossbar is shown.

### ID system
A bossbar has an ID, which can be used to do certain actions with one bossbar. An ID is not shown on the bossbar[verify].

## Removal

  

This section needs expansion. 
You can help by expanding it.


A bossbar can be disabled by using /bossbar remove <id>.

