# Tutorials/Combination locks
Combination locks are a type of redstone circuit. They generally have a number of components which must be set in the right combination in order to activate something such as a door. Combination locks can be very useful in creating adventure maps. Note that if you are playing in survival multiplayer, other players will still be able to break into the mechanism and cause it to activate without knowing the password.

## Contents
- 1 Order-insensitive combination locks
	- 1.1 Lever lock
	- 1.2 Item frame lock
	- 1.3 RS NOR Combo Lock
- 2 Order-sensitive combination locks
	- 2.1 Order-sensitive changing code XNOR Combo Lock
	- 2.2 Order-sensitive RS NOR Combo Lock
		- 2.2.1 Tutorial Video
		- 2.2.2 Tutorial video
		- 2.2.3 Combination lock with order-sensitive reset

## Order-insensitive combination locks
### Lever lock
















































Lever lock  16 (24) combinations
A lever lock is one of the easiest redstone locks to create. Each lever doubles the number of combinations the lock has. The possibilities can be found using 2n, where n is the number of levers used.

When constructing, you will probably first want to place the levers and put them into the desired positions. Next, you should place the redstone torches and repeaters. Torches go behind levers that are down and repeaters go behind levers that are up. When you are done, all of the torches and repeaters should be turned off. If not, double check any components that are turned on.


Detailed Instructions
Follow these steps carefully.
Step 1

First, place an 11 block row of any block, and make it two blocks high. Then, add a row of 7 branching off both sides.


Step 2
Add levers/switches on the bottom row of the 11 blocks, followed by signs on the top row. Each sign should have a number in order (1, 2, 3 etc.). Alternatively, you can make the signs have letters or words on them instead.
 

Step 3
Place a repeater in front of each block of the row that has the levers.


Step 4
According to the password you want, you need to place a block in front of the switches that make up your password and put a redstone torch on top of each. For example, if your password for 1-2-6 (like in the example), each block and redstone torch is placed in front of switches 1, 2 and 6.


Step 5
Next, place a block in front of each block that you just placed. Fill all the spaces in between the blocks with repeaters.


Step 6
Place a row of redstone dust in front of the repeaters and blocks.


Step 7
Place a strand of the redstone, starting from the middle, down to the 2nd last row. At the last row, place one block in front of the redstone.


Step 8
Add one redstone torch on top of the block just added. Then, add another block on top of the torch. Once you've done this, add a door on top of that block.


Step 9
Your passlock door is finished. To activate, flick all of the levers of which you had the password made up of, but no others. For example, if your password is 1-2-6, turn the levers below the signs that say 1, 2, and 6, on, but all the others should be off. The door should open.
  

Final Touches
Cover all the redstone with blocks, so that players can't see it.


Notes
The design shown in these directions can have up to 29 inputs. Larger amounts are more secure; the number of possibilities is 2^c, where c is the number of levers used. You can't have more than 29 inputs with this design as the redstone signal won't travel far enough.



| Demonstration video (view on YouTube) |
|---------------------------------------|
|                                       |


### Item frame lock









































































































































Item frame combination lock  512 (83) combinations
Item frame combination locks are a step up in complexity from lever locks. Items in item frames can be rotated into 8 different positions. This rotation can be detected by a comparator which will output a signal strength from 1 to 8 depending on the position. Since each item frame has 8 possible states, the number of possible combinations can be found with 8n, where n is the number of item frames.

The horizontal redstone paths on the floor decrease the signal emitted by the comparator down to a fixed strength of 1, and then feed it into an "A OR NOT B" gate that is true if the strength is either too small (B is not powered, i.e. false) or too large (A is powered, i.e. true). These gates are all ORed together so that the overall result is true if any item frame in the lock is misplaced; finally a torch (optional) inverts the result.

If you want to make it extra tricky, it is also possible to detect an empty item frame by when a comparator doesn't output anything. Simply leave a repeater connected to the comparator and feeding into the vertical redstone wire on the right side; a filled item frame will give a signal strength of 15 out of the repeater and keep the door locked.

| Tutorial video (view on YouTube) |
|----------------------------------|
|                                  |

