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

