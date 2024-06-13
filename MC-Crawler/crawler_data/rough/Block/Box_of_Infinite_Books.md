# Box of Infinite Books
The box of infinite books is a joke block introduced in Java Edition 20w14∞ that provides a written book containing random text when used. It uses the texture of oak planks on all but one face, on which it has its own bookshelf-like texture randomized based on its location.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
- 2 Usage
- 3 Sounds
- 4 Data values
	- 4.1 ID
- 5 History
- 6 Issues
- 7 Gallery
	- 7.1 Screenshots

## Obtaining
Boxes of infinite books can't be crafted. They naturally generate in the "library" and "isolation" dimensions. They are also available in the creative inventory.

### Breaking
Boxes of infinite books can be mined by hand, but are broken faster with an axe. In either case, they drop themselves. Unlike bookshelves, they do not require Silk Touch to obtain.

| Block     | Box of infinite books |
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

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
Boxes of infinite books naturally generate in the "library" dimension where they make up the bulk of the dimension’s terrain, and in the "isolation" dimension where 10 boxes can be found in the basement of the house.

## Usage
When used, if the block is not on one of its chunk's edges and facing along that edge, a random written book is generated. This book can be thrown into a nether portal to create a funky portal.

The random books are tied to the block such that using the same block multiple times always returns an identical book. The title of the random books given by the block is correlated with the location of the block. The title's pattern takes the format <chunk X>/<chunk Z>/<block orientation>/<distance to the chunk's edge to the right of the block>/<block Y>, so books from the same block always has the same title and content.

The author of every book is "Universe itself", obfuscated, and every book has 16 pages filled with random text. No books ever drop if game rule doTileDrops is set to false.

## Data values
### ID
| Name                  | Identifier | Form         | Translation key            |
|-----------------------|------------|--------------|----------------------------|
| Box of Infinite Books | `book_box` | Block & Item | `block.minecraft.book_box` |

