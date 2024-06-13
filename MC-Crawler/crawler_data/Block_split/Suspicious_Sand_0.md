# Suspicious Sand
Suspicious sand is a fragile gravity-affected block found in various Overworld structures. They can be brushed to extract structure-dependent loot, and are the only source of pottery sherds alongside suspicious gravel. Suspicious sand drops nothing if broken, and break if they fall from any height or are moved with a piston.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
- 2 Usage
	- 2.1 Brushing
	- 2.2 Loot
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
	- 4.3 Block data
	- 4.4 Falling block entity
- 5 Advancements
- 6 History
- 7 Issues
- 8 Gallery
	- 8.1 Development Images
- 9 References

## Obtaining
### Breaking
Suspicious sand is unobtainable by mining, even using a tool enchanted with Silk Touch. They are much softer than normal sand, and can be instantly broken with merely an unenchanted diamond shovel. They are affected by gravity, but they always break with no drop after falling. They break immediately if pushed by a piston or sticky piston, and cannot be pulled by sticky pistons or slime blocks. They also break immediately without drop when affected by explosion.

In Java Edition, suspicious sand drops as an item if it falls for more than 30 seconds, which can be achieved by falling into an upward bubble column, or through two cobwebs stacked on top of each other.[1] However, it does not retain its loot.

In Creative mode, the player can obtain suspicious sand while retaining its loot by using Ctrl + pick block on the block.

| Block     | Suspicious Sand       |
|-----------|-----------------------|
| Hardness  | 0.25                  |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 0.4                   |
| Wooden    | 0.2                   |
| Stone     | 0.1                   |
| Iron      | 0.1                   |
| Diamond   | 0.05                  |
| Netherite | 0.05                  |
| Golden    | 0.05                  |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


### Natural generation
Suspicious sand generates naturally in buried rooms under desert pyramids, as well as in the bottom of desert wells. It also generates within warm ocean ruins.


## Usage
### Brushing
When a brush is used on a suspicious sand, cracks start to appear on all sides of the block as the dusted block state of the block starts to increase. If the suspicious sand being brushed is naturally generated, an item gradually emerges from the side where the player starts brushing. After 96 (6+20+30+40 per stage) game ticks (4.8 seconds), the item is extracted, and the suspicious sand is converted into sand.

If the player stops brushing a suspicious sand, the block remains in its half-excavated state for a few seconds, before gradually returning to its unexcavated state one stage at a time.

### Loot
The item obtained and the loot table of suspicious sand is dependent on which structure it has generated in. Items can be extracted only from naturally generated suspicious sand. When placed by the player, nothing is produced after brushing.

In Java Edition and Bedrock Edition, each warm ocean ruin's suspicious sand contains 1 item stack,  with the following distribution: 




 Item 
  Stack Size  [A]
  Weight   [B]
  Chance   [C]
  Avg.per block   [D]
  Avg. # blocksto brush   [E]

Coal
12⁄1513.3%0.1337.5

Emerald
12⁄1513.3%0.1337.5

Wheat
12⁄1513.3%0.1337.5

Wooden Hoe
12⁄1513.3%0.1337.5

Gold Nugget
12⁄1513.3%0.1337.5

Angler Pottery Sherd
11⁄156.7%0.06715.0

Shelter Pottery Sherd
11⁄156.7%0.06715.0

Sniffer Egg
11⁄156.7%0.06715.0

Snort Pottery Sherd
11⁄156.7%0.06715.0

