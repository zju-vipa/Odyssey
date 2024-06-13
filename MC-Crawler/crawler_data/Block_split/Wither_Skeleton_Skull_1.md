### Enchantments
Wither skeleton skulls can receive the following enchantments, but only through an anvil.

| Name               | Max level | Method |
|--------------------|-----------|--------|
| Curse of Binding   | I         | Anvil  |
| Curse of Vanishing | I         | Anvil  |

### Note blocks
Placing a wither skeleton skull above a note block causes the note block to play the wither skeleton's ambient sound when activated.

The block below the note block does not affect the mob sound it creates.

## Data values
### ID
Java Edition:

| Name                       | Identifier                 | Form         | Translation key                            |
|----------------------------|----------------------------|--------------|--------------------------------------------|
| Wither Skeleton Skull      | wither_skeleton_skull      | Block & Item | block.minecraft.wither_skeleton_skull      |
| Wither Skeleton Wall Skull | wither_skeleton_wall_skull | Block        | block.minecraft.wither_skeleton_wall_skull |

| Name         | Identifier |
|--------------|------------|
| Block entity | skull      |

Bedrock Edition:

| Wither Skeleton Skull | Identifier | Numeric ID | Form                         | Item ID[i 1] | Translation key        |
|-----------------------|------------|------------|------------------------------|--------------|------------------------|
| Block                 | skull      | 144        | Block & Ungiveable Item[i 2] | item.skull   | —                      |
| Item                  | skull      | 516        | Item                         | —            | item.skull.wither.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Unavailable with /give command


| Name         | Savegame ID |
|--------------|-------------|
| Block entity | Skull       |

### Metadata
See also: Data values

In Bedrock Edition, mob heads use the following data values:
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




