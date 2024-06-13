# Tutorials/Logic gates
A full adder takes two inputs A and B and a Carry input and produces the Sum and Carry outputs. It relies on two XOR gates, two AND gates, and one OR gate. With some thought, these gates can be compressed (as both AND and XOR gates already exist in the game, and an OR gate can simply be a redstone wire).

A and B are the bit inputs and C' is the carry in. It produces a sum at S and a carry out at C. When full adder modules are tiled together C' and C are connected, which allows the carry to propagate to the next module.

## Contents
- 1 Adders
	- 1.1 Version 1
	- 1.2 In-line adder
	- 1.3 Version 2
	- 1.4 Version 3
	- 1.5 Fast adding
	- 1.6 Piston adders
	- 1.7 4-bit adder
	- 1.8 Alternate 4-bit adder
- 2 Subtracting
- 3 Logic units
	- 3.1 Arithmetic logic unit

## Adders
### Version 1
In-game screenshot of the Full adder
Full adder 1 View at: Tutorials/Logic gates/Full adder 1 [edit]
** Full Adder **
A full adder takes two inputs A and B and a Carry input and produces the Sum and Carry outputs. It relies on two XOR gates, two AND gates, and one OR gate. With some thought, these gates can be compressed (as both AND and XOR gates already exist in the game, and an OR gate can simply be a redstone wire).

A and B are the bit inputs and C' is the carry in. It produces a sum at S and a carry out at C. When full adder modules are tiled together C' and C are connected, which allows the carry to propagate to the next module.


Full Adder Schematic



