# Tutorials/Summoning jockeys
Summoning a jockey (a mob riding on top of another mob) can be useful for adventure maps and interesting to experiment with.

## Contents
- 1 Generation
	- 1.1 Natural Generation
	- 1.2 Command Generation
		- 1.2.1 Java Edition
		- 1.2.2 Bedrock Edition
- 2 Behavior
	- 2.1 Passenger Behavior
	- 2.2 Mount Behavior
		- 2.2.1 Java Edition
		- 2.2.2 Bedrock Edition
	- 2.3 Examples

## Generation
### Natural Generation
The few naturally-spawning jockeys in the game include spider jockeys (skeleton riding a spider), chicken jockeys (a baby zombie riding a chicken), also a skeleton trap (skeletons riding skeleton horses), a ravager rider (illager riding ravager), or a strider jockey (zombified piglin or a baby strider riding a strider).

Additionally, in Bedrock Edition baby zombies, husks, or zombie villagers can ride other mobs than chickens, though drowned and zombified piglin jockey doesn't exist. Cave spiders can also spawn as spider jockeys.

A spider jockey has a 1% chance of spawning out of every spider or cave spider‌[Bedrock Edition  only] spawned, and in the Nether, there is an 80% chance of a spider jockey becoming a wither skeleton jockey, in snowy biomes there is 80% chance of a spider jockey with the stray rider. In Java Edition, baby zombies have a 5% chance of spawning on a chicken and an additional 5% chance if there are no chickens in a 10×6×10 area, while in Bedrock Edition, baby zombies, husks, or zombie villagers has 15% chance to become jockey when try to attack a player, villager, wandering trader, or golems and can ride more mobs (not just chicken). For a skeleton trap to spawn, there is a small fraction of a chance they will spawn under a lightning strike in a group of 4 (0.75–1.5% chance on Easy, 1.5–4% on Normal, and 2.8125–6.75% on Hard, depending on regional difficulty).

### Command Generation
#### Java Edition
They can also each be summoned via commands:

- Spider Jockey:

/summon spider ~ ~ ~ {Passengers:[{id:skeleton,HandItems:[{id:bow,Count:1b}]}]}

- Chicken Jockey:

/summon chicken ~ ~ ~ {Passengers:[{id:zombie,IsBaby:1}]}

- Skeleton Trap:

/summon skeleton_horse ~ ~ ~ {SkeletonTrap:1}

- An evoker riding ravager:

/summon minecraft:ravager ~ ~ ~ {Passengers:[{id:evoker}]}

- a pillager riding ravager:

/summon minecraft:ravager ~ ~ ~ {Passengers:[{id:pillager,HandItems:[{id:crossbow,Count:1b}]}]}

- a vindicator riding ravager:

/summon minecraft:ravager ~ ~ ~ {Passengers:[{id:vindicator,HandItems:[{id:iron_axe,Count:1b}]}]}

- Enderman Jockey:

/summon chicken ~ ~ ~ {Passengers:[{id:enderman}]}

- Baby Zombie Riding Pig:

/summon pig ~ ~ ~ {Passengers:[{id:zombie,IsBaby:1}]}

- Piglin Riding Hoglin with Crossbow:

/summon hoglin ~ ~ ~ {IsImmuneToZombification:1b,CannotBeHunted:1b,Passengers:[{id:piglin,IsImmuneToZombification:1b,HandItems:[{id:crossbow,Count:1b}]}]}

#### Bedrock Edition
Only some jockeys can be summoned via commands:

- Skeleton Trap

/summon skeleton_horse ~ ~ ~ minecraft:set_trap

- 
	- This command will spawn 4 skeleton horsemen.

- Ravager Rider

/summon ravager ~ ~ ~ minecraft:spawn_for_raid_with_evoker_rider

- 
	- This command will spawn an evoker riding ravager for the raid.

/summon ravager ~ ~ ~ minecraft:spawn_with_pillager_rider

- 
	- This command will spawn a pillager riding ravager.

/summon ravager ~ ~ ~ minecraft:spawn_with_vindicator_rider

- 
	- This command will spawn a vindicator riding ravager.

/summon ravager ~ ~ ~ minecraft:spawn_for_raid_with_pillager_rider

- 
	- This command will spawn a pillager riding ravager, but the pillager drops special loot upon death and is also for the raid.

/summon ravager ~ ~ ~ minecraft:spawn_with_pillager_captain_rider

- 
	- This command will spawn a pillager riding ravager, but the pillager israid captain.

/summon ravager ~ ~ ~ minecraft:spawn_with_vindicator_captain_rider

- 
	- This command will spawn a vindicator riding ravager, but the vindicator is raid captain.

## Behavior

  

This article needs to be updated. 
Please update this page to reflect recent updates or newly available information.Reason: far different from the behavior in current version


### Passenger Behavior
3 wolves turned hostile, using their cow mounts to chase and attack the player.
The "passenger" or the mob on top, will always have control over the mob it is mounted on as of Java Edition 1.12. This means no matter what the mount's intentions (attacking a villager, for example), the passenger will always have control over the mount. For example, if there is a skeleton on the bottom with a zombie on top, the zombie will move the mount itself and pursue a villager instead of you (only if it notices the villager first, like all zombies). Mobs on the bottom have small resistance, they can move slowly towards their own intentions (attacking a player) but the second the passenger moves the mount will be forced to move to that location.

- /summon skeleton ~ ~ ~ {Passengers:[{id:zombie,HandItems:[{id:iron_shovel,Count:1b}]}]}

In a nutshell, the passenger will behave regularly if they are mounted on a mob, but they will have a speed boost (equivalent to the players walking speed, or the passenger speed if the Passenger's speed is faster than the players' speed). For example, if there is a wolf mounted on a cow, and you punch the wolf, the wolf will ride the cow towards you and inflict damage, and it will also make nearby wolves (even wolf jockeys) hostile. If a skeleton mounts a mob, it can strafe (as skeletons do when attacking). The only exception are endermen. They will teleport away (with the passenger), if a projectile is shot through them. However, if the enderman is the passenger, it will not teleport away but it cannot be damaged by projectiles.

- /summon cow ~ ~ ~ {Passengers:[{id:enderman}]}

-If a passenger is teleported by the player it will dismount the passenger and leave the mount at the previous location. For example, if you teleport all skeletons to your location, it will take all the skeletons off the spiders and teleport them to your location.

-Passengers can be infinitely stacked as of 1.12, if you stack the Passengers tag correctly.

- /summon spider ~ ~ ~ {Passengers:[{id:skeleton,Passengers:[{id:zombie,Passengers:[{id:creeper,Passengers:[{id:enderman,Passengers:[{id:blaze}]}]}]}]}]}

6 different Monsters stacked on top of each other
