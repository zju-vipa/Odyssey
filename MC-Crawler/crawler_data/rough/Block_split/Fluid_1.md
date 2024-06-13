#### Flow direction
Fluids consider the shortest distance to the edge of a cliff, and prioritize flowing in that direction.
The shape of the ground around a flow is considered when evaluating its spread, giving preference to the creation of water or lava falls, for aesthetic purposes. During the evaluation of horizontal spread, the 5-block area around source and flowing blocks is checked for air one block below the fluid block. These air blocks, and the blocks preceding them, are all converted to fluid blocks with depth level of 1 greater than the current block to establish a simple flow, but are not added to the collection for later consideration.

For example, the flow of water from a single source placed within 7 blocks of an edge is only one block wide to the edge, and then falls as a one block wide stream, as demonstrated in the image to the right.

#### Directional flow
Normal water spreading
Water normally spreads equally in all directions from a waterlogged block, as seen to the right.

In the same test setup the water flow from a stair or banner is one-directional.

- Water flowing from a waterlogged stair.

### Dripping
Lava seeping through one layer of dirt
If particles are fully enabled in the options menu, solid blocks that have air below and fluid above drip, as a visual indication that only one layer of blocks separates the player from the fluid above. Dripping lava does not cause damage or start fires. It can take several seconds before dripping starts.

### Block updates
These actions cause a fluid block to update:

- Another block is placed into its space
- Fluid starts to flow in from an adjacent block
- An established incoming flow stops

Generated structures never cause block updates to adjacent fluids when they generate. For example, a cave entrance that is created partly below water level at the edge of a body of water or lava does not cause the fluid to flow until it receives a block update. On the other hand, fluids created as part of a structure flow immediately if not completely confined; this includes holes in the bottom of an ocean that open into a ravine below.

### Mixing
When the two fluids interact, the results vary depending on the position of the fluid source.

- If lava flows vertically into a water source block, the water source block turns intostone.
- If lava flows vertically into flowing water, the flowing water turns intostone.
- If lava flows horizontally into water, the lava turns intocobblestone.
- If water flows horizontally into flowing lava, the lava turns intocobblestone.
- If water flows vertically into flowing lava, eithercobblestoneor nothing may result.
- If water flows into a lava source block, the lava source block turns intoobsidian.
- If water falling vertically touches a lava source block on any side, the lava turns intoobsidian—even if the water would not otherwise run into the lava.
- If lava flows oversoul soilnext toblue ice, the lava turns intobasalt.


