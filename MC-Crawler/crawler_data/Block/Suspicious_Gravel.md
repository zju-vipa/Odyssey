# Suspicious Gravel
Suspicious gravel is a fragile gravity-affected block found in various Overworld structures. They can be brushed to extract structure-dependent loot, and are the only source of pottery sherds alongside suspicious sand. Suspicious gravel drops nothing if broken, and break if they fall from any height or are moved with a piston.

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
Suspicious gravel is unobtainable by mining, even using a tool enchanted with Silk Touch. They are much softer than normal gravel, and can be instantly broken with merely an unenchanted diamond shovel. They are affected by gravity, but they always break with no drop after falling. They break immediately if pushed by a piston or sticky piston, and cannot be pulled by sticky pistons or slime blocks. They also break immediately without drop when affected by explosion.

In Java Edition, suspicious gravel drops as an item if it falls for more than 30 seconds, which can be achieved by falling into an upward bubble column, or through two cobwebs stacked on top of each other.[1] However, it does not retain its loot.

In Creative mode, the player can obtain suspicious gravel while retaining its loot by using Ctrl + pick block on the block.

| Block     | Suspicious Gravel     |
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
Suspicious gravel generates naturally in cold ocean ruins. Additionally, some of the gravel within trail ruins is replaced with suspicious gravel upon generation.


## Usage
### Brushing
When a brush is used on suspicious gravel, cracks start to appear on all sides of the block as the dusted block state of the block starts to increase. If the suspicious gravel being brushed is naturally generated, an item gradually emerges from the side where the player starts brushing. After 96 (6+20+30+40 per stage) game ticks (4.8 seconds), the item is extracted, and the suspicious gravel is converted into gravel.

If the player stops brushing a suspicious gravel, the block remains in its half-excavated state for a few seconds, before gradually returning to its unexcavated state one stage at a time.

### Loot
The item obtained and the loot table of suspicious gravel is dependent on which structure it has generated in. Items can be extracted only from naturally generated suspicious gravel. When placed by the player, nothing is produced after brushing.

In Java Edition, each trail ruin's suspicious gravel contains 1 item stack,  with the following distribution: 




 Item 
  Stack Size  [A]
  Weight   [B]
  Chance   [C]
  Avg.per block   [D]
  Avg. # blocksto brush   [E]

Blue Dye
12⁄454.4%0.04422.5

Brick
12⁄454.4%0.04422.5

Brown Candle
12⁄454.4%0.04422.5

Emerald
12⁄454.4%0.04422.5

Green Candle
12⁄454.4%0.04422.5

Light Blue Dye
12⁄454.4%0.04422.5

Orange Dye
12⁄454.4%0.04422.5

Purple Candle
12⁄454.4%0.04422.5

Red Candle
12⁄454.4%0.04422.5

Wheat
12⁄454.4%0.04422.5

White Dye
12⁄454.4%0.04422.5

Wooden Hoe
12⁄454.4%0.04422.5

Yellow Dye
12⁄454.4%0.04422.5

Beetroot Seeds
11⁄452.2%0.02245.0

Blue Stained Glass Pane
11⁄452.2%0.02245.0

Coal
11⁄452.2%0.02245.0

Dead Bush
11⁄452.2%0.02245.0

Flower Pot
11⁄452.2%0.02245.0

Lead
11⁄452.2%0.02245.0

Light Blue Stained Glass Pane
11⁄452.2%0.02245.0

Magenta Stained Glass Pane
11⁄452.2%0.02245.0

Oak Hanging Sign
11⁄452.2%0.02245.0

Pink Stained Glass Pane
11⁄452.2%0.02245.0

Purple Stained Glass Pane
11⁄452.2%0.02245.0

Red Stained Glass Pane
11⁄452.2%0.02245.0

Spruce Hanging Sign
11⁄452.2%0.02245.0

String
11⁄452.2%0.02245.0

Wheat Seeds
11⁄452.2%0.02245.0

Yellow Stained Glass Pane
11⁄452.2%0.02245.0

