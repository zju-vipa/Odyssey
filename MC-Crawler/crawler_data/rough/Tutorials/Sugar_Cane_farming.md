# Tutorials/Sugar Cane farming
Sugar cane is a valuable plant for crafting rockets, making books for bookshelves, maps, and trading paper. Sugar cane can also be used with a composter to get bone meal, however, melon farms are probably more suited for this. The large amount of sugar cane obtainable from some of these farms can make it much easier to get firework rockets or emeralds.

## Contents
- 1 Mechanics
- 2 Manual farm designs
- 3 Semi automatic farm designs
	- 3.1 Water canal design
	- 3.2 Piston harvester
	- 3.3 Bone meal design
- 4 Fully automatic designs
	- 4.1 Stationary design
	- 4.2 Flying design

## Mechanics
Sugar cane can only be planted on grass block, dirt, coarse dirt, rooted dirt, podzol, mycelium, sand, red sand, moss block and mud. The block must be directly adjacent to water and not merely above or diagonal as with crops. If a plant's water source is removed, it breaks when it is next updated. In Bedrock Edition, the sugar cane is updated with its water, so it breaks immediately.

Every 16 random ticks, sugar cane grows 1 block in height, similar to how cactus, kelp, and bamboo grow. On average, sugar cane grows 1 block every 18 minutes. Sugar cane's growth rate is unaffected by the absence of light.

Sugar cane can naturally grow up to 3 blocks in height. This limit can be bypassed by placing additional plants on top of an existing one but it does not grow naturally any further.

Sugar cane, like saplings, wheat, and cacti, grows only if the chunk they are on is loaded into memory, so you should not venture too far from the field if you want it to grow. The growth range is based on simulation distance.

## Manual farm designs
This pattern is easier to harvest since the player doesn't fall into the water as often.
The first step in building a sugar cane farm is choosing a design. When starting out, simply placing sugar cane on a river bank should be sufficient. However, this quickly becomes impractical when implemented on a large scale. Sugar cane farms must balance between compactness, ease of harvest, and difficulty to build.

A double rowed design, while not the most efficient of designs as it has only 2 canes per water, is relatively easy to build and harvest. It is also a good choice for some of the semi-automatic designs below. With this design, it is recommended to use flowing water rather than water sources. Not only is it easier to build it flowing, but when harvesting, any items that fall into the water flow into a central location.

This compact pattern allows planting four sugar cane per water block.
A more efficient grid pattern design can also be used. This design has 4 sugar canes per water source, so it is highly compact. Placing lily pads or something similar on top of all water blocks makes the ground smooth and easy for the player to walk on without falling. Light blocks can be used under or above the water to prevent mob spawning. Slabs or trapdoors can be placed as waterlogged blocks in the upper half of the water sources instead of lily pads without interfering with their ability to sustain plant growth.

When harvesting, walk slowly and sweep side to side breaking all but the bottom block of each sugar cane. Then, pick up any missed items and continue. Watch out for creepers camouflaged among the plants.

## Semi automatic farm designs
In Bedrock Edition, when sugar cane's water source is removed, it immediately breaks. Using this principle, it is easy to create semi-automatic farms that harvest the sugar cane. These designs should still work in Java Edition, however, it takes a bit more time for the sugar cane to break. Some other designs here are classified as semi-automatic due to their lack of ability to pick up the sugar cane. These can often be easily converted into automatic designs as seen in the next section.

### Water canal design
Build the double rowed design as shown in the manual farms list. Then, place dispensers containing water buckets to control the water flow. Removing the water streams with the dispensers should cause the sugar cane to break so the player can pick them up and replant.

### Piston harvester


















Top view of an extended piston harvester


















Side view of a piston harvester
This design uses pistons to harvest the sugar cane. If the sugar cane is only two blocks tall, it can all be pushed into a water stream. However, if it grows any taller, the top blocks may fall down to the sand where the player can pick it up. This design is often used as the basis for fully automatic farms, however, it must be modified to push the top blocks as well or some of the sugar cane may be lost.

### Bone meal design

  

This tutorial is exclusive to  Bedrock Edition. 


See also: Tutorials/Bone meal farming






















Side view of a simple bone meal farm
In Bedrock Edition, bone meal can be used to instantly grow sugar cane to maximum height. This mechanic can be used to create automatic sugar cane farms.

In the shown design, the dispenser can be filled with bone meal to constantly grow the sugar cane. Since bone meal is not used up on fully grown sugar cane, none is wasted. The player can then stand and constantly break the middle block of sugar cane to quickly farm large quantities.

