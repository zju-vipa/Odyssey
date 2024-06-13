#### Analog 3-RNG














→







→













Analog 3-RNG
The dropper contains one 64-stackable item, one 16-stackable item, and one non-stackable item.



The hopper contains five 16-stackable items in the far right slot.

5
1×3×3 (9 block volume), 1-wide, silent
circuit delay: 3 ticks (rising) and 1 tick (falling)
Outputs power levels 1, 2, or 4 while on, power level 1 while off (but see variations below).
When building this circuit, wait until the hopper is deactivated by the powered dust before putting five 16-stackable items in its far right slot. Then put a 64-stackable item, a 16-stackable item, and a non-stackable item in the dropper.
Before the input turns on, the hopper's five 16-stackable items are enough to produce a power level 1 output from its comparator (even a single 64-stackable item would be enough for that). These five items should never be returned to the dropper, so the comparator's output will never drop below power level 1.
When the input turns on, the dropper will push an item into the hopper, which will be placed in the hopper's left slot. It takes 23 64-stackable items (or five 16-stackable items and three 64-stackable items, or six 16-stackable items) to produce power level 2, so if the 64-stackable item is pushed that won't be enough to increase the output power level, but if the 16-stackable item is pushed the output power level will increase to 2. And if the non-stackable item is pushed, the output power level will increase to 4.
The hopper is held deactivated by the powered dust when the circuit is off, and by the powered dropper when the circuit is on. But, when the input turns off, there is a brief 1-tick moment when the dropper has just turned off, but the torch attached to it hasn't turned on again. This allows the hopper to activate for 1 tick, pushing an item back into the dropper. A hopper always pushes items from its left slots first, so the hopper will push back the item the dropper pushed into it, rather than any of the 16-stackable items in its far right slot, allowing the circuit to reset itself.
Variations:The player can remove one of the items from the dropper to create a 2-RNG with different power level outputs than the regular 2-RNG: removing the 64-stackable item outputs power levels 2 or 4, removing the 16-stackable item outputs power levels 1 or 4, and removing the non-stackable item outputs power levels 1 or 2.
You can add additional redstone dust leading from the hopper to a block next to it, and then down to the side of the comparator. This 2-wide variation will keep the comparator's output off while the input is off.
With only three items in the dropper, all three output power levels will be chosen with equal probability. The probability of the output levels can be changed by adding additional 64-stackable, 16-stackable, and non-stackable items to the dropper (which must all be different from each other so they won't stack). For example, with one 64-stackable item, one 16-stackable item, and two different non-stackable items, the RNG will output power level 1 25% of the time, power level 2 25% of the time, and power level 4 50% of the time.
Additional items can be added to the hopper to increase all of the output power levels.
Earliest Known Publication:16 April 2013[2]

#### Analog 16-RNG
5×8×4 (160 block volume)
circuit delay: 8.5 ticks
Outputs power levels 0 to 15 while on, power level 1 while off.
Uses four 2-RNGs to subtract 1, 2, 4, and/or 8 from 15.
Reducing the number of 2-RNGs reduces the possible outputs: three 2-RNGs produces an 8-RNG, and two 2-RNGs produces a 4-RNG (the exact power levels depend on the power level provided to the subtraction comparators).
Earliest Known Publication:June 10, 2013[3]
Schematic: Analog 16-RNG View at: Mechanics/Redstone/Miscellaneous circuits/analog 16-rng [edit]
### Randomizers with digital signal output
Digital randomizers work by randomly generating a binary number and selecting a corresponding output using a binary decoder. To achieve a flat probability the bits are randomly generated, typically using an analog randomizer with a 50% chance of activation and a red-coder.

