# Tutorials/Flying machines
Flying machines are mechanisms that use slime blocks, honey blocks, redstone blocks, observers, and/or pistons to move a structure of blocks in one or more directions, moving freely through air or water without support. They can also be designed to carry along a player and/or other entities, which may be riding in a minecart or towed along by honey blocks. They can also be crouching on honey blocks to stick onto them.

The mechanics of such machines vary slightly between the Java and Bedrock Editions of Minecraft; This guide covers Java Edition and Bedrock Edition in separate sections.



## Contents
- 1 General Principles
- 2 Java Edition Flying Machines
	- 2.1 Engines
		- 2.1.1 Schematics
	- 2.2 Extensions
		- 2.2.1 One-way extension
		- 2.2.2 Two-way extensions
	- 2.3 Driveable flying machines
		- 2.3.1 Schematics
		- 2.3.2 Driveable flying machine A, 2-way
		- 2.3.3 Driveable flying machine B, 2-way
		- 2.3.4 Driveable flying machine C, 2/4-way
		- 2.3.5 Driveable flying machine D, 4-way
		- 2.3.6 Driveable flying machine E, 4-way, compact
	- 2.4 More complex engines
- 3 Bedrock engine designs
	- 3.1 Simple engine 1
	- 3.2 Multi-directional engines
	- 3.3 Extensions
- 4 Video
- 5 Gallery
	- 5.1 Piston machines
- 6 See also

## General Principles
The key blocks for flying machines, more or less in order of appearance:

- Pistons are capable of pushing or (sticky pistons) pulling up to 12 blocks. These can simply be arranged in a line in front of the piston, but slime and honey blocks allow carrying along blocks placed to all sides of that line.
- Various immovable blocks (notably obsidian and tile entities such as furnaces‌[JE  only]) provide limits and frameworks.
- Redstone Blocks: The key point here is while mostotherredstone power sources are partial blocks that get broken by pistons, this onecanbe pushed or pulled by pistons, so a machine can carry its own power source.
- Observers are sensors for both the environment and adjacent parts of the same machine, which can also turn a change in one part of the machines into power elsewhere.
- Slime and Honey blocks are similar: both can "stick to" other blocks at their sides, carrying those along with them when pushed or pulled by a piston. Theirdifferencesare as follows:
	- They do not stick to each other.
	- Slime blocks are solid blocks, which can take and transmit a redstone signal, while honey blocks are transparent blocks which cannot.
	- Slime blocks bounce entities away from them, while honey blocks drag entities along with them (and prevent players or mobs atop them from jumping very high).

There are two main components of slime block flying machines:

The engine provides the basic control and motion, based on the idea that a slime block pushed by a piston will move adjacent movable blocks, including other slime blocks, when pushed or pulled. However, each piston is limited to moving 12 blocks total. 

Extensions uses additional pistons to let tow along additional segments of a larger machine. Honey blocks can also be used to bypass the piston push limit by using adjacent slime block and honey block flying machines to divide the number of blocks in a structure among pistons. In Bedrock Edition, extensions are divided into leading and trailing types. 

Note that the schematics in this section use the usual building scheme where layer 1 (or occasionally layer 0) is the bottom layer. 



## Java Edition Flying Machines
### Engines
A simple flying engine. The central piston is the only sticky piston used in this configuration.
Engines are mechanical parts of slime-block based flying machines used to move them.

In all cases, a major issue is control, especially how to start and stop the machine. There are several options here:

- Asemi-automaticengine needs player's intervention to move it, generally by updating a piston -- e.g., usingflint and steelon it, or rapidly placingtripwireagainst it.
- A fully automatic engine can be started by a single update, say by breaking a block (perhaps a button or a sign). A switch can be used, but is likely to be left behind once the machine starts to move. Stopping them can be more difficult -- many engines will stop only when they run into an obstacle. If the obstacle is wrongly shaped, it may break the machine, thus a prepared docking station may be needed.
- A few "drivable" machines take advantage of the point that a note block produces an update when played, so a player riding the machine can trigger note blocks to start and/or stop the machine.
- Engines can also differ in available directions and speed. The simplest can only move in a single direction, but two-way and even diagonal motion are possible. Again, dedicated docking stations are sometimes needed.



#### Schematics
Schematic Gallery: Engines (Java Edition) View at: Tutorials/Flying machines/Java Engine Gallery [edit]

A two-way engine can be made with as few as 6 blocks – 2 Observers, 2 Slime Blocks, and 2 Sticky Pistons. Two-way engines A and B (see gallery above) show two different ways to do this.
In both cases, the direction of flight depends on which observer is updated first. Note that in the diagram shown, each observer directly powers a slime block. The dock shown is placed so that the trapdoor will cover the face of the incoming machine's near observer, which lets it send the machine back the way it came.

Adding honey blocks allows a player to be carried with the machine in relative safety. The rideable engine shown adds two honey blocks, and a player can stand on each of them. It can be made with 14 blocks – 8 slimeblocks, 2 honey blocks, 2 sticky pistons and 2 observers. Getting on and off is another problem....

Turbo engine A. Breaking the sign starts the engine.
Turbo Engine A (see gallery) is a high-speed single-direction engine. It fits into 2×2×6 dimensions and uses 14 blocks. Since zero ticking pistons is not possible on Bedrock Edition, this kind of flying machine will still be the same speed on Bedrock Edition as normal flyers, however, several 2.5 meters per second flying machines have been created for specific use on Bedrock Edition.

An engine can also move diagonally by moving alternately along 2 axes. The Diagonal Engine shown is best built out from level 3 (the upper slime--and-piston layer). It moves along its slime-block diagonal, but is guided by immovable (e.g., obsidian) barriers on level 3, so it can follow a straight or curved "rail", in whichever direction(s) it can move until it reaches a corner to block it. It is started by activating either of the observers on top (placing a block, flint-and-steel), and will move away from that corner (that is, it is also a two-way flyer).
Credits: design from "samnrad" ("smart diagonal flying machine and curved flying machines" YouTube

This video demonstrates two-way engine A above, with long slime-block arms for harvesting, which shuttles between two prepared docks. It can be triggered by placing a block atop the pistons, or by switches at the stations. Note that the harvested crops will be launched at some speed, so this design may be better for an enclosed farm.






