# Bed
A bed is a block that can be dyed. It allows a player to sleep and reset their spawn point to within a few blocks of the bed in the Overworld. If the bed is obstructed or removed, the player spawns at the default world spawning location.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
	- 1.4 Trading
- 2 Usage
	- 2.1 Sleeping
		- 2.1.1 Passing the night
		- 2.1.2 Setting the spawn point
	- 2.2 Bouncing
	- 2.3 Curing
	- 2.4 Placement
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Metadata
	- 4.3 Block states
	- 4.4 Block data
- 5 Advancements
- 6 History
	- 6.1 Data history
	- 6.2 Bed "item"
		- 6.2.1 Appearances
		- 6.2.2 Names
- 7 Issues
- 8 Trivia
- 9 Gallery
	- 9.1 Screenshots
	- 9.2 In other media
- 10 References

## Obtaining
### Breaking
Beds can be mined with any tool, or without a tool.[1]

| Block    | Bed                 |
|----------|---------------------|
| Hardness | 0.2                 |
|          | Breakingtime (secs) |
| Default  | 0.3                 |

A bed also drops itself as an item when pushed by a piston.

### Natural generation
** Igloo **
A red bed naturally generates in each igloo.

** Village **
Beds of various colors generate in village houses, depending on the specific structure and biome:

- Desertvillage houses have cyan, green, or lime beds.
- Plainsvillage houses have white or yellow beds.
- Savannavillage houses have orange, red, or yellow beds.
- Snowy taiga‌[BE  only]andtaigavillage houses have blue or purple beds.
- Snowy tundravillage houses have blue, red, or white beds.

** Trial chambers **
Beds can generate inside the trial chambers as red, purple, white, or green.

### Crafting
| Ingredients                 | Crafting recipe | Description                                                                          |
|-----------------------------|-----------------|--------------------------------------------------------------------------------------|
| MatchingWool+<br/>AnyPlanks |                 | The wool color must match. The planks can be different.                              |
| AnyBed+<br/>MatchingDye     |                 | A bed of any color can be re-dyed using dyes.                                        |
| AnyDyed Bed+<br/>Bleach     |                 | This removes the color from the bed.‌[Bedrock Edition and Minecraft Education  only] |

| Ingredients                                                              | Crafting recipe | Description                                      |
|--------------------------------------------------------------------------|-----------------|--------------------------------------------------|
| AnyBed+<br/>Bone Mealor<br/>Lapis Lazulior<br/>Cocoa Beansor<br/>Ink Sac |                 | ‌[Bedrock Edition and Minecraft Education  only] |

### Trading
Journeyman-level shepherd villagers sell 1 of 16 beds for 3 emeralds as part of their trades.

## Usage
### Sleeping
Player falling asleep.
Beds are used by pressing the use item button while looking at the bed.

A player sleeps by using a bed during a thunderstorm, or at night (between 12542 and 23459 ticks in clear weather, when stars appear in the sky, or between 12010 and 23991 ticks in rainy weather). Players can sleep during a thunderstorm even if they are in a biome where it does not rain (i.e. desert). Attempting to use a bed at any other time results in the message "You can sleep only at night or during thunderstorms" in Java Edition or "You can only sleep at night" in Bedrock Edition. A player sleeps in a bed for 101 in-game ticks, or 5.05 seconds before the time skips to the next day. Sleeping in a bed with the /gamerule doDaylightCycle set to false results in the player being kicked out of the bed after the 101 ticks, but does not change time of the world to day.

Sleeping in a bed is possible only in the Overworld. Attempting to sleep in a bed in the Nether, the End, and custom dimensions in which they are disabled causes it to explode and set fire to surrounding blocks.[2] The explosion has power 5, which is stronger than TNT (4), but not as strong as a charged creeper or end crystal (6). The explosion centers on the head part of the bed. Villagers can sleep normally in any dimension without the bed being blown up.[3] Upon death from a bed explosion, the message "(Player) was killed by [Intentional Game Design]" appears. In Bedrock Edition, bed explosions can be disabled by setting /gamerule respawnBlocksExplode to false; this still prevents beds to be used in invalid dimensions.

The player must be close to the bed to sleep. If the player is close enough to interact with the bed, but not close enough to sleep in it, the message "You may not rest now, the bed is too far away" in Java Edition or "Bed is too far away" in Bedrock Edition appears. To use a bed, a player must be within a distance of 3 blocks in Java Edition or 2 blocks in Bedrock Edition from the bed.

If a "monster" is within 8 blocks of the bed head horizontally (in the X- and Z-axis), and 5 blocks vertically (in the Y-axis), the message "You may not rest now, there are monsters nearby" appears and the player is prevented from sleeping until the monsters leave or are killed. Most hostile mobs, as well as some neutral mobs prevent players from sleeping, as shown in the table below.

