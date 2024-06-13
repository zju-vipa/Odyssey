### Bedrock Edition

  

This section of the article is empty. 
You can help by adding to it.


## Data values
### ID
Java Edition:

| Name       | Identifier   | Form         | Translation key              |
|------------|--------------|--------------|------------------------------|
| Sugar Cane | `sugar_cane` | Block & Item | `block.minecraft.sugar_cane` |

Bedrock Edition:

| Sugar Cane | Identifier   | Alias ID | Numeric ID | Form                         | Item ID[i 1] | Translation key   |
|------------|--------------|----------|------------|------------------------------|--------------|-------------------|
| Block      | `reeds`      | None     | `83`       | Block & Ungiveable Item[i 2] | `item.reeds` | `tile.reeds.name` |
| Item       | `sugar_cane` | `reeds`  | `385`      | Item                         | —            | `item.reeds.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Unavailable with /give command

### Block states
See also: Block states

Java Edition:

| Name | Default value | Allowed values                                                                                                                    | Description                                                                                                                                                                                              |
|------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| age  | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | A freshly planted cane – and a cane that has just grown cane above it – each have an age of 0.<br/>The age is incremented at random intervals.<br/>At age 15, a cane may try to grow more cane above it. |

Bedrock Edition:

| Name | Metadata Bits                       | Default value | Allowed values                                                                                                                    | Values forMetadata Bits                                                                                                           | Description                                                                                                                                                                                              |
|------|-------------------------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| age  | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | A freshly planted cane – and a cane that has just grown cane above it – each have an age of 0.<br/>The age is incremented at random intervals.<br/>At age 15, a cane may try to grow more cane above it. |




