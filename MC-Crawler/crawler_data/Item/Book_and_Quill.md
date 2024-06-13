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
| Ingredients          | Crafting recipe |
|----------------------|-----------------|
| Book+Ink Sac+Feather |                 |

## Usage
### Crafting ingredient
| Name         | Ingredients                 | Crafting recipe | Description                                                                                                                                                                                                                                                                                                                  |
|--------------|-----------------------------|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Written Book | Book and Quill+Written Book | 2345678         | The input written book is not consumed.The new copies are "Copy of Original" or "Copy of Copy", depending on whether the input written book is "Original" or "Copy of Original".Copies of copies cannot be copied.Copied books of the same generation ("Original", "Copy of Original", "Copy of Copy", or "Tattered") stack. |

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

| Name           | Identifier    | Form | Item tags                    | Translation key              |
|----------------|---------------|------|------------------------------|------------------------------|
| Book and Quill | writable_book | Item | bookshelf_bookslectern_books | item.minecraft.writable_book |

Bedrock Edition:

| Name           | Identifier    | Numeric ID | Form | Item tags                                        | Translation key         |
|----------------|---------------|------------|------|--------------------------------------------------|-------------------------|
| Book and Quill | writable_book | 510        | Item | minecraft:bookshelf_booksminecraft:lectern_books | item.writable_book.name |

### Item data
Java Edition:

Main article: Item format

 tag: The tag tag.
 filtered_pages: Only in Realms. The pages shown to players with the profanity filter turned on instead of some of the regular pages. This compound is automatically given a tag named after the page number and set to "" when a player with the profanity filter turned off closes a book with that specific page containing one or more blocked words, so players with the filter on cannot see the blocked words. If a player with the filter on tries to use blocked words in one or more of the pages, this compound is not given any new tags and the specific page(s) in  pages are instead set to "", which makes the page(s) render completely blank. If multiple pages have been edited before the book is closed, only the pages containing blocked words are blanked.
 pages: The list of pages in the book.
: A single page in the book. Each page is a string and uses the escape sequence \n for a line break. However, the command parser does not accept \n, so line breaks need to be set by a player or using loot tables.[4]

Bedrock Edition:

See Bedrock Edition level format/Item format.
## See also
- Book
- Bookshelf
- Written Book

| Tools, weapons, and armor |                                                                                                                                                                       |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Tools                     | Axe Brush Elytra Fishing Rod Carrot on a Stick Warped Fungus on a Stick Flint and Steel Hoe Pickaxe Shears ShovelBE & EE only   Glow Stick                            |
| BE&EEonly                 | Glow Stick                                                                                                                                                            |
| Weapons                   | Arrow Tipped Axe Bow Crossbow Egg Fire Charge Shield Snowball Sword TridentJava Edition only   Spectral Arrow   BE & EE only   Ice Bomb   Upcoming   Mace Wind Charge |
| Java Editiononly          | Spectral Arrow                                                                                                                                                        |
| BE&EEonly                 | Ice Bomb                                                                                                                                                              |
| Upcoming                  | Mace Wind Charge                                                                                                                                                      |
| Armor                     | Boots Chestplate Helmet Turtle Shell Horse Armor LeggingsUpcoming   Wolf Armor                                                                                        |
| Upcoming                  | Wolf Armor                                                                                                                                                            |

| BE & EE only | Glow Stick |
|--------------|------------|

| Java Edition only | Spectral Arrow   |
|-------------------|------------------|
| BE&EEonly         | Ice Bomb         |
| Upcoming          | Mace Wind Charge |

| Upcoming | Wolf Armor |
|----------|------------|