Gold Nugget
11⁄452.2%0.02245.0
{ "chestNames": [ "brushable-trail-ruins" ], "gameVersion": "Java", "loot": { "brushable-trail-ruins": { "poolsJava": [ { "items": { "wheat": [ 1, 1, 2 ], "brown-candle": [ 1, 1, 2 ], "wheat-seeds": [ 1, 1, 1 ], "purple-candle": [ 1, 1, 2 ], "flower-pot": [ 1, 1, 1 ], "blue-stained-glass-pane": [ 1, 1, 1 ], "lead": [ 1, 1, 1 ], "string": [ 1, 1, 1 ], "brick": [ 1, 1, 2 ], "green-candle": [ 1, 1, 2 ], "dead-bush": [ 1, 1, 1 ], "beetroot-seeds": [ 1, 1, 1 ], "coal": [ 1, 1, 1 ], "spruce-hanging-sign": [ 1, 1, 1 ], "oak-hanging-sign": [ 1, 1, 1 ], "yellow-stained-glass-pane": [ 1, 1, 1 ], "gold-nugget": [ 1, 1, 1 ], "purple-stained-glass-pane": [ 1, 1, 1 ], "red-stained-glass-pane": [ 1, 1, 1 ], "light-blue-dye": [ 1, 1, 2 ], "light-blue-stained-glass-pane": [ 1, 1, 1 ], "white-dye": [ 1, 1, 2 ], "orange-dye": [ 1, 1, 2 ], "blue-dye": [ 1, 1, 2 ], "pink-stained-glass-pane": [ 1, 1, 1 ], "magenta-stained-glass-pane": [ 1, 1, 1 ], "clay": [ 1, 1, 2 ], "red-candle": [ 1, 1, 2 ], "emerald": [ 1, 1, 2 ], "wooden-hoe": [ 1, 1, 2 ], "yellow-dye": [ 1, 1, 2 ] }, "rolls": [ 1, 1 ], "totalweight": 45 } ], "poolsBedrockUpcoming": [], "itemDataJava": { "wheat": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.0444444444444444, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.044444444444444446, "itemname": "wheat" }, "brown-candle": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.0444444444444444, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.044444444444444446, "itemname": "brown-candle" }, "wheat-seeds": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.022222222222222254, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.022222222222222223, "itemname": "wheat-seeds" }, "purple-candle": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.0444444444444444, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.044444444444444446, "itemname": "purple-candle" }, "flower-pot": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.022222222222222254, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.022222222222222223, "itemname": "flower-pot" }, "coal": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.022222222222222254, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.022222222222222223, "itemname": "coal" }, "yellow-dye": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.0444444444444444, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.044444444444444446, "itemname": "yellow-dye" }, "brick": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.0444444444444444, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.044444444444444446, "itemname": "brick" }, "green-candle": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.0444444444444444, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.044444444444444446, "itemname": "green-candle" }, "wooden-hoe": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.0444444444444444, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.044444444444444446, "itemname": "wooden-hoe" }, "emerald": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.0444444444444444, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.044444444444444446, "itemname": "emerald" }, "red-candle": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.0444444444444444, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.044444444444444446, "itemname": "red-candle" }, "magenta-stained-glass-pane": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.022222222222222254, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.022222222222222223, "itemname": "magenta-stained-glass-pane" }, "string": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.022222222222222254, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.022222222222222223, "itemname": "string" }, "yellow-stained-glass-pane": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.022222222222222254, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.022222222222222223, "itemname": "yellow-stained-glass-pane" }, "gold-nugget": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.022222222222222254, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 3, "avgamount": 0.022222222222222223, "itemname": "gold-nugget" }, "dead-bush": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.022222222222222254, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.022222222222222223, "itemname": "dead-bush" }, "blue-dye": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.0444444444444444, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.044444444444444446, "itemname": "blue-dye" }, "light-blue-dye": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.0444444444444444, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.044444444444444446, "itemname": "light-blue-dye" }, "orange-dye": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.0444444444444444, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.044444444444444446, "itemname": "orange-dye" }, "oak-hanging-sign": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.022222222222222254, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.022222222222222223, "itemname": "oak-hanging-sign" }, "lead": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.022222222222222254, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.022222222222222223, "itemname": "lead" }, "light-blue-stained-glass-pane": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.022222222222222254, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.022222222222222223, "itemname": "light-blue-stained-glass-pane" }, "white-dye": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.0444444444444444, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.044444444444444446, "itemname": "white-dye" }, "red-stained-glass-pane": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.022222222222222254, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.022222222222222223, "itemname": "red-stained-glass-pane" }, "spruce-hanging-sign": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.022222222222222254, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.022222222222222223, "itemname": "spruce-hanging-sign" }, "purple-stained-glass-pane": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.022222222222222254, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.022222222222222223, "itemname": "purple-stained-glass-pane" }, "beetroot-seeds": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.022222222222222254, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.022222222222222223, "itemname": "beetroot-seeds" }, "pink-stained-glass-pane": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.022222222222222254, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.022222222222222223, "itemname": "pink-stained-glass-pane" }, "blue-stained-glass-pane": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.022222222222222254, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.022222222222222223, "itemname": "blue-stained-glass-pane" } }, "display_name": "trail ruin's suspicious gravel", "structID": "trail-ruins", "poolsJavaUpcoming": [], "structure": "Trail Ruins", "container": "Suspicious gravel", "itemDataJavaUpcoming": [], "allRollsJavaUpcoming": [], "itemDataBedrock": { "wheat": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.04347826086956519, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.043478260869565216, "itemname": "wheat" }, "string": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.021739130434782594, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.021739130434782608, "itemname": "string" }, "wheat-seeds": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.021739130434782594, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.021739130434782608, "itemname": "wheat-seeds" }, "purple-candle": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.04347826086956519, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.043478260869565216, "itemname": "purple-candle" }, "flower-pot": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.021739130434782594, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.021739130434782608, "itemname": "flower-pot" }, "blue-stained-glass-pane": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.021739130434782594, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.021739130434782608, "itemname": "blue-stained-glass-pane" }, "yellow-dye": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.04347826086956519, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.043478260869565216, "itemname": "yellow-dye" }, "brick": { "itemname": "brick", "sizes": [ 1 ], "sortsize": [ 1 ], "sortweight": [ 4 ], "weights": [ "<sup>4</sup>&frasl;<sub>46</sub>" ], "avgamount": 0.08695652173913043, "chanceany": 0.08695652173913049 }, "green-candle": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.04347826086956519, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.043478260869565216, "itemname": "green-candle" }, "wooden-hoe": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.04347826086956519, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.043478260869565216, "itemname": "wooden-hoe" }, "emerald": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.04347826086956519, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.043478260869565216, "itemname": "emerald" }, "clay-ball": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.04347826086956519, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.043478260869565216, "itemname": "clay-ball" }, "red-candle": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.04347826086956519, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.043478260869565216, "itemname": "red-candle" }, "red-stained-glass-pane": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.021739130434782594, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.021739130434782608, "itemname": "red-stained-glass-pane" }, "yellow-stained-glass-pane": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.021739130434782594, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.021739130434782608, "itemname": "yellow-stained-glass-pane" }, "gold-nugget": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.021739130434782594, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 3, "avgamount": 0.021739130434782608, "itemname": "gold-nugget" }, "dead-bush": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.021739130434782594, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.021739130434782608, "itemname": "dead-bush" }, "purple-stained-glass-pane": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.021739130434782594, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.021739130434782608, "itemname": "purple-stained-glass-pane" }, "light-blue-dye": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.04347826086956519, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.043478260869565216, "itemname": "light-blue-dye" }, "light-blue-stained-glass-pane": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.021739130434782594, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.021739130434782608, "itemname": "light-blue-stained-glass-pane" }, "oak-hanging-sign": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.021739130434782594, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.021739130434782608, "itemname": "oak-hanging-sign" }, "lead": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.021739130434782594, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.021739130434782608, "itemname": "lead" }, "blue-dye": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.04347826086956519, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.043478260869565216, "itemname": "blue-dye" }, "orange-dye": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.04347826086956519, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.043478260869565216, "itemname": "orange-dye" }, "white-dye": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.04347826086956519, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.043478260869565216, "itemname": "white-dye" }, "spruce-hanging-sign": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.021739130434782594, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.021739130434782608, "itemname": "spruce-hanging-sign" }, "magenta-stained-glass-pane": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.021739130434782594, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.021739130434782608, "itemname": "magenta-stained-glass-pane" }, "beetroot-seeds": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.021739130434782594, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.021739130434782608, "itemname": "beetroot-seeds" }, "pink-stained-glass-pane": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.021739130434782594, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.021739130434782608, "itemname": "pink-stained-glass-pane" }, "brown-candle": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.04347826086956519, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.043478260869565216, "itemname": "brown-candle" } }, "poolsBedrock": [ { "items": { "wheat": [ 1, 1, 2 ], "brown-candle": [ 1, 1, 2 ], "wheat-seeds": [ 1, 1, 1 ], "purple-candle": [ 1, 1, 2 ], "flower-pot": [ 1, 1, 1 ], "blue-stained-glass-pane": [ 1, 1, 1 ], "lead": [ 1, 1, 1 ], "brick": [ 1, 1, 4 ], "green-candle": [ 1, 1, 2 ], "string": [ 1, 1, 1 ], "dead-bush": [ 1, 1, 1 ], "clay-ball": [ 1, 1, 2 ], "beetroot-seeds": [ 1, 1, 1 ], "oak-hanging-sign": [ 1, 1, 1 ], "yellow-stained-glass-pane": [ 1, 1, 1 ], "gold-nugget": [ 1, 1, 1 ], "purple-stained-glass-pane": [ 1, 1, 1 ], "magenta-stained-glass-pane": [ 1, 1, 1 ], "light-blue-dye": [ 1, 1, 2 ], "red-stained-glass-pane": [ 1, 1, 1 ], "white-dye": [ 1, 1, 2 ], "orange-dye": [ 1, 1, 2 ], "blue-dye": [ 1, 1, 2 ], "light-blue-stained-glass-pane": [ 1, 1, 1 ], "pink-stained-glass-pane": [ 1, 1, 1 ], "spruce-hanging-sign": [ 1, 1, 1 ], "red-candle": [ 1, 1, 2 ], "emerald": [ 1, 1, 2 ], "wooden-hoe": [ 1, 1, 2 ], "yellow-dye": [ 1, 1, 2 ] }, "rolls": [ 1, 1 ], "totalweight": 46 } ], "allRollsBedrockUpcoming": [], "allRollsBedrock": [ 1 ], "itemDataBedrockUpcoming": [], "chest_type": "suspicious gravel", "header": "[[Trail Ruins]]", "allRollsJava": [ 1 ], "link": "[[trail ruins]]" } } }
In Bedrock Edition, each trail ruin's suspicious gravel contains 1 item stack,  with the following distribution: 




 Item 
  Stack Size  [A]
  Weight   [B]
  Chance   [C]
  Avg.per block   [D]
  Avg. # blocksto brush   [E]

