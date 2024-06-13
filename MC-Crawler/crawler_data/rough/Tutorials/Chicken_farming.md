# Tutorials/Egg farming
Egg farming is the process of collecting a large number of chicken eggs from chickens. From an automated source of eggs, a chicken farm which produces additional end products like raw/cooked chicken and feather can be constructed with the addition of egg-dispensing and chicken-killing systems.

The chicken is the most farmable animal in Minecraft. Unlike cows and sheep, it does not require any food to grow up or to reproduce. No matter where the chicken is kept, everything just happens automatically. In addition, cooked chicken is almost as good as other cooked meats for restoring hunger.

## Contents
- 1 Catching or hatching a chicken
- 2 Setting up the farm
	- 2.1 3x3x4 Automatic Farm
	- 2.2 Building up
	- 2.3 11x11x6 Automatic farm
		- 2.3.1 Materials
		- 2.3.2 Building it
		- 2.3.3 Running the farm
	- 2.4 Joghurts Design
	- 2.5 Trench Farm
	- 2.6 Water Egg farms
	- 2.7 Realistic Chicken Coop
- 3 Chicken farming and cooking
	- 3.1 Extending the 3×3×4 farm
	- 3.2 Filtering out immature chicks
	- 3.3 Full automation
		- 3.3.1 Example farms
- 4 Trivia

## Catching or hatching a chicken
In general, you'll want to first build a pen to hold them. Single-height wooden fences (or a small cave) will suffice, but either way it's best to add an "entry lock": a fenced space with gates leading both to the pen and to outside. This will help prevent escapees: if one of the gates is always closed, the chickens' pathfinding will never see an escape route to the outside.

The usual way to capture chickens is to hold seeds of any kind, which will make any chickens nearby follow you across the landscape and right into the pen. Alternatively, if you already have slimeballs and string, you can use leads to drag them along; this will mostly keep them from wandering away. You will need a separate lead for each chicken. With care, chickens can even be led across water, as they will follow your boat.

Another option is to collect eggs and throw the eggs into your closed pen. There is only a 1 in 8 chance of spawning a chicken when you throw an Egg, so you should try to collect at least one stack. They will take some time to grow to adulthood but once you have at least one adult chicken it will start producing eggs and with two or more adults you can breed them with any seeds.  Each adult chicken will lay an average of 8 eggs per hour.

When hatching large numbers of chickens, a good rule of thumb is that the chickens will need well over a real-time hour to replace the eggs used to hatch them. Nights skipped in a bed do not count toward this time, and the chunk(s) containing the chicken must remain loaded (that is, near a player or in the spawn chunks). This also assumes you are collecting all the eggs -- remember, loose items like eggs despawn after 5 minutes.

## Setting up the farm
You can farm chicken eggs the traditional way, where you have to run around and collect chicken eggs all the time.

Alternatively, you can follow one of the tutorials below, to create a farm that channels eggs to a single point. Most such will do the same for chicken meat, feathers, and even experience orbs as well.

### 3x3x4 Automatic Farm
This is a minimal egg farm consisting of 8 blocks, a hopper and chest: it's incredibly efficient in versions prior to 1.11, when it could house hundreds of chickens in an 1×1 area. Since version Java Edition 1.11's introduction of the maxEntityCramming gamerule, the number has reduced to 24. Check your servers settings on cramming before settling on this farm solution (this is not a problem on bedrock edition). Alternatively, you can place a single vines block in the space that the chickens occupy, and they will not suffer from entity cramming damage.

Bottom Layer















2 Middle Layers
















The opening at the top can either be used as a one-way entrance or simply sealed. Bait a chicken in or throw some eggs at the interior walls to start the system.

### Building up
This system may be extended with a larger living area with all hoppers eventually pointing to one that goes to a chest. At a certain point, the system becomes prone to mob spawns, and slabs can be laid over hoppers to deter mobs spawning. (Hoppers can fetch dropped eggs through a slab.) As using many hoppers becomes too expensive, water flow is used instead of the initial collection in the following version.

### 11x11x6 Automatic farm
The hopper egg farm is a relatively simple contraption, which does not require access to nether quartz: On the main floor, chickens are contained by water while they grow and lay eggs, which also wash the eggs into a hopper; from there the eggs go back into the system's supply chest. This chest feeds an automatic hatcher, which can refill the main floor after a harvest. The hatcher is controlled through a despawn timer, which prevents the system from spawning chickens ad infinitum (or at least until the server crashes).

This farm will be surrounded on the surface by an 11×11 fence or wall, with doors or gates at or near the middle of a side. There is a pillar and (at least a) partial roof in the center, and an "egg room" dug 3 blocks deep beneath that. The egg room and its pillar can be adapted to other farm layouts. You will also want a tunnel leading to the egg room, with space to get at the chest and other devices to retrieve meat and feathers), and the switches to trigger or disable the hatcher. The chickens are contained primarily by water, so the farm partly resists any problems with chickens walking through walls and fences. The schematics are below. The gold and stone-brick blocks represent "any full block", but the blocks shown as gold must also be opaque, while stone-brick blocks can be opaque, transparent, or in some cases air.


