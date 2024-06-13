# Tutorials/Redstone computers
This article aims to examine the design and implementation of redstone computers in Minecraft. This article is extremely complicated, for nerds.

See chapter 1, Tutorial on Building a Computer, for a detailed tutorial on building a computer in Minecraft and how to expand and improve on the example. Does not require any extensive knowledge of computer science. NOT FINISHED. 

See chapter 2, Planning a Redstone Computer, for basic computer concepts of designing and understanding a redstone computer in Minecraft. Does not require any extensive knowledge of computer science.

## Contents
- 1 Overview
	- 1.1 Implementations
- 2 Chapter 1: Tutorial on Building a Computer
	- 2.1 Introduction & Prerequisites
	- 2.2 The MASIC Computer
	- 2.3 Step 1: Memory and Address Decoders (THEORY)
	- 2.4 Step 1: Memory and Address Decoders (PRACTICE)
		- 2.4.1 Address Decoder
	- 2.5 Step 2: Building an Arithmetic Logic Unit (THEORY)
		- 2.5.1 Adding two numbers
			- 2.5.1.1 Fractional numbers
		- 2.5.2 Subtracting two numbers
		- 2.5.3 Multiplying two numbers
	- 2.6 Step 2: Building an Arithmetic Logic Unit (PRACTICE)
	- 2.7 Step 3: Instruction set and machine architecture (THEORY)
		- 2.7.1 Prerequisites
		- 2.7.2 The MASIC Instruction Set
		- 2.7.3 Writing programs
		- 2.7.4 Instruction Cycle
	- 2.8 Step 3: Instruction set and machine architecture (PRACTICE)
- 3 Chapter 2: Planning a Redstone Computer
	- 3.1 Fundamentals of a Computer
	- 3.2 Machine-Architecture
	- 3.3 Computer Data Storage
		- 3.3.1 Primary Storage
			- 3.3.1.1 Registers & Flags
		- 3.3.2 Caches
		- 3.3.3 Random Access Memory (RAM)
		- 3.3.4 Secondary Storage
		- 3.3.5 Tertiary Storage
	- 3.4 Execution Model
		- 3.4.1 Harvard
		- 3.4.2 von Neumann
	- 3.5 Word sizes
		- 3.5.1 Data-Word
		- 3.5.2 Instruction-Word
	- 3.6 Instruction Set
	- 3.7 Architecture of the Computer
		- 3.7.1 Busses
		- 3.7.2 Components
- 4 Tips
- 5 See also
- 6 References

## Overview
Computers facilitate the implementation of ideas that are communicated from humans through programming.

This article will explain the basics of designing and building a computer in Minecraft, assuming the reader is fairly familiar with redstone and computers to a basic level.

 There really is no way of building a computer without knowing how a computer works. The tutorial attempts to explain everything that you need to know but does require a bit of understand here and there of computer science, which is stated in the prerequisites section of each tab. The deepest part we cover is up to IGCSE CS.

All computer systems have at least one processing unit. During operation, processing units execute instructions stored in the computer's memory. For a good start on Minecraft computers you should learn computer science. There are many sources and tutorials to learn computer science but for a basic start, it is recommended to watch Crash Course on Computer Science especially episodes 1–8. Although it isn't completely thorough, it can work as a basis in your understanding of computers.

Most computers in Minecraft are made of redstone dust, redstone torches, and repeaters, leading into sticky pistons or redstone lamps which are controlled using a series of buttons, levers, pressure plates, etc. Other proposed ideas (not covered) are to use hoppers, mine carts, or boats with redstone.

See chapter 1, Tutorial on Building a Computer, for a detailed tutorial on building a computer in Minecraft and how to expand and improve on the given example. It does not require any extensive knowledge of Computer Science as it will be explained but will delve quite deep into it.

