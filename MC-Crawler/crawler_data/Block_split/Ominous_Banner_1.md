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

| Name   | Default value | Allowed values     | Description                                                                                                                                                               |
|--------|---------------|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing | north         | eastnorthsouthwest | The direction the block is facing. For example, a block facing east is attached to a block to its west.Opposite from the direction a player faces when placing the block. |

Bedrock Edition:

Standing
| Name                  | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                          |
|-----------------------|---------------|---------------|----------------|-------------------------|--------------------------------------|
| ground_sign_direction | 0x10x20x40x8  | 0             | 0              | 0                       | The block is facing south.           |
|                       |               |               | 1              | 1                       | The block is facing south-southwest. |
|                       |               |               | 2              | 2                       | The block is facing southwest.       |
|                       |               |               | 3              | 3                       | The block is facing west-southwest.  |
|                       |               |               | 4              | 4                       | The block is facing west.            |
|                       |               |               | 5              | 5                       | The block is facing west-northwest.  |
|                       |               |               | 6              | 6                       | The block is facing northwest.       |
|                       |               |               | 7              | 7                       | The block is facing north-northwest. |
|                       |               |               | 8              | 8                       | The block is facing north.           |
|                       |               |               | 9              | 9                       | The block is facing north-northeast. |
|                       |               |               | 10             | 10                      | The block is facing northeast.       |
|                       |               |               | 11             | 11                      | The block is facing east-northeast.  |
|                       |               |               | 12             | 12                      | The block is facing east.            |
|                       |               |               | 13             | 13                      | The block is facing east-southeast.  |
|                       |               |               | 14             | 14                      | The block is facing southeast.       |
|                       |               |               | 15             | 15                      | The block is facing south-southeast. |

Wall
| Name             | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                                                                                                              |
|------------------|---------------|---------------|----------------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| facing_direction | 0x10x20x4     | 0             | 2345           | 2345                    | The direction the block is facing. For example, a block facing east is attached to a block to its west.2: north 3: south 4: west 5: east |
|                  |               |               | 01             | 01                      | Unused                                                                                                                                   |

### Block data
An ominous banner has a block entity associated with it that holds additional data about the block. 

Bedrock Edition:

See Bedrock Edition level format/Block entity format.
Java Edition:

See also: Block entity format


 Block entity data
Tags common to all block entities
 CustomName: Optional. The name of this banner in JSON text component, which is used for showing the banner on a map.
 Patterns: List of all patterns applied to the banner.
: An individual pattern.
 Color: Color of the section.
 Pattern: The banner pattern code the color is applied to.


Pattern color
Main article: Banner/DV[edit]


Pattern
Main article: Banner/Patterns[edit]

### Item data
Java Edition:

Main article: Item format
Ominous banners, as items, use an NBT tag BlockEntityTag to indicate the patterns and details when it is placed.


 Item: The item
 tag: Additional information about the item. This tag is optional for most items.
 BlockEntityTag: The details of the onimous banner.
All block data, except tags common to all block entities.

Bedrock Edition:

See Bedrock Edition level format/Item format.

