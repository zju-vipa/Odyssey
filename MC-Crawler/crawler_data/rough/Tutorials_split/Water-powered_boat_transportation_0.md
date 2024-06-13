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

