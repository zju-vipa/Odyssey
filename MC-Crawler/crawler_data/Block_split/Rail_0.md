# Rail
Rails are non-solid blocks that provide a path along which minecarts can travel.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Chest loot
	- 1.4 Crafting
- 2 Usage
	- 2.1 Placement
		- 2.1.1 Piston interactivity
	- 2.2 Redstone component
	- 2.3 Minecart behavior
		- 2.3.1 South-east rule
		- 2.3.2 Downhill rule
		- 2.3.3 Ramp clearance/one-way effect
		- 2.3.4 Curve intersections
		- 2.3.5 Rail performance
	- 2.4 Mob behavior
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 Achievements
- 6 Video
- 7 History
- 8 Issues
- 9 Trivia
- 10 Gallery
	- 10.1 Screenshots
- 11 See also
- 12 References

## Obtaining
### Breaking
Rails can be mined with anything, but pickaxes are the quickest.

| Block     | Rail                  |
|-----------|-----------------------|
| Hardness  | 0.7                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 1.05                  |
| Wooden    | 0.55                  |
| Stone     | 0.3                   |
| Iron      | 0.2                   |
| Diamond   | 0.15                  |
| Netherite | 0.15                  |
| Golden    | 0.1                   |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


A rail also drops as an item when the block beneath it is removed, or a piston moves it into a space with no block below it.

### Natural generation
Rails can be found naturally running along the floor in mineshafts, both in the center of tunnels and under loot chest minecarts, and in the "pumpkin ring room" of woodland mansions.


### Chest loot
| Item  | Structure | Container | Quantity | Chance                         |
|-------|-----------|-----------|----------|--------------------------------|
|       |           |           |          | Java EditionandBedrock Edition |
| Rails | Mineshaft | Chest     | 4–8      | 78.4%                          |

### Crafting
| Ingredients      | Crafting recipe |
|------------------|-----------------|
| Iron Ingot+Stick | 16              |

## Usage
See also: Tutorials/Minecarts

A rail can be used as a minecart track and as a redstone component. A sequence of rails (including regular rails, activator rails, detector rails, and powered rails) is called a track.

### Placement
To place a rail, use a rail item while pointing at a surface facing the space the rail should occupy. A rail can be placed on:

- thetopof any full block (stone, dirt, blocks of gold, glass, etc.), including full-block mechanism components (command blocks,dispensers,droppers,note blocks, andredstone lamps)
- thetopof an upside-downslab, upside-downstairs, ortrapdoor.
- any of the above underwater (making the railwaterlogged)

Rails visually float 1⁄16 blocks above the ground, with an outline 2⁄16 blocks high.

A rail cannot be attached to the side or bottom of any block, but attempting to make such an attachment may cause the rail to attach to the top of a block under the destination space. For example, if a fence is on the ground, attempting to attach a rail to the side of the fence causes the rail to be attached to the top of the ground next to the fence instead.

More information regarding placement on transparent blocks can be found at Opacity/Placement.

A placed rail configures itself to be straight or curved according to rail blocks around it. 

- If there are no other rails adjacent, or if placed beside an existing stretch of track of any type, then inBedrock Editionthe new rail orients itself as a straight north-south track, and inJava Editionthe new rail orients itself in the direction the player is facing.
- A new rail placed at the end of an existing stretch of track continues the existing track in the same direction, either east-west or north-south.
- If there are two adjacent rails on its level, or one level up or down, the newly placed rail configures itself as straight or curved as needed to connect the other two.
- If placed between three adjacent rails (forming a T-junction) the newly placed rail configures itself as curved to join two of the sides.

- T-junction before filling in tracks
- T-junction after filling in tracks

Existing tracks one block up and down are considered for adjacency in the same manner, and the new piece of track gets laid as a curve, but unless space is left for sloping track sections, minecarts can continue past the curve only on level or one-block-down corners. In one-block-up corners, the cart ends up buried in the ground.

- Before placing the top block.
- Top block is placed as curve.
- Showing cart getting buried.

Some placement of rails produces track layouts that cause minecarts to collide and enter blocks.

- Minecarts always buried
- Minecarts get through

- If placed to form a 4-way intersection with no curved section, it does not form a cross-roads connection.
- If placed between four adjacent rails to form a curved intersection it always curves south-to-east.

- Curve controls minecart passage

Existing sections of track may be re-oriented, become sloping, or even change into curved sections when the new rail is placed adjacent to it:

- An existing straight, north-south rail re-orients to east-west when a new rail is placed at the east or west sides.
- If placed next to an existing rail that is one block up or down, the new rail slants up or down to join it. Rail "prefers", in order: west, east, south, and north. Other configurations can be created by placing and removing rails.
- If a track is placed perpendicular to an existing length of track, it appears as a straight rail, but in fact, it is curved according to the patterns for tee junctions as seen above; mine carts going through the intersection turn the corner. Breaking and re-laying track so that the intersection block is laid last causes the intersection block to be updated as a curved section.

