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


