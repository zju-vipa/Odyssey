# Lava
Lava is a light-emitting fluid that causes fire damage, mostly found in the lower reaches of the Overworld and the Nether.

## Contents
- 1 Obtaining
	- 1.1 Natural generation
	- 1.2 Post-generation
- 2 Usage
	- 2.1 Fuel
	- 2.2 Burning
		- 2.2.1 Java Edition
		- 2.2.2 Bedrock Edition
		- 2.2.3 Fire spread
			- 2.2.3.1 Java Edition
			- 2.2.3.2 Bedrock Edition
	- 2.3 Flow
		- 2.3.1 Flow arrangement tables
			- 2.3.1.1 Overworld and the End
			- 2.3.1.2 The Nether
	- 2.4 Lava and water
	- 2.5 Light source
	- 2.6 Other
- 3 Farming
- 4 Sounds
- 5 Data values
	- 5.1 ID
	- 5.2 Block states
	- 5.3 Fluid states
- 6 Achievements
- 7 Advancements
- 8 History
	- 8.1 Data history
- 9 Issues
- 10 Trivia
- 11 Gallery
	- 11.1 Screenshots
	- 11.2 In other media
- 12 References
- 13 External links

## Obtaining
Lava can be collected by using a bucket on a lava source block or a full lava cauldron, creating a lava bucket. Lava may be obtained renewably from cauldrons, as pointed dripstone with a lava source above it can slowly fill a cauldron with lava.

In Java Edition, lava does not have a direct item form, but in Bedrock Edition it may be obtained as an item via inventory editing or add-ons.

### Natural generation
During world generation, lava replaces air blocks generated in caves and canyons between Y=-55 and Y=-63. Aquifers are sometimes filled with lava below Y=0. Lava does not replace air blocks inside mineshafts, monster rooms, amethyst geodes, or strongholds.

Lava can also occur as lava flows from a single spring block, pouring down walls into pools. The spring block can be on the side of a cave, ravine, mineshaft, or stone cliff above ground.

Lava also generates as small lava lakes, which can be found above Y=0 within any biome.

Two blocks of lava can also be found in plains, snowy plains, and desert village weaponsmith buildings, or one source in savanna village weaponsmith buildings.

Fifteen blocks of lava can be found in the end portal room of a stronghold: 3 along each side wall, and 9 below the portal frame.

Lava also generates in woodland mansions: two blocks of lava generate in the "blacksmith room", and 25 blocks of lava generate in a secret "lava room".

In the Nether, lava is more common than water is in the Overworld. Seas of lava occur, with sea level at y-level 32, about a quarter of the total height of the Nether (as the usable space in the Nether is 128 blocks tall). They can extend down to about y-level 19-22. Lava also randomly appears in single blocks inside netherrack formations. Lava is also generated as a single source in well rooms in nether fortresses. There are also large pockets of lava generated under y-19 and can reach all the way down to bedrock level. These pockets are generally over 12 blocks in height and often connect to a large lava lake on y-32; the size of these pockets in 1.18 can range from the size of a singular pre-1.18 ravine to multiple ravines combined.

Lava generates as delta shapes, which can be found commonly in the basalt deltas biome. Lava also generates in ruined portals and bastion remnants.

### Post-generation
Unlike water source blocks, new lava source blocks cannot be created in a space by two or more adjacent source blocks. However in Java Edition, if the game rule lavaSourceConversion is set to true, new lava source blocks can form in a similar way to water source blocks.

## Usage
### Fuel
When used in a furnace, a bucket of lava lasts 1000 seconds (100 items).

### Burning
What it looks like inside lava.
What it looks like inside lava using Fire Resistance in Java Edition.
Most entities take 4 damage every half-second while in contact with lava, and are set on fire. An entity/player in lava also has its remainingFireTicks set to 300, setting it on fire for 15 seconds. This timer is reset to 300 every tick that the victim spends in lava, so it starts counting down once the victim leaves the lava. Once the victim does exit the lava source, it burns for just under 15 seconds, taking fire damage 14 times. This is due to the fact that for the first tick outside of lava, its remainingFireTicks decreases to 299, and entities take fire damage when remainingFireTicks is a multiple of 20 and greater than 0. If the victim touches water or rain falls on it, the fire is extinguished, but the lava continues to damage them directly.

In addition, a dense fog effect is applied for players under lava to obscure vision. This can be slightly mitigated via the Fire Resistance effect.

An entity/player moving in lava has their horizontal movement speed reduced by 50% and their vertical movement speed reduced by 20%.

In Bedrock Edition, a player with the Fire Resistance effect or a total Fire Protection of 7 or higher does not catch fire. 

Most of the Nether mobs (blazes, ghasts, magma cubes, striders, wither skeletons, zoglins, and zombified piglins), agents, NPCs, vexes, shulkers, wardens, withers, and players or mobs affected by the Fire Resistance effect are not damaged when touching lava. 

The embers or fireballs that fly out of lava are purely decorative and do not cause fires or damage to entities. When rain falls on lava, the black ember particles appear more frequently.

A player in lava lasts a few seconds before dying:

