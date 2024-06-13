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

#### Piston interactivity
Rails can be pushed and pulled by pistons. Pushing a rail upward may cause adjacent rails to become slanted. Subsequently pulling the rail back down again causes those newly-slanted rails to break because they are no longer supported on their upper end.

### Redstone component
The intersection rail at a T-intersection may be made to change its direction of curvature by applying redstone power using a redstone torch, lever, or button.

- 
- 
- 

Separate tracks are laid adjacent, but at the next level, lower or higher can sometimes cause issues. However, normally they do not interact with the switched rail.

### Minecart behavior
#### South-east rule


Main article: South-east rule
A minecart travels straight through a T-shaped intersection when entering from the "back of" the curved rail. It follows the curve when entering from either of the other two legs.

A minecart passes straight through a 4-way intersection constructed to have no curved rail. When entering the 4-way from east or west a cart turns according to the south-east rule.


#### Downhill rule

At non-curve track intersections, minecarts always travel downhill if they can. This is known as the downhill rule and overrides the south-east rule.


#### 

A block placed above the track at the downhill end of a ramp prevents minecarts from traveling down the slope, but not up. For a minecart to move down a diagonal tunnel, there must be clearance sufficient for a player to walk it.


#### Curve intersections
A diagram on how minecarts travel according to track curves.
If a straight track piece leads to a curve block and isn't attached to the curve, a minecart runs over the gap and continues to go straight over the curve. This is not applicable to other types of rails.

Notably, the minecart can exceed the normal 8 m/s speed limit while it jumps over the gap. For example, by placing intersections on every other block of a straight track, it is possible to travel (uncomfortably) at 10 m/s in a straight direction.

As with straight T-intersections and 4-way intersections, the practice of making a minecart jump track can be used to make one-way entries onto a track. On curve intersections the behavior is more intuitive because the cart simply proceeds in the direction it is already going, allowing designs that don't rely on the south-east rule.


#### Rail performance
To ascend from 0 to max speed, most minecarts needs 7 powered rails (a minecart with furnace has a lower top speed). After a certain number of rails, a minecart begins slowing down. This slowdown can be negated with a powered rail. A certain number of rails followed by 1 powered rail can then be repeated indefinitely to maintain full speed with the minimum amount of powered rails.

| Minecart type                              | Initial maximum rails at full speed | Subsequent maximums          |
|--------------------------------------------|-------------------------------------|------------------------------|
| Emptyminecartandminecart with TNT          | 7                                   | 3                            |
| Minecart with entity                       | 112                                 | Alternates between 38 and 26 |
| Minecart with chestandminecart with hopper | 85                                  | 20, then 29 onward           |

For example, a minecart with an entity would require 112 rails, then 1 powered rail, then 38 rails, then 1 powered rail, then 26 rails, then 1 powered rail, then 38 rails, etc. Note that these rails can go in any direction: going 112 rails diagonally would still require a powered rail.

A minecart with no rider at full speed can climb 10 blocks on an unpowered track. This suggests that a powered track is needed at a height of only 10 blocks to keep a cart climbing. However, the cart slows so much that it can reach only another 5 blocks high with 2 lengths of powered track starting at 9 blocks high. The minimum number of powered rails to keep the cart climbing perpetually is 3 every 6 blocks.

Carts with a rider, or minecarts with chests, have more momentum and so climb higher than carts that are unloaded. With a rider, a minecart can climb at least 24 blocks before needing powered rails to go higher.

### Mob behavior

  

This feature is exclusive to  Java Edition. 


In Java Edition, most mobs avoid walking on rails,[1] but they ignore rails when they are already on them. Jumping mobs like slimes, frogs[2], and goats can jump onto rails, but frogs and goats do not walk onto rails. Aquatic creatures like guardians, tadpoles, and fish that flop around on land can flop onto rails. Parrots can land on rails and endermen can teleport onto rails, although they do not walk onto them. In pursuit of their targets, zombies may push other mobs onto the rails in which case the mob on the rail ignores rails while on them. The only mobs that freely walk onto rails are spiders, cave spiders, and wardens.

In Bedrock Edition, rails don't affect mob pathfinding in any way.

## Data values
### ID
Java Edition:

| Name | Identifier | Form         | Block tags                       | Item tags | Translation key      |
|------|------------|--------------|----------------------------------|-----------|----------------------|
| Rail | rail       | Block & Item | prevent_mob_spawning_insiderails | rails     | block.minecraft.rail |

Bedrock Edition:

| Name | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key |
|------|------------|------------|----------------------------|----------------|-----------------|
| Rail | rail       | 66         | Block & Giveable Item[i 2] | Identical[i 3] | tile.rail.name  |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block states

Java Edition:

| Name        | Default value | Allowed values                                               | Description                                                                                                                                     |
|-------------|---------------|--------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| shape       | north_south   | east_westnorth_eastnorth_southnorth_westsouth_eastsouth_west | The two directions a rail connects to.For example, asouth_eastrail is a curved rail that connects to the south and to the east.                 |
|             |               | ascending_eastascending_northascending_southascending_west   | A rail that ascendstowardthe direction noted.For example, anascending_westrail is a straight rail that goes upward from the easttowardthe west. |
| waterlogged | false         | truefalse                                                    | Whether or not there's water in the same place as this rail.                                                                                    |

Bedrock Edition:

| Name           | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                      |
|----------------|---------------|---------------|----------------|-------------------------|--------------------------------------------------|
| rail_direction | 0x10x20x40x8  | 0             | 0              | 0                       | Straight rail connecting to the north and south. |
|                |               |               | 1              | 1                       | Straight rail connecting to the east and west.   |
|                |               |               | 2              | 2                       | Sloped rail ascending to the east.               |
|                |               |               | 3              | 3                       | Sloped rail ascending to the west.               |
|                |               |               | 4              | 4                       | Sloped rail ascending to the north.              |
|                |               |               | 5              | 5                       | Sloped rail ascending to the south.              |
|                |               |               | 6              | 6                       | Curved rail connecting to the south and east.    |
|                |               |               | 7              | 7                       | Curved rail connecting to the south and west.    |
|                |               |               | 8              | 8                       | Curved rail connecting to the north and west.    |
|                |               |               | 9              | 9                       | Curved rail connecting to the north and east.    |

## See also
- Powered rail
- Activator rail
- Detector rail

