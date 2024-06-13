# Tutorials/Water-powered boat transportation
Water-powered boat transportation is a flexible and reasonably easy way to transport mobs and villagers along arbitrary paths (even uphill‌[BE  only]) using only the power of flowing water, without the need for any tools more exotic than a bucket and pickaxe, and needing only three common materials (water, buttons‌[BE  only] or signs, and common building blocks). No rowing, rails, minecarts, redstone gadgets, or bubble columns are needed, just a boat and water. With proper water management, one can construct flowing moats around arbitrary areas in which a boat can circle endlessly. The boat can even change elevation up or down using only the power of water flow.

## Contents
- 1 Water management
	- 1.1 Extending a straight channel
	- 1.2 Turning a corner
	- 1.3 Shifting to one side
	- 1.4 Example: Endlessly circling moat
- 2 Floating uphill
	- 2.1 Basic up-step
	- 2.2 How it works
	- 2.3 Practical construction
- 3 Gallery

## Water management
The illustrations in this article control water using buttons. You can use either buttons or signs in Bedrock Edition, but you must use signs in Java Edition. Buttons require less wood to craft, and are easier to identify in the illustrations.

Signs or buttons are used to block the water at the end of the flow in a channel, forming a gap between one channel and the next. The current from the end of the first channel pushes the boat into the gap, and the second channel's current must pull the boat across the gap, otherwise the boat gets stuck in the gap. The trick to pulling the boat into the next channel is to use only one water source block on each channel, right next to one of the buttons, to create a flow away from the gap.

To make channels wide enough to transport a boat, and remain on a level surface without changing elevation (elevation changes are described later), the water flow must be managed so that the channel can turn a corner, or keep moving in the same direction. The schematics below illustrate a method of creating a corner turn, and methods of extending travel in one direction by shifting the flow over a bit when the water runs out from the water source block.

The flow direction is often diagonal in any implementation of a closed-loop flowing moat. This is fine. The important thing is to have one flowing region push the boat into the gap, and the next flowing region pull the boat out of the gap.

As the boat crosses the gap, it appears submerged briefly under the next flow until it clears the gap, after which it floats up. This is not a problem; the boat does not capsize. However, in Java Edition, it is a good idea avoid exceeding 4 blocks taxicab distance between water sources to avoid submerging the boat.

### Extending a straight channel
Water flows only so far before it dies out. To continue the channel in the same direction, it needs to be extended. You can do this with a gap and either one or two water source blocks on the other side of the gap. Two water source blocks provide a flow straight down the channel, which moves the boat faster. These transitions can be stacked indefinitely.

















↘

↘



S

→

→


↘

↘



S

→

→
















Extending a straight channel by transitioning to a straight flow, using the two water source blocks labeled S.

### Turning a corner
A corner involves creating a gap just before or after the corner, and starting the new flow on the other side of the gap. The new flow must flow away from the gap.










↗

↗










↗

↗




→

→



↗

↗




→

→



S

↗

















Example of left turn. Signs or buttons create a gap between channels. The water source block S is placed so that water flows away from the gap and along the next channel.







↖

↖








↖

S















↗

↗

↗

↗




↗

↗

↗

↗















Left turn with the gap after the corner, taking advantage of diagonal flow. The source block can be on either side of the channel.







↑

↑








S

S















↗

↗

↗

↗




↗

↗

↗

↗















It is also possible to transition to a straight flow using two source blocks, as long as the next transition pulls the boat across the next gap.

In the first example, the next turn or shift must be to the right, because that is the direction of the diagonal flow.

In the second example, the source block can be on either side of the channel, depending on the direction of the next turn or shift. The water should flow diagonally to the right if the next turn is to the right, and diagonally to the left if the next turn is to the left.

In the third example, you can have another straight flow only in the same direction; you cannot have a new straight flow perpendicular to a previous straight flow, or the boat cannot be pulled across the gap. The straight flow must end with a gap across it, and if the next flow is a turn, it must have a diagonal flow to pull the boat across the gap properly. Otherwise the straight flow can be continued with another straight flow.

### Shifting to one side
Often you may want to continue a flow in the same direction but shift it to one side by one or more blocks, to align the flow with something ahead. You can stack these single-block shifts, making a diagonal channel, until the water runs out, and then you must create a new gap. Just make a channel that keeps shifting to the left or right as needed.

The directional shift (not the flow) can be perpendicular to the desired direction, or diagonal. The boat's movement is slightly faster with the gentler turn into a diagonal flow.


































↗

↗

↗

↗


→



↗

↗

↗

↗


→



S

↗

































Example of left shift by one block. The flow from water block S is diagonal due to its placement.






























↗

↗



S

↘








↗

↗

↗



↘

↘






↗

↗

↗

↗








→



↗

↗

↗










→



S

↗
































Example of left shift by three blocks. To guarantee the boat gets through, the channel should be four blocks wide in the diagonal path.




















