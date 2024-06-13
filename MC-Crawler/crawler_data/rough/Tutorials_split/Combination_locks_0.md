# Tutorials/Combination locks
Combination locks are a type of redstone circuit. They generally have a number of components which must be set in the right combination in order to activate something such as a door. Combination locks can be very useful in creating adventure maps. Note that if you are playing in survival multiplayer, other players will still be able to break into the mechanism and cause it to activate without knowing the password.

## Contents
- 1 Order-insensitive combination locks
	- 1.1 Lever lock
	- 1.2 Item frame lock
	- 1.3 RS NOR Combo Lock
- 2 Order-sensitive combination locks
	- 2.1 Order-sensitive changing code XNOR Combo Lock
	- 2.2 Order-sensitive RS NOR Combo Lock
		- 2.2.1 Tutorial Video
		- 2.2.2 Tutorial video
		- 2.2.3 Combination lock with order-sensitive reset

## Order-insensitive combination locks
### Lever lock
















































Lever lock  16 (24) combinations
A lever lock is one of the easiest redstone locks to create. Each lever doubles the number of combinations the lock has. The possibilities can be found using 2n, where n is the number of levers used.

When constructing, you will probably first want to place the levers and put them into the desired positions. Next, you should place the redstone torches and repeaters. Torches go behind levers that are down and repeaters go behind levers that are up. When you are done, all of the torches and repeaters should be turned off. If not, double check any components that are turned on.


Detailed Instructions
Follow these steps carefully.
Step 1

First, place an 11 block row of any block, and make it two blocks high. Then, add a row of 7 branching off both sides.


Step 2
Add levers/switches on the bottom row of the 11 blocks, followed by signs on the top row. Each sign should have a number in order (1, 2, 3 etc.). Alternatively, you can make the signs have letters or words on them instead.
 

Step 3
Place a repeater in front of each block of the row that has the levers.


Step 4
According to the password you want, you need to place a block in front of the switches that make up your password and put a redstone torch on top of each. For example, if your password for 1-2-6 (like in the example), each block and redstone torch is placed in front of switches 1, 2 and 6.


Step 5
Next, place a block in front of each block that you just placed. Fill all the spaces in between the blocks with repeaters.


Step 6
Place a row of redstone dust in front of the repeaters and blocks.


Step 7
Place a strand of the redstone, starting from the middle, down to the 2nd last row. At the last row, place one block in front of the redstone.


Step 8
Add one redstone torch on top of the block just added. Then, add another block on top of the torch. Once you've done this, add a door on top of that block.


Step 9
Your passlock door is finished. To activate, flick all of the levers of which you had the password made up of, but no others. For example, if your password is 1-2-6, turn the levers below the signs that say 1, 2, and 6, on, but all the others should be off. The door should open.
  

Final Touches
Cover all the redstone with blocks, so that players can't see it.


Notes
The design shown in these directions can have up to 29 inputs. Larger amounts are more secure; the number of possibilities is 2^c, where c is the number of levers used. You can't have more than 29 inputs with this design as the redstone signal won't travel far enough.



| Demonstration video (view on YouTube) |
|---------------------------------------|
|                                       |


### Item frame lock









































































































































Item frame combination lock  512 (83) combinations
Item frame combination locks are a step up in complexity from lever locks. Items in item frames can be rotated into 8 different positions. This rotation can be detected by a comparator which will output a signal strength from 1 to 8 depending on the position. Since each item frame has 8 possible states, the number of possible combinations can be found with 8n, where n is the number of item frames.

The horizontal redstone paths on the floor decrease the signal emitted by the comparator down to a fixed strength of 1, and then feed it into an "A OR NOT B" gate that is true if the strength is either too small (B is not powered, i.e. false) or too large (A is powered, i.e. true). These gates are all ORed together so that the overall result is true if any item frame in the lock is misplaced; finally a torch (optional) inverts the result.

If you want to make it extra tricky, it is also possible to detect an empty item frame by when a comparator doesn't output anything. Simply leave a repeater connected to the comparator and feeding into the vertical redstone wire on the right side; a filled item frame will give a signal strength of 15 out of the repeater and keep the door locked.

| Tutorial video (view on YouTube) |
|----------------------------------|
|                                  |

### RS NOR Combo Lock
Connect a series of buttons to the S-input of RS Latches. Feed the Q or Q (choose which one for each latch to set the combination) outputs of the RS Latches into a series of AND gates, and connect the final output to an iron door. Finally, connect a single button to all the R-inputs of the RS Latches. The combination is configured by using either Q or Q for each button (Q means that the button would need to be pressed, Q don't press).

Example:




With the automated reset it causes the correct combo to cause a pulse instead of a "always on" until reset.

