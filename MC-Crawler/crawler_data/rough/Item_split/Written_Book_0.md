# Written Book
A written book is an item created after a book and quill is signed.

## Contents
- 1 Obtaining
	- 1.1 Signing a book and quill
	- 1.2 Copying
- 2 Usage
	- 2.1 Lecterns
	- 2.2 Chiseled bookshelf
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Item data
- 5 History
- 6 Issues
- 7 Trivia
- 8 Gallery
	- 8.1 Textures
	- 8.2 Screenshots
- 9 See also

## Obtaining
### Signing a book and quill
Written books can be obtained by signing a book and quill. After it has been signed, it cannot be edited again. The label does not say "Written Book", but whatever the player titles it. The title appears on the top line of the label, and "by <player>" (the player's username) on the bottom. In Bedrock Edition, this is customizable without commands.

### Copying
A signed written book can be be copied using a crafting table. Books have four generations: "Original", "Copy of Original", "Copy of Copy", and "Tattered". Only books of the generations "Original" and "Copy of Original" may be copied, creating the "Copy of Original" and "Copy of Copy" generations respectively. Books of the generation "Copy of Copy" may not be copied. The "Tattered" generation is unused in normal gameplay.

| SourceGeneration | Copiable? | OutcomeGeneration |
|------------------|-----------|-------------------|
| Original         | Yes       | Copy of Original  |
| Copy of Original | Yes       | Copy of Copy      |
| Copy of Copy     | No        | N/A               |
| Tattered         | No        | N/A               |

| Ingredients                      | Crafting recipe | Description                                                                                                                                                                                                                                                                                                                                 |
|----------------------------------|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Book and Quill+<br/>Written Book | 2345678         | The input written book is not consumed.<br/>The new copies are "Copy of Original" or "Copy of Copy", depending on whether the input written book is "Original" or "Copy of Original".<br/>Copies of copies cannot be copied.<br/>Copied books of the same generation ("Original", "Copy of Original", "Copy of Copy", or "Tattered") stack. |

## Usage
Written books can be opened by pressing the use control (or holding down on the touchscreen in Bedrock Edition), and display a GUI allowing the player to read it or turn the page.

The contents of a book are an extra set of data attached to the item. This means that when a book is destroyed, its contents are lost with it.

### Lecterns
One can place a written book on an empty lectern.

The lectern then emits a redstone signal depending on the displayed page in the book. On the last page, the lectern emits a signal strength of 15.

### Chiseled bookshelf
Using the chiseled bookshelf while having a written book in the main hand puts the book inside the chiseled bookshelf.

## Data values
### ID
Java Edition:

| Name         | Identifier     | Form | Item tags                             | Translation key               |
|--------------|----------------|------|---------------------------------------|-------------------------------|
| Written Book | `written_book` | Item | `bookshelf_books`<br/>`lectern_books` | `item.minecraft.written_book` |

Bedrock Edition:

| Name         | Identifier     | Numeric ID | Form | Item tags                                                 | Translation key          |
|--------------|----------------|------------|------|-----------------------------------------------------------|--------------------------|
| Written Book | `written_book` | `511`      | Item | `minecraft:bookshelf_books`<br/>`minecraft:lectern_books` | `item.written_book.name` |

### Item data
Java Edition:

Main article: Item format
- tag: The item'stagtag.

- 
	- filtered_pages: Only inRealms. The pages shown to players with the profanity filter turned on instead of some of the regular pages. This compound is automatically given a tag named after the page number and set to""when a player with the profanity filter turnedoffcloses or signs a book with that specific page containing one or more blocked words, so players with the filteroncannot see the blocked words. If a player with the filterontries to use blocked words in one or more of the pages, this compound is not given any new tags and the specific page(s) inpagesare instead set to"", which makes the page(s) render completely blank. If multiple pages have been edited before the book is closed, only the pages containing blocked words are blanked.
	- filtered_title: Only inRealms. The title shown to players with the profanity filter turned on instead of the regular title. This tag is automatically set to""when a player with the profanity filter turnedoffsigns a book with a title containing one or more blocked words, so players with the filteroncannot see the blocked words. If a player with the filterontries to use blocked words in the title, this tag is not added and thetitletag is instead set to"", which makes the title render as "Written Book", as if it weren't named.
	- resolved: Optional. Created and set to 1 when the book (or a book from the stack) is opened for the first time after being created. Used to determine whether toresolve advanced componentswithin JSON, because their values become fixed at that point.
	- generation: Optional. The copy tier of the book. 0 = original, 1 = copy of original, 2 = copy of copy, 3 = tattered. If the value is greater than 1, the book cannot be copied. Does not exist for original books. If this tag is missing, it is assumed the book is an original. 'Tattered' is unused in normal gameplay, and functions identically to the 'copy of copy' tier.
	- author: The author of the written book.
	- title: The title of the written book. Lower priority than the item name set bytag.display.Name. Cannot be used to open locked containers.
	- pages: The list of pages in the book.
		- : A single page in the book. Each page is a serializedJSON text.

Bedrock Edition:

SeeBedrock Edition level format/Item format.

