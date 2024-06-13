# Tutorials/Pumpkin and Melon farming
This is a tutorial on how to farm pumpkins and melons, both manually and automatically. For other types of farming see Farming.

## Contents
- 1 Growth mechanics
	- 1.1 Finding Seeds
	- 1.2 Growth Factors
- 2 Manual farms
	- 2.1 Simple farms
	- 2.2 Large farms
	- 2.3 Multi-level farms
	- 2.4 Rapid-harvest farms
- 3 Semi automatic farms
	- 3.1 Basic design
	- 3.2 Stackable design
		- 3.2.1 Base Layer
		- 3.2.2 Piston and Farm Layers
		- 3.2.3 Cap and Water Layers
- 4 Fully automatic farms
	- 4.1 Efficient pumpkin/melon farm
	- 4.2 Opaque block detection farms
		- 4.2.1 Single plant detection
		- 4.2.2 Dropper hopper trigger
		- 4.2.3 Dual-piston growth detection
	- 4.3 BUD circuit farm
		- 4.3.1 Design 6 (doesn’t work in bedrock edition)
	- 4.4 Vertical observer farms
		- 4.4.1 Design 7
		- 4.4.2 Design 8
	- 4.5 Horizontal observer farm
		- 4.5.1 Design 9
		- 4.5.2 Design 10 - stackable horizontal piston observer melon/pumpkin farm
	- 4.6 Time-based farm
		- 4.6.1 Design 11 - High-density pumpkin and melon farm

## Growth mechanics
Melons and pumpkins use essentially the same mechanics for growth and can be easily farmed with the same techniques. Once the plants are mature, they provide a steady supply of fruit for your needs. Surprisingly, water is not needed to grow pumpkins or melons. When planted, they create a stalk that starts out short, but grows and becomes yellow as it matures. Only mature stalks can grow pumpkins and melons.

### Finding Seeds
To begin farming, seeds must first be found. You can either find seeds in chests or find whole melons or pumpkins and craft them into seeds.

- Pumpkins can be found growing "wild" in anybiomewith grass[1]or intaigavillages.
- Melons can be found growing "wild" injungles[2]or insavannavillages.
- Pumpkin and melon seeds can both be found inminecarts with chestsinsidemineshafts, and in chests indungeons.

If you do have a whole pumpkin or melon, but no seeds, simply place the pumpkin in a crafting grid, which yields 4 seeds, or, alternatively, place the pumpkin somewhere and use shears on it. The melon drops melon slices when mined, yielding 1 seed each when putting in a crafting area. 

On average, it takes around 272 seconds (4 minutes, 31 seconds) for each stem to generate fruit (be it a Pumpkin or a Melon).

### Growth Factors
The growth rate of melon and pumpkin stems and the spawning of melon and pumpkin fruit is determined by the same growth rate algorithm as for wheat, carrots, and potatoes. The stem itself has 8 phases of growth until maturity. Bone meal may be used to accelerate growth.

The attempt to grow a fruit happens when the mature stem would grow again (to "phase 9") and is not already adjacent to an instance of its fruit. First one of the four sides is chosen. If this space is suitable (empty with dirt, coarse dirt, rooted dirt, grass block, farmland, podzol, mycelium, moss block, mud or muddy mangrove roots beneath) the fruit is created. Bone meal does not force fruit production.

- Thus, hydratedfarmlandadjacent increases growth rates of stems and production rate of fruit, having the same stem type adjacent to the stem (unless in rows) reduces growth rates and fruit production, light level 9 in the block above the stem is required for any growth, etc.
- The maximum probability of fruit production from a single stem would, therefore, require a stem in hydrated farmland with hydrated farmland on all eight sides, with four of those farmland blocks remaining unplanted (the corners may be planted with some other crop). Practical farms often accept reduced per-plant production rates (⅔, ⅓, or even ⅙ of the maximum) for greater space efficiency and ease of harvest.

Both sorts of fruit revert farmland below them to dirt when they grow. Pumpkins can most easily be harvested with an axe, and drop whole as items. Melons can be broken quickest using an axe. They also break faster using a sword but at the cost of double durability. While melons grow as blocks, the melons are broken into 3–7 slices by harvesting (unless a Silk Touch tool is used). In both cases, the harvested fruit can be crafted back into seeds. Harvesting mature stems also produces seeds (1–4 per stem), but it is faster to wait for the already-mature stem to grow a fruit than to regrow a mature stem from seed.

## Manual farms
This section contains suitable layouts for farms that must be manually harvested. The percentages given are space efficiencies. Parenthesized values are theoretical maximums, which assume that there are free blocks surrounding the farm for the border plants to place melons. The maximum possible efficiency for any melon or pumpkin farm is 50% (one fruit per stem). Spaces, where fruit can occupy two or more stems, reduce the efficiency and yield. Question-mark blocks indicate that anything could be put in that spot—perhaps lighting, or other crops such as wheat, carrots, or potatoes. You may want to cover the water with a slab, a lily pad, or a carpet.

### Simple farms
The following grids provide different availabilities for designs of pumpkin and melon farms.

If you just want a quick, compact farm, use design D below. C and D have slightly lower efficiency, but both fit on a "standard farm plot", and are easy to harvest. Of those two, D likely has a faster growth rate due to the separated rows of stalks, but the middle row should not be open dirt/grass or farmland (or more stalks), because any fruit spawned there can tie up two stems. For C, the middle row can be anything except more stalks, for the same reason.

Design A is slightly larger and maximizes space efficiency. It can be tiled for larger farms, but alternate rows should be mirrored top-to-bottom to keep the efficiency. Design B is least efficient but fits in a slightly smaller plot.

| Farm Plan A, 9×10, 48.88%. | Farm Plan B, 9×8, 43.21%. |
|----------------------------|---------------------------|
| Farm Plan C, 9×9, 44.44%.  | Farm Plan D, 9×9, 44.44%. |

