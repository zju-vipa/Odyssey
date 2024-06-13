# Oxidation
Oxidation is a mechanic that causes most blocks made from copper to oxidize over time, changing their appearance. 

All blocks that oxidize can be 'locked' in their current oxidation state by being waxed with honeycombs, and can gradually be scraped of their wax and/or oxidation using an axe.

## Contents
- 1 Mechanics
	- 1.1 Waxing
	- 1.2 Deoxidation
- 2 Affected blocks
- 3 Achievements
- 4 Advancements
- 5 History
- 6 References

## Mechanics
Non-waxed copper blocks have four stages of oxidation (including the initial normal state). Lightning bolts and axes can remove the oxidation on copper blocks. 

As the block begins to oxidize (exposed copper), it gets discolored and green spots begin to appear. As the oxidation continues (weathered copper), the block is a green color with brown spots. In the last stage (oxidized copper), the block is teal with several green spots.

Oxidation is a purely visual mechanic in most cases. However, the light level of copper bulbs depends on the oxidation level. Normal copper bulbs have a light level of 15, exposed copper bulbs have a light level of 12, weathered copper bulbs have a light level of 8, and oxidized copper bulbs have a light level of 4.

Oxidation of copper blocks relies only on random ticks. Rain or water does not accelerate oxidation, and covering copper blocks with other blocks does not prevent oxidation.

In Java Edition, groups of non-waxed copper blocks oxidize far more slowly than single copper blocks that are spaced at least 4 blocks apart. This is because a block in a group being less oxidized than the others slows down the oxidation process for all other blocks within 4 blocks of taxicab distance. However, if one wishes to increase the oxidation speed, placing oxidized copper blocks around less oxidized copper blocks does not offer a speed improvement over simply placing the blocks 4 apart. The calculations for the oxidation behavior are as follows:

In Java Edition, when a random tick is given, a copper block has a 64⁄1125 chance to enter a state called pre-oxidation. This means a copper block enters pre-oxidation after approximately 20 minutes.

In pre-oxidation, the copper block searches its nearby non-waxed copper blocks for a distance of 4 blocks taxicab distance. If there is any copper block that has a lower oxidation level, then the pre-oxidation ends, meaning that this copper block does not weather. 

Let a be the number of all nearby non-waxed copper blocks, and b be the number of nearby non-waxed copper blocks that have a higher oxidation level. We derive the value of c from this equation: c = b + 1⁄a + 1. We also let the modifying factor m be 0.75 if the copper block has no oxidation level, or 1 if the copper block is exposed or weathered.[1] Then the oxidation probability is  mc2.

For example, an unweathered copper block surrounded by 6 unweathered copper blocks and 6 exposed copper blocks has a 21.7% chance to oxidize if it enters the pre-oxidation state. In this case, a = 12, b = 6, and m = 0.75.[2]

### Waxing
Using a honeycomb on a non-waxed copper block (or crafting them together) turns it into its waxed variant, which prevents the block from oxidizing entirely. Using an axe on a waxed copper block turns it into the respective non-waxed copper block.

### Deoxidation
Using an axe on an exposed, weathered, or oxidized copper block reverts it one stage to a regular, exposed, or weathered copper block respectively. The axe removes wax first, then oxidation layers.

Lightning can also remove oxidation from copper blocks. A lightning bolt striking an non-waxed copper block (or a lightning rod attached to one) removes all oxidation from the struck block, and may also deoxidize randomly selected copper blocks nearby.

In Java Edition, these additional blocks are chosen by random walks as follows: The position of the struck copper block is set as the start point. Then, the game performs 3 to 5 walks. In the beginning of each walk, a judgment point is set at the start point. For each step of the walk, the game randomly selects 10 blocks from a 3×3×3 volume centered on the judgment point. If an non-waxed copper block is found among these 10 blocks, the judgment point is transferred to the first such block found, and 1 oxidation layer of that block is removed (if the block is still unoxidized, the block stays as it is). The number of steps in a walk is between 1 and 8 (inclusive), chosen randomly for each walk. This means that one single lightning strike can deoxidize up to 41 blocks (1 block initially struck by lightning + 5 max walks*8 max steps in every walk).[3]

## Affected blocks
The following blocks are affected by oxidation:

- Block of Copper
- Chiseled Copper‌[upcoming]
- Copper Bulb‌[upcoming]
- Copper Door‌[upcoming]
- Copper Grate‌[upcoming]
- Copper Trapdoor‌[upcoming]
- Cut Copper
- Cut Copper Slab
- Cut Copper Stairs

