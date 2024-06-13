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



