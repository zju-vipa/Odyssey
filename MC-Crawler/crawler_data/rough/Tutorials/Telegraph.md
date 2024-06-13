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

#### Pistons
Pistons can be used in multiple bit receivers so that they look like dots and dashes.

#### Note block
When coupled with an inverted rapid pulser, note blocks can be used for an auditory means of displaying messages (the inverted pulser is required in order to tell dots and dashes apart).

### Message displays
Message displays are basically receivers are able to be viewed by the sender. Using these, one can view their message before it is sent to its destination. Either redstone torches or redstone repeaters can be used, usually corresponding to the type of receiver in the other telegraph room. When using a series of connected redstone repeaters, one can upgrade the display with a loop and eraser system.

#### Display loops and erasing devices
A 12-bit receiver with a loop and eraser system.
A display loop is a useful addition to both receivers and message displays. It connects the end of a redstone repeater display to its beginning, showing the message again and again until the eraser is activated. Erasing devices are an absolute necessity when creating a display loop. They end the looping message, and allow a new one to be shown before the two messages overlap pulses. A full loop and eraser system requires a customized NOR gate, through which the message is transferred and looped.

#### Erasers
An erasing device, though it can be as simple as an exposed, destroyable piece of the loop, is generally a lever wired to the custom NOR gate. Although they do take extra space, receiver loops should be built so that the input is on the opposite side of the NOR gate, so that no wires should have to cross paths. Also, remember, you can always use multiple levels of wire to avoid other parts of the telegraph.

#### NOR gate
A NOR gate can be used in holding loops until you wish to send, delete or edit the message. You have to pull both levers back in order to activate it. Having both levers forward or one forward and one backwards will not activate the redstone torch.

## Types of telegraphs
### One-way telegraph
A one-way telegraph with a redstone torch receiver.
Example of one-way telegraph use.
As indicated by the name, messages created in a one-way telegraph may only be sent in one direction, greatly limiting its capabilities. The schematic shown demonstrates a short configuration, complete with the required sender (1), inverter (2), wiring (3) and receiver (4). However, it is the only kind of telegraph with any real practicality in single player. If one were to have the sender in a mine, and the receiver in their house, they could effectively use it like a post-it stamp, leaving a message in their house to remind them, for example, that there was diamond in that mine. Expanding on this idea, they could have a series of redstone torches in their home indicating which of their mines had diamond or some other valuable element. Whenever another mine was discovered to have this element, they could simply flip a switch, and the mine's corresponding torch would activate in the house. An example of this is shown on the left. Another use would be as a simple distress signal in multiplayer, as it is always an issue of having to simultaneously type your call for help and run away from whatever is troubling you.


### Classic telegraph
A typical classic telegraph room.
A two-way telegraph with control rooms on both sides.
The most basic system, the classic telegraph is quite easy to build, but not so easy to use. It consists of one lever, one inverter, and one redstone torch for each direction of communication. The schematic of a simple two-way telegraph is shown on the right. 1 and 2 are small control rooms, and A and B are inverters. Note that the area in between the two inverters can be elongated, with appropriately spaced redstone repeaters. The classic telegraph allows for a speedy construction and a space as small as 1×2×2 for each control room. In addition, due to its limited size and capability, it requires little to no knowledge of logic gates or circuitry, making it ideal for beginners or when you're low on redstone. The downside is that while you may be new to Minecraft, you have to be remarkably fluent in whatever language you decide to send the telegram in. This goes for the receiving party as well. In fact, they must begin reading the message the instant you begin sending it, or risk losing its meaning entirely. This quickly becomes problematic, especially when the server is lagging. Despite this, players use it anyway, often because they enjoy the great similarity it holds to real telegraphs. So while the classic telegraph is compact, simple, and highly realistic, it may be worthwhile to look into a more advanced system.


### Multi-directional telegraph
A three-way telegraph room with a 'send to all' switch.
Although the classification spans most telegraph types, the multi-directional telegraph is quite unique in its general design, and can be challenging to configure. This is mainly due to the amount of wiring required, and, in turn, the amount of space needed. For instance, a three direction telegraph requires a minimum of six separate lengths of wire, and that's just to create a classic one-torch receiver system, with no additional capabilities. While this is less of a problem over short distances, acquiring the massive quantities of redstone needed for such a project can be problematic, and it is good practice to make a rough estimate of how much you'll need before beginning its construction.



## Simple multi-directional Morse telegraph
This is a really simple Morse code receiver and sender. The redstone lamp aligned near the lever shows what the sending is, and the lamp in the wall on layer 1 is the receiver. The signs are to show which telegraph room is receiving the message. Build a mirror of the structure to complete a multi-directional Morse telegraph sender and receiver room. The redstone on the floor is the sender and the line on the slab is the receiver.