Iron Axe
11⁄156.7%0.06715.0
{ "chestNames": [ "brushable-warm-ocean-ruins" ], "gameVersion": "Java", "loot": { "brushable-warm-ocean-ruins": { "poolsJava": [ { "items": { "wheat": [ 1, 1, 2 ], "gold-nugget": [ 1, 1, 2 ], "angler-pottery-sherd": [ 1, 1, 1 ], "snort-pottery-sherd": [ 1, 1, 1 ], "iron-axe": [ 1, 1, 1 ], "shelter-pottery-sherd": [ 1, 1, 1 ], "coal": [ 1, 1, 2 ], "emerald": [ 1, 1, 2 ], "wooden-hoe": [ 1, 1, 2 ], "sniffer-egg": [ 1, 1, 1 ] }, "rolls": [ 1, 1 ], "totalweight": 15 } ], "poolsBedrockUpcoming": [], "itemDataJava": { "wheat": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>15</sub>" ], "chanceany": 0.1333333333333333, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.13333333333333333, "itemname": "wheat" }, "gold-nugget": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>15</sub>" ], "chanceany": 0.1333333333333333, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 3, "avgamount": 0.13333333333333333, "itemname": "gold-nugget" }, "angler-pottery-sherd": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>15</sub>" ], "chanceany": 0.06666666666666665, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.06666666666666667, "itemname": "angler-pottery-sherd" }, "snort-pottery-sherd": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>15</sub>" ], "chanceany": 0.06666666666666665, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.06666666666666667, "itemname": "snort-pottery-sherd" }, "iron-axe": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>15</sub>" ], "chanceany": 0.06666666666666665, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 2, "avgamount": 0.06666666666666667, "itemname": "iron-axe" }, "shelter-pottery-sherd": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>15</sub>" ], "chanceany": 0.06666666666666665, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.06666666666666667, "itemname": "shelter-pottery-sherd" }, "sniffer-egg": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>15</sub>" ], "chanceany": 0.06666666666666665, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.06666666666666667, "itemname": "sniffer-egg" }, "emerald": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>15</sub>" ], "chanceany": 0.1333333333333333, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.13333333333333333, "itemname": "emerald" }, "wooden-hoe": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>15</sub>" ], "chanceany": 0.1333333333333333, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.13333333333333333, "itemname": "wooden-hoe" }, "coal": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>15</sub>" ], "chanceany": 0.1333333333333333, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.13333333333333333, "itemname": "coal" } }, "display_name": "warm ocean ruin's suspicious sand", "structID": "ocean-ruins", "poolsJavaUpcoming": [], "structure": "Ocean ruins", "container": "Warm ruins suspicious sand", "itemDataJavaUpcoming": [], "allRollsJavaUpcoming": [], "itemDataBedrock": { "wheat": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>15</sub>" ], "chanceany": 0.1333333333333333, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.13333333333333333, "itemname": "wheat" }, "gold-nugget": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>15</sub>" ], "chanceany": 0.1333333333333333, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 3, "avgamount": 0.13333333333333333, "itemname": "gold-nugget" }, "angler-pottery-sherd": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>15</sub>" ], "chanceany": 0.06666666666666665, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.06666666666666667, "itemname": "angler-pottery-sherd" }, "snort-pottery-sherd": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>15</sub>" ], "chanceany": 0.06666666666666665, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.06666666666666667, "itemname": "snort-pottery-sherd" }, "iron-axe": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>15</sub>" ], "chanceany": 0.06666666666666665, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 2, "avgamount": 0.06666666666666667, "itemname": "iron-axe" }, "shelter-pottery-sherd": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>15</sub>" ], "chanceany": 0.06666666666666665, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.06666666666666667, "itemname": "shelter-pottery-sherd" }, "sniffer-egg": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>15</sub>" ], "chanceany": 0.06666666666666665, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.06666666666666667, "itemname": "sniffer-egg" }, "emerald": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>15</sub>" ], "chanceany": 0.1333333333333333, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.13333333333333333, "itemname": "emerald" }, "wooden-hoe": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>15</sub>" ], "chanceany": 0.1333333333333333, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.13333333333333333, "itemname": "wooden-hoe" }, "coal": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>15</sub>" ], "chanceany": 0.1333333333333333, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.13333333333333333, "itemname": "coal" } }, "poolsBedrock": [ { "items": { "wheat": [ 1, 1, 2 ], "gold-nugget": [ 1, 1, 2 ], "angler-pottery-sherd": [ 1, 1, 1 ], "snort-pottery-sherd": [ 1, 1, 1 ], "iron-axe": [ 1, 1, 1 ], "shelter-pottery-sherd": [ 1, 1, 1 ], "coal": [ 1, 1, 2 ], "emerald": [ 1, 1, 2 ], "wooden-hoe": [ 1, 1, 2 ], "sniffer-egg": [ 1, 1, 1 ] }, "rolls": [ 1, 1 ], "totalweight": 15 } ], "allRollsBedrockUpcoming": [], "allRollsBedrock": [ 1 ], "itemDataBedrockUpcoming": [], "chest_type": "suspicious sand", "header": "[[Ocean Ruins]]", "allRollsJava": [ 1 ], "link": "warm [[ocean Ruins]]" } } }


↑ The size of stacks (or for unstackable items, number) of this item on any given roll.

↑ The weight of this item relative to other items in the pool.

↑ The odds of finding any of this item in a single chest.

↑ The number of items expected per chest, averaged over a large number of chests.

↑ The average number of chests the player should expect to search to find any of this item.



