# Tutorials/Zero-ticking
This tutorial seeks to teach the player how to make a redstone signal turn on and off in the same tick, go over how this could be used, particularly with its uses on pistons.

## Contents
- 1 Introduction
	- 1.1 Zero-tick pulse generation
	- 1.2 Zero-tick chaining
	- 1.3 Zero-tick repeaters
	- 1.4 Creating a zero-tick clock
- 2 Uses of zero-ticking
	- 2.1 Embedding entities
	- 2.2 Fast block farms
	- 2.3 Zero-tick plant farms

## Introduction
When a redstone signal is sent through a pulse limiter, it shortens the pulse. When the pulse is shortened enough, strange behaviors arise. If a sticky piston is powered by a 2-tick pulse, it will start extending but after two ticks, the piston will drop its block and start retracting. If a sticky piston is powered by a 1-tick pulse, the same behavior will happen, but instead of happening after 2 ticks it will only happen after one tick.

When a piston receives a pulse that turns on, and then off in the same tick, this is known as a 0-tick pulse. This will cause sticky pistons to instantly drop their block and start retracting.‌[Java Edition  only]. Regular pistons will start retracting instantly when powered by a 0-tick pulse, but the block will not instantly teleport unlike sticky pistons. Because a 0-tick pulse turns on and off in the same tick, many 0-tick pulses will not render, but the pulse still exists. Due to how 0-tick pulses work, some 0-tick pulses are unable to bud-power pistons in some circumstances.

### Zero-tick pulse generation
See also: Pulse circuit § Pulse limiter

All 0-tick pulses are created by powering a redstone line, and then using pistons to remove the power source later in the tick. 























Producing a 0-tick pulse using tile tick priorities

One method of doing so is using tile tick priorities. Since comparators are processed in a tick later than repeaters, one can generate a 0-tick pulse by powering a redstone line using this behavior. In this example, redstone repeater is used to power the output line, and a comparator is used to power a piston which will remove the block in front of repeater to depower the line. Since the comparator always powers after repeaters, the redstone line will always turn off after it turns on, creating a reliable 0-tick pulse. The advantage to this 0-tick generator is that it's 0-tick pulse is earlier in a tick relative to 0-tick pulses generated through other methods.

A 0-tick generator that uses budded pistons






Another common method of generating 0-tick pulses is to use budded pistons. As budded pistons only retract when updated, this can be used to control which order pistons move and therefore controlling the order in which a redstone line is powered then unpowered. One example is to have a redstone line that directly powers a sticky piston and bud-powers two other sticky pistons. The piston directly powered by the redstone line will have a block on its face, and the last piston in the chain will have a redstone block on its face. A second redstone line will be at the bottom which is the output; it will be powered by the piston with a redstone block and is cut off by the solid block. When the redstone line on top is powered, nothing will happen. But when the input is depowered, then a 0-tick pulse is created. The redstone line will depower, but only cause the piston that is directly powered to start retracting. This will uncut the output line, turning it on. When this piston retracts it will then update the piston in the middle, causing that one to retract which will then cause the last piston to start retracting, which will remove power from the line.


### Zero-tick chaining
Within a tick, 0-tick pulses happen , but 0-tick pulses can happen after other 0-tick pulses while still being in the same tick. This is known as 0-tick chaining where two or more 0-tick pulses are activated in a row.

0-tick chaining that relies on the fact that tileticks process before block events
One method of 0-tick chaining is to utilize the fact that tileticks such as repeaters and comparators will process in a tick before block events such as piston extensions and retractions. In the shown example, when the input is powered, the quartz block will be 0-ticked by both pistons causing it to instantly move two blocks, ending up above the diamond block. The 0-tick generator to the right makes use of tileticks and will activate before the 0-tick generator on the left, which uses block events. This method of chaining is very compact, but it comes at a downside that this method can only be used once per chain.


