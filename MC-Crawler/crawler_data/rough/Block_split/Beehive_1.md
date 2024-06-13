### Redstone component
Beehives and bee nests have comparator output with a strength equal to the honey level in the block. Once the beehive or bee nest is filled with honey it emits a signal strength of five.

### Note blocks
Beehives and bee nests can be placed under note blocks to produce "bass" sound.

### Fuel
In Bedrock Edition, beehives and bee nests can be used as fuel in a furnace, smelting 1.5 items per block.



## Data values
### ID
Java Edition:

| Name    | Identifier | Form         | Block tags | Translation key           |
|---------|------------|--------------|------------|---------------------------|
| Beehive | `beehive`  | Block & Item | `beehives` | `block.minecraft.beehive` |

| Name         | Identifier |
|--------------|------------|
| Block entity | `beehive`  |

Bedrock Edition:

| Name    | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key     |
|---------|------------|------------|----------------------------|----------------|---------------------|
| Beehive | `beehive`  | `474`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.beehive.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

| Name         | Savegame ID |
|--------------|-------------|
| Block entity | `Beehive`   |

### Block states
Java Edition:

| Name        | Default value | Allowed values                              | Description                                                                                                                                                     |
|-------------|---------------|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing      | `north`       | `east`<br/>`north`<br/>`south`<br/>`west`   | The opposite from the direction the player faces while placing the block.                                                                                       |
| honey_level | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | Every pollinated bee that leaves the hive after working increases the honey level by one. When at level 5, honey can be bottled or honeycombs can be harvested. |

Bedrock Edition:

| Name        | Metadata Bits | Default value | Allowed values                              | Values forMetadata Bits | Description                                                                                                                                                     |
|-------------|---------------|---------------|---------------------------------------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| direction   | Not Supported | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`                 | `Unsupported`           | The direction the block faces.0: south<br/>1: west<br/>2: north<br/>3: east<br/>                                                                                |
| honey_level | Not Supported | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | `Unsupported`           | Every pollinated bee that leaves the hive after working increases the honey level by one. When at level 5, honey can be bottled or honeycombs can be harvested. |



### Block data
A beehive has a block entity associated with it that holds additional data about the block.
Java Edition:

See also: Block entity format

- Block entity data
	- 
	- Tags common to all block entities
	- Bees: Entities currently in the hive.
		- An entity in the hive.
			- EntityData: The NBT data of the entity in the hive.
				- Seeentity format.
			- MinOccupationTicks: The minimum amount of time in ticks for this entity to stay in the hive.
			- TicksInHive: The amount of ticks the entity has stayed in the hive.
	- FlowerPos: Stores the location of a flower, so other bees can go to it.
		- X: X coordinate of the flower.
		- Y: Y coordinate of the flower.
		- Z: Z coordinate of the flower.

Bedrock Edition:

SeeBedrock Edition level format/Block entity format.