↗

↗

↗

↗






S

↗

↗

↗















↗

↗

↗

↗






↗

↗

↗

↗




















Alternative 3-block shift without diagonals. In this case the next turn or shift must be in the same direction (left).

Either the first or second designs can be adjusted easily for a two-block shift.

### Example: Endlessly circling moat
See also: Tutorials/Endless circling pool

The smallest endlessly circling moat that can accommodate a boat.
The smallest circling pool that can accommodate a boat has one solid block in the center and four quadrants of water flowing from one corner of each quadrant. This design requires a 7×7 area, 1 layer, 4 water source blocks, and 8 buttons or signs — one on each side of the central block and one on the wall opposite each central sign or button.





















↗

↗



S

↘






S

↗



↘

↘





















↖

↖



↙

S






↖

S



↙

↙




















The smallest circling pool that can accommodate a boat, using four water source blocks and eight buttons.
This can be used as an AFK pool for the purpose of continually moving to avoid getting kicked off a server. The advantage over a normal AFK pool is that you don't get hungry because you're in a boat.

Remember, in Java Edition you need to use signs, not buttons. You can use either signs or buttons in Bedrock Edition.


## Floating uphill

  

This tutorial is exclusive to  Bedrock Edition. 


In Java Edition, the simplest way to make a boat float uphill is to use soul sand to build a bubble column elevator, although this requires a foray into The Nether or an ancient city to obtain the soul sand. The technique described in this section for floating a boat uphill doesn't work in Java Edition because boats want to sink, whereas in Bedrock Edition, boats want to float.

In Bedrock Edition, it is actually possible to cause a boat to be propelled uphill using only the power of water flow; no fancy techniques like pistons or bubble columns are required. A boat can be made to float up a slope as steep as 1⁄2 (one block elevation per two blocks horizontal distance) with careful attention to water flow management.

The concept involves a zig-zag water flow, changing diagonal direction at each step, while ensuring that all surface water is flowing, and the necessary deeper water at the step is used to buoy the boat up into the flowing water. As with the level-ground water management techniques described above, each section of water flow must push the boat across an empty space into the next flow, and the next flow must pull the boat out from the previous flow.

### Basic up-step
To float a boat up a step, the construction requires blocks to form a channel with a step, four buttons (or signs), one water block, and one temporary block (such as dirt) to be removed as the final step.

In the blueprints below:

- Stone represents the water channel.
- The water flow direction isupin these illustrations.
- The buttons are shown unattached in the diagrams. Each button is actually attached to the channel wall nearest to the button.
- The incoming water is assumed to be diagonal flow up toward the temporary dirt block.

The final block to be placed is the water source block. The temporary block of dirt causes the water to flow over the step. Without the block of dirt, the water simply stops at the step. After the water is placed, destroy the block of dirt.

** Up step with zigzag flow left to right **
The incoming water in the lower channel should be upward diagonal flow toward the dirt block on the left. The water block on the left resumes the flow diagonally upward to the right.

Layer 1
























Layer 2
























Layer 3





































** Up step with zigzag flow right to left **
Each successive step is a mirror image of the prior one. Here, the incoming water in the lower channel should be upward diagonal flow toward the dirt block on the right. The water block on the right resumes flow diagonally upward to the left. 

Layer 1
























Layer 2
























Layer 3



































Remember the dirt block shown is temporary. It must be removed after placing the water source block.

### How it works
After the final dirt block is removed, the two-block-wide space in front of the step has a void space (occupied by a button) and a still-water block (where the dirt used to be). Another void space is upstream ("downhill" direction) one block diagonally from the void space at the step. Otherwise the channel is completely filled with flowing water. Because the boat is bigger than one block, it does not get stuck in either void space. The current pushes the boat diagonally into the still-water block at the bottom of the step, at which point the boat floats up into the flowing water above, and the boat continues on its way.

The boat is always floating downstream, but at each step, it runs into submerged still-water block that buoys the boat up into the next flow. In this way the boat can climb uphill.

The boat submerges while navigating the step, but mobs in the boat do not drown. The top half of a villager's head is always exposed when the boat is submerged.

### Practical construction
Here is a simple procedure for constructing a water-powered uphill boat channel, using a step depth of 3 blocks for each 1 block increase in elevation. The example illustrates a channel that raises the boat in height by four steps, using only water power.

- 1. Create the channel steps and make walls around the channel.2. Place dirt blocks at the bottom of each step on alternating sides.
- 3. Place a button behind ("downhill") and diagonally up from each dirt block and from each step. Add more wall blocks to accommodate the buttons.4. Place a water block on the wall block diagonally up ("downhill") from each dirt block. Each wall block that gets a water block is indicated by a torch.
- 5. Remove the dirt blocks and place a boat at the bottom. Watch it float upward to the top!
- This is a steeper hill, with a step depth of 2 blocks for each 1 block increase in elevation. It is constructed exactly the same way.

