## Data values
### ID
Java Edition:

| Name                | Identifier   | Form         | Translation key              |
|---------------------|--------------|--------------|------------------------------|
| Redstone Comparator | `comparator` | Block & Item | `block.minecraft.comparator` |

| Name         | Identifier   |
|--------------|--------------|
| Block entity | `comparator` |

Bedrock Edition:

| Redstone Comparator | Identifier             | Numeric ID | Form                         | Item ID[i 1]   | Translation key        |
|---------------------|------------------------|------------|------------------------------|----------------|------------------------|
| Unpowered block     | `unpowered_comparator` | `149`      | Block & Ungiveable Item[i 2] | Identical[i 3] | —                      |
| Powered block       | `powered_comparator`   | `150`      | Block & Ungiveable Item[i 2] | Identical[i 3] | —                      |
| Item                | `comparator`           | `522`      | Item                         | —              | `item.comparator.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑ a bUnavailable with /give command
3. ↑ a bThe block's direct item form has the same id as the block.

| Name         | Savegame ID  |
|--------------|--------------|
| Block entity | `Comparator` |

### Block states
See also: Block states

Java Edition:

| Name    | Default value | Allowed values                            | Description                                                                                                                                               |
|---------|---------------|-------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing  | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction from theoutputside to theinputside of the comparator,<br/>or the opposite from the direction the player faces while placing the comparator. |
| mode    | `compare`     | `compare`<br/>`subtract`                  | Specifies the current mode of the redstone comparator.                                                                                                    |
| powered | `false`       | `false`<br/>`true`                        | True if the redstone comparator is being powered.                                                                                                         |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values                            | Values forMetadata Bits | Description                                                                                                                                               |
|------------------------------|---------------|---------------|-------------------------------------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| minecraft:cardinal_direction | Not Supported | `south`       | `east`<br/>`north`<br/>`south`<br/>`west` | `Unsupported`           | The direction from theoutputside to theinputside of the comparator,<br/>or the opposite from the direction the player faces while placing the comparator. |
| output_lit_bit               | `0x8`         | `false`       | `false`<br/>`true`                        | `0`<br/>`1`             | True if the redstone comparator is being powered.                                                                                                         |
| output_subtract_bit          | `0x4`         | `false`       | `false`<br/>`true`                        | `0`<br/>`1`             | Specifies the current mode of the redstone comparator.                                                                                                    |



### Block data
A redstone comparator has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format

- Block entity data
	- 
	- Tags common to all block entities
	- OutputSignal: Represents the strength of the analog signal output of this redstone comparator.

Bedrock Edition:

SeeBedrock Edition level format/Block entity format.

