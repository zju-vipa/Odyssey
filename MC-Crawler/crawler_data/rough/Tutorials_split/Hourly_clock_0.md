# Tutorials/Hourly clock
This page contains instructions for a clock that signals you every Minecraft hour, or every 50 seconds of real-time.

## Contents
- 1 Description
- 2 Supplies
- 3 Construction
	- 3.1 Basic circuit
	- 3.2 75-clock
	- 3.3 150-clock
- 4 Configuration
	- 4.1 75-clock configuration
	- 4.2 Using a Hopper system
- 5 Chimes
- 6 Cool Ideas
	- 6.1 Super Complex Clock
	- 6.2 Multibase Clock
	- 6.3 Clock Tower with 7-segment display
	- 6.4 Timed Stations
- 7 See also

## Description
An hourly clock is a redstone intensive device that makes some indication of when an in-game hour has passed. This clock is just an extension of the standard 4 clock, except that this is a 75- or 150-clock. Note that one in-game hour is equal to 50 seconds of real-time. Also, this program is best done with inventory editing, due to the amount of resources it would take to make all the components.

## Supplies
The basic supplies needed are:

- 75-150redstone repeater
- Several stacks ofredstone dust
- 1-2redstone torch
- a fewnote blocks
- 2-3 blocks of your choice (not glass)
- 75-100pistons(optional)

## Construction
### Basic circuit
This clock is your standard clock circuit, except it has a delay of 75-150 ticks, instead of 4-5. To start the circuit, use one of your redstone torches and a block of your choice to set up an inverter. Once that is done set a repeater either in range of the inverter's torch or with a wire running from the inverter to it. Now you have some options.

### 75-clock
A 75-clock has half the repeaters of a full circuit, and one more inverter for the signal telling you that an hour has passed. After the basic circuit is built, add 74 more repeaters to the chain and connect then end of the chain back to the inverter. then, before the inverter, have a wire branch off and lead to another inverter, which in turn leads to a note block, or a sequence of note blocks. The second inverter is needed for this reason: As the clock only has 75 repeaters instead of 150, the note blocks need to go off only once every 2 cycles. And, a clock circuit has 2 sequences. The first is a power up, in which the repeaters all turn on; the second is a power down, where the repeaters all turn off. This cycle repeats endlessly unless interrupted by a broken chain or a save and quit. Sleeping in a bed can cause clocks to get off-time. A reset system that loses very little time can be made using pistons.

### 150-clock
A 150-clock is what this writer and builder considers a full circuit, meaning it uses the max amount of repeaters needed. Set up the basic circuit from 4.1. Then put on a chain of 149 more repeaters. Then at the end of the circuit, make a wire branch off to one side, and attach 2 note blocks or sequences of note blocks. But, put an inverter before one of the note block sequences. As explained in 4.2, a clock circuit has 2 sequences, running in an endless cycle. So the inverter in front of one note block sequence makes it so that every 150 repeater run, on or off, powers a note block sequence. This method requires more materials and time, but is more rewarding when finished and more fun for showing off to friends or in videos.

