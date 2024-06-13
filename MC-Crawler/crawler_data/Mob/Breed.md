# Breeding
Breeding is a game mechanic that allows certain mobs, including villagers and many animals, to produce offspring.

## Contents
- 1 Mechanics
	- 1.1 Love mode
	- 1.2 Breeding foods
	- 1.3 Villagers
- 2 Baby mobs
	- 2.1 Ageable
	- 2.2 Monsters
- 3 Similar mechanics
	- 3.1 Allay duplication
	- 3.2 Shulker duplication
- 4 Achievements
- 5 Advancements
- 6 History
- 7 Issues
- 8 Trivia
- 9 Gallery
	- 9.1 Screenshots
- 10 See also
- 11 References

## Mechanics
A cow following the player.
Most animals that can be bred have a food item used to lead and breed it (there are a few special cases, described below). Once an animal notices a player holding its food, it follows the player until either the player is out of range, the player stops holding the item, it begins the breeding process, or it is attacked. Baby animals behave the same way. Most animals are uninterested in food lying on the ground, and those that are do not breed from eating this food; animals breed only when fed by a player. One item per parent is needed to breed a single baby.

### Love mode
When an animal is fed its food, it enters "love mode", preparing to breed with another animal of the same species that is also in love mode. Animals that are in love mode emit heart particles constantly. When both animals are fed, they pathfind toward each other, up to eight blocks away. The two animals walk into each other for about two and a half seconds, and then drop 1–7 and end love mode to produce their offspring, the method of which depends on the animal. Most animals immediately spawn a baby animal at the feet of the parents, usually of the same species as their parents, with the exception of mules, which cannot breed with each other and must be bred via the union of a horse and donkey. Some animals lay eggs, but the method and location they perform this varies from animal to animal. Chickens are the only animals that can both directly produce babies and lay eggs, as well as the only animals that lay eggs without being fed. After breeding, the parents cannot be fed to breed again for five minutes, but they (and their babies) always follow players holding breeding items. An animal exits love mode if it does not breed 30 seconds after being fed, but it immediately becomes able to be fed and enter love mode again.

The number of animals that are produced starting from a single pair of animals, assuming the offspring is fully grown before breeding again, is represented by this sequence: (OEIS A061418)

a1=2a2=3a3=4a4=6a5=9a6=13a7=19⋮an+1=⌊32an⌋⋮

where ⌊x⌋ is the floor function.

The nth term of the sequence can also be computed with this formula: an=⌈K×(3/2)n⌉ where K=1.08151366859... and ⌈x⌉ is the ceiling function. The constant K is defined to be (2/3)×K(3) (see OEIS A083286)

