# Experience
Experience orbs (EXP or XP for short) can be obtained by gathering experience orbs from mining, defeating mobs, breeding, trading, fishing, completing advancements,‌[Java Edition  only] and using grindstones and furnaces. Experience orbs gained during a player's life affects the player's score on the death screen. While having no direct effect on the player character, it can be used to enhance their equipment through enchanting, or by using an anvil to repair, rename, or combine enchantments on equipment. Experience orbs also recovers durability on items with Mending that are being worn or are in-hand.

## Contents
- 1 Sources
	- 1.1 Experience orbs
	- 1.2 Experience amounts by source
- 2 Leveling up
	- 2.1 Useful numbers
- 3 Score
- 4 Sounds
- 5 Data values
	- 5.1 ID
	- 5.2 Entity data
- 6 Video
- 7 History
	- 7.1 Values from Java Edition Beta 1.8 to 1.3.1 (12w23a)
	- 7.2 Values from Java Edition 1.3.1 to 1.8 (14w02a)
- 8 Issues
- 9 Trivia
- 10 Gallery
	- 10.1 Renders
	- 10.2 Textures
	- 10.3 Screenshots
- 11 References

## Sources
Experience orbs can be gained from several different sources:

- From killing most mobs, which drop experience orbs along with any other items.
	- A mob does not drop experience orbs unless it dies within five seconds (100 game ticks) of an attack registered as a player hit (including tamedwolves, player thrown fireballs, and TNT). This allows gaining experience orbs from, say, knocking a monster off a cliff, lighting a mob on fire, etc. (fetching the orbs might be another question). Theplayercan also try to "claim" a burning monster by hitting or shooting it once—even if the blow doesn't kill it, if the mob dies within 5 seconds, it drops experience orbs.
	- Deaths ofzombified piglinsalways register as kills by the player they are targeting, regardless of whether that player ever touched that zombified piglin.[2]
	- Mobs killed byTNTactivated by a player usingflint and steelor a flaming arrow drop XP as usual; however, mobs killed by TNT that was activated by fire,redstone, or an explosion that wasn'tplayeractivated does not drop any experience orbs.
	- Mobsdrop a random number of experience orbs, which can have different values. However, the total value always remains within the values given below, regardless ofdifficultysetting.
	- Hostile mobs give more experience orbs than passive ones. Baby animals,bats,golems, andvillagersgive no experience orbs at all. Theender dragongives experience orbs totaling 12,000 XP the first time aplayerkills it—12 times more than anything else in the game—and 500 XP in subsequent defeats.
		- Some hostilemobsspawn with weapons, orcanspawn with weapons and/orarmor. These mobs give an extra 1–3 points (randomly) per piece of equipment that they spawned with. Equipment picked up after spawning doesn't count.
	- Mining(destroying) amonster spawnerblock gives 15–43 points of experience orbs.
	- While they do not drop experience orbs normally, baby mobs as well as mobs killed by non-player means are accepted by thesculk catalyst, allowing for experience orbs to be obtained in a more indirect way.
- Fromminingany ore that drops a resource, rather than raw metals or themselves. The experience orbs are produced along with the mineral item(s). If aSilk Touchpickaxe is used to mine the ore block, the experience is not dropped, but the block can later be placed and mined normally to release the mineral and the experience.
	- The ore still produces orbs if destroyed by an explosion, whether or not it was caused by player activated TNT.
- Fromsmeltingany of various items.
	- Smelting any ore yields some experience, but normally onlynether gold oreandancient debrisare worthwhile. For all other ores,mining them is better.
	- Moderate amounts are gained by smelting/cooking other materials: food, clay balls or blocks,cactus, wood logs, sand, or cobblestone, cactus giving the most.‌[JE  only]
	- The smelted material must be taken from the furnace through its GUI window. If the player uses a hopper to unload the furnace, it is possible to retrieve all experience produced by the furnace by smelting an extra item and taking it from the GUI. Breaking the furnace drops all stored experience as collectable experience orbs.
