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

## Configuration
(Note: you can also use a counter instead of repeaters for longer time.)
As there are 3 repeaters required to time a second, and 50 seconds in a Minecraft hour, there need to be repeaters configured in some way to make 500 ticks delay (1 tick = 0.1 seconds).

### 75-clock configuration
To set this clock to the right delay, set 50 of the repeaters to 4 ticks, and 25 to 2 ticks (or 62 repeaters to 4 ticks and one to 2 ticks.) This creates 25 seconds delay and, with the inverter setup on the chime, will sound the signal once every 50 seconds.



### Using a Hopper system
Using a hopper clock with 128 items will result in an output being sent out every 1 in game hour. It takes approximately 50.02 seconds for 128 items to travel from one hopper into another. Using this method results in a more compacted design for an hourly clock configuration can be done in any way. The video below shows how using droppers and comparators to display the hour. 




## Chimes
The chime is the part of the clock that tells you when an hour has passed. It is made of note blocks, and can be anything from a single note to a complex melody. A good idea is to build your chime under the floor of your base so that it is heard from inside home.

## Cool Ideas
These are just some other cool ideas for an hourly clock.

### Super Complex Clock
Make a giant complex housing 12 hourly clocks. Have each one chime the number of the hour, and rig the circuits so that each chime goes off 2 times a day. A T Flip-Flop counter and 4-bit to hexadecimal converters can be used to save space.

### Multibase Clock
If you want your clock to sound in all your bases, but don't want to build different clocks all over the map, it is possible to connect all your bases to the clock. This will mean more delay from repeaters needed to carry power the distance from clock to base, but you can just say that there are minute time zone differences across the map (or make every base have an equal delay). Then just build more chimes in your bases. The inverters can also be connected to different parts of your central clock to offset the delay caused by the repeaters.

### Clock Tower with 7-segment display
While this requires a lot of extra work (as well as extra Redstone) this clock could tell the time over great distances—at least far greater than 48 blocks.

### Timed Stations
Link a clock of any time period to a powered rails controlling minecarts within a station, making minecarts leave at uniform intervals. Additionally, the station can be placed nearby a visible clock display to determine accurate timetables and tell players when the next carts will leave or arrive.