See chapter 2, Planning a Redstone Computer, for basic computer concepts of designing and understanding a redstone computer in Minecraft. It does not require any extensive knowledge of Computer Science but will delve quite deep into it.

### Implementations
Computers can be used in many ways, from creating a smart house to using it to run an adventure map. However, due to the limitations of computers in Minecraft, stated below, they remain an abstract concept and serve as good tools to understand lower-level concepts of CPU architecture and embedded systems.

The thing that sets apart computers and calculators are that calculators cannot perform multiple instructions in a row without user input. A computer can compare and assess instructions in a flow to perform tasks. 

However, in Minecraft, they are extremely slow and with their large size, redstone computers are difficult to find practical applications for. Even the fastest redstone computers take seconds to complete one calculation and take up a few thousand blocks of space. Command blocks are far superior to computers in Minecraft because of their speed and legible, higher-level commands.

Mods can change the computer's speed such as TickrateChanger will change the tick rate of the game.

## Chapter 1: Tutorial on Building a Computer
### 
Redstone logic closely reflects simple binary logic, as redstone can be either on or off, and can, therefore, be interpreted as 1s or 0s. We will be referencing in this tutorial, basic binary logic and various simple computer science terms. There is an excellent article which explains binary and conversion to binary. Please read the Architecture of building the Computer section as we will be following that to plan our computer, it is located in this article, thank you. 


This chapter will focus on the application of the knowledge and manipulation of redstone to create a simple 8-bit computer, and will describe how to make one and how it works.

All subjects will be split into (THEORY) and (PRACTICE), THEORY will go in-depth of exactly what will go on. PRACTICE will cover how to build it in Minecraft, what it will look like and possibly world downloads.

The computer we will be building (MASIC Computer)

Step 1: Memory and Address Decoders (THEORY) (NOT FINISHED)

Step 1: Memory and Address Decoders (PRACTICE)

Step 2: Building an Arithmetic Logic Unit (THEORY)

Step 2: Building an Arithmetic Logic Unit (PRACTICE) (NOT FINISHED)

Step 3: Instruction set and machine architecture (THEORY)

Step 3: Instruction set and machine architecture (PRACTICE) (NOT FINISHED)

There are three primary design objectives for a computer in Minecraft, to make your computer most suitable for your task at hand. There are trade offs to consider, such as the larger the computer, the slower it will get because the number of redstone repeaters will increase by distance. The more memory, the less speed and larger size.

** Compactness **
How small is the computer? In Minecraft, designing a survival computer will most likely emphasize on this point. The number of repeats required will increase as size increases.

** Memory **
How much memory can it hold? How many bits and numbers can it count up to? This is important for large-scale computers, say ones which can do more complex algorithms and require larger instruction sets (e.g. doing square roots or trigonometry). The larger the memory size or bit architecture, the more complex the computer will get.

** Speed/Performance **
How fast can it do operations? Is it optimized to run its tasks? Custom designing and building a computer will significantly increase its speed as more redundant wiring and code could be switched to purpose-built hardware and software. This is apparent in some real-world supercomputers which are programmed to run one task very, very efficiently. The speed of computers in Minecraft is very slow, therefore a mod could be installed for the client to significantly increase the speed of the game, and therefore the computer.

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

#### Prerequisites
The section will cover simple topics and components commonly found in a computer, so information from chapter 2 will be used, such as the ALU, RAM, registers and binary manipulation.

#### The MASIC Instruction Set
Since the computer
Here is the first draft of the instruction set, with only essentials. This is based on other assembly languages, but changed to adapt to our architecture. There are two registers, so we need instructions to perform operations on both registers.

