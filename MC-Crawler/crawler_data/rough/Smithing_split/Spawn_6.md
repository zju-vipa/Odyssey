## Despawning
This article is about Mob Despawning.  For Item Despawning, see Item § Behavior.
### Java Edition
Various mob spawning ranges, illustrated.
All monster, ambient, and aquatic mobs excluding shulkers, withers, elder guardians and ender dragons despawn unless they have been marked persistent. Other mobs that are not monster, ambient, or aquatic that do despawn include ocelots, stray cats, wandering traders, and untamed trader llamas.

- A mob that has had no player within 32 blocks of it for more than 30 seconds, or 10 seconds if in low light levels, has a1⁄800chance of despawning on each gametick(1⁄20of a second), which is a 2.47% chance per second. Therefore, the mob population declines so that half remains after 27.75 seconds, and the average lifetime of monsters not within 32 blocks of a player is 40 seconds (afterthe initial 30 seconds have elapsed).
- Mobs other than fish despawn immediately if no player is within 128 blocks of it, while fish despawn if no player is within 64 blocks.[6]
	- This is a Euclidean sphere, not a cylinder from map top to bottom and not ataxicabsphere (an octahedron). Example: A mob at 0/y/0 remains at least 10 seconds (as above) if the player moves to 65/y/65 (real distance 91.9), but despawns immediately if the player moves to 91/y/91 (real distance 128.7).
	- Thechunkthe mob is in must still be loaded for the mob to despawn. Otherwise, the mob is saved until thechunk is loadedagain. For example, if a player enters anether portalwhile being chased by a spider, the spider is saved, and it resumes chasing the player coming back through the same portal. In the case of a player reloading chunks, the loading happens before the player is added, meaning they may despawn.
- Ocelots and most monster mobs (including those that are holding items) despawn if the difficulty is set to Peaceful, regardless of where the player is located. Monster mobs that do not despawn include hoglins, piglins, and shulkers in all editions, as well as vindicators, zoglins, piglin brutes, and evokers inBedrock Edition.
- For despawning to occur, there must be at least one non-spectator player in the dimension.
- Chickens that originally spawned aschicken jockeysfollow zombie despawn rules, rather than chicken despawn rules.
- Wandering traders and trader llamas despawn after 40-60 minutes (2-3 in game days). They also despawn sooner if all the trades are locked.‌[Bedrock Edition  only][verify]
- Endermites despawn after 2 minutes unless named with a name tag or have persistent tag.
- Wardens despawn after 1 minute if they couldn't detect a vibration or smell by any mob or player.



Mobs are persistent, meaning they do not despawn and do not count toward the mob cap, when they:

- are a passenger to another mob.
- are riding aboator aminecart.[7]
- spawned as part of agenerated structure.
- have had something added to theirinventory, including having somethingdispensedupon them (such as asaddle) or something they have picked up, but never for anything they spawn with. This includes dolphins playing with items[verify].
- have been named with aname tag. However, one created from a renamedspawn eggdoes despawn as normal.
- have had the NBT tag{PersistenceRequired: 1b}set on them, whether by being summoned with it, or by being set manually with/data mergeor/data modify‌[JE  only]. This is also the only way to prevent wandering traders from despawning.

Following mobs also have another way to prevent despawning and do not count toward mob cap:

- Enderman: During the time that they hold a block
- Fish(all variants),axolotlsandtadpoles: Spawned as a result of placing out of abucket of mob.
- Zombie villagers: If they were converted from avillagerthat has been traded with. This still counts toward the hostile mob cap.[8]
- Zombified piglinsandwitches: If they were converted from apigorvillagerstruck by lightning.
- Hoglins: If acrimson fungusisusedon them.Zoglinsas a result of hoglins have crimson fungususedon them before they zombify also do not despawn.

### Bedrock Edition
In Bedrock Edition, like Java, despawning occurs based on distance and chance.

- On simulation distances 6 and higher, almost all environmentally spawned mobs immediately despawn when they are either (1) in a chunk at the edge of the simulation distance (technically, a chunk not fully surrounded by 8 chunks that were simulated on the last game tick), or (2) more than 128 blocks from the nearest player.
- On simulation distance 4, mobs immediately despawn when they are more than 44 blocks from the nearest player.
- Fishdespawn at a shorter distance, when they are more than 40 blocks from the nearest player on all simulation distances.
- Mobs more than 32 blocks from the nearest player have a 1 in 800 chance to despawn on each game tick if they have not taken damage for 30 seconds.

Mobs with persistence do not despawn. Mobs gain persistence in the following ways:

- The entity interacts with a player (except for attacking, which does not count as a persistence-inducing interaction):
	- Is ridden by the player.
	- Is named with aname tag.
	- Is tempted withfood.
	- Isbred, or born as a result of breeding (except for turtles hatched from eggs before 1.17.10[9]).
	- Is tamed by the player.
	- Is summoned using the/summoncommand or a spawn egg.
	- Iscured from being a zombie villager.
	- Is spawned by the player triggering askeleton trap(spawnsskeletonsandskeleton horses).
- The entity picks up an item.
- The entity is spawned during the generation of a certain kind ofstructure:
	- Shulkerspawned in anend city.
	- Witchspawned in aswamp hut.
	- Villagerorzombie villagerspawned in anigloo.
	- Villager or animals spawned in a village.
	- Zombie villager or animals spawned in azombie village.
	- Vindicatororevokerspawned in awoodland mansion.
- The entity is spawned in a raid.

The following entities always have persistence: 

- Ender Dragon
- Wither
- Elder Guardian
- Evoker
- Vindicator
- Iron Golem
- Snow Golem
- Villager
- Armor Stand
- Minecart
- Painting
- Agent‌[BE & edu  only]
- Camera‌[BE & edu  only]
- NPC‌[BE & edu  only]


