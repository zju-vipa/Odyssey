### Pulse circuit
Main article: Pulse circuit
Some circuits require specific pulses; other circuits use pulse duration to convey information. Pulse circuits manage these requirements.

A circuit that is stable in one output state and unstable in the other is known as a monostable circuit.[note 1] Many pulse circuits are monostable because their OFF state is stable, but their ON state soon reverts to OFF.

** Pulse generator **
A pulse generator produces a pulse of a specific duration.
** Pulse limiter **
A pulse limiter (aka pulse shortener) reduces the duration of pulses that are too long.
** Pulse extender **
A pulse extender (aka pulse sustainer, pulse lengthener) increases the duration of pulses that are too short.
** Pulse multiplier **
A pulse multiplier outputs multiple pulses for every input pulse (it multiplies the number of pulses).
** Pulse divider **
A pulse divider (aka pulse counter) outputs a signal only after a certain number of pulses have been detected through the input (the number of pulses is indicative of the number of loops).
** Edge detector **
An edge detector reacts to either a redstone signal changing from OFF to ON (a "rising edge" detector), from ON to OFF (a "falling edge" detector), or switching between ON and OFF in either order(a "dual edge" detector).
** Pulse length detector **
A pulse length detector reacts only to pulses in a certain range of durations (often only to pulses of one specific duration).
### Clock circuit
Main article: Clock circuit
A clock circuit is a pulse generator that produces a loop of specific pulses repeatedly. Some are designed to run forever, while others can be stopped and started.

A simple clock with only two states of equal duration is named for the duration of its ON state (e.g., for example, a clock that alternates between a 5-tick ON state and a 5-tick OFF state is called a 5-clock) while others are usually named for their period (the time it takes for the clock to return to its original state; for example, a "1-minute clock" might produce a 1-tick pulse every 60 seconds).

** Observer clock 1 **
A repeating clock made with Observers and Pistons (an Observer looking at a piston).Observer clock 2
A repeating clock made with two Observers with their faces facing each other.
** Repeater clock **
A repeater clock consists of a loop of repeaters (usually eitherredstone repeatersorredstone torches) with occasional dust or blocks to draw off the appropriate pulses.
** Hopper clock **
A hopper clock produces timed pulses by moving items back and forth between 2 hoppers feeding into each other and taking a redstone output with comparators.
** Piston clock **
A piston clock produces a loop of pulses by passing a block back and forth (or around, with many pistons) and drawing off a redstone pulse when the block is in a certain location.
** Comparator clock **
The clock of short or moderate cycle length utilizing comparator's subtraction or signal fading feature. Clocks can also be built usingdaylight sensors,minecarts,boats, water flow, item despawn, etc.
### Memory circuit
Main article: Memory circuit
Unlike a logic circuit whose state always reflects its current inputs, a memory circuit's output depends not on the current state of its inputs, but on the history of its inputs. This allows a memory circuit to "remember" what state it should be in, until told to remember something else. There are five basic types of memory circuits. (A few circuits combine two different types.) 

** RS latch **
An RS latch has two inputs, one to set the output on and another to reset the output back to off. An RS latch built from NOR gates is known as an "RS NORlatch", which is the oldest and most common memory circuit inMinecraft.
** T flip-flop **
A T flip-flop is used to toggle a signal (like a lever). It has one input, which toggles the output between on and off.
** Gated D latch **
A gated D latch has a "data" input and a "clock" input. When the clock input turns on, it sets the output to equal its data input. Not to be confused with a D flip-flop, which sets the output equal to its data input on a clock rising transition.
** JK latch **
A JK latch has two inputs, one to set the output on and another to reset the output back to off (like an RS latch), but when both turn on simultaneously it toggles the output between on and off (like a T flip-flop).
** Counter **
Unlike T flip-flops and RS latches, which can hold two states (ON or OFF), a counter can be designed to hold a greater number of states.
Many other memory circuits are possible.

### Piston circuits
Main article: Piston circuits
Pistons allow players to design circuits that are smaller and/or faster than the standard, redstone-only counterparts. An understanding of standard redstone circuits is helpful, as this tutorial is focused on the circuit design rather than the function. The main components here are sticky pistons, regular pistons, redstone wire, repeaters and redstone torches.

There are several benefits of piston circuitry:

- Neither repeaters nor pistons 'burn out', unlike redstone torches.
- Piston circuits are often (not always) smaller and/or faster than their redstone counterparts. This allows building devices such as fast clocks and "instant" signal transmission.
- Pistons' ability to move blocks within the world makes them a natural for memory circuits, as well as the obvious doorways and switchable bridges. With slime or honey blocks involved, entire structures can "get up and move" (see alsotutorial on flying machines).
- Piston circuits can sharply reduce the use of redstone in favor of wood, stone, and iron.