| BINARY | OPCODE     | COMMENT                                          |
|--------|------------|--------------------------------------------------|
| 0000   | LOAD R1    | Load the ADDRESS into register 1                 |
| 0001   | STORE R1   | Store contents of register 1 into ADDRESS        |
| 0010   | JUMP R1 IF | Jump to line ADDRESS if register 1 is equal to 0 |
| 0011   | ADD R1     | Add contents at ADDRESS to register 1            |
| 0100   | <<R1       | Bitshift register 1 left                         |
| 0101   | NOT R1     | Bitwise NOT register 1                           |
| 0110   | JUMP       | Jump to line OPERAND                             |
| 0111   | STOP       | Terminate the program.                           |
|        |            |                                                  |
|        |            |                                                  |
| 1000   | LOAD R2    | Load the ADDRESS into register 2                 |
| 1001   | STORE R2   | Store contents of register 2 into ADDRESS        |
| 1010   | JUMP R2 IF | Jump to line ADDRESS if register 2 is equal to 0 |
| 1011   | ADD R2     | Add ADDRESS to register 2                        |
| 1100   | <<R2       | Bitshift register 2 left                         |
| 1101   | NOT R2     | Bitwise NOT register 2                           |
| 1110   | OUT R1     | Outputs register 1                               |
| 1111   |            |                                                  |

To translate:

1000 0011 means LOAD R2 3 because LOADR2 is 1000 and 0011 is 3.

These can be in a process so that functions can be performed.

#### Writing programs
This one does the Fibonacci sequence: (0,1,1,2,3,5,8... etc.)

| FIBONACCI |           |             |                                                                |
|-----------|-----------|-------------|----------------------------------------------------------------|
| LINE      | BINARY    | INSTRUCTION | COMMENT                                                        |
| 1         | 0000 1110 | LOAD R1 14  | set register 1 to 0 (the value at line 14)                     |
| 2         | 0011 1111 | ADD R1 16   | add the value at line 16                                       |
| 3         | 1110 0000 | OUT R1      | output the register                                            |
| 4         | 0001 1111 | STORE R1 16 | put that in line 16                                            |
| 5         | 0011 1110 | ADD R1 15   | add the value at line 15                                       |
| 6         | 1110 0000 | OUT R1      | output the register again                                      |
| 7         | 0001 1110 | STORE R1 15 | now put the output back                                        |
| 8         | 0110 0010 | JUMP 2      | we don't have to reset the register so we loop back to line 2. |
| ...       |           |             |                                                                |
| 14        | 0000 0000 | 0           |                                                                |
| 15        | 0000 0001 | 1           |                                                                |
| 16        | 0000 0001 | 1           |                                                                |

The previous is an example of a low-level assembly language. If it was written in a high level language such as C++, it would look more like this:

#include <iostream>
using namespace std;
int main()
{
    int n, t1 = 0, t2 = 1, nextTerm = 0;
    cout << "Enter the number of terms: ";
    cin >> n;
    cout << "Fibonacci Series: ";
    for (int i = 1; i <= n; ++i)
    {
        // Prints the first two terms.
        if(i == 1)
        {
            cout << " " << t1;
            continue;
        }
        if(i == 2)
        {
            cout << t2 << " ";
            continue;
        }
        nextTerm = t1 + t2;
        t1 = t2;
        t2 = nextTerm;

        cout << nextTerm << " ";
    }
    return 0;
}

#### Instruction Cycle
Rounded squares are components, squares are registers. Green arrows are busses
The instruction set is the lower assembly language, so we want to integrate that more with the hardware side. This revolves around the fetch-decode-execute cycle (explained above).
In the CPU, there will be 4 important registers, 

the Program Counter (PC), 
keeps track of which program the computer is currently on

the Memory Address Register (MAR), 
keeps track of where the next memory location will be

the Memory Data Register (MDR), 
keeps track of what the memory AT the location is

the Current Instruction Register (CIR), 
keeps track of what instruction is currently being worked on

and the ALU Accumulator (ACC), 
keeps track of the input and output from the ALU

There are also four components to keep in mind, the Address Decoder, the memory, the Instruction Decoder and the ALU.


FETCH
The program will get the next instruction.