| Mob                                   | Prevent the player from sleeping       |
|---------------------------------------|----------------------------------------|
| Blaze                                 | Yes                                    |
| Bogged,Skeleton,Stray,Wither Skeleton | Yes                                    |
| Breeze‌[upcoming: JE 1.21]            | Yes                                    |
| Creeper                               | Yes                                    |
| Drowned                               | Yes                                    |
| Endermite                             | Yes                                    |
| Enderman                              | When hostile                           |
| Ender Dragon                          | No                                     |
| Evoker                                | Yes                                    |
| Ghast                                 | No                                     |
| Giant                                 | Yes                                    |
| Guardian,Elder Guardian               | Yes                                    |
| Hoglin                                | No                                     |
| Illusioner                            | Yes                                    |
| Killer Bunny                          | No                                     |
| Magma Cube                            | No‌[JE  only]/Yes‌[BE  only]           |
| Piglin                                | Yes                                    |
| Piglin Brute                          | Yes                                    |
| Pillager                              | Yes                                    |
| Phantom                               | Yes                                    |
| Ravager                               | Yes                                    |
| Shulker                               | No                                     |
| Silverfish                            | Yes                                    |
| Skeleton Horse,Zombie Horse           | No‌[JE  only]/Yes‌[BE  only][4]        |
| Spider,Cave Spider                    | Yes                                    |
| Slime                                 | No‌[JE  only]/Yes‌[BE  only]           |
| Vex                                   | Yes                                    |
| Vindicator                            | Yes                                    |
| Warden                                | Yes                                    |
| Witch                                 | Yes                                    |
| Wither                                | Yes                                    |
| Zoglin                                | Yes                                    |
| Zombie,Zombie Villager,Husk           | Yes                                    |
| Zombified Piglin                      | When hostile‌[JE  only]/Yes‌[BE  only] |

If the player has not entered a bed and didn't die for 3 in-game days, phantoms can spawn unless /gamerule doInsomnia is set to false. In Java Edition, this can be verified by checking if the "Time Since Last Rest" statistic is greater than 1.00 h.

A hostile mob can wake a player that is sleeping.

The player also cannot sleep in a bed occupied by another player, resulting in the message, "This bed is occupied".

A player can, however, sleep in a bed being used by a villager. The player may first wake the villager (pressing use on the villager) and then quickly enter the bed before the villager can lie down again. The villager reclaims the bed after the player wakes. The villager is kicked out of its bed when a player attempts to sleep there.

A player also cannot sleep while on fire, while poisoned, or while starving.

If all sleeping requirements are met and the player enters a bed, the player is positioned in the bed. The player falls asleep as the screen fades to black. In Bedrock Edition, the sleeping animation slowly lowers the player into bed.

Once all players in a world are asleep, after 5 seconds (100 ticks) the time of day changes to sunrise. (time 0)

During this time, the chat window is focused, and the player can leave the bed by clicking the Leave Bed button.

Waterlogged beds‌[Bedrock Edition  only] cannot be slept in unless the player or villager has the Water Breathing or Conduit Power status effects. Attempting to use a waterlogged bed otherwise does not display any message.[5]

Beds displaying an error above the hotbar is a feature exclusive to beds; other blocks that cannot be used do not display such a message.[6]

If there are two or more blocks of space above the bed, then the player can wake up on the bed. If there is less than two blocks above the bed and there is room on the side, then the player wakes up on the side of the bed. If there is no space on the side of the bed and there is less than two blocks above the bed, then the player still wakes up on top of the bed, but suffocates if it's a solid block. 

Villagers always wake up on top of the bed, meaning they can suffocate if there isn't enough room above the bed.

#### Passing the night
Sleeping changes the time of day to sunrise and resets the weather cycle, changing the weather to clear conditions. In Java Edition, the weather cycle resets only during rainy or snowy weather. The player wakes up next to the bed, facing the bed.

Sleeping does not accelerate processes that take place over time such as the growth of crops or smelting. If /gamerule doDaylightCycle is false, the player instead wakes up in the night.

To skip the night in multiplayer, all players in the Overworld must be in bed at the same time. Pressing the Leave Bed button is not necessary in this case. The percentage of players that need to sleep to skip the night can be customized with the game rule playersSleepingPercentage.

Villagers are unable to skip the night by sleeping in beds, unlike players.

If the bed is destroyed while the player is in it, due to for example an explosion or by another player, the player wakes prematurely and the night does not pass.

