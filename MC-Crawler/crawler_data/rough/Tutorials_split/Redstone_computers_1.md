### The MASIC Computer
The work in progress computer which we will be making in the tutorial.
8 bits, 16 bytes of RAM. I/O is a seven-segment display (for hex and decimal) and a control panel which we will make.



The MASIC computer aims to be a one-size-fits-all computer and does not specialize in one task, so it is fully programmable by reading its own memory (explained in Section 2: instruction sets). The simple I/O is great for multipurpose use and the memory is sufficiently sized. It runs at quite a fast speed (because of its small size).

### 
Decoders convert binary figures into decimals. For example, looking at the 8-bit decoder, 00 turns on the first lamp which stands for 0. 01 turns on the second lamp which is 1. 10 turns on the third which is 2. 11 turns on the last one which is 3.

### 
#### Address Decoder
0000 0000 (notice output 1 is lit)
0000 0001 (notice 2nd output is lit)
0000 0010
0000 0011
This is the design for the address decoder we are going to build.




Above is a simple 2-bit state, so it has two inputs (left and right) through the repeaters. The output is the redstone line above which will turn OFF when the state is met. The state is whether the redstone input will turn OFF the redstone line above; if so, the state is the redstone inputs. In the above case, the left must be turned OFF (0) and the right (blue) must be turned ON (1) to yield an OFF on the top redstone line. So it expects a state of OFF ON (aka 01 for binary).

They are colored blue for bits which should be ON (1) for it to stop powering the top redstone line. Once every bit stops powering the redstone line, it then turns off.

These are basically either one or two NOT gates feeding into a OR gate and then NOT the output.





Above is an 8-bit state, it expects 8 inputs in exactly the order 0000 1101. So that state it expects is 0000 1101. So the redstone torches power the inputs, and so we see the redstone line on the top turns OFF (only when exactly three redstone torches are placed in that exact order of 0000 1101).

Now if we put multiple of these together, we can count up in binary with the blue bits to get all 255 states of 8 bits. The one below is 8 bits, and has four state expectations. See the right images to see it in action. Now each green output can be a memory cell, and if we continue counting in binary, it will reach 255.



The input is 0000 0011 (see the redstone torches for input) and where the blue bits match the current state, the green output is ON.

- 0000 0000—first signal out (on the images on the right)
- 0000 0001—second signal out
- 0000 0010—third signal out
- 0000 0011—fourth signal out

So now we keep counting up in binary to get up to 0000 1111 and stop there; we should now have 24 (16) state expectors. Now we're done with the address decoder. We do not continue counting up to 1111 1111 because of instruction set limitations, explained in section 3: instruction sets

### 
The Arithmetic Logic Unit referred to as the ALU will compare and perform mathematical operations with binary numbers and communicate the results with the Control Unit, the central component of the computer (and Central Processing Unit but that is going to be as big as the computer itself). Many tutorials will want the reader to build an ALU first, and therefore the topic is covered very widely around the internet. 

The ALU we will be building can perform four important operations on two inputs and return a correct output. A, B, being both 8-bit inputs

- A + B (Add A to B)
- A >> (bitshift A right (the same as binary divide by 2))
- << A (bitshift A left (the same as binary multiply by 2))
- NOT A (The opposite of A)

There can also be multiple ALUs inside a computer, as some programs require a lot of operations to run, which do not depend on the previous operations (so they can be threaded) 
so delegating them to different ALUs could significantly speed up the program.

binary adder
#### Adding two numbers
In an adding unit, for each bit (for our computer, we require four, hence 4-bit), there is a full adder. The full adder will take three inputs, each input can be either 1 or 0. The first two will be the user's input and the third will be the carry input. The carry input is the output of the previous full adder, this will be explained later. The adder will output two statements: first, the output and then the carry output, which is sent as input into the next full adder, a place value up.
For example, I wish to add the number 0101 to 1011. The first full adder will consider the first place value, 1 and 1 as their two inputs (we are reading right to left). There is no carry input as there is no previous full adder. The full adder will add 1 and 1; which is 0, and carries a 1 to the next place value. The next full adder would add 0 and 1 and the carry input would be 1 which the previous full adder stated. The output of 0 and 1 would be 1 but there is a carry input of 1 and therefore will add 0 and 1 and 1, which is 0 and carries a 1 to the next place value. Reviewing addition in binary should resolve any confusion. 

All ALUs, to perform adding operations, require the presence of multiple adders. Every two bits will feed into an adder which, when joined with other adders, will produce an output which is the sum of the two bytes added together. An adder has an input, an output, and two carry input/output as would a person carry when doing the addition of 9 + 1 or 01 + 01. The adders are made of logic gates which is possible by the nomenclature of binary.
Tutorials/Arithmetic logic gives a very detailed look into full adders and half adders, for now, there is a schematic of how to construct one. It gives four inputs/outputs and should be connected with other adders to create a unit. For this example, we will connect four adders together in our four-bit computer so that we can take in all four bits to make an output. There will be an input carry missing from the first adder, this is because there is nothing to carry from the bit before it, it is the first bit. The input carry will remain at zero. There will also be an output carry missing from the fourth adder, and the output of this will be ignored as we can only support four bits. The additional fourth carry output is wired to the overflow flag to signify the operation couldn't be done. This is called a binary overflow.

So basically, go into Minecraft and build a full binary adder (picture show) and connect them up. There should be eight inputs and outputs. Try placing levers and redstone lamps at the respective ends to test your creation. So 0010 + 0011 should yield 0101 (2 + 3 = 5, we are reading right not left).