1. PC sends the instruction number to the MAR
2. PC increments by 1, to prepare for the next instruction
3. Address Decoder decodes the address, and requests information at that address from the memory
4. MDR receives the requested information (in the case of the picture, if the MAR is 0001, it receives 'LOADR1 1')

DECODE
The program will identify what the instruction is

1. CIR receives the information from the MDR, through the information flow
2. Instruction Decoder decodes the instruction and what to do

EXECUTE
The program will execute the instruction

1. In the case of the picture, the program receives 'LOADR1 1' as the instruction, the Instruction Decoder splits the instruction up into the opcode and the operand.

The opcode is 'LOADR1' and the operand is '1'.

1. Operand is sent to the MAR, to get the information at that address
2. MDR receives the information at that address (in the example, it is the same line)

Now four things could happen depending on what the instruction is.

If the instruction is an ADD instruction, the ACC will be told to receive the information from the information flow and the ALU will perform operations on it, outputting it to the ACC again.

If the instruction is a LOAD instruction, the CU will load the instruction to the register.

If the instruction is a STORE instruction, the CU will instead SET the data at the location specified by the MAR in the memory.

If the instruction is an OUT instruction, the CU will send the instruction to the output peripheral.

REPEAT
The instruction cycle repeats itself until it reaches a STOP instruction or runs out of memory

### 
Chapter 2: Planning a Redstone Computer[edit | edit source]
A redstone computer can be planned very much like a real computer, following principles used in computer design and hardware architecture. There are several key design decisions that will affect the organization; the size and performance of your prospective computer should be made concretely prior to the construction of specific components.       

Building a redstone computer will require an understanding of these five concepts and consider the most suitable approach, which would be most practical for your computer.

- Machine-Architecture (Components of a computer, what are they and what they do)
- Execution Model (The organization of components, making them efficient)
- Word Size (How manybitsthe system uses. Usually, powers of 2, around 4, 8, 16 bit is normal in Minecraft)
- Instruction Set (The instructions to be performed by the CPU)

and we will be applying this knowledge and plan the architecture of our CPU in the last section. This CPU will then be built in the next chapter.

### Fundamentals of a Computer
A computer is a machine which has the ability to

- Read and write from a memory which can be addressed
- Perform comparisons on the state of the memory, and perform an operation as a result of that. These operations include rewriting memory.
- Start functions based on content written in the memory. We call such content "programs + data", and the act of writing them programming.

A very notable example of this is the most basic concept of computing, a Turing machine, where the machine will read from one infinite line of code and instruction set in order to complete a function.

Designing and building a Turing machine in Minecraft is possible. This however, is not covered as we will be designing something more basic.

### Machine-Architecture
There are five fundamental components in a basic modern computer. These are essential in order to produce a functioning computer and manipulate data by performing computations. 

five components of a computer
Arithmetic Logic Unit (ALU) (optional, but is normally present)

- Perform adding and subtracting
- Compare booleans using logic gates

Control Unit (CU)

- Perform/Execute instructions sent to it
- Communicate with all components

Data Memory

- Store and return data from memory

Instruction Memory

- Return instructions, sent to the CU
- Can be set, but doesn't need to be as often as the Data Memory

Input/Output devices (I/O)

- Allows the computer to communicate with the world and the player.
- Can input information the computer (button push, daylight sensor)
- Can output information from the computer (redstone lamp, note block)

### Computer Data Storage
There are many methods of storing data, in Minecraft or in real life. The states of memory usually are binary, either on or off and can be computed with boolean logic.

On a computer, there are three types of storage. Keeping in mind that increasing the device's capacity would increase its size, each type would have speed and capacity appropriate to it.

#### Primary Storage
These are the storage which directly accessible to the CPU, referred to as memory and is fastest to access but usually is smaller in capacity for it to be addressed quicker.

