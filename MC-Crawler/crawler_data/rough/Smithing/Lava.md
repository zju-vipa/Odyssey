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

#### Java Edition
- 2.5 seconds with no armor
- 3.5 seconds with full leather armor, no enchantments
- 4 seconds with full gold armor, no enchantments
- 4.5 seconds with full chain armor, no enchantments
- 5.5 seconds with full iron armor, no enchantments
- 10.5 seconds with full diamond armor, no enchantments
- 11 seconds with full netherite armor, no enchantments

#### Bedrock Edition
- 2.5 seconds with no armor
- 3.5 seconds with full leather armor, no enchantments
- 4.5 seconds with full gold armor, no enchantments
- 5 seconds with full chain armor, no enchantments
- 6.5 seconds with full iron armor, no enchantments
- 12.5 seconds with full diamond armor, no enchantments
- 12.5 seconds with full netherite armor, no enchantments

If the player is wearing armor enchanted with Fire Protection, they can last even longer. With the maximum bonus, the damage is small enough that the natural healing from a full hunger bar can outpace it,‌[JE  only] so a player could survive indefinitely as long as they have food and their armor holds up (non-netherite armor is damaged by lava). This maximum bonus can be obtained by wearing 2 pieces of armor with Fire Protection IV and 1 with Protection IV, or 1 piece of armor with Fire Protection IV and 3 with Protection IV.

#### Fire spread
Lava can cause fires by turning air blocks to fire blocks.

In order for air above lava to turn to fire, a block adjacent to the air has to be flammable, or one of the wood-constructed non-flammable blocks. Since catching fire depends on air blocks, even torches or lava itself can prevent a flammable block from catching fire.  Additionally, not all flammable or wood-constructed blocks can be ignited by lava.

The lava of any depth can start fires this way, whether or not it appears to have a current.

Additional conditions must be met, depending on the edition of Minecraft.

##### Java Edition






































































Example for JE. The orange area represents areas where air could catch flame if the gray and orange areas contain flammable blocks. The wood is all at a safe distance.



Air block must be in a 3×1×3 area right above the lava or in a 5×1×5 2 blocks above the lava.

An air block in the 5×1×5 area does not catch on fire if the 3×1×3 area is completely filled, even if the latter is filled with flammable blocks.

##### Bedrock Edition
The block to be set on fire must be in a 3×3×3 cube centered on a lava block, above which there must be either air or an ignitable block.

### Flow
See also: Fluid

Lava flows from "source blocks". Most streams or "lava-falls" come from a single source block, but lava lakes (including the "flood lava" in the bottom 10 layers) are composed entirely of source blocks. A source block can be captured only with a bucket.

In the Overworld and the End, lava travels 3 blocks in any horizontal direction from a source block. Lava flows far more slowly than water (1 block every 30 game ticks, or 1.5 seconds), and sourceless lava flows linger for a short time more. In the Nether, lava travels 7 blocks horizontally and spreads 1 block every 10 game ticks, or 2 blocks per second, which is half the speed as water in the Overworld. In all dimensions, lava spreading uses the same mechanic as water: for every adjacent block it can flow into it tries to find a way down that is reachable in four or fewer blocks from the block it wants to flow to. When found, the flow weight for that direction is set to the shortest path distance to the way down. (This can result in lava flows turning toward dropoffs that they cannot reach in the Overworld and the End.)

Flowing lava destroys the following in its path: saplings, cobwebs, tall grass, dead bushes, wheat, flowers, mushrooms, snow on ground (but snow blocks are immune), lily pads, vines, levers, buttons, all three types of torches, redstone, repeaters, end rods, and rails. Sugar canes hold back lava, but disappear if the sugar cane's water source is destroyed by the lava. Lava also slows down entities, including those that are normally immune to lava damage.

Using redstone wire, a one-block lava flow can be redirected by supplying power to the source block, which causes it to reset the flow toward the now-nearest terrain depression. It cannot, however, be reversed. This re-calculation is made because of the redstone wire when toggled changes the block from redstone (on) to redstone (off). Whenever a block updates on any side of the lava, the lava re-calculates where to flow, but does not cut off its current direction of flow. In Bedrock Edition using the /setblock command can be used to create stationary lava without the use of barriers. 

Flowing lava can push entities.

#### Flow arrangement tables
##### Overworld and the End
|   |   |   | 4 |   |   |   |
|---|---|---|---|---|---|---|
|   |   | 4 | 3 | 4 |   |   |
|   | 4 | 3 | 2 | 3 | 4 |   |
| 4 | 3 | 2 | 1 | 2 | 3 | 4 |
|   | 4 | 3 | 2 | 3 | 4 |   |
|   |   | 4 | 3 | 4 |   |   |
|   |   |   | 4 |   |   |   |

| Range |        | Height in blocks |
|-------|--------|------------------|
| 1     | block  | 1                |
| 2     | blocks | 0.75-1           |
| 3     | blocks | 0.5-0.75         |
| 4     | blocks | 0.25-0.5         |

##### The Nether
|   |   |   |   |   |   |   | 8 |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   | 8 | 7 | 8 |   |   |   |   |   |   |
|   |   |   |   |   | 8 | 7 | 6 | 7 | 8 |   |   |   |   |   |
|   |   |   |   | 8 | 7 | 6 | 5 | 6 | 7 | 8 |   |   |   |   |
|   |   |   | 8 | 7 | 6 | 5 | 4 | 5 | 6 | 7 | 8 |   |   |   |
|   |   | 8 | 7 | 6 | 5 | 4 | 3 | 4 | 5 | 6 | 7 | 8 |   |   |
|   | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |   |
| 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|   | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |   |
|   |   | 8 | 7 | 6 | 5 | 4 | 3 | 4 | 5 | 6 | 7 | 8 |   |   |
|   |   |   | 8 | 7 | 6 | 5 | 4 | 5 | 6 | 7 | 8 |   |   |   |
|   |   |   |   | 8 | 7 | 6 | 5 | 6 | 7 | 8 |   |   |   |   |
|   |   |   |   |   | 8 | 7 | 6 | 7 | 8 |   |   |   |   |   |
|   |   |   |   |   |   | 8 | 7 | 8 |   |   |   |   |   |   |
|   |   |   |   |   |   |   | 8 |   |   |   |   |   |   |   |

