# Tutorials/Quasi-connectivity
Quasi-connectivity is a property of dispensers, droppers, and pistons that allows them to be activated by anything that would activate the space above them, no matter what is actually in that space. While quasi-connectivity can be difficult to work around sometimes and might seem like a bug, it was a bug, but now it  is officially recognized as a feature that "works as intended" and does make some builds much easier (for example, piston walls).

"Quasi-connectivity" means the block's activation is quasi-connected to the space above itself ("quasi-" means "seemingly" or "apparently"). Quasi-connectivity can be abbreviated as QC. Other terms used for this property include "connectivity", "piston connectivity" (as the property originated with pistons), "indirect power" (but that term is also sometimes used for activating mechanism components with an adjacent powered block), and "BUD-powered" (although quasi-connectivity and block update detectors are not synonymous).

Rather than repeating "dispensers, droppers, and pistons", this tutorial discusses only pistons, but everything discussed here applies to dispensers and droppers as well.

## Contents
- 1 Activation by normal methods
- 2 Activation by quasi-connectivity
	- 2.1 Immediate QC activation
	- 2.2 Update QC activation
- 3 Benefits of quasi-connectivity
	- 3.1 More activation options
	- 3.2 Remote activation
	- 3.3 Block update detectors
	- 3.4 Torch keys
	- 3.5 Floating button
- 4 Drawbacks of quasi-connectivity
	- 4.1 Workarounds

## Activation by normal methods
Activation of Mechanism Components — Mechanism components can be activated by power components (for example, redstone torches), powered blocks, redstone dust, repeaters, and comparators (not shown), but only if configured correctly.
Before discussing activation by quasi-connectivity, let's review more general methods of activation.

Mechanism components (pistons, doors, redstone lamps, etc.) can be activated, which causes the mechanism component to do something (push a block, open the door, turn on, etc.). Most Minecrafters would just say they are "powered", but it can be useful to distinguish powered and activated.

All mechanism components are activated by:

- an adjacent activepower component, including above or below

Exceptions:a redstone torch does not activate a mechanism component it is attached to, and a piston is not activated by a power component directly in front of it
Examples:Redstone torches don't power blocks that aren't above them, but can activate mechanism components in any space next to them. Levers and buttons don't power blocks they aren't attached to, but can activate mechanism components in any space next to them.
- an adjacentpowered opaque block(either strongly-powered or weakly-powered), including above or below

- a poweredredstone comparatororredstone repeaterfacing the mechanism component

- poweredredstone dustconfigured to point at the mechanism component (or on top of it, for mechanism components that can support redstone dust, butnotbeneath it), or adjacent "directionless" redstone dust; a mechanism component isnotactivated by adjacent powered redstone dust that is not configured to point at it.


## Activation by quasi-connectivity





















Quasi-Connectivity — Anything that would activate the lamp can also activate the piston, even if the lamp isn't there.
In addition to the normal methods of activation described above, pistons can also be activated if one of the methods above would activate a mechanism component in the space above the piston, even if there is no mechanism component there (even if the block above the component is air or a transparent block).

Another way to look at it is that pistons have an activation "shape"/"hitbox" similar to doors. Anything that activates the top of a door also activates the bottom of the door, and anything that activates the space above a piston also activates the piston.

This method of activation is known as "quasi-connectivity" (QC) and is often simplified to saying that pistons can be powered by blocks diagonally above or two blocks above, but other methods of such activation exist (described below).



















The Update Problem — The lever can activate the piston by quasi-connectivity, but is too far away to update the piston when it changes.
Where quasi-connectivity gets complicated is that it can cause states where a piston should be activated by QC … but doesn't know it. When redstone components change their state, they update other redstone component around them of the change so that they can update their state in response (for example, when a lever turns on, it updates nearby components that they should now be powered or activated). However, redstone components only update other blocks a maximum of two spaces away, but quasi-connectivity can create situations where a piston should be activated from a redstone component three spaces away. For example, a redstone component powering a block next to the space above a piston—the redstone component can activate the piston by QC but is three spaces away so does not provide an update to the piston.

Because of this update problem, some methods of activation by quasi-connectivity  ("QC activation", for short) update the piston immediately ("immediate QC activation"), while others put the piston into a state where it should be activated but doesn't know it yet, so it waits to activate until it is updated ("update QC activation").


### Immediate QC activation
Immediate QC activation is the activation of a piston by quasi-connectivity that occurs immediately and doesn't require the piston to be separately updated. This only works with redstone components that can update other redstone components two blocks away from them.

** Two blocks by taxicab distance **



























































Two blocks by taxicab distance
The following redstone components canactivatemechanism components one block away, butupdateall redstone components up to two blocks away (bytaxicab distance):
- Redstone Comparator
- Redstone Dust
- Redstone Repeater
- Redstone Torch

