## Data values
### ID
Java Edition:

| Name      | Identifier  | Form         | Translation key             |
|-----------|-------------|--------------|-----------------------------|
| Dispenser | `dispenser` | Block & Item | `block.minecraft.dispenser` |

| Name         | Identifier  |
|--------------|-------------|
| Block entity | `dispenser` |

Bedrock Edition:

| Name      | Identifier  | Numeric ID | Form                       | Item ID[i 1]   | Translation key       |
|-----------|-------------|------------|----------------------------|----------------|-----------------------|
| Dispenser | `dispenser` | `23`       | Block & Giveable Item[i 2] | Identical[i 3] | `tile.dispenser.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

| Name         | Savegame ID |
|--------------|-------------|
| Block entity | `Dispenser` |

### Block states
See also: Block states

Java Edition:

| Name      | Default value | Allowed values                                                | Description                                                                                                                        |
|-----------|---------------|---------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| facing    | `north`       | `down`<br/>`east`<br/>`north`<br/>`south`<br/>`up`<br/>`west` | The direction in which contents are shot or dropped.<br/>The opposite from the direction the player faces while placing the block. |
| triggered | `false`       | `false`<br/>`true`                                            | True if this block is activated.                                                                                                   |

Bedrock Edition:

| Name             | Metadata Bits             | Default value | Allowed values                                              | Values forMetadata Bits                                     | Description                                                                                                                                                            |
|------------------|---------------------------|---------------|-------------------------------------------------------------|-------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing_direction | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7` | The direction in which contents are shot or dropped.0: facing down<br/>1: facing up<br/>2: facing north<br/>3: facing south<br/>4: facing west<br/>5: facing east<br/> |
| triggered_bit    | `0x8`                     | `false`       | `false`<br/>`true`                                          | `0`<br/>`1`                                                 | True if this block is activated.                                                                                                                                       |



### Block data
A dispenser has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format

- Block entity data
	- 
	- Tags common to all block entities
	- 
	- Tags common to all objects that can be renamed
	- Items: List of items in this container.
		- : An item, including the slot tag. Dispenser slots are numbered 0-8 with 0 in the top left corner.
			- 
			- Tags common to all items
	- 
	- Tags common to all containers that can be locked
	- 
	- Tags common to all objects that use loot tables to produce items

Bedrock Edition:

SeeBedrock Edition level format/Block entity format.

