# Redstone circuits/Piston
Pistons have allowed players to design circuits that are smaller and/or faster than the standard, redstone-only counterparts. An understanding of standard redstone circuits is helpful, as this tutorial is focused on the circuit design rather than the function.

There are three benefits of piston circuitry:

## Contents
- 1 Principles
- 2 Piston gate designs
	- 2.1 NOT gate
	- 2.2 OR gate
	- 2.3 AND gate
	- 2.4 IMPLIES gate
	- 2.5 XNOR gate
	- 2.6 XOR gate
- 3 Latches
	- 3.1 RS latches
	- 3.2 T flip-flops
- 4 Ring memory
- 5 Clocks
	- 5.1 Rapidfire piston clock
	- 5.2 Alternate rapidfire piston clock
	- 5.3 Pulser
	- 5.4 Rapid fire trap clock
- 6 Edge detector
- 7 Double extender

## Principles
Power and Repeaters View at: Mechanics/Redstone/Piston circuits/Power 1 [edit]

Power is transmitted in several ways that are useful to pistons. The first thing to note is that there are two types of blocks; transparent and solid. Transparent blocks are things such as glass, slabs, or air, while solid blocks are more common materials such as dirt, stone, or wool. 

The key is that redstone power can be transmitted through solid blocks, but not transparent blocks.  However, power can pass through only one solid block at a go, it cannot be passed from one solid block to another.  A solid block can power wire leading from it only if it was "strongly powered" (by a redstone torch, repeater, or comparator, but not by redstone wire). Redstone dust can be placed on some transparent blocks, but then it transmits power only upward, not downward (that is, not through the transparent block).