Brick
14⁄468.7%0.08711.5

Blue Dye
12⁄464.3%0.04323.0

Brown Candle
12⁄464.3%0.04323.0

Clay Ball
12⁄464.3%0.04323.0

Emerald
12⁄464.3%0.04323.0

Green Candle
12⁄464.3%0.04323.0

Light Blue Dye
12⁄464.3%0.04323.0

Orange Dye
12⁄464.3%0.04323.0

Purple Candle
12⁄464.3%0.04323.0

Red Candle
12⁄464.3%0.04323.0

Wheat
12⁄464.3%0.04323.0

White Dye
12⁄464.3%0.04323.0

Wooden Hoe
12⁄464.3%0.04323.0

Yellow Dye
12⁄464.3%0.04323.0

Beetroot Seeds
11⁄462.2%0.02246.0

Blue Stained Glass Pane
11⁄462.2%0.02246.0

Dead Bush
11⁄462.2%0.02246.0

Flower Pot
11⁄462.2%0.02246.0

Lead
11⁄462.2%0.02246.0

Light Blue Stained Glass Pane
11⁄462.2%0.02246.0

Magenta Stained Glass Pane
11⁄462.2%0.02246.0

Oak Hanging Sign
11⁄462.2%0.02246.0

Pink Stained Glass Pane
11⁄462.2%0.02246.0

Purple Stained Glass Pane
11⁄462.2%0.02246.0

Red Stained Glass Pane
11⁄462.2%0.02246.0

Spruce Hanging Sign
11⁄462.2%0.02246.0

String
11⁄462.2%0.02246.0

Wheat Seeds
11⁄462.2%0.02246.0

Yellow Stained Glass Pane
11⁄462.2%0.02246.0

