### Drops

  

This feature is exclusive to  Bedrock Edition. 


Vindicators and pillagers that spawn from raids have a small chance to drop an enchanted book with a level 30 enchantment, which may be a treasure enchantment.

### Enchanting
An enchanted book with multiple high level enchantments.
An enchanted book with multiple enchantments that can be applied to the same item.
Players can create an enchanted book by enchanting a book on an enchantment table. Books have a decreased chance of getting multiple enchantments (specifically, if multiple enchantments would be added, then one is removed at random), and have a lower "enchantability level" than most other items. Treasure enchantments such as Mending cannot be obtained from an enchantment table.

### Bartering
Players can barter with piglins by using or throwing gold ingots, and doing so has a 5⁄459 chance for piglins to give the player an enchanted book with any level of Soul Speed. Soul Speed enchanted books are obtainable only through bartering, chest loot inside a bastion remnant, and fishing. They cannot be obtained through enchanting or trading.

## Usage
See also: Anvil mechanics

In Survival, enchanted books are the only method to obtain certain enchantments on certain tools, such as Unbreaking on shields. Enchanted books have a shine effect on their sprite.

To use an enchanted book, the player must place an item in the first slot in an anvil, and a book in the next. In order to complete the enchantment, the player must have the required amount of experience. Note that using an enchanted book gets significant discounts at the anvil. Enchanted books themselves can be combined to create a single book with increased or multiple enchantments, similar to combining tools or weapons.

When combining items, the compatible enchantments from the book in the second slot are transferred to the item from the first slot, keeping the highest level of any type. If two enchantments have the same level and a higher level is available, they combine into the next level. If a book is applied to an item that can't take all of its spells, the appropriate spells are transferred, while the unusable ones are lost. Enchanted books are single-use. 

Enchanted books do not exhibit their enchantment. For example, a book with Sharpness IV as an enchantment does no more damage than an un-enchanted book, or any non-weapon item, would when used as a weapon. An exception is the Fire Aspect book which can ignite TNT and light campfires and the Fortune book if the block mined can be broken by fist.‌[Bedrock Edition  only]

### Available items
See also: Enchantments

Enchanted books can enchant the usual items that can be enchanted at an enchanting table, but unlike an enchanting table, they are able to boost enchantments such as Sharpness or Thorns to their maximum power, and may apply the following enchantments to items (the table displays only netherite tools and armor, but any type can be enchanted):

| Enchantment        | Items not enchantableat an enchanting table | Note                                                                 |
|--------------------|---------------------------------------------|----------------------------------------------------------------------|
| Efficiency         |                                             | Increases mining speed                                               |
| Thorns             |                                             | Inflicts damage on attacker                                          |
| Unbreaking         | <br/>                                       | Increasing durability on enchanted tools/armors                      |
| Frost Walker       |                                             | Creates walkable ice layer over water                                |
| Mending            | <br/>                                       | Uses XP orbs to repair damaged tools/weapons/armors                  |
| Curse of Binding   | <br/>                                       | Prevents removal of cursed item                                      |
| Curse of Vanishing | <br/>                                       | Cursed item is destroyed upon death                                  |
| Soul Speed         |                                             | The wearer's speed is increased when walking onsoul sandorsoul soil. |
| Swift Sneak        |                                             | The wearer's sneaking speed is increased.                            |

### Creative mode
The player can enchant any item with any enchantment in Creative mode, allowing any applied effects to exhibit themselves.‌[Java Edition  only] For example, a stick can be enchanted with Silk Touch to allow the player to successfully dig grass blocks. The enchanted item can still be used in Survival mode without any loss of enchantments.

Enchantments that are normally incompatible are still incompatible; for example, Piercing and Multishot cannot be both applied to the same item, even in Creative mode.

If a block is enchanted, it loses the enchantment upon being placed in the world.

### Disenchanting
Disenchanting an enchanted book at a grindstone yields a normal book and some experience depending on the quality of the book.

### Chiseled bookshelf
Using the chiseled bookshelf while having an enchanted book in the main hand puts the book inside the chiseled bookshelf. Hoppers also interact with the chiseled bookshelf to insert and remove books, allowing it to act as an item filter in various mob farms.

## Data values
### ID
Java Edition:

| Name           | Identifier       | Form | Translation key                 |
|----------------|------------------|------|---------------------------------|
| Enchanted Book | `enchanted_book` | Item | `item.minecraft.enchanted_book` |

Bedrock Edition:

| Name           | Identifier       | Numeric ID | Form | Item tags                   | Translation key            |
|----------------|------------------|------------|------|-----------------------------|----------------------------|
| Enchanted Book | `enchanted_book` | `521`      | Item | `minecraft:bookshelf_books` | `item.enchanted_book.name` |

### Item data
Java Edition:

Main article: Item format
Enchanted books use an NBT tag, called StoredEnchantments, to indicate their enchantments. 

The allowed properties on an individual are id and lvl.

- tag: Item data.
	- StoredEnchantments: The list of enchantments on this book.
		- Each enchantment.
			- id: The in-game ID of the enchantment.
			- lvl: The level of the enchantment.

Bedrock Edition:

SeeBedrock Edition level format/Item format.

