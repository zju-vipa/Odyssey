# Tutorials/Minecart booster
Minecarts behave in a unique manner when running alongside one another: they accelerate rapidly. This effect is used to create boosters. A booster consists of a short track with another minecart placed next to the track you want to boost. The two tracks must have one or more blocks of contact. When your minecart is next to the other cart, they will both accelerate. There is a maximum speed (8 m/s, 1 block = 1 meter), but the internal value from which speed is derived is not capped, allowing the cart to maintain the maximum speed for much longer than it would normally be able to. However, if a minecart is repeatedly accelerated this way for a long period of time, it may suddenly stop, most likely due to an integer overflow resetting the value to zero. To avoid this, make sure that no cart is continuously being boosted over a long period of time.

Example of two boosters in a loop. The first booster loop is continuously working, which will eventually cause the cart to stop. The second booster loop provides a pause by stopping every cart, every iteration. This creates a more reliable system.

## Contents
- 1 Boosting Principle
	- 1.1 Good (will result in a boost)
	- 1.2 Bad (will slow down cart)
- 2 Launcher types
	- 2.1 New-style door launchers
	- 2.2 Classic door launchers
	- 2.3 Powered Rail launchers
- 3 Booster types
	- 3.1 Two-way corner manual-reset
	- 3.2 One-way up-downhill manual-reset
	- 3.3 One-way auto-reset (south-west rule)
	- 3.4 One-way auto-reset (based on inclination)
	- 3.5 One-way auto-reset (reduced reset loop)
	- 3.6 One-way auto-reset (leveled and omnidirectional)
	- 3.7 Two-way auto-reset
	- 3.8 Two-way corner auto-reset
	- 3.9 Two-way auto-reset compact design
	- 3.10 Two-way auto-reset efficient design
	- 3.11 Uphill auto-reset booster
	- 3.12 Booster in turns
	- 3.13 Auto-Start booster
	- 3.14 Double Booster
	- 3.15 Spin Booster
	- 3.16 Triple Booster
	- 3.17 C-Booster
	- 3.18 Reverse Double-V Booster
	- 3.19 Multiplayer Tips
- 4 See also

## Boosting Principle
Do take note that the methods above are not the only configurations that can be used to boost a minecart. Instead, rely on the following principle when designing booster systems:

- A minecart pair will boost when they are side by side.
- As long as the carts are side-by-side, they will continue to accelerate, until reaching 8 m/s.
- Despite not exceeding this speed, they will continue to gain energy, illustrated by the fact that a longer booster is required to climb a taller hill or mine shaft without eventually slowing down and reversing.
- It is ideal to have the booster cart reset itself after use (i.e. return to its original position) so it can be used again right away, but this is not required.
- Thesouth-west ruleor other track layout techniques can be used to accomplish this reset.
- When boosting an unoccupied minecart it will travel about 9 tracks per booster length on level ground (not including reset loop)
- When boosting an unoccupied minecart it will travel about 6 tracks up per booster length (not including reset loop)
- An occupied minecart will go roughly 12 times an unoccupied minecart on level ground (110 per booster track)
- An occupied minecart will go roughly 3 times an unoccupied minecart upwards (16 per booster track)
- Stacked boosters (i.e. when more than one cart exists in one space) multiply the boost by the number of stacked carts
- Boosters on both sides of a track going the same direction boost by roughly an additional ⅓
- Boosters in a series (one after another) boost by roughly an additional 5/9
- A cart will slow down if it approaches a neighbor cart head-on (e.g., not off of a slope or curve), and a proper boost will not be accomplished. The sides must come into contact through diagonal or vertical motion. Keep this in mind when designing two-way systems. The following diagrams illustrate this concept:

### 
 

### 
 

## Launcher types
Launchers are boosters that are activated with a button.

### New-style door launchers
This launcher is an improvement over the classic door launchers. A door properly placed above a block will prevent a minecart from passing through the block only when it's opened.



### Classic door launchers
This launcher uses a ladder in order to hold a minecart in place. Opening a door will release the minecart onto the track below it.