| Utilities        |                                                                                                                                                                                                                                                                                                                                                                                             |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Vehicles         | Boat with Chest Minecart with Chest with Hopper with TNTJava Edition only   Minecart with Furnace                                                                                                                                                                                                                                                                                           |
| Java Editiononly | Minecart with Furnace                                                                                                                                                                                                                                                                                                                                                                       |
| Aesthetic        | Item Frame Glow Painting                                                                                                                                                                                                                                                                                                                                                                    |
| Music Discs      | 13 Cat Blocks Chirp Far Mall Mellohi Stal Strad Ward 11 Wait Otherside 5 Pigstep Relic                                                                                                                                                                                                                                                                                                      |
| Informational    | Book and Quill Written Clock Compass Recovery Map Empty Explorer Name Tag Spyglass                                                                                                                                                                                                                                                                                                          |
| Utility          | Armor Stand Bone Meal Bottle o' Enchanting Bowl Bucket Water Lava Milk Powder Snow Axolotl Cod Pufferfish Salmon Tadpole Tropical Fish Enchanted Books End Crystal Eye of Ender Firework Rocket Glass Bottle Water Potion Lingering Splash Goat Horn Lead Saddle Totem of UndyingBE & EE only   Balloon    Medicine Sparkler Super Fertilizer   Upcoming   Ominous Bottle Trial Key Ominous |
| BE&EEonly        | Balloon    Medicine Sparkler Super Fertilizer                                                                                                                                                                                                                                                                                                                                               |
| Upcoming         | Ominous Bottle Trial Key Ominous                                                                                                                                                                                                                                                                                                                                                            |

| Java Edition only | Minecart with Furnace |
|-------------------|-----------------------|

| BE & EE only | Balloon    Medicine Sparkler Super Fertilizer |
|--------------|-----------------------------------------------|
| Upcoming     | Ominous Bottle Trial Key Ominous              |

| Food         |                                                                                                                  |
|--------------|------------------------------------------------------------------------------------------------------------------|
| Natural      | Apple Beetroot Carrot Chorus Fruit Glow Berries Melon Slice Sweet Berries Potato Baked Poisonous Spider Eye      |
| Rawmeat      | Raw Beef Raw Chicken Raw Mutton Raw Porkchop Raw Rabbit Raw Cod Raw Salmon Tropical Fish Pufferfish Rotten Flesh |
| Cookedmeat   | Steak Cooked Chicken Cooked Mutton Cooked Porkchop Cooked Rabbit Cooked Cod Cooked Salmon                        |
| Crafted      | Bread Cookie Dried Kelp Honey Bottle Mushroom Stew Beetroot Rabbit Suspicious Pumpkin Pie                        |
| Supernatural | Golden Apple Enchanted Golden Carrot                                                                             |

| Ingredients        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Seeds              | Beetroot Seeds Cocoa Beans Melon Seeds Pitcher Pod Pumpkin Seeds Torchflower Seeds Wheat Seeds                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Raw materials      | Amethyst Shard Blaze Rod Bone Clay Ball Coal Diamond Disc Fragment 5 Dragon's Breath Echo Shard Emerald Ender Pearl Feather Flint Ghast Tear Glowstone Dust Gunpowder Heart of the Sea Honeycomb Ink Sac Glow Lapis Lazuli Leather Magma Cream Nautilus Shell Nether Quartz Nether Star Nether Wart Phantom Membrane Prismarine Shard Prismarine Crystals Rabbit Hide Rabbit's Foot Raw Copper Raw Gold Raw Iron Redstone Dust Shulker Shell Slimeball Stick String Turtle Scute WheatUpcoming   Armadillo Scute Breeze Rod |
| Upcoming           | Armadillo Scute Breeze Rod                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Processed          | Blaze Powder Book Brick Nether Charcoal Copper Ingot Fermented Spider Eye Firework Star Glistering Melon Slice Gold Ingot Nugget Iron Ingot Nugget Netherite Ingot Netherite Scrap Paper Popped Chorus Fruit SugarBE & EE only   Bleach    Compounds                                                                                                                                                                                                                                                                        |
| BE&EEonly          | Bleach    Compounds                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Dyes               | Black Dye Blue Dye Brown Dye Cyan Dye Gray Dye Green Dye Light Blue Dye Light Gray Dye Lime Dye Magenta Dye Orange Dye Pink Dye Purple Dye Red Dye White Dye Yellow Dye                                                                                                                                                                                                                                                                                                                                                     |
| Banner Patterns    | Flower Charge Creeper Charge Skull Charge Thing Globe SnoutBE & EE only   Field Masoned Bordure Indented   Upcoming   Flow Guster                                                                                                                                                                                                                                                                                                                                                                                           |
| BE&EEonly          | Field Masoned Bordure Indented                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Upcoming           | Flow Guster                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Pottery Sherds     | Angler Archer Arms Up Blade Brewer Burn Danger Explorer Friend Heart Heartbreak Howl Miner Mourner Plenty Prize Sheaf Shelter Skull SnortUpcoming   Flow Guster Scrape                                                                                                                                                                                                                                                                                                                                                      |
| Upcoming           | Flow Guster Scrape                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Smithing Templates | Armor Trim Coast Dune Eye Host Raiser Rib Sentry Shaper Silence Snout Spire Tide Vex Ward Wayfinder Wild Netherite UpgradeUpcoming   Flow Bolt                                                                                                                                                                                                                                                                                                                                                                              |
| Upcoming           | Flow Bolt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