### Breeding foods
| Mob                                          | Items                                                                                                                                 | Other                                                                                                                                                                                                                                                                                                                                                                                                                               |
|----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Horse (Tamed) Donkey (Tamed)                 | Golden Apple Enchanted Golden Apple Golden Carrot                                                                                     | These mobs must be tamed by repeatedly mounting them before they can breed. They can be tamed faster by being fed. A horse breeding with a donkey produces amule. Mules cannot breed.The following items cannot be used for leading or breeding, but can be used to feed an untamed horse, donkey, or mule, grow a baby, or for healing:Sugar Wheat Apple Hay Bale                                                                  |
| Cow Goat Mooshroom Sheep                     | Wheat                                                                                                                                 | Sheep can grow faster if they eatgrassorgrass blocks. They cannot be hand-fed these items; they eat them only if they are placed in the world.                                                                                                                                                                                                                                                                                      |
| Pig                                          | Carrot Potato Beetroot                                                                                                                | Pigs can also be led, but not bred, with acarrot on a stick.                                                                                                                                                                                                                                                                                                                                                                        |
| Chicken                                      | Wheat Seeds Pumpkin Seeds Melon Seeds Beetroot Seeds Torchflower Seeds Pitcher Pod                                                    | Chickens directly produce a chick when bred. They also automatically produceeggs, and do so without having to be fed.                                                                                                                                                                                                                                                                                                               |
| Wolf(Tamed)                                  | Raw Beef Raw Chicken Raw Porkchop Raw Mutton Raw Rabbit Rotten Flesh Steak Cooked Chicken Cooked Porkchop Cooked Rabbit Cooked Mutton | Wolves must be tamed by being given enoughbonesbefore they can be fed anything else, and do not enter love mode from eating bones. Tamed wolves can be fed to restore health, and must be at full health to enter love mode.In Bedrock Edition, the following can also be used for healing, but cannot be used for breeding or growing a baby wolf:Raw Cod Raw Salmon Pufferfish Tropical Fish Cooked Cod Cooked Salmon Rabbit Stew |
| Cat (tamed) Ocelot                           | Raw Cod Raw Salmon                                                                                                                    | Cats must be tamed by being given enough food before they can breed. Tamed cats can be fed to restore health, and must be at full health to enter love mode.When fed, ocelots trust the player that fed them, and do not run away. An ocelot does not need to be trusting to breed.                                                                                                                                                 |
| Axolotl                                      | Bucket of Tropical Fish                                                                                                               | Only bucketed tropical fish can be used to breed axolotls.Tropical fishitems cannot be used.A water bucket is returned upon feeding.                                                                                                                                                                                                                                                                                                |
| Llama Trader Llama                           | Hay Bale                                                                                                                              | Llamas must be tamed by repeatedly mounting them before they can breed. They can be tamed faster by being fed. Llamas and trader llamas can crossbreed, and the offspring is always a normal llama.Wheat can also be used to feed an untamed llama, grow a baby, or for healing, but it cannot be used to lead or breed llamas.                                                                                                     |
| Rabbit                                       | Dandelion Carrot Golden Carrot                                                                                                        | Rabbits always run from players unless they hold a breeding item, even if they are fed or grown from a baby by a player.                                                                                                                                                                                                                                                                                                            |
| Turtle                                       | Seagrass                                                                                                                              | Turtles layeggsonsandwhen bred that take a few days to hatch into baby turtles. They lay eggs only at the place they spawned or were hatched. Turtle eggs can be obtained only withSilk Touch, hatch only when placed on sand, and hatch significantly faster at night. Turtle eggs can be trampled and broken, andzombiesand their variants do so deliberately.                                                                    |
| Panda                                        | Bamboo                                                                                                                                | Pandas can eat bamboo and other food items without player input, but breed only when fed by a player.Pandas breed only if there are at least eight bamboo plants placed in a radius of five blocks around them.                                                                                                                                                                                                                     |
| Fox                                          | Sweet Berries Glow Berries                                                                                                            | Foxes can eat berries and other food items without player input, but breed only when fed by a player.The baby fox always trusts the player that bred the foxes, even when it grows up, and does not run away when approached.                                                                                                                                                                                                       |
| Bee                                          | Flowers                                                                                                                               | All flowers and flowering blocks work. Feeding beeswither rosesdoes notgive them theWither effector anger them.                                                                                                                                                                                                                                                                                                                     |
| Strider                                      | Warped Fungus                                                                                                                         | Striders can also be led, but not bred, with awarped fungus on a stick.                                                                                                                                                                                                                                                                                                                                                             |
| Hoglin                                       | Crimson Fungus                                                                                                                        | Hoglins continue to attack during the breeding process. Hoglins that are fleeing fromwarped fungi,nether portalsorrespawn anchorscannot be bred.Zoglins cannot breed.                                                                                                                                                                                                                                                               |
| Frog                                         | Slimeball                                                                                                                             | Frogs layeggson water that take ten minutes to hatch intotadpoles. These eggs cannot be obtained in item form or moved.                                                                                                                                                                                                                                                                                                             |
| Camel                                        | Cactus                                                                                                                                | Despite being fed cacti to breed (and not taking damage from it), camels still take damage from touching it when it is placed in the world.                                                                                                                                                                                                                                                                                         |
| Sniffer                                      | Torchflower Seeds                                                                                                                     | Sniffers layeggswhen bred that take twenty minutes (or ten, if the egg is placed on amoss block) to hatch into a snifflet. They lay their eggs in item form, and they must be placed by a player.                                                                                                                                                                                                                                   |
| Armadillo‌[upcoming: JE 1.20.5 & BE 1.20.80] | Spider Eye                                                                                                                            | When an armadillo is rolled up it cannot eat.                                                                                                                                                                                                                                                                                                                                                                                       |

