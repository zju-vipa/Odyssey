# Pointed Dripstone
Pointed dripstone is a block that makes up stalactites and stalagmites. 

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Trading
	- 1.4 Post-generation
- 2 Usage
	- 2.1 Stalactites
		- 2.1.1 Cauldrons
		- 2.1.2 Converting mud into clay
	- 2.2 Stalagmites
	- 2.3 Columns
	- 2.4 Crafting ingredient
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Gallery
	- 7.1 Screenshots
	- 7.2 Concept artwork
- 8 References

## Obtaining
### Breaking
Pointed dripstone can be mined with any tool,[1] but pickaxes are the quickest. Pointed dripstone breaks instantly when hit by a thrown trident. 

| Block     | Pointed Dripstone     |
|-----------|-----------------------|
| Hardness  | 1.5                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 2.25                  |
| Wooden    | 1.15                  |
| Stone     | 0.6                   |
| Iron      | 0.4                   |
| Diamond   | 0.3                   |
| Netherite | 0.25                  |
| Golden    | 0.2                   |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


### Natural generation
Pointed dripstone can be found in dripstone caves in cluster formations.


### Trading
Wandering traders can sell 2 pointed dripstone for 1 emerald.

### Post-generation
Pointed dripstone can grow only if it is hanging directly under a dripstone block while there is a water source above. In addition, if there is a solid block less than eleven blocks below this stalactite, a stalagmite grows on that block toward the stalactite. This growth does not occur if the stalactite's tip is waterlogged, and a stalagmite below does not grow if its tip is waterlogged. They do not grow to more than seven blocks long.

Every time the block receives a random tick there is a small chance of 1.138% (64⁄5625) for a stalactite or stalagmite to grow one block, meaning that every single growth step takes an average time of 5 in-game days (100 minutes).

## Usage
Pointed dripstone comes in two different forms, stalactites and stalagmites. Placing a pointed dripstone between a stalagmite and stalactite without sneaking connects them. It can be waterlogged. Mobs can jump up pointed dripstone as long as its height does not exceed four blocks. Horses and other similar mobs can travel up the same pointed dripstone as if they were stairs.

### Stalactites
A stalactite.
Stalactites are created when pointed dripstone is placed on the bottom of a block.

Stalactites less than 11 blocks tall passively drip water particles (or lava particles in the Nether) in the absence of a liquid source, but these particles do not fill cauldrons. A waterlogged pointed dripstone at the tip of a stalactite does not produce drip particles. Waterlogging other parts of the stalactite does not affect the dripping.

If the block supporting a stalactite or any block of the stalactite is broken, all of the unsupported pointed dripstone below the broken block drops, causing damage to any player and mobs standing beneath it, similar to a falling anvil. The amount of damage is 6 for each block of falling distance after 2 blocks (e.g., a stalactite that falls 4 blocks deals 18 × 9 damage). The damage is capped at 40 × 20, no matter how far the stalactite falls. Wearing a helmet reduces the damage by 1⁄4, but this costs twice as much durability on the helmet as on other armor pieces. When a player dies by a stalactite falling on them, the death message "<player> was skewered by a falling stalactite" appears. However, if a player is merely touched by a falling stalactite entity, no damage is dealt unless the stalactite hits the ground in the same block where the player is located. Stalactites with multiple pointed dripstone can cause multiple damage; however, damage immunity prevents most of the damage from additional blocks.

#### Cauldrons
When the uppermost block of a stalactite less than 11 blocks tall gets randomly ticked, it checks for a water source or waterlogged block two blocks above it and a cauldron within 10 blocks under the tip with no non-air blocks in between. In Java Edition, open trapdoors, ladders and blocks with no collision box are also allowed.[2] If both conditions are satisfied, there is a 45⁄256 (~17.6%) chance for it to drip water and fill the cauldron by one level. If there is a lava source above the stalactite, there is a 15⁄256 (~5.9%) chance for it to completely fill an empty cauldron with lava instead, making lava a renewable resource. Refilling a cauldron with water or lava averages nearly one Minecraft day (19+ minutes) although the actual time for any individual refill varies.

#### Converting mud into clay
If mud‌ is placed above a block with a stalactite underneath, the mud eventually turns into clay. There is a 44⁄256 (~17.2%) chance of this happening when the block gets randomly ticked. This conversion does not happen in the Nether.[3]

### Stalagmites
A stalagmite.
Stalagmites are created when pointed dripstone is placed on the ground.

Falling onto stalagmites multiplies the fall distance by two to calculate the total amount of fall damage, using the formula ceil(fall_distance × 2 − 2). A player or mob gets 1 damage each time they jump on top of a single stalagmite (with a normal jump height of 1 1⁄4 blocks). The distance traveled during the last game tick of falling time is not included in this calculation, making it slightly off at higher distances; see Damage § Fall damage for more information.

If a player dies from falling onto a stalagmite, the death message "<player> was impaled on a stalagmite" appears.

All mobs that are immune to fall damage do not take damage from falling into stalagmites; the same applies to the player if the game rule fallDamage is set to false.[4][5]

### Columns
A naturally generated dripstone column.
Dripstone columns can be found naturally in dripstone caves, they are formed when stalactites and stalagmites join together in mid-air.

To create them manually, simply keep stacking pointed dripstones on either the stalactite or the stalagmite or both until they join together, the last pointed dripstone placed being the most slender part of the whole column. Based on the direction of the last block placed, the shape of the column's slender part can vary.

### Crafting ingredient
| Name            | Ingredients       | Crafting recipe |
|-----------------|-------------------|-----------------|
| Dripstone Block | Pointed Dripstone |                 |

## Data values
### ID
Java Edition:

| Name              | Identifier        | Form         | Translation key                   |
|-------------------|-------------------|--------------|-----------------------------------|
| Pointed Dripstone | pointed_dripstone | Block & Item | block.minecraft.pointed_dripstone |

Bedrock Edition:

| Name              | Identifier        | Numeric ID | Form                       | Item ID[i 1]   | Translation key             |
|-------------------|-------------------|------------|----------------------------|----------------|-----------------------------|
| Pointed Dripstone | pointed_dripstone | 563        | Block & Giveable Item[i 2] | Identical[i 3] | tile.pointed_dripstone.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block states

Java Edition:

| Name               | Default value | Allowed values | Description                                                               |
|--------------------|---------------|----------------|---------------------------------------------------------------------------|
| thickness          | tip           | tip_merge      |                                                                           |
|                    |               | tip            |                                                                           |
|                    |               | frustum        |                                                                           |
|                    |               | middle         |                                                                           |
|                    |               | base           |                                                                           |
| vertical_direction | up            | updown         | The direction of the pointed dripstone.                                   |
| waterlogged        | false         | truefalse      | Whether or not there's water in the same place as this pointed dripstone. |

Bedrock Edition:

| Name                | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                            |
|---------------------|---------------|---------------|----------------|-------------------------|--------------------------------------------------------|
| dripstone_thickness | Not Supported | tip           | merge          | Unsupported             |                                                        |
|                     |               |               | tip            | Unsupported             |                                                        |
|                     |               |               | frustum        | Unsupported             |                                                        |
|                     |               |               | middle         | Unsupported             |                                                        |
|                     |               |               | base           | Unsupported             |                                                        |
| hanging             | Not Supported | true          | falsetrue      | Unsupported             | Whether or not the pointed dripstone is pointing down. |