##### 
Fastest is the memory stored within the CPU. These are registers and flags as they can be set almost instantaneously and do not require any address sent to it as there is only one byte stored in each register.
Redstone bits that can be toggled are extremely large but can be toggled within 2 ticks. This requires a very large amount of space but is perfect for caches and registers. The redstone is also required for logic gates (not shown) to set the bit, as in the images, sending an input would cause the bit to flip. The gate would take up more space. Registers could also utilize locking redstone repeaters and timing them correctly. This is explained below, in RAM). With the use of a computer clock, it may not be necessary to build registers. Registers are useful when the data goes through the line before either the CU or ALU is ready to process it. It would save it to the register and wait until the CU or ALU can perform its function.




#### Caches
Second to those are caches, which feed information into the processor. In real life, they are separated into levels, each one with separate speed and capacities. It is useful for the same reason as the registers.

#### 
Thirdly is Random Access Memory (RAM), this is much slower than the caches and registers as they have address systems. They are connected to three busses, data bus, control bus and the address bus. The data is sent through the data bus, either setting the RAM or getting values from the RAM. The control bus tells it whether it is being get or set. The address bus tells the RAM where the byte is. Refer to the Architecture of the Computer to understand this more in-depth. RAM is very useful and could fully replace tertiary memory (explained below) because of its non-volatility in Minecraft. Volatile means that when power is lost, it will lose information. The RAM will not lose information unlike in real life, and therefore in an excellent method of storing information.

The RAM in the first case is utilizing the locking redstone repeaters with the correct timing. This requires a bit of a plan but is very space-efficient. The conversion of a bus to the lines in order to lock the redstone repeaters also requires setting timings. This is time-consuming, much more than the registers, however, it is very compact and efficient. The address bus (green) would turn in binary to unlock a certain byte, either to be read or set by the control bus (second line, on the left).



Most often, making it volatile has no use in Minecraft, so the easiest way to make some is to use d-flip-flops and to add a reading and writing function. The bottom image shows instead of locking repeaters, it uses d-flip-flops which is much more space inefficient but simpler to build. D-flip-flops work more or less like locked repeaters, one input, if on, unlocks in until the input is off and the other will set it once unlocked. The output can be read as a bit and with a NAND gate, be ignored or put onto the bus. This is gone over in detail in the second chapter, Tutorial on building a Computer. Excuse the texture pack.



Random Access Memory also known as RAM is a kind of memory used by programs and is volatile. Volatile means that when the power is lost, it will lose information. Most often, making it volatile has no use in Minecraft, so the easiest way to make some is to use d-flip-flops and to add a reading and writing function.

#### Secondary Storage
These are equivalent of HDDs and SSDs. There is a very compact storage technique, involving redstone comparators with the ability to store up to 1KB, being practically sized.

#### Tertiary Storage
Third and last, is a tertiary memory, which requires a lot of time to read/write but can hold massive amounts of information at the expense of speed. Real-world tertiary storage use a mechanism of mounting the memory which takes about a minute for each drive. This is used for archival purposes and for memory which is rarely used. In Minecraft, a system where shulker boxes are used and block in the shulker boxes must be sorted out by a sorting system to represent a form of data. This can also be used to create removable storage. The read/write speed is fairly slow due to the massive amount of comparators and a lot of time is required. The aforementioned mods could speed up tick rate and eliminate this problem, however. This is used for storing long-term data that needed to be loaded at the beginning of a program or rarely due to its poor read/write speed and large capacity. This is the equivalent of a real computer's hard disk or solid-state drive.

### Execution Model
The technique of storing blocks of instructions called programs within memory is what allows computers to perform such a variety of tasks.

The apparatus employed by a computer for storing and retrieving these programs is the computer's Execution Model.

Two of the world's most successful execution models, Harvard and von Neumann, run on nearly 100% of the computers available today.

 This is more advanced, and is for inquisitive and curious readers

