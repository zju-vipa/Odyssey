# Tutorials/Comparator update detector
A comparator update detector or CUD switch is a redstone mechanism that exploits a feature in the game in order to detect comparator updates. Comparator updates are updates that only update comparators, for example, interacting with a container. Block update detectors cannot detect comparator updates, but CUDs can detect block updates.

There are many different designs, but they are all based on the same general idea: a comparator is turned on while it should be turned off, or the other way around. To get a comparator in such a state, the player have to make sure that it doesn't realize that it should change. This can be done in several ways.

When the comparator gets an update, it will realize that it should change state. This update can be a block update, or a comparator update. CUDs can detect comparator updates next to the comparator, but also 1 block in between, provided that the block in between is a solid block.

## Contents
- 1 What it detects
- 2 Types of CUD Switches
	- 2.1 Overview of most designs
	- 2.2 Chest based
		- 2.2.1 Using Ocelot
	- 2.3 Cauldron based
	- 2.4 Redirecting based
	- 2.5 Item frame based
- 3 Variations
	- 3.1 T-CUD
- 4 Why and how it works
- 5 History
- 6 References

## What it detects
The CUD switch detects everything a BUD detects, however the CUD can detect updates from the following blocks 2 blocks away from the comparator horizontally (but only if a solid block exists between the comparator and the target block). This means that the player can have a CUD behind a wall that detects the following updates in front of the wall:

| Block                   | Placement | Removal | Interactions |
|-------------------------|-----------|---------|--------------|
| Chest                   | Yes       | Yes     | Yes          |
| Trapped Chest           | Yes       | Yes     | Yes          |
| Barrel                  | Yes       | Yes     | Yes          |
| Dispenser               | Yes       | Yes     | Yes          |
| Dropper                 | Yes       | Yes     | Yes          |
| Furnace                 | Yes       | Yes     | Yes          |
| Blast Furnace           | Yes       | Yes     | Yes          |
| Smoker                  | Yes       | Yes     | Yes          |
| Brewing Stand           | Yes       | No      | Yes          |
| Jukebox                 | Yes       | No      | Yes          |
| Beacon                  | No        | No      | Yes          |
| Command Block           | Yes       | No      | Yes          |
| Chain Command Block     | Yes       | No      | Yes          |
| Repeating Command Block | Yes       | No      | Yes          |
| Sign                    | Yes       | No      | Yes          |
| Composter               | Yes       | Yes     | Yes          |
| Detector Rail           | Yes       | No      | Yes          |

The CUD detects many things which are undetectable by any other method. some examples of this include closing the edit mode in a sign, an item smelting in a furnace, blast furnace or smoker, a potion being brewed in a brewing stand, a slot being clicked in any of the containers in the table above, or pressing done in a command block. It also essentially turns a detector rail into a pressure plate, and the CUD will update with any entity landing on the Detector rail, including arrows.

## Types of CUD Switches
The CUD can be only based on a comparator because only comparators can detect comparator updates. Each time players does one of the actions listed above, a comparator update is being sent 2 blocks away in all the 4 directions.  

### Overview of most designs
This video by mooing_cowmilk provides an overview of most CUD designs, and also includes an explanation of them.




### Chest based
This method uses the mechanics of a chest. When a chest is locked, the comparator doesn't realize that it shouldn't be turned on anymore. When the player updated the comparator, it realizes, and resets the system.

#### Using Ocelot



It's also possible to block the chest with an ocelot. When ocelot sits on a chest, the player can't open it. The player can move them using pistons, minecarts or water. Using minecarts, players can make a silent CUD, besides the meow-sound of the ocelot or cat.

### Cauldron based
A cauldron based CUD.
This method uses a filled cauldron that is being pushed by a piston, the comparator doesn't notice that the cauldron has been pushed down and stays powered until it gets an update. Note that the cauldron should contain water.


### Redirecting based
A redirecting based CUD. The redstone is redirected by a detector rail. Note that the lever should always be turned on.
This method is often used in BUD's. The player can turn any repeater-based BUD into a CUD by replacing the repeater with a comparator. They can redirect redstone with a detector rail, redstone block or a solid block, blocking 2 redstone diagonal to each other. Again, the comparator doesn't realize that the redstone isn't pointing the right direction anymore and it will stay turned on until it receives an update.


### Item frame based
An Item-frame based CUD.
Another item-frame based CUD.
Comparators can take a redstone output from an item frame, but only if the item frame's position isn't occupied by a block. Many blocks will break the item frame, if they are in the same position, but some blocks don't. Examples are water, fence gates, skulls and flowers.


## Variations
Other devices can be built using the same underlying principle as the CUD switch. CUDs can be made stackable and even tile-able. They can be turned into a toggle-CUD. CUDs can be made pistonless using ocelots.

### T-CUD



A T-CUD toggles between 2 states. The first update will turn the comparator off, and the second update will turn the comparator on again.

## Why and how it works



