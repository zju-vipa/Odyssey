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