Automatic 11x11 Egg farm Plans View at: Tutorials/Egg_farming/Egg Farm 12 [edit]
[Schematic Help] 


#### Materials
- The base machinery includes threedroppers, adispenser, threehoppers, a chest, a couple oflevers, two redstone repeaters, two redstone torches, and six redstone dust. Making that equipment from scratch will cost a minimum of 6 smooth stone, 15 iron, 29 cobblestone, 10 "logs" of wood (with some bits left over), 18 redstone dust, and 3 string. Also needed are 7 solidopaqueblocks, and several that can be opaque or transparent. The chest can optionally be doubled (another 2 wood), and you may well want another chest elsewhere in the egg room, for ordinary storage.
- The 9×9 floor inside the room will need 78 additional blocks or slabs (if the optional second chest is used, then at least the space above it needs to be a slab). You may want a trapdoor from the chicken floor to the egg room; the water not only won't flow through the trapdoor, but will generally prevent chickens from slipping down there too.
- The pillar will be a slab and another two blocks, one of which should be a jack-o-lantern or other light source. Even a block with four torches will do, but you do need a light there to keep the chicks from drowning themselves at the edges.
- The roof will need at least 10 solid blocks to intercept eggs (3×3 over the dispenser, and one topping the pillar). The rest of the ceiling can be filled in with slabs.
- The walls should be solid blocks, at least 2 high (the ceiling layer will usually be a third) This will cost most of 80 blocks of stone and/or glass (or 20 wood "logs" converted to planks). Doors can be best placed in the middle of any wall, or all four of them. Given creepers, it's much safer to make at least the floor and the bottom row of the wall out of blast resistant blocks: Any stone will do, as will brick or hardened clay, or even obsidian. This will minimize the mess if it does get blasted, and make it much easier to fix up. Making the top row out of glass blocks lets you see in and out of the farm, which helps avoid creeper blasts in the first place. You can also surround it with other protections such as a moat, which would prevent creepers from damaging the blocks even if they do explode.
- If you've been to the Nether, you can add a comparator and redstone lamp, with a bit of dust and maybe a repeater to connect them.  This lets you set up a convenient display outside the building, to show when the egger has enough eggs for a full run.

#### Building it
Once the walls are set up, it is easiest to build the egg room from above. Make sure to offset the room so the input hopper is in the center of the floor, and light the egg room properly. When orienting the room, think about where you want the access tunnel to go. As shown, an access corridor leading to the lower left of the diagram allows getting at all the containers and both switches.

The hatcher consists of two droppers facing up, with a dispenser facing up on top of them. These are fed by the hoppers, with the chest providing extra storage, and driven by a 3-clock. The clock is on the right edge of the diagram, from the block with the lever southwards and downwards. That lever lets you disable the hatcher completely—place it and turn it on as soon as the clock is built, so you can build the rest without clicking noises.

The despawn timer (upper edge of diagram) is a dropper facing down over pressure plate. It works by dropping an item onto the pressure plate, which will turn off the torch and enable the clock until the item despawns. The block in front of the pressure plate helps avoid accidentally picking up the item as you pass near, but if you go close enough you can still pick it up and cut off the timer. Once you've built and connected the despawn timer, you can turn the lever back off, as the inactive timer will keep the clock disabled. The despawn timer's dropper can be loaded with any disposable item, such as surplus seeds or eggs. The block in front of the pressure plate is just to make it a little harder to accidentally pick up the item—glass will let you see if the item is on target, or has missed the pressure plate.

Once the egg room is built and closed over, continue with the central pillar: Above the hopper, place a top slab, then two blocks above that. You can make the lower one a jack-o-lantern, for simple lighting. From the top block of the pillar, extend a roof out over the dispenser and at least one square around it in every direction. Put a torch on the roof to avoid unfortunate monster spawns. Note that if you use slabs, you may get chicks on top of the roof. If you have the minimum roof, they'll just fall into the water, but if you want to extend the roof to the edges, use non-transparent blocks to avoid escapees.

Note that the dispenser is purposely separated from the collection hopper/central pillar, to allow for the dispenser's variable aim. The slab (or other transparent block) between them is only needed if you add the optional chest, but if you do, an opaque block there will prevent the chest from being opened. Note that as of version 1.14, you can place the optional chest without connecting it to the main chest. It will still feed into the egger, but may be useful for stashing extra eggs, especially when you are about to harvest and want space in the main chest for feathers and meat.

