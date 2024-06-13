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

#### By mobs
In Java Edition, the movement of a mount is controlled by its passenger, if both the mount and the passenger are mobs (not players). However, there are some exceptions:

- Mobs with theirNoAINBT being true cannot be controlled by any mob, though they can be controlled by players.
- Slimes and magma cubes cannot control any mob, which is controlled by entity type tagnon_controlling_rider.

In Bedrock Edition, for most of rideable mobs, when its mob passenger tries to chase and attack player or mobs, the passenger takes control, otherwise the mount controls movement. The following mobs are exceptions:

- Hoglin: cannot be controlled by mob passengers.
- Strider: cannot be controlled by mob passengers.

In Bedrock Edition, some AI goals are disabled if the entities is ridden by or riding an entity. For example in Bedrock Edition, when a zombie rides a pig, the pig controls the movement when they are idle; but the pig cannot follow players holding a carrot even when the zombie is idle; the pig controls the movement when it is breeding and the zombie is idle; the zombie controls the movement when it targets a player even when the pig is breeding.  

When being controlled by its passenger, the mount uses its own walk speed. However, in Java Edition, speed modifier of its passenger's AI is applied. For example, spiders ridden by a chicken, a sheep, or a llama have different speed when they follows a player holding seeds, wheat, or hay block, respectively. Because the AIs of chicken, sheep, and llama have different speed modifiers. While in Bedrock Edition, the speed modifier (speed multiplier) for being controlled is defined for each entity type (by minecraft:behavior.mount_pathing component).

#### Behavior
For an entity that is ridden by multiple passengers, only the front passenger has control over the mount. If a player and other entities ride it at the same time, the player becomes the front passenger.

In Java Edition, the passenger controlling its mount can be targeted with /execute on controller.

In Java Edition, mobs cannot float on water when they are controlled. They are submerged in the water instead. In Bedrock Edition, they can float on water when being controlled, however, because they float up and down more fiercely than in Java Edition, their heads are often submerged so that the passenger is evicted，while tall mobs can float on water without their heads being submerged and the passenger is not evicted.

