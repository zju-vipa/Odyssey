# Fluid
Fluids are blocks that are able to flow over the terrain, forming rivers or falls. There are two blocks of this type in the main versions of Minecraft: water and lava.

## Contents
- 1 Properties
	- 1.1 Mechanics
		- 1.1.1 Depth
		- 1.1.2 Spread
		- 1.1.3 Flow direction
		- 1.1.4 Directional flow
	- 1.2 Dripping
	- 1.3 Block updates
	- 1.4 Mixing
- 2 Video
- 3 History
- 4 Issues
- 5 Gallery
	- 5.1 Screenshots

## Properties
Fluids can be placed like solid blocks, but cannot be picked up without a bucket or a glass bottle.

When placed in open terrain, fluid blocks are a source for a flow, unless they are confined by other blocks. A completely confined fluid renders as still.

Water and lava as still blocks.
Source blocks that are at least partly liberated begin to flow, spreading according to the flowing fluid rules, and render as flowing, with animated lines demonstrating their direction of flow.

Lava block open to flow on one side
A source block appears as being "full" nearly to the top of its containing blocks (if any) while flowing fluid blocks appear to be "emptier" the further they are from their source.

Fluids can interact with each other, and with other blocks they are placed next to or flow over or past, according to the properties of the affected block.

Flowing fluids exert pressure on entities pushing them in the direction of the flow. Item drops that fall into a flowing fluid are carried along until they get caught in an eddy or the flow reaches its maximum extent. Mobs that are able to float in fluids do not drown, but cannot swim upstream. The minority of mobs that swim (such as fish and axolotl) can also swim upstream.

Fluid blocks are non-solids in the same way that air is, so placing a solid into a fluid block, source or flowing, succeeds if placement detects the side of a solid block through the fluid.

Water source blocks placed such that they create a waterlogged non-solid block behave as any source block would, with the exceptions noted in the following sections.

Water cannot be placed in the Nether, in both survival mode and creative mode. The only way to get water into the Nether is by using the /setblock or /fill commands.

When two fluid sources are directly adjacent to an air block (or a waterloggable block for water), the block is filled with the corresponding fluid. This only happens if the corresponding game rule is set to true (waterSourceConversion for water, set to true by default; lavaSourceConversion for lava, set to false by default).

### Mechanics
Water flowing down a cliff, demonstrating flowing mechanics.
#### Depth
Fluid blocks have a depth value that measures how "empty" it is. A source block is "full" with a depth value of 0. Flowing fluids have a depth value equal to their source's depth + 1, with a maximum possible "emptiness" value where the flow stops. Thus, a flowing block next to a source has depth value 1, the next further away 2, and so on until the flow stops. If the flow travels down in elevation, the depth resets to 0 at the new elevation.

The maximum emptiness depth for water is 7. Lava in the Overworld or the End has a maximum depth of 3, but in the Nether its maximum depth value is 7. The maximum distance a fluid can flow from its original source block is a taxicab distance corresponding to the maximum depth of that fluid.

The rendering of fluids is controlled by their depth values both in the height of fluid level and the direction of flow displayed.

#### Spread
- Water spreading from source
- Lava spreading from a source
- Water flowing around fence posts already placed

Once a source block is placed, the fluid spreading procedure begins. It does not matter if the source placed makes a waterlogged block or is placed into a block of air; both work the same way.
This block is the first of a list of blocks involved in the spreading procedure.
The fluid spreading procedure also begins when a fluid block that has stopped flowing receives a block update.

First, each open side of a fluid block starts a flow. A water block in a flat plain spreads out in all four directions until it reaches the depth limit, forming a diamond shape spanning fifteen blocks point-to-point. A water source floating in midair flows out to each of its four sides and then down. Each flowing block created is added to a list of blocks to be considered for further spreading.

Now the blocks directly below each source or flowing blocks on the "spreading list" are checked:

1. If that block isair, it is replaced by a flowing fluid block with a depth value of 0. This new block is also added to the "spreading list".
	- Because of this, a fluid can flow much farther if it flows downward occasionally than if it remains on a flat surface.
2. If the block below is a waterlogged,non-solid block, then checking stops as the waterlogged source block has its own "spreading list".
3. If the block below is a type ofnon-solid blockthat is affected by the fluid, then it may be converted into a droppeditem. The block is then replaced by a flowing block with depth value 1 greater that the block above and is added to the spreading list. The block above is removed from the "spreading list".
4. If the block below is asolid block, or one of a few non-solid blocks (e.g.fences) that are unaffected by fluids, flow spreads out to all open sides. These additional flowing blocks are added to the list.
	- If all four of the surrounding blocks are also solid, the spreading procedure stops. This is how a lava or water column that does not spread over the ground can be created.
5. If the block below is a fluid block of another type, the rules for mixing fluids are considered. If new flowing blocks are created they are added to the list.
6. If the block below is a source block of the same fluid, then flowing stops.

Flowing fluid has a speed value that governs how fast the spreading effect takes place. Water in the Overworld moves at 1 block every 5 ticks, or 4 blocks per second. Lava in the Nether moves at 1 block every 10 ticks, or 2 blocks per second. However, lava in the Overworld is much slower, and moves at only 1 block every 30 game ticks, or 2 blocks every 3 seconds.