In Java Edition and Bedrock Edition, each desert temple's suspicious sand contains 1 item stack,  with the following distribution: 




 Item 
  Stack Size  [A]
  Weight   [B]
  Chance   [C]
  Avg.per block   [D]
  Avg. # blocksto brush   [E]

Archer Pottery Sherd
11⁄812.5%0.1258.0

Emerald
11⁄812.5%0.1258.0

Gunpowder
11⁄812.5%0.1258.0

Miner Pottery Sherd
11⁄812.5%0.1258.0

Prize Pottery Sherd
11⁄812.5%0.1258.0

Skull Pottery Sherd
11⁄812.5%0.1258.0

TNT
11⁄812.5%0.1258.0

Diamond
11⁄812.5%0.1258.0
{ "chestNames": [ "brushable-desert-temple" ], "gameVersion": "Java", "loot": { "brushable-desert-temple": { "poolsJava": [ { "items": { "emerald": [ 1, 1, 1 ], "diamond": [ 1, 1, 1 ], "prize-pottery-sherd": [ 1, 1, 1 ], "gunpowder": [ 1, 1, 1 ], "tnt": [ 1, 1, 1 ], "miner-pottery-sherd": [ 1, 1, 1 ], "archer-pottery-sherd": [ 1, 1, 1 ], "skull-pottery-sherd": [ 1, 1, 1 ] }, "rolls": [ 1, 1 ], "totalweight": 8 } ], "poolsBedrockUpcoming": [], "itemDataJava": { "tnt": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>8</sub>" ], "chanceany": 0.125, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.125, "itemname": "tnt" }, "diamond": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>8</sub>" ], "chanceany": 0.125, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 4, "avgamount": 0.125, "itemname": "diamond" }, "prize-pottery-sherd": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>8</sub>" ], "chanceany": 0.125, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.125, "itemname": "prize-pottery-sherd" }, "gunpowder": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>8</sub>" ], "chanceany": 0.125, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.125, "itemname": "gunpowder" }, "miner-pottery-sherd": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>8</sub>" ], "chanceany": 0.125, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.125, "itemname": "miner-pottery-sherd" }, "emerald": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>8</sub>" ], "chanceany": 0.125, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.125, "itemname": "emerald" }, "archer-pottery-sherd": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>8</sub>" ], "chanceany": 0.125, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.125, "itemname": "archer-pottery-sherd" }, "skull-pottery-sherd": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>8</sub>" ], "chanceany": 0.125, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.125, "itemname": "skull-pottery-sherd" } }, "display_name": "desert temple's suspicious sand", "structID": "desert-temple", "poolsJavaUpcoming": [], "structure": "Desert Pyramid", "container": "Suspicious sand", "itemDataJavaUpcoming": [], "allRollsJavaUpcoming": [], "itemDataBedrock": { "emerald": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>8</sub>" ], "chanceany": 0.125, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.125, "itemname": "emerald" }, "diamond": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>8</sub>" ], "chanceany": 0.125, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 4, "avgamount": 0.125, "itemname": "diamond" }, "prize-pottery-sherd": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>8</sub>" ], "chanceany": 0.125, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.125, "itemname": "prize-pottery-sherd" }, "gunpowder": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>8</sub>" ], "chanceany": 0.125, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.125, "itemname": "gunpowder" }, "miner-pottery-sherd": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>8</sub>" ], "chanceany": 0.125, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.125, "itemname": "miner-pottery-sherd" }, "tnt": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>8</sub>" ], "chanceany": 0.125, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.125, "itemname": "tnt" }, "archer-pottery-sherd": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>8</sub>" ], "chanceany": 0.125, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.125, "itemname": "archer-pottery-sherd" }, "skull-pottery-sherd": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>8</sub>" ], "chanceany": 0.125, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.125, "itemname": "skull-pottery-sherd" } }, "poolsBedrock": [ { "items": { "tnt": [ 1, 1, 1 ], "diamond": [ 1, 1, 1 ], "prize-pottery-sherd": [ 1, 1, 1 ], "gunpowder": [ 1, 1, 1 ], "emerald": [ 1, 1, 1 ], "miner-pottery-sherd": [ 1, 1, 1 ], "archer-pottery-sherd": [ 1, 1, 1 ], "skull-pottery-sherd": [ 1, 1, 1 ] }, "rolls": [ 1, 1 ], "totalweight": 8 } ], "allRollsBedrockUpcoming": [], "allRollsBedrock": [ 1 ], "itemDataBedrockUpcoming": [], "chest_type": "suspicious sand", "header": "[[Desert Pyramid]]", "allRollsJava": [ 1 ], "link": "[[desert pyramid]]" } } }


