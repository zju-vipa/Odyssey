### Raid
See also: Tutorials/Defeating a village raid

When the bell is rung, villagers within a distance of 32 blocks run into their houses immediately.

When a raid's first wave appears, in Java Edition, at least one villager rushes to ring the bell in the center of the village (if they are close enough) to warn the other villagers of an incoming raid before going into their house. In Bedrock Edition, bells in the corresponding village ring automatically at the start of a raid, warning villagers to return to their houses.

#### Glowing effect
Additionally, in Java Edition, if a bell is rung and there is a raid mob within a 32 block spherical range, the Glowing effect is applied to all raid mobs within 48 blocks for 3 seconds, and  particles appear. It produces a resonating sound once this process is complete. The raid mobs don't have to be actively participating in a raid to receive the Glowing effect: the effect applies to illagers in woodland mansions, or witches that naturally spawns in the Overworld.

### Piglins
Piglins admire bells as golden items. However, breaking a bell does not aggravate them.[1]

### Redstone component
In Bedrock Edition, observers can detect when a bell is rung. Observers do not emit a signal when the bell stops ringing or becomes unpowered.

## Data values
### ID
Java Edition:

| Name | Identifier | Form         | Item tags      | Translation key        |
|------|------------|--------------|----------------|------------------------|
| Bell | `bell`     | Block & Item | `piglin_loved` | `block.minecraft.bell` |

| Name         | Identifier |
|--------------|------------|
| Block entity | `bell`     |

Bedrock Edition:

| Name | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key  |
|------|------------|------------|----------------------------|----------------|------------------|
| Bell | `bell`     | `461`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.bell.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

| Name         | Savegame ID |
|--------------|-------------|
| Block entity | `Bell`      |

### Block states
See also: Block states

Java Edition:

| Name       | Default value | Allowed values                                            | Description                                                                                             |
|------------|---------------|-----------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| attachment | `floor`       | `ceiling`<br/>`double_wall`<br/>`floor`<br/>`single_wall` | What the bell is attached to.                                                                           |
| facing     | `north`       | `east`<br/>`north`<br/>`south`<br/>`west`                 | The direction the bell is facing.<br/>Opposite from the direction the player faces when placing a bell. |
| powered    | `false`       | `true`<br/>`false`                                        | Whether the bell is attached to a power source, such as a redstone torch.                               |

Bedrock Edition:

| Name       | Metadata Bits   | Default value | Allowed values                                     | Values forMetadata Bits     | Description                                                                                                                                                                                            |
|------------|-----------------|---------------|----------------------------------------------------|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| attachment | `0x4`<br/>`0x8` | `standing`    | `standing`<br/>`hanging`<br/>`side`<br/>`multiple` | `0`<br/>`1`<br/>`2`<br/>`3` | What the bell is attached to.                                                                                                                                                                          |
| direction  | `0x1`<br/>`0x2` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`                        | `0`<br/>`1`<br/>`2`<br/>`3` | The direction the bell is facing. Opposite from the direction a player faces when placing the block.0: South facing bell<br/>1: West facing bell<br/>2: North facing bell<br/>3: East facing bell<br/> |
| toggle_bit | `0x10`          | `false`       | `false`<br/>`true`                                 | `0`<br/>`1`                 | Each time the bell is rung, this value toggles between true and false.                                                                                                                                 |



### Block data
A bell has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format

- Block entity data
	- 
	- Tags common to all block entities

Bedrock Edition:

SeeBedrock Edition level format/Block entity format.

