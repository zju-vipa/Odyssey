### Fuel
A ladder can be used as fuel in furnaces, smelting 1.5 items per ladder.‌[Java Edition  only]

## Data values
### ID
Java Edition:

| Name   | Identifier | Form         | Block tags  | Translation key          |
|--------|------------|--------------|-------------|--------------------------|
| Ladder | `ladder`   | Block & Item | `climbable` | `block.minecraft.ladder` |

Bedrock Edition:

| Name   | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key    |
|--------|------------|------------|----------------------------|----------------|--------------------|
| Ladder | `ladder`   | `65`       | Block & Giveable Item[i 2] | Identical[i 3] | `tile.ladder.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:

| Name        | Default value | Allowed values                            | Description                                                            |
|-------------|---------------|-------------------------------------------|------------------------------------------------------------------------|
| facing      | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction from the block the ladder is attached to, to the ladder. |
| waterlogged | `false`       | `false`<br/>`true`                        | Whether or not there's water in the same place as this ladder.         |

Bedrock Edition:

| Name             | Metadata Bits             | Default value | Allowed values              | Values forMetadata Bits     | Description                                                                                                                                                                      |
|------------------|---------------------------|---------------|-----------------------------|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing_direction | `0x1`<br/>`0x2`<br/>`0x4` | `2`           | `2`<br/>`3`<br/>`4`<br/>`5` | `2`<br/>`3`<br/>`4`<br/>`5` | The direction from the block the ladder is attached to, to the ladder.2: Ladder facing north<br/>3: Ladder facing south<br/>4: Ladder facing west<br/>5: Ladder facing east<br/> |
|                  |                           |               | `0`<br/>`1`                 | `0`<br/>`1`                 | Unused                                                                                                                                                                           |


