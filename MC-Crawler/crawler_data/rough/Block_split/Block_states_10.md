### Jigsaw Block
Java Edition:

| Name        | Default value | Allowed values                                                                                                                                                                    | Description                               |
|-------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| orientation | `north_up`    | `down_east`<br/>`down_north`<br/>`down_south`<br/>`down_west`<br/>`east_up`<br/>`north_up`<br/>`south_up`<br/>`up_east`<br/>`up_north`<br/>`up_south`<br/>`up_west`<br/>`west_up` | The direction the jigsaw block is facing. |

Bedrock Edition:

| Name             | Metadata Bits | Default value | Allowed values                              | Values forMetadata Bits | Description                               |
|------------------|---------------|---------------|---------------------------------------------|-------------------------|-------------------------------------------|
| facing_direction | Not Supported | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | `Unsupported`           | The direction the jigsaw block is facing. |
| rotation         | Not Supported | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`                 | `Unsupported`           | The rotation around the axis.             |



### 
Java Edition:

| Name   | Default value | Allowed values                            | Description                                                                                                                                      |
|--------|---------------|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the jack o'lantern's carved face is facing.<br/>The opposite from the direction the player faces while placing the jack o'lantern. |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values                            | Values forMetadata Bits | Description                                                                                                                                      |
|------------------------------|---------------|---------------|-------------------------------------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| minecraft:cardinal_direction | Not Supported | `south`       | `east`<br/>`north`<br/>`south`<br/>`west` | `Unsupported`           | The direction the jack o'lantern's carved face is facing.<br/>The opposite from the direction the player faces while placing the jack o'lantern. |



### Jukebox
Java Edition:

| Name       | Default value | Allowed values     | Description                                 |
|------------|---------------|--------------------|---------------------------------------------|
| has_record | `false`       | `false`<br/>`true` | True when the jukebox contains amusic disc. |



### Kelp
Java Edition:
Top kelp block:

| Name | Default value | Allowed values                                                                                                                                                                                                              | Description                                                                                                                                                                                                 |
|------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| age  | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15`<br/>`16`<br/>`17`<br/>`18`<br/>`19`<br/>`20`<br/>`21`<br/>`22`<br/>`23`<br/>`24`<br/>`25` | A freshly planted kelp starts with a random age between 0 and 24.<br/>Below age 25, a kelp may try go grow more kelp above it with the same age value incremented by one.<br/>Kelp stops growing at age 25. |

Bedrock Edition:

| Name     | Metadata Bits                       | Default value | Allowed values                                                                                                                    | Values forMetadata Bits                                                                                                           | Description                                                                                |
|----------|-------------------------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| kelp_age | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | The age of the kelp. The kelp renders as a non-top piece if there's another kelp above it. |
|          |                                     |               | `16`<br/>`17`<br/>`18`<br/>`19`<br/>`20`<br/>`21`<br/>`22`<br/>`23`<br/>`24`<br/>`25`                                             | `Unsupported`                                                                                                                     | Unused                                                                                     |



### Ladder
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

### Lantern and Soul Lantern
Java Edition:

| Name        | Default value | Allowed values     | Description                                                     |
|-------------|---------------|--------------------|-----------------------------------------------------------------|
| hanging     | `false`       | `false`<br/>`true` | If the lantern is hanging from a block.                         |
| waterlogged | `false`       | `false`<br/>`true` | Whether or not there's water in the same place as this lantern. |

Bedrock Edition:

| Name    | Metadata Bits | Default value | Allowed values     | Values forMetadata Bits | Description                             |
|---------|---------------|---------------|--------------------|-------------------------|-----------------------------------------|
| hanging | `0x1`         | `false`       | `false`<br/>`true` | `0`<br/>`1`             | If the lantern is hanging from a block. |



### Lava
Java Edition:

| Name  | Default value | Allowed values                                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| level | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | If bit 0x8 is set, this fluid is "falling" and spreads only downward. At this level, the lower bits are essentially ignored, since this block is then at its highest fluid level. This level is equal to the falling lava above, equal to 8 plus the level of the non-falling lava above it.The lower three bits are the fluid block's level. 0 is the highest fluid level (not necessarily filling the block - this depends on the neighboring fluid blocks above each upper corner of the block). Data values increase as the fluid level of the block drops: 1 is the next highest, 2 lower, on through 7, the lowest fluid level. Along a line on a flat plane, lava drops one level per meter in the Nether and two everywhere else. So inthe EndandOverworld, only 2, 4 and 6 are used. |

Bedrock Edition:
Lava and flowing lava

| Name         | Metadata Bits                       | Default value | Allowed values                                                                                                                    | Values forMetadata Bits                                                                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|--------------|-------------------------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| liquid_depth | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | If bit 0x8 is set, this fluid is "falling" and spreads only downward. At this level, the lower bits are essentially ignored, since this block is then at its highest fluid level. This level is equal to the falling lava above, equal to 8 plus the level of the non-falling lava above it.The lower three bits are the fluid block's level. 0 is the highest fluid level (not necessarily filling the block - this depends on the neighboring fluid blocks above each upper corner of the block). Data values increase as the fluid level of the block drops: 1 is the next highest, 2 lower, on through 7, the lowest fluid level. Along a line on a flat plane, lava drops one level per meter in the Nether and two everywhere else. So inthe EndandOverworld, only 2, 4 and 6 are used. |



### Leaves
Java Edition:

| Name        | Default value | Allowed values                                      | Description                                                                                    |
|-------------|---------------|-----------------------------------------------------|------------------------------------------------------------------------------------------------|
| distance    | `7`           | `1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7` | How far away this block is from the nearest log or wood, intaxicab distance.                   |
| persistent  | `false`       | `false`<br/>`true`                                  | If the block persists regardless of having no wood nearby.<br/>`true`for player-placed leaves. |
| waterlogged | `false`       | `false`<br/>`true`                                  | Whether or not there's water in the same place as this leaves.                                 |

Bedrock Edition:

| Name           | Metadata Bits | Default value | Allowed values     | Values forMetadata Bits | Description                                                |
|----------------|---------------|---------------|--------------------|-------------------------|------------------------------------------------------------|
| persistent_bit | Not Supported | `false`       | `false`<br/>`true` | `Unsupported`           | If the block persists regardless of having no wood nearby. |
| update_bit     | Not Supported | `false`       | `false`<br/>`true` | `Unsupported`           | If the block checks for nearby wood and decays.            |