The minecart sits on a door, which is wired to a button or other mechanism using redstone. When the door is momentarily opened, the minecart drops onto a section of slanted track next to the minecart to be boosted.



A ladder piece is necessary to keep the minecart in place.



NOTE: In laggy multiplayer conditions, the booster cart will occasionally have trouble resetting itself properly. To help the booster cart get back up the hill with sufficient speed to get into its correct position on top of the door, an additional uphill auto-reset booster (see above) can be placed on the far side of the mechanism from the main track.

### Powered Rail launchers
This launcher is similar in function to a door launcher, but uses a Powered Rail to launch the booster cart and is much simpler in design. The player presses a button to power the rail and launch the booster cart, which then turns around and stops on the unpowered rail ready to be used again.

 

## Booster types
### Two-way corner manual-reset
This example demonstrates a two-way manual reset booster. The booster only requires a manual reset should you want to go the same direction twice. It is an excellent solution for those who prefer to have minimal alterations made to their terrain.



### One-way up-downhill manual-reset
This allows you to boost minecarts up or down a hill. Note that you must already be moving to reach the booster while travelling uphill.



### 
These are two possible configurations for one-way resetting boosters based on the south-west rule. The one on the left is a south→north booster, and the one on the right is a west→east booster. 



### 
This booster uses a raised auto-reset loop, so that it can be built in any direction. The booster minecart will go through the loop and fall onto the inclined track, going back to the starting position.





### 
This booster is just like the previous booster but only requires three tracks for the auto-reset loop. It takes a couple more steps. 



First build the tracks like this. In order to bend the third track around so that it resets, you need to add a block above the track like this.



Then place a track on top of the block. That will bend the third track into its proper placement. 



The last step is to remove the block.



### 
This booster uses a simple loop that throws the cart back onto the track, since the track is angled it hops onto the track and continues in a straight line, ignoring the S-W rule that applies when running into perpendicular tracks.



