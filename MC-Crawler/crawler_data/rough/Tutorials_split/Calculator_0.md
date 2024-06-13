# Tutorials/Calculator
This tutorial will show you how to make a calculator in Minecraft using redstone.

## Contents
- 1 Resume
- 2 Current parts
	- 2.1 Control panel (room)
		- 2.1.1 Numbers input panel
		- 2.1.2 Operation panel
	- 2.2 Input wires (white and orange)
	- 2.3 Logic units
		- 2.3.1 Adder/Subtractor (yellow and red)
		- 2.3.2 Multiplier (light blue)
		- 2.3.3 Divider (pink)
	- 2.4 Output wires
	- 2.5 Binary-to-decimal decoder
- 3 See also

## Resume

See the following image for an example of a calculator: 
Calculator Plan
Calculator Scheme

Of course, all compilations are made with binary code. This is why this calculator has many different decoders.

## Current parts
The following are the components of a calculator. They are in a somewhat logical order.

### 
The control panel is the room from which you set the inputs and decide of the operation.

#### Numbers input panel
Numbers Input Panel
Here, the users will decide what numbers they want to use. In the picture, a lever-based binary input system is used, so the users must decompose the numbers they want to use into powers of two.

#### Operation panel
From this panel, the user chooses between the operations he is going to use: add (+), subtract (-), multiply (*) and divide (/). Like for the Number's Input Panel, this picture of the Operation Panel uses the lever system.

Operation Panel
### 
These wires link the input panel and the operation panel to the different logic units. Try to rearrange them in a manner where the same values go together. So, your wires should look like, from left to right: A1; B1; A2; B2; A4; B4; ...

### Logic units
The logic units in a calculator are the machines that perform the operations.

#### 
The picture to the left shows a version of an adder/subtractor. Its construction is simple because it is modulated (made of many same parts). That means that if you use more bits, you can just add more parts on the side. However, this means that you'll have to change some links.

2-in-1 Adder/Subtractor
In this machine, your inputs (in binary code) go into the bottom (yellow) full adders. Each adder needs the two inputs (A and B) with the same values. Also, the least significant bit has to be on the left, so they should all be connected by their carries. Basically, your inputs look like the wires in the #Input Wires (white and orange) section. Use basic bridges to pass wires over the others without connecting them.
 Your A inputs (left) are the minuend (X in X-Y=Z), and go straight in the adders. The B inputs, your subtrahend (Y in X-Y=Z), have to pass through a multiplexer, made out of a modified version of a XOR gate which gives to the adder an inverted signal in case of a subtraction. The multiplexer is controlled by a switch (on the picture, that switch is on the left). The sums go into another multiplexer, which, again, gives an inverted input in case of a subtraction. This is controlled by an IMPLIES gate (in the top right) which gives a true output if the switch is on "Subtraction" AND if the last carry is true. This is required because on a subtraction, that last carry actually means the "-" (minus) sign. 


The white machines are half-adders, that use, as inputs, the carry of the last adder and the sum of their respective full adder. We need this because, if the answer is negative, it uses the equation " -A = !A (inverted A)+ 1 ", as explained here.
The final outputs are all of the top-most wires you can observe, plus the wire on the right (the carry from the last full adder) and the carry that goes in the first (left) half-adder, as the negation sign.

