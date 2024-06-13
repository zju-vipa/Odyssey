# Tutorials/Advanced redstone circuits
Advanced redstone circuits encompass mechanisms that require complicated redstone circuitry. They are usually composed of many simpler components, such as logic gates. For simpler mechanisms, see electronic mechanisms, wired traps, and redstone.

## Contents
- 1 Computers
- 2 Converters
	- 2.1 Piston mask demultiplexer
	- 2.2 Binary to 1-of-8
	- 2.3 Binary to 1-of-16 or 1-of-10
	- 2.4 1-of-16 to Binary
		- 2.4.1 Example
- 3 Miscellaneous
	- 3.1 Combination locks
	- 3.2 Sorting device
	- 3.3 Timer
	- 3.4 Serial interface lock with D flip-flops
- 4 See also

## Computers
Main article: Tutorials/Redstone computers
In Minecraft, several in-game systems can usefully perform information processing. These systems include water, sand, minecarts, pistons, and redstone. Of all these systems, only redstone was specifically added for its ability to manipulate information, in the form of redstone signals. 

Redstone, like electricity, has high reliability and high switching-speeds, which has seen it overtake the other mechanical systems as the high-tech of Minecraft, just as electricity overtook the various mechanics such as pneumatics to become the high-tech of our world.

In both modern digital electronics and redstone engineering, the construction of complex information processing elements is simplified using multiple layers of abstraction.

The first layer is that of atomic components; redstone/redstone torches/redstone repeaters/blocks, pistons, buttons, levers and pressure plates are all capable of affecting redstone signals. 

The second layer is binary logic gates; these are composite devices, possessing a very limited internal state and usually operating on between one and three bits.

The third layer is high-level components, made by combining logic gates. These devices operate on patterns of bits, often abstracting them into a more humanly comprehensible encoding like natural numbers. Such devices include mathematical adders, combination locks, memory-registers, etc.

In the fourth and final layer, a key set of components are combined to create functional computer systems which can process any arbitrary data, often without user oversight.

An 8-bit register page would be in the third layer of component abstraction
## Converters
These circuits simply convert inputs of a given format to another format. Converters include Binary to BCD, Binary to Octal, Binary to Hex, BCD to 7-Segment, etc.

### Piston mask demultiplexer
You can understand this design as a combination of AND gates. 

Demultiplexer is a circuit that uses the following logic:

Output 0 = (~bit2) & (~bit1) & (~bit0)

Output 1 = (~bit2) & (~bit1) & (bit0)

...

The most obvious way to implement a demultiplexer would be to put a whole bunch of logic gates and connect them together, but even with 3 or 4 bits it turns into a mess.

If you look at the binary numbers table, you can notice a pattern.

| N | Bit2 | Bit1 | Bit0 |
|---|------|------|------|
| 0 | 0    | 0    | 0    |
| 1 | 0    | 0    | 1    |
| 2 | 0    | 1    | 0    |
| 3 | 0    | 1    | 1    |
| 4 | 1    | 0    | 0    |
| 5 | 1    | 0    | 1    |
| 6 | 1    | 1    | 0    |
| 7 | 1    | 1    | 1    |

If the number of bits is Q, the most significant bit reverses every Q/2 numbers, the next bit reverses every Q/4 numbers an so on until we get to the Qth bit.

Therefore, we should make a circuit that looks like this:



Where the green triangles are non-reversing and red triangles are reversing. The black lines are imaginary AND gates.

We can easily implement this using 3 "punch cards" that consist of solid blocks and air. The "punch cards" or the masks are being moved by pistons with slime blocks. 

So the signal is only being propagated if all three layers of masks align in a specific way.



 Open the picture to see the layers.

As you can see, this system is very compact and comprehensible.

You can use this in reverse as well (not as a multiplexer, but if you reverse the repeaters the signal from every ex-outptut (0–7) will only propagate if it matches the current state of the demultiplexer, so it works like "Output3 = (Input3) AND (Demux=011)").

### Binary to 1-of-8
3-bit Binary to 1-of-8 gates.
A series of gates that converts a 3-bit binary input to a single active line out of many. They are useful in many ways as they are compact, 5×5×3 at the largest.

As there are many lines combined using implicit-ORs, you have to place diodes before each input into a circuit to keep signals from feeding back into other inputs.

Requirements for each output line (excluding separating diodes):

| Number   | 0     | 1     | 2     | 3     | 4     | 5     | 6     | 7     |
|----------|-------|-------|-------|-------|-------|-------|-------|-------|
| Size     | 5×3×2 | 5×3×3 | 5×5×3 | 5×5×3 | 5×3×3 | 5×4×3 | 5×5×3 | 5×5×3 |
| Torches  | 1     | 2     | 2     | 3     | 2     | 3     | 3     | 4     |
| Redstone | 7     | 7     | 12    | 10    | 7     | 7     | 10    | 10    |


### Binary to 1-of-16 or 1-of-10
A series of gates that converts a 4-bit binary input to a single active line out of many (e.g. 0-9 if the input is decimal or 0-F if the input is hexadecimal). They are useful in many ways as they are compact, 3×5×2 at the largest.

