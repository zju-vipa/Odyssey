###  Dragon Head
Main article: Dragon Head
The dragon head opens and closes its mouth repeatedly like the ender dragon when placed and powered by redstone.

###  Dropper
Main article: Dropper
A dropper is used to eject items or push them into containers (including other droppers).

** Placement **
A dropper can be placed so that its output faces in any direction.
** Activation **
SeeQuasi-Connectivityabove.
** Effect **
When activated, a dropper ejects one item. If multiple slots are occupied by items, a random occupied slot is chosen for ejection.
If the dropper is facing a container, the ejected item is transferred into the container. Otherwise, the item is ejected in the direction the dropper is facing, as if the player had used the Dropcontrol.
** Considerations **
A dropper is an opaque block, so powering it directly can cause adjacent mechanism components (including other droppers) to activate as well.
###  Fence gate
Main article: Fence Gate
A fence gate is used to control or prevent the movement of mobs, items, boats, and other entities.

** Placement **
A fence gate can be placed on thetopof most blocks. Once placed, the block beneath it may be removed without popping the fence gate.
** Effect **
While activated, a fence gate re-positions its two gates to either side, allowing movement through it. When activated, any entities on the fence gate falls down.
A fence gate doesn't actually move (the way a piston arm or a pushed block moves), it simply disappears from one state and re-appears in another, so it does not push entities as it opens.
Unlike a door or trapdoor, while active, a fence gate is completely non-solid (lacks a collision mask) to all entities.
###  Hopper
Main article: Hopper
A hopper is used to move items to and from containers (including other hoppers).

** Placement **
A hopper can be placed so that its output faces in any direction except up.
** Effect **
Whilenotactivated, a hopper pulls items from a container above it (or item entities in the space above it) into its own slots and pushes items from its own slots into a container it is facing. Both types of transfers occur every 4 redstone ticks (0.4 seconds), and pushes are processed before pulls. A hopper always pulls items into the leftmost available slot, and pushes items from leftmost slots before rightmost slots (it does not start pushing items from the second slot before the first is empty, from the third slot before the second is empty, etc.).
While activated, a hopper does not pull items from above or push them out, but may receive items from other mechanism components such as droppers, and may have its items removed by another hopper beneath it.
###  Note block
Main article: Note Block
A note block is used to produce a player-chosen sound.

** Placement **
After being placed, a note block's pitch can be adjusted over a two-octave range by right-clicking the note block, and its timbre can be adjusted by placing different blocks beneath it.
** Effect **
When activated, a note block produces a sound and send out block updates to all adjacent blocks. A note block must haveairabove it to activate.
** Considerations **
A note block is an opaque block, so powering it directly can cause adjacent mechanism components (including other note blocks) to activate as well.
###  Piston
Main article: Piston
A piston is used to move blocks or entities. A piston may be of two types: a regular piston only pushes blocks, while a sticky piston pushes and pulls blocks.

** Placement **
A piston has a stone base and a wooden head, and can be placed so the head faces in any direction (its front).
** Activation **
See Quasi-Connectivity above.

** Effect **
When activated, a piston pushes the block in front of its arm, and up to 11 more blocks in front of that (up to 12 blocks total). When deactivated, a regular piston pulls its arm back (leaving anairblock in front of the piston), while a sticky piston pulls back both its arm and one block (leaving an air block on the other side of the pulled block).
A moving piston or block can also push anentitysuch as a mob or item.
Some blocks (bedrock, obsidian, end portal frame, etc.) cannot be moved by a piston. Some blocks (flowers, leaves, torches, etc.) is destroyed, but may drop items (as if destroyed by the player). For full details of how pistons interact with other blocks, seePushing Blocks.
Slime blocksstick to blocks and make them move when adjacent blocks are moved. The 12 block limit still holds.
** Considerations **
When a sticky piston is activated by a pulseshorter than 1.5 ticks, itpushesthe block in front of it, butfails to pull backthe pushed block on the end of the pulse. If that sticky piston is activated again by any pulse, itcan still pull backthe block. Thus, a sticky piston running on fast pulses (for example, 1-tick pulses) pushes and pulls a block everyotherpulse.
A piston is a transparent block, so powering it directly does not cause adjacent mechanism components (including other pistons) to activate (for exceptions seeQuasi-Connectivityabove).
###  Powered rail
Main article: Powered Rail
A powered rail is used to propel a minecart.

** Placement **
A powered rail can be attached to thetopof anyopaqueblock, or to thetopof an upside-downslabor upside-downstairs. If the attachment block is removed, the powered rail drops as an item.
When placed, a powered rail configures itself to line up with adjacent rails, powered rails, and detector rails, as well as such adjacent rails one block up. If there are two such adjacent rails on non-opposite sides, or three or more such adjacent rails, a powered rail lines up in the east-west direction. If there are no such adjacent rails, a powered rail lines up in the north-south direction. If a rail it would line up with is one block up, a powered rail slants upward toward it (with multiple options to slant upward to, a powered rail prefers, in order: west, east, south, and north). Other configurations can be created by placing and removing various rail.
** Activation **
In addition to the methods above, a powered rail can also be activated by other adjacent activated powered rails. A powered rail can transmit activation up to 9 rails (the first originally-powered powered rail, and up to eight additional activated rails). Activation transmitted in this way cannot power any redstone components except powered rails, but the power change states can be detected by observers.
** Effect **
While activated, a powered rail boosts the speed of a minecart passing over it, or starts a minecart moving away from an adjacent solid block it is in contact with.
While not activated, it acts as a brake, reducing the speed or even stopping a minecart passing over it.