#### Harvard
The Harvard architecture physically separates the apparatus for retrieving the instructions which make up an active program from that of the data access apparatus which the program accesses during execution. 

Programs written for computers employing a Harvard architecture may perform up-to 100% faster for tasks that access the main memory bus. Note however that certain memory circuitry is necessarily larger for those who select a Harvard architecture. Harvard architecture is very important.

#### von Neumann
The von Neumann architecture uses a two-step process to execute instructions. First, the memory containing the next instruction is loaded, then the new instruction just loaded is allowed to access this same memory as it executes; using a single memory for both program and data facilitates Meta-Programming technology like compilers and Self-modifying Code.

The von Neumann architecture was the first proposed model of computation and almost all real-world computers are von Neumann in nature.

### Word sizes
Word-size is a primary factor in a computer's physical size.

In Minecraft, machines from 1-bit all the way up to 32-bits have been successfully constructed.

Common word-size combinations:

| Data | Instruction |
|------|-------------|
| 4    | 8           |
| 8    | 8           |
| 8    | 16          |
| 16   | 16          |

#### Data-Word
The amount of information a computer can manipulate at any particular time is representative of the computer's data word-size.

In digital binary, the computer's data-word size (measured in bits) is equal to the width or number of channels in the computer's main bus.

Data-Words commonly represent integers or whole numbers encoded as patterns of binary digits.

The maximum sized number representable by a Binary encoded integer is given by 
2data-word width in bits - 1.

For example, a computer with a data-word size of 8-bit will have eight channels on its bus (set of wires, connecting components) and therefore, we can count up to (28 - 1). 255. Counting further than 255 is not possible with eight bits, as the operation 255 + 1 carries over a one, which requires a ninth bit or what is called a binary overflow will occur, returning 0 as the answer, which is incorrect.

This is simply visualized;

|   | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 255 |
|---|---|---|---|---|---|---|---|---|-----|
| + | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1   |
| = | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0   |

Some common Integer data sizes are:

| Max Representable Number | Number of Bits Required |
|--------------------------|-------------------------|
| 1 = (21- 1)              | 1                       |
| 7 = (23- 1)              | 3                       |
| 15 = (24- 1)             | 4                       |
| 255 = (28- 1)            | 8                       |
| 65535 = (216- 1)         | 16                      |
| 4294967295 = (232- 1)    | 32                      |

Data-Word size also governs the maximum size of numbers which can be processed by a computer's ALU (Arithmetic and Logic Unit).

#### Instruction-Word
The amount of data a computer needs in order to complete one single instruction is representative of a computer's instruction word-size.

The instruction-word size of a computer is generally a multiple of its Data-Word size, This helps minimize memory misalignment while retrieving instructions during program execution.

### Instruction Set
This is a collection of instructions the control unit (CU) can decode, and then execute.

Instructions are essentially functions run by the computer, examples of instructions include:

- Add, subtract, multiply and divide
- Read/Write from RAM/ROM/tertiary memory
- Load and unload data into the RAM
- Branching to other parts of the code
- Comparing registers
- Selecting alogicfunction (NAND, NOR, NOT etc.)

Instructions can be programmed into the RAM, loaded from ROM or directly activated by using a lever or button. Each instruction would have its own specific binary string assigned to it (e.g. 0000=Load data from register 0001=add A and B 1011=Save RAM into tertiary memory etc.) and would probably require its own binary to decimal or binary to BCD to decimal encoders and buses to the ALU/registers.

### Architecture of the Computer
Inside the computer, there is a Central Processing Unit (not to be confused with the Control Unit (CU), a component inside the CPU), which in real life, is a very small and powerful component that acts as more or less, the brain of the computer.
In Minecraft, it is difficult to compact it to the scale we see in real life so don't worry if it looks wrong.

We will first be designing our 4-bit Central Processing Unit in the next chapter, as it is the most important thing in our computer with the Execution Model (the method of communication and organization of the CPU) in mind, (talked about in this page, before, in the Execution Model section) we can map out the construction of the computer.

