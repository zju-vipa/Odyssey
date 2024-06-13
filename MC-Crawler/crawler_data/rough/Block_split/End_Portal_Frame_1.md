## Usage
Using eyes of ender on end portal frames inserts them to the top of the frame if it is not inserted previously.

An end portal frame has a front face that faces the player when placed. Although the facing is almost invisible (one can distinguish only 2 rotations of end portal frames), all end portal frames must be placed correctly and face inward in order to be able to activate the end portal, and if all of the frames have eyes of ender inserted, the portal activates, replacing the inner 3×3 space with end portal blocks.

If an end portal is built in the End, entities are teleported back to the world spawn point in the Overworld, similar to the exit portal.

### Redstone
End portal frames output a redstone comparator signal of 15 when an eye is present. If there is no eye in the frame, it outputs a signal of 0.

### Light source
End portals frames emit a light level of 1.

### Note blocks
End portals frames can be placed under note blocks to produce "bass drum" sound.

### Piston interactivity
End portal frames cannot be pushed by pistons. They also cannot be pushed nor pulled by sticky pistons.

## Data values
### ID
Java Edition:

| Name             | Identifier         | Form         | Block tags                          | Translation key                    |
|------------------|--------------------|--------------|-------------------------------------|------------------------------------|
| End Portal Frame | `end_portal_frame` | Block & Item | `dragon_immune`<br/>`wither_immune` | `block.minecraft.end_portal_frame` |

Bedrock Edition:

| Name             | Identifier         | Numeric ID | Form                       | Item ID[i 1]   | Translation key              |
|------------------|--------------------|------------|----------------------------|----------------|------------------------------|
| End Portal Frame | `end_portal_frame` | `120`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.end_portal_frame.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:

| Name   | Default value | Allowed values                            | Description                                                                                                                                                                                                                                                        |
|--------|---------------|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| eye    | `false`       | `false`<br/>`true`                        | If true, the portal frame block contains aneye of ender.                                                                                                                                                                                                           |
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction of the end portal frame block.<br/>The opposite from the direction the player faces while placing the block.<br/>In order to activate a portal, all 12 blocks must be facing inward;<br/>for example, the northern three blocks must all face south. |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values                            | Values forMetadata Bits | Description                                                                                                                                                                                                                                                        |
|------------------------------|---------------|---------------|-------------------------------------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| end_portal_eye_bit           | `0x4`         | `false`       | `false`<br/>`true`                        | `0`<br/>`1`             | If the portal frame block contains aneye of ender.                                                                                                                                                                                                                 |
| minecraft:cardinal_direction | Not Supported | `south`       | `east`<br/>`north`<br/>`south`<br/>`west` | `Unsupported`           | The direction of the end portal frame block.<br/>The opposite from the direction the player faces while placing the block.<br/>In order to activate a portal, all 12 blocks must be facing inward;<br/>for example, the northern three blocks must all face south. |




