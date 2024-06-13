# Riding
Riding (aka. mounting) is the behavior that allows an entity to mount another entity.

## Contents
- 1 Behaviors
	- 1.1 Passengers
	- 1.2 Mounts
	- 1.3 Controlling
		- 1.3.1 By players
		- 1.3.2 By mobs
		- 1.3.3 Behavior
	- 1.4 Dismounting
- 2 Riding in vanilla game
	- 2.1 Ridden by player
	- 2.2 Minecart
	- 2.3 Boat
	- 2.4 Jockey
		- 2.4.1 Spider jockey
		- 2.4.2 Chicken jockey
		- 2.4.3 Jockey of baby zombie
		- 2.4.4 Skeleton Horseman
	- 2.5 Baby piglin riding baby hoglin
	- 2.6 Strider or zombified piglin riding strider
	- 2.7 Illager riding ravager
	- 2.8 Parrot riding player
- 3 Valid riding combinations in vanilla
- 4 Posture
	- 4.1 Gallery
		- 4.1.1 Player
		- 4.1.2 Illagers
		- 4.1.3 Monsters
		- 4.1.4 Zombie Villagers
- 5 Achievements
- 6 Advancements
- 7 History
- 8 References

## Behaviors
Riding connects one entity to another. An entity riding another entity is called a passenger (aka. rider), and an entity being ridden is called a mount (aka. vehicle). An entity can be both a passenger and a mount at the same time if it is riding another entity while being ridden by other entities.

An entity can only ride at most one entity at the same time. Most entities support only one passenger, but boat, bamboo raft and camel can support two passengers at the same time. In Java Edition, by modifying entity NBT through commands, an entity may be ridden by any number of entities. In Bedrock Edition, a baby hoglin can support 3 baby piglins, which looks like they are stacked one by one. However, in Java Edition, baby piglins ride each other and are indeed stacked one by one, instead of all riding on the hoglin. In Bedrock Edition, a player can support 2 parrots. However, in Java Edition, parrots become not entities and are stored into the player's NBT data when sitting on the shoulders of a player.

The collision and movement of a mount is not affected by its passengers, so the accessible position for the mount may put the passengers into danger, for example, making the passenger's head inside of a block and causing suffocation.[1] However, in Java Edition, a passenger riding on a passenger of an entity collides with the entity, resulting bugs like MC-71998.

When a player leaving the world, all the entities that is ridden by or riding it also disappear from the world, and will respawn with the player when the player rejoins the world, unless the affected entity has another player passenger.

In Java Edition, with /ride command, all entities are rideable by any entity, except marker and player, which never can be ridden. In Bedrock Edition, only some riding combinations are valid for /ride command, see #Valid riding combinations in vanilla

In Java Edition, when a leashed mob starts riding, it drops the lead. In Bedrock Edition, a leashed mob cannot start riding unless using /ride command, and when starting riding, it doesn't drop the lead.

A passenger cannot set its mount as its target for attack, a mount cannot set its passenger as the target for attack either, unless using /damage command. In Bedrock Edition, they cannot attack each other at all even when they target each other through /damage command.

### Passengers
Passengers have the following behaviors:

- The position of a passenger is fixed on its mount, that is, the position and movement of a passenger cannot be affected by any other gameplay features.
	- Passengers have no collision with entities and blocks.
	- Passengers cannot be moved byknockback,explosion,fishing rod, andtridentwithriptideenchantment.
	- InBedrock Edition, passengers cannot be teleported bychorus fruitandend gateway.
	- InJava Edition, when a passenger goes into anend gateway, it is teleported with its mount.
	- When ashulkeris a passenger, it cannot teleport on its own. InJava Edition, anendermancannot teleport on its own either.
	- InJava Edition, passengers cannot be teleported by/tp. InBedrock Edition, passengers dismount when teleported by/tp.
- Passengers cannot be transported bynether portalsorend portals.[2]
- Passengers do not calculate the falling height. When starting riding, the falling height is reset.
- When a player is a passenger, it cannot interact with its mount.
- When a player is a passenger, it cannot interact with other passengers on the same mount as its.
- When a player is a passenger and the mount is a mob or an armor stand, thehealthbar of the mount is displayed on the player'sHUDin the form of. InJava Edition, the hunger bar is replaced by it inSurvivalorAdventuremode.

### Mounts
Mounts have the following behaviors:

- Mounts cannot be transported by nether portals or end portals.[2]
	- InBedrock Edition, mounts cannot be teleported byend gateway.
- When a mount receivesfalling damage, all passengers also receive falling damage.
	- InJava Edition, if a mount is immune to falling damage, the damage is not passed to passengers.
	- InBedrock Edition, even if a mount is immune to falling damage, the damage is still passed to passengers.

### Controlling
#### By players
The movement of the following mounts are controlled by the player when being ridden by it:

- Saddledhorses
- Saddleddonkeys
- Saddledmules
- Saddledcamels
- Pigscan be controlled by players holding acarrot on a stick.
- Saddled‌[Java Edition  only]striderscan be controlled by players holding awarped fungus on a stick.
- Saddledskeleton horses‌[Java Edition  only]/ Adultskeleton horses‌[Bedrock Edition  only]
- Saddledzombie horses‌[Java Edition  only]
- Boats
- Boats with chests

In Java Edition, though minecarts on rails receive the input from its player passenger, they are not regarded as being controlled in game. In Java Edition, boats and boats with chest are regarded as being controlled by a armor stand when being ridden by it, but never move.

The following mounts have the ability of "jumping charging". When players ride them, the experience bar on HUD will be replaced by jumping charging bar:

- Saddledhorses
- Saddleddonkeys
- Saddledmules
- Saddledskeleton horses‌[Java Edition  only]/ Adultskeleton horses‌[Bedrock Edition  only]
- Saddledzombie horses‌[Java Edition  only]

When a player ride the following entities, pressing inventory opens the interaction interface of these creatures instead of the normal item bar interface:

- Tamedhorse
- Tameddonkey
- Tamedmule
- Tamedllama
- Tamedtrader llama
- Camel
- Tamedskeleton horse‌[Java Edition  only]
- Tamedzombie horse‌[Java Edition  only]
- Boat with chest

