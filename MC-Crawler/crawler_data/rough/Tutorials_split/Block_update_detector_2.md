## Variations
Other devices can be built using the same underlying principle as the BUD switch.

### BUD in Bedrock Edition
This method no longer works in 1.14.1.
By using a waterlogged block that is not allowed to flow (through the use of trapdoors or other techniques) and an observer clock, if the player updates the waterlogged block rapidly and the observer clock is in the same chunk the clock will break and give a constant output out of both sides. Then whenever the block is next updated, one side of the clock will pulse off for one tick. You can create a BUD switch using this by linking up using both sides as the output of the BUD.

Video describing this phenomenon: 




### T-BUD
By eliminating the reset mechanism of a BUD switch, it becomes a T-BUD or Toggle-BUD. This device has two stable states, which it switches between when it detects a block update next to the piston. This is equivalent to a normal BUD connected to a T Flip-Flop, but much simpler to build. It is useful for tracking the state of blocks like furnaces, grass block, dirt, and beds. However, it has useful capabilities for placing some blocks two blocks away. When placing a piece of redstone dust two blocks away, the T-BUD activates when it is destroyed only. When placing a repeater two blocks away, the T-BUD activates only on the placement.

- T-BUD in first state
- T-BUD in second state

Note: As of Java Edition 1.7.4,[note 1] the repeater in the picture must be set to a two tick delay. If the repeater is left at one tick, it will work as a BUD.

Besides connecting the block moved by the piston and the repeater with redstone wire, a T-BUD can also use slime blocks sticking a redstone block (or a charged redstone conductor) to activate the repeater.

































Slime Block T-BUD

#### Compound slime block T-BUD
This type of T-BUD QC activates a piston without updating when extending, and uses moving blocks in front of the piston to stick it when retracting. It can detect an update immediately after completing retraction and very soon after extension.
























































































This design features not being affected by updates during extension.

1. ↑It is unconfirmed in which version this has become a requirement.


