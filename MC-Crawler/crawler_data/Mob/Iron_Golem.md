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
Java Edition
In Java Edition, villagers can summon iron golems, either when they are gossiping or panicking and the following criteria are met:

The villager has slept in the last 20 minutes
The villager has not detected an iron golem in the last 30 seconds
An iron golem is detected when it is within 16 blocks of the villager (±16X ±16Z ±16Y axis)
The villager scans for golems once every 10 seconds
The villager has not been near a summoning in the last 30 seconds
A villager is near a summoning when it is within 10 blocks of a villager (±10X ±10Z ±10Y axis) who successfully summons an iron golem
There are enough participants within 10 blocks of the villager, including the villager itself; participating villagers need to fulfill the previous 3 conditions:
When gossiping, 5 or more participants are needed
When panicking, 3 or more are needed
A valid spawn point for the golem is found
Iron golems still spawn even when the game rule doMobSpawning is set to false.[1]

To find a valid spawn point, up to 10 attempts are made to spawn a golem within a 17×13×17 box centered on the villager (villager block position ±8 blocks along x/z axes and ±6 blocks along y axis). A random y column is picked and then the topmost block in that column is selected that is air or liquid and has a "solid-blocking" block underneath. 

The target location is then checked whether the block underneath has a solid top surface (which is not the same as "solid-blocking"). The target block and 2 blocks above must not be a full block, nor be redstone-powered, nor be rails, and the two blocks above must not be water. This means the iron golem can spawn inside 1-deep water or inside blocks like slabs, fences, and carpets (if other checks pass). Adjacent blocks are irrelevant, so golems can spawn partially inside adjacent solid blocks.[2] However, the spawning iron golem still must not collide with any existing entities.

Bedrock Edition
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


### Pillager outposts
Main article: Tutorials/Defeating a pillager outpost
An iron golem found within one of the cages surrounding an outpost.
Iron golems can also be found surrounding pillager outposts, confined inside dark oak cages. When freed, they can help the player by attacking any nearby pillagers. Pillagers do not attack iron golems in cages.

## Drops
See also: Tutorials/Iron golem farming

### On death
| Item |            | Roll Chance | Quantity (Roll Chance) |           |            |             |
|------|------------|-------------|------------------------|-----------|------------|-------------|
|      |            |             | Default                | Looting I | Looting II | Looting III |
|      | Poppy      | 100%        | 0–2                    | 0–2       | 0–2        | 0–2         |
|      | Iron Ingot | 100%        | 3–5                    | 3–5       | 3–5        | 3–5         |

In Bedrock Edition, trading prices are unaffected by the killing of iron golems; however, village popularity decreases by 10, affecting village iron golem behavior if the popularity ranges below -15.

## Behavior
An iron golem offering a poppy.
Iron golems wander around a village in a patrol-like fashion, staying close to buildings and other structures. Like villagers, iron golems do not wander away from a village, regardless of how they were spawned, but sometimes stand at the border of the village. 

An iron golem sometimes faces a villager as if they are conversing. Iron golems can spawn poppies in their hands and offer them to villagers, symbolizing the friendly relationship between villagers and iron golems. Baby villagers accept the poppy offered by the iron golem.‌[Bedrock Edition  only][3] Attacking an iron golem that is not player-built while the iron golem is holding out a poppy causes it to take back the poppy and attack the player instead. If the iron golem sees a target while it is offering the poppy, it runs toward the target and kills the target instead.

In Bedrock Edition, iron golems completely ignore villagers, pushing them aside while walking if a villager is in the iron golem's path, but they still offer poppies if possible.

If not within a village, iron golems slowly wander around attacking hostile mobs, (skeletons, zombies, etc.) usually making their way to a nearby village. If in that village, the iron golem doesn't leave.

Iron golems can walk up a full block height without jumping and walk over a 1 block wide hole without falling in. They avoid water, lava, fire, and cactus. Iron golems are immune to both drowning and fall damage. When in water, they sink, but can still move freely. 

When an iron golem's health reduces to 75%, cracks appear on its surface. An iron golem can be healed when the player right-clicks the chest of the iron golem with an iron ingot. This action consumes the ingot.