| Upcoming | Armadillo Scute Breeze Rod |
|----------|----------------------------|

| BE & EE only | Bleach    Compounds |
|--------------|---------------------|

| BE & EE only | Field Masoned Bordure Indented |
|--------------|--------------------------------|
| Upcoming     | Flow Guster                    |

| Upcoming | Flow Guster Scrape |
|----------|--------------------|

| Upcoming | Flow Bolt |
|----------|-----------|

| Creative or commands only |                                                                                                                                            |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Creativeonly              | Spawn EggsJava Edition only   Debug Stick Minecart with Command Block Unused Paintings   Minecraft Education only   Camera Photo Portfolio |
| Java Editiononly          | Debug Stick Minecart with Command Block Unused Paintings                                                                                   |
| Minecraft Educationonly   | Camera Photo Portfolio                                                                                                                     |
| Commandsonly              | Boss Spawn Eggs Ender Dragon WitherJava Edition only   Bundle Knowledge Book                                                               |
| Java Editiononly          | Bundle Knowledge Book                                                                                                                      |

| Java Edition only       | Debug Stick Minecart with Command Block Unused Paintings |
|-------------------------|----------------------------------------------------------|
| Minecraft Educationonly | Camera Photo Portfolio                                   |

| Java Edition only | Bundle Knowledge Book |
|-------------------|-----------------------|

| Unused              |                                        |
|---------------------|----------------------------------------|
| All editions        | Mundane Potion Thick Potion            |
| Java Editiononly    | Potion of Luck Uncraftable Potion      |
| Bedrock Editiononly | Camera Potion of Decay  Unused Potions |

| Unimplemented       |                                                          |
|---------------------|----------------------------------------------------------|
| All editions        | Quiver Ruby                                              |
| Java Editiononly    | Crystallized Honey Minecart with Dispenser Studded Armor |
| Bedrock Editiononly | Minecart with Furnace Hoglin Meat                        |

| Joke features    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| April Fools 2015 | Obsidian Boat                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| April Fools 2016 | Smarter Watch Reality Vision Ankle Monitor                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| April Fools 2019 | 3D Blue Key Red Key Yellow Key                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| April Fools 2020 | Footprint A Very Fine Item                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| April Fools 2023 | Air Banner Pattern (New Thing) Bit Bottle of Entity Splash Bottle of Void La Baguette Le Tricolore minecraft:dupe_hack Moon Cow Spawn Egg Longer String Potion of Big Splash Lingering Arrow Potion of Small Splash Lingering Arrow Tag                                                                                                                                                                                                                                                                                                                                              |
| April Fools 2024 | Amber Gem Batato Spawn Egg Golden Poisonous Potato Enchanted Dent Hash Browns Hot potato Mega Spud Spawn Egg Plaguewhale Slab Spawn Egg Poisonous Polytra Poisonous Pota-Toes Poisonous Potato Chestplate Poisonous Potato Chips Poisonous Potato Fries Poisonous Potato Plant Poisonous Potato Slices Poisonous Potato Sticks Poisonous Potato Zombie Spawn Egg Poisonous Potato Hammer Potato Eye Potato of Knowledge Potato Oil Poisonous Potato Peeler Potato Peels Corrupted Potatiesh, Greatstaff of the Peasant Toxic Beam Toxic Resin Toxifin Slab Spawn Egg Venomous Potato |

| Removed             |                                                |
|---------------------|------------------------------------------------|
| Java Editiononly    | Cauldron Potions Horse Saddle Reverted Potions |
| Bedrock Editiononly | Copper Horn                                    |
| Legacy Consoleonly  | debug fourj item                               |
| MinecraftEduonly    | Block Inspector                                |

