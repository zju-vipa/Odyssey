# Tutorials/Mushroom farming
Mushroom items are useful for a variety of purposes. They are available from three sources: huge mushrooms, mooshrooms and normal small mushrooms.

## Contents
- 1 Huge mushrooms
	- 1.1 Huge mushroom farming
- 2 Small mushrooms
	- 2.1 Spread Mechanics
- 3 Mooshrooms
- 4 Farming methods
	- 4.1 Mooshroom farming
	- 4.2 Basic small mushroom farming
	- 4.3 Tunnel method
	- 4.4 Semi-Automatic Farming
	- 4.5 Fully-Automatic Mushroom Farming
		- 4.5.1 Using water dispensers and a light sensor circuit
		- 4.5.2 Using pistons
		- 4.5.3 Piston/Glass Based "Dry farming"
- 5 History

## Huge mushrooms
Huge mushroom minimum growth requirements
Using bone meal on either a red or brown mushroom causes a huge mushroom to grow if enough room is available, and if the mushroom is planted on the appropriate block. Huge mushrooms can give at least 20 mushrooms when harvested. The image to the right illustrates the minimum growth requirements:

- The wood above illustrates the minimum height required to grow a huge mushroom of that size. Huge mushrooms can be 5, 6, or 7 blocks tall, with the maximum height being 1 block shorter than the available space above it. Thus, if there is a block 7 meters above, the huge mushroom always grows to be 5 blocks tall.
- Theslabsbelow illustrate the area required, 7×7, as well as the fact that the blocks immediately adjacent to the stalk must be free, but not the rest of the bottom row.
- The mycelium on the right shows the area where the required space overlaps due to the smaller footprint of the huge red mushroom.
- The mushroom must be planted on adirt,grass,podzol,mycelium, ornyliumblocks (not shown).
- Placing blocks where the inside of a red mushroom would be does not hinder the growth of the mushroom substantially. Placing blocks directly in the way or outside of the mushroom prevents its growth.  Occasionally much taller (11+ blocks) mushrooms grow when blocked by blocks in the normal growth space below, however this is unreliable and takes significantbone meal.
- By placingdirtblocks around where the stem of the mushroom is supposed to be, you can block the light, allowing you to place the mushroom even closer to the surface. Then, fill up your tunnel and remove the dirt inside of the mushroom once it has grown.

Bear in mind that the huge mushroom may still attempt to grow at a taller height than space is available, failing and wasting a bone meal. It is therefore usually ideal to farm with the maximum space available (7×7×8), so that the bone meal can never fail.

### Huge mushroom farming
The basics of huge mushroom farming involve a 7×7×8 space and suitable ground. If you are outdoors, you can plant the mushroom using podzol, mycelium, or nylium. In the overworld, podzol is more easily available. To make podzol, plant a giant spruce tree with four saplings, and wait for it to grow. When it grows up, chop the tree down and use the newly formed podzol to plant a mushroom and bone meal it up. Planting consumes the underlying block, so you must occasionally regenerate by planting giant spruce again. (Mycelium can spread to the dirt, so no manual work is required.)

Another way to farm mushroom outside relies on timing: dig a 1×1 hole where you want your farm to be. Place water in the 1×1 hole. Then, plant a mushroom in the water and use bone meal on it quickly before the mushroom unplants.

In the nether, nylium is a good choice for growing huge mushrooms on. Note that you can spread nylium to adjacent netherrack blocks by using bone meal on the netherrack.

The extent of automation possible with mushroom farms is close to that of tree farms. You might be able to get some ideas from these harvesters. The bone meal input may require farming too.

## Small mushrooms
Because mushrooms do not grow on areas where the light level is greater than 12, the farmer must carefully consider the placement of light sources. Mushrooms are placeable everywhere but well lit areas or non solid / transparent blocks, and do not require water, sand, or extra space like crops, cacti or saplings.
However, even at night, they can be planted only on blocks where the light level would be less than or equal to 12. The exceptions to this are mycelium, nylium, and podzol, on which they can be planted and remain in full light. They can then spread slowly to other opaque blocks.