Gold Nugget
11⁄462.2%0.02246.0
{ "chestNames": [ "brushable-trail-ruins" ], "gameVersion": "Bedrock", "loot": { "brushable-trail-ruins": { "poolsJava": [ { "items": { "wheat": [ 1, 1, 2 ], "brown-candle": [ 1, 1, 2 ], "wheat-seeds": [ 1, 1, 1 ], "purple-candle": [ 1, 1, 2 ], "flower-pot": [ 1, 1, 1 ], "blue-stained-glass-pane": [ 1, 1, 1 ], "lead": [ 1, 1, 1 ], "string": [ 1, 1, 1 ], "brick": [ 1, 1, 2 ], "green-candle": [ 1, 1, 2 ], "dead-bush": [ 1, 1, 1 ], "beetroot-seeds": [ 1, 1, 1 ], "coal": [ 1, 1, 1 ], "spruce-hanging-sign": [ 1, 1, 1 ], "oak-hanging-sign": [ 1, 1, 1 ], "yellow-stained-glass-pane": [ 1, 1, 1 ], "gold-nugget": [ 1, 1, 1 ], "purple-stained-glass-pane": [ 1, 1, 1 ], "red-stained-glass-pane": [ 1, 1, 1 ], "light-blue-dye": [ 1, 1, 2 ], "light-blue-stained-glass-pane": [ 1, 1, 1 ], "white-dye": [ 1, 1, 2 ], "orange-dye": [ 1, 1, 2 ], "blue-dye": [ 1, 1, 2 ], "pink-stained-glass-pane": [ 1, 1, 1 ], "magenta-stained-glass-pane": [ 1, 1, 1 ], "clay": [ 1, 1, 2 ], "red-candle": [ 1, 1, 2 ], "emerald": [ 1, 1, 2 ], "wooden-hoe": [ 1, 1, 2 ], "yellow-dye": [ 1, 1, 2 ] }, "rolls": [ 1, 1 ], "totalweight": 45 } ], "poolsBedrockUpcoming": [], "itemDataJava": { "wheat": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.0444444444444444, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.044444444444444446, "itemname": "wheat" }, "brown-candle": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.0444444444444444, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.044444444444444446, "itemname": "brown-candle" }, "wheat-seeds": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.022222222222222254, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.022222222222222223, "itemname": "wheat-seeds" }, "purple-candle": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.0444444444444444, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.044444444444444446, "itemname": "purple-candle" }, "flower-pot": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.022222222222222254, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.022222222222222223, "itemname": "flower-pot" }, "coal": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.022222222222222254, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.022222222222222223, "itemname": "coal" }, "yellow-dye": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.0444444444444444, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.044444444444444446, "itemname": "yellow-dye" }, "brick": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.0444444444444444, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.044444444444444446, "itemname": "brick" }, "green-candle": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.0444444444444444, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.044444444444444446, "itemname": "green-candle" }, "wooden-hoe": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.0444444444444444, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.044444444444444446, "itemname": "wooden-hoe" }, "emerald": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.0444444444444444, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.044444444444444446, "itemname": "emerald" }, "red-candle": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.0444444444444444, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.044444444444444446, "itemname": "red-candle" }, "magenta-stained-glass-pane": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.022222222222222254, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.022222222222222223, "itemname": "magenta-stained-glass-pane" }, "string": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.022222222222222254, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.022222222222222223, "itemname": "string" }, "yellow-stained-glass-pane": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.022222222222222254, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.022222222222222223, "itemname": "yellow-stained-glass-pane" }, "gold-nugget": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.022222222222222254, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 3, "avgamount": 0.022222222222222223, "itemname": "gold-nugget" }, "dead-bush": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.022222222222222254, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.022222222222222223, "itemname": "dead-bush" }, "blue-dye": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.0444444444444444, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.044444444444444446, "itemname": "blue-dye" }, "light-blue-dye": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.0444444444444444, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.044444444444444446, "itemname": "light-blue-dye" }, "orange-dye": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.0444444444444444, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.044444444444444446, "itemname": "orange-dye" }, "oak-hanging-sign": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.022222222222222254, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.022222222222222223, "itemname": "oak-hanging-sign" }, "lead": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.022222222222222254, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.022222222222222223, "itemname": "lead" }, "light-blue-stained-glass-pane": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.022222222222222254, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.022222222222222223, "itemname": "light-blue-stained-glass-pane" }, "white-dye": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.0444444444444444, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.044444444444444446, "itemname": "white-dye" }, "red-stained-glass-pane": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.022222222222222254, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.022222222222222223, "itemname": "red-stained-glass-pane" }, "spruce-hanging-sign": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.022222222222222254, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.022222222222222223, "itemname": "spruce-hanging-sign" }, "purple-stained-glass-pane": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.022222222222222254, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.022222222222222223, "itemname": "purple-stained-glass-pane" }, "beetroot-seeds": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.022222222222222254, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.022222222222222223, "itemname": "beetroot-seeds" }, "pink-stained-glass-pane": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.022222222222222254, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.022222222222222223, "itemname": "pink-stained-glass-pane" }, "blue-stained-glass-pane": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>45</sub>" ], "chanceany": 0.022222222222222254, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.022222222222222223, "itemname": "blue-stained-glass-pane" } }, "display_name": "trail ruin's suspicious gravel", "structID": "trail-ruins", "poolsJavaUpcoming": [], "structure": "Trail Ruins", "container": "Suspicious gravel", "itemDataJavaUpcoming": [], "allRollsJavaUpcoming": [], "itemDataBedrock": { "wheat": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.04347826086956519, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.043478260869565216, "itemname": "wheat" }, "string": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.021739130434782594, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.021739130434782608, "itemname": "string" }, "wheat-seeds": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.021739130434782594, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.021739130434782608, "itemname": "wheat-seeds" }, "purple-candle": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.04347826086956519, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.043478260869565216, "itemname": "purple-candle" }, "flower-pot": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.021739130434782594, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.021739130434782608, "itemname": "flower-pot" }, "blue-stained-glass-pane": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.021739130434782594, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.021739130434782608, "itemname": "blue-stained-glass-pane" }, "yellow-dye": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.04347826086956519, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.043478260869565216, "itemname": "yellow-dye" }, "brick": { "itemname": "brick", "sizes": [ 1 ], "sortsize": [ 1 ], "sortweight": [ 4 ], "weights": [ "<sup>4</sup>&frasl;<sub>46</sub>" ], "avgamount": 0.08695652173913043, "chanceany": 0.08695652173913049 }, "green-candle": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.04347826086956519, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.043478260869565216, "itemname": "green-candle" }, "wooden-hoe": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.04347826086956519, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.043478260869565216, "itemname": "wooden-hoe" }, "emerald": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.04347826086956519, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.043478260869565216, "itemname": "emerald" }, "clay-ball": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.04347826086956519, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.043478260869565216, "itemname": "clay-ball" }, "red-candle": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.04347826086956519, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.043478260869565216, "itemname": "red-candle" }, "red-stained-glass-pane": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.021739130434782594, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.021739130434782608, "itemname": "red-stained-glass-pane" }, "yellow-stained-glass-pane": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.021739130434782594, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.021739130434782608, "itemname": "yellow-stained-glass-pane" }, "gold-nugget": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.021739130434782594, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 3, "avgamount": 0.021739130434782608, "itemname": "gold-nugget" }, "dead-bush": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.021739130434782594, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.021739130434782608, "itemname": "dead-bush" }, "purple-stained-glass-pane": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.021739130434782594, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.021739130434782608, "itemname": "purple-stained-glass-pane" }, "light-blue-dye": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.04347826086956519, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.043478260869565216, "itemname": "light-blue-dye" }, "light-blue-stained-glass-pane": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.021739130434782594, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.021739130434782608, "itemname": "light-blue-stained-glass-pane" }, "oak-hanging-sign": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.021739130434782594, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.021739130434782608, "itemname": "oak-hanging-sign" }, "lead": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.021739130434782594, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.021739130434782608, "itemname": "lead" }, "blue-dye": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.04347826086956519, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.043478260869565216, "itemname": "blue-dye" }, "orange-dye": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.04347826086956519, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.043478260869565216, "itemname": "orange-dye" }, "white-dye": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.04347826086956519, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.043478260869565216, "itemname": "white-dye" }, "spruce-hanging-sign": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.021739130434782594, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.021739130434782608, "itemname": "spruce-hanging-sign" }, "magenta-stained-glass-pane": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.021739130434782594, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.021739130434782608, "itemname": "magenta-stained-glass-pane" }, "beetroot-seeds": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.021739130434782594, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.021739130434782608, "itemname": "beetroot-seeds" }, "pink-stained-glass-pane": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.021739130434782594, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.021739130434782608, "itemname": "pink-stained-glass-pane" }, "brown-candle": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>46</sub>" ], "chanceany": 0.04347826086956519, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.043478260869565216, "itemname": "brown-candle" } }, "poolsBedrock": [ { "items": { "wheat": [ 1, 1, 2 ], "brown-candle": [ 1, 1, 2 ], "wheat-seeds": [ 1, 1, 1 ], "purple-candle": [ 1, 1, 2 ], "flower-pot": [ 1, 1, 1 ], "blue-stained-glass-pane": [ 1, 1, 1 ], "lead": [ 1, 1, 1 ], "brick": [ 1, 1, 4 ], "green-candle": [ 1, 1, 2 ], "string": [ 1, 1, 1 ], "dead-bush": [ 1, 1, 1 ], "clay-ball": [ 1, 1, 2 ], "beetroot-seeds": [ 1, 1, 1 ], "oak-hanging-sign": [ 1, 1, 1 ], "yellow-stained-glass-pane": [ 1, 1, 1 ], "gold-nugget": [ 1, 1, 1 ], "purple-stained-glass-pane": [ 1, 1, 1 ], "magenta-stained-glass-pane": [ 1, 1, 1 ], "light-blue-dye": [ 1, 1, 2 ], "red-stained-glass-pane": [ 1, 1, 1 ], "white-dye": [ 1, 1, 2 ], "orange-dye": [ 1, 1, 2 ], "blue-dye": [ 1, 1, 2 ], "light-blue-stained-glass-pane": [ 1, 1, 1 ], "pink-stained-glass-pane": [ 1, 1, 1 ], "spruce-hanging-sign": [ 1, 1, 1 ], "red-candle": [ 1, 1, 2 ], "emerald": [ 1, 1, 2 ], "wooden-hoe": [ 1, 1, 2 ], "yellow-dye": [ 1, 1, 2 ] }, "rolls": [ 1, 1 ], "totalweight": 46 } ], "allRollsBedrockUpcoming": [], "allRollsBedrock": [ 1 ], "itemDataBedrockUpcoming": [], "chest_type": "suspicious gravel", "header": "[[Trail Ruins]]", "allRollsJava": [ 1 ], "link": "[[trail ruins]]" } } }


