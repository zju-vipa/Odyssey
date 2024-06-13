### Metadata
See also: Data values

In Bedrock Edition, zomie heads use the following data values:
For the item and for the tile entity, data values determine the skull type:

|  | DV | Description           |
|--|----|-----------------------|
|  | 0  | Skeleton Skull        |
|  | 1  | Wither Skeleton Skull |
|  | 2  | Zombie Head           |
|  | 3  | Head                  |
|  | 4  | Creeper Head          |
|  | 5  | Dragon Head           |

### Block states
See also: Block states

Java Edition:
Floor

| Name     | Default value | Allowed values | Description                          |
|----------|---------------|----------------|--------------------------------------|
| rotation | 0             | 0              | The block is facing south.           |
|          |               | 1              | The block is facing south-southwest. |
|          |               | 2              | The block is facing southwest.       |
|          |               | 3              | The block is facing west-southwest.  |
|          |               | 4              | The block is facing west.            |
|          |               | 5              | The block is facing west-northwest.  |
|          |               | 6              | The block is facing northwest.       |
|          |               | 7              | The block is facing north-northwest. |
|          |               | 8              | The block is facing north.           |
|          |               | 9              | The block is facing north-northeast. |
|          |               | 10             | The block is facing northeast.       |
|          |               | 11             | The block is facing east-northeast.  |
|          |               | 12             | The block is facing east.            |
|          |               | 13             | The block is facing east-southeast.  |
|          |               | 14             | The block is facing southeast.       |
|          |               | 15             | The block is facing south-southeast. |

Wall

| Name   | Default value | Allowed values     | Description                                                                                      |
|--------|---------------|--------------------|--------------------------------------------------------------------------------------------------|
| facing | north         | eastnorthsouthwest | The direction the head is facing.Opposite from the direction a player is facing when placing it. |

Bedrock Edition:

| Name             | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                          |
|------------------|---------------|---------------|----------------|-------------------------|------------------------------------------------------|
| facing_direction | 0x10x20x4     | 0             | 1              | 1                       | On the floor (rotation is stored in the tile entity) |
|                  |               |               | 2              | 2                       | On a wall, facing north                              |
|                  |               |               | 3              | 3                       | On a wall, facing south                              |
|                  |               |               | 4              | 4                       | On a wall, facing east                               |
|                  |               |               | 5              | 5                       | On a wall, facing west                               |
|                  |               |               | 0              | 0                       | Unused                                               |




