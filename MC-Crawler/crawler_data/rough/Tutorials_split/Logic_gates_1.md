### Version 3
** Full Adder **
Size: 5×6×3

Carry input and output are aligned to easily connect many of these modules in series.


Schematic of the Full Adder



### Fast adding
When building advanced digital circuits like computers and multipliers, the adders used must be as fast as possible to ensure maximum running speed. Simple adders have one fundamental speed problem that numerous adder designs try to correct to speed up. The issue is carry propagation delay: delay caused by the way adders borrow carries. We can see this when we do the problem 1111 + 0001:

1111
0001
----
1110

This is the first step of the addition process, XORing the two inputs. Because there were two 1s in the least significant bit, the AND gate activates and carries to the next bit:

  1
1111
0001
----
1100

But here is the issue: You now need to borrow a carry again, because, in the two's place, there are two ones. This is done by ANDing the output of the first half-adder with the carry from the previous bit and this is a huge issue. Because, for the next bit, you AND the borrowed carry again, and again. Each AND gate takes 2 ticks, so, in order to calculate all of the carries that need to be added up in the final step, it takes 2 ticks times 4 bits, or 8 ticks.

Imagine you see the problem 999 + 1. You don't sit around thinking "9 + 1 is 10, carry 1, so 9 + 1 is 10, carry the 1, so 9 + 1 is 10, so 1000." It's the same situation in an advanced circuit.

Real electrical engineers and creative redstoners have designed circuits that calculate adder carries faster than this sequential method.

Incidentally, adders that calculate carries one at a time in this fashion are called Ripple Carry adders.

### Piston adders
One of the simplest and most classic ways of solving the ripple carry problem is to use instant AND gates that use pistons. These adders are simple and fast, but are inconstant because they use pistons. When blocks are accidentally dropped, the entire circuit breaks. Pistons also have timing awkwardness that can be excruciatingly inconvenient when building an advanced circuit that relies heavily on timing.



Whenever a carry is created, it is sent through the wire with the lever on it, and, instead of going through an AND gate, the piston retracts and the carry can move on to the next bit, which adds no carry propagation delay at all (until the signal strength runs out).

This video shows a straightforward implementation of the logic. The design is large and spread out, so it's easy to see each individual part of the adder and the carry logic.






### 4-bit adder
Gates: XNOR (7), IMPLIES (4), NOT (4), OR (3), AND (3)
Size: 23X12X5

Note! The least significant digit ("ones" digit) is on the left of the diagram so that the progression from half adder to the full adders can be seen more clearly. Reverse the diagram if you want a conventional left to right input.

This adder takes two 4-bit numbers (A and B) and adds them together, producing a sum (S) bit for each bit added and a carry (C) for the whole sum. The sum bits are in the same order as the input bits, which on the diagram means that the leftmost S output is the least significant digit of the answer. This is just an example of a string of adders; adders can be strung in this way to add bigger numbers as well.


4-bit Adder schematic




### Alternate 4-bit adder
The same function but a different design with 4 full adders instead of 1 half adder and 3 full adders

NOTE: switches are inputs A and B (top switch C input)


Alternate 4-bit Adder schematic



## Subtracting
Subtracting and adding are the same thing when reduced down to the idea that, for example, 3-2 = 3 + (-2) = 1. Since we already have the framework in place to add bits, it is fairly simple to subtract by just adding the negative bit. The problem lies in the representation of negative numbers. 

We are all familiar with the elementary school concept of "borrowing" in subtraction from the next column like this:

 5623
- 128
-----

We are not capable of taking 8 from three, so we "borrow" a 1 from the next decimal place to allow us to subtract 8 from 13 instead, resulting in 5

   1
 5623
- 128
-----
    5

Computers are not capable of assumptions, so when a computer needs to find a negative it does not (and cannot) put a negative sign in front of the input. It just subtracts from zero "borrowing" from the next column like so:

 000000
 -    3
-------
-999997

This is the same in binary. Let us, for example use a 4 bit binary number for the example:

   1      11     111    1111
 0000    0000    0000    0000
-0011   -0011   -0011   -0011
-----   -----   -----   -----
-   1   -  01   - 101   -1101

We could repeat this forever, but that would be useless. This is about what a 4 bit register does: it truncates after 4 bits worth of data. So after we truncate the number (which I kindly did for you in the example, otherwise the number would have an infinite number of 1's to the left). Thanks to this little perk, we can do whatever we want to the 0's after the four of them, including (which is fantastically useful later) adding a single 1 in front of them.

10000
-0011
-----
 1101 <-- NOTE: This number is positive! Success!

Remember how we said that our redstone had no special way of designating a negative from a positive? We just created a way. If the most significant (first) bit of a number is 1 that means that it is a negative number. This fantastic perk of binary numbers is a theorem called "Two's Complement".

Formally, Two's Complement is defined as:

The negative of a number b with bit length n is equal to 2n+1 − b

Essentially what this is saying is that −b is just the inversion of b (exchange 1's for 0's and 0's for 1's) plus 1.

What we have done is turn the first bit into a "negative sign" if it is on, but if you have been reading this you realize it is not that simple. Numbers that have a negative sign like this are commonly referred to as signed integers. Numbers like in a normal adder, where two's compliment is not taken into effect are called unsigned integers. Unsigned integers can go to a higher value, but cannot go below zero where as signed integers can go only half as high, but they can go equally as far below zero. This means that the two numbers have the same range, it is just in a different location like so (this is with an 8 bit number):

Unsigned: 0-255
Signed -128-127

It should be noted that some strange effects can take place when using the lowest signed value (in this case -128) so this should be avoided.

Now that we have a positive way of representing our negative numbers it is very trivial to implement this into an adder. Currently our adder solves

A + B

We want it to solve

A − B

or

A + (−B)

Therefore, if we enter the two's complement of B, our adder becomes a subtractor. This is easily implemented by using the Carry-in bit of the least significant (first) bit as the "+1" and then all that is left is to invert B.

There is one important thing to note when implementing this. Because it is possible to get a two's complement number out, when subtracting the most significant digit must be inverted. This is usually the Carry out of the last adder.

This can all be implemented into an adder like so:



A control bit is added to the circuit such that when it is on, the unit subtracts, and when it is off the unit adds. After this, add XOR gates between the control bit and each B input. Route the output of each XOR to the B input of each adder. Finally, to make the unit Two's compliment compatible, a final XOR gate must be added between the control bit and the carry out of the most significant bit.

This is the simplest way to implement negatives and subtraction in a CPU, as it adds gracefully and store well in registers. If this is to be implemented in a calculator, simply subtract 1 from the output and then invert all the outputs except the most significant one. The most significant bit is on if the number is negative.

In order to make a subtracter, simply invert one of the binary inputs (the 1st or 2nd number). If the number is negative, the answer comes out inverted. In real computers, the first bit (also called the sign) decides whether the number is positive or negative, if you include this (applying the same inverting rule) you can detect whether the number is negative, or if it is just a big number.