### Two-way auto-reset
Here is an example of a two-way resetting booster that is direction-independent (its cardinal direction doesn't matter):



Video demonstration

### Two-way corner auto-reset
An example of a  two-way booster for corners that auto-resets.



### Two-way auto-reset compact design
Here is an example of a two-way resetting booster that is direction-independent. This design is a little more compact. 



### Two-way auto-reset efficient design
Here is yet another two-way gravity powered auto-reseting booster. The lower cart pictured (the booster) sits in the center of a symmetrical section of track, and will always come to rest at that point. This may be the most efficient when it comes to amount of iron that is needed to make it. This design was made by alfadark on Reddit.

It should be noted that this design requires time to settle after each use and it may only propel users a few blocks. This design should not be used on heavily used tracks or on multi-player.



### Uphill auto-reset booster
This is a simple, compact and effective way of going uphill.  It won't boost you downhill, but gravity will handle things for you there.



1. This is your main track. You want to build a booster here.
2. Dig a 2×2×1 hole containing your main track.
3. Rebuild the two pieces your main track inside the hole (like a "V" letter). Then, start building a booster track.
4. At the top end of the booster track...
5. ...remove the last track piece...
6. ...and put a block there. This way, the booster minecart will hit that block and go back down to the starting position.
7. Your finished track.

An other version, only to extend the distance your minecart is able to cover.



### Booster in turns
There are two ways to make your booster keep working even if you need to make a turn. Follow the picture below to make one, but there are two restrictions on its usage:

- It cannot make more than a single turn. If you need to circle something while going up, you will need to use many separate boosters.
- After the turn, it must boost you for at least 6 more blocks, else it won't have speed to reset.



The second way to still have a booster work after a turn:
unlike the one above this one will work for any number of turns.
It is 5×5×4 and uses only 16 pieces of track.



### Auto-Start booster
Getting a minecart going initially can be tricky and requires good timing to place the cart, push off, and jump in. This setup simplifies the process by giving the cart a boost from a dead stop. This is a useful configuration to have at stations in a minecart network.

The outer loop cart, once started, is repeatedly boosted by the inner cart, which simply travels back and forth along its short track. The outer loop cart in turn can be used to boost a stationary cart placed next to the corners. Just wait for the outer loop cart to pass, place your cart, get in, and when the outer loop cart loops around again your cart will get a boost.

Unfortunately, the loop cart can bug out after a while, which while easily fixed, is still annoying.



The following design of an auto-start holding station attempts to rectify the infinite loop bug encountered in the above design.  Place carts 1 and 3 in their initial positions as shown, then drop cart 2 into its initial position from above to start the perpetual motion.

Cart 1 is a simple uphill booster used to force cart 2 back to its initial position.  Cart 2 actually drives the rider's cart (cart 3).  Point 4 is a position for a switch that will allow cart 3 to exit the loop.  The rider can then enter at any point after point 4.  Point 5 shows the return track for Cart 3.  The rider can exit at any time before point 5 or after point 4 safely (cart 3 will likely go around its full track again, so this design is inefficient for long tracks).

After cart 3 has left the holding station, cart 2 will always move just far enough from its initial position to reach cart 1, boosting it uphill.  Both return to their initial positions, stopping each iteration, allowing for perpetual motion without infinite momentum.



### Double Booster
This is a way that you can put two carts into one, which is believed to more than double the distance you can get out of your booster.

In order to make the double booster, you need to put a block, then a piece of track (may require two tracks in order to align the cart correctly) above the cart to be doubled and place a cart on that track.  



Next remove the block. This will drop the first cart into the second, merging them. At least, until they fall off the track. 



You can also ride "them" and they'll move nearly forever if there is no dead end. It also moves slower off track and can move through water.



Here is another way to create the double booster. The carts will collide and merge partially, creating the same effect as the double booster explained above. This version, however, can be used automatically since there is no need dig any blocks. Using this method you can also merge more that two carts, but the results will usually be more or less unstable.

### Spin Booster
This is a simple principle, it involves 4 minecart tracks, and 2 minecarts. You put the 4 tracks in a circle, and then place 1 minecart on a track in that circle, and place the other one opposite. Then, put your track for transport next to it. When a minecart is pushed into it, it boosts it. PLEASE NOTE the minecarts sometimes have to be replaced.

Another method of Spin Boosting is to use 8 minecart tracks and 5 minecarts. This is easier to determine the direction the booster will take effect.

This method should be avoided in multiplayer as it creates high amounts of lag.

Spin boosters still work in modern versions of the game, but generally require more carts and don't provide as large of a boost.



### Triple Booster
Possibly the simplest booster (recommended for long, level tracks) only requires a single track and three minecarts. Line the carts up on the track and push the rear one into the other two repeatedly, and at least two of the carts will lock together and boost each other continuously until they reach their destination. This is a bug that seems to have to do with the carts hitting each other, so this may take a few attempts. As such, it's recommended to make the rear cart a Powered Minecart and start it with a few coal, then jump in the front cart so you don't get left behind. The powered cart will knock into the other two until the bug kicks in.

### C-Booster
The C-Booster, also known as the collision booster, is a relatively small booster that produces max speed and momentum instantly, allowing fast uphill travel and instant speed. To make one, dig two trenches in the ground, both one block deep, two blocks wide, and 1 block in length. These trenches/lines must be parallel. Place minecart tracks inside them, then link them together in the area in the center by placing a line of track. Cover the trenches with any block, and place two minecarts per line of track. You should now have four closely compacted minecarts. If another minecart directly approaches it and bumps into a minecart inside the C-Booster, it will instantly accelerate in the opposite direction at max speed and max momentum.


The direction of the boost may change randomly.

Credit goes to Moosety on the Minecraft forums for the discovery of this booster.

### Reverse Double-V Booster
This booster is a booster where you get blasted out the same way you come in very powerfully. It is auto-resetting.





### Multiplayer Tips
Certain types of boosters should be avoided in multiplayer, as they can cause lag or may work unreliably.

- Don't use always-moving boosters, such as spin boosters. Use launchers instead, as these cause less lag due to not having to constantly update the minecarts.
- Check the rules: Some servers may disallow boosters and launchers entirely, and/or have mods installed to replace this functionality.

