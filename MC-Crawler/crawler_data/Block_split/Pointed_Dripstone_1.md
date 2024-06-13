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




