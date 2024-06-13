# Redstone circuits/Logic
A logic gate can be thought of as a simple device that returns a number of outputs, determined by the pattern of inputs and rules that the logic gate follows. For example, if both inputs in an AND gate are in the 'true'/'on'/'powered'/'1' state, then the gate returns 'true'/'on'/'powered'/'1'.

There are many different kinds of logic gates, each of which can be implemented with many different designs. Each design has various advantages and disadvantages, such as size, complexity, speed, maintenance overhead, or cost. The various sections describe different designs for each gate type.

## Contents
- 1 Concepts
- 2 Logic gate
	- 2.1 NOT gate
	- 2.2 OR gate
	- 2.3 NOR gate
	- 2.4 AND gate
	- 2.5 NAND gate
	- 2.6 XOR gate
	- 2.7 XNOR gate
	- 2.8 IMPLY gate
- 3 Gallery
- 4 Video
- 5 See also

## Concepts
The output of each logic circuit reflects the state of its inputs at all times (though possibly with some delay incurred by the circuit).

** Swapping inputs **
For most of these gates, A and B can be swapped without changing the output.
Swapping the inputs of the IMPLIES gatedoesaffect its output, and the NOT gate has only one input.
** Stacking inputs **
The AND, OR, and XOR gates can each be used in arrays to perform their operation on more than two inputs, by combining two inputs at a time, then combining the results with each other and/or other inputs. For these gates, the order in which the inputs are combined doesn't matter.
When an XOR gate is combined in this way, its output is on when anoddnumber of inputs is on.
** Choosing a logic gate **
When unsure which logic gate to use, try building a table like the one down below but with just one row of outputs. List the known inputs coming in and the possible combinations of power, and for each combination write down what the output should be for the structure to work. Then compare that to the table on the right and see which gate matches the desired outputs.
If the the output needs to change when the input is stable, or needs to be remembered after the input has ended, the player may also need to look atpulse circuitsormemory circuits.

| A                | On  | On  | Off | Off | Question Answered         |
|------------------|-----|-----|-----|-----|---------------------------|
| B                | On  | Off | On  | Off |                           |
| A AND B          | ON  | off | off | off | Are A and B on?           |
| NOT(A IMPLIES B) | off | ON  | off | off | Is A on and B off?        |
| NOT(B IMPLIES A) | off | off | ON  | off | Is B on and A off?        |
| A NOR B          | off | off | off | ON  | Are both inputs off?      |
| A                | ON  | ON  | off | off | Is A on?                  |
| A XOR B          | off | ON  | ON  | off | Are the inputs different? |
| NOT A            | off | off | ON  | ON  | Is A off?                 |
| A XNOR B         | ON  | off | off | ON  | Are the inputs the same?  |
| B                | ON  | off | ON  | off | Is B on?                  |
| NOT B            | off | ON  | off | ON  | Is B off?                 |
| A NAND B         | off | ON  | ON  | ON  | Is either input off?      |
| A IMPLIES B      | ON  | off | ON  | ON  | If A is on, is B also on? |
| B IMPLIES A      | ON  | ON  | off | ON  | If B is on, is A also on? |
| A OR B           | ON  | ON  | ON  | off | Is either input on?       |

## Logic gate
A logic gate is a basic logic circuit.

### NOT gate
| A     | On  | Off |
|-------|-----|-----|
| NOT A | off | ON  |

A NOT gate (A‾), also known as an inverter, is a gate used when an opposite output is wanted from the input given. For instance, when the switch, or input, is set to "on", the output toggles to "off", and when the switch is toggled to "off", the output toggles to "on".

** Torch Inverter **
1-wide, flat (horizontal only), silent, tileable
circuit delay: 1 tick
The torch inverter is the most commonly used NOT gate, due to its small size, versatility, and easy construction.
One drawback of the torch inverter is that it "burns out" if run on a clock cycle faster than a 3-clock (3 ticks on, 3 ticks off). A burnt out torch inverter turns on after it receives a block update.
** Subtraction Inverter **
flat, silent
circuit delay: 1 tick
The subtraction inverter offers little advantage over the torch inverter except that it can run on a 2-clock cycle without burning out. Faster clocks do not work though — the comparator simply doesn't react to them.
Variations:The powered lever can be replaced with another always-on power component (e.g., redstone torch, block of redstone), or with a full container if a power component would be inconvenient in that location.
The repeater is required to ensure the input signal is strong enough to overcome the comparator's rear source, but can be removed in a number of ways. If the input power level is known (because the circuit design is fixed, so it can be calculated), the repeater can be removed by replacing the powered lever with a container, which produces the same power level. Alternatively, the repeater can be removed if the output continues to a length of redstone wire that reduces the subtracted signal enough that the signal is inverted eventually.
** Instant Inverter **
instant
circuit delay: 0 ticks
The instant inverter is a basic building block of larger instant circuits.
The "ground" version has the largest volume, but is shorter and fits easily with flatter circuits. The 1-wide version is the smaller in total volume and 2-tileable.
Behavior (i.e., how it works):An instant inverter has two functional elements, and a piston, or pistons, that activate them:
1. a constant power source with output that can be instantly powered off (but powering it on takes time): either a redstone block that ceases to provide power as soon as piston starts moving it (within the same tick the piston receives or loses power) or a solid block in front of a powered repeater or comparator, powering redstone dust; as soon as the block starts moving the dust is unpowered.
2. a signal line with output that can be instantly powered on but not necessarily off, its input delayed by and sustained for 2 ticks. The "instant on" is achieved by the dust-cut technique: a solid block placed against edge of a block over which a redstone line is running, disconnects that line from line below. Start of motion of that block instantly reconnects the line and provides power. The delay is achieved by running the input through a 2 tick repeater, two torches or similar means. That means, when power appears on input, the block moved by piston is able to cut the line before signal passes through the delay. With input unpowered, the output is instantly activated and the line still provides power "stored" in the repeater for two ticks, which time is sufficient to reactivate the constant power source from previous point.
3. Piston, or pistons, to move the block/blocks activating the elements from point 1 or 2.

Schematic gallery: NOT gate View at: Redstone circuits/Logic/NOT [edit]