↑ a b The size of stacks (or for unstackable items, number) of this item on any given roll.

↑ a b The weight of this item relative to other items in the pool.

↑ a b The odds of finding any of this item in a single chest.

↑ a b The number of items expected per chest, averaged over a large number of chests.

↑ a b The average number of chests the player should expect to search to find any of this item.



In Java Edition and Bedrock Edition, each trail ruin's rare suspicious gravel contains 1 item stack,  with the following distribution: 




 Item 
  Stack Size  [A]
  Weight   [B]
  Chance   [C]
  Avg.per block   [D]
  Avg. # blocksto brush   [E]

Burn Pottery Sherd
11⁄128.3%0.08312.0

Danger Pottery Sherd
11⁄128.3%0.08312.0

Music Disc (Relic)
11⁄128.3%0.08312.0

Friend Pottery Sherd
11⁄128.3%0.08312.0

Heart Pottery Sherd
11⁄128.3%0.08312.0

Heartbreak Pottery Sherd
11⁄128.3%0.08312.0

Host Armor Trim Smithing Template
11⁄128.3%0.08312.0

Howl Pottery Sherd
11⁄128.3%0.08312.0

Raiser Armor Trim Smithing Template
11⁄128.3%0.08312.0

Shaper Armor Trim Smithing Template
11⁄128.3%0.08312.0