Last of all, place buckets of water in each corner; they will flow to the central pillar. Load up your chest with eggs and/or lead in some chickens, and just hit the button. Then let the eggs accumulate until you have enough for a full run (at least a dozen stacks in the chest).  (If you are starting with just a few chickens and/or eggs, an early run with just a few stacks can get you a few more chickens to fill the system more quickly.)  If you have many eggs, you might want to do a longer run by disabling the despawn timer (add a lever to the block for its output torch), or just do a second run immediately when the first finishes.

If you have glowstone and nether quartz, you can optionally add a couple of top slabs on level one, next to the hoppers.  Atop these you'll want a comparator facing out from the main chest, and next to it something to provide a comparison signal of 8.  This corresponds to 13 stacks in the chest, which is enough for a full run.  A cake with three slices eaten will do fine.  You can then run a redstone trail from the comparator to a redstone lamp.  Embedding the lamp in the ground near the entrance can let you reach it with 8 or less dust; any further, and you'll need a repeater in there too.  This is not shown in the schematic, because without it this build does not need Nether materials.

#### Running the farm
The clock is normally disabled by either the inactive timer, or by the lever, either of which will disable the clock. With the clock disabled, the incoming eggs will fill first the bottom dropper, then the bottom hoppers, then the chest, and finally the intake hopper. This gives a total of 52 stacks storage, or 79 with the optional second chest. 

Now, 79 stacks of eggs would produce an average of 163 chickens, which may be enough to seriously lag the game when you are nearby. Worse, they will take over 15 minutes to feed through, because the hoppers are slower than the clock. If you leave the hatcher running much longer than that, the first chickens will grow up and start laying eggs! At that point, you'll be facing exponential growth, limited only by the speed of the hoppers. If the hatcher is left running after the first generation grows up, the system will be producing 2.6 chickens a minute at first, but if the game doesn't crash, it will eventually peak at 18 per minute, 363 per game day. In such numbers, the chickens will overflow any enclosure, and the huge numbers will cause the game to lag badly. However, if you don't mind risking "Chickmageddon", you can skip the despawn timer forming the top two rows of the egg room. In more recent versions of Minecraft, the crowding will eventually cause chickens to start suffocating, but for this design that may not be enough to prevent problems.

This despawn timer and inverter will enable the clock for 5 minutes only, letting you hatch 500 eggs at a time (about 31 stacks, producing an average of 64 chickens). There is a bit of a trick here: Since the clock has a period of 0.6 seconds, 300 seconds gets you 500 cycles, but the clock and dispenser are faster than the hoppers feeding the dispenser. The hoppers alone could deliver less than 375 eggs to the dispenser, but the eggs in the bottom dropper give just enough of a head start to cover a batch of 500. As noted above, the chickens will need a bit over a real-time hour to replenish the eggs used; if you don't want to wait for that, you can harvest the chickens as soon as they're mature, then run the egger again and let the second batch refill the chests while you do other things.







### Joghurts Design
Joghurts egg-farm
Bottom layer of Joghurts egg farm
Just dig a square hole 11 by 11 blocks and one block deep, then dig one more layer in a circle shape. You'll need an additional one-block-hole in the center where the water and the eggs will flush out.

Now you need to build the “isle" to prevent the chicken from also being flushed out and to give them some ground to lay eggs that can hatch to slowly expand the total population of chickens on your farm.

Connect the center drain hole to your system from below, place water in the corners, and you're good to go.

### Trench Farm
The "14 Second Compact Egg Farm" is a farm designed by Minecraftmaximizer for the Minecraft 1.5 release which takes only 14 seconds to build. It costs 8 logs of wood, 10 ingots of iron, two arbitrary blocks, and an optional ladder. It is essentially the 3×3×4 farm put in a pit.

This farm is begun by digging a hole 3 deep, by 4 long, by one wide hole. The chests and hoppers are placed on the bottom (a double chest on one side, two hoppers feeding into it on the other). The ladder can go over the chests. Two blocks then go over the hopper next to the chest, to keep the chickens in place. Then you can hatch chickens over the exposed hopper, and eventually collect eggs from the chest.

Because it has a volume of only twelve blocks, this farm is one of the most compact farms possible, especially with the inclusion of hoppers. A video demonstrating it and a schematic:

Compact Pit Egg Farm with Hopper View at: Tutorials/Egg_farming/Compact Pit Egg Farm [edit]





### Water Egg farms
Most current egg farms have the chickens supported by water, with their eggs falling through the water into a collection area below. The water can be supported by signs or ladders, which will keep it from flowing into the collection area.

For a fairly space efficient design, build walls around a 2×2×2 column. The bottom two spaces are the collection area (make sure to leave a door), and the upper of those has 4 signs to support the water. The next two layers are a water pool with no flow, especially not downwards. It's probably best to make the whole pool of source blocks. The chickens will go in and above the water—there should be a 1 or 2 tall gap above the water for the chickens to breathe in. The walls around and above the water should be glass blocks, to keep the chickens from suffocating each other against the walls.

