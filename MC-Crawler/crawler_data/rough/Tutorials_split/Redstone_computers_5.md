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

