# Lectern
A lectern is a block from which written books can be displayed and read. It also serves as a librarian's job site block.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
- 2 Usage
	- 2.1 Holding books
	- 2.2 Changing profession
	- 2.3 Redstone signal
	- 2.4 Fuel
	- 2.5 Note blocks
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
	- 4.3 Block data
- 5 History
- 6 Issues
- 7 Gallery
	- 7.1 Renders
	- 7.2 Screenshots
- 8 References
- 9 External links

## Obtaining
### Breaking
Lecterns can be broken with any tool, but an axe is the fastest. Lecterns drop themselves and the book they are holding.

| Block     | Lectern               |
|-----------|-----------------------|
| Hardness  | 2.5                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 3.75                  |
| Wooden    | 1.9                   |
| Stone     | 0.95                  |
| Iron      | 0.65                  |
| Diamond   | 0.5                   |
| Netherite | 0.45                  |
| Golden    | 0.35                  |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
Empty lecterns can generate naturally in village libraries, up to two for some library variants.

One lectern generates as part of each ancient city, in the secret room at the city center.

### Crafting
| Ingredients                   | Crafting recipe |
|-------------------------------|-----------------|
| AnyWooden Slab+<br/>Bookshelf |                 |

## Usage
Lecterns are the job site block of librarian villagers.

Librarian villagers do not place books into lecterns. They only stare at the lectern from less than a block away as "working".

### Holding books
The UI when reading a book on a lectern.
Lecterns can also hold a single book and quill or written book that other players can read at the same time. Right-clicking an empty one with a book and quill or written book places it. Right-clicking a lectern with a book already occupied opens an interface to read the book. Books occupying a lectern can be retrieved through the interface,‌[Java Edition  only] punching the lectern‌[Bedrock Edition  only] or by destroying the lectern, even when game rule doTileDrops is false.

Lecterns cannot hold enchanted books or normal books. Instead, right clicking the lectern with an enchanted book or a normal book does nothing and the book won't be placed.

### Changing profession
If a village has a lectern that has not been claimed by a villager, any villager has a chance to change their profession into librarian if that villager has not already chosen a job site block.

### Redstone signal
Lecterns holding a book emit a full-strength redstone pulse that is one game tick long (0.5 redstone ticks) when a page is turned. A redstone comparator also records book reading and sends a signal, depending on what page the player is currently on. Because Bedrock Edition displays two pages of the book at once, the same signal strength increments require double the number of pages.

In Java Edition, a book with only 1 page gives maximum signal strength, however page 1 always gives 1 signal strength if the book contains at least 2 pages.

Due to this, to calculate the signal strength S of books with more than 1 page, use the following formula: 

S=⌊1+14(P−1)M−1⌋

Where ⌊⌋ is the "floor" operation (round down), M is the maximum number of pages the book on the lectern has, and P is the current page number the lectern is turned to.

This is most noticeable when a book has 2 pages where the signal strength is either 1 on page 1 or 15 on page 2.

A book that would step up or down in increments of 1 per page would be 15 pages long.

In Bedrock Edition, the formula is slightly different. Due to Bedrock Edition showing 2 pages at once and counting a change to the book's output only if the highest even numbered page contains information, a redstone comparator treats books with 3 pages the same as those with 1 or 2 pages of information, the same as how Java Edition would treat a book with just 1 page.

For 4 or more pages of information use the following formula to calculate signal strength.

S=⌊1+14(P′−1)M′−1⌋

In this case M′ is half of the maximum page number rounded down, and P′ is half of the current highest page number containing data displayed on the book interface, rounded down.

Rounding down is required to eliminate the discrepancy caused by books containing an odd number of pages. For example, a book with 8 pages gives a signal strength of 15 when looking at pages 7-8. A book with 9 pages has a signal strength of 15 when looking at either pages 7-8 and 9-10.

In Bedrock Edition, a book that steps up or down in increments of 1 per page turned must be exactly 30 pages long, with information left on page 30.

### Fuel
Lecterns can be used as fuel in furnaces to smelt 1.5 items.

### Note blocks
Lecterns can be placed under note blocks to produce "bass" sound.

## Data values
### ID
Java Edition:

| Name    | Identifier | Form         | Translation key           |
|---------|------------|--------------|---------------------------|
| Lectern | `lectern`  | Block & Item | `block.minecraft.lectern` |

| Name         | Identifier |
|--------------|------------|
| Block entity | `lectern`  |

Bedrock Edition:

| Name    | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key     |
|---------|------------|------------|----------------------------|----------------|---------------------|
| Lectern | `lectern`  | `449`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.lectern.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

| Name         | Savegame ID |
|--------------|-------------|
| Block entity | `Lectern`   |

### Block states
See also: Block states

Java Edition:

| Name     | Default value | Allowed values                            | Description                                                                                                          |
|----------|---------------|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| facing   | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the lectern is facing.<br/>The opposite from the direction the player faces while placing the lectern. |
| has_book | `false`       | `false`<br/>`true`                        | If the lectern currently has a book.                                                                                 |
| powered  | `false`       | `false`<br/>`true`                        | If the lectern is currently outputting a redstone signal.                                                            |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values                            | Values forMetadata Bits | Description                                                                                                          |
|------------------------------|---------------|---------------|-------------------------------------------|-------------------------|----------------------------------------------------------------------------------------------------------------------|
| minecraft:cardinal_direction | Not Supported | `south`       | `east`<br/>`north`<br/>`south`<br/>`west` | `Unsupported`           | The direction the lectern is facing.<br/>The opposite from the direction the player faces while placing the lectern. |
| powered_bit                  | `0x4`         | `false`       | `false`<br/>`true`                        | `0`<br/>`1`             | If the lectern is currently outputting a redstone signal.                                                            |



### Block data
A lectern has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format

- Block entity data
	- 
	- Tags common to all block entities
	- Book: The book item, without the slot tag, currently on the lectern, may not exist.
		- 
		- Tags common to all items
	- Page: The page the book is currently on, starting from 0, does not exist if there's no book. Value is clamped between 0 and the last page - 1.

Bedrock Edition:

SeeBedrock Edition level format/Block entity format.
