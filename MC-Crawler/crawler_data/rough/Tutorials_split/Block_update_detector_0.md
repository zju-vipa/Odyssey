# Tutorials/Block update detector
The Block Update Detector, or BUD switch, is a redstone mechanism that uses quirks in the game in order to detect NC updates from nearby blocks. There are many different designs that are all based on the same general idea: a redstone circuit is put in a state where it should be following a mechanic, but the game has not updated the block to follow this rule. This unupdated block then functions as the "sensor". When an adjacent block changes state in some way, the game updates all adjacent blocks—including the sensor block—and powers them up. The circuit then performs some other action and, with most designs, goes back into standby.

As comparators accept NC updates, a comparator made into a BUD can serve as a CUD, and a CUD can serve as a BUD.

## Contents
- 1 What it detects
- 2 Types of BUD Switches
	- 2.1 In-Game
	- 2.2 Piston Based
	- 2.3 Stuck-Piston Based
	- 2.4 Dropper Based
	- 2.5 Other QC components based
	- 2.6 Redstone Torch Based
	- 2.7 Redirection based
	- 2.8 Powered rail based
	- 2.9 Fluid based
	- 2.10 Components on Trapdoors based
	- 2.11 Tripwire Hook on Doors based
- 3 Variations
	- 3.1 BUD in Bedrock Edition
	- 3.2 T-BUD
		- 3.2.1 Compound slime block T-BUD
- 4 History
- 5 References

## What it detects
Main article: Block update
The BUD switch detects the following events when they happen next to the sensor block:

- Placement of blocks
- Destruction of blocks
- Waterorlavalevel changes
- Freezing of water or melting oficeandfrosted ice
- Agravity-affected block(e.g. asandblock) landing after falling
- Movement ofblocksbypistons, includingpiston heads, except creation ofmoving pistons(moved blocks being replaced can be detected), sticky piston heads retracting from a movable block (even if the sticky piston cannot pull the block because a block stuck to it is blocked) and blocksself updatingupon arrival
- Endermenpicking up and putting down blocks
- Saplingsgrowing intotrees
- Mushroomsgrowing intohuge mushrooms
- Growth and spread of plants, including:cacti,flowers,grass,mushrooms,melons,pumpkins, andsugar canes,cocoabeans,bamboo,crops(e.g.melon stems),nether wart, andvines)
- Leafgrowth and decay
- Growth and death ofgrass blocks
- Dirtbecomingfarmland, farmland becoming hydrated, farmland reverting to dirt
- Fireigniting or burning out
- Afurnacebeginning or ceasing to smelt
- Aredstone oreblock beginning or ceasing to glow
- Changes inredstonestate or power level, and activation of redstone devices
- Changing the delay of arepeater
- Railschanging orientation
- Powered railsandactivator railsgetting powered or depowered
- TNTigniting and becoming an entity
- Silverfishentering a block
- Cakebeing eaten
- The opening or closing of achestortrapped chest
- The activation of atripwire(even if not attached to atripwire hook).
- Vines,crops(e.g.melon stems),nether wart, orcocoa beansgrowing
- The upper block of a 2-block tall plant (e.g.tall grass,rose bush) replacing/being replaced by an air block when that plant is placed or broken
- Adragon eggreplacing an air block when it teleports to a location after a player tries to break it
- Agrass blockchanging todirtdue tosheep"eating" the grass
- Achorus flowergrowing into achorus plant
- Adry spongeabsorbing water
- Switching acomparatorbetween comparison and subtraction modes
- Playing anote block
- Changing the number of layers in asnow layerblock
- Leafdistance from a log changing
- Scaffoldingdistance changing
- Composterfill level changing

Block and block state changes that some BUDs may not be able to detect, include:

- Opening or closing anender chest
- Inserting or removing amusic discin/from ajukebox
- Placing or removing of abottle/potionin/from abrewing stand
- Changing the contents of achest,trapped chest,shulker box,ender chest,dispenser,dropper,brewing stand, orfurnace.

## Types of BUD Switches
Below is a comprehensive video from SethBling (outdated), which showcases a variety of compact block update detectors, mostly making use of the redstone block.




### In-Game

The BUD switch now has a compact block form in-game and it was added in 1.11 snapshot 16w39a called the 'Observer'. The observer does not detect block updates, instead it detects block state changes.

### Piston Based
Many BUD switch designs exploit a property of pistons called quasi-connectivity. A piston can receive power through a space one block above itself. In this case, the power source is either above and to the side of the piston, or two blocks above it. However, when powered in this way, the piston does not immediately notice changes in the state of the power source. When some other block update happens next to the piston, it will "wake up" and react to the change. By forming a feedback loop, where the state of the piston controls the state of its power source, it becomes the sensor of a simple BUD switch:


In this design, the piston will only extend in response to an adjacent block update, but after extending it will immediately retract because the arm of the piston notices the repeater next to it turning off. This is how a piston BUD resets itself: by having the power run next to the extended piston arm, with a delay.

Note: If the block diagonally adjacent to the sticky piston becomes horizontally adjacent, the circuit will constantly pulse instead. 

This design can be extended with multiple sensor blocks. All of the pistons in this design are sensors.

A piston-based "BUD array", with multiple sensor blocks. All the pistons are sticky.

A 1-wide tileable design using redstone blocks:




























Alternative method: if players take a sticky piston facing parallel to the ground, then place a Block of Redstone on its face, and connect the block of redstone out to the side of the piston through a repeater that goes into a block diagonally adjacent to the piston, it works a fully functional BUD. Then, if you set a delay of any number of ticks other than the default 1-tick delay on the repeater, it turns into a T-BUD. This process can also be reversed by setting the repeater back to its default 1-tick setting. (It only works since release of Redstone Blocks, though players could theoretically use a normal block and a redstone torch to mimic its effects.)

An extremely compact one-time design that is easily hidden and therefore ideal for traps is as follows: Place a piston, a sticky piston is most useful, parallel to the ground. Place a block one block to any side except the piston head and one block above the
piston. On the side of the block facing the piston, place a redstone torch. Then place a lever on any other side of the block and switch it on. The redstone torch will go out but the piston will remain extended. You can then break everything except for the piston, but make sure to break the lever after you break the torch. A block update will then cause the piston to retract, possibly pulling the floor out from under the victim. Remember, though, that after the detector is tripped, it has to be rebuilt to be used again.


The design looks something like this:
























Or, for it being smaller:
The player can make a 2×1 (3×1 when extended) BUD by having a 2 sticky pistons (stacked) both facing any direction except up and down, then on both of those sticky pistons add Redstone Blocks. Whenever a block is updated, (destroyed, placed etc.) it will switch the bottom piston outwards. Good for traps, as the BUD may need to be compact. The only con to this is that it has to be reset.

Another extremely compact design involves using 1 sticky piston facing up with a slime block and redstone block stacked on top of it. This design is 1×3 (1×4 when extended) and allows the piston to be updated from 5 of its sides. It does not need to be reset after triggering, but players do need to make sure that the slime block isn't grabbing a wall in order to activate in the first place.