As with most passive and neutral mobs, iron golems can be leashed. The leashed iron golem does not try to break from the lead when it sees a hostile mob. Instead, it looks at the mob while moving. An iron golem that is leashed in mid-air moves its arms and legs while moving. If an iron golem is leashed to a fence, it attacks the hostile mob but does not follow the mob if the hostile mob goes out the attack range, as the iron golem cannot break free from fence leads.

In Java Edition, when iron golems move when provoked, they look like if they're taking strides toward the mob. Iron golems that aren't provoked move slower in Java Edition. Iron golems move faster in Bedrock Edition, as it walks like its normal walking speed, either when provoked or not provoked.  

Iron golems cannot pick up weapons or armor, but the player can use NBT commands in Java Edition  or the /replaceitem command in Bedrock Edition to give the iron golem weapons or armor, although the armor or weapons are not visible.  

### Attacking
When attacking, an iron golem moves quickly toward its target and swings its arms up violently to attack, flinging the target into the air, and dealing 7.5 × 3.75 to 21.5 × 10.75 damage in Normal difficulty. When an iron golem attacks, it also deals a long knockback range. Iron golems cannot attack targets that are three blocks high above the same ground level as the golem.

It is possible for multiple golems to hit the same target simultaneously, flinging the victim to a height proportional to the number of golems that attacked. The mob/player flung can die from fall damage.

If an iron golem attacks a group of zombies, for example, it targets one zombie to attack until that zombie dies before it attacks a different zombie, even while other zombies are attacking at the same time. The iron golem attacks hostile mobs that attack it in order.

If the mob is flung out of sight, the iron golem attacks the next mob that attacks it. Sometimes, the iron golem might attack the nearest hostile mob if they are in groups.

When an iron golem kills any mob, the player can obtain items dropped by the mob, but no experience orbs. An iron golem that kills a raid mob in Bedrock Edition also causes the mob to drop its raid loot, even when the mob wasn't attacked by the player before it was killed.

Iron golems never attack each other, as iron golems cannot "accidentally" hit another iron golem when attacking.

#### Provocation by players
An iron golem built by a player never attacks players, even when hit or when the player attacks another villager or another golem in front of the player-built golem. A player-built golem attacks the player's tamed wolf if the wolf attacks the golem.

A naturally-spawned iron golem becomes hostile toward a player who attacks a villager near an iron golem. Also, if a player has -15 popularity or less in a village, or has -100 or lower reputation with any nearby villager, naturally-spawned iron golems become hostile to that player until the player's popularity climbs above -15 and reputation with all nearby villagers goes above -100.

A village iron golem retaliates when attacked by a player (even throwing an ender pearl at an iron golem provokes it). If a village has more than one naturally-spawned iron golems and a player attacks one in front of the other(s), all of iron golems in that type may become hostile to the player.

Iron golems are not provoked by players who attack wandering traders.[4]

Throwing a positive splash potion or a positive lingering potion does not anger Iron golems.

#### Provocation by other mobs


Although they are guardians of villages, iron golems are not actually provoked when a mob attacks a nearby villager (in contrast to a player attacking a villager). With the exception of creepers and goats, they are provoked when attacked by any mobs, and by the presence of nearby monsters. Even if a witch accidentally throws a positive splash potion at an iron golem during a raid, this does not stop the iron golem from attacking the witch. Iron golems are ineffective against flying hostile mobs that don't venture into the iron golem's reach, such as ghasts and phantoms.

The list below contains mobs that can have hostile interactions with iron golems. The iron golem also attacks neutral mobs or hostile mobs that attack the player such as piglins or zombified piglins.