Sheaf Pottery Sherd
11⁄128.3%0.08312.0

Wayfinder Armor Trim Smithing Template
11⁄128.3%0.08312.0
{ "chestNames": [ "brushable-trail-ruins-rare" ], "gameVersion": "Java", "loot": { "brushable-trail-ruins-rare": { "poolsJava": [ { "items": { "friend-pottery-sherd": [ 1, 1, 1 ], "danger-pottery-sherd": [ 1, 1, 1 ], "wayfinder-armor-trim-smithing-template": [ 1, 1, 1 ], "heart-pottery-sherd": [ 1, 1, 1 ], "shaper-armor-trim-smithing-template": [ 1, 1, 1 ], "burn-pottery-sherd": [ 1, 1, 1 ], "disc-relic": [ 1, 1, 1 ], "heartbreak-pottery-sherd": [ 1, 1, 1 ], "raiser-armor-trim-smithing-template": [ 1, 1, 1 ], "sheaf-pottery-sherd": [ 1, 1, 1 ], "howl-pottery-sherd": [ 1, 1, 1 ], "host-armor-trim-smithing-template": [ 1, 1, 1 ] }, "rolls": [ 1, 1 ], "totalweight": 12 } ], "poolsBedrockUpcoming": [], "itemDataJava": { "heartbreak-pottery-sherd": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>12</sub>" ], "chanceany": 0.08333333333333337, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.08333333333333333, "itemname": "heartbreak-pottery-sherd" }, "danger-pottery-sherd": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>12</sub>" ], "chanceany": 0.08333333333333337, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.08333333333333333, "itemname": "danger-pottery-sherd" }, "wayfinder-armor-trim-smithing-template": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>12</sub>" ], "chanceany": 0.08333333333333337, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.08333333333333333, "itemname": "wayfinder-armor-trim-smithing-template" }, "heart-pottery-sherd": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>12</sub>" ], "chanceany": 0.08333333333333337, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.08333333333333333, "itemname": "heart-pottery-sherd" }, "disc-relic": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>12</sub>" ], "chanceany": 0.08333333333333337, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.08333333333333333, "itemname": "disc-relic" }, "burn-pottery-sherd": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>12</sub>" ], "chanceany": 0.08333333333333337, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.08333333333333333, "itemname": "burn-pottery-sherd" }, "shaper-armor-trim-smithing-template": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>12</sub>" ], "chanceany": 0.08333333333333337, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.08333333333333333, "itemname": "shaper-armor-trim-smithing-template" }, "friend-pottery-sherd": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>12</sub>" ], "chanceany": 0.08333333333333337, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.08333333333333333, "itemname": "friend-pottery-sherd" }, "raiser-armor-trim-smithing-template": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>12</sub>" ], "chanceany": 0.08333333333333337, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.08333333333333333, "itemname": "raiser-armor-trim-smithing-template" }, "sheaf-pottery-sherd": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>12</sub>" ], "chanceany": 0.08333333333333337, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.08333333333333333, "itemname": "sheaf-pottery-sherd" }, "howl-pottery-sherd": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>12</sub>" ], "chanceany": 0.08333333333333337, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.08333333333333333, "itemname": "howl-pottery-sherd" }, "host-armor-trim-smithing-template": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>12</sub>" ], "chanceany": 0.08333333333333337, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.08333333333333333, "itemname": "host-armor-trim-smithing-template" } }, "display_name": "trail ruin's rare suspicious gravel", "structID": "trail-ruins", "poolsJavaUpcoming": [], "structure": "Trail Ruins", "container": "Suspicious gravel", "itemDataJavaUpcoming": [], "allRollsJavaUpcoming": [], "itemDataBedrock": { "heartbreak-pottery-sherd": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>12</sub>" ], "chanceany": 0.08333333333333337, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.08333333333333333, "itemname": "heartbreak-pottery-sherd" }, "danger-pottery-sherd": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>12</sub>" ], "chanceany": 0.08333333333333337, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.08333333333333333, "itemname": "danger-pottery-sherd" }, "wayfinder-armor-trim-smithing-template": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>12</sub>" ], "chanceany": 0.08333333333333337, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.08333333333333333, "itemname": "wayfinder-armor-trim-smithing-template" }, "heart-pottery-sherd": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>12</sub>" ], "chanceany": 0.08333333333333337, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.08333333333333333, "itemname": "heart-pottery-sherd" }, "disc-relic": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>12</sub>" ], "chanceany": 0.08333333333333337, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.08333333333333333, "itemname": "disc-relic" }, "burn-pottery-sherd": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>12</sub>" ], "chanceany": 0.08333333333333337, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.08333333333333333, "itemname": "burn-pottery-sherd" }, "shaper-armor-trim-smithing-template": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>12</sub>" ], "chanceany": 0.08333333333333337, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.08333333333333333, "itemname": "shaper-armor-trim-smithing-template" }, "friend-pottery-sherd": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>12</sub>" ], "chanceany": 0.08333333333333337, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.08333333333333333, "itemname": "friend-pottery-sherd" }, "raiser-armor-trim-smithing-template": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>12</sub>" ], "chanceany": 0.08333333333333337, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.08333333333333333, "itemname": "raiser-armor-trim-smithing-template" }, "sheaf-pottery-sherd": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>12</sub>" ], "chanceany": 0.08333333333333337, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.08333333333333333, "itemname": "sheaf-pottery-sherd" }, "howl-pottery-sherd": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>12</sub>" ], "chanceany": 0.08333333333333337, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.08333333333333333, "itemname": "howl-pottery-sherd" }, "host-armor-trim-smithing-template": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>12</sub>" ], "chanceany": 0.08333333333333337, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.08333333333333333, "itemname": "host-armor-trim-smithing-template" } }, "poolsBedrock": [ { "items": { "friend-pottery-sherd": [ 1, 1, 1 ], "danger-pottery-sherd": [ 1, 1, 1 ], "wayfinder-armor-trim-smithing-template": [ 1, 1, 1 ], "heart-pottery-sherd": [ 1, 1, 1 ], "shaper-armor-trim-smithing-template": [ 1, 1, 1 ], "burn-pottery-sherd": [ 1, 1, 1 ], "disc-relic": [ 1, 1, 1 ], "heartbreak-pottery-sherd": [ 1, 1, 1 ], "raiser-armor-trim-smithing-template": [ 1, 1, 1 ], "sheaf-pottery-sherd": [ 1, 1, 1 ], "howl-pottery-sherd": [ 1, 1, 1 ], "host-armor-trim-smithing-template": [ 1, 1, 1 ] }, "rolls": [ 1, 1 ], "totalweight": 12 } ], "allRollsBedrockUpcoming": [], "allRollsBedrock": [ 1 ], "itemDataBedrockUpcoming": [], "chest_type": "suspicious gravel", "header": "[[Trail Ruins]]", "allRollsJava": [ 1 ], "link": "[[Trail Ruins]]" } } }