As there are many lines combined using implicit-ORs, you have to place diodes before each input into a circuit to keep signals from feeding back into other inputs.

4-bit Binary to 1-of-16 gates.
Requirements for each output line (excluding separating diodes):

| Number   | 0     | 1     | 2     | 3     | 4     | 5     | 6     | 7     | 8     | 9     | A     | B     | C     | D     | E     | F     |
|----------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| Size     | 3×3×2 | 3×4×2 | 3×4×2 | 3×4×2 | 3×4×2 | 3×5×2 | 3×5×2 | 3×5×2 | 3×4×2 | 3×5×2 | 3×5×2 | 3×5×2 | 3×5×2 | 3×5×2 | 3×5×2 | 3×5×2 |
| Torches  | 1     | 2     | 2     | 3     | 2     | 3     | 3     | 4     | 2     | 3     | 3     | 4     | 3     | 4     | 4     | 5     |
| Redstone | 2     | 2     | 2     | 2     | 2     | 2     | 2     | 2     | 2     | 2     | 2     | 2     | 2     | 2     | 2     | 2     |


### 1-of-16 to Binary
You also can convert a 1-of-16 signal to a 4-bit binary number. You only need 4 OR gates, with 8 inputs each. These have to be isolating ORs to prevent signals from feeding back into other inputs.

For every output line, make an OR gate with the inputs wired to the input lines where there is a '1' in the table below.

| Number | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | A | B | C | D | E | F |
|--------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4-bit  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 3-bit  | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 |
| 2-bit  | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 |
| 1-bit  | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 |


#### Example
Logic for a 3-digit key log, with digits 0-9. It's order-sensitive
The example on the right uses ORs (>=1), XNORs (=), RS NOR latches (SR) and some delays (dt*). For the XNORs I would prefer the C-design.

The example on the right uses a 4-bit design, so you can handle a hexadecimal key. So you can use 15 various digits, [1,F] or [0,E]. You only can use 15, because the state (0)16 = (0000)2 won't activate the system. If you want to handle 16 states, you edit the logic, to interact for a 5-bit input, where the 5th bit represents the (0)16 state.

In the following we'll use (0)16 = (1111)2. And for [1,9] the MUX-table upon. So the key uses decimal digits. Therefore, we have to mux the used buttons to binary data. Here look through the first two columns. The first represents the input-digit in (hexa)decimal, the second represents the input-digit in binary code. Here you can add also buttons for [A,E], but I disclaimed them preferring a better arranging. The /b1\-box outputs the first bit, the /b2\-box the second, and so on.

Now you see Key[i] with i=1..3, here you set the key you want to use. The first output of them is the 1-bit, the second the 2-bit and so on. You can set your key here with levers in binary-encryption. Use here the MUX-table upon, and for (0)h := (1111)2. If we enter the first digit, we have to compare the bits by pairs (b1=b1, b2=b2, b3=b3, b4=b4). If every comparison is correct, we set the state, that the first digit is correct.

Therefore, we combine (((b1=b1 & b2=b2) & b3=b3) & b4=b4) =: (b*=b*). In Minecraft we have to use four ANDs like the left handside. Now we save the status to the RS-latch /A\. The comparison works the same way for Key[2], and Key[3].

Now we have to make sure, that the state will be erased, if the following digit is wrong. Therefore, we handle a key-press-event (--/b1 OR b2 OR b3 OR b4\--/dt-\--/dt-\--). Search the diagram for the three blocks near "dt-". Here we look, if any key is pressed, and we forward the event with a minor delay. For resetting /A\, if the second digit is wrong, we combine (key pressed) & (not B). It means: any key is pressed and the second digit of the key is entered false. Therewith /A\ will be not reset, if we enter the first digit, /A\ only should be reset, if /A\ is already active.
So we combine (B* & A) =: (AB*). /AB*\ now resets the memory-cell /A\, if the second digit is entered false and the first key has been already entered. The major delay /dt+\ must be used, because /A\ resets itself, if we press the digit-button too long. To prevent this failure for a little bit, we use the delay /dt+\. The OR after /AB*\ is used, for manually resetting, i.e. by a pressure plate.

Now we copy the whole reset-circuit for Key[2]. The only changes are, that the manually reset comes from (not A) and the auto-reset (wrong digit after), comes from (C). The manual reset from A prevents B to be activated, if the first digit is not entered. So this line makes sure, that our key is order-sensitive.

The question is, why we use the minor-delay-blocks /dt-\. Visualize /A\ is on. Now we enter a correct second digit. So B will be on, and (not B) is off. But while (not B) is still on, the key-pressed-event is working yet, so A will be reset, but it shouldn't. With the /dt-\-blocks, we give /B\ the chance to act, before key-pressed-event is activated.

For /C\ the reset-event is only the manual-reset-line, from B. So it is prevented to be activated, before /B\ is true. And it will be deactivated, when a pressure-plate resets /A\ and /B\.

** Pros **
- You can change the key in every digit, without changing the circuit itself.

- You can extend the key by any amount of digits, by copying the comparison-circuit. Dependencies from previous output only.

- You can decrease the amount of digits by one by setting any digit (except the last) to (0000)2.