↑ The size of stacks (or for unstackable items, number) of this item on any given roll.

↑ The weight of this item relative to other items in the pool.

↑ The odds of finding any of this item in a single chest.

↑ The number of items expected per chest, averaged over a large number of chests.

↑ The average number of chests the player should expect to search to find any of this item.



In Java Edition and Bedrock Edition, each desert well's suspicious sand contains 1 item stack,  with the following distribution: 




 Item 
  Stack Size  [A]
  Weight   [B]
  Chance   [C]
  Avg.per block   [D]
  Avg. # blocksto brush   [E]

Arms Up Pottery Sherd
12⁄825.0%0.2504.0

Brewer Pottery Sherd
12⁄825.0%0.2504.0

Brick
11⁄812.5%0.1258.0

Emerald
11⁄812.5%0.1258.0

Stick
11⁄812.5%0.1258.0

Suspicious Stew[F]
11⁄812.5%0.1258.0
{ "chestNames": [ "brushable-desert-well" ], "gameVersion": "Java", "loot": { "brushable-desert-well": { "poolsJava": [ { "items": { "brick": [ 1, 1, 1 ], "brewer-pottery-sherd": [ 1, 1, 2 ], "suspicious-stew": [ 1, 1, 1 ], "emerald": [ 1, 1, 1 ], "arms-up-pottery-sherd": [ 1, 1, 2 ], "stick": [ 1, 1, 1 ] }, "rolls": [ 1, 1 ], "totalweight": 8 } ], "poolsBedrockUpcoming": [], "itemDataJava": { "brick": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>8</sub>" ], "chanceany": 0.125, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.125, "itemname": "brick" }, "brewer-pottery-sherd": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>8</sub>" ], "chanceany": 0.25, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.25, "itemname": "brewer-pottery-sherd" }, "stick": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>8</sub>" ], "chanceany": 0.125, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.125, "itemname": "stick" }, "emerald": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>8</sub>" ], "chanceany": 0.125, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.125, "itemname": "emerald" }, "arms-up-pottery-sherd": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>8</sub>" ], "chanceany": 0.25, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.25, "itemname": "arms-up-pottery-sherd" }, "suspicious-stew": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>8</sub>" ], "chanceany": 0.125, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.125, "itemname": "suspicious-stew" } }, "display_name": "desert well's suspicious sand", "structID": "desert-well", "poolsJavaUpcoming": [], "structure": "Desert well", "container": "Suspicious sand", "itemDataJavaUpcoming": [], "allRollsJavaUpcoming": [], "itemDataBedrock": { "brick": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>8</sub>" ], "chanceany": 0.125, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.125, "itemname": "brick" }, "brewer-pottery-sherd": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>8</sub>" ], "chanceany": 0.25, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.25, "itemname": "brewer-pottery-sherd" }, "stick": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>8</sub>" ], "chanceany": 0.125, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.125, "itemname": "stick" }, "emerald": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>8</sub>" ], "chanceany": 0.125, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.125, "itemname": "emerald" }, "arms-up-pottery-sherd": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>8</sub>" ], "chanceany": 0.25, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.25, "itemname": "arms-up-pottery-sherd" }, "suspicious-stew": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>8</sub>" ], "chanceany": 0.125, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.125, "itemname": "suspicious-stew" } }, "poolsBedrock": [ { "items": { "brick": [ 1, 1, 1 ], "brewer-pottery-sherd": [ 1, 1, 2 ], "suspicious-stew": [ 1, 1, 1 ], "emerald": [ 1, 1, 1 ], "arms-up-pottery-sherd": [ 1, 1, 2 ], "stick": [ 1, 1, 1 ] }, "rolls": [ 1, 1 ], "totalweight": 8 } ], "allRollsBedrockUpcoming": [], "allRollsBedrock": [ 1 ], "itemDataBedrockUpcoming": [], "chest_type": "suspicious sand", "header": "[[Desert Well]]", "allRollsJava": [ 1 ], "link": "[[desert well]]" } } }


↑ The size of stacks (or for unstackable items, number) of this item on any given roll.

↑ The weight of this item relative to other items in the pool.

↑ The odds of finding any of this item in a single chest.

↑ The number of items expected per chest, averaged over a large number of chests.

↑ The average number of chests the player should expect to search to find any of this item.

↑ The stew grants one of the following effects: 5–7 seconds of Blindness, 7–10 seconds of Jump Boost, 7-10 seconds of Night Vision, 10–20 seconds of Poison, 0.35-0.5 seconds of Saturation, or 6–8 seconds of Weakness.



