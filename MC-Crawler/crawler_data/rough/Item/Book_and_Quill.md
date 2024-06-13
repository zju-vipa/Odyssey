# Book and Quill
A book and quill is an item used by players to store and edit text. After signing, it turns into a written book with all the text inside saved permanently.

## Contents
- 1 Obtaining
	- 1.1 Natural generation
	- 1.2 Crafting
- 2 Usage
	- 2.1 Crafting ingredient
	- 2.2 Writing
	- 2.3 Lecterns
	- 2.4 Formatting codes
	- 2.5 Signing
	- 2.6 Chiseled bookshelf
	- 2.7 Trading
	- 2.8 Inserting screenshots
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Item data
- 5 Video
- 6 History
- 7 Issues
- 8 Trivia
- 9 Gallery
	- 9.1 Screenshots
- 10 References
- 11 External links
- 12 See also

## Obtaining
### Natural generation
| Item           | Structure       | Container | Quantity | Chance          |
|----------------|-----------------|-----------|----------|-----------------|
|                |                 |           |          | Bedrock Edition |
| Book and Quill | Buried Treasure | Chest     | 1–2      | 18.9%           |

### Crafting
| Ingredients                    | Crafting recipe |
|--------------------------------|-----------------|
| Book+<br/>Ink Sac+<br/>Feather |                 |

## Usage
### Crafting ingredient
| Name         | Ingredients                      | Crafting recipe | Description                                                                                                                                                                                                                                                                                                                                 |
|--------------|----------------------------------|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Written Book | Book and Quill+<br/>Written Book | 2345678         | The input written book is not consumed.<br/>The new copies are "Copy of Original" or "Copy of Copy", depending on whether the input written book is "Original" or "Copy of Original".<br/>Copies of copies cannot be copied.<br/>Copied books of the same generation ("Original", "Copy of Original", "Copy of Copy", or "Tattered") stack. |

### Writing
By pressing use item or long pressing screen anywhere‌[Bedrock Edition  only] while holding a book and quill in their hand, the player can open a text editor GUI.

In Java Edition, the player can write a single book up to 100 pages, with up to 1023 characters per page, and up to 102,300 characters inside the entire book.

In Bedrock Edition, the player can write a single book up to 50 pages long, with up to 256 characters per page, and up to 12,800 characters inside the entire book.

No page may be longer than 14 lines and each line can have a width of 122 pixels.

The player has the ability to copy and paste into books. However, the paste does not work if the text being pasted is longer than a single page. Most Unicode characters are available in books, and they may be pasted in without issue.

In singleplayer, the world pauses while a book is being edited.‌[Java Edition  only]

### Lecterns
A book and quill (as well as a written book) can be placed on an empty lectern.

The lectern then emits a redstone signal depending on the displayed page in the book. On the last page, the lectern emits a signal strength of 15. This is why lecterns are listed in the "redstone" tab in the creative inventory.

### Formatting codes
Main article: Formatting codes

  

This feature is exclusive to  Bedrock Edition. 


Text in a book can be styled using codes starting with the § character (section sign).

- §+kcreates randomly changing characters.
- §+lcreates bold text.
- §+mcreates strikethrough text.
- §+ncreates underlined text.
- §+ocreates italic text.
- §+0–f(hexadecimal) creates colored text.
- §+rresets any of the previous styles so text after it appears normally.

If the player uses multiple codes, and continue typing past the end of a line, the next line exhibits only the last formatting code used.

### Signing
Books can be signed by pressing the "Sign" button while in the interface. In Java Edition, when signed, a book bears the name of the player who wrote it and a title chosen upon signing. In Bedrock Edition, the book doesn't display the name of the player as the author; instead, the author can be any text the player wants. After it has been signed, it cannot be edited again – it has turned into a written book.

Special characters can be used in the title, if typed from a keyboard that supports them. Alt codes do not work, and the § character cannot be typed even using a keyboard that implements it, meaning titles cannot be colored or formatted in-game. However, on Linux using the compose key to produce special characters does work.

The title of the book can be up to 15 characters long[1], and the player cannot paste into a title. If a custom name is removed from a written book, it reverts back to the title it was given during the signing process.

### Chiseled bookshelf
Using the chiseled bookshelf while having a book and quill in the main hand puts the book inside the chiseled bookshelf.

### Trading
In Bedrock Edition, expert-level librarian villagers buy 2 books and quills for one emerald. Book and quill is offered in two item slots due to being non-stackable.

In Java Edition, expert-level librarian villagers have a 50% chance to buy 2 books and quills for one emerald. The amount of books and quills needed is supposed to be 2, but due to the item being non-stackable, only one is needed for the trade.[2]

### Inserting screenshots

  

This feature is exclusive to  Minecraft Education. 


Screenshots in the portfolio can be inserted into book and quill.[3] This can be done by clicking the pencil button on the bottom of the page, and clicking the photo button (shown as an icon that looks like photo with a plus next to it).

The photo button brings up the portfolio menu, where players can select which screenshot to be inserted into the book and quill page. Each screenshot takes up one page.

Players can export their books and quills photos and written texts as a PDF file. The default name for the file is formatted "(Book Name) (Author Name)".

## Data values
### ID
Java Edition:

| Name           | Identifier      | Form | Item tags                             | Translation key                |
|----------------|-----------------|------|---------------------------------------|--------------------------------|
| Book and Quill | `writable_book` | Item | `bookshelf_books`<br/>`lectern_books` | `item.minecraft.writable_book` |

Bedrock Edition:

| Name           | Identifier      | Numeric ID | Form | Item tags                                                 | Translation key           |
|----------------|-----------------|------------|------|-----------------------------------------------------------|---------------------------|
| Book and Quill | `writable_book` | `510`      | Item | `minecraft:bookshelf_books`<br/>`minecraft:lectern_books` | `item.writable_book.name` |

### Item data
Java Edition:

Main article: Item format
- tag: Thetagtag.

- 
	- filtered_pages: Only inRealms. The pages shown to players with the profanity filter turned on instead of some of the regular pages. This compound is automatically given a tag named after the page number and set to""when a player with the profanity filter turnedoffcloses a book with that specific page containing one or more blocked words, so players with the filteroncannot see the blocked words. If a player with the filterontries to use blocked words in one or more of the pages, this compound is not given any new tags and the specific page(s) inpagesare instead set to"", which makes the page(s) render completely blank. If multiple pages have been edited before the book is closed, only the pages containing blocked words are blanked.
	- pages: The list of pages in the book.
		- : A single page in the book. Each page is a string and uses the escape sequence\nfor a line break. However, thecommand parserdoes not accept\n, so line breaks need to be set by aplayeror usingloot tables.[4]

Bedrock Edition:

SeeBedrock Edition level format/Item format.
