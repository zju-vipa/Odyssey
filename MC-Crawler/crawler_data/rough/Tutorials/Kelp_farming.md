# Tutorials/Kelp farming
This tutorial seeks to explain common practices for farming kelp, a plant found naturally underwater.

## Contents
- 1 Uses
- 2 Mechanics
	- 2.1 Experimental testing
- 3 Manual farming
	- 3.1 Helpful equipment
	- 3.2 Infrastructure
- 4 Automatic farming
	- 4.1 Piston design
	- 4.2 Flying machine
	- 4.3 Bone meal design
	- 4.4 Review Techniques

## Uses
When smelted and crafted into dried kelp blocks, kelp can be used to smelt items. One kelp block can smelt 20 items, so a single undried kelp ends up smelting 1.22 items. This makes kelp useful as a renewable fuel source.

Smelting kelp also grants 0.1 experience. To put this into perspective, it would take about 3,060 smelted kelp to go from level 27 to level 30.

In addition, kelp can be composted, giving an average of 1 bone meal per 23.33 kelp. Dried kelp works the same way, so it would be possible to smelt kelp for the experience, and then compost it.

## Mechanics
Kelp grows similar to sugar cane. One stem block can be placed underwater, and then it spontaneously grows upward until the top of the kelp is one block below the water surface. When kelp is planted or the plant above is broken, it sets a random age from 0 to 24, which determines the maximum height the kelp is able to reach. When kelp grows, the plant adds 1 to the age from below. A kelp plant stops growing at age 25. This means that a kelp plant can grow between 2 and 26 blocks tall.

Kelp has a 14% chance of growing each random tick. This means that there is a 50% chance for the kelp to grow in the first 4.6 ticks, a 75% chance for it to grow within 9.19 ticks, and a 25% chance for later growth. For information on random tick timings, see block tick.

Gnembon kelp mechanics


Bone meal can be used to speed up the growth of kelp. One bone meal grows kelp by one block.

Additionally, the maximum growth of a kelp plant may be reset to the current height of the plant, hindering any further growth. Not even bone meal can make a kelp plant grow again if the maximum height becomes reset to current height.

### Experimental testing
Based on testing, a 20×20 square of kelp (400) down results in a rough 50% gain over the course of 1 minute, or about 600 kelp. This does not mean that half of the kelp grows 1 block; the random nature of the growth creates a negative logarithmic curve of how many plants reach certain heights. (L shaped curve)

Here is the results from a 256 kelp test over a period of 1 real-life minute (1,200 ticks)
All kelp were made to be less than age 20 for the trial, so age did not matter as none grew to 6 tall.

| Category                        | Data     |        |        |       |       |
|---------------------------------|----------|--------|--------|-------|-------|
| Height Of Kelp                  | 1        | 2      | 3      | 4     | 5     |
| Number Of Times Grown           | 0        | 1      | 2      | 3     | 4     |
| Number Of Kelp Plants           | 106      | 109    | 33     | 7     | 1     |
| Percentage of Kelp Plants       | 41.41%   | 42.58% | 12.90% | 2.73% | 0.38% |
| Percent that reached each stage | starting | 58.59% | 16.02% | 3.12% | 0.39% |

## Manual farming
Kelp can be manually farmed by placing kelp underwater, waiting for it to grow, and breaking it. Usually you want to break the block above the bottom kelp plant so as to allow continued growth. If you do not need a large amount of kelp, such as several double chests filled, it is possible that harvesting naturally grown kelp in the ocean is sufficient.

It is important to note that kelp may not always grow to max height due to the random age value mentioned above. As such, it may be desirable to harvest kelp more frequently to allow it to constantly grow. In Java Edition, this age value can be checked by pressing F3.

When harvesting kelp, you should swim down close to the base of the plants and sweep your view, breaking large amounts of kelp. Once you have broken a sufficient amount, swim to the surface to collect the items. Make sure to collect the items within 5 minutes before they despawn.

### Helpful equipment
Kelp only grows underwater, which creates some difficulties when trying to harvest. The difficulties can be alleviated through the use of the right equipment, however.

- Ahelmetenchanted withRespirationcan allow you to stay underwater for longer. Such a helmet allows for up to an entire minute of time underwater. ATurtle Shellhelmet would also be helpful as it allows you to instantly recover air when breaking the surface.
- Moving underwater can also be slow. This can be helped withbootsenchanted withDepth Strider. ARiptidetridentmay also be helpful. If mining out an area for a farm, you may also wantAqua Affinity.
- Some potions can also be helpful. A potion ofWater Breathingcan allow you to stay underwater indefinitely and a potion ofNight Visioncan allow you to see much better.
- A sword withSmitemay be helpful for fending offDrowned.
- UsingIceto create Water Sources with a Silk Touch Pickaxe is more convenient and effective than using water buckets to place water.

### Infrastructure
To help streamline the farming process, you can also build up the infrastructure within the farm itself.

- To increase visibility, you could light up the area withJack o'Lanternsorsea pickles.
- Constructing nearby air pockets allow the player to enter and replenish breath more easily.
- Aconduitis extremely helpful as it provides all players within a 32-96-block spherical range with water breathing and better vision. In addition, it also attacks nearby hostile mobs.

For the farm itself, you should probably clear out a large area and cover it with kelp. Ideally, make the area at least 25 blocks deep to allow the kelp maximum growth.

It is also possible to automate collection by placing flowing water at the top, flowing into hoppers. This can be tricky however, and the kelp must not be allowed to grow into the flowing water and break the stream.

## Automatic farming
Kelp can be automatically farmed by using pistons to break the second-to-bottom kelp block. Since kelp can vary in height from 2 blocks to 26 blocks, it is most efficient to have a chamber that can handle the maximum height.

### Piston design












jsap-$













jsap-$






jsap-$











Basis of a kelp farm
It is possible to create several kelp farms using the design shown in the schematic. For the design to work, there needs to be a way to trigger the piston. This can be done with either a clock circuit or an observer. In addition, it could also be fired manually by the player.

In Java Edition, an observer facing the bottom kelp plant detects when it grows. This can be used to fire the piston facing the second kelp block. It is also possible to have the observer above the piston. However, it is possible that the kelp grows to 2 block in height and never triggers the observer. This makes it necessary to also have a clock or manual way to reset the farm.

### Flying machine
It is possible to use a flying machine to harvest large amounts of kelp all at once. This sort of design is more practical on a large scale as the kelp plants are all planted compactly next to each other.

| ilmango Flying Kelp Farm (view on YouTube) |
|--------------------------------------------|
|                                            |

### Bone meal design
It is possible to use bone meal to accelerate plant growth. Since kelp does not break instantly, it is necessary to have a delay on how fast the farm runs. Otherwise, the kelp may grow before the rest is done breaking.

| ilmango Bone Meal Based Kelp Farm (view on YouTube) |
|-----------------------------------------------------|
|                                                     |

### Review Techniques
Fizedi compares three techniques and determines the most efficient farm.






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

