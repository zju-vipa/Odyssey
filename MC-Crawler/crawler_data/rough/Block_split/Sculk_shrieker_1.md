## Data values
### ID
Java Edition:

| Name           | Identifier       | Form         | Translation key                  |
|----------------|------------------|--------------|----------------------------------|
| Sculk Shrieker | `sculk_shrieker` | Block & Item | `block.minecraft.sculk_shrieker` |

| Name         | Identifier       |
|--------------|------------------|
| Block entity | `sculk_shrieker` |

Bedrock Edition:

| Name           | Identifier       | Numeric ID | Form                       | Item ID[i 1]   | Translation key            |
|----------------|------------------|------------|----------------------------|----------------|----------------------------|
| Sculk Shrieker | `sculk_shrieker` | `716`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.sculk_shrieker.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

| Name         | Savegame ID     |
|--------------|-----------------|
| Block entity | `SculkShrieker` |

### Block states
See also: Block states

Java Edition:

| Name        | Default value | Allowed values     | Description                                                            |
|-------------|---------------|--------------------|------------------------------------------------------------------------|
| can_summon  | `false`       | `false`<br/>`true` | If true, the sculk shrieker can summon thewarden.                      |
| shrieking   | `false`       | `false`<br/>`true` | Whether the sculk shrieker is shrieking or not.                        |
| waterlogged | `false`       | `false`<br/>`true` | Whether or not there's water in the same place as this sculk shrieker. |

Bedrock Edition:

| Name       | Metadata Bits | Default value | Allowed values     | Values forMetadata Bits | Description                                       |
|------------|---------------|---------------|--------------------|-------------------------|---------------------------------------------------|
| active     | Not Supported | `0`           | `0`<br/>`1`        | `Unsupported`           | Whether the sculk shrieker is shrieking or not.   |
| can_summon | Not Supported | `false`       | `true`<br/>`false` | `Unsupported`           | If true, the sculk shrieker can summon thewarden. |



### Block data
A sculk shrieker has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format

- : The block entity's root tag.
	- VibrationListener: The vibration event listener of the sculk shrieker, sculk sensor, and calibrated sculk sensor.
		- event: Unknown.
		- pending: Unknown.
			- distance: Unknown.
			- source: Unknown.
			- vibration: Unknown.
			- x: Unknown.
			- y: Unknown.
			- z: Unknown.
		- selector: Unknown.
		- ticks: Unknown.

Bedrock Edition:

SeeBedrock Edition level format/Block entity format.