| Range |        | Height in blocks |
|-------|--------|------------------|
| 1     | block  | 1                |
| 2     | blocks | 0.75-1           |
| 3     | blocks | 0.625-0.75       |
| 4     | blocks | 0.5-0.625        |
| 5     | blocks | 0.375-0.5        |
| 6     | blocks | 0.25-0.375       |
| 7     | blocks | 0.125-0.25       |

### Lava and water
Main article: Fluid § Mixing
Water and lava can produce stone, cobblestone, or obsidian based on how they interact. Lava can also generate basalt when above soul soil and touching blue ice.

### Light source
Lava blocks emit a light level of 15.

### Other
If there is lava flowing above a block, the lava seeps through.
Lava above a non-transparent block (does not include stairs, fences, and slabs) produces dripping particles on the underside of that block. These droplets do not do anything other than warn the player that a deluge of lava lies above that block. The particles function identically to their water counterparts, except that they drip slower.

Flowing lava can set off tripwires because it breaks placed string. Lava triggers a tripwire only once.

Any item dropped into lava is immediately destroyed, except for netherite-related items. Lodestones, however, can be destroyed by lava despite containing netherite.[1]

Lava can be placed in an empty cauldron.

If lava is above a non-transparent block supporting pointed dripstone, dripping particles are created on the end. These can fill cauldrons with lava.

## Farming
Main article: Tutorials/Lava farming
Lava farms can be created by placing a lava source block on top of a solid block and placing a pointed dripstone and a cauldron underneath it.

## Data values
### ID
Java Edition:

| Lava  | Identifier | Form  | Block tags            | Translation key        |
|-------|------------|-------|-----------------------|------------------------|
| Block | `lava`     | Block | `strider_warm_blocks` | `block.minecraft.lava` |

| Lava          | Identifier     | Fluid tags |
|---------------|----------------|------------|
| Fluid         | `lava`         | `lava`     |
| Flowing Fluid | `flowing_lava` | `lava`     |

Bedrock Edition:

| Lava       | Identifier     | Numeric ID | Form                         | Item ID[i 1]   | Translation key          |
|------------|----------------|------------|------------------------------|----------------|--------------------------|
| Flowing    | `flowing_lava` | `10`       | Block & Ungiveable Item[i 2] | Identical[i 3] | `tile.flowing_lava.name` |
| Stationary | `lava`         | `11`       | Block & Ungiveable Item[i 2] | Identical[i 3] | `tile.lava.name`         |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑ a bUnavailable with /give command
3. ↑ a bThe block's direct item form has the same id as the block.

Lava spends most of its time as stationary, rather than 'flowing' – regardless of its level, or whether it contains a current downward or to the side.  When specifically triggered by a block update, lava changes to 'flowing', update its level, then change back to stationary.  Lava springs are generated as flowing, and lava lakes are generated as stationary.

### Block states
See also: Block states

Java Edition:

| Name  | Default value | Allowed values                                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| level | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | If bit 0x8 is set, this fluid is "falling" and spreads only downward. At this level, the lower bits are essentially ignored, since this block is then at its highest fluid level. This level is equal to the falling lava above, equal to 8 plus the level of the non-falling lava above it.The lower three bits are the fluid block's level. 0 is the highest fluid level (not necessarily filling the block - this depends on the neighboring fluid blocks above each upper corner of the block). Data values increase as the fluid level of the block drops: 1 is the next highest, 2 lower, on through 7, the lowest fluid level. Along a line on a flat plane, lava drops one level per meter in the Nether and two everywhere else. So inthe EndandOverworld, only 2, 4 and 6 are used. |

Bedrock Edition:
Lava and flowing lava

| Name         | Metadata Bits                       | Default value | Allowed values                                                                                                                    | Values forMetadata Bits                                                                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|--------------|-------------------------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| liquid_depth | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | If bit 0x8 is set, this fluid is "falling" and spreads only downward. At this level, the lower bits are essentially ignored, since this block is then at its highest fluid level. This level is equal to the falling lava above, equal to 8 plus the level of the non-falling lava above it.The lower three bits are the fluid block's level. 0 is the highest fluid level (not necessarily filling the block - this depends on the neighboring fluid blocks above each upper corner of the block). Data values increase as the fluid level of the block drops: 1 is the next highest, 2 lower, on through 7, the lowest fluid level. Along a line on a flat plane, lava drops one level per meter in the Nether and two everywhere else. So inthe EndandOverworld, only 2, 4 and 6 are used. |



### Fluid states
See also: Block states

Java Edition:
Lava

| Name    | Default value | Allowed values     | Description   |
|---------|---------------|--------------------|---------------|
| falling | `false`       | `true`<br/>`false` | Always false. |

Flowing lava

| Name    | Default value | Allowed values                                              | Description                                               |
|---------|---------------|-------------------------------------------------------------|-----------------------------------------------------------|
| falling | `false`       | `false`<br/>`true`                                          | True for falling lava, false for lava with a block below. |
| level   | `1`           | `1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8` | Height of the lava, 8 when the lava is falling.           |

