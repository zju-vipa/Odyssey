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


