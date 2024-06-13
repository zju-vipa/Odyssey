### Changing profession
If a village has a grindstone that has not been claimed by a villager, any villager who did not already pick a job site block has a chance to change their profession into weaponsmith.

### Piston interactivity
Grindstones cannot be pushed by pistons or pulled by sticky pistons.

## Data values
### ID
Java Edition:

| Name       | Identifier   | Form         | Translation key              |
|------------|--------------|--------------|------------------------------|
| Grindstone | `grindstone` | Block & Item | `block.minecraft.grindstone` |

Bedrock Edition:

| Name       | Identifier   | Numeric ID | Form                       | Item ID[i 1]   | Translation key        |
|------------|--------------|------------|----------------------------|----------------|------------------------|
| Grindstone | `grindstone` | `450`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.grindstone.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:

| Name   | Default value | Allowed values                            | Description                                                                                                                                 |
|--------|---------------|-------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| face   | `wall`        | `ceiling`<br/>`floor`<br/>`wall`          | What the grindstone is attached to.                                                                                                         |
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the grindstone is facing.<br/>Opposite from the direction the player faces when placing a grindstone on the floor or ceiling. |

Bedrock Edition:

| Name       | Metadata Bits   | Default value | Allowed values                                     | Values forMetadata Bits     | Description                                                                                                                                                                              |
|------------|-----------------|---------------|----------------------------------------------------|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| attachment | `0x4`<br/>`0x8` | `standing`    | `standing`<br/>`hanging`<br/>`side`<br/>`multiple` | `0`<br/>`1`<br/>`2`<br/>`3` | What the grindstone is attached to.                                                                                                                                                      |
| direction  | `0x1`<br/>`0x2` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`                        | `0`<br/>`1`<br/>`2`<br/>`3` | The direction the grindstone is facing. Opposite from the direction a player faces when placing the block.0: South facing<br/>1: West facing<br/>2: North facing<br/>3: East facing<br/> |