| Entity                                 | Iron golem actively attacks the mob? | Actively attacks the iron golem? | Notes                                                                                                                                                                                                                                                                                     |
|----------------------------------------|--------------------------------------|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Blaze                                  | Yes                                  | No                               | Blaze retaliates.                                                                                                                                                                                                                                                                         |
| Bogged‌[upcoming: JE 1.21 & BE 1.21.0] | Yes                                  | Yes                              |                                                                                                                                                                                                                                                                                           |
| Breeze‌[upcoming: JE 1.21 & BE 1.21.0] | Yes                                  | Yes                              |                                                                                                                                                                                                                                                                                           |
| Creeper                                | No                                   | No                               | Creepers can still unintentionally damage the iron golem.                                                                                                                                                                                                                                 |
| Drowned                                | Yes                                  | Partial                          | Drowned do not attack any mob that is not touching water during daytime.                                                                                                                                                                                                                  |
| Ender Dragon                           | Yes                                  | No                               |                                                                                                                                                                                                                                                                                           |
| Enderman                               | Yes                                  | No                               | Enderman retaliates.                                                                                                                                                                                                                                                                      |
| Endermite                              | Yes                                  | No                               | Endermite retaliates.                                                                                                                                                                                                                                                                     |
| Evoker                                 | Yes                                  | Yes                              |                                                                                                                                                                                                                                                                                           |
| Fox                                    | No                                   | No                               | InBedrock Edition, trusting foxes attack the iron golem if it attacks its owner. When attacked by the fox, the golem retaliates.                                                                                                                                                          |
| Ghast                                  | Yes                                  | No                               |                                                                                                                                                                                                                                                                                           |
| Giant‌[JE  only]                       | Yes                                  | N/A                              | Giants do not have any AI.                                                                                                                                                                                                                                                                |
| Goat                                   | No                                   | Randomly                         |                                                                                                                                                                                                                                                                                           |
| GuardianElder Guardian                 | Yes                                  | No                               | Guardians can still damage iron golems with their spikes defense.                                                                                                                                                                                                                         |
| Hoglin                                 | Yes                                  | No                               | Hoglin retaliates.                                                                                                                                                                                                                                                                        |
| HuskZombieZombie Villager              | Yes                                  | Yes                              |                                                                                                                                                                                                                                                                                           |
| Illusioner‌[JE  only]                  | Yes                                  | Yes                              |                                                                                                                                                                                                                                                                                           |
| LlamaTrader Llama                      | No                                   | No                               | An iron golem attacks a llama that accidentally hits the golem with its spit. After being hit by the golem, the llama deliberately attacks the golem.                                                                                                                                     |
| Magma Cube                             | Yes                                  | Yes                              |                                                                                                                                                                                                                                                                                           |
| Phantom                                | Yes                                  | No                               |                                                                                                                                                                                                                                                                                           |
| Pillager                               | Yes                                  | Yes                              |                                                                                                                                                                                                                                                                                           |
| Piglin                                 | Yes                                  | No                               | Piglin retaliates                                                                                                                                                                                                                                                                         |
| Piglin Brute                           | Yes                                  | No                               | Piglin brute retaliates.                                                                                                                                                                                                                                                                  |
| Pufferfish                             | No                                   | No                               | Iron golems only attack pufferfish if damaged by the pufferfish's defense.                                                                                                                                                                                                                |
| Ravager                                | Yes                                  | Yes                              |                                                                                                                                                                                                                                                                                           |
| Shulker                                | Yes                                  | No                               | Shulker retaliates.                                                                                                                                                                                                                                                                       |
| Silverfish                             | Yes                                  | Yes‌[BE  only]No‌[JE  only]      | Silverfish retaliates inJava Edition.                                                                                                                                                                                                                                                     |
| SkeletonStrayWither Skeleton           | Yes                                  | Yes                              |                                                                                                                                                                                                                                                                                           |
| Slime                                  | Yes                                  | Yes                              |                                                                                                                                                                                                                                                                                           |
| Snow Golem                             | No                                   | No                               | The iron golem only retaliates if a snow golem accidentally hits it with a snowball.                                                                                                                                                                                                      |
| SpiderCave Spider                      | Yes                                  | Partial                          | Spiders are hostile toward iron golems when light level is below 12. Otherwise, they retaliate only if attacked.                                                                                                                                                                          |
| Vex                                    | Yes                                  | Partial                          | A vex attacks an iron golem rarely when the vex is near to golem. It attacks immediately when an evoker summons three vexes.                                                                                                                                                              |
| Villager                               | No                                   | No                               | An iron golem retaliates against a villager who accidentally damages it by setting off a firework.‌[Java Edition  only][5]                                                                                                                                                                |
| Vindicator                             | Yes                                  | Yes                              |                                                                                                                                                                                                                                                                                           |
| Warden                                 | Yes                                  | Yes                              |                                                                                                                                                                                                                                                                                           |
| Witch                                  | Yes                                  | Yes‌[BE  only]Partial‌[JE  only] | InJava Edition, witches attack iron golems if patrolling in anillager patrol.                                                                                                                                                                                                             |
| Wither                                 | Yes                                  | Yes                              |                                                                                                                                                                                                                                                                                           |
| Wolf                                   | No                                   | No                               | Tamed wolves only attack the iron golem if it attacks its owner, or the owner attacks the golem. When attacked by the wolf, the golem retaliates. A player-built iron golem attacks the player's wolves if attacked by the wolf. Iron golems and untamed wolves never attack one another. |
| Zoglin                                 | Yes                                  | Yes                              |                                                                                                                                                                                                                                                                                           |
| Zombified Piglin                       | Yes                                  | No                               | Zombified piglins retaliates.                                                                                                                                                                                                                                                             |
| All other mobs                         | No                                   | No                               |                                                                                                                                                                                                                                                                                           |

