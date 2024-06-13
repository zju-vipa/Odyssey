# Tutorials/Instant wire
Instant wiring is a glitch found in Beta which allows for Instant redstone repeater, and logic gates to be created by players.

## Contents
- 1 History
	- 1.1 The First Redstone Repeater
	- 1.2 The First Logic Gates
- 2 Basic Mechanics
	- 2.1 The Redstone Instant Repeater
	- 2.2 Instant Logic Gates
		- 2.2.1 NOT Gate (¬)
		- 2.2.2 OR Gate
		- 2.2.3 NOR Gate
		- 2.2.4 AND Gate
		- 2.2.5 NAND Gate
		- 2.2.6 T Flip-Flop
- 3 References

## Basic Mechanics
### The Redstone Instant Repeater
SethBling's design of an Instant Repeater
This new design of an instant repeater was released by SethBling via YouTube. It is somewhat compact, and it could repeat the signal instantly. It did not send pulses like the previous repeaters, so when the input is off the output is off. When the input is on, the output is on.

| A | Q |
|---|---|
| 1 | 1 |
| 0 | 0 |

| Design         | A     |
|----------------|-------|
| Size           | 5×4×2 |
| Torches        | 2     |
| Redstone       | 9     |
| Repeaters      | 2     |
| Sticky Pistons | 1     |


### Instant Logic Gates
#### 
A device that inverts the input, as such it is also called an "Inverter" Gate. It is very similar to the repeater, just it has a few things switched around.

| A | ¬A |
|---|----|
| 1 | 0  |
| 0 | 1  |

| Design         | A     |
|----------------|-------|
| Size           | 5×4×2 |
| Torches        | 2     |
| Redstone       | 15    |
| Repeaters      | 2     |
| Sticky Pistons | 1     |




#### OR Gate
A device where the output is on when at least one of the inputs are on. This is very simple. All you do is combine the two input lines.

| A | B | A∨B |
|---|---|-----|
| 1 | 1 | 1   |
| 1 | 0 | 1   |
| 0 | 1 | 1   |
| 0 | 0 | 0   |

| Design         | A     |
|----------------|-------|
| Size           | 1×1×1 |
| Torches        | 0     |
| Redstone       | 1     |
| Repeaters      | 0     |
| Sticky Pistons | 0     |


#### NOR Gate
A device where the output is off when at least one of the inputs are on. Almost the same as OR Gate, except here the player combined the lines before an inverter.

| A | B | A∨B |
|---|---|-----|
| 1 | 1 | 0   |
| 1 | 0 | 0   |
| 0 | 1 | 0   |
| 0 | 0 | 1   |

| Design         | A     |
|----------------|-------|
| Size           | 5×4×2 |
| Torches        | 2     |
| Redstone       | 15    |
| Repeaters      | 2     |
| Sticky Pistons | 1     |


#### AND Gate
TheMaterial4's Design of an AND Gate
A device that requires both inputs to be ON for the output to be ON. Basically an AND gate is an inverted signal hooked up to a NOR Gate. Easy to make and VERY big, but instant.

| A | B | A∨B |
|---|---|-----|
| 1 | 1 | 1   |
| 1 | 0 | 0   |
| 0 | 1 | 0   |
| 0 | 0 | 0   |

| Design         | A       |
|----------------|---------|
| Size           | 11×10×2 |
| Torches        | 6       |
| Redstone       | 51      |
| Repeaters      | 6       |
| Sticky Pistons | 3       |




#### NAND Gate
A device that requires both inputs to be ON for the output to be OFF. Basically an AND gate is an inverted signal hooked up to a NOR Gate, then into an inverter. Easy to make and VERY big, but instant.

| A | B | A∨B |
|---|---|-----|
| 1 | 1 | 0   |
| 1 | 0 | 1   |
| 0 | 1 | 1   |
| 0 | 0 | 1   |

| Design   | A     |
|----------|-------|
| Size     | 3×1×2 |
| Torches  | 2     |
| Redstone | 1     |


#### T Flip-Flop
A memory device that switches between on and off with each pulse. In simple terms, you can make a button work like a lever. Very compact design, 100% instant, but works on falling edge of the input. To make it work on the rising edge, put an inverter before and after the T Flip-Flop.