#### Setting the spawn point
Once a player has entered a bed (or right clicked the bed during daytime), their spawn point is set to the location of that bed. In Java Edition, multiple players can set their spawn point on a single bed. In Bedrock Edition, the last player to use a specific bed is the only player who can respawn there, and players who had previously slept there respawn at the world spawn.

Using a bed in the daytime likewise sets the spawn point, without actually entering the bed. 

When a bed explodes, it does not set the spawn point. 

The message "Respawn point set" is displayed in chat when the respawn point is successfully changed.

The check for a bed is made only when the player respawns. This means that the bed can be destroyed and replaced or even reoriented, but as long as there is a bed present in the same location, the player can respawn there. If a player's bed is absent, or if the area around the bed is made unsuitable for respawning (see below), a message is displayed saying "You have no home bed or respawn anchor, or it was obstructed" in Java Edition or "Your home bed was missing or obstructed" in Bedrock Edition, and the player respawns at the world spawn point. 

When choosing where to respawn the player, the northwesternmost (lowest X- and Z-coordinates) location of the seven blocks adjacent to the head of the bed is chosen first. If this location is obstructed, the next choice is to its south (+Z), rather than the east (+X). Only when all seven locations around the head are obstructed are the three remaining ones adjacent to the foot then to be considered. 

For a location to be unobstructed, the block at the level of the bed must be air or non-solid (e.g. torches, but not glass) and there must be a space with a solid block below it and two non-colliding blocks for the player to stand in 0-2 blocks below the bed. It does not matter if the bed itself has blocks above it. Putting a slab one block above a bed can act as a two block tall space, as the bed is half a block tall. The bed never spawns the player on or directly below itself even if all other locations are obstructed. If a bed is obstructed, the player's spawn point is cleared after they respawn. That is, even if the bed is subsequently made usable again, the player continues to respawn at the world spawn until interacting with the bed again. 

Specifically, when interacting with it, the location of the head of the bed is saved as the spawn point, and if a bed is in that space (whether it is the foot or the head) then the respawn works. This can be observed by reorienting the bed with its head in the same location. Interacting with it does not produce a "Respawn point set" message as the game doesn't change the saved spawn point. If a bed is reoriented so that its foot is in this space, it still functions on the next respawn, but it can also be interacted with to update the spawn point to the new head of the bed and cause a "Respawn point set" message. Attempting the reverse, reorienting the bed so that it overlaps the original location of the foot, results in a respawn at world spawn. However, the location of the foot of the bed is also saved. If the bed is moved so that part of it overlaps the original location of the head, it can be observed that the same locations need to be obstructed to stop spawning. It is possible to respawn 2 blocks away from the bed this way.

### Bouncing
Falling onto a bed bounces the player with 66% strength – the bouncing-up velocity is 66% of the impact velocity. The player also takes 50% of normal fall damage.

Baby villagers bounce on beds during the day.

If the player is falling while sleeping requirements are met, and presses use on a bed within reach before hitting the ground, the fall damage is delayed until the player wakes.

A player can bounce on a bed while another player or villager is sleeping on it without waking the player or the villager up.

Villagers can be pushed onto beds, as the bed is half a block tall.

### Curing
Each bed in the vicinity of a zombie villager has a chance to speed up the process of curing the zombie villager. Iron bars (such as in a prison cell) also have this effect.

### Placement
Beds require two blocks of floor space. Placement requires at least 2 blocks from the player's facing direction. When placed, the foot of the bed is placed on the block selected and the head of the bed on the block farther away from the player. In Bedrock Edition, beds require solid blocks below them when placed. However, the bed remains in place if its supporting blocks are later removed. In Java Edition, beds do not require supporting blocks and can be placed anywhere, provided there is enough room.

## Data values
### ID
Java Edition:

| Name           | Identifier       | Form         | Block tags | Item tags | Translation key                  |
|----------------|------------------|--------------|------------|-----------|----------------------------------|
| White Bed      | `white_bed`      | Block & Item | `beds`     | `beds`    | `block.minecraft.white_bed`      |
| Orange Bed     | `orange_bed`     | Block & Item | `beds`     | `beds`    | `block.minecraft.orange_bed`     |
| Magenta Bed    | `magenta_bed`    | Block & Item | `beds`     | `beds`    | `block.minecraft.magenta_bed`    |
| Light Blue Bed | `light_blue_bed` | Block & Item | `beds`     | `beds`    | `block.minecraft.light_blue_bed` |
| Yellow Bed     | `yellow_bed`     | Block & Item | `beds`     | `beds`    | `block.minecraft.yellow_bed`     |
| Lime Bed       | `lime_bed`       | Block & Item | `beds`     | `beds`    | `block.minecraft.lime_bed`       |
| Pink Bed       | `pink_bed`       | Block & Item | `beds`     | `beds`    | `block.minecraft.pink_bed`       |
| Gray Bed       | `gray_bed`       | Block & Item | `beds`     | `beds`    | `block.minecraft.gray_bed`       |
| Light Gray Bed | `light_gray_bed` | Block & Item | `beds`     | `beds`    | `block.minecraft.light_gray_bed` |
| Cyan Bed       | `cyan_bed`       | Block & Item | `beds`     | `beds`    | `block.minecraft.cyan_bed`       |
| Purple Bed     | `purple_bed`     | Block & Item | `beds`     | `beds`    | `block.minecraft.purple_bed`     |
| Blue Bed       | `blue_bed`       | Block & Item | `beds`     | `beds`    | `block.minecraft.blue_bed`       |
| Brown Bed      | `brown_bed`      | Block & Item | `beds`     | `beds`    | `block.minecraft.brown_bed`      |
| Green Bed      | `green_bed`      | Block & Item | `beds`     | `beds`    | `block.minecraft.green_bed`      |
| Red Bed        | `red_bed`        | Block & Item | `beds`     | `beds`    | `block.minecraft.red_bed`        |
| Black Bed      | `black_bed`      | Block & Item | `beds`     | `beds`    | `block.minecraft.black_bed`      |

| Name         | Identifier |
|--------------|------------|
| Block entity | `bed`      |

Bedrock Edition:

| Bed   | Identifier | Numeric ID | Form                         | Item ID[i 1] | Translation key                                                                                                                                                                                                                                                                                                                                                                                     |
|-------|------------|------------|------------------------------|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Block | `bed`      | `26`       | Block & Ungiveable Item[i 2] | `item.bed`   | `tile.bed.name`                                                                                                                                                                                                                                                                                                                                                                                     |
| Item  | `bed`      | `418`      | Item                         | —            | `item.bed.black.name`<br/>`item.bed.red.name`<br/>`item.bed.green.name`<br/>`item.bed.brown.name`<br/>`item.bed.blue.name`<br/>`item.bed.cyan.name`<br/>`item.bed.silver.name`<br/>`item.bed.gray.name`<br/>`item.bed.pink.name`<br/>`item.bed.lime.name`<br/>`item.bed.yellow.name`<br/>`item.bed.lightBlue.name`<br/>`item.bed.magenta.name`<br/>`item.bed.orange.name`<br/>`item.bed.white.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Unavailable with /give command

| Name         | Savegame ID |
|--------------|-------------|
| Block entity | `Bed`       |

### Metadata
See also: Data values

In Bedrock Edition, bed items use the following data values:

|  | DV | Description    |
|--|----|----------------|
|  | 0  | White Bed      |
|  | 1  | Orange Bed     |
|  | 2  | Magenta Bed    |
|  | 3  | Light Blue Bed |
|  | 4  | Yellow Bed     |
|  | 5  | Lime Bed       |
|  | 6  | Pink Bed       |
|  | 7  | Gray Bed       |
|  | 8  | Light Gray Bed |
|  | 9  | Cyan Bed       |
|  | 10 | Purple Bed     |
|  | 11 | Blue Bed       |
|  | 12 | Brown Bed      |
|  | 13 | Green Bed      |
|  | 14 | Red Bed        |
|  | 15 | Black Bed      |

### Block states
See also: Block states

Java Edition:

| Name     | Default value | Allowed values                            | Description                                                                                                  |
|----------|---------------|-------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| facing   | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the head of the bed is pointing.<br/>The same direction the player faces when placing the bed. |
| occupied | `false`       | `false`<br/>`true`                        | True when a player or villager is using the bed.                                                             |
| part     | `foot`        | `foot`<br/>`head`                         | The half of the bed in the current block.                                                                    |

Bedrock Edition:

| Name           | Metadata Bits   | Default value | Allowed values              | Values forMetadata Bits     | Description                                                                                                                                  |
|----------------|-----------------|---------------|-----------------------------|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| direction      | `0x1`<br/>`0x2` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3` | `0`<br/>`1`<br/>`2`<br/>`3` | The direction the head of the bed is pointing.0:Head facing South<br/>1:Head facing West<br/>2:Head facing North<br/>3:Head facing East<br/> |
| head_piece_bit | `0x8`           | `true`        | `false`<br/>`true`          | `0`<br/>`1`                 | If the current block is the head part.                                                                                                       |
| occupied_bit   | `0x4`           | `false`       | `false`<br/>`true`          | `0`<br/>`1`                 | True when a player or villager is using the bed.                                                                                             |



### Block data
A bed has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format

- Block entity data
	- 
	- Tags common to all block entities

Bedrock Edition:

SeeBedrock Edition level format/Block entity format.