- Frombreedinganimals, which produces orbs where the parents are, along with the baby animal. Breakingeggsdoes not give experience.
- Fromfishing. The experience is awarded immediately upon reeling in the fish, even if the fish itself is not picked up.
- Fromtradingwith villagers.
- Abottle o' enchantingreleases orbs when broken.
- From the/experiencecommand.
- From disenchanting items in agrindstone.
- From completing a challengeadvancement.‌[JE  only]

Gathering experience points from experience orbs increases the player's experience level by gradually filling a bar on the bottom of the screen until a new level is achieved when the bar is full. When the player dies, they drop experience orbs worth 7 * current level experience points, up to a maximum of 100 points (enough to reach level 7), and all of the other experience vanishes. If the gamerule keepInventory is set to true, the experience is kept even if the player dies.

### Experience orbs
Experience orbs fade between green and yellow colors and float or glide toward the player up to a distance of 7.25 blocks (calculated from the center of player's feet and the center of the experience orb), speeding up as they get nearer to the player. Experience orbs pulled toward a player are slowed by cobwebs. Experience orbs can also be pulled around or away from the player by running water currents.

When collected, experience orbs make a bell-like sound for a split second. Unlike resources, experience points are picked up gradually: no matter how many orbs are in the range of the player, they are added to the player's experience one at a time (10 orbs/second). In extreme cases, this can result in the player being followed by a swarm of orbs for many seconds. If an experience orb isn't collected within 5 minutes of its appearance, it disappears.

Experience orbs vary in value. The general worth of an orb is reflected by its size, with eleven possible sizes corresponding to specific values. The three smallest sizes are the most commonly encountered, as the majority of experience dropped by mobs and blocks is less than ten. Dense experience orbs, from values 17 and up, have orange "eyes" or "cores", and are less frequently encountered, most commonly from defeating the ender dragon, wither and other players, disenchanting objects on a grindstone, breaking spawners, and collecting items from high- traffic furnaces. For performance improvement, experience orbs of the same value can merge into a single entity, but they do not create a higher value orb.

| Orb | Minimum value | Maximum value |
|-----|---------------|---------------|
|     | -32768[3]     | 2             |
|     | 3             | 6             |
|     | 7             | 16            |
|     | 17            | 36            |
|     | 37            | 72            |
|     | 73            | 148           |
|     | 149           | 306           |
|     | 307           | 616           |
|     | 617           | 1236          |
|     | 1237          | 2476          |
|     | 2477          | 32767         |

Naturally spawned orbs always have an integer value of 1–11, 17, 37, 73, 149, 307, 617, 1237, or 2477. Fishing, breeding, and trading drop a single orb with a random value in the appropriate range. Breaking blocks, killing mobs and players, smelting items, and bottles o' enchanting calculate their total experience amount and then split it into values of 1, 3, 7, 17, 37, 73, 149, 307, 617, 1237, and 2477. Higher values are chosen first, so, for example, a total value of 1000 would be dropped as orbs with values 617, 307, 73, and 3. Note that while the first Ender Dragon in a world drops 12,000 experience, it is dropped in 10 waves of 1000 and one of 2000, so no orbs of value 2477 are dropped. Such orbs can only exist in the world via furnaces that have had a lot of traffic.

Experience orbs with negative values can be created using the /summon command, either using values below 0 or above 32767 due to 16-bit integer overflow. They have the smallest texture of experience orb. While collecting them does not affect the player's experience bar in any way, they can deduct durability from a tool enchanted with Mending, provided the tool is already damaged prior to collection of the orbs.[4]

Like items, experience orbs float when on water. Experience orbs can be destroyed by fire, lava, explosions, and cacti, and can trigger pressure plates and tripwires. Experience orbs can also stop minecarts. 

In Bedrock Edition, although mob drops spawn the instant the final blow is dealt to the mob, experience orbs do not appear until the mob entity disappears and the smoke appears.

In Java Edition, experience orbs appear in the same spatial and temporal location as loot when an entity is killed.

The following mobs and similar entities don't drop experience when killed:

- Babyanimals(except for the hoglin)
- Agent
- Allay
- Armor Stand
- Bat
- Camera
- Elder Guardian Ghost
- Iron Golem
- NPC
- Snow Golem
- Tadpole
- Villager
- Wandering Trader

### Experience amounts by source
| Source                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Experience                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Killinganimals                                                           |
| Fox‌[BE  only],Strider‌[JE  only]                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | 1–2                                                                      |
| Armadillo,Axolotl,Bee,Camel,Cat,Chicken,Cod,Cow,Dolphin,Donkey,Fox‌[JE  only],Frog,Glow Squid,Goat,Hoglin‌[BE  only],Horse,Llama,Mooshroom,Ocelot,Panda,Parrot,Pig,Polar Bear,Pufferfish,Rabbit,Salmon,Sheep,Skeleton Horse,Sniffer,Squid,Strider‌[BE  only],Trader Llama,Tropical Fish,Turtle,Wolf,Zombie Horse                                                                                                                                                                                          | 1–3                                                                      |
| Chicken(spawned as a jockey)                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 10                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Killingmonsters                                                          |
| Baby Piglin                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | 1‌[BE  only]                                                             |
| Endermite                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 3                                                                        |
| Magma CubeandSlime                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | 4 (large)<br/>2 (medium)<br/>1 (small)                                   |
| Bogged,Breeze,Cave Spider,Creeper,Drowned,Enderman,Giant,Ghast,Hoglin‌[JE  only],Husk,Illusioner,Phantom,Piglin,Pillager,Shulker,Silverfish,Skeleton,Spider,Stray,Vex,Vindicator,Warden,Witch,Wither Skeleton,Zombie,Zombie Villager,Zoglin,Zombified Piglin                                                                                                                                                                                                                                              | 5 + 1–3 (per equipment)                                                  |
| Blaze,Elder Guardian,Evoker,Guardian                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | 10                                                                       |
| Baby Drowned,Baby Husk,Baby Zombie,Baby Zombie Villager,Baby Zombified Piglin                                                                                                                                                                                                                                                                                                                                                                                                                             | 12 + 1–3 (per equipment)                                                 |
| Ravager,Piglin Brute                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | 20 + 1–3 (per equipment)                                                 |
| Wither                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 50                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Entity dying (no requirement for player involvement)                     |
| Player                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 7 per level, up to 100                                                   |
| Ender Dragon                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 12,000 (500 if respawned withend crystals)                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Mining blocks                                                            |
| Coal Ore                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 0–2                                                                      |
| Nether Gold Ore                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 0–1                                                                      |
| Diamond Ore,Emerald Ore                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | 3–7                                                                      |
| Lapis Lazuli Ore,Nether Quartz Ore                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | 2–5                                                                      |
| Redstone Ore                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 1–5                                                                      |
| Monster Spawner                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 15–43                                                                    |
| Sculk                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | 1                                                                        |
| Sculk Sensor,Sculk Shrieker,Sculk Catalyst                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 5                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Smelting/Cooking                                                         |
| Ancient Debris                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | 2                                                                        |
| Cactus‌[JE  only][5],Diamond Ore,Emerald Ore,Gold Ore,Nether Gold Ore                                                                                                                                                                                                                                                                                                                                                                                                                                     | 1                                                                        |
| Copper Ore,Iron Ore,Raw Iron,Raw Gold,Raw Copper,Redstone Ore                                                                                                                                                                                                                                                                                                                                                                                                                                             | 0.7[note 1]                                                              |
| Clay,Potato,Raw Beef,Raw Chicken,Raw Cod,<br/>Raw Mutton,Raw Porkchop,Raw Rabbit,Raw Salmon                                                                                                                                                                                                                                                                                                                                                                                                               | 0.35[note 1]                                                             |
| Clay Ball                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 0.3[note 1]                                                              |
| Lapis Lazuli Ore,Nether Quartz Ore,Cactus‌[BE  only]                                                                                                                                                                                                                                                                                                                                                                                                                                                      | 0.2[note 1]                                                              |
| Wet Sponge,Wood                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 0.15[note 1]                                                             |
| Chorus Fruit,Coal Ore,Cobblestone,Stone<br/>Stained Terracotta,Netherrack,Sand,Stone Bricks,Basalt<br/>Iron Sword,Golden Sword,<br/>Iron Pickaxe,Iron Axe,Iron Shovel,Iron Hoe,<br/>Golden Pickaxe,Golden Axe,Golden Shovel,Golden Hoe,<br/>Iron Helmet,Iron Chestplate,Iron Leggings,Iron Boots,<br/>Golden Helmet,Golden Chestplate,Golden Leggings,Golden Boots,<br/>Chainmail Helmet,Chainmail Chestplate,Chainmail Leggings,Chainmail Boots,<br/>Iron Horse Armor,Golden Horse Armor,Kelp,Sea Pickle | 0.1[note 1]                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | CompletingChallenges‌[Java Edition  only]                                |
| Return to Sender,Great View From Up Here,Sniper Duel,Bullseye,A Complete Catalogue                                                                                                                                                                                                                                                                                                                                                                                                                        | 50                                                                       |
| Two Birds, One Arrow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | 65                                                                       |
| Arbalistic                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 85                                                                       |
| Subspace Bubble,Uneasy Alliance,Cover Me in Debris,A Furious Cocktail,Hero of the Village,Monsters Hunted,Two by Two,A Balanced Diet,Serious Dedication                                                                                                                                                                                                                                                                                                                                                   | 100                                                                      |
| Hot Tourist Destinations,Adventuring Time                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 500                                                                      |
| How Did We Get Here?                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | 1,000                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Other                                                                    |
| Bottle o' Enchanting                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | 3–11                                                                     |
| Trading with villagers                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 3–6 (8–11 if the villagers are willing to breed; not working since 1.14) |
| Breeding animals                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 1–7                                                                      |
| Catching Fish                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 1–6                                                                      |

1. ↑ a b c d e fFor fractional values, first multiply this value by the number of smelted items removed from the furnace, then award the player the whole-number part, and if there is a fractional part remaining, this represents the chance of an additional experience point.

For example, when smelting 1 coal ore and removing the coal, the value is 0.1, so this grants a 10% chance of getting 1 experience point.
Or, when smelting 64 cobblestone and removing all 64 stone, the value is 0.1 * 64 = 6.4, so this grants 6 experience points, plus a 40% chance of getting 1 additional experience point.
	- For example, when smelting 1 coal ore and removing the coal, the value is 0.1, so this grants a 10% chance of getting 1 experience point.
	- Or, when smelting 64 cobblestone and removing all 64 stone, the value is 0.1 * 64 = 6.4, so this grants 6 experience points, plus a 40% chance of getting 1 additional experience point.

## Leveling up
| Level | Experience |       |
|-------|------------|-------|
|       | Total      | Diff. |
| 1     | 7          | 7     |
| 2     | 16         | 9     |
| 3     | 27         | 11    |
| 4     | 40         | 13    |
| 5     | 55         | 15    |
| 6     | 72         | 17    |
| 7     | 91         | 19    |
| 8     | 112        | 21    |
| 9     | 135        | 23    |
| 10    | 160        | 25    |
| 11    | 187        | 27    |
| 12    | 216        | 29    |
| 13    | 247        | 31    |
| 14    | 280        | 33    |
| 15    | 315        | 35    |
| 16    | 352        | 37    |
| 17    | 394        | 42    |
| 18    | 441        | 47    |
| 19    | 493        | 52    |
| 20    | 550        | 57    |
| 21    | 612        | 62    |
| 22    | 679        | 67    |
| 23    | 751        | 72    |
| 24    | 828        | 77    |
| 25    | 910        | 82    |
| 26    | 997        | 87    |
| 27    | 1089       | 92    |
| 28    | 1186       | 97    |
| 29    | 1288       | 102   |
| 30    | 1395       | 107   |
| 31    | 1507       | 112   |
| 32    | 1628       | 121   |
| 33    | 1758       | 130   |
| 34    | 1897       | 139   |
| 35    | 2045       | 148   |
| 36    | 2202       | 157   |
| 37    | 2368       | 166   |
| 38    | 2543       | 175   |
| 39    | 2727       | 184   |
| 40    | 2920       | 193   |
| 41    | 3122       | 202   |
| 42    | 3333       | 211   |
| 43    | 3553       | 220   |
| 44    | 3782       | 229   |
| 45    | 4020       | 238   |
| 46    | 4267       | 247   |
| 47    | 4523       | 256   |
| 48    | 4788       | 265   |
| 49    | 5062       | 274   |
| 50    | 5345       | 283   |
| 51    | 5637       | 292   |
| 52    | 5938       | 301   |
| 53    | 6248       | 310   |
| 54    | 6567       | 319   |
| 55    | 6895       | 328   |
| 56    | 7232       | 336   |
| 57    | 7578       | 345   |
| 58    | 7933       | 354   |
| 59    | 8297       | 363   |
| 60    | 8670       | 372   |
| 61    | 9052       | 381   |
| 62    | 9443       | 390   |
| 63    | 9843       | 399   |
| 64    | 10267      | 424   |




The formulas for figuring out how many experience orbs needed to get to the next level are as follows:

Experience required =2 × current_level + 7 (for levels 0–15)
5 × current_level – 38 (for levels 16–30)
9 × current_level – 158 (for levels 31+)
One can determine how much experience has been collected to reach a level using the equations:

Total experience =level2 + 6 × level (at levels 0–16)
2.5 × level2 – 40.5 × level + 360 (at levels 17–31)
4.5 × level2 – 162.5 × level + 2220 (at levels 32+)
Likewise, to get the number of levels from the total experience value, one can utilize the following inverse equations:

Total Levels =At levels 0-16 (totals 0 to 352): total+9−3
At levels 17–31 (totals 353 to 1507): 8110+25(total−783940)
At levels 32+ (totals 1508+): 32518+29(total−5421572)
### Useful numbers
- To get from level 0 to level 30 requires 1395 experience.
- To get from level 27 to level 30 requires 306 experience.
- Killing one largeslimeand all the slimes that split from it yield from 12 to 28 experience, with an average of 19.
- Killing a slime of the largest size that can be spawned using the/summoncommand and all slimes that split from it yield 448 to 8128 experience, with an average of 3025.
- The maximum level required for enchanting is level 30, while the anvil accepts jobs up to level 39 (in creative mode the anvil limit is removed).
- Level 16 is a quarter of the way to level 30, while level 22 is about halfway there. Level 30 in turn, is halfway to level 39.
- Killing the ender dragon the first time gives approximately 68 XP levels. The ender dragon actually drops 10 waves of orbs worth a total of 1,000 experience points per wave, and another worth a total of 2,000. Taken separately, the smaller waves could take a player from zero to level 26, while the big wave would take a player from zero to level 34. The largest orb dropped has a value of 1237 experience points, and can take a player from zero to level 28 all by itself.
- The maximum level that players can get legitimately is 238,609,312, and at this level the experience bar disappears, because reaching the next level would require more XP than the 32-bit integer limit (2,147,483,647, which is 231- 1). However, it is possible to reach level 2,147,483,647 using commands. In this case, the experience bar may disappear and reappear.[6]

## Score
Example of the score in Hardcore mode.
The score is the number of experience the player has collected since their last death. This number is the total experience the player has collected, rather than the amount of experience they had upon death. When the player dies, the score is displayed on the death screen.

## Data values
### ID
Java Edition:

| Name           | Identifier       | Translation key                   |
|----------------|------------------|-----------------------------------|
| Experience Orb | `experience_orb` | `entity.minecraft.experience_orb` |

Bedrock Edition:

| Name           | Identifier | Numeric ID | Translation key      |
|----------------|------------|------------|----------------------|
| Experience Orb | `xp_orb`   | `69`       | `entity.xp_orb.name` |

### Entity data
Experience orbs have entity data associated with them that contain various properties.

Java Edition:

Main article: Entity format
- Entity data
	- 
	- Tags common to all entities
	- Age: The number of ticks the XP orb has been "untouched". After 6000 ticks (5 minutes) the orb is destroyed.
	- Count: The remaining number of times that the orb can be picked up. When the orb is picked up, the value decreases by 1. When multiple orbs are merged, their values are added up to result orb. When the value reaches 0, the orb is depleted.
	- Health: The health of XP orbs. XP orbs take damage from fire, lava, falling anvils, and explosions. The orb is destroyed when its health reaches 0.
	- Value: The amount of experience the orb gives when picked up.

Bedrock Edition:

SeeBedrock Edition level format/Entity format.
