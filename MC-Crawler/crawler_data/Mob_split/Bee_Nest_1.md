### Redstone component
Beehives and bee nests have comparator output with a strength equal to the honey level in the block. Once the beehive or bee nest is filled with honey it emits a signal strength of five.

### Note blocks
Beehives and bee nests can be placed under note blocks to produce "bass" sound.

### Fuel
In Bedrock Edition, beehives and bee nests can be used as fuel in a furnace, smelting 1.5 items per block.



## Data values
### ID
Java Edition:

| Name     | Identifier | Form         | Block tags | Translation key          |
|----------|------------|--------------|------------|--------------------------|
| Bee Nest | bee_nest   | Block & Item | beehives   | block.minecraft.bee_nest |

| Name         | Identifier |
|--------------|------------|
| Block entity | beehive    |

Bedrock Edition:

| Name     | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key    |
|----------|------------|------------|----------------------------|----------------|--------------------|
| Bee Nest | bee_nest   | 473        | Block & Giveable Item[i 2] | Identical[i 3] | tile.bee_nest.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


| Name         | Savegame ID |
|--------------|-------------|
| Block entity | Beehive     |

### Block states
Java Edition:

| Name        | Default value | Allowed values     | Description                                                                                                                                                     |
|-------------|---------------|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing      | north         | eastnorthsouthwest | The opposite from the direction the player faces while placing the block.                                                                                       |
| honey_level | 0             | 012345             | Every pollinated bee that leaves the hive after working increases the honey level by one. When at level 5, honey can be bottled or honeycombs can be harvested. |

Bedrock Edition:

| Name        | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                                                                                                                                     |
|-------------|---------------|---------------|----------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| direction   | Not Supported | 0             | 0123           | Unsupported             | The direction the block faces.0: south 1: west 2: north 3: east                                                                                                 |
| honey_level | Not Supported | 0             | 012345         | Unsupported             | Every pollinated bee that leaves the hive after working increases the honey level by one. When at level 5, honey can be bottled or honeycombs can be harvested. |



### Block data
A beehive has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format


 Block entity data
Tags common to all block entities
 Bees: Entities currently in the hive.
 An entity in the hive.
 EntityData: The NBT data of the entity in the hive.
See entity format.
 MinOccupationTicks: The minimum amount of time in ticks for this entity to stay in the hive.
 TicksInHive: The amount of ticks the entity has stayed in the hive.
 FlowerPos: Stores the location of a flower, so other bees can go to it.
 X: X coordinate of the flower.
 Y: Y coordinate of the flower.
 Z: Z coordinate of the flower.

Bedrock Edition:

See Bedrock Edition level format/Block entity format.
## See also
- Beehive
- Tutorials/Honey farming