The main danger in small mushroom farming is that they must be low-lit indoor rooms, which poses the risk of hostile mobs spawning in the same area (except on Peaceful mode). This can be countered in several ways. The easiest way is to place copious numbers of soul torches, as they emit light level 10, which is dark-enough for mushrooms and lit-enough to prevent mobs.  Another way is to place normal torches two blocks above from where you want your mushrooms to grow (sometimes in tiny holes cut into the ceiling overhead). Another way involves making the farming area just one block high and paving any walkways with slabs and using a water system to channel the mushrooms out of the farm room and into a collection point. This removes most of the danger, since mobs cannot spawn on half-blocks or in one-block-tall areas and any other areas can be lit up. The Nether is a safe place to start a mushroom farm, since mobs there do not spawn in small spaces.

### Spread Mechanics
When a mushroom receives a  random tick, it has a 4% chance of attempting to spread. When this happens, the game chooses a block near the mushroom and, if a mushroom could be planted in the chosen location, a new mushroom appears there; otherwise the attempt fails. The algorithm used to choose the new location for the attempt is not a simple random selection, but a multi-step algorithm that depends partly on which surrounding blocks are valid locations for planting a mushroom.

Some key aspects of the spread algorithm are:

- Mushrooms may theoretically spread up to five blocks away (including diagonally along all 3 axes), though only if the blocks in between are valid mushroom locations. Spreading this far has a low probability as a majority of spreads are within 2 blocks of the original mushroom, and the most common locations are within one block of the original mushroom.
- The algorithm is weighted in a way that favors spread to nearby y-levels. This further reduces the chance of a mushroom spreading far in the y direction.

Note that a block is considered a valid location for a mushroom to be planted if:

- the block at the new location is empty
- the block below the new location isopaque
- the light level at the new location must be < 13 (unless the block below is mycelium, podzol, or nylium)

In addition, mushrooms attempt to spread only if there are fewer than 5 mushrooms of the same type in an area of 9×9×3 around the original mushroom.

## Mooshrooms
Shearing a mooshroom drops 5 of its respective mushrooms and convert it into the normal cow. Every ~5 minutes mooshrooms can enter love mode and make a baby, which can replace any adults that have been sheared.

## Farming methods
### Mooshroom farming
This method involves breeding mooshroom cows or striking Mooshroom cows with lightning, and then shearing them for their respective mushroom type. 5 mushrooms are dropped when sheared. This is a cheap and quick method to obtain large quantities of mushrooms in quick succession.

### Basic small mushroom farming
This method relies on thorough lighting to ensure a monster-free, no-mining-required farm for the beginner mushroom farmer. Create a room two blocks high and as large horizontally as desired. At regular intervals dig one block up into the ceiling of your room, and place a torch to create recessed lighting. This casts light of level 12 at floor height, allowing mushrooms to grow and spread. You can place torches at a distance of up to six squares between each other with no danger of mobs spawning. This setup allows for the fastest mushroom growth. Spread the mushrooms on the floor with room around them to grow and wait.

Another way involves making the farming area just one block high and paving any walkways with slabs and using a water system to channel the mushrooms out of the farm room and into a collection point. This removes most of the danger since mobs cannot spawn on half-blocks or in one-block-tall areas and any other areas can be lit up. The Nether is a safe place to start a mushroom farm since mobs there do not spawn in small spaces.

Farming mushrooms in this way can be rather difficult due to their slow growth. The most efficient method if one must use small mushrooms would be to plant unlike mushrooms in pairs, each pair no less than 9 blocks away from its neighbors -- preferably on mycelium so they can spread in any light level. By planting unlike pairs, one can get 10 mushrooms in a 9×10×3 space instead of just 5 in a 9×9×3 space. Obtaining a high yield requires a significant time and space investment, and typically isn't preferable unless huge mushrooms aren't feasible.