### RS NOR Combo Lock
Connect a series of buttons to the S-input of RS Latches. Feed the Q or Q (choose which one for each latch to set the combination) outputs of the RS Latches into a series of AND gates, and connect the final output to an iron door. Finally, connect a single button to all the R-inputs of the RS Latches. The combination is configured by using either Q or Q for each button (Q means that the button would need to be pressed, Q don't press).

Example:




With the automated reset it causes the correct combo to cause a pulse instead of a "always on" until reset.

## Order-sensitive combination locks
Order-sensitive combination locks are sometimes known as permutation locks.

### Order-sensitive changing code XNOR Combo Lock
Opens when a certain order of switches are pressed.
You can change the order.
(Note: A moderate understanding of logic gates is needed for this device.)
Have 4 blocks near each other with a switch and a sign saying 4,3,2 or 1 respectively.
10 blocks to the right and 2 blocks down place a block then place 2 more with a 5 block space. 6 right and 3 up place the block. Label them 4-3-2-1 respectively.
Have a 11 block wire or 13 for left to a repeater on the 9th block or 11th for left and on the right side. Place a repeater 2 blocks over with the same wire from it. Connect the left repeaters.
to the code changing module. (You may use bridges of cobblestone for getting over other wire and repeaters for boosting the signal. Construct a XNOR Gate where).
2 of the wires meet. Connect to adjacent outputs with AND gates. These Outputs are connected to final AND gate. Final AND gate if connected to iron door.

### Order-sensitive RS NOR Combo Lock
A door that opens when buttons are pressed in certain order.

(Note: A moderate understanding of logic gates is needed for this device.)

Make a series of buttons, and connect only one to an RS NOR latch. Then connect both the RS NOR latch and a second button to an AND gate, which feeds to another RS NOR latch. Do this continually until you have either filled all of the buttons or are satisfied with the lock. Connect the final RS NOR latch to a separate AND gate with a signal from an enter button. Feed that to the output RS NOR latch. Then connect any of the left-over buttons to the enter button and send reset signals to all of the RS NOR latches. A pressure plate next to a door can reset the door. This type of lock has severe limitations its security. For example, not all the buttons could be used in the pin or there would be nothing to reset the system.

For a lock that can have a combination of any size, using all the buttons, and still have a wrong entry reset the system, you need a different way for it to reset. To construct this, hook up a panel of buttons (any number, but four or more is preferred) to a parallel series of adjacent repeaters. Invert as necessary so that all the repeaters are powered and are unpowered by the press of the corresponding button. These repeaters power a row of blocks. On top of the blocks, place a torch corresponding to the incorrect buttons for the fist number in the PIN. For the correct button/number, place dust under the powered block which leads to a RS NOR Latch. Place a row of blocks above the torches for the incorrect buttons, with redstone dust on top. Then connect this dust to the reset of the first RS NOR Latch. Only the correct button will set the RS NOR Latch and all others will reset it. Connect the output of the RS NOR LATCH to half of an AND gate. After the first row of blocks with the reset torches, place another row of repeaters and another row of blocks. Again place torches for the incorrect buttons and dust under the correct button's line. Power will be fed from the buttons through the rows of repeaters and blocks for as many rows as there are digits in the PIN number. Connect the dust from the correct button to the other half of the AND gate coming from the first RS NOR Latch. Only if the two conditions are met, that the first button was pushed correctly, setting the first RS NOR Latch, and the second button is pushed correctly will the AND gate send a signal to set the second RS NOR Latch. Again, connect a reset line from the incorrect button's torches to the reset of the second RS NOR Latch. Delay the reset signals by one full repeater to give time for the next RS NOR Latch to be set before the reset happens. Continue building the array in the same manner until you reach the desired number of digits. In operation, when a button is hit, each RS NOR Latch checks (through the AND gate) to see if the previous RS NOR Latch is set, and the correct button for this RS NOR Latch has been pushed. Only when the correct buttons are pressed in order, will the signal progress through the conditional RS NOR Latches to the end. Connect the output of the last RS NOR Latch to a door and attach a line to a pressure plate inside the door to reset the last RS NOR Latch.

#### Tutorial Video
Combination Lock RS NOR




There is also another way to make order-sensitive combination locks. It is based on several RS NOR latches that is placed on a row. The RS NOR latches are connected together, and each latch is connected to one button. The combination lock opens when all the latches are activated. To activate all of them, the latches have to be activated in the right order. If wrong button is pressed, the lock automatically sends a reset signal to the first latch, and resets the entire lock. The circuit also has a T flip-flop that controls the output. The T flip-flop turns on and stays on when the right combination is pressed. When the lock is open, all the buttons works like a reset button. This makes it easy to close the door from the outside. Just press a random button. It is also possible to connect buttons that overrides the lock and makes the output signal toggle like on a normal T flip-flop.

#### Tutorial video



#### Combination lock with order-sensitive reset
This is an order-sensitive combination lock with order sensitive reset function. It works like an ordinary order-sensitive combination lock, but in addition it has a function that resets everything when a button is pressed too early. The function consists of AND-gates that sends a reset signal if the previous button hasn't been pressed yet. The lock does not need a reset button because it resets automatically when the code is wrong.




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

