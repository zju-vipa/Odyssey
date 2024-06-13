# Item Frame
An item frame is an entity‌[JE  only] or block entity‌[BE  only] that displays the item or block that is inside it.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
	- 1.4 Trading
- 2 Usage
	- 2.1 Item display
	- 2.2 Rotation
	- 2.3 Crafting ingredient
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Achievements
- 5 Data values
	- 5.1 ID
	- 5.2 Block states
	- 5.3 Item data
	- 5.4 Entity data
	- 5.5 Block data
- 6 Video
- 7 History
	- 7.1 Item Frame "item"
		- 7.1.1 Appearances
		- 7.1.2 Names
- 8 Issues
- 9 Trivia
- 10 Gallery
	- 10.1 Renders
	- 10.2 Screenshots
	- 10.3 Development images
- 11 See also
- 12 References

## Obtaining
### Breaking
An empty item frame can be broken simply by punching it. If the item frame contains an item, punching it drops the item, leaving the frame on the wall.

Because item frames are entities in Java Edition, they can be broken in Adventure mode. They will also be targeted by commands using the @e selector.‌[Java Edition  only]

### Natural generation
An item frame containing a pair of elytra generates in each end ship.

An item frame naturally generating in an end ship.
### Crafting
| Ingredients        | Crafting recipe |
|--------------------|-----------------|
| Stick+<br/>Leather |                 |

### Trading
Expert-level cartographer villagers have a chance to sell an item frame for 7 emeralds.

## Usage
### Item display
Item frame with partially filled map
Item frames can be placed on the sides of cactus blocks, pressure plates, fences, trees, slabs, cobblestone walls, chests, doors, and all solid blocks. They can also be placed on the top and bottom of these blocks. To place on chests and doors, the player needs to be sneaking. As item frames are an entity, multiple item frames can occupy the same block, although on different faces. It also allows non-solid blocks to occupy the same space.‌[Java Edition  only]

Players can place items in the frame by using the item. If a map is placed in an item frame, it enlarges to show the map in the size of a full block, with the item frame's location displayed as a green pointer on the map, pointing in the direction the item frame is facing. If this is done in the Nether, the green cursor spins around similar to the white cursor (players). If an item in an item frame has been renamed using an anvil, it displays its custom name when the cursor is over the item frame. If the player places a block inside the frame, it is displayed in miniature half in, half out of the block. This can be most notably seen on stairs or slabs.

Pick block may be used on item frames by players in creative mode only, the control has no effect for players in Survival or Adventure mode. When the item frame is displaying an item, pick block picks the displayed item instead of the item frame.

Item frames can be placed on the lid of a shulker box that is positioned horizontally, but pop off when the lid is opened.‌[Java Edition  only]

### Rotation
The displayed item can then be rotated by right-clicking the frame. Items displayed in the item frame can turn 45° diagonally, with a total of 8 possibilities (90° and 4 possibilities if it is a map), and the frame outputs a redstone signal depending on the rotation phase that can be interpreted by a redstone comparator (note that this rotation value is separate from the clock or compass rotation). As long as the frame remains placed, it remembers the orientation of the last item it held, and uses it for the next item it holds.‌[Java Edition  only]



### Crafting ingredient
| Name            | Ingredients                  | Crafting recipe |
|-----------------|------------------------------|-----------------|
| Glow Item Frame | Glow Ink Sac+<br/>Item Frame |                 |

## Data values
### ID
Java Edition:

| Item       | Identifier   | Form | Translation key             |
|------------|--------------|------|-----------------------------|
| Item Frame | `item_frame` | Item | `item.minecraft.item_frame` |

| Entity     | Identifier   | Translation key               |
|------------|--------------|-------------------------------|
| Item Frame | `item_frame` | `entity.minecraft.item_frame` |

Bedrock Edition:

| Item Frame | Identifier | Numeric ID | Form                         | Item ID[i 1] | Translation key   |
|------------|------------|------------|------------------------------|--------------|-------------------|
| Item       | `frame`    | `513`      | Item                         | —            | `item.frame.name` |
| Block      | `frame`    | `199`      | Block & Ungiveable Item[i 2] | `item.frame` | —                 |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Unavailable with /give command

| Name         | Savegame ID |
|--------------|-------------|
| Block entity | `ItemFrame` |

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
- tagtag: The item'stagtag.

- 
	- EntityTag: Stores entity data that is applied to the entity when created.
		- SeeEntity Format.

### Entity data
Main article: Entity format
In Java Edition, item frames have entity data that define various properties of the entity.

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
In Bedrock Edition, an item frame has a block entity associated with it that holds additional data about the block.

See Bedrock Edition level format/Block entity format.