Another option is to prepare a large underground room and use bonemeal to grow huge mushrooms, which can then be mined for multiple mushrooms per mushroom block. In order to secure a reliable source of bonemeal, the player can set up a crop farm and grow wheat, potatoes, carrots, pumpkins or melons as a "fodder crop" and use a composter to convert the produce and any excess seeds into bonemeal.

### Tunnel method
One way of growing a red mushroom on the surface of the world at any time of day without mycelium (using bone meal) is to dig a tunnel starting from several blocks where the mushroom should sprout, and plant the mushroom two or three blocks below the surface at the end of the tunnel. Then, dig a single block chute to the surface from above the mushroom. If the mushroom is deep enough underground, it does not pop off when exposed to the light above it. Once there's light, use the bone meal and see if it grows the mushroom. If it does not, there may be too many blocks in the way of the mushroom, in which case, planting the mushroom closer to the surface may make it grow.

### Semi-Automatic Farming
1. Lay downredstonein lines with 2 blocks in between each line 15 blocks long. Attach a button to this circuit. Fill the spaces in between the lines with sticky pistons. Placedirton top of everything (pistonsand redstone). Place a piston circuit to allow water to spill forward like in the original design. Attach aleverto this circuit. Adjust circuits as needed for length.
2. Place seedmushroomson the dirt on top of theredstone.
3. Press button to dislodge mushrooms, then flip theleverto havewaterbring them down to you. Repeat the design down a hallway, raising the floor one time with each repetition. Allow the water to spill into a central channel and bring the mushrooms to you.

### Fully-Automatic Mushroom Farming
#### Using water dispensers and a light sensor circuit
In the following design, mushrooms are planted on central platforms and new mushrooms spread to side platforms. Water flows once a day through the side platforms delivering the newly-spread mushrooms to hoppers and finally into chests.

On the central platforms, mushrooms can be planted in packs up to four mushroom of each kind. Planting more mushroom increases the spreading speed, but also reaches its cap limit sooner. In the video (that is unlinked in any form), three mushroom of each kind are planted, as it gives higher daily output.

The side platforms should be one block high to improve efficiency. The central platforms should be 3 blocks high. 
In the video (that is unlinked in any form), the central platform uses glass blocks, as mushroom can't spread over glass.

A circuit, using a daylight detector, emits two delayed pulses once a day. Activating and deactivating dispensers containing water buckets, making water flow through the side platforms for about 12 seconds. Enough to deliver every new mushroom spread in the side platforms to a hopper collection point that eventually stores the mushrooms into chests.

The farm can be covered in glass, if the platforms are built in mycelium. They can also be covered with any other non-transparent block.

#### Using pistons
A simple fully automated mushroom farm can be built with the use of pistons. 

First, a room of the height 2 is needed, in this room, place a water stream in the floor, 2 blocks wide. It transports the mushrooms out of the room. Mushrooms should be planted along the bank of the water, leaving every other block empty. Lastly, pistons are required to be placed facing toward the water stream. They need to be placed beside the blocks, where no mushrooms are planted.

The pistons need to be wired to an outside switch, the water stream shall be redirected to your favorite collection point. Then, the room needs to be sealed to be completely dark. The only opening should be 1×1 wide, for the water stream. This being the only opening, spawned monsters cannot leave the room. Eventually, the mushrooms spread to the blocks in front of the pistons. Activating the pistons then harvests the mushrooms and push them into the water stream. The system is reset by deactivating the pistons without any need for replanting.

Higher efficiency can be achieved by multiple arrangements. The system can even be arranged in a room of the height 1, this makes setup more difficult though.

#### 
The idea here is that mushrooms can also be popped off by causing the block beneath them to change to glass. Using pistons, you can push 12 blocks of alternating block/Glass rows causing any mushrooms growing on them to pop off.


The basic set up is two sets of pistons facing each other on either side of the seed mushroom row. Upon pushing a button a signal is sent causing the first group to extend popping off the mushrooms. The signal is delayed 12 ticks (3 repeaters) and the second group of pistons then extends resetting the farm.

Generally this is designed for use in the Nether, where “wet" methods are unavailable. Some benefits over other "dry" methods are simplicity and low resource requirements.