### Villagers
Main article: Villager § Breeding
A group of villager children playing tag.
Villagers do not breed automatically when given food. Villager breeding depends on both the number of valid beds in the area (see the village page for full details), as well as whether the villagers are "willing." A villager may become willing if they have 3 bread, 12 carrots, 12 potatoes, or 12 beetroots in their inventory. They may also become willing as a result of trading with a player. When they breed, they produce a smaller villager. Unlike many baby animals, baby villagers do not have big heads in Java Edition. Zombie villagers and wandering traders cannot breed, and baby zombie villagers do not grow up.

## Baby mobs
An example of how a bred sheep inherits a mixture of its parents' colors when possible.
Baby mobs are smaller variations of their adult counterparts, having small bodies, relatively big heads (with some exceptions), and faster walking speeds. Their sounds are the same as their adult variants but 50% faster and are pitched up by 6 semitones. The only exception to this are tadpoles, which are a wholly unique mob from frogs. Many baby mobs have different interactions or behavior compared to their elders that depends on the mob. For example, lambs cannot be sheared for their wool, calves, mooshroom calves and kids (baby goats) cannot be milked, and baby piglins take gold but do not barter. Most baby mobs do not drop loot or experience when killed, with the exception of items they pick up. Baby mobs that do drop loot or experience consist of the following:

- Babyzombies,zombie villagers,husks,drowned,zombified piglinsandzoglins(both loot and experience)
- Babyhoglins(only experience)
- Babypiglins(only experience, less than adults)

Most baby animals choose and follow an adult within 8 blocks of the same species, regardless of whether it is their parent. Babies can choose new targets to follow whenever they do not have a valid target, such as when the previous target dies or moves further than 16 blocks away. Tamed pups and kittens follow their owner if the parent is absent or sitting. Baby animals that do not follow adults consist of:

- Tadpoles(which do not followfrogs)
- Snifflets[1]
- Babyrabbits‌[Java Edition  only][2]
- Babyturtles‌[Java Edition  only][3]
- Ocelotkittens‌[Java Edition  only][3]
- Stray kittens‌[Java Edition  only][3]
- Wildwolfpups‌[Java Edition  only][3]

Baby mobs that are not animals never follow adult mobs.

When a baby of a species with different fur/pattern variants is born, they usually inherit the pattern of one of their parents, chosen at random, with some exceptions: 

- In the case ofsheep, if the parents have "compatible" colors (meaning that their correspondingdyeitems could be combined into a third dye), the lamb inherits a mix of the parents' colors‌[Java Edition  only].
- In the case ofmooshrooms, breeding two of the same variant has a1⁄1024chance to spawn a mooshroom of the opposite variant. Breeding two mooshrooms of differing variants has an equal chance of a baby mooshroom of either type.
- In the case ofhorses, there is a13⁄45chance of having a random color/markings instead of matching either of its parents.
- In the case ofaxolotls, a baby axolotl bred by a player (not found in the world) has a1⁄1200chance to be the rare blue variant, with this being the only way to obtain this variant. Otherwise, it inherits the color of one of its parents at random.
- Frogsdo not inherit their variants from their parents. A frog's variant is determined by the biome it matures from atadpolein.


