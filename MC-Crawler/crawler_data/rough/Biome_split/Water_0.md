# Water
Water is a fluid that naturally generates abundantly in the Overworld.

## Contents
- 1 Obtaining
	- 1.1 Natural generation
- 2 Usage
	- 2.1 Appearance
	- 2.2 Swimming
	- 2.3 Spreading
		- 2.3.1 Flow arrangement tables
	- 2.4 Source blocks
	- 2.5 Current
	- 2.6 Light
	- 2.7 Color
		- 2.7.1 Java Edition
		- 2.7.2 Bedrock Edition
	- 2.8 Water and lava
	- 2.9 Interactions with mobs
		- 2.9.1 Direct contact
		- 2.9.2 Drowning
	- 2.10 Slower mining speed
	- 2.11 Explosions
	- 2.12 Hardening concrete powder
	- 2.13 Sponges
	- 2.14 Dripping
	- 2.15 Vertical transport
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
	- 4.3 Fluid states
- 5 Achievements
- 6 Advancements
- 7 History
	- 7.1 Data history
- 8 Issues
- 9 Trivia
- 10 Gallery
	- 10.1 Textures
	- 10.2 Screenshots
- 11 See also
- 12 References
- 13 External links

## Obtaining
Water can be collected by using a bucket on a water source block or a full water cauldron, creating a water bucket.

In Java Edition, water does not have a direct item form, but in Bedrock Edition it may be obtained as an item via inventory editing or add-ons.

### Natural generation
Water naturally generates in the Overworld to form oceans, rivers and springs. The water level is at layer 63 near oceans and rivers, but changes depending on location due to the aquifer system, filling some carvers, noise caves and canyons with water at different levels. Water also generates as small puddles on the floor next to dripstone clusters, and as clay pools on the floor of lush caves.

Water also generates in villages, desert wells, strongholds, woodland mansions, ancient cities and ocean monuments. 

Water never generates in the Nether and instantly disappears if placed there with a water bucket. However, water can exist in the Nether in a cauldron. Water can also be placed in the Nether using commands such as /setblock and /fill. Although it does not naturally generate there, water can be placed and function normally in the End.

In Bedrock Edition, water also generates as part of ocean ruins with loot chests, but only two water blocks generate: 

- One water block generates inside the loot chest, making it awaterloggedloot chest.
- The other water block generates on top of the loot chest.

These water blocks generate even if the ruin is located on the surface.[1] This is not the case in Java Edition; if an underwater ruin generates on the surface, no water generates.[2] This also happens with shipwrecks.

Water spends most of its time as stationary, rather than flowing – regardless of its level, or whether it contains a current downward or to the side. When specifically triggered by a block update, water changes to 'flowing', updates its level, then changes back to stationary. Water springs are generated as flowing, and oceans, and rivers are generated as stationary. This happens before most types of generated structure are created, and the main cause of water "glitches" is that generated structures do not trigger a block update to let water flow into them.

## Usage
### Appearance
Water uses a translucent animated texture that is tinted differently in different biomes. In Java Edition, water in cauldrons is completely opaque.[3]

Unlike other translucent blocks such as ice, stained glass and tinted glass, water shows the opposite sides of its external planes when viewed from within and from outside.[4] However, it applies only to the top plane and four side planes; the bottom face is always unseen from above.[5]

### Swimming
Main article: Swimming
The button for swimming is the same as the button for jumping; non-swimming players and mobs sink slowly in water. Holding the swim button raises the player through the water, and when the surface is reached, the player bobs up and down. The crouch button can be used to sink faster. The sprint button can be used to put the player in "swim mode" when the player is completely submerged in water. When in swim mode, the player is horizontal and one block high. The player has an arm-waving animation when viewed in third person or by other players.

Swimming in water is considerably slower against currents (see Current below), but faster when going with the current.

Most mobs that can stand can also swim any time they are in water, except for iron golems, piglins, hoglins, striders, piglin brutes and undead mobs. This can lead to drowning if the water is falling from above.

Water of any depth prevents any entity, including the player, from sustaining falling damage if they fall into it, regardless of the distance fallen.

Being inside of water also imparts a fog effect, tinted accordingly.

### Spreading
Main article: Fluid § Spread
An image showing water's spreading distance
Water spreads horizontally and downward into nearby air blocks. Water can spread downward infinitely until stopped by a block, and 7 blocks horizontally from a source block on a flat surface. Water spreads at a rate of 1 block every 5 game ticks, or 4 blocks per second.

When spreading horizontally, a weight is assigned to every direction water can flow. For each direction, this weight is initially set to 1000. Then, for every adjacent block it can flow into it tries to find a way down that is reachable in four or fewer blocks from the block it wants to flow to. When found, the flow weight for that direction is set to the shortest path distance to the way down. Finally, water spreads in the directions with the lowest flow weight.

Spreading water extinguishes fire and washes away certain types of items or placed blocks, causing them to drop as items and then carrying them along in the flow until the edge of the spread. Affected items include plants (except trees), snow, torches, carpets, redstone dust and some other redstone components, cobweb, end rods, heads, and flower pots.

