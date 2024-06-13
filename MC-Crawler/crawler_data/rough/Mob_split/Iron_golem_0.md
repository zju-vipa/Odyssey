# Iron Golem
An iron golem is a buildable neutral mob that attacks monsters with its arms, knocking them into the air. Iron golems created by villagers or spawned in villages patrol their village, and may attack players that attack it or have a low popularity or reputation with their village.

## Contents
- 1 Spawning
	- 1.1 Villages
	- 1.2 Creation
	- 1.3 Pillager outposts
- 2 Drops
	- 2.1 On death
- 3 Behavior
	- 3.1 Attacking
		- 3.1.1 Provocation by players
		- 3.1.2 Provocation by other mobs
	- 3.2 Being attacked
	- 3.3 Cracking
	- 3.4 Healing
- 4 Preferred path
	- 4.1 Climbing
- 5 Sounds
- 6 Data values
	- 6.1 ID
	- 6.2 Entity data
- 7 Achievements
- 8 Advancements
- 9 History
- 10 Issues
- 11 Trivia
- 12 Gallery
	- 12.1 Screenshots
	- 12.2 Development images
	- 12.3 In other media
- 13 References
- 14 External links

## Spawning
### Villages
** Java Edition **
In Java Edition, villagers can summon iron golems, either when they are gossiping or panicking and the following criteria are met:

1. The villager has slept in the last 20 minutes
2. The villager has not detected an iron golem in the last 30 seconds
	- An iron golem is detected when it is within 16 blocks of the villager (±16X±16Z±16Yaxis)
	- The villager scans for golems once every 10 seconds
3. The villager has not been near a summoning in the last 30 seconds
	- A villager is near a summoning when it is within 10 blocks of a villager (±10X±10Z±10Yaxis) who successfully summons an iron golem
4. There are enough participants within 10 blocks of the villager, including the villager itself; participating villagers need to fulfill the previous 3 conditions:
	- Whengossiping, 5 or more participants are needed
	- Whenpanicking, 3 or more are needed
5. A valid spawn point for the golem is found

Iron golems still spawn even when the game rule doMobSpawning is set to false.[1]

To find a valid spawn point, up to 10 attempts are made to spawn a golem within a 17×13×17 box centered on the villager (villager block position ±8 blocks along x/z axes and ±6 blocks along y axis). A random y column is picked and then the topmost block in that column is selected that is air or liquid and has a "solid-blocking" block underneath. 

The target location is then checked whether the block underneath has a solid top surface (which is not the same as "solid-blocking"). The target block and 2 blocks above must not be a full block, nor be redstone-powered, nor be rails, and the two blocks above must not be water. This means the iron golem can spawn inside 1-deep water or inside blocks like slabs, fences, and carpets (if other checks pass). Adjacent blocks are irrelevant, so golems can spawn partially inside adjacent solid blocks.[2] However, the spawning iron golem still must not collide with any existing entities.

** Bedrock Edition **
In Bedrock Edition, an iron golem can spawn naturally when a village first generates in the world. Iron golems also spawn in villages having at least 20 beds and 10 villagers. The golem attempts to spawn in a 17×13×17 volume, ±8 blocks horizontal and ±6 blocks vertical from the village's center block, which can be (but isn't necessarily) a bed pillow or a bell. 

First, X and Z coordinates are randomly chosen within the spawn volume. Next, the highest block at those coordinates within the spawn volume is found. If it is a block with a full top surface— including glass, upside-down stairs, top slabs, and even hoppers (though this has varied with version)—and there is no obstruction above it by a block above the spawn volume, then the golem spawns there. Otherwise, the spawn attempt is canceled.

For a village to spawn iron golems, it must have at least 10 villagers. 75% of these villagers must have worked (i.e. stood beside or atop their workstation) in the past day, and 100% of them must be linked to a bed. Additionally, the village center must be within a player's simulation distance volume.

The maximum distance the player can be from the village for iron golems to spawn can be calculated with the following formulas. These are approximate because they yield a cuboid volume, but the simulation distance volume is an octahedral shape based on taxicab distance.

Horizontal=8×SimulationDistance+32
Vertical=8×SimulationDistance+12

If the village's original iron golem is killed, a new one cannot spawn unless all of the conditions are met. Therefore, a small village does not regenerate an iron golem unless the village is expanded.

If the spawn conditions are met, then the chance of attempting a spawn is 1⁄700 per game tick, which averages to one spawn attempt every 35 seconds. Iron golems can spawn provided the 2×3×2 space above the spawn point (that is, horizontally centered on the northwest corner of the block it spawns on) contains only non-full blocks, and the block it spawns on is solid.

An additional iron golem spawns for each additional 10 villagers beyond the initial population requirement, provided that the other requirements are met.

### Creation



















Iron Golem build configuration.





















Iron Golem build configuration 2.





















Iron Golem build configuration 3. ‌[BE  only]


Iron golems are created by placing four iron blocks in a T shape (as shown in the image), and then placing a carved pumpkin, jack o'lantern or pumpkin‌[BE  only] on top of the center upper block. The pumpkin may be placed by the player, a dispenser or an enderman, but it must be placed last. It needs at least one block of space around the bottom iron block to be able to spawn and cannot spawn in a confined area; even grass can prevent an iron golem from spawning. Alternatively, the blocks can be placed in any order with an uncarved pumpkin; the player can shear the pumpkin to spawn the golem. When successfully transformed, it is naturally passive toward all players under all circumstances. It can, however, attack the player’s tamed wolves, if punched accidentally, but it never directly attacks the player. The constructed golem attacks hostile mobs like a naturally spawned iron golem.

The block arrangement can be placed upright, lying down, or upside-down. The four empty spaces in the diagram (above and below each of the arms) must be air blocks. Any non-air block (including blocks such as snow layers, grass, and water) present in any of the empty spaces prevent the golem from spawning. 

In Java Edition, the player can place a pumpkin on the four blocks of iron, then shear the pumpkin. The iron golem still spawns like normal.

Like other constructed mobs, iron golems always spawn facing south. Their large size may cause them to take suffocation damage from nearby solid blocks at the level of their head.

Dropping a pumpkin on the correct arrangement of iron blocks does not spawn a iron golem.