Map of the CPU, based on the Havard Execution Mode
The CPU follows a cycle four steps, fetch, decode, execute and (sometimes) stores to perform instructions. The CPU first fetches the instruction from RAM, decodes what it means (the instruction will most likely be a number, and the CPU must find out what number it is), and once it understands what the instruction is, it will perform that action. This sometimes requires the data to be put back into the storage, therefore it will store the data. The cycle is then repeated.

#### Busses
There are five busses in the CPU, each to carry information from one component to the next. Busses are channels of redstone connecting each component. Since we are building a 4-bit computer, we only need four channels in our bus. These are the red and blue lines connecting the components inside the CPU. Notice that the blue buses have less than four lines, this is because they do not carry data. Since busses can only carry data one way (in Minecraft, due to repeaters only working one way), there are two buses connecting the CPU to the outer computer.

The first bus is the data bus, this is to transfer information from the storage or I/O devices to the CU. Instructions are also sent through this line The CU can also use this bus to transfer data to the ALU. The ALU cannot transfer data onto this bus because buses only work one way and once the information is taken by the ALU, the bus cuts off beyond the ALU. Information from the ALU is passed through bus 2.

The second bus is the data bus, but returns the data from the ALU to the CU. The CU cannot send data through this bus to the ALU because the bus goes from left to right and works in one direction only. The CU can send information back to the storage units though, and is used to set values of storage devices.

The third bus is the address bus, which the CU can send the address of storage. This is where the information resides. For example, the CU asks for the address of the byte living in 0001. It sends the address (0001) through the address bus and the RAM will return the value of the byte through the first bus. 0001 is the location of the byte, not the value of it.

The fourth bus is the control bus, which the CU will communicate with the RAM with. For example, one wire could tell the RAM to set the byte to the value to the data sent to it by the CU. Another wire could tell the RAM to get the byte from the address sent to it by the CU.

The fifth bus is another control bus, linking with the ALU, which sends flags from the ALU. Flags are notes which could be error messages. For example, the CU could ask the ALU to add 15 and 1 in a 4-bit system. Adding 15 and 1 in 4 bits would yield 0 (explained above) and this is called a binary overflow. This is an error and the ALU will tell the CU about this through the fifth bus as a flag. The CPU could also send data to the ALU and ask for it to perform an action with that data.

#### Components
Control Unit (CU) will fetch instructions from the instruction ROM (for other computers, instructions can be changed and therefore is RAM. For our case, we are running a fixed program and do not need to change the instructions. This simplifies the process entirely and the instruction is Read-Only Memory (ROM)). Inside the CU, it will then decode the instruction, which is normally a number, into a sensible action. It will then perform that action and if the instruction requires, store the result into the RAM. It communicates with the RAM through the control bus and receives flags from the ALU. It can also ask the ALU to perform actions on data it sends to the ALU (e.g. addition). To communicate with the RAM, for example, one wire could tell the RAM to set the byte (the location of it is specified through the third, address bus) to the value to the data sent to it by the CU through the second, data bus.

Arithmetic logic unit (ALU) will execute instructions sent to it from the CU and will compare binary numbers and communicate with the Control Unit. It can do simple addition and subtraction which can be repeated to do multiplication and whole-number division, outputting a whole number (then division). There are also logic gates for booleans, the fundamental logic gates are required, such as the NOT gate and the NAND gate.

Now we can choose from a range of designs of busses, each contributing to the aforementioned three key designing goals of a Minecraft computer.

## Tips
- The player may want to use mods or data packs like WorldEdit.
- Color code your computer (use blue wool or concrete for RAM, yellow for the ALU, etc.)
- Start small, and get the hang of small computers before you try more complex machines.
- Structure blockscan be very helpful for moving components around, and combining multiple components together. However, note that these cannot be obtained without usingcommands.