- Structure starts above ground
- Slabs are on upper section
- Levers hooked onto top wall

### Single direction
Layer 1






































Layer 2






































Layer 3






































Layer 4



































Layer 5




































### Multi-directional
Layer 1































































Layer 2
































































Layer 3

































































Layer 4

















































Layer 5
















































A multi-directional telegraph room in use from outside and inside
## Alternative designs
### Frequency matching


This device allows you to transmit different signals without any modification to the transmission line (it can remain a combination of redstone wires and repeaters). In this system, different frequencies represent different signals.

To build this circuit, you should build a transmitter — a simple oscillator — and attach it to the transmission line with a repeater. At the other end of the line, build another oscillator with the same delay. Configure the output of the transmission line in order to match the oscillators (they should turn on and off exactly at the same time, this is very important). 

Then, connect the receiver oscillator and the output of the transmission line to a comparator in subtraction mode. If the received waveform is different from the receiver oscillator waveform, the comparator will generate a blinking signal at its output.

You can connect the transmission line to different receivers with different frequencies, and don't forget to match the timing. 

The receiver circuit might get bulky, but this system allows you to spend much less redstone on the transmission line, if you have the transmitter and the receiver far away from each other.

### Analog telegraph
Analog transmission line
Analog telegraph uses up to 16 states of a redstone wire, instead of just two. Animation on the left is pretty self-explanatory: connect the repeaters as shown. The distance between the matching repeaters should be exactly 15. 