### Dismounting
Mobs usually cannot leave their mounts on their own AI (there're some exceptions, e.g. in Java Edition, baby piglins stop riding baby hoglins when being hurt), but there are many ways to make passengers leave their mounts:

- When the passenger is a player, the player usesdismountcontrol.
- When the passenger is a player, the player starts sleeping by usinguseon a bed.
- When the passenger is a player, the player starts riding another mount.
- When the mount is dead or destroyed.
- When the passenger starts being leashed with alead.
- When riding chicken, pig, ravager, spider, strider, horses, donkeys, mules, zombie horses, llamas, trader llamas and camels underwater, being driven off by them. InJava Edition, this is controlled bydismounts_underwaterentitytag.[3]
- Being driven off by the mount (e.g. untamed horses, donkeys and llamas, underwater boats, minecarts on a poweredactivator rail, etc.).
- InJava Edition, When the passenger finishes eating achorus fruit.
- InBedrock Edition, when the passenger is pulled by afishing rod.
- InBedrock Edition, when the passenger is teleported by/tp.
- InBedrock Edition, when the passenger is a piglin, and it converts to a zombified piglin.
- Dismounting by/ridecommand.

## Riding in vanilla game
### Ridden by player
Players can ride the following entities by pressing use on the entity:

- Saddledpig
- Saddledstrider
- Adulthorse
- Adultdonkey
- Adultmule
- Tamedskeleton horse‌[Java Edition  only]/ Adultskeleton horse‌[Bedrock Edition  only]
- Tamedzombie horse‌[Java Edition  only]
- Adultllama
- Adulttrader llama
- Adultcamel
- Minecart
- Boat
- Boat with Chest

### Minecart
A mob can ride a minecart when pushing by a moving minecart on rails in Java Edition or when colliding with a minecart in Bedrock Edition. In Bedrock Edition, armor stand can also be picked up.

Ender dragons, wardens, and withers cannot be picked up by a minecart. In Java Edition, iron golems cannot be picked up either.

In Bedrock Edition, unlike wardens, ender dragons can ride a minecart via /ride command; withers cannot ride a minecart via /ride though a success message is returned.

### Boat
Mobs can be picked up into a boat or a boat with chest when they collide with the side of the boat or boat with chest. In Java Edition, a boat being ridden by a player cannot pick up a mob. In Bedrock Edition, mobs can be picked up by a boat being ridden by a player.

Mobs wider than the width of a boat cannot be picked up. Wardens and withers cannot be picked up.

In Bedrock Edition, mobs wider than the width of a boat can ride a boat via /ride command. Unlike wardens, ender dragons can ride a boat via /ride command; withers cannot ride a boat via /ride though a success message is returned.

### Jockey
Main article: Jockey
#### Spider jockey
Main article: Spider Jockey
Spider jockeys are the rare appearance of a spider being ridden by a skeleton.

#### Chicken jockey

  

This feature is exclusive to  Java Edition. 


Main article: Chicken Jockey
Chicken jockeys are the rare appearance of a baby zombie, baby zombified piglin, baby zombie villager, baby husk, or baby drowned riding a chicken.

#### Jockey of baby zombie

  

This feature is exclusive to  Bedrock Edition. 


In Bedrock Edition, 15% naturally spawned baby zombies, baby husks, and baby zombie villagers try to find a mount when it tries attacking a villager, player, or iron golem, which can ride:

- Adultchickens
- Untamedocelots
- Untamedcats
- Untamedwolves
- Adultzombies
- Adulthusks
- Adultzombie villagers
- Adultzombified piglins
- Cows
- Adult unsaddledpigs
- Sheep
- Adult untamedhorses
- Adult untameddonkeys
- Adult untamedmules
- Adultskeleton horses
- Adultzombie horses
- Mooshrooms
- Spidersthat were not spawned as a jockey mount
- Cave spidersthat were not spawned as a jockey mount
- Pandas

#### Skeleton Horseman
Main article: Skeleton Horseman
Skeleton horseman is a jockey consisting of a skeleton (or stray and wither skeleton) riding a skeleton horse. Skeleton horsemen spawn only from a "skeleton trap horse".

### Baby piglin riding baby hoglin
Main articles: Piglin and Hoglin
Baby piglins play with baby hoglins, running around and riding upon them. Up to 3 baby piglins may stack on top of each other while riding a baby hoglin. In Bedrock Edition, a baby hoglin can support 3 baby piglins, which looks like they are stacked one by one. However, in Java Edition, baby piglins ride each other and are indeed stacked one by one, instead of all riding on the hoglin.

### Strider or zombified piglin riding strider
Main articles: Strider and Zombified Piglin
For every strider that spawns, there is a 1 in 10 chance of an additional baby strider to spawn riding on top of the previous strider. Zombified piglins have a 1 in 30 chance of spawning on top of a strider.

### Illager riding ravager
Main article: Ravager
A ravager generated in raids may generate with a pillager, evoker or vindicator riding on it.

### Parrot riding player
Main article: Parrot
A tamed parrot on the ground can be made to perch on its player's shoulder by moving through the parrot. In Bedrock Edition, technically the parrot is riding the player. In Java Edition, technically the parrot on the shoulder is not an entity.

## Valid riding combinations in vanilla

  

This feature is exclusive to  Bedrock Edition. 


In Bedrock Edition, whether an entity is rideable is mainly defined with minecraft:rideable component and entity familliers in vanilla behavior packs. Besides, some entities have hardcoded riding behaviors, for, example, wardens being not able to riding a boat, boat doing not pick up adult horses although they can ride boats via /ride command.

In the following table, none means that the entity is rideable by these families no matter what component groups it has. Multiple components separated by | symbols means that the entity must have at least one of them to be rideable by these families.

| rideable entity | valid families for specific component_groups                                                                                            |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Boat            | `minecraft:can_ride_default | minecraft:can_ride_bamboo`: all                                                                           |
| Boat with chest | `minecraft:can_ride_default | minecraft:can_ride_bamboo`: all                                                                           |
| Camel           | `minecraft:camel_adult`: player                                                                                                         |
| Cat             | `minecraft:cat_wild`: zombie                                                                                                            |
| Cave spider     | `minecraft:spider_jockey | minecraft:spider_stray_jockey | minecraft:spider_wither_jockey`: skeleton; Otherwise: zombie                 |
| Chicken         | `minecraft:chicken_adult`: zombie                                                                                                       |
| Cow             | `none`: zombie                                                                                                                          |
| Donkey          | `minecraft:donkey_wild`: player, zombie;`minecraft:donkey_tamed`: player                                                                |
| Hoglin          | `minecraft:hoglin_baby`: piglin                                                                                                         |
| Horse           | `minecraft:horse_wild`: player, zombie;`minecraft:horse_tamed`: player                                                                  |
| Husk            | `minecraft:zombie_husk_adult`: zombie                                                                                                   |
| Llama           | `minecraft:llama_wild | minecraft:llama_tamed`: player                                                                                  |
| Minecart        | `none`: all                                                                                                                             |
| Mooshroom       | `none`: zombie                                                                                                                          |
| Mule            | `minecraft:mule_wild`: player, zombie;`minecraft:mule_tamed`: player                                                                    |
| Ocelot          | `minecraft:ocelot_wild`: zombie                                                                                                         |
| Panda           | `none`: zombie                                                                                                                          |
| Pig             | `minecraft:pig_unsaddled`: zombie;`minecraft:pig_saddled`: player                                                                       |
| Player          | `none`: parrot_tame                                                                                                                     |
| Ravager         | `none`: pillager, vindicator, evocation_illager                                                                                         |
| Sheep           | `minecraft:rideable_sheared | minecraft:rideable_wooly`: zombie                                                                         |
| Skeleton horse  | `minecraft:skeleton_horse_adult`: player, skeleton, zombie                                                                              |
| Spider          | `minecraft:spider_jockey | minecraft:spider_stray_jockey | minecraft:spider_wither_jockey`: skeleton; Otherwise: zombie                 |
| Strider         | `minecraft:strider_saddled`: player;`minecraft:strider_piglin_jockey`: player, zombie_pigman;`minecraft:strider_parent_jockey`: strider |
| Trader llama    | `minecraft:llama_wild | minecraft:llama_tamed`: player                                                                                  |
| Wolf            | `minecraft:wolf_angry | minecraft:wolf_wild`: zombie                                                                                    |
| Zombie          | `minecraft:zombie_adult`: zombie                                                                                                        |
| Zombie horse    | `minecraft:horse_adult`: zombie                                                                                                         |
| Zombie piglin   | `minecraft:pig_zombie_adult`: zombie                                                                                                    |
| Zombie villager | `adult`: zombie                                                                                                                         |

## Posture
The following passengers have riding posture when riding:

- Player
- Zombie
- Zombie Villager
- Husk
- Drowned
- Skeleton
- Stray
- Wither Skeleton
- Piglin
- Piglin Brute
- Zombified Piglin
- Pillager
- Vindicator
- Evoker
- Enderman‌[JE  only]
- Illusioner‌[JE  only]
- Giant‌[JE  only]

Witches, villagers, iron golems, and wandering traders do not have a riding posture although similar mobs do.[4]

### Gallery
#### Player
- Alex
- Ari
- Efe
- Kai
- Makena
- Noor
- Steve
- Sunny
- Zuri

#### Illagers
- Vindicator
- Pillager
- Evoker
- Illusioner

#### Monsters
- Zombie
- Husk
- Drowned
- Skeleton
- Stray
- Wither skeleton
- Piglin
- Piglin brute
- Zombified piglin
- Enderman

#### Zombie Villagers
- Unemployed
- Librarian
- Mason
- Nitwit
- Shepherd
- Toolsmith
- Weaponsmith
- Armorer
- Butcher
- Cartographer
- Cleric
- Farmer
- Fisherman
- Fletcher
- Leatherworker

