# Tutorials/Train station
When making a minecart railway, it's good to make a station. This tutorial lists multiple designs of train stations.

## Contents
- 1 The rail part
	- 1.1 Putting it together
- 2 Compact Auto Minecart Station
- 3 Automated Single-Car People Mover Stop
- 4 Automated Single-Cart Two-way Small Station (Tripwire)
- 5 Major Multi-Car Train Station
	- 5.1 Station Construction
	- 5.2 Platform
- 6 Ticket Machines, Booths, and Turnstiles
	- 6.1 Profits
	- 6.2 Hopper Ticket System
- 7 Enhancements
- 8 Platform screen doors
	- 8.1 Tutorial
		- 8.1.1 WolvHaven Metro
			- 8.1.1.1 Type 1 (Platform door lights won't work, and end up breaking the doors)
			- 8.1.1.2 Type 2
- 9 Automatic platform gates
- 10 Pictures

## The rail part
Main article: Tutorials/Minecarts
It might be a good idea to go over a few things about the rail first:

- Keeping Maximum Speed: On the mainrail, make sure that you have an activatedpowered railevery 32 blocks or, if you prefer fanciness over resource cost, you can use powered rails for the entire track. However, this requires much moreredstone, but definitely ensures that free carts do not slow down. If you possess vast quantities of redstone andgold, this isn't troubling.

A simple train station.
### Putting it together
The following flat-ground design, from left to right, has the following features:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|

- A station in the three nominally inactivated powered rails.
- Two "main" boosters, made up of a detector and 2 powered rails. The detector prevents backtracking. The spacing is determined by thetype of minecart.
- One "station mini" booster, made up of a detector and a single powered rail. The lower amount of powered rails prevents getting stopped by a second powered rail when the speed is insufficient to go clear of it before the detector unpowers.

## Compact Auto Minecart Station
| Train Hub in 1.6.2 showcase (view on YouTube) |
|-----------------------------------------------|
|                                               |

The above video is a slight variation that of the first design, that uses lava instead along with pistons is available and does not rely on any glitches, thus is considered to be safe for use in the latest versions of Minecraft (1.6+). When the player arrives in a minecart, the minecart gets broken by the lava and collected by the hoppers while the player is pushed out of the exit using a glass block connected to a sticky piston. While slightly more redstone intensive than Sethbling's design (which was exceptionally simple), it does not have any problems associated with it and is thus recommended for anyone playing in 1.6+. If you are playing in Java Edition 1.5.2 or below (and not planning on updating), Sethbling's design is definitely better.

Here's a tutorial on how to build this design:

| Train Hub in 1.6.2 tutorial (view on YouTube) |
|-----------------------------------------------|
|                                               |

Another variation made by nmoleo64 uses a detector rail wired to a command block with the command /kill @e [type=MinecartRideable,r=2] to remove the minecart.

## Automated Single-Car People Mover Stop
The following video is a good example of a small station:

| YouTube Video (view on YouTube) |
|---------------------------------|
|                                 |



Direction changing:

| YouTube Video (view on YouTube) |
|---------------------------------|
|                                 |



These designs are more complex and not as annoying. It is possible to minimize the number of powered rails used. Also, this can be implemented on any server, it doesn't require weeks of experimenting. This is recommended for beginners.

## 
The tripwire toggles the minecart between 2 different routes, the cart either moves in circles, awaiting a passenger. When a passenger is present, the tripwire activates and the cart moves in another route away from the station.

## Major Multi-Car Train Station
Note: This design requires lots of materials, so it is not recommended for a survival world that has been recently started. The design also uses a lot of redstone.

Here is how to make a working train station and powered rail system. It is most useful in multiplayer.

You need the following materials to build this station:

- 200+redstone dust(You may need more depending on how big it is).
- 64+gold ingots(Forpowered railsdepending on your decision).
- 100+iron ingots(Forrailsand tools).
- 1+stone pressure plate(s) (Usewooden pressure platesfor ticket collectors shown below).
- Lots ofwood(2 stacks or more).
- 500+ building material (cobblestone,stone,brick,dirt, etc...)

Note: all of these amounts may vary on the size of the station.

### Station Construction
The construction of the station is one of the most important parts. Firstly, determine the size and structure of your station. You can have a massive central terminal with many platforms and on top, have ferry piers and light rail and etc. or a simple humble station with a 5-car light rail. For the test experiment, the platform only fits 3 passenger cars. You can include luggage cars in front or at the back, but to build the platform, you need a large open area. Also, determine whether your platform is a side platform or an island platform. A side platform serves only one track while an island platform serves two tracks.

### Platform
Platform diagram.
Now, start the boarding area. The track below the platform are all powered rails. You should include extra powered rails beyond the platform for luggage cars. Before the platform, have another set of powered rails(not connected to platform track). Make a station box across from the platform with levers controlling both sets of powered rails, and place a station attendant here. Before the non-platform set of powered rails, have a room set into the side so another attendant can push the carts in an emergency.

## 
At a ticket booth, have a person behind a glass screen with a 1×1 hole, with the stated price and destination above the hole. For a ticket turnstile, have a series of iron doors separated by walls with holes in the bottom. Below the holes, have pits that open out into a room. Below each pit, have a wooden pressure plate connected to the door (preferably under) with a person standing next to it to collect the ticket. The ticket can be anything. 
Another idea is to have a separate room with redstone connecting the iron door in the waiting room. In the staff room, there can be a lever that opens the door when pressed. Finally, have controlled water flowing through a 1 block high gap which flows into the staff room (be careful of redstone.) Now, patrons can drop "tickets" into the water and when it reaches the staff, they can open the door.

A new idea is a machine reading your ticket. Have a hole, then a water shaft. 2 blocks in, put hopper and a dropper below that. And put some space further on. Put a redstone comparator next to the hopper above the dropper. Then, put 64×9 of your "money" in the dropper. Put 22 "coins" in the hopper. Then, put two redstone next to it and a redstone repeater after that. Wire this up to an AND gate and a redstone clock. Wire this up to the dropper and another wire to a dropper, which has all your tickets in.

When you put your money in it goes inside the hopper. This makes the comparator go one more block which powers the rest of circuit. You need an AND gate and a clock to make a pulse. The pulse makes the dropper lose one thing so it reverts to its one block. This makes it resettable. It powers the dropper to give you a ticket. If you have any wrong ones, it does not go in the hopper and disappears after a while. Make the money from the first dropper go into lava or into a hopper chain to a chest.
This is quite advanced so only attempt if good with redstone.

Turnstile diagram.
### Profits
If well made, ticket fees yield a considerable profit on multiplayer, possibly giving you enough resources to build a massive subway network similar to the New York City Subway, taking vast amounts of people to various places.

It is also possible to do a huge rail network with smaller,  stops. Instead of using up many pickaxes while making stations, a simple single-cart network can be used.

Remember, building a structure this large requires significant time and effort, not to mention the resources. When building an underground network, you may find that sealing off ravines and caves becomes an additional problem. It is therefore wise to start building once you have gotten experience with redstone circuits.

### Hopper Ticket System
Using hoppers, all the tickets (or other fees) thrown into the ticket machine could be pushed with a piston into a hopper on top of a chest, giving the owner the tickets back (or extra money, even)!

## Enhancements
If your train station gets really big, you can add some of the following features:

- Mapsinitem frames. This can show people where they are going.
- Shops. A small trading station where you can buy and sell things from a server user. You could also add more shops that usevillagersfor trading purposes.
- A mini restaurant. The meals could be cooked meat and the drinks could bepotions.
- A goods station. You could use this to send storage carts to your friends.
- Someender chestsfor secure transport of goods, even though this cannot be used to send items to others.
- Aclockin anitem frame.
- For some added fun makemobsoccasionally fall to their deaths, giving free items.

## Platform screen doors
Platform screen doors screen the platform from minecarts. They are found in rapid transit systems like the WolvHaven Metro made by Silver Wolv and the New WolvHaven Blocky Electric Rapid Transit (BERT) made by Axton, the Kasukano Train Railway built by members of Watersuno, and the Nazca Railway built by Nazca Wilde.

### Tutorial
#### WolvHaven Metro
##### 
1. Place 3sticky pistons1 block aside from the opening
2. Place a block next to the middle sticky piston withredstonedust
3. Place aredstone torchunder the block with the redstone dust
4. Place another redstone torch under the block with the other redstone torch
5. Place a block diagonal right to the bottom redstone torch, and put another redstone torch aside the block, that on its side is the torch tower
6. Mirror the same redstone from Step 1 on the right, and skip Step 5
7. Place redstone from the torch aside the block, and carry it to the other side to the bottom of the other torch tower
8. Place aredstone repeatertoward the left of the bottom block of the right torch tower, it should be next to the redstone from the torch diagonal to the bottom of the torch tower
9. Replace the redstone dust with a redstone repeater facing the left torch tower
10. Place adetector railabove the redstone diagonal to the right torch tower

##### Type 2
1. Do the same mechanism from Step 1 until Step 5 from Type 1
2. Place 3 pieces ofredstonedust, one on the block diagonal to the torch tower on both sides
3. Place adropperfacing across 2 blocks right, and 1 block down from the redstone from the diagonal block
4. Place another dropper facing down toward the dropper facing across
5. Place a final dropper facing up in front of the across dropper
6. Place a hopper facing the dropper facing down, and place any item inside the dropper facing across. This creates a quietT-Flip Flop
7. Place 2 blocks in front of the downward facing dropper, and place aredstone comparatoroutput from that dropper
8. Place redstone dust in front of the comparator, and place another block right from the block with the redstone
9. Place aredstone repeaterat the right side from that redstone from the comparator
10. Link the torch towers with redstone dust coming from the repeater

## Automatic platform gates
Automatic platform gates (or half-height platform screen doors) are one-block sliding doors at the edge of railway platforms to prevent passengers from falling off the platform edge onto the railway tracks. 

## Pictures
- The platform, with the station box opposite.
- The view from an arriving minecart, showing the first set of powered rails in the foreground, with the second set further on.
- Looking back from a departing minecart, with the second set of powered rails in the foreground, the platform on the left, and the station box on the right.
- The arrival track, viewed from the platform, with the first set of powered rails in the foreground.
- The first set of powered rails, with the second set in the background.
- The bell for alerting of incoming trains.
- The rail that connects to the alarm bell.
- A pig activating the alarm bell.
- The interior of a station box, showing both levers(platform track(second set) lever left, first set powered rail lever right).
- Looking into the station box from the arrival end, showing the platform(second set) powered track lever.

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