An iron golem looks down at a husk, but cannot attack the husk.
A naturally-spawned iron golem knows where raiding illager locations are from behind solid walls and from underground and attempts to move toward them. An iron golem created by the player or summoned by a command cannot detect raiders through obstructions. Iron golems also looks down or looks up if the hostile mob is above or below the iron golem.

### Being attacked
Zombies (and variants), zoglins, skeletons (and variants), spiders, cave spiders, slimes, magma cubes, withers, ravagers and illagers naturally attack iron golems on sight and may cause major damage, especially if the mobs attack in groups. In Bedrock Edition, silverfish and witches also naturally attack iron golems without provocation.

Iron golems have 100% knockback resistance from normal attacks. They can still be knocked back by the Knockback enchantment on swords and the Punch enchantment on bows.‌[Java Edition  only]

### Cracking
Iron golems have different stages of being cracked to show their health. When their health is above 74 × 37, they do not have any cracks. When their health is between 50 × 25 and 74 × 37, some cracks appear. When their health is between 25 × 12.5 and 49 × 24.5, they appear more cracked. When their health is lower than 25 × 12.5, many cracks are visible.

- No deterioration  More than 75% of health remaining
- Low deterioration  More than 50% but no more than 75% of health remaining
- Average deterioration  More than 25% but no more than 50% of health remaining
- Strong deterioration  No more than 25% of health remaining

### Healing
Using an iron ingot on an iron golem restores its health by 25 × 12.5.

## Preferred path

  

This feature is exclusive to  Bedrock Edition. 


See also: Villager § Preferred path

Like villagers, iron golems in Bedrock Edition use a strategy of pathfinding that prioritizes walking on certain "low-cost" blocks.

| Preferred Path Blocks                                                                                                                                                                                                                                                                           | Block Cost |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| Dirt pathSmooth Sandstone                                                                                                                                                                                                                                                                       | 0          |
| CobblestoneStone Stone Bricks Sandstone Mossy Cobblestone Slabs Planks Bricks Nether Bricks Red Nether Bricks End Stone Bricks Red Sandstone Stained Glass Glass Glowstone Prismarine Block of Emerald Block of Diamond Block of Lapis Lazuli Block of Gold Block of Redstone Glazed Terracotta | 1          |
| BedsLectern Composter Grindstone Blast Furnace Smoker Fletching Table Cartography Table Brewing Stand Smithing Table Cauldron Barrel Loom Stonecutter                                                                                                                                           | 50         |
| other                                                                                                                                                                                                                                                                                           | 1.5        |
| Jump cost                                                                                                                                                                                                                                                                                       | 5          |

Iron golems attempt to walk on a one-block-wide path, despite them being two blocks wide. An iron golem favors a wider path if it sees one.

### Climbing
Iron golems can climb ladders or vines if the ladder or vine is in its path, or if pushed onto a ladder or vine.

## Data values
### ID
Java Edition:

| Name       | Identifier | Entity tags        | Translation key             |
|------------|------------|--------------------|-----------------------------|
| Iron Golem | iron_golem | fall_damage_immune | entity.minecraft.iron_golem |

Bedrock Edition:

| Name       | Identifier | Numeric ID | Translation key        |
|------------|------------|------------|------------------------|
| Iron Golem | iron_golem | 20         | entity.iron_golem.name |

### Entity data
Iron golems have entity data associated with them that contain various properties.

Java Edition:

Main article: Entity format

 Entity data
Additional fields for mobs that can become angry
Tags common to all entities
Tags common to all mobs
 PlayerCreated: 1 or 0 (true/false) - if true, this golem is player-created and never attacks players.

Bedrock Edition:

See Bedrock Edition level format/Entity format.
