# Chiseled Bookshelf
Chiseled bookshelves are blocks that can hold books, books and quills, written books, enchanted books and knowledge books.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Crafting
- 2 Usage
	- 2.1 Holding books
	- 2.2 Redstone signal
	- 2.3 Hoppers, minecarts with hopper, and droppers
	- 2.4 Fuel
	- 2.5 Note blocks
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
	- 4.3 Block data
- 5 Advancements
- 6 History
- 7 Issues
- 8 Trivia
- 9 Gallery
	- 9.1 Renders
	- 9.2 Screenshots
	- 9.3 In other media
- 10 References
- 11 External links

## Obtaining
### Breaking
Chiseled bookshelves can be destroyed with any tool, but an axe mines it the fastest. When broken, all contained books are dropped as items. The block itself drops only when broken using a tool enchanted with Silk Touch.[1]

| Block     | Chiseled Bookshelf    |
|-----------|-----------------------|
| Hardness  | 1.5                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 2.25                  |
| Wooden    | 1.15                  |
| Stone     | 0.6                   |
| Iron      | 0.4                   |
| Diamond   | 0.3                   |
| Netherite | 0.25                  |
| Golden    | 0.2                   |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


### Crafting
| Ingredients              | Crafting recipe |
|--------------------------|-----------------|
| AnyPlanks+AnyWooden Slab |                 |

## Usage
### Holding books
All of the chiseled bookshelf textures before 22w46a.
Chiseled bookshelves can hold up to six books, books and quills, written books, enchanted books, and/or knowledge books. There is no GUI; books are instead added into the bookshelf by using on a slot with a book. Doing so places a book in that slot. Using on an occupied slot removes the book from that slot.

Chiseled bookshelves do not increase the power of enchanting tables.

### Redstone signal
The correspondences between slot and signal power.
A redstone comparator sends a signal (1–6) indicating the last slot interacted with. When no slot has been interacted with yet, it outputs 0.

An observer can detect when a book is added or removed from the bookshelf.

### 
Hoppers and minecart with hoppers can insert and remove books from the bookshelf. As with any other container, items are taken from the first slot that has an item that can fit in the hopper and are inserted into the first empty slot. Droppers behave similarly when inserting books into the bookshelf.

When a hopper that is not already 100% full fails to remove a book from a non-empty bookshelf because there is no room for the book in the hopper's inventory, that is still counted as an "interaction" with the slot. Thus, a hopper that cannot remove any of the books effectively sets the last-interacted slot to the last non-empty slot in the bookshelf.[2]

### Fuel
Chiseled bookshelves can be used as fuel in furnaces to smelt 1.5 items.

### Note blocks
Chiseled bookshelves can be placed under note blocks to produce a "bass" sound.

## Data values
### ID
Java Edition:

| Name               | Identifier         | Form         | Translation key                    |
|--------------------|--------------------|--------------|------------------------------------|
| Chiseled Bookshelf | chiseled_bookshelf | Block & Item | block.minecraft.chiseled_bookshelf |

| Name         | Identifier         |
|--------------|--------------------|
| Block entity | chiseled_bookshelf |

Bedrock Edition:

| Name               | Identifier         | Numeric ID | Form                       | Item ID[i 1]   | Translation key              |
|--------------------|--------------------|------------|----------------------------|----------------|------------------------------|
| Chiseled Bookshelf | chiseled_bookshelf | -526       | Block & Giveable Item[i 2] | Identical[i 3] | tile.chiseled_bookshelf.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


| Name         | Savegame ID       |
|--------------|-------------------|
| Block entity | ChiseledBookshelf |

### Block states
See also: Block states

Java Edition:

| Name            | Default value | Allowed values     | Description                                                                                         |
|-----------------|---------------|--------------------|-----------------------------------------------------------------------------------------------------|
| facing          | north         | eastnorthsouthwest | The direction the bookshelf is facing.Opposite from the direction the player faces when placing it. |
| slot_0_occupied | false         | truefalse          | Whether there is a book in the upper-left slot.                                                     |
| slot_1_occupied | false         | truefalse          | Whether there is a book in the upper-middle slot.                                                   |
| slot_2_occupied | false         | truefalse          | Whether there is a book in the upper-right slot.                                                    |
| slot_3_occupied | false         | truefalse          | Whether there is a book in the lower-left slot.                                                     |
| slot_4_occupied | false         | truefalse          | Whether there is a book in the lower-middle slot.                                                   |
| slot_5_occupied | false         | truefalse          | Whether there is a book in the lower-right slot.                                                    |

Bedrock Edition:

| Name         | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                                                                                                                                      |
|--------------|---------------|---------------|----------------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| books_stored | Not Supported | 0             | 0 — 63         | Unsupported             | The confguration of the books in the bookshelf.                                                                                                                  |
| direction    | Not Supported | 0             | 0123           | Unsupported             | The direction the bookshelf is facing.Opposite from the direction the player faces when placing it.0: facing South 1: facing West 2: facing North 3: facing East |

### Block data
A chiseled bookshelf has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format


 Block entity data
Tags common to all block entities
 Items: List of books in the bookshelf.
: An item, including the slot tag. The valid slot numbers are 0-5.
Tags common to all items
 last_interacted_slot: Last interacted slot (0–5), or -1 if no slot has been interacted with yet.

Bedrock Edition:

See Bedrock Edition level format/Block entity format.