↑ The size of stacks (or for unstackable items, number) of this item on any given roll.

↑ The weight of this item relative to other items in the pool.

↑ The odds of finding any of this item in a single chest.

↑ The number of items expected per chest, averaged over a large number of chests.

↑ The average number of chests the player should expect to search to find any of this item.



In Java Edition and Bedrock Edition, each cold ocean ruin's suspicious gravel contains 1 item stack,  with the following distribution: 




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

Blade Pottery Sherd
11⁄156.7%0.06715.0

Explorer Pottery Sherd
11⁄156.7%0.06715.0

Mourner Pottery Sherd
11⁄156.7%0.06715.0

Plenty Pottery Sherd
11⁄156.7%0.06715.0

Iron Axe
11⁄156.7%0.06715.0
{ "chestNames": [ "brushable-cold-ocean-ruins" ], "gameVersion": "Java", "loot": { "brushable-cold-ocean-ruins": { "poolsJava": [ { "items": { "mourner-pottery-sherd": [ 1, 1, 1 ], "gold-nugget": [ 1, 1, 2 ], "blade-pottery-sherd": [ 1, 1, 1 ], "coal": [ 1, 1, 2 ], "iron-axe": [ 1, 1, 1 ], "emerald": [ 1, 1, 2 ], "wheat": [ 1, 1, 2 ], "explorer-pottery-sherd": [ 1, 1, 1 ], "wooden-hoe": [ 1, 1, 2 ], "plenty-pottery-sherd": [ 1, 1, 1 ] }, "rolls": [ 1, 1 ], "totalweight": 15 } ], "poolsBedrockUpcoming": [], "itemDataJava": { "wheat": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>15</sub>" ], "chanceany": 0.1333333333333333, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.13333333333333333, "itemname": "wheat" }, "gold-nugget": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>15</sub>" ], "chanceany": 0.1333333333333333, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 3, "avgamount": 0.13333333333333333, "itemname": "gold-nugget" }, "blade-pottery-sherd": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>15</sub>" ], "chanceany": 0.06666666666666665, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.06666666666666667, "itemname": "blade-pottery-sherd" }, "coal": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>15</sub>" ], "chanceany": 0.1333333333333333, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.13333333333333333, "itemname": "coal" }, "iron-axe": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>15</sub>" ], "chanceany": 0.06666666666666665, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 2, "avgamount": 0.06666666666666667, "itemname": "iron-axe" }, "plenty-pottery-sherd": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>15</sub>" ], "chanceany": 0.06666666666666665, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.06666666666666667, "itemname": "plenty-pottery-sherd" }, "mourner-pottery-sherd": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>15</sub>" ], "chanceany": 0.06666666666666665, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.06666666666666667, "itemname": "mourner-pottery-sherd" }, "emerald": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>15</sub>" ], "chanceany": 0.1333333333333333, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.13333333333333333, "itemname": "emerald" }, "wooden-hoe": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>15</sub>" ], "chanceany": 0.1333333333333333, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.13333333333333333, "itemname": "wooden-hoe" }, "explorer-pottery-sherd": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>15</sub>" ], "chanceany": 0.06666666666666665, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.06666666666666667, "itemname": "explorer-pottery-sherd" } }, "display_name": "cold ocean ruin's suspicious gravel", "structID": "ocean-ruins", "poolsJavaUpcoming": [], "structure": "Ocean Ruins", "container": "Cold ruins suspicious gravel", "itemDataJavaUpcoming": [], "allRollsJavaUpcoming": [], "itemDataBedrock": { "wheat": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>15</sub>" ], "chanceany": 0.1333333333333333, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.13333333333333333, "itemname": "wheat" }, "gold-nugget": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>15</sub>" ], "chanceany": 0.1333333333333333, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 3, "avgamount": 0.13333333333333333, "itemname": "gold-nugget" }, "plenty-pottery-sherd": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>15</sub>" ], "chanceany": 0.06666666666666665, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.06666666666666667, "itemname": "plenty-pottery-sherd" }, "coal": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>15</sub>" ], "chanceany": 0.1333333333333333, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.13333333333333333, "itemname": "coal" }, "iron-axe": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>15</sub>" ], "chanceany": 0.06666666666666665, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 2, "avgamount": 0.06666666666666667, "itemname": "iron-axe" }, "blade-pottery-sherd": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>15</sub>" ], "chanceany": 0.06666666666666665, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.06666666666666667, "itemname": "blade-pottery-sherd" }, "mourner-pottery-sherd": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>15</sub>" ], "chanceany": 0.06666666666666665, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.06666666666666667, "itemname": "mourner-pottery-sherd" }, "emerald": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>15</sub>" ], "chanceany": 0.1333333333333333, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.13333333333333333, "itemname": "emerald" }, "wooden-hoe": { "sortsize": [ 1 ], "weights": [ "<sup>2</sup>&frasl;<sub>15</sub>" ], "chanceany": 0.1333333333333333, "sizes": [ 1 ], "sortweight": [ 2 ], "armor": 0, "material": 0, "avgamount": 0.13333333333333333, "itemname": "wooden-hoe" }, "explorer-pottery-sherd": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>15</sub>" ], "chanceany": 0.06666666666666665, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.06666666666666667, "itemname": "explorer-pottery-sherd" } }, "poolsBedrock": [ { "items": { "mourner-pottery-sherd": [ 1, 1, 1 ], "gold-nugget": [ 1, 1, 2 ], "plenty-pottery-sherd": [ 1, 1, 1 ], "coal": [ 1, 1, 2 ], "iron-axe": [ 1, 1, 1 ], "emerald": [ 1, 1, 2 ], "wheat": [ 1, 1, 2 ], "explorer-pottery-sherd": [ 1, 1, 1 ], "wooden-hoe": [ 1, 1, 2 ], "blade-pottery-sherd": [ 1, 1, 1 ] }, "rolls": [ 1, 1 ], "totalweight": 15 } ], "allRollsBedrockUpcoming": [], "allRollsBedrock": [ 1 ], "itemDataBedrockUpcoming": [], "chest_type": "suspicious gravel", "header": "[[Ocean Ruins]]", "allRollsJava": [ 1 ], "link": "cold [[ocean ruins]]" } } }


