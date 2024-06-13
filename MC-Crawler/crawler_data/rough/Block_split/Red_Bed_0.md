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

