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