Redstone torches are considered logic components only if they change states as the gate is used.  (Otherwise they're just power supplies.)  If they change state too often, they are susceptible to burning out.  If a solid block is on top of a redstone torch, any wire connected to the block becomes powered. If, however, the block is transparent, the torch does not power the wires. In Creative mode, using torches as power-supplies for blocks above is mostly deprecated by the introduction of redstone blocks, which are permanently powered. They have a higher cost in Survival, though.

When a repeater is directed at a solid block, it passes power into that block in the same way redstone torches do.  A repeater can also take power from a solid block that is powered, even weakly powered (that is, it turns a weakly powered signal into a strong one).  Power cannot be transmitted by transparent blocks.

Pistons extend if powered, but it's notable that they can take power from the block above them – that is, even if the block is air, if that block would have been powered, then the piston is powered. They can also be powered through their extended piston, which produces several useful quirks that are commonly used in circuits.  A piston can push up to 12 blocks when it extends; however, a sticky piston can pull back only one block when it retracts. Some blocks are immune to being pushed or pulled, notably obsidian and any block with a GUI or inventory (except crafting tables).  Other blocks drop as items if a piston tries to push them; this includes most "attached" blocks such as either sort of torch, or doors, but also a few others such as jack-o-lanterns.

## Piston gate designs
Main article: Logic circuit
Pistons can produce alternate designs for many of the classic logic gates.  Piston gates may also use redstone torches to supply a constant signal (in which case they can often be replaced by levers), or for other purposes.

### NOT gate
Piston NOT gate View at: Mechanics/Redstone/Piston circuits/Piston NOT [edit]
The piston-only NOT gate, also called an inverter, is slightly larger than a standard redstone NOT gate, so it is rarely used alone.  However, it demonstrates an important concept used in many piston mechanisms, namely that torches below solid blocks create a current in any surrounding wire. When an input is triggered, the piston extends, uncovering the torch hole removing the signal from the output line.  The input can power the piston from almost any direction. Alternatively, a block of redstone can be used in to shrink the design.


### OR gate
Piston OR gate View at: Mechanics/Redstone/Piston circuits/Piston OR [edit]
This design is slightly faster than the standard redstone OR gate, with a comparable size.
It uses one piston that covers a torch when extended by any of the inputs.


### AND gate
Piston AND gate View at: Mechanics/Redstone/Piston circuits/Piston AND [edit]
Incredibly fast AND gate. When unpowered, the sticky piston pulls the block over the hole, breaking the circuit.  When powered, it extends and lets the current flow in and out of the hole.  One input feeds the piston, the other feeds the circuit it interrupts; both must be ON to release a signal.


### IMPLIES gate
Piston IMPLIES gate View at: Mechanics/Redstone/Piston circuits/Piston IMPLIES [edit]
Comparable size and speed to some of the basic redstone IMPLIES gate.
This gate represents material implication. Returns false only if the implication A → B is false. That is, if the conditional A is true, but the consequent B is false. It is often read "if A then B." It is the logical equivalent of "B or NOT A".  The torch under the mobile block is in a hole.




### XNOR gate
Piston XNOR gate View at: Mechanics/Redstone/Piston circuits/Piston XNOR [edit]
Pronounced "ex-nor", this device activates when both inputs are equal. A useful attribute is that a XOR or XNOR gate always changes its output when one of its inputs changes, allowing for 2 switches to be combined to open or close a door, or activate another device. This design is significantly smaller than the redstone-only equivalent and slightly faster. Adding a NOT gate to the end or to either input produces an XOR gate, which activates when the inputs are different.


### XOR gate
Piston XOR gate View at: Mechanics/Redstone/Piston circuits/Piston XOR [edit]
Pronounced "ex-or" (a shortening of "exclusive or"), this device activates when only one of the inputs is on. This design, like the XNOR gate, is smaller and faster than the redstone-only equivalent.


## Latches
Main article: Memory circuit
Latches are memory circuits.  Naturally, pistons' ability to physically move blocks to new locations make them a natural tool for these.

### RS latches
Piston RS Latches View at: Mechanics/Redstone/Piston circuits/Piston RS Latches [edit]
The basic piston RS Latch is small and easy to make. The pistons used here are regular pistons, not sticky pistons, and push a block over one of two holes containing a Redstone Torch. One hole can be omitted if only one output is required.  Using a Block of Redstone lets the circuit become even smaller, and adds the inverse output.


### T flip-flops
These T flip-flops use one input to switch between two states. 

Sticky pistons behave strangely when they receive a 1-tick signal. If a block is directly next to the piston, the piston pushes the block but does not pull it back when the signal ends. If the piston receives another 1-tick signal, the piston extends and retract the block. This can be used to toggle the position of blocks. 

Piston Toggle A View at: Mechanics/Redstone/Piston circuits/Piston Toggle A [edit]
Design A, 4×2×4. Uses regular pistons. Both of the pistons are regular pistons. This flip flop is quite fast and quite small. It toggles when the input changes from ON to OFF. Inverting the input increases the speed of the circuit.  


Piston Toggle B View at: Mechanics/Redstone/Piston circuits/Piston Toggle B [edit]
Design B (5×3×2) is actually an RST latch, combining the functionality of both the Set/Reset (RS) and toggle (T) latches.  Uses regular pistons. This flip flop doesn't use torches for logic so it can work with signals of any length.   The dust on level 1 is there to redirect the redstone wire away from block X, which powers the piston.   However, this circuit does not have an inverse output.


Piston Toggle C View at: Mechanics/Redstone/Piston circuits/Piston Toggle C [edit]
Design C is a combination pulse limiter and downward edge detector. When the signal turns off, the first sticky piston retracts the second, which receives a 1-tick signal. The 1-tick signal toggles the mobile block.  It is sensitive to timing.


1-wide Sticky Piston TFF View at: Mechanics/Redstone/Piston circuits/Sticky Piston Compact TFF [edit]
The 1-wide Sticky Piston TFF design is 5×1×3. It depends on the fact that a sticky piston leaves the block after extending when given a short pulse of 0.5 ticks of delay. A circuit breaker is used to give a 0.5 ticks pulse to the sticky piston. This makes the sticky piston leave the redstone block, which then provides power to the output. When powered again, the sticky piston pulls the redstone block switching the output off. It is possible to make this TFF tileable.


## Ring memory

  

This section needs schematic(s) or diagram(s) instead of YouTube video links. 
Please remove this notice once you've added suitable diagram(s) to the article.


A simple ring of blocks, rotated by pistons. The reading head is on the right side of the ring. The rightmost circuit is a clock that drives the pistons
This is a ring of blocks attached to regular pistons at the corners so it can rotate. The blocks are usually a combination of solid and non-solid blocks. The pistons are often connected to a clock so that they rotate the ring. Most (if not all) rings have a reading head consisting of a repeater pointing at the ring and a redstone torch powering the repeater. By using redstone on the other side of a ring, one can see which type of block is in front of the reading head (1 = Solid; 0 = Non-solid). This information now can be passed to a circuit. By using a comparator and reading a cauldron's fill level, 3 additional memory cell states are available. For repeater-based reading heads those act as zeroes.

Adding multiple rings together in a row creates a band. A band stores even more information and works similar to punched tape. Examples include music machines, combination locks, and memory.



## Clocks
Main article: Mechanics/Redstone/Clock circuit
### Rapidfire piston clock
Rapidfire Piston Clock View at: Mechanics/Redstone/Piston circuits/Rapidfire Piston Clock [edit]
This rapidfire clock is fairly simple to build.  It requires 2 non-sticky pistons, 2 repeaters, and 6 redstone, and 5 solid blocks. The repeaters must be set to at least 2 ticks, and they must match.  Place the mobile block last to start the clock, and take output from either end or any wire.  Note that this clock is not switchable, and if it does stop for any reason, it's difficult to restart by a redstone signal.  The player can restart it by breaking and replacing the mobile block, or by changing the repeater delays (both of them; the clock restarts when they match and are set to at least 2 ticks).


### Alternate rapidfire piston clock
Alternate Rapidfire Piston Clock View at: Mechanics/Redstone/Piston circuits/Alternate Rapidfire Piston Clock [edit]
This piston clock is a simple way of repeating a circuit that goes at high speed without burning out. It does not require repeaters or redstone torches. A tutorial is available here. It requies a single sticky piston, one lever, a small amount of redstone, and some solid blocks. From the lever, the redstone has to be placed so it goes up a block, before linking up to the piston. The piston has to be placed in a way that, when it is extended, it blocks the redstone from going up the side of the block without breaking the redstone. This breaks the circuit, removing power from the piston and thus retracting it, causing the circuit to open again. The signals are too fast to affect lighting sources such as lamps and redstone torches. Doors and dispensers both work well at this speed.


### Pulser
Piston Pulser View at: Mechanics/Redstone/Piston circuits/Piston pulser [edit]
A small, stable pulser in a space of 2×3×2.  The period can be adjusted with the repeater, and the clock can be turned off or on with the lever.  (Turning the lever ON stops the clock, and vice versa.)  The lever can be placed on any of the solid blocks.


### Rapid fire trap clock
Another way of doing this is placing a sticky piston with a redstone block on its face and a line of redstone dust connecting the redstone block and the sticky piston. It must be two long to prevent lockup. To make it toggleable, connect the dust with a lever. This is useful for traps.

## Edge detector
A rising edge detector creates a brief signal when the input turns on. Conversely, a falling edge detector creates a brief signal when the input is turned off, and a dual-edge (aka "zero-crossing")  detector responds to both.

Switchable Edge Detector (A) View at: Mechanics/Redstone/Piston circuits/Edge Detector A [edit]
Design A can be a rising- or falling-edge detector depending on the delays of the repeaters.

- For a rising edge, set both repeaters to 1-tick.
- For a falling edge, set the left repeater to four-ticks and the right repeater to one-tick. This creates a 2-tick signal.


Double-Edge Detector (B) View at: Mechanics/Redstone/Piston circuits/Edge Detector B [edit]
Design B is a variant of the piston XOR gate, and a dual-edge detector.  The right-hand repeater can be adjusted to output a longer or shorter pulse.


Inline Edge Detectors View at: Mechanics/Redstone/Piston circuits/Edge Detectors Inline [edit]
Designs D, E, and F are straight-line versions, 1×2×2.  Design D is a rising edge detector; design F, a falling edge detector; both with an output pulse of 2 ticks. Design E is a zero crossing detector, activating on both rising and falling edges. However, it produces only a single-tick pulse output. This can be moderated by adding a 2-tick repeater to the output, producing a 2-tick pulse, same as the other two.


## Double extender
Basic Double Extender View at: Mechanics/Redstone/Piston circuits/Double Extender 1 [edit]
This design pushes and pull a block two spaces instead of one.  The first and second repeaters must be set to delays of 2 and 4 respectively. The pistons are sticky and the device correctly pushes and retracts the block. The main trick is properly sequencing the retraction because the back piston does not pull back the forward piston when it is extended. Additionally, the back piston retract only the forward piston, not the block. To handle these issues the forward piston must be retracted, pulled back, then extended and retracted again.  

Triple extenders and so forth are possible, but involve more complex circuitry. As more pistons are added to the circuit, the logic becomes more complex. In an ideal circuit the extension and retraction of the pistons are governed by the number of pistons, denoted P. Then, the time to extend the pistons equals P ticks. The time to retract the pistons equals 3P−2 ticks. This relationship is linear, and implies that the time for the circuit to execute goes up proportionately with the number of pistons. This relationship is achieved by moving multiple pistons per tick rather than only one at time. This relationship applies to both horizontal and vertical extenders.

Due to the pistons limit to pushing 12 blocks at a time, an 11 piston extender is the largest possible extender. Assuming the design is constructed ideally, this needs 11 ticks to extend and 31 ticks to retract. A player built design would likely use more delays for ease of construction.


Piston-Safe Double Extender View at: Mechanics/Redstone/Piston circuits/Double Extender 2 [edit]
A more advanced (and much larger) circuit can double-push pistons, without extending them (and stopping the system).  This circuit can also can be powered with torches from below, to hide all the wiring.  Either way, input to any of the green-marked squares, so the signal reaches all the way round without needing extra repeaters.  The design can be mirrored to push a pair of pistons on the same switch.


Vertical Double Extender (side view) View at: Redstone_circuits/Piston/Double_Extender_4 [edit]
Vertical double extenders are more difficult to make than horizontal extenders; the release of observers in 1.11, however, has greatly simplified the design of vertical double extenders.
Design A is a 3×3 tileable design that extends upward. Design B is a 4×3 tileable design that extends downward. The repeater in both designs are set to 1-tick.

Longer vertical extenders require complex circuitry, and are often used as elevators. To slightly simplify the required circuits, a gravity-affected block like gravel or sand can be used as the elevator platform. This avoids the need for the top piston to be sticky and for it to execute multiple extensions to pull down the top block at each stage of descent. If more than two pistons are used in total, multiple extensions of lower sticky pistons are still required to pull down the pistons higher in the stack, which are not gravity-affected.




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

