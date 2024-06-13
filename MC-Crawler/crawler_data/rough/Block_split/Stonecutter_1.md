### Changing profession
If a village has a stonecutter that has not been claimed by a villager, any nearby villager who has not yet chosen a job site block has a chance to change their profession to a stone mason.

### Note blocks
Stonecutters can be placed under note blocks to produce "bass drum" sounds.

## Data values
### ID
Java Edition:

| Name        | Identifier    | Form         | Translation key               |
|-------------|---------------|--------------|-------------------------------|
| Stonecutter | `stonecutter` | Block & Item | `block.minecraft.stonecutter` |

Bedrock Edition:

| Name        | Identifier          | Numeric ID | Form                       | Item ID[i 1]   | Translation key               |
|-------------|---------------------|------------|----------------------------|----------------|-------------------------------|
| Stonecutter | `stonecutter_block` | `452`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.stonecutter_block.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
Java Edition:

| Name   | Default value | Allowed values                            | Description                                                                                                               |
|--------|---------------|-------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the stonecutter is facing.<br/>The opposite from the direction the player faces when placing a stonecutter. |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values                            | Values forMetadata Bits | Description                                                                                                               |
|------------------------------|---------------|---------------|-------------------------------------------|-------------------------|---------------------------------------------------------------------------------------------------------------------------|
| minecraft:cardinal_direction | Not Supported | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | `Unsupported`           | The direction the stonecutter is facing.<br/>The opposite from the direction the player faces when placing a stonecutter. |