0-tick chaining that uses a long update chain before the second 0-tick generator
Another method of chaining is to utilize the fact that update chains can be used to manipulate the order in which things are processed in a tick. In the shown example, there are two 0-tick generators. The one on the left has an update chain before powering it, while the one on the right is directly powered. When the input is depowered, the 0-tick generator on the right will activate first as it is directly powered causing its output piston to instantly drop its block. While this is happening, the update chain is retracting. Then, the 0-tick generator on the left will will activate causing its output piston to instantly drop its block.


### Zero-tick repeaters
The three most common forms of a 0-tick repeater
A regular redstone repeater can't be used to refresh the signal of a 0-tick pulse as they would extend the pulse to a length of 2 ticks. So one must use a 0-tick repeater. A 0-tick repeater works by receiving an input as a 0-tick pulse, which will 0-tick a redstone block that is inside of the 0-tick repeater. And right after that, the redstone block is 0-ticked back to it's original position. This can be used to repeat 0-tick signals, but one must note that they add block event delay.


Using a 0-tick repeater to chain 0-tick pulses. Powering the input will cause the quartz block to move on top of the diamond block.
One can also use 0-tick repeaters as a method of 0-tick chaining. This is possible because 0-tick repeaters add block event delay. 0-tick repeaters are very useful because they can be used to chain signals created by 0-tick clocks, as only 0-tick repeaters have the ability to reset fast enough.

NOTE: The piston under the left most piston here is a sticky piston


### Creating a zero-tick clock
This is a top down view of the clock without a block in it.
A 0-tick clock is made by putting two 0-tick block pushers facing each other and pushing a block between themselves, one line will appear on, while the other appears off, each has unique behavior, the "off" line is BUD-proof, while the "on" line allows for BUD pistons, and to set which is which, simply place a lever on the torch under the side you wish to be "on" and flip it twice, also this lever can turn it off. 

Another thing to note is that if it is built right, the block WILL NOT seem to move while the piston heads will glitch through it, and the redstone lines WILL NOT pulse at all.

This is a top down view of the clock with a block in it.
Side view of a running 0-tick Clock

## Uses of zero-ticking
Since a comparator does not react to a 0-tick pulse and the pulse will lose its effects if it goes through a repeater, most 0-tick uses involve pistons. Pistons can be used to move blocks before the game has a chance to react as it normally would.

### Embedding entities
Normally, when you power a sticky piston with a block on it towards an entity, and the entity has enough room to move, it will be pushed by the block. Zero-ticking a block places it over the space occupied by the entity without moving the entity. This can be used decoratively, e.g. creating 1-block glass 'display cases' with entities (mobs, armor stands) inside, or offensively, causing mobs to suffocate if using solid blocks, or in contraptions where you can overlay an armor stand and a solid block within the same space, e.g. for vertical signal transport using piston and tripwire, crossing with horizontal transport through the block. This can easily be done by placing a button on the side (not the back) of a piston. This will power the piston and the piston powering will instantly break the button causing a 0-tick pulse.

### Fast block farms
Farms such as tree farms, cobblestone farms, and basalt farms generate blocks. Using 0-tick pistons, one can create quick harvesting cycles, as well as quickly moving the blocks from the farm output into a TNT blast chamber or wither cage.

### Zero-tick plant farms
These farms are patched and no longer function as of Java Edition 1.16.

Zero-ticking allowed for incredibly fast farms of Bamboo, Cactus, Chorus Plant, Kelp, Sugar Cane, Twisting Vines, and Weeping Vines.

The farms worked by exploiting certain buggy behavior. When the block supporting a plant is instantly replaced with another of the same block, the plant forcibly receives a random tick. Chorus Plants require only a single random tick to grow, plants like Cactus and Sugar Cane require 16 random ticks to grow, and still other plants react differently to random ticks. In essence, the exploit allows the plants to grow and be farmed at very high speeds for relatively low build cost.


The zero-tick plant growth exploit was observed October 2016 by ToseRedstone. The corresponding bug MC-113809 was documented on the bug tracker February 2017. The bug was accidentally patched in snapshot 18w06a, and it was officially patched in snapshot 20w12a ahead of release 1.16.





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