- You can open the door permanently by setting the last digit to (0000)2

** Cons **
- The bar to set the key will be get the bigger, the longer the key you want to be. The hard-coded key-setting is a compromise for a pretty smaller circuit, when using not too long keys. If you want to use very long keys, you also should softcode the key-setting. But mention, in fact the key-setting-input will be very small, but the circuit will be much more bigger, than using hard-coded key-setting.

Not really a con: in this circuit the following happens with maybe the code 311: 3 pressed, A activated; 1 pressed, B activated, C activated. To prevent this, only set a delay with a repeater between (not A) and (reset B). So the following won't be activated with the actual digit.

If you fix this, the circuit will have the following skill, depending on key-length. ( digit = 2n-1, possibilities: digitLength )

| Length | 1  | 2   | 3      | 4       | 5          |
|--------|----|-----|--------|---------|------------|
| 2 bit  | 3  | 9   | 27     | 81      | 243        |
| 3 bit  | 7  | 49  | 343    | 2.401   | 16.807     |
| 4 bit  | 15 | 225 | 3.375  | 50.625  | 759.375    |
| 5 bit  | 31 | 961 | 29.791 | 923.521 | 28.629.151 |



## Miscellaneous
### Combination locks
Main article: Tutorials/Combination locks
Combination locks are a type of redstone circuit. They generally have a number of components which must be set in the right combination in order to activate something such as a door. Combination locks can be very useful in creating adventure maps. Note that if you are playing in survival multiplayer, other players will still be able to break into the mechanism and cause it to activate without knowing the password.

### Sorting device
|  |  |  |  |  |  |  |
|--|--|--|--|--|--|--|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |

This is a device which sorts the inputs, putting 1s at the bottom and 0s at the top, in effect counting how many 1s and how many 0s there are.
It is designed so that it is easily expandable, as shown in the diagram. The 5×5 center square is tileable. The inputs are at the bottom and right and the outputs are at the top and left

Truth table for a three-bit sorting device:

| A | B | C | 1 | 2 | 3 |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 1 | 0 | 0 |
| 0 | 1 | 0 | 1 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 | 0 |
| 1 | 1 | 0 | 1 | 1 | 0 |
| 0 | 1 | 1 | 1 | 1 | 0 |
| 1 | 0 | 1 | 1 | 1 | 0 |
| 1 | 1 | 1 | 1 | 1 | 1 |


### Timer
Timers can detect the time difference between the first input and the second.




2





















1










A timer. The extra repeater at the bottom is to compensate for the delay of the upper repeaters.










































Example of a timer in action. This one determines the time difference between the input and output of a 2-tick repeater.

The amount of time can be determined by how far the signal travels. For example, if 5 of the locked repeaters are powered, it means the time difference was 0.4-0.5 seconds, ignoring lag. If the time difference is exactly 0.4 seconds, 4 repeaters will be powered.

The repeaters that will lock can be set to different delays. For example, if they are set to 4 ticks and the first 3 are active, it means the time difference was 0.8-1.2 seconds. You can even have a mix, which can be handy if you know what the range is likely to be. However, you will need to be careful when reading these timers.

If you are measuring higher scales, the second signal might not reach all of the repeaters. You will need repeaters to replenish the signal.

























A section of the timer that replenishes the signal. Since the upper repeater has a delay, another repeater is required in the lower section.

If the signals are short times (like if you are using observers), you may not have time to read the data. 











2



1
















An input modifier. When the inputs are applied, the timer will treat them as active until the button is pressed.

You can also measure how long a signal lasts.











































A timer that measures the duration of a stone button.

Please note the following when making a duration timer:

- Because of the delay that the redstone torch adds, the delay of the initial repeater, the one that stays unlocked, must be increased to 2 ticks.
- The data from the timer will be preserved.
- Because the repeaters will still be powered when the timer is used again, the circuit must be obstructed between uses in order to unlock the repeaters. To do this mine theredstone torch, wait for all of the repeaters to deactivate, and put the redstone torch back.

### Serial interface lock with D flip-flops


D flip-flop is an electronic component that allows you to change its output according to the clock. It's and RS NOR latch that sets its value to the D input when the ">" (clock) input is changing its state from low to high (in some cases from high to low). 

Basically, it's equivalent to the expression: "Set the output Q to the input D when the input C goes from 0 to 1".

For example, you can use D flip-flops to shift the value from left to right.



In this lock, the > signal propagates from the rightmost flip-flop to the leftmost, so the signal shifts to the right. This circuit allows you to input a 4-bit number with two levers. You can use any number of bits, but this configuration is already pretty secure even if someone figures out what a lock it is.

So, if you want to input the combination 1-0-1-0, follow these steps:

1. D = 1
2. > = 1
3. > = 0
4. D = 0
5. > = 1
6. > = 0
7. D = 1
8. > = 1
9. > = 0
10. D = 0
11. > = 1
12. > = 0

In theory, you can program the lock from this serial interface as well. Just attach 4 RS NOR latches and a hidden place for the programming levers.

This design is not very practical as a lock, but might be a nice feature on something like a puzzle challenge map.

