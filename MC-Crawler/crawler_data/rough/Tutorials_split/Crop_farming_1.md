## Growth and harvesting
In-game wheat at several stages.
### Growing conditions

  

This section needs to be updated. 
Please update this section to reflect recent updates or newly available information.Reason: Need to ensure light level conditions are up to date. Crops can grow at night in recent versions, even without block light.


Alternating rows of different crops (right) vs one type of crop (left).
Any of wheat, carrots, beetroots and/or potatoes grow only under the following conditions:

- It is directly above a block offarmland. If the farmland is removed or reverts todirt, the crop breaks.
- Alightlevel of 10 or higher at the plant. This doesn't have to be sunlight, sotorcheslet crops grow atnightor underground.
- The chunk the crop is in is receivingchunk ticks, onBedrock Editionthis only requires that the chunk is loaded, while onJava Editionthe chunk also has to be within 128 blocks of the nearest player.

In single-player or in multiplayer with only one player nearby, crops do not grow faster while the player is sleeping. However, if torches are not being used, sleeping skips past the nights when the crops would not grow.

Wheat, carrots and potatoes have a total of 8 growth stages. Beetroot has 4 growth stages. For wheat, each stage is a little taller and darker than the last, and the crop is mature when the wheat turns brown. Carrots and potatoes have only 4 distinct appearances—each pair of stages appears identical except that stage 7 shares the appearance of stages 5-6 (so the player can tell if it's fully mature or not, otherwise the fully mature and its previous stage can confuse the player). When mature (stage 8 for carrots and potatoes, stage 4 for beetroots), carrots and beetroots show bright crops protruding from the ground, while on a potato plant, the leaves appear significantly taller than in previous stages.

Growth happens at random intervals and is affected by growing conditions. The average duration of each stage ranges from 5 minutes (in ideal conditions) to 35 minutes (in worst-case conditions). Aside from being placed on hydrated farmland, "ideal conditions" include having light sources (for night growth) and planting crops in alternate rows: each row of plants should be next to either a different crop or empty farmland. For the plants on the edges of the plot, it's also ideal to have more farmland beyond the row ends and the outer rows; however, this is rarely done since it amounts to leaving the edges of the available field empty. Full details of the growth mechanics are given below.

### Accelerating growth
Using bone meal on any crop plant has a chance to advance it a random number of growing stages, allowing you to harvest it faster.

Bees can also be used to accelerate the growth of crops by pollinating them. After collecting pollen from flowers, bees visually drop pollen particles as they make their way back to their hive or nest. If these particles land on a crop, the crop advances one growth stage. Each bee can pollinate up to 10 crops per trip. Players can utilize this behavior by placing their crops between beehives and flowers to maximize crop pollen exposure. For more details, see Bee § Pollinating.

### Harvesting



Crop stages.


Crops can be harvested at any time by left-clicking on them with or without a tool, but when immature, they yield only one of the corresponding seed item. When mature, wheat yields 0-3 seeds and one item of wheat. Carrots and potatoes yield 1-4 of the crop when mature. Mature potato plants have a 2% chance of dropping a poisonous potato in addition to the normal potatoes. Beetroots drop 0-3 seeds and 1 beetroot.

Because harvesting one block at a time can become very tedious, methods for automatically harvesting fields have been developed. The most common tactic is to flood the field with water (which harvests all the plants it touches), but other methods are possible as discussed below.

## Growth rate
Probability of a crop plant being in each of the eight growth stages, as a function of time.
The progression of crops over time is shown in the plot to the right. Each line represents the probability of finding a given crop in that particular growth stage, assuming ideal conditions. The plots for non-ideal conditions look similar with only the scale of the x-axis (time passed) being longer.

Early in the game it may be helpful to maximize the growth rate of a crop in order to quickly multiply the seeds and/or get some wheat quickly. Doing so requires some understanding of the growth mechanics which are discussed here.

Crop growth is prompted by random ticks—the same random events that, for example, causes  zombified piglins to appear in nether portals. For a given block, a random update occurs an average of once every 68.27 seconds in Java Edition, or once every 204.8 seconds in Bedrock Edition. However, the delay can vary widely, and it is rare, but possible for plants to gain a stage the moment after planting or grow two stages a moment apart.

| Surrounding farmland | Probability of crop per random tick(hydrated farmland) | Probability of crop per random tick(dehydrated farmland) |
|----------------------|--------------------------------------------------------|----------------------------------------------------------|
| 0                    | 14.29%                                                 | 7.69%                                                    |
| 1                    | 16.67%                                                 | 8.33%                                                    |
| 2                    | 20.00%                                                 | 9.09%                                                    |
| 3                    | 20.00%                                                 | 10.00%                                                   |
| 4                    | 25.00%                                                 | 11.11%                                                   |
| 5                    | 25.00%                                                 | 12.50%                                                   |
| 6                    | 33.33%                                                 | 12.50%                                                   |
| 7                    | 33.33%                                                 | 14.29%                                                   |
| 8                    | 33.33%                                                 | 14.29%                                                   |

During every update, a crop plant gets a chance to grow to the next stage with the exact chance depending on conditions:

- As noted above, growth requires alightlevel of at least 9 in the block above the plant.
- The growth probability is1/(floor(25/points) + 1), where "points" is as follows:
	- Thefarmlandblock the crop is planted on gives 2 points if dry or 4 ifhydrated.
	- For each of the 8 blocks around the block on which the crop is planted, dry farmland gives 0.25 points, and hydrated farmland gives 0.75.
		- Note that if a field is bordered with anything besides more farmland, the plants at the edge grow more slowly.
- Having a crop of the same type diagonally from another of the same type will halve the growth rates of both crops. This does not stack.

If any plants of the same type are growing in the eight surrounding blocks, the point total is cut in half, unless the crops are arranged in rows. That is, having the same sort of plant either on a diagonal or in both north-south and east-west directions cuts the growth chance, but having the same type of plant only north-south or east-west does not. The growth chance is only halved once no matter how many plants surround the central one.


Expected number of successful harvests per hour as a function of the time elapsed at harvest. Applies to crops planted in rows surrounded by hydrated farmland.
From this we can figure the growth periods for the common cases:

|  |  |  |
|--|--|--|
|  |  |  |
|  |  |  |

|  |  |  |
|--|--|--|
|  |  |  |
|  |  |  |

|  |  |  |
|--|--|--|
|  |  |  |
|  |  |  |

- For the fastest growth per seed, a full layer of hydrated farmland with crops in rows is ideal. Under these conditions, the probability of growth during each update is1⁄3, or approximately 33%. Most (4⁄5) planted crops reach maturity within 31minutes(about 1.5 minecraft days). In fact, 31 minutes is very close to the ideal time at which to harvest if an auto-farming system is set to a timer, precisely 31 minutes and 3.14 seconds. For all plants to have this probability, crop rows must be separated by empty farmland or by a different crop, and the edges and corners of the field must be empty farmland. However, this probability also applies to crops adjacent to one or two non-farmland blocks (e.g. blocks ofwaterin the middle of a field for hydration and/or a torch) due to thefloorfunction.


|  |  |  |
|--|--|--|
|  |  |  |
|  |  |  |

|  |  |  |
|--|--|--|
|  |  |  |
|  |  |  |

- For hydrated crops in rows at the edge of a field (having 3 blocks of non-farmland along one side), the growth probability is1⁄4(25%). Most planted crops in this case reach maturity within 41 minutes (about 2 minecraft days).[verify]


|  |  |  |
|--|--|--|
|  |  |  |
|  |  |  |

- For hydrated crops in rows at the corner of a field (having 5 blocks of non-farmland adjacent), the growth probability is1⁄5(20%). Most crops reach maturity within 52 minutes (about 2.5 minecraft days).[verify]


|  |  |  |
|--|--|--|
|  |  |  |
|  |  |  |

|  |  |  |
|--|--|--|
|  |  |  |
|  |  |  |

|  |  |  |
|--|--|--|
|  |  |  |
|  |  |  |

- Hydrated crops not in rows have approximately half the growth probabilities:1⁄6(16.7%) for mid-field plants,1⁄7(14%) for edges, and1⁄9(11%) for corners.


|  |  |  |
|--|--|--|
|  |  |  |
|  |  |  |

|  |  |  |
|--|--|--|
|  |  |  |
|  |  |  |

- The usual worst-case conditions for growing are crops placed out of rows on dry farmland. In this case, the growth probability is1⁄13(approximately 8%) for the middle crops,1⁄16(6%) for the edges, and1⁄19(5%) for the corners.


|  |  |  |  |
|--|--|--|--|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

- The worst case would be two crops diagonally adjacent on dry farmland (all other surrounding blocks being non-farmland) which has a growth probability of1⁄23, about 4%.
- The average rate of production per wheat crop can be found by the expression (6.591 x Growth Probability) wheat per hour, assuming the crops are harvested as soon as they are fully mature.


Later in the game, the highest yield per area of a given field may be more important than the fastest growth per seed. Fields sown solidly to achieve this with a single crop do grow at half the speed, but they also let you separate each type of crop into its own respective field and harvest one type all at once. However, one large field with alternating rows of different crops would still grow faster than smaller fields each sown solidly with a single crop.

For melons and pumpkins:

| Sides to grow to | Surrounding farmland | Probability of fruit per random tick,(hydrated farmland) | Probability of fruit per random tick,(dehydrated farmland) |
|------------------|----------------------|----------------------------------------------------------|------------------------------------------------------------|
| 1                | 0                    | 3.57%                                                    | 1.92%                                                      |
|                  | 1                    | 4.17%                                                    | 2.08%                                                      |
|                  | 2                    | 5.00%                                                    | 2.27%                                                      |
|                  | 3                    | 5.00%                                                    | 2.50%                                                      |
|                  | 4                    | 6.25%                                                    | 2.78%                                                      |
|                  | 5                    | 6.25%                                                    | 3.13%                                                      |
|                  | 6                    | 8.33%                                                    | 3.13%                                                      |
|                  | 7                    | 8.33%                                                    | 3.57%                                                      |
| 2                | 0                    | 7.14%                                                    | 3.85%                                                      |
|                  | 1                    | 8.33%                                                    | 4.17%                                                      |
|                  | 2                    | 10.00%                                                   | 4.55%                                                      |
|                  | 3                    | 10.00%                                                   | 5.00%                                                      |
|                  | 4                    | 12.50%                                                   | 5.56%                                                      |
|                  | 5                    | 12.50%                                                   | 6.25%                                                      |
|                  | 6                    | 16.67%                                                   | 6.25%                                                      |
| 3                | 0                    | 10.71%                                                   | 5.77%                                                      |
|                  | 1                    | 12.50%                                                   | 6.25%                                                      |
|                  | 2                    | 15.00%                                                   | 6.82%                                                      |
|                  | 3                    | 15.00%                                                   | 7.50%                                                      |
|                  | 4                    | 18.75%                                                   | 8.33%                                                      |
|                  | 5                    | 18.75%                                                   | 9.38%                                                      |
| 4                | 0                    | 14.29%                                                   | 7.69%                                                      |
|                  | 1                    | 16.67%                                                   | 8.33%                                                      |
|                  | 2                    | 20.00%                                                   | 9.09%                                                      |
|                  | 3                    | 20.00%                                                   | 10.00%                                                     |
|                  | 4                    | 25.00%                                                   | 11.11%                                                     |

