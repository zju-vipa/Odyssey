#### Container interactions
Some containers interact with hoppers in specific ways:

Barrel, boat with chest, dispenser, dropper
Hoppers interact normally with barrels, dispensers, droppers, and boats with chests.
Brewing stand
A working hopper on the top face of a brewing stand deposits only into the ingredient slot and it can push only valid brewing ingredients. A hopper on side face of a brewing stand can deposit only blaze powder or bottles (including empty bottles) into the three brew slots. A hopper underneath a brewing stand always extracts from the three brew slots, whether brewing is finished or not—The hopper must be locked to allow potions to finish brewing.
Chest, trapped chest
Large chests and large trapped chests are treated as a single container: a hopper depositing into a large chest fills up the entire chest and a hopper underneath a large chest empties the entire chest. Trapped chests being accessed by a player lock any adjacent hoppers, per the standard behavior of a hopper next to an active power source.
Chiseled bookshelf
Hoppers and minecarts with hoppers can insert and remove books from the bookshelf. As with any other container, items are taken from the first slot that has an item that can fit in the hopper and are inserted into the first empty slot.
Composter
Hoppers above composters can push compostable items into the composter's top face, with a chance of increasing the compost level as if the player used the item on the composter. Items that are not compostable cannot be pushed into the composter. Hoppers below the composter can pull bone meal when the composter is in stage 8, emptying the composter and resetting it to stage 0. Hoppers to the side of a composter do not interact with it.
Crafter‌[upcoming: JE 1.21 & BE 1.21.0]
Hoppers can insert ingredients in the crafting grid. Items are distributed in enabled slots, going left to right starting from the first row; if the crafter has all item slots filled then items are added to the lowest count item stack of the same type. A hopper below a crafter collects the ingredients from the crafting grid, not the resulting item.
Decorated pot
Hoppers can deposit up to a stack of a single type of item into a decorated pot. Items are not pushed if the decorated pot is full or the pot contains a different item. Using a hopper (or a minecart with hopper) is the only way to retrieve items from a decorated pot without breaking it.
Ender chest
Hoppers cannot interact with ender chests in any way.
Furnace, blast furnace, smoker
A working hopper pointing into the top of a furnace deposits only into the ingredient slot. It can push any item, including items that can't be smelted by the furnace. A hopper pointing into the side of a furnace deposits into the fuel slot, and only items that are usable as fuel. A hopper below a furnace pulls everything from the output slot and empty buckets from the fuel slot left over from using lava buckets as fuel. When a hopper removes items from a furnace, the experience points are 'stored' in the furnace until a player removes at least one smelted item, or the furnace block is broken.
 Other hoppers
A sequence of three or more hoppers, each pushing items into the next, is called a hopper pipe. Working horizontal hopper pipes simply push items into each other at the expected rate of 2.5 items per second, but vertical hopper pipes are more complicated, as the hoppers are trying both to pull and to push. When a vertical pipe pulls from a single container, it simply transfers items at 2.5 items per second because the transfer rate is limited by the first hopper pulling items from the container. If a stack of items is in a vertical pipe, the items can be transferred twice as fast, because the hopper with the item stack is pushing items down while the hopper below it is also pulling items down.
Jukebox
Hoppers can insert music discs into jukeboxes, and extract the music discs after they finish playing. A jukebox emits a redstone signal while playing a disc, locking any adjacent hoppers.
Lectern
Hoppers cannot remove or place books on lecterns. The redstone pulse emitted from a lectern when a page is turned can temporarily lock hoppers.
Minecart with chest, minecart with hopper
Unlocked hoppers fill minecarts with chests and minecarts with hoppers if any part of the entity's hitbox is within the hopper's target block-space. Hopper minecarts try to pull items from the hopper at high speed. Hoppers can pull items from minecarts above them so rails can be placed directly on the top faces of a hoppers. If a detector rail is in the right position, it could lock the hopper per standard redstone-hopper behavior.
Shulker box
Hoppers cannot put shulker boxes into other shulker boxes. This allows for the creation of certain item filters.
Otherwise, hoppers interact with shulker boxes normally.
## Data values
### ID
Java Edition:

| Name   | Identifier | Form         | Translation key        |
|--------|------------|--------------|------------------------|
| Hopper | hopper     | Block & Item | block.minecraft.hopper |

| Name         | Identifier |
|--------------|------------|
| Block entity | hopper     |

Bedrock Edition:

| Hopper | Identifier | Numeric ID | Form                         | Item ID[i 1] | Translation key  |
|--------|------------|------------|------------------------------|--------------|------------------|
| Block  | hopper     | 154        | Block & Ungiveable Item[i 2] | item.hopper  | tile.hopper.name |
| Item   | hopper     | 527        | Item                         | —            | tile.hopper.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Unavailable with /give command


| Name         | Savegame ID |
|--------------|-------------|
| Block entity | Hopper      |

