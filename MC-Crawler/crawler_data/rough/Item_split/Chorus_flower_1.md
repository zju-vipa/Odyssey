### Bee nests
Oak, birch, and cherry trees grown from saplings that are within 2 blocks of a chorus flower have a 5% chance to grow with a bee nest and 1-3 bees in it.

## Data values
### ID
Java Edition:

| Name          | Identifier      | Form         | Translation key                 |
|---------------|-----------------|--------------|---------------------------------|
| Chorus Flower | `chorus_flower` | Block & Item | `block.minecraft.chorus_flower` |

Bedrock Edition:

| Name          | Identifier      | Numeric ID | Form                       | Item ID[i 1]   | Translation key           |
|---------------|-----------------|------------|----------------------------|----------------|---------------------------|
| Chorus Flower | `chorus_flower` | `200`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.chorus_flower.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition

| Name | Default value | Allowed values                      | Description                                                                                                                                                                   |
|------|---------------|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| age  | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4` | A freshly planted chorus flower starts at age 0. The age is incremented when a chorus flower turns horizontally and/or generates additional chorus flowers on the same plant. |
|      |               | `5`                                 | At age 5, the chorus flower does not grow further. A chorus flower can become age 5 at any time.                                                                              |

Bedrock Edition

| Name | Metadata Bits             | Default value | Allowed values                                                                    | Values forMetadata Bits             | Description                                                                                                                                                                   |
|------|---------------------------|---------------|-----------------------------------------------------------------------------------|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| age  | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`                                               | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4` | A freshly planted chorus flower starts at age 0. The age is incremented when a chorus flower turns horizontally and/or generates additional chorus flowers on the same plant. |
|      |                           |               | `5`                                                                               | `5`                                 | At age 5, the chorus flower does not grow further. A chorus flower can become age 5 at any time.                                                                              |
|      |                           |               | `6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | `Unsupported`                       | Unused                                                                                                                                                                        |