It is not difficult to connect this with a piston to make it more automatic. However, since pistons cannot push and retract as quickly as the observer clock, it may be desirable to use a different redstone clock. Additionally, a single hopper may not be able to keep up with the large amount of sugar cane, so multiple hoppers or a slower clock should be used. Ideally, a 4 gametick delay clock should be used instead of an observer clock. Even more ideal is a 2 gametick alternating dispenser bone meal system with a ravager in a minecart to break the top 2 sugarcane blocks.

Example sugar cane farm using bone meal


## Fully automatic designs
Fully automatic designs automatically harvest and collect sugar cane, usually relying on some sort of redstone clock or growth detection. These designs are often expensive to build and more lag prone than other designs. However, the large amount of sugar cane they produce can pay off.

The easiest way is to pillar up 3 blocks, and the second block is a piston, the third an observer. Plant the sugarcane and collect it using a hopper system or any other means.

There are four main types of automatic sugar cane farms: Stationary, flying, sim-tick, and zero-tick. Stationary designs, while simpler for platforms without quasi-connectivity, are generally more resource and space intensive as compared to flying designs. Flying designs usually require slime blocks however which may be difficult to obtain for some players. Sim-tick designs move the player so the plant is out of simulation distance, then uses a sticky piston that is within simulation distance to remove and then replace the block beneath it, and when you move back so the plant is within simulation distance, the plant has grown. Zero-tick designs remove and replace a requirement for the plant within the same game tick, also forcing a growth update. These designs usually use pistons or sand manipulation. Zero-tick sugar cane farms are faster in Bedrock Edition, with some getting at or above 2,000 sugarcane per hour per plant.

### Stationary design
















































Automatic observer farm
By using a daylight sensor or other clock circuit, the semi-automatic piston design is shown above can be made fully automatic. To make it more lossless, it is recommended to add another layer of pistons above the original one. In Bedrock Edition, these designs can be an alternative to flying machines that are difficult to create and use for this purpose.

| Basic clock based design (view on YouTube) |
|--------------------------------------------|
|                                            |

Other variations are also possible, such as this diagonal design which uses a hopper clock rather than a daylight sensor.

Diamond shaped tower design


Rather than use a clock, some designs use observers to harvest the sugar cane as soon as it grows. Designs such as these may inefficiently use space compared to the clock method. Since simple designs cause all of the pistons to activate anytime sugar cane grows, they are often less lag efficient too.  Repeaters can be used to create a simple alternating pattern to singly fire the pistons.  Creating your farm with two rows of sugarcane and two rows of pistons facing each other solves the problem of the central sugarcane being pushed, while the top sugarcane drops straight down.  A double row of hoppers or a hopper cart system can feed a timed dropper to load the sugarcane into a water sorting/transportation system.

Two simple redstone harvesting machines that can be used in an alternating pattern for singly-firing pistons.
Two simple redstone harvesting machines that can be used in an alternating pattern for singly-firing pistons.  A double row of hoppers or a hopper cart can be used to collect 100% of the sugarcane that is dropped.  The design can be stacked and tiled with timed droppers to feed a water collection/sorting system.

When constructing, the sugar cane goes on the dirt and rails run where the minecart is shown. The minecart with hopper can be replaced with a line of hoppers if the sugar cane is planted on mud.

Observer Farm


Farms can be designed to cost less resources early game by replacing the minecart with hopper and rails with a water stream and a singular hopper. These designs are also significantly quieter since they remove the minecart traveling underneath. These designs can also be more server-friendly than traditional minecart with hopper designs as some servers choose to disallow minecarts to reduce lag. The downside of these designs is that occasionally items can land on the sand and not be picked up, meaning they are not lossless.

Water Stream Design


It is possible to speed up the process of sugar cane by removing the water source and replacing it in the same game tick, this process is called zero-ticking. Although this does not work in Java Edition as of 1.16 it does work in Bedrock.

Wattles Tutorial


### Flying design
The use of flying machines and minecarts with hoppers can be combined to create some of the most efficient farms. Flying machine designs generally use only a few pistons and don't create lag except when harvesting. This is usually the preferred type of design when creating a large farm. The main disadvantage to farms such as these is that they can break if unloaded while running. Due to this, it can be risky to have these run without supervision.

Flying machine based design


This video has some useful information regarding flying sugar cane farming. It contains a practically lossless flying machine design similar to the one above. The lossless design works by covering the water with leaves and using the flying machine to ensure items pushed to places they can be picked up.

Flying sugar cane


Some flying farms focus on just individual rows of sugar cane, instead of larger fields. Designs like these typically cost fewer slime blocks to build, and are usually the cheapest option for mass farming.

4-Way Flying machine based design


This farm uses a four directional flying machine which works out cheaper than most designs, especially for larger farms. It even can reduce the lag caused by entites as it drops less entities into the world.

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

| Row based design (view on YouTube) |
|------------------------------------|
|                                    |

