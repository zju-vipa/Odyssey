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

