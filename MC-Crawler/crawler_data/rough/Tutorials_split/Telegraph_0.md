# Tutorials/Telegraph
A telegraph in Minecraft works identically to a real telegraph device, sending a series of redstone pulses over long distances to be decoded and interpreted by a receiving party. There are multiple designs, from the simple flashing redstone torch, to massive machines capable of reviewing, deleting, and editing messages before sending them to their destination. This tutorial will explain how to operate these devices, and how to create your own.

## Contents
- 1 How they work
- 2 Telegraph components
	- 2.1 Sending devices
		- 2.1.1 Lever
		- 2.1.2 Button
		- 2.1.3 Pressure plate
	- 2.2 Receivers
		- 2.2.1 Redstone torch
		- 2.2.2 Redstone lamp
		- 2.2.3 Redstone repeater
		- 2.2.4 Pistons
		- 2.2.5 Note block
	- 2.3 Message displays
		- 2.3.1 Display loops and erasing devices
		- 2.3.2 Erasers
		- 2.3.3 NOR gate
- 3 Types of telegraphs
	- 3.1 One-way telegraph
	- 3.2 Classic telegraph
	- 3.3 Multi-directional telegraph
- 4 Simple multi-directional Morse telegraph
	- 4.1 Single direction
	- 4.2 Multi-directional
- 5 Alternative designs
	- 5.1 Frequency matching
	- 5.2 Analog telegraph
- 6 Redstone clock telegraph
	- 6.1 Steps
	- 6.2 Pros and cons
	- 6.3 Tips
- 7 Bugs

## How they work
All telegraphs, no matter how basic or complex they are, require four things: a sending device, an inverter, redstone wire, and a receiving device. The sender will just about always be in the form of a lever. Anything else, such as a button or pressure plate, cannot be easily used to create a message, as they will remain activated for at least 0.9 seconds. A lever, on the other hand, can be shut off as soon as the player wants to, allowing for the quick pulses needed for telegraph languages such as Morse code. After the sender comes the inverter, a simple logic gate that inverts its input to create the output. For instance, if the input wire is powered, the output wire will be off. These are almost always used in telegraphs because redstone torches (a common type of receiver) create their own power. This means that without an inverter, the torch will turn off when a pulse is sent. Although this is only an issue of appearance, it may lead to confusion during interpretation of the message, which is tricky enough by itself. Then comes the all-important wire, which allows you to send your message as far as you want (although the longer the wire, the more likely it is that something goes wrong). The wire consists of redstone wire, and, depending on its length, redstone repeaters placed on every fifteenth block. This will stretch out for as long as needed, until it reaches its destination; the receiver. Receivers can be anything from a redstone torch that blinks when a single pulse is received to a room filled with redstone repeaters, displaying the entire message before the player.

## Telegraph components
### Sending devices
A lever in a telegraph room.
A sending device is the mechanism used to transmit a series of pulses to the receiver, whether it creates those pulses or simply allows a looping message to enter the telegraph line. It can be one of three objects; a lever, a button, or a pressure plate.

#### Lever
Levers are by far the most common of all sending devices, and are the most practical choice in nearly every scenario. They can create as long or as short a pulse as the sending party wishes, and are the most accurate representations of real life telegraph keys.

#### Button
The only situation that a button could be used is in a one-way telegraph system for distress signals to other players in multiplayer. However, the receiver would not remain activated due to buttons automatically returning to the 'off' position after only 0.9 seconds.
It is also a small target to aim for, especially when a player is in the kind of situation that a distress signal seems like a good idea. So when it comes to telegraphs, use of buttons should probably be avoided entirely.

#### Pressure plate
Although they are similar to buttons in their general impracticality, the player could potentially utilize the pressure plate's unique ability to be activated by mobs. Multiple pressure plates could be positioned at different points of a cave, all of which could be connected to the one-way distress telegraph mentioned earlier. If any mob (only harmful mobs would spawn in a deep cave) stepped on one, it would trigger the distress signal, and players elsewhere would be alerted and be able to take action.

### Receivers
A 6-bit receiver using redstone repeaters.
The receiver is the means of displaying a message sent from another telegraph room. They can be either redstone torches or redstone repeaters.

#### Redstone torch
The redstone torch is a primitive, but compact receiver, displaying each pulse as it arrives from the sender. It does not record, loop or display the entire message, and it cannot be interpreted easily without a solid understanding of the language being transmitted. It is most common in the one-way and classic telegraph systems, where simplicity and instantaneous viewing are most valuable. In addition, they are the only type of receiver that can be wall-mounted. 

#### Redstone lamp
The addition of redstone lamps makes display a lot simpler by eliminating the need for an inverter.

#### Redstone repeater
Redstone repeaters, in their simplest form, can be used like the redstone torch receiver. However, they cannot be sent pulses as quickly or be mounted on walls, making them much more useful when placed in lines of two or more. This allows the receiving party to view a larger portion of the message as it is received, or, if the line is long enough, the entire message. The speed at which each pulse is displayed and lost can be adjusted by right-clicking each redstone repeater. This will increase or decrease the delay on each repeater before it passes on the signal. Such a system can be looped, so that the message is repeated to the receiving party indefinitely (note that looping a received message requires an erasing device and a message no longer than the receiver can display at one time).

In addition to being able to loop, redstone repeaters have the advantage of being able to be "locked" to a state. Thus, if a message is sent in a pre-configured pulse, it's possible to have a pulse preceding the message to lock the message in place in the repeaters, removing the need for a loop, and adding the possibility of a "timed eraser" if executed correctly. To lock a repeater in its current state, a repeater must power the side of it, then locking the current state.