** Half adder **
The half adder is nearly identical to the full adder, except the second XOR gate is removed and the output from the first XOR gate becomes S. There is no carry in (C'), but the carry out (C) circuit is still on top of the first XOR gate and provides a carry to the first full adder. Some ALUs do not use a half adder for the first bit, to support INCREMENT (allow a carry in on the first bit).


### In-line adder
** Full adder **
In-game screenshot of the 2 wide Full Adder
This full adder is similar to the previous one, except for the fact that it is two wide and the inputs are aligned vertically. This design is great for minimizing horizontal space and can be built in-line with two redstone buses, eliminating the space required to expand a bus to reach the inputs of a wider full adder.


Schematic of the Full Adder



| Tutorial video (view on YouTube) |
|----------------------------------|
|                                  |


### Version 2
** Full Adder **
Gates: XNOR (2), IMPLIES, NOT, OR, AND 
Size: 6×12×5 (including I/O spaces)

This adder takes 2 bits and a carried over bit (actually C, rather than C, a value held in the redstone in the bottom left corner on layer 1) and adds them all together, producing a sum (S) bit and a carry (actually C rather than C).

When using the gates above; mind the inputs and outputs. You may be wondering why there are so many inverted signals being used instead of the regular signal.

The adders shown here use XNOR gates rather than XOR gates because they are more compact, and as a result, implies gates must be used instead of AND gates, which also happen to be more compact.

Therefore, for the most compact adder, inverse signals must be used. These adders are too complex to be easily deciphered with 2 layers per square, so each single layer has been drawn separately to ease the building process.


Schematic of the Full Adder



** Half Adder **
Gates: XNOR, IMPLIES
Size: 5×4×4

This adder takes 2 bits and adds them together. The resulting bit is the output of S (sum). If both bits are 1, there is a carry over, and C becomes 1 (C becomes 0). This half adder can be modified to create a non inverted C output, but this configuration is used so that it can be implemented as the start of a chain of full adders.

Extension:
for those new to advanced redstone like myself, it's easier to understand it like this: let's say output B (C) has a NOT gate that inverts the signal and it leads to an iron door or piston door etc. Output A (S) is connected to sticky pistons controlling the floor. Let's say for sake of argument that there is 1×1×1 block NOT affected by the sticky pistons, this is the safety block. When you activate input A, the door opens and the floor drops, if you're standing on the safety block, then you cannot fall. Input B controls only the floor, but if input A is on then input B controls them both. When both are on, input A affects only the floor. This means if you are off the server and want no one in, leave A and B on, when they deactivate A, the floor drops, but the door stays closed, so if they know the secret, they still cannot get in.


Schematic of the Half Adder



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

## Logic units
In circuits, it might be useful to have a logic unit that determines which output is to be chosen based on its input. Such a unit can then be used for more complex circuits, such as an ALU.

This is an example of a 2-bit logic unit having four states depending on the input.



The outputs are in top row, with 11, 00, 01, 10 order (input order: first first, bottom second).

This is another example of a simplified version using Gray codes. The output appears at the torches at the end of the top rows. This design can be extended to any number of bits, but practical limitations due to timing considerations restrict the use of more than a byte or so. The outputs are triggered by the inputs 11, 01, 00, 10, respectively.



### Arithmetic logic unit

The Arithmetic logic unit (ALU) is the central part of the CPU. It does calculations and logical processing and then passes this information to a register. The ALU, on basis of the input, selects a specific function, performs it, and then gives the result.

The ALU shown below is a 1-bit ALU with the functions: ADD, AND, XOR. It takes the A and B inputs and then performs the selected functions. Read about the adders to see how the ADD function works.
XOR and AND are basic functions that are explained on the logic circuits page.
There can be more functions added to an ALU, like multiplication, division, OR, NAND... etc. These functions could, with some modifications, be added to this 1 bit ALU.

This 1-bit ALU can be linked to each other to create an as many bit ALU as possible.
Just like adders you need to connect the Carry out (Cout) to the Carry in (Cin) of the next ALU


1-bit ALU schematic
This is a screenshot of the actual 1 bit ALU in Minecraft. You can view the ALU in 3D here.




| Redstone circuits & tutorials |                                                                                                                                                                                   |
|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Redstone circuits             | Clock circuits<br/>Components<br/>Logic circuits<br/>Memory circuits<br/>Miscellaneous circuits<br/>Pulse circuits<br/>Transmission circuits<br/>                                 |
| Featured tutorials            | Advanced redstone circuits<br/>Block update detector (BUD)<br/>Comparator update detector (CUD)<br/>Mechanisms<br/>Piston circuits<br/>Quasi-connectivity<br/>Redstone music<br/> |

| Redstone components |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Power               | Block of Redstone<br/>Buttons Wooden Stone Polished Blackstone<br/>Wooden<br/>Stone<br/>Polished Blackstone<br/>Chiseled Bookshelf<br/>Daylight Detector<br/>Detector Rail<br/>Lectern<br/>Lever<br/>Lightning Rod<br/>Observer<br/>Pressure Plates Wooden Stone Polished Blackstone Heavy Weighted Light Weighted<br/>Wooden<br/>Stone<br/>Polished Blackstone<br/>Heavy Weighted<br/>Light Weighted<br/>Redstone Torch<br/>Sculk Sensor Calibrated<br/>Calibrated<br/>Target<br/>Trapped Chest<br/>Tripwire Hook Tripwire<br/>Tripwire<br/> |
| Transmission        | Redstone Wire<br/>Redstone Comparator<br/>Redstone Repeater<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Mechanisms          | Bell<br/>Dropper<br/>Dispenser<br/>Doors Iron Wooden<br/>Iron<br/>Wooden<br/>Fence Gates<br/>Hopper<br/>Jukebox<br/>Note Block<br/>Piston Sticky<br/>Sticky<br/>Rail Activator Powered Detector<br/>Activator<br/>Powered<br/>Detector<br/>Redstone Lamp<br/>TNT<br/>Trapdoors Iron Wooden<br/>Iron<br/>Wooden<br/>Command Block<br/>Structure Block<br/>                                                                                                                                                                                     |
| Other               | Block of Amethyst<br/>Minecart with Chest with Command Block with Furnace with Hopper with Monster Spawner with TNT<br/>with Chest<br/>with Command Block<br/>with Furnace<br/>with Hopper<br/>with Monster Spawner<br/>with TNT<br/>Opaque and transparent blocks<br/>Movable and immovable blocks<br/>Slime Block and Honey Block<br/>                                                                                                                                                                                                      |
| Miscellaneous       | Redstone Ore Deepslate<br/>Deepslate<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Upcoming            | Copper Bulb<br/>Copper Door<br/>Copper Trapdoor<br/>Crafter<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Joke                | Etho Slab<br/>Pickaxe Block<br/>Place Block<br/>USB Charger Block<br/>Floatater<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

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

