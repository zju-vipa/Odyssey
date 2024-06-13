### Block states
See also: Block states

Bedrock Edition
Item Frame:

| Name                 | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                         |
|----------------------|---------------|---------------|----------------|-------------------------|-------------------------------------|
| facing_direction     | 0x10x2        | 0             | 5              | 0                       | East facing item frame              |
|                      |               |               | 4              | 1                       | West facing item frame              |
|                      |               |               | 3              | 2                       | South facing item frame             |
|                      |               |               | 2              | 3                       | North facing item frame             |
|                      |               |               | 1              | Unsupported             | Up facing item frame                |
|                      |               |               | 0              | Unsupported             | Down facing item frame              |
| item_frame_map_bit   | 0x4           | false         | falsetrue      | 01                      | If this item frame contains a map.  |
| item_frame_photo_bit | Not Supported | false         | falsetrue      | Unsupported             | If this item frame contains aphoto. |

Glow Item Frame:

| Name                 | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                         |
|----------------------|---------------|---------------|----------------|-------------------------|-------------------------------------|
| facing_direction     | Not Supported | 0             | 5              | Unsupported             | East facing item frame              |
|                      |               |               | 4              | Unsupported             | West facing item frame              |
|                      |               |               | 3              | Unsupported             | South facing item frame             |
|                      |               |               | 2              | Unsupported             | North facing item frame             |
|                      |               |               | 1              | Unsupported             | Up facing item frame                |
|                      |               |               | 0              | Unsupported             | Down facing item frame              |
| item_frame_map_bit   | Not Supported | false         | falsetrue      | Unsupported             | If this item frame contains a map.  |
| item_frame_photo_bit | Not Supported | false         | falsetrue      | Unsupported             | If this item frame contains aphoto. |



### Item data
Java Edition:

Main article: Item format

 tag tag: The item's tag tag.
 EntityTag: Stores entity data that is applied to the entity when created.
See Entity Format.
Unlike spawn eggs, cannot change the type of entity created using the id tag. Data that item frames do not normally use (see below) has no effect. 


### Entity data
Main article: Entity format
In Java Edition, item frames have entity data that define various properties of the entity.


 Entity data
Tags common to all entities
Tags common to all block entities that can hang from blocks
 Fixed:  1 or 0 (true/false) -  If true: the item frame does not drop when it has no support block, it can not be moved by pistons, and it won't take damage (except from creative players). An item can not be placed in or remove from a fixed item frame. The item in a fixed item frame (if any) can not be rotated.
 Invisible: 1 or 0 (true/false) -  Whether the item frame (background) is invisible. An item or map inside an invisible item frame is still visible.
 Item: The item in the item frame (no slot tag). If the item frame is empty, this tag does not exist.
Tags common to all items
 ItemDropChance: The chance for the item to drop when the item frame breaks. This is a 100% chance by default.
 ItemRotation: The current angle or rotation of the item, as a multiple of 45 degrees, going clockwise. 0 means the item is upright, 1 means the item is turned 90 degrees clockwise from the upright orientation. This value can only ever be between 0 7 and, just like its redstone output when measured with a comparator.

### Block data
In Bedrock Edition, an item frame has a block entity associated with it that holds additional data about the block.

See Bedrock Edition level format/Block entity format.

## See also
- Painting