This means that when these redstone components activate the space above a piston (one block away), they also simultaneously update the piston as well (two blocks away). Redstone comparators and repeaters can only activate mechanism components adjacent to themselves horizontally, but redstone dust and torches can also activate mechanism components below themselves as well (redstone torches can also activate above, but that doesn't help for QC activation).


















Immediate QC Activation by Redstone Comparator — The piston activates immediately when the redstone comparator turns on.






























Immediate QC Activation by Redstone Dust — Both pistons activate immediately when the redstone dust turns on (we're not using a solid block under the dust because its powering would activate the pistons directly).

















Immediate QC Activation by Redstone Repeater — The piston activates immediately when the redstone repeater turns on.






























Immediate QC Activation by Redstone Torch — Both pistons activate immediately when the redstone torch turns on.

** Neighbors of component and of attachment block **
































Neighbors of component and of attachment block
The following redstone components canactivatemechanism components one block away, andupdateredstone components adjacent to the block they are attached to (including above and below) as well as redstone components adjacent to themselves:
- Buttons(attaches in any direction)
- Detector Rail(attaches only downward)
- Lever(attaches in any direction)
- Pressure Plates(attaches only downward)
- Trapped Chest(doesn't actually attach, but updates as if attached to block beneath)
- Tripwire Hook(attaches only sideways)
- Weighted Pressure Plates(attaches only downward)

This means that when these redstone components are attached to a block beneath them, they can activate the space above a piston (one block away), and also simultaneously update the piston as well (two blocks away). A trapped chest updates redstone components adjacent to the space beneath it, but doesn't need to be attached to any block (for example, like a pressure plate) — the other examples below use an upside-down slab instead of a block because a powered block would activate the pistons directly. A tripwire hook cannot be attached to a block beneath itself so cannot be used for immediate QC activation.



















Immediate QC Activation by Button — Both pistons activate immediately when the button gets pressed.


















Immediate QC Activation by Detector Rail — Both pistons activate immediately when the detector rail gets activated by a minecart.


















Immediate QC Activation by Lever — Both pistons activate immediately when the lever gets switched on.


















Immediate QC Activation by Pressure Plate — Both pistons activate immediately when the pressure plate gets stepped on. Also works with weighted pressure plates.


















Immediate QC Activation by Trapped Chest — Both pistons activate immediately when the trapped chest gets opened.

Other redstone components cannot update redstone components more than one block away so cannot be used for immediate QC activation, only for update QC activation.

### Update QC activation
Update QC activation is the act of putting a piston into a state where it should activate by quasi-connectivity, but it hasn't received a redstone update so doesn't know it should activate — it then waits to activate until it receives an update.

Pistons can be updated in a number of ways:

- placing or destroying a block next to a piston
- moving a block next to a piston
- changing the state of some blocks next to a piston (for example, changing the delay on a repeater)
- changing some states of some redstone components within two spaces of a piston:
	- changing the state of a redstone torch within two spaces of a piston
	- changing the power level (but not the orientation) of redstone dust within two spaces of a piston
	- changing the power level (but not the delay) of a repeater facing a space next to a piston
	- changing the power level or changing the operating mode of a comparator facing a space next to a piston

** Powered block **
A powered block*can activate the space above a piston, from the side or from above, without updating the piston, producing an update QC activation:












*


















Update QC Activation by Button-Powered Block — When either button is pressed, neither piston activates unless updated before the button pops out.







*






















Update QC Activation by Comparator-Powered Block — Neither piston activates until updated.








*














Update QC Activation by Detector Rail-Powered Block — When the detector rail is activated, neither piston activates until updated.







*






*
























Update QC Activation by Dust-Powered Block — None of the pistons activate until updated.












*


















Update QC Activation by Lever-Powered Block — When either lever is activated, neither piston activates until updated.








*














Update QC Activation by Pressure Plate-Powered Block — When the pressure plate is activated, neither piston activates until updated.







*






















Update QC Activation by Repeater-Powered Block — Neither piston activates until updated.








*














Update QC Activation by Trapped Chest-Powered Block — When the trapped chest is activated, neither piston activates until updated.

Ablock of redstoneacts like a powered block but can't be turned off, so the only way it can activate or deactivate pistons by quasi-connectivity is if it is moved into or out of a position where it would activate the space above the piston, either from the side or from above.























































Update QC Activation by Block of Redstone — Neither of the bottom two pistons activate until updated.

** Neighbors of component and of attachment block **































Neighbors of component and of attachment block
The following redstone components canactivatemechanism components one block away, andupdateredstone components adjacent to the block they are attached to (including above and below) as well as redstone components adjacent to themselves:
- Buttons(attaches in any direction)
- Detector Rail(attaches only downward)
- Lever(attaches in any direction)
- Pressure Plates(attaches only downward)
- Trapped Chest(doesn't actually attach, but updates as if attached to block beneath)
- Tripwire Hook(attaches only sideways)
- Weighted Pressure Plates(attaches only downward)

Of these redstone components, only buttons, levers, and tripwire hooks can attach sideways so can be used to produce an update QC activation. The others can be attached to a block beneath them, but then it's the block creating the update QC activation (described above).
























Update QC Activation by Button — When the button is activated, neither piston activates unless updated before the button pops out.
























Update QC Activation by Lever — When the lever is activated, neither piston activates until updated.




































Update QC Activation by Tripwire Hook — When the tripwire hook is activated, neither piston activates until updated.

** Immediate neighbors **
























Immediate neighbors
The following redstone components update only their immediate neighbors when they change their state, including above and below:
- Activator Rail
- Daylight Detector
- Tripwire(can also activate tripwire hooks in valid tripwire circuit)
- Pistonand Sticky Piston (from both the piston base and the piston head when extended)
- Powered Rail
- Rail

Of these redstone components, only a daylight sensor can activate the space above a piston and thus can be used to produce an update QC activation.
























Update QC Activation by Daylight Sensor — When the daylight sensor is activated, neither piston activates until updated.

The redstone components that cannot be used to put a piston into a QC activation may still be useful for updating them. For example, a tripwire updates adjacent blocks when an entity moves into or out of its space, and activator rails and powered rails are useful in that they update adjacent blocks when activated or deactivated (thus updates can be controlled with redstone without directly powering neighbors).

## Benefits of quasi-connectivity
Although somewhat difficult to understand, quasi-connectivity does offer many benefits.

### More activation options
Because a piston can be activated in its own space or the space above it, there are simply more options when figuring out how to activate it.

### Remote activation
Because a piston can be activated by anything that would activate the space above it, pistons can be activated from two spaces away while most redstone components can only be activated from one space away.

### Block update detectors
Main article: Tutorials/Block update detector
Update QC activation can be used to create a block update detector: a redstone circuit that is triggered by a block update rather than a redstone power input.

A piston activated by quasi-connectivity is sometimes described as "BUD-powered". However, quasi-connectivity and block update detectors (BUDs) are neither synonymous nor even subsets of each other. There are methods of QC activation that do not produce block update detectors (for example, any immediate QC activation method) and there are block update detectors that do not depend on quasi-connectivity (for example, stuck-piston BUDs).

### Torch keys
A torch key is a circuit that can react to the placement of a redstone torch in a particular location, even when the circuit is hidden beneath the ground. They are used to create a hidden method of activating another mechanism (for example, a piston door).

There are two primary methods of designing a torch key. The first is to place a block update detector under the ground so that the placement of a redstone torch updates the BUD. However, BUDs can also be updated remotely by other redstone components, increasing the chances of discovery. The second method is to use immediate QC activation by placing the torch so that it simply activates a piston by quasi-connectivity.

### Floating button

































→
























Dropper-Based Floating Button — The dropper and the bottom right hopper each have a single item in them.




























































→

















Piston-Based Floating Button
Similar to torch keys, but with an obvious input, a floating button is a button that doesn't appear to be connected to anything but can still be used. The strategy is to put a button far enough away that it can activate a piston by update QC activation and then repeatedly update the piston (without activating it) so that it responds quickly to the button turning on and off.

For example, the schematic on the left shows one way to build a floating button. The clock circuit on the left repeatedly powers and unpowers the powered rail next to the piston. When the powered rail changes state it updates the piston without activating it. If the piston is updated while the button has been pushed, it extends because the button would activate a mechanism in the space above the piston. Similarly, if the piston is updated after the button pops back out, the piston retracts again.

A quieter floating button (right schematic) can be created by using a dropper instead of a piston and using it to push an item into a hopper, which pushes it right back (unlike the dropper, the hopper isn't affected by redstone components two blocks above it), but briefly activates a comparator output. This version updates the dropper with a hopper clock, which is a little slower and thus slightly less responsive, but smaller than a torch-repeater clock.

## Drawbacks of quasi-connectivity
Quasi-connectivity can make it difficult to do things above pistons compactly without also activating them. For example, the player can't run redstone dust over a block on a piston because the dust affects the piston even if the block is a top slab.

### Workarounds
There are a number of strategies for getting a signal over a piston without affecting the piston:

** Go up a block and use redstone dust on a top slab **
Fastest transmission, but takes up the most vertical space.



→



→























Redstone dust over piston
** "Insulate" the space below with a repeater or comparator **
Adds minimum 1 tick delay to transmission, takes up two spaces above piston.



→







→
























Repeater or comparator over piston 1



→







→
























Repeater or comparator over piston 2
** Move a cauldron to power a comparator **
Adds 2 ticks delay to signal rising edge (1 tick for piston extension, 1 tick for comparator) and 1 tick delay to signal falling edge, takes up only one space above piston. The difference in rising and falling edge delay shortens pulses by 1 tick. If the piston moving the cauldron gets a pulse shorter than 1.5 ticks, it drops the cauldron in the extended position, turning on the output until the next time the input turns on and off again. A composter or chiseled bookshelf can be used for the same purpose.


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