## Redstone clock telegraph
### Steps
1. First you need to make a building, at smallest 16 blocks by 5 blocks, and if you want, you can make it look like a realistic building in real life, such as a post office.
2. Next, make a long hole in a wall. It must be 12 blocks long for a building 16 by 5 (If you made a building bigger, leave four blocks on the wall or make space somewhere else). Youmusthave space for four blocks.
3. Place repeaters along the hole on full delay.
4. Hook up to aredstone clock(the bigger the better). A good way to save space is to go up and down repeatedly in rows. That will be the storer.
5. The next thing to build is the sender. Place aleveron one of the spaces. So that you can remember that this is the sender, it is recommended to place a sign on top of the lever saying sender.
6. After that, make a line of repeaters on full delay to the other telegraph office (A good way to do this is to go back and forth between solid blocks and repeaters). To make a turn, place a block, and then place a repeater facing towards the place. Hook up to the redstone the clock on the other one telegraph office.
7. To use the sender, do it inMorse code. To make a dot, turn the telegraph on and off as fast you can. To make a dash, turn on, count to three, and then turn off again.
8. The next thing to build is the deleter. Place blocks in the clock with sticky pistons touching them when on, so you can take them out of the clock stopping the pulse. (Make the sticky pistons so that it won't break things, but just take the block out.)
9. The final thing to build is the canceller. If you were to send a telegraph, make a mistake, and want to stop it from sending, just make a deleter. It's good to make plenty up the track, as with the clock.

### Pros and cons
** Pros **
- Can leave messages.
- Fast.
- Easy to use.

** Cons **
- Needs lots of repeaters.
- Morse code needed.
- Lags a fair bit (A good way to stop this is to keep it well lit in the redstone clock.)
- Needs a large clock to do 7 letter words.

### Tips
- Write the Morse code equivalent to each letter in the alphabet on a piece of paper.
- Place signs on top of levers.
- A nice touch is to hook note blocks up to the line, not the clock.
- Make more clocks to take more messages.

## Bugs
If the telegraph goes outside the loaded chunks, it will not work, as redstone repeaters (needed to maintain signal) will not update (tested in 1.18.1), however this is the most important use for the telegraph, as no visual signals can be given. This can be fixed to setting custom ticking areas.

| Introductory      |                                                                                                                                                                           |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Basics            | Menu screen<br/>Game terms<br/>                                                                                                                                           |
| Newcomer survival | The first day/beginner's guide<br/>The second day<br/>The third day<br/>Hunger management<br/>Things not to do<br/>Simple tips and tricks<br/>Your first ten minutes<br/> |
| Shelters          | Best biomes for homes<br/>Best building materials<br/>Building and construction<br/>Navigation<br/>Shelters<br/>Shelter types<br/>                                        |

| General                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| General                    | Achievement guide<br/>Advancement guide<br/>Best enchantments guide<br/>Breaking a fall<br/>Breaking bedrock<br/>Combat<br/>Complete main adventure<br/>Creating a village<br/>Downgrading<br/>Dual wielding<br/>End survival<br/>Exploring caverns<br/>Gathering resources on peaceful difficulty<br/>Getting food quickly<br/>Headless pistons<br/>Hitboxes<br/>Horses<br/>Indestructible end crystals<br/>Mapping<br/>Measuring distance<br/>Minecraft in education<br/>Mining Diamonds Fossils Ancient Debris<br/>Diamonds<br/>Fossils<br/>Ancient Debris<br/>Nether hub<br/>Nether portals<br/>Nether survival<br/>Organization<br/>Pillar jumping<br/>Playing with a controller<br/>PvP PvP bases<br/>PvP bases<br/>Spawn-proofing<br/>Summoning jockeys<br/>The Void<br/>Time-saving tips<br/>Thunderstorm survival<br/>Units of measure<br/>Village mechanics Trading<br/>Trading<br/>X-ray glitches<br/> |
| Enchanting<br/>andsmelting | Enchanting mechanics<br/>Anvil mechanics<br/>Automatic smelting<br/>Manual smelting<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

| Challenges                |                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| General                   | Acquiring a conduit<br/>Curing a zombie villager<br/>Defeating temples<br/>Defeating a village raid<br/>Defeating a Nether fortress<br/>Defeating a bastion remnant<br/>Defeating a monster room<br/>Defeating a pillager outpost<br/>Defeating a woodland mansion<br/>Defeating a monument<br/>Defeating an End city<br/>Defeating the Ender dragon<br/>Defeating the Wither<br/>Exploring an ancient city<br/>Obtaining every music disc<br/> |
| Non-standard<br/>survival | Adventure survival<br/>Half hearted hardcore<br/>Hardcore mode<br/>Surviving in a single area indefinitely<br/>Infinite desert survival<br/>Island survival<br/>Manhunt<br/>Mob switch<br/>Nomadic experience<br/>Skywars survival<br/>Superflat survival<br/>Flat survival<br/>Ultra hardcore survival<br/>                                                                                                                                    |
| Challenge maps            | Beating a challenge map<br/>Creating a challenge map<br/>                                                                                                                                                                                                                                                                                                                                                                                       |

| Constructions |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Constructions | Adding beauty to constructions<br/>Airlock<br/>Architectural terms<br/>Building a cruise ship<br/>Building a metropolis<br/>Building a rollercoaster<br/>Building safe homes<br/>Building water features<br/>Color palette<br/>Creating shapes<br/>Defense<br/>Desert shelter<br/>Elevators<br/>Endless circling pool<br/>Furniture<br/>Glazed terracotta patterns<br/>Making nice floors<br/>Pixel art<br/>Ranches<br/>Roof types Curved roofs Roof construction guidelines Roof decorations<br/>Curved roofs<br/>Roof construction guidelines<br/>Roof decorations<br/>Secret door<br/>Settlement guide<br/>Underwater home<br/>Walls and buttresses<br/>Water gate<br/>Water-powered boat transportation<br/> |
| Blockbreaking | Blast chamber<br/>Igniting TNT underwater<br/>Wither cage<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

| Farming        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Blocksanditems | Amethyst<br/>Armor<br/>Azalea<br/>Bamboo<br/>Basalt<br/>Bedrock<br/>Blaze rod<br/>Bone meal<br/>Cactus<br/>Chorus fruit<br/>Clay and mud<br/>Cobblestone<br/>Cocoa bean<br/>Copper<br/>Crops (Beetroot, Carrot, Potato, Wheat)<br/>Dirt<br/>Dragon's Breath<br/>Dripstone<br/>Egg<br/>Fern<br/>Fish<br/>Flower<br/>Froglight<br/>Glow berries<br/>Glow ink sac<br/>Glow lichen<br/>Goat horn<br/>Gold<br/>Hanging roots<br/>Honey<br/>Ice<br/>Iron<br/>Kelp<br/>Lava<br/>Meat<br/>Moss block<br/>Mushroom<br/>Music disc<br/>Nautilus shell<br/>Nether growth<br/>Nether vine<br/>Nether wart<br/>Obsidian<br/>Powder snow<br/>Pumpkin, Melon<br/>Rooted dirt<br/>Sculk growths<br/>Scute<br/>Seagrass<br/>Sea pickle<br/>Snow<br/>Soul soil<br/>Sugar cane<br/>Sweet berries<br/>Tree<br/>Trident<br/>Vine<br/>Villager trading hall<br/>Wither rose<br/>Wool<br/>Duplication<br/> |
| Mobs           | Mob farming<br/>Mob grinding<br/>Monster spawner traps<br/>Allay<br/>Animals<br/>Axolotl<br/>Blaze<br/>Cat<br/>Cave spider<br/>Creeper<br/>Drowned<br/>Ender dragon<br/>Enderman<br/>Frog<br/>Goat<br/>Guardian<br/>Hoglin<br/>Iron golem<br/>Magma cube<br/>Phantom<br/>Piglin bartering farm<br/>Raid<br/>Shulker<br/>Slime<br/>Squid<br/>Turtle<br/>Villager<br/>Wandering trader<br/>Warden<br/>Witch<br/>Wither<br/>Wither skeleton<br/>Zombie<br/>Zombie villager<br/>Zombified piglin<br/>                                                                                                                                                                                                                                                                                                                                                                                   |

| Mechanisms            |                                                                                                                                                                                                                                                                                                                                                                  |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Basicredstone         | Automatic respawn anchor recharger<br/>Basic logic gates<br/>Combination locks<br/>Command block<br/>Flying machines<br/>Hopper<br/>Item sorting<br/>Item transportation<br/>Mechanisms<br/>Observer stabilizer<br/>Randomizers<br/>Redstone music<br/>Redstone tips<br/>Rube Goldberg machine<br/>Shulker box storage<br/>Villager trading hall*Water tram<br/> |
| Detectors             | Block update detector<br/>Comparator update detector<br/>Daylight detector<br/>                                                                                                                                                                                                                                                                                  |
| Minecarts             | Train station<br/>Minecarts Storage Storage system<br/>Storage<br/>Storage system<br/>                                                                                                                                                                                                                                                                           |
| Traps                 | Snow golems<br/>TNT cannons<br/>Trapdoor uses<br/>Trap design<br/>Traps<br/>                                                                                                                                                                                                                                                                                     |
| Pistons               | Piston uses<br/>Piston circuits<br/>Quasi-connectivity<br/>Zero-ticking<br/>Instant repeaters<br/>                                                                                                                                                                                                                                                               |
| Advanced<br/>redstone | Advanced redstone circuits<br/>Arithmetic logic<br/>Calculator<br/>Command stats<br/>Hourly clock<br/>Morse code<br/>Printer<br/>Redstone computers<br/>Redstone telegraph<br/>                                                                                                                                                                                  |

| Servers      |                                                                                                                                                                                                                                                                      |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| General      | Playing on servers<br/>Multiplayer Survival<br/>Spawn jail<br/>Griefing prevention<br/>Joining a LAN world with alternate accounts<br/>                                                                                                                              |
| Server setup | Setting up a server<br/>Server startup script<br/>FreeBSD startup script<br/>OpenBSD startup script<br/>Ubuntu startup script<br/>Setting up a Hamachi server<br/>Setting up a Minecraft Forge server<br/>Setting up a Spigot server<br/>Ramdisk enabled server<br/> |

| Technical                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Technical                   | Improving frame rate<br/>Minecraft help FAQ (IRC channel)<br/>Running the data generator<br/>Update Java<br/>                                                                                                                                                                                                                                                                                                                                            |
| Maps                        | Custom maps<br/>Map downloads<br/>Command NBT tags<br/>Falling blocks<br/>Updating old terrain using MCEdit<br/>                                                                                                                                                                                                                                                                                                                                         |
| Resource packs              | Creating a resource pack<br/>Loading a resource pack<br/>Sound directory<br/>                                                                                                                                                                                                                                                                                                                                                                            |
| Data packs                  | Creating a data pack<br/>Installing a data pack<br/>Custom world generation<br/>                                                                                                                                                                                                                                                                                                                                                                         |
| Creating<br/>Minecraftmedia | Creating videos<br/>Livestreaming<br/>                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Game installation           | Installing snapshots<br/>Installing Minecraft Preview and beta versions<br/>How to get a crash report<br/>Installing Forge mods<br/>Custom Minecraft directory<br/>Playing and saving Minecraft on a thumb drive<br/>Playing and saving Minecraft on a thumb drive with the old launcher<br/>Recover corrupted saved world data<br/>Run Minecraft through Google Drive<br/>Save game data to Dropbox (world data only)<br/>Saved data Dropbox guide<br/> |

| Outdated |                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Outdated | Building micro shelters<br/>Custom texture packs<br/>Door-based iron golem farming<br/>End of light mob farms<br/>Far Lands<br/>How to get a crash report<br/>Installing mods<br/>Man-made lake<br/>Managing slimes in superflat mode<br/>Minecart booster<br/>Potion farming<br/>Repeater reboot system<br/>Survival with no enabled data packs<br/>Update LWJGL<br/>Update Minecraft<br/>Village chaining<br/>Water ladder<br/> |

