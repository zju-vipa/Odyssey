## Data values
### ID
| Name             | Identifier        | Numeric ID | Form                       | Item ID[i 1]   | Translation key             |
|------------------|-------------------|------------|----------------------------|----------------|-----------------------------|
| Material Reducer | `chemistry_table` | `238`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.materialreducer.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

| Name                 | Metadata Bits   | Default value      | Allowed values              | Values forMetadata Bits     | Description                                                                           |
|----------------------|-----------------|--------------------|-----------------------------|-----------------------------|---------------------------------------------------------------------------------------|
| chemistry_table_type | `0x1`<br/>`0x2` | `compound_creator` | `compound_creator`          | `0`                         | Compound Creator                                                                      |
|                      |                 |                    | `element_constructor`       | `2`                         | Element Constructor                                                                   |
|                      |                 |                    | `lab_table`                 | `3`                         | Lab Table                                                                             |
|                      |                 |                    | `material_reducer`          | `1`                         | Material Reducer                                                                      |
| direction            | `0x4`<br/>`0x8` | `0`                | `0`<br/>`1`<br/>`2`<br/>`3` | `0`<br/>`1`<br/>`2`<br/>`3` | The direction the block's front is.0: north<br/>1: east<br/>2: south<br/>3: west<br/> |