↑ The size of stacks (or for unstackable items, number) of this item on any given roll.

↑ The weight of this item relative to other items in the pool.

↑ The odds of finding any of this item in a single chest.

↑ The number of items expected per chest, averaged over a large number of chests.

↑ The average number of chests the player should expect to search to find any of this item.



## Data values
### ID
Java Edition:

| Name              | Identifier        | Form         | Block tags                                                                 | Item tags | Translation key                   |
|-------------------|-------------------|--------------|----------------------------------------------------------------------------|-----------|-----------------------------------|
| Suspicious Gravel | suspicious_gravel | Block & Item | bamboo_plantable_onenderman_holdablelush_ground_replaceablemineable/shovel | None      | block.minecraft.suspicious_gravel |

| Name         | Identifier      |
|--------------|-----------------|
| Block entity | brushable_block |

Bedrock Edition:

| Name              | Identifier        | Numeric ID | Form                       | Item ID[i 1]   | Translation key             |
|-------------------|-------------------|------------|----------------------------|----------------|-----------------------------|
| Suspicious Gravel | suspicious_gravel | -573       | Block & Giveable Item[i 2] | Identical[i 3] | tile.suspicious_gravel.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


| Name         | Savegame ID    |
|--------------|----------------|
| Block entity | BrushableBlock |

### Block states
Java Edition:

| Name   | Default value | Allowed values | Description                              |
|--------|---------------|----------------|------------------------------------------|
| dusted | 0             | 0123           | Increases as the block is being brushed. |

Bedrock Edition:

| Name             | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                              |
|------------------|---------------|---------------|----------------|-------------------------|------------------------------------------|
| brushed_progress | Not Supported | 0             | 0123           | Unsupported             | Increases as the block is being brushed. |
| hanging          | Not Supported | true          | truefalse      | Unsupported             | [more information needed]                |



### Block data
Main article: Block entity format

 Block entity data
Tags common to all block entities
 LootTable: Optional. Loot table to be used to generate the hidden item when brushed.[note 1]
 LootTableSeed: Optional. Seed for generating the loot table. 0 or omitted use a random seed.[note 1]
 item: The item in the block. May not exist.
See item format.


↑ a b Both loot table tags are removed once the items have been generated.


### Falling block entity
Main article: Falling Block

Falling Block




Hitbox size


Height: 0.98 BlocksWidth: 0.98 Blocks 




{
    "title": "Falling Block",
    "rows": [
        {
            "field": "Height: 0.98 Blocks<br>Width: 0.98 Blocks",
            "label": "(link to Hitbox article, displayed as Hitbox size)"
        }
    ],
    "invimages": [],
    "images": []
}

 Dynamic block entity data
Tags common to all entities
 BlockState: The falling block represented by this entity.
 Name: The resource location of the block.
 Properties: Optional. The block states of the block.
 Name: The block state name and its value.
 CancelDrop: 1 or 0 (true/false) - true if the block should be destroyed instead of placed after landing on a solid block. When true, the block is not dropped as an item, even if the DropItem tag is set to true. However, if the entity is deleted due to its Time value being too high, this tag is ignored and an item is dropped depending on the DropItem tag. CancelDrop defaults to 1 for falling suspicious sand and suspicious gravel, and 0 for the other vanilla falling blocks and any summoned falling block.
 DropItem: 1 or 0 (true/false) – true if the block should drop as an item when it breaks. Any block that does not have an item form with the same ID as the block does not drop even if this is set.
 FallHurtAmount: Multiplied by the FallDistance to calculate the amount of damage to inflict. By default this value is 2 for anvils, and 6 for pointed dripstone.
 FallHurtMax: The maximum hit points of damage to inflict on entities that intersect this falling block. For vanilla falling blocks, always 40 × 20.
 HurtEntities: 1 or 0 (true/false) – true if the block should hurt entities it falls on. Defaults to 1 for anvils and pointed dripstone and to 0 for the other vanilla falling blocks and any summoned falling block.
 TileEntityData: Optional. The tags of the block entity for this block.
 Time: The number of ticks the entity has existed. When Time goes above 600, or above 100 while the block is at Y=-64 or is outside building height, the entity is deleted.