Baby animals can be manually spawned by using spawn eggs on a grown animal. This also works on zombies or variants. Baby animals may also be spawned using the /summon command with a negative Age tag; for example, using /summon sheep ~ ~ ~ {Age:-100} spawns a baby sheep at the player's position, that matures in 100 ticks (5 seconds). For baby mobs that don't grow up like zombies and piglins, the IsBaby:1 tag is used instead.
Feed graphic for baby animals in Java Edition.
Most baby mobs take 20 minutes to grow up. This can be accelerated by feeding them their breeding item. Green sparkles appear similar to those caused by bone meal. in Java Edition, each feeding usually reduces the remaining time before the animal grows up by 10%. The less time remains, the less time is saved by each feeding, making it inefficient to feed an animal continuously until it becomes an adult. After the eighth feeding, the time saved by one feeding is less than a minute, as shown in the graph. in Bedrock Edition, each feeding saves 10% of the total time rather than the remaining time, so it will take no more than ten feedings to age up a single baby.

Horses, donkeys, and llamas have different mechanics: different breeding items grow babies by different amounts, and each item ages babies by a constant time rather than a percentage of the remaining time. Skeleton horses and zombie horses are not breedable, but they can be fed while being ridden by another mob.

Baby zombies, zombie villagers, husks, drowned, zombified piglins, piglins, and zoglins do not grow up, and none of these mobs can breed.

Polar bears have a baby form that can grow up into an adult, but cannot be bred. This also applies to squid, glow squid and dolphins in Bedrock Edition.

### Ageable
These baby mobs age naturally, with the exception of the undead horses in Bedrock Edition.

- Cow calf
- Chick
- Piglet
- Kid
- Lamb
- Mooshroom calf
- Rabbit kit
- Wolf pup
- Ocelot kitten
- Domestic kitten
- Baby villager in Java Edition
- Baby villager in Bedrock Edition
- Horse foal
- Donkey foal
- Mule foal
- Skeleton horse foal
- Zombie horse foal
- Cria
- Trader Cria
- Fox kit
- Axolotl juvenile
- Bee larvae
- Panda cub
- Turtle hatchling
- Hoglin piglet
- Baby strider
- Polar bear cub
- Tadpole
- Dolphin calf‌[BE  only]
- Baby glow squid‌[BE  only]
- Baby squid‌[BE  only]
- Camel calf
- Snifflet
- Armadillo pup‌[upcoming: JE 1.20.5 & BE 1.21.0]

### Monsters
These baby mobs are monsters and they do not grow up.

- Baby zombie
- Baby drowned
- Baby husk
- Baby zombified piglin
- Baby piglin
- Baby zombie villager
- Zoglin piglet

## Similar mechanics
### Allay duplication
An allay duplicating. Note the Portuguese translation of the phrase "Amethyst Shard".
If an allay is given an amethyst shard while it is dancing due to a nearby jukebox playing any music disc, it splits into two allays (itself and a new allay) and the amethyst shard is consumed. After duplication, both allays have a five minute cooldown before being able to duplicate again. Allays do not have a baby form.

### Shulker duplication
There is a chance for a new shulker of the same color to spawn when a shulker is hit with a shulker bullet (including one of its own).

The following conditions must be met:

- When the shulker gets hit and then has less than half its health remaining, there is a 25% chance for it to teleport without spawning a new shulker instead of checking the conditions below.
- The hit shulker must have its lid open.
- The hit shulker needs to find somewhere to teleport. For this, it takes a random block in a 17×17×17 cuboid centered on the shulker and then checks if the block has a valid face to teleport to. If not it proceeds to try this up to 4 more times. If no valid face is found, the attempt fails.
- Each other shulker within 8 blocks of the hit shulker decreases the odds of success by 20%. When five or more other shulkers are nearby, no shulkers can spawn, but the hit shulker still teleports.

If the attempt succeeds a new shulker spawns where the old shulker was before it teleported. Shulkers do not have a baby form, and, other than the above criteria, have no duplication cooldown.

## See also
- Tutorials/Animal farming

