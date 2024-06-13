#### 
The multiplier is probably the most complicated part of the calculator. For our purposes, multiplication is a repeated addition. That means that, once again, adders will be used here.
Before you add the adders, you actually have to set up an AND gate (not including the control one). Its use is simple: in binary multiplication, because only 0's and 1's are used, the only way that we can have an output is by multiplying 1 by 1.

Here is how to construct a multiplier, in order from the least to the most significant bits.

Least significant bits :
1×1 = 1. That means that the output of the second AND gate (the control one) goes straight to the output collective wires.

Second to last:
1×2 = 2 and 2×1 = 2.
Those two outputs meet in a full adder. The sum goes to the output, and the carry goes to the next bit.

Next:
1×4 = 4; 2×2 = 4; and 4×1 = 4
The carry from the last bit goes in the first adder as the carry input. The two normal inputs are 2 of the 3 AND gates. The sum of this goes in a second adder, where the second input is the third AND gate. Both carry outs go to the next stage, and the sum goes to the output.

You continue like this until you run out of AND gates, or equations.

#### 
Dividers on a redstone calculator are less complicated than multipliers. Again, full adders should be used here. Basically, for each A input, set up n adders where n is the quantity of inputs by B. Also, this time, you have to "reverse them". Now the most significant bit should pass its carry downwards.

### Output wires
Output wires have to get every output from every machine and redirect them to the next part using redstone dust.

### Binary-to-decimal decoder
This transforms your binary code into a decimal output. The size of it will be (Binary inputs*2)*(Decimal output)
*Quick note* It uses a "programmable" XOR gate cane tend to a not gate. This activates a line of preset redstone torches to output the correct answer.


