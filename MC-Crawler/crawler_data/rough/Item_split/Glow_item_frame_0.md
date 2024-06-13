# Glow Item Frame
A glow item frame is an entity‌[JE only] or block entity‌[BE only] that keeps itself and the item inside it illuminated, even in the dark.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Crafting
- 2 Usage
	- 2.1 Unique properties
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
	- 4.3 Item data
	- 4.4 Entity data
	- 4.5 Block data
- 5 History
	- 5.1 Glow Item Frame "item"
		- 5.1.1 Appearances
		- 5.1.2 Names
- 6 Issues
- 7 Gallery
	- 7.1 Renders
	- 7.2 Screenshots
- 8 See also
- 9 References

## Obtaining
### Breaking
An empty glow item frame can be broken simply by punching it. If the glow item frame contains an item, punching it drops the item, leaving the frame on the wall.

Because glow item frames are entities in Java Edition, they can be broken in Adventure mode. They are also targeted by commands using the @e selector.‌[Java Edition  only]

### Crafting
| Ingredients                  | Crafting recipe |
|------------------------------|-----------------|
| Glow Ink Sac+<br/>Item Frame |                 |

## Usage
Main article: Item Frame § Usage
Glow item frames have the same properties, usage, and rotation functionalities as regular item frames. 

### Unique properties
Comparison between ordinary item frame and glow item frame in the dark.
When an item is placed inside a glow item frame, it appears to glow, even though it does not emit any light level.

## Data values
### ID
Java Edition:

| Item            | Identifier        | Form | Translation key                  |
|-----------------|-------------------|------|----------------------------------|
| Glow Item Frame | `glow_item_frame` | Item | `item.minecraft.glow_item_frame` |

| Entity          | Identifier        | Translation key                    |
|-----------------|-------------------|------------------------------------|
| Glow Item Frame | `glow_item_frame` | `entity.minecraft.glow_item_frame` |

Bedrock Edition:

| Item Frame | Identifier   | Numeric ID | Form                         | Item ID[i 1]      | Translation key        |
|------------|--------------|------------|------------------------------|-------------------|------------------------|
| Item       | `glow_frame` | `623`      | Item                         | —                 | `item.glow_frame.name` |
| Block      | `glow_frame` | `594`      | Block & Ungiveable Item[i 2] | `item.glow_frame` | —                      |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Unavailable with /give command

| Name         | Savegame ID     |
|--------------|-----------------|
| Block entity | `GlowItemFrame` |

### Block states
See also: Block states

Bedrock Edition
Item Frame:

| Name                 | Metadata Bits   | Default value | Allowed values     | Values forMetadata Bits | Description                         |
|----------------------|-----------------|---------------|--------------------|-------------------------|-------------------------------------|
| facing_direction     | `0x1`<br/>`0x2` | `0`           | `5`                | `0`                     | East facing item frame              |
|                      |                 |               | `4`                | `1`                     | West facing item frame              |
|                      |                 |               | `3`                | `2`                     | South facing item frame             |
|                      |                 |               | `2`                | `3`                     | North facing item frame             |
|                      |                 |               | `1`                | `Unsupported`           | Up facing item frame                |
|                      |                 |               | `0`                | `Unsupported`           | Down facing item frame              |
| item_frame_map_bit   | `0x4`           | `false`       | `false`<br/>`true` | `0`<br/>`1`             | If this item frame contains a map.  |
| item_frame_photo_bit | Not Supported   | `false`       | `false`<br/>`true` | `Unsupported`           | If this item frame contains aphoto. |

Glow Item Frame:

| Name                 | Metadata Bits | Default value | Allowed values     | Values forMetadata Bits | Description                         |
|----------------------|---------------|---------------|--------------------|-------------------------|-------------------------------------|
| facing_direction     | Not Supported | `0`           | `5`                | `Unsupported`           | East facing item frame              |
|                      |               |               | `4`                | `Unsupported`           | West facing item frame              |
|                      |               |               | `3`                | `Unsupported`           | South facing item frame             |
|                      |               |               | `2`                | `Unsupported`           | North facing item frame             |
|                      |               |               | `1`                | `Unsupported`           | Up facing item frame                |
|                      |               |               | `0`                | `Unsupported`           | Down facing item frame              |
| item_frame_map_bit   | Not Supported | `false`       | `false`<br/>`true` | `Unsupported`           | If this item frame contains a map.  |
| item_frame_photo_bit | Not Supported | `false`       | `false`<br/>`true` | `Unsupported`           | If this item frame contains aphoto. |



### Item data
Java Edition:

Main article: Item format
- tag: The item'stagtag.

- 
	- EntityTag: Stores entity data that is applied to the entity when created.
		- SeeEntity Format.

### Entity data
Main article: Entity format
In Java Edition, glow item frames have entity data that define various properties of the entity.

- Entity data
	- 
	- Tags common to all entities
	- 
	- Tags common to all block entities that can hang from blocks
	- Fixed:1or0(true/false) -  Iftrue: the item frame does not drop when it has no support block, it can not be moved by pistons, and it won't take damage (except from creative players). An item can not be placed in or remove from a fixed item frame. The item in a fixed item frame (if any) can not be rotated.
	- Invisible:1or0(true/false) -  Whether the item frame (background) is invisible. An item or map inside an invisible item frame is still visible.
	- Item: The item in the item frame (no slot tag). If the item frame is empty, this tag does not exist.
		- 
		- Tags common to all items
	- ItemDropChance: The chance for the item to drop when the item frame breaks. This is a 100% chance by default.
	- ItemRotation: The current angle or rotation of the item, as a multiple of 45 degrees, going clockwise.0means the item is upright,1means the item is turned 90 degrees clockwise from the upright orientation. This value can only ever be between07and, just like its redstone output when measured with acomparator.

### Block data
In Bedrock Edition, a glow item frame has a block entity associated with it that holds additional data about the block.

See Bedrock Edition level format/Block entity format.


