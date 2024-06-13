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

 

