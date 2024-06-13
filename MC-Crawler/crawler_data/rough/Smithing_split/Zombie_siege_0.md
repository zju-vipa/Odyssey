# Zombie siege
Zombie sieges are in-game events where many zombies spawn in and attack a village.

## Contents
- 1 Mechanics
	- 1.1 Siege start checks
	- 1.2 Zombie spawning
- 2 Defense tactics
- 3 Recovery
- 4 Video
- 5 History
- 6 Issues
- 7 Trivia
- 8 Gallery
	- 8.1 Screenshots
- 9 See also
- 10 Notes
- 11 References

## Mechanics
At midnight each night (tick 18000 in Minecraft time), a zombie siege is determined to occur somewhere in the overworld that night with a 10% probability. If a siege has been determined to occur, attempts are made each tick to start the siege until either an attempt is successful or the sky light level reaches 12 due to sunrise, although the reduction in sky light level from a Thunderstorm allows siege start attempts to continue well past dawn. 

### Siege start checks
The decisions whether to start a siege, spawn a siege zombie, or to abort any siege start attempt are made while the game rule doMobSpawning is enabled. If the rule is disabled after the decision to attempt a siege was made, and then enabled again during another night (even before midnight), the decision still stands until a new decision is made at midnight, a siege starts, or the start attempt is aborted due to sunrise or Peaceful difficulty. Disabling the game rule also halts the spawning phase of an active siege, continuing with the remaining spawns when mob spawning is enabled again, unless conditions for aborting the siege are met. There is no way to force the game to start making siege attempts.

Players who are not in spectator mode can trigger the night's siege if they are in an area that is considered part of a logical village[note 1] and are not in a biome with the without_zombie_sieges tag.[note 2] The start check iterates over all players in the dimension every tick, until either a player satisfies the starting conditions or the siege attempt is aborted as described above. The game does not attempt to start sieges in peaceful difficulty, and any active decision to make such attempts is canceled when the difficulty is set to Peaceful, and not resumed if difficult is set higher again.

Ten attempts are made per player to choose a random siege starting point. First, a random location on a horizontal circle with 32 blocks radius around the player is chosen as the starting point, then that location is used to find a potential spawn location for a siege zombie as per the zombie spawning logic described below. If this successfully finds a valid zombie spawning point, the siege is started at the chosen starting point. If all ten starting points fail to find valid spawning locations, the checks pass to the next player.

### Zombie spawning
During a siege, 20 zombies try to spawn in intervals of 2 ticks. For each zombie, 10 attempts are made to randomly choose a valid spawning point on the surface (i.e. highest non-air block at given horizontal coordinates) within a 16×16 horizontal distance around the chosen point. If a valid spawn point is found, the zombie is spawned. Failed spawns are not repeated, leading to fewer total zombies spawning for the siege.

Zombies spawned within a siege ignore player proximity, the presence of other mobs, and whether an area would usually spawn zombies. Only the minimal spawning conditions are checked:

- Light level must be appropriate for zombie spawning.
- The surface block must allow zombie spawning on top.
- The block must be within a logical village.[note 1]

Zombie villagers, husks and drowned are never spawned as part of a siege, but all other variations (e.g. baby, jockey, and equipment) are determined as for normal random spawns.

The zombies that spawn as part of a siege behave in the same manner as normally-spawned zombies; they attack all villagers within sight, and villagers and iron golems react accordingly. The zombies despawn as usual if the player is far enough away.

## Defense tactics
Main article: Zombie siege defense
## Recovery
If at least two villagers survive the siege, the villagers can breed and repopulate the village. Without player intervention, however, it is likely for villages to be wiped out by sieges and randomly-spawned zombies, and all the villagers would be either dead or zombified. 

Even if no villagers survive, a village may be repopulated by curing zombie villagers, or by luring in villagers from another village.

## Notes
1. ↑ a bBeing "in a village" is defined as being in a 3×3×3 cube of chunk sections centered on a section containing a claimed bed, bell, or job site, which is not necessarily related to any generated village structures.
2. ↑By default this tag only includes mushroom fields.


