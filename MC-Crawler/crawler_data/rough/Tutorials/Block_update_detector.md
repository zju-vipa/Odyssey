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















### Stuck-Piston Based
The following designs works because pistons can't be pushed by other pistons while extended. Also, when a piston retracts, it doesn't notify any other pistons that were trying to push it. The piston with the block attached to it is sticky and acts as the sensor. This design has the advantage of a low profile, and also that the quirk it exploits is less "buggy" and less likely to be fixed in the future.

























A perpendicular "stuck piston" BUD switch. The piston with the block attached to it is sticky.
A perpendicular "stuck piston" BUD switch. The piston with the block attached to it is sticky.
An in-line "stuck piston" BUD switch. Left piston is sticky.)
The latter design above can also be extended to an array in a variety of ways, including a one-wide design.

A very compact "in-line" BUD array. Every piston is a sensor except the one next to the obsidian. None of the pistons are sticky.
A one-wide BUD array. Every piston is a sensor except the one next to the obsidian. None of the pistons are sticky.

The stuck-piston principle can also be used to hide a BUD completely underground, as shown by this video:






























Using an observer to block a sticky piston.

The design on the right uses an observer which self updates when arriving in front of the sticky piston to stick it. During retraction, when the sticky piston resets, the observer in front of it is still a block of moving piston, so the sticky piston doesn't schedule a block event; then the moving piston becomes an observer with no block update, and the sticky piston enters BUD state.






















Slime Block BUD

Sticky pistons in slime block BUDs are often stuck by a block behind a slime (or honey) block next to its head. When the design on the right retracts, the slime block updates the sticky piston after the redstone block arrives, but the diamond block is still moving so the sticky piston doesn't plan to extend; the diamond block cannot update the sticky piston on arrival. Like the compact BUD, it can reset itself unless it is updated when extending. 

### Dropper Based
Here is a video about this.[needs testing]




### Other QC components based
Here are examples based on update QC activation of a dispenser and half a door.




































Dispenser Based

The dispenser contains a water bucket, lava bucket or powder snow bucket.






























Door Based

### Redstone Torch Based

As of 14w25a (with the fix of MC-56541), a burned-out redstone torch can be used as a reliable BUD. Once burned-out, a redstone torch will reset upon an update from any adjacent block. This is the smallest and simplest BUD, only requiring a single torch and redstone dust (plus two repeaters for a solid output signal.) 
A burned torch BUD with a solid output.
A redstone torch on the side of a block and put redstone dust make the redstone signal loops with itself is also a BUD. The place around the redstone torch (include upside and downside) is the detecting place, but not the redstone dust. The redstone torch will blink for 16 ticks, and finally burn down. It has a 56 ticks cool down. It can't detect sleeping in a bed.














An example of a redstone torch based BUD.
An example of a redstone torch based BUD.
This works in the Bedrock Edition of Minecraft, as shown in the video below.




### Redirection based
A simple redirection bud
When redstone dust redirects, it does not send out block updates, so a piston can have its power removed by redirecting redstone dust away from it to remove power. When the piston receives a block update, it will update its state accordingly and the redirection bud will reset.


### Powered rail based

















































Powered Rail BUD
A powered rail or detector rail will be activated if one among the first to eighth of connected rails of the same type on the same direction should be activated, but cannot be properly updated when being activated or deactivated if part of rails before the power source are not activated or deactivated along with it. This can be used to create a BUD. Powered rails can be replaced by detector rails as a whole.


Unless integrated with minecarts and detector rails, the powered rail BUD only outputs block updates, but it causes little delay and burden on the server, and are often used to transfer block updates.

### Fluid based
Fluids calculate flow directions when receiving block updates, and can be detected by observers if flowing toward new directions.

### Components on Trapdoors based
Powered rails, detector rails,rails and activator rails attached to trapdoors break when receiving NC updates after the trapdoor opens. This type of BUD can reset itself if used for a rail duper as rails reappear after breaking.

### Tripwire Hook on Doors based












Using tripwire hooks to keep a door open.
As shown on the right, build a tripwire circuit missing one tripwire hook, trigger the tripwire, and place the missing hook on any half of a door. The tripwire hook breaks when activating the door but the door remains open. 


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

