### Block states
See also: Block states

Java Edition:

| Name  | Default value | Allowed values         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-------|---------------|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| level | 0             | 0123456789101112131415 | If bit 0x8 is set, this fluid is "falling" and spreads only downward. At this level, the lower bits are essentially ignored, since this block is then at its highest fluid level. This level is equal to the falling lava above, equal to 8 plus the level of the non-falling lava above it.The lower three bits are the fluid block's level. 0 is the highest fluid level (not necessarily filling the block - this depends on the neighboring fluid blocks above each upper corner of the block). Data values increase as the fluid level of the block drops: 1 is the next highest, 2 lower, on through 7, the lowest fluid level. Along a line on a flat plane, lava drops one level per meter in the Nether and two everywhere else. So inthe EndandOverworld, only 2, 4 and 6 are used. |

Bedrock Edition:
Lava and flowing lava

| Name         | Metadata Bits | Default value | Allowed values         | Values forMetadata Bits | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|--------------|---------------|---------------|------------------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| liquid_depth | 0x10x20x40x8  | 0             | 0123456789101112131415 | 0123456789101112131415  | If bit 0x8 is set, this fluid is "falling" and spreads only downward. At this level, the lower bits are essentially ignored, since this block is then at its highest fluid level. This level is equal to the falling lava above, equal to 8 plus the level of the non-falling lava above it.The lower three bits are the fluid block's level. 0 is the highest fluid level (not necessarily filling the block - this depends on the neighboring fluid blocks above each upper corner of the block). Data values increase as the fluid level of the block drops: 1 is the next highest, 2 lower, on through 7, the lowest fluid level. Along a line on a flat plane, lava drops one level per meter in the Nether and two everywhere else. So inthe EndandOverworld, only 2, 4 and 6 are used. |



### Fluid states
See also: Block states

Java Edition:
Lava

| Name    | Default value | Allowed values | Description   |
|---------|---------------|----------------|---------------|
| falling | false         | truefalse      | Always false. |

Flowing lava

| Name    | Default value | Allowed values | Description                                               |
|---------|---------------|----------------|-----------------------------------------------------------|
| falling | false         | falsetrue      | True for falling lava, false for lava with a block below. |
| level   | 1             | 12345678       | Height of the lava, 8 when the lava is falling.           |


