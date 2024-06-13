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

