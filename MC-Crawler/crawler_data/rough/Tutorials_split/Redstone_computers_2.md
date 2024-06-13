##### Fractional numbers
A computer takes care of numbers less than one by form of float-point arithmetic, it is only so useful in larger-bit computers (16-64 bits) and computers which do need to use numbers less than one. Floating-point arithmetic or arbitrary-precision arithmetic are two ways to achieve this. Another simpler but less efficient way would be to assign all numbers a power of two so that they are 'bumped up' by the power of two chosen. The player must do this to every number and assume the one as one times the power of the two you have chosen. For example, 5 = 1012 so 5 × 23 = 1010002; five is bumped up by three. So now, one in your new system would be 1 × 23 = 10002 and that would leave room for 0.1, 0.01 or 0.001; 0.01 * 23 = 102. This leads to a more complicated setup for your computer.

#### Subtracting two numbers
An adder with all labeled parts.
The subtraction of numbers is surprisingly simple. The ALU first must change the second number (the value subtracting by) and convert it from a positive number to a negative number. A two's complement is when you invert the binary number (so that all the 0s are 1s and 1s are 0s) and add one to it.

Example: do 10 subtract 9

| 1. 0000 1001 | (9 in binary, we want -9, not 9)                                                                        |
|--------------|---------------------------------------------------------------------------------------------------------|
| 2. 1111 0110 | (Invert 9, so that all 0s are 1s and 1s are 0s)                                                         |
| 3. 1111 0111 | add one (this the two's complement of 9)                                                                |
|              |                                                                                                         |
| 4.           |                                                                                                         |
| 0000 1010    | (10 in binary)                                                                                          |
| +1111 0111   | add two's complement of 9 (aka -9)                                                                      |
| ----         |                                                                                                         |
| 0000 0001    | result (10 + (-9) = 1) (there is an overflow, this just means that the result is not a negative number) |

This poses the complexity of signed numbers.[1] This is a weight to the binary number to assign it as a positive or negative number. Whether the result is a negative or positive number is determined by the overflow flag. If there is an overflow, this means that the number is positive and otherwise, negative.

To implement this, you can ask the ALU to do 3 operations. To do A subtract B, the operations are

Operation: A SUB B

- NOT B
- (set B to) B ADD 1
- (set A to) A ADD B
- RETURN A

#### Multiplying two numbers
Multiplication is repeated addition, so the easiest (inefficiently) is to add A to a variable B amount of times.

Here's pseudomachine code for it

Operation: A * B

- C = 0
- (set C to) C ADD A
- (set B to) B SUB 1
- JUMP IF (B > 0) TO LINE 2
- RETURN C

However, there are more efficient ways of multiplication. A good method is to repeatedly bitshift the first number to the location of each 1 in the second number and sum it.

There are underscores to mark indents, since padding with 0s are less intuitive. subscript 2 means in binary, and decimal numbers are also in bold

| __ __11 | 3 (notice that there are 2 1s)                     |
|---------|----------------------------------------------------|
| x_ 1011 | 11                                                 |
| ----    |                                                    |
| __ __11 | We shift 112by010since the1stbit of 10112is 12     |
| +_ _110 | We shift 112by110since the2ndbit of 10112is a 12   |
| +1 1000 | We shift 112by310since the4thbit of 10112is a 12   |
| ----    | the3rdbit of 10112is 02so we do not add a 112there |
| 10 0001 | 33(result)                                         |

so this is more efficient for larger numbers.

Operation: A * B

- C = 0
- D = 0
- (Set A to) << A (bitshift A to the left)
- JUMP IF (BIT (D) OF B == 0) TO LINE 6
- (Set C to) C ADD A
- (Set D to) D ADD 1
- JUMP IF (D < LENGTH OF B) TO LINE 3
- RETURN C

Don't forget that

<< A (bitshift to the left) is effectively, A * 2

and

>> A (bitshift to the right) is effectively, A / 2

If the numbers are predictable or the CPU must do a lot of similar numbers in bulk, consider using a look-up table to quickly get results to frequently called multiplication. Is this a way of hard-coding your answers and is used in extreme cases.

### 

### 
This is pretty fun, this part.

Elaborating on Chapter 2: Instruction Set, we will be creating one for ours.

For the MASIC Computer, the computer which we are building, has an 8-bit system, so that means each instruction on each slot of the stack memory will be 8 bits. The stack memory is the memory where any information can be stored and is on the RAM. There will be a counter, called the program counter, which increments by 1 every cycle. A cycle is the CPU fetching the instruction, decoding the instruction (finding out what to do with the instruction) and executing the instruction (doing what it tells it to do). Then it moves on to the next one by incrementing the program counter and reading the information at that location in the stack memory.

So each byte in the stack memory has 8 bits for us to work with.

0000 0000

and some instructions require an address, say loading memory into a register so that we can perform operations (such as addition) on it. Each instruction will be split into two parts, each 4 bits. The first is the TYPE. the TYPE will specify what the computer must do and the ADDRESS will be where the value we will perform our operations are located.

OPCODE OPERAND

so 4 bits for the TYPE, we can have 2^4 types, so 16 different ones. Our computer will have two registers, so one bit will be for specifying the register the operation will executing on and is denoted by an x.

Instructions are put in the same place as memory and as the ADDRESS part of the instruction is only four bits, we can only reference memory from 1-16 lines, requiring some clever programming to fit larger programs. Memory is also limited to 16 bytes per program. Values and instructions are essentially the same thing, so if you write an instruction to store it onto a line that previously-stored an instruction, that effectively overwrites the instruction with a value. Accidental execution of values might be a problem, so a STOP command must be used to prevent any errors. This is a whole lot to understand, so good sources are https://www.computerscience.gcse.guru/theory/high-low-level-languages and https://scratch.mit.edu/projects/881462/ <-- really helpful actually. and also don't forget to take both CS and ICT for your IGCSEs.