After this is constructed, eggs can be thrown directly up from the collection area. The chickens will float on the water and their eggs will drop to the floor for easy collection, where they can be thrown back to hatch more chickens. When meat or feathers are needed, a sword can be used to pick off chickens from below. A water flow can be placed in the collection area to bring the eggs to one block, but this makes throwing eggs and collecting meat or feathers more difficult.

Automatic Egg Farm
The static water of the design above lets some eggs get stuck on signs. Expanding the pool area (the "Flowing Egg Farm") allows a water current to gather eggs to the center, and the inward flowing current helps prevent chickens from "phasing" through the walls, allowing far more chickens to be kept. This design can be "squared off", flowing to a central 2×2 hole, or it can simply be extended horizontally, perhaps with another water current carrying eggs down the "collection corridor". It need not be the full 18 blocks wide, either, as long as the collection area is under where the currents meet.


Basic Water Egg Farm Gallery View at: Tutorials/Egg_farming/Water Egg Farms A [edit]

Another large egg farm:




### Realistic Chicken Coop
Put a Chicken on top of each Hopper. Each coop can house 6 Chickens. You can also switch the oak wood planks for stone or cobblestone for a nicer look depending on the biome or just your choice.



Ground Layer































































Layer 1































































Layer 2































































Layer 3
























































Layer 4

















































Layer 5















































## Chicken farming and cooking
A chicken farm produces chicken products including raw chicken, cooked chicken, and feathers. Generally speaking, such farms combine a source of eggs, a dispenser to generate chickens, and a killing mechanism to obtain the loot from the mature chickens.

### 
A simple modification with the egg/feather hopper can be a dropper/hopper path pointing back to an egg dispenser under clock circuit pulses. As the dispenser creates chicks by re-throwing the eggs into the chicken area, a closed cycle for generating more and more eggs and chickens form. If left unmanaged, it's likely that the game would lag with a huge number of chickens, possibly before the maxEntityCramming gamerule kicks in.

A block of water laid on top of the air block controlled by air, controlled by a dispenser with a bucket can be used as a "kill switch" for obtaining cooked chicken. The down-flowing water stops the chickens from swimming up, and a top lid made of trapdoor would guarantee suffocation. Replace the block of water with a block of lava to get a cooked-chicken farm.

### Filtering out immature chicks
To filter out immature chicks which produce no loot, lay a block of lower-half slab over the hopper. This slab would stop water or lava from invading, while still allowing taller, grown-up chicken to suffocate or burn.

### Full automation
An obvious first modification of the full automation step is replacing the kill-switch mechanism with a mostly persistent source of death. Therefore, one should use the slab construction to wait for the immature ones to grow. However, this is not enough as this system kills mature chicken instantly and provides no chance of replenishing the egg supply.

The fix involves adding another dedicated egg farm. Just replace the input for the closed-cycle egg dispenser with a collecting hopper of an independent, normal egg farm, and you are ready to go. You may use a large chest to equally divide eggs produced from the extra farm for egg collection and chicken farming. You can control the generation rate by controlling the egg input. The point of the farm is that adult chicken in an egg farm will provide an endless supply of eggs. We can send these eggs to a dispenser in another farm where they get killed and turned into meat.

Example farm with 1/2 of the egg output used for making lava-roasted chicken:



|  |  |  |  |  |  |  |
|--|--|--|--|--|--|--|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |

Dispensers are connected to clock circuits.

Timing: a baby chicken takes 20 minutes to grow up; a chicken 5–10 minutes to lay an egg; an egg has some 1/8 chance to spawn a baby chicken. Some redstone controls on the egg-feeding hopper can be used to limit the amount of eggs put into the system in each cycle.

#### Example farms
- Frilioth’s Chicken cooker




- 
	- Frilioth puts the dispenser at the slab (chicken) level in the meat farm. This allows fewer layers of construction to be used and makes the design much simpler.
	- Another innovation is that the system is self-powering: by letting a comparator analyze the first (egg-carrying) hopper and an observer amplifying the signal, the egg-shooting dispenser can automatically fire (twice) without a clock circuit constantly working.
	- Instead of being constantly there, the lava is controlled by another dispenser to only appear for two ticks. There is no real benefit to this level of caution, before 1.14 at least.
	- Since 1.14 the lava destroys the cooked-chicken drops almost instantly. Frilioth has published aguide to upgradethe farm. The idea is to replace the hopper with aMinecart with Hoppersitting directly on a hopper while keeping the same slab mechanism. The minecart collects items much faster so all products can be saved from the flame.



- Compact 1.16+ Design for Java, this design by Cheesedud6 has a lever to switch between cooked chicken/feathers and eggs. Target blocks help make the design compact.







