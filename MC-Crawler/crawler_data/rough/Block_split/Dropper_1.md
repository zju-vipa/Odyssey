#### Container interactions
Some containers interact with droppers in specific ways:

Barrel, boat with chest, dispenser, dropper
Droppers interact normally with barrels, boats with chests, dispensers, and other droppers.
Brewing stand
A dropper facing toward a brewing stand from above deposits only into the ingredient slot and it can insert only valid brewing ingredients. A dropper facing toward a brewing stand from the sides or from below can deposit only blaze powder in the fuel slot, or filled bottles into the three brew slots.
Chest, trapped chest
Large chests and large trapped chests are treated as a single container: a dropper depositing into a large chest fills up the entire chest. Trapped chests being accessed by a player trigger any adjacent droppers, depositing items into the chest if they are facing toward it.
Chiseled bookshelf
A dropper facing toward a chiseled bookshelf from any direction can insert books, books and quills, written books, enchanted books, and knowledge books.
Crafter‌[upcoming: JE 1.21 & BE 1.21.0]
Droppers can insert ingredients in the crafting grid. Items are distributed in enabled slots, going left to right starting from the first row; if the crafter has all item slots filled then items are added to the lowest count item stack of the same type.
Composter
A dropper facing toward a composter from above can push compostable items into the composter, with a chance of increasing the compost level as if the player used the item on the composter.
Decorated pot
Droppers can deposit up to a stack of a single type of item into a decorated pot. Items are not inserted if the decorated pot is full or the pot contains a different item.
Ender chest
Droppers cannot interact with ender chests in any way.
Furnace, blast furnace, smoker
A dropper facing toward a furnace from above deposits only into the ingredient slot. It can insert any item, including items that can't be smelted by the furnace. A dropper facing toward a furnace from the sides or from below deposits only into the fuel slot, and only items that are usable as fuel.
Hopper
A dropper facing toward a hopper can insert items even if the hopper is locked by an active redstone signal.
Jukebox
A dropper can insert music discs into a jukebox from any direction. The dropper does not activate if the jukebox is already playing a disc.
Lectern
Droppers cannot interact with lecterns in any way.
Minecart with chest, minecart with hopper
A dropper can insert items into minecarts with chests and minecarts with hoppers if any part of the entity's hitbox is within the dropper's target block-space. A dropper can fill a minecart with hopper even if the latter has been locked by an activator rail.
Shulker box
Droppers cannot put shulker boxes into other shulker boxes. Otherwise, droppers interact with shulker boxes normally.
### Note blocks
Droppers can be placed under note blocks to produce "bass drum" sounds.

### Crafting ingredient
| Name    | Ingredients                                                    | Crafting recipe | Description                      |
|---------|----------------------------------------------------------------|-----------------|----------------------------------|
| Crafter | Iron Ingot+<br/>Crafting Table+<br/>Redstone Dust+<br/>Dropper |                 | ‌[upcoming: JE 1.21 & BE 1.21.0] |

## Data values
### ID
Java Edition:

| Name    | Identifier | Form         | Translation key           |
|---------|------------|--------------|---------------------------|
| Dropper | `dropper`  | Block & Item | `block.minecraft.dropper` |

| Name         | Identifier |
|--------------|------------|
| Block entity | `dropper`  |

Bedrock Edition:

| Name    | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key     |
|---------|------------|------------|----------------------------|----------------|---------------------|
| Dropper | `dropper`  | `125`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.dropper.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

| Name         | Savegame ID |
|--------------|-------------|
| Block entity | `Dropper`   |

### Block states
See also: Block states


Java Edition:

| Name      | Default value | Allowed values                                                | Description                                                                                                                        |
|-----------|---------------|---------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| facing    | `north`       | `down`<br/>`east`<br/>`north`<br/>`south`<br/>`up`<br/>`west` | The direction in which contents are shot or dropped.<br/>The opposite from the direction the player faces while placing the block. |
| triggered | `false`       | `false`<br/>`true`                                            | True if this block is activated.                                                                                                   |

Bedrock Edition:

| Name             | Metadata Bits             | Default value | Allowed values                                              | Values forMetadata Bits                                     | Description                                                                                                                                                            |
|------------------|---------------------------|---------------|-------------------------------------------------------------|-------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing_direction | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7` | The direction in which contents are shot or dropped.0: facing down<br/>1: facing up<br/>2: facing north<br/>3: facing south<br/>4: facing west<br/>5: facing east<br/> |
| triggered_bit    | `0x8`                     | `false`       | `false`<br/>`true`                                          | `0`<br/>`1`                                                 | True if this block is activated.                                                                                                                                       |



### Block data
A dropper has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format

- Block entity data
	- 
	- Tags common to all block entities
	- 
	- Tags common to all objects that can be renamed
	- Items: List of items in this container.
		- : An item, including the slot tag. Dropper slots are numbered 0-8 with 0 in the top left corner.
			- 
			- Tags common to all items
	- 
	- Tags common to all containers that can be locked
	- 
	- Tags common to all objects that use loot tables to produce items
	- Lunar: Exists only in the april fools snapshot23w13a_or_b. Optional. When set to any full number from -128 to 127, turns it to a lunar base dropper, and placing light or heavypressure plateon top of it creates thelunar basestructure.

Bedrock Edition:

SeeBedrock Edition level format/Block entity format.

