### 
One of the fastest ways to descend in the game is falling, but ascending via ladders is not a fast method of upward transport at all. While a soul sand bubble column is one of the fastest ways of going up, soul sand is hard to acquire without a trip to the Nether. One simple method of ascending a downward flowing column of water is to hold down forward, sprint and jump at the same time, as their effect stacks together. When executed correctly, the player can rise at a speed of 6.98 m/s, three times the speed of climbing up ladders even in a downward flowing column of water. Based on this mechanic, the player can construct a simple 1×2 vertical shaft with the following materials.

- looking down the vertical shaft. Only the top water block is a source.
- The bottom of this sprint-swimming vertical shaft. Notice the height where the signs are placed.
- The 1×2 shaft design. "S" is water source, brown squares are signs, placed in numeric order.

#### Materials
a sign in one of the spaces attached to the side, and the water in the other space. 

[[File:FastShaftTop.png|thumb|looking down the vertical shaft. Only the top water block is a so

#### Construction
First, dig a 1 by 2 pit in the ground. place a sign in one of the spaces attached to the side, and the water in the other space. 

Second, stand in the pit between the water and the sign, and start digging below the water. When you reach the limit of your reach, start digging on the other side (below the sign). Remember to always keep the hole at least one block deeper below the water than below the sign, so that the water does not flow sideways and push you away from the optimal spot. You can stand slightly towards the side with air, while still touching the water, so that you can breathe.

If the player hits a cave or a lava pool, the flowing water will keep the player safe, turning all lava into obsidian or letting the player swim up and out of a cave. 

when the player reaches the intended y-level, block off the water with the sign as indicated in the images and they are free to expand the mining area. 

#### 
the positioning of the player while swimming up the shaft.
A player is 1.8 blocks tall and jumps 1.25 blocks, this means the player's head is 3.05 blocks above the ground, just enough to enter the water 3 blocks above. Once fully in the water, look up and hold sprint, forward and jump at the same to reach the fastest speed.

To go down the shaft, simply walk into the air column under the first sign. The player will drop down into the water below and take no fall damage.



## 
### Safety
Horizontal mining is not as dangerous as vertical. But there are some similar suggestions. Carry a water bucket and some blocks of some disposable, non flammable material (e.g. sand, gravel, cobblestone) somewhere on the player's hotbar. A block can be used to quickly plug the leakage in cases of lava, and water can be poured over source lava to turn it into obsidian, as well as to put out fires. (Flowing lava will usually turn to cobblestone, occasionally stone, if the water is a source block.)

### Terms and Definitions
Main shaft/access shaft: a 1×2 or 2×2 tunnel use accessing other tunnels.

Efficiency: how many ores the player gets for the amount of effort they put into the mine, or how many ores and cobblestone they dig to find them.

Thoroughness: how many of the ores the player extract per chunk.

The tradeoff: a mine can be made more thorough at the price of efficiency, or vice versa.

Layout: the top-down view of the mine.

Branch: the tunnels dug purely to gather ores.

Branch-length: how many blocks the player dig their branches out. One recommendation is to measure a length with the durability of a stone pickaxe.

Spacing: how far apart the branches are.

Completely Thorough: a mine that reveals 4 new blocks dug, and reveals every block within a chunk, is completely thorough.

Tiering: "stacking" one branch mine on top of another, in order to obtain a much greater degree of thoroughness without sacrificing too much efficiency.

### Efficiency vs Thoroughness
Efficiency in Minecraft mining is defined as how many ore blocks the player mines, relative to the time spent reaching them. Thoroughness is the percentage of the ores a player has extracted from a given chunk. Efficiency is approximated by blocks revealed per blocks mined, while thoroughness is approximated by blocks revealed per blocks in a chunk. Since both include "blocks revealed", they are often confused.

If we assume that all ores spawn in 2×2×2 cubes or larger, then there is no need to reveal every block. Mining three spaces wide, with four blocks between each shaft will be completely thorough. If we assume that 90% of ores are 2×2×2, but 10% are 1×1×1; while obtaining 100% unitary thoroughness then requires a spacing of 3 and a tiering distance of 2, the original mine (the 3-space 4-tiering) maintains a thoroughness of 98%. The 100% thorough mine requires mining twice as much stone while only increasing the total yield by 2%, resulting in half the efficiency.

In order to give an actual number for efficiency, we can use efficiency=100×(number of ores collected / number of blocks mined)-or, equivalently,
%efficiency = (number of ores collected/number of blocks mined)

Several assumptions must be made:

1. Ore is distributed randomly
2. Ore is oriented randomly
3. Ore occupies a certain width, whereby two tunnels running too close to each other would intersect the same orebody twice.

In Minecraft these assumptions are essentially true, though there is some distortion since diamonds only spawn once per chunk.

So we reach the crux of the argument; tunnel spacing. In the traditional "efficient" mining methods, tunnels are spaced close together in order to "observe" the maximum number of blocks possible, therefore removing all of the ore from an area. So, let's consider a spacing of 1; that is one tunnel separated by one block from another tunnel. During the digging of the first tunnel, several ore bodies are encountered. This tunnel has a high efficiency (in fact, the maximum efficiency possible, as we shall see later). The second tunnel has a very low efficiency because almost all of the ore bodies it encounters have already been removed by the first tunnel. This causes the efficiency of the mining operation to plummet. A spacing of 1 is incredibly inefficient. Now we move to a spacing of 2. This is a spacing that a lot of people use because it leads to 100% observed blocks in a single layer. However, with a spacing of 2, the second tunnel still encounters several ore bodies that have already been removed, so it is also quite inefficient. We can go on like this; as long as the second tunnel has a chance of encountering ore bodies which have already been removed by the adjacent tunnel, it will have a less than maximum efficiency. It follows that the most efficient way to mine is to place the second tunnel far enough away from the adjacent tunnel that there is no chance of encountering ores that have already been removed.

The problem has been modeled in MATLAB using a 2D slice of a real Minecraft level and a virtual mining procedure.[verify] The model mines a 1 block wide tunnel through the 2D layer and removes all diamonds it encounters, just like a real player would do. The model is limited to diamonds but the principle applies to all ores. It repeats the mining for different tunnel spacings, from 1 to 10. The model then records how many diamonds were mined for each case, how many blocks were removed, and calculates the efficiency of each spacing. A simple graph is produced:



The results indicate what is expected — that when tunnels are close together they are not efficient because the miner will encounter diamonds which were already removed by the adjacent tunnel(s). A good efficiency is reached at a spacing of around 6 blocks (that is, 6 solid blocks left in-between the tunnels). At this spacing, efficiency is about 0.017, corresponding to 1.7% of blocks removed being a diamond. At this spacing, the tunnels effectively become independent of each other and so, statistically speaking, the chance of encountering an ore are maximized because there is no chance the ore has been removed by an adjacent tunnel.(true independence would need spacings more than a chunk)  Above a spacing of 6, efficiency does not increase greatly because ore collection rate is simply a function of the distribution of ores within the level. Note: in the above graph, efficiency appears to drop-off at a spacing of 10. This is simply a limitation of the size of the level used to model the process, resulting in a large error at high spacings. If a larger level were used, the line would smoothly approach a maximum efficiency but never quite reach it.

In summary:

1. The term "efficiency" is often applied to the practice of making every block observable, however this is not usually the objective of a miner.
2. A more practical definition of "efficiency" describes the percentage of blocks removed that are ores, in other words efficiency = (ores removed / blocks removed).
3. A significant portion of the efficiency comes from the size of an ore cluster, or the chance of having already mined that ore from an adjacent tunnel.
4. A good efficiency, for diamonds, is reached at a spacing of 6. Since other ores are usually collected in copious amounts compared to diamonds, this spacing is recommended for every-day mining operations.
5. Maximum efficiency is reached in the case of infinite spacing between the tunnels. Or in other words, the humble single straight tunnel.

