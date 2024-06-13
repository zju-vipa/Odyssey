# Dropper
A dropper is a low-capacity storage block that can eject its contents into the world or into other containers when given a redstone signal.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Crafting
- 2 Usage
	- 2.1 Container
	- 2.2 Redstone component
		- 2.2.1 Container interactions
	- 2.3 Note blocks
	- 2.4 Crafting ingredient
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
	- 4.3 Block data
- 5 Video
- 6 History
- 7 Issues
- 8 Trivia
- 9 Gallery
	- 9.1 Renders
		- 9.1.1 Java Edition
		- 9.1.2 Bedrock Edition
- 10 See also
- 11 References
- 12 External links

## Obtaining
### Breaking
A dropper can be mined with a pickaxe, in which case it drops itself and its contents. If mined without a pickaxe, the dropper drops only its contents.

| Block     | Dropper               |
|-----------|-----------------------|
| Hardness  | 3.5                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 17.5                  |
| Wooden    | 2.65                  |
| Stone     | 1.35                  |
| Iron      | 0.9                   |
| Diamond   | 0.7                   |
| Netherite | 0.6                   |
| Golden    | 0.45                  |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Crafting
| Ingredients                    | Crafting recipe |
|--------------------------------|-----------------|
| Cobblestone+<br/>Redstone Dust |                 |

## Usage
A dropper can be used as a container or as a redstone component to move items.

A dropper can be placed so that its output faces in any direction, including up or down. When placed, the dropper's output faces toward the player. With default textures, the droppers output side looks like a face when positioned for horizontal output. Otherwise, the output side has a square hole.

In Java Edition, droppers cannot be moved by pistons.

### Container
GUI of the dropper.
A dropper has 9 slots of inventory space.

To open the dropper GUI, use the Use Item control. To move items between the dropper inventory and the player inventory or hotbar while the dropper GUI is open, drag or shift-click the items. To exit the dropper GUI, use the Esc control.

By default, the GUI of a dropper is labeled "Dropper". A dropper's GUI label can be changed by naming the dropper in an anvil before placing it. In Java Edition, droppers can also be renamed by using the /data command (for example, to label a dropper at (0,64,0) "Alice's Dropper", use /data merge block 0 64 0 {CustomName:'"Alice's Dropper"'}).

In Java Edition, a dropper can be "locked" (or subsequently unlocked) by setting the dropper's Lock tag with the /data command. If a dropper's Lock tag is not blank, the dropper cannot be accessed except by players holding an item with the same name as the Lock tag's text. For example, to lock a dropper at (0,64,0) so that only players holding an item named "Alice's Key" can access the dropper, use /data merge block 0 64 0 {Lock:"Alice's Key"}.

### Redstone component
See also: Redstone circuit

A dropper can be used to eject items, or push items into another container.

** Activation **
A dropper can be activated by:
- an adjacent activepower component(exceptions:a redstone torch does not turn ON a dropper it is attached to)
- an adjacent powered opaqueblock(strongly-powered or weakly-powered)
- a poweredredstone repeaterorredstone comparatorfacing the dropper
- poweredredstone dustconfigured to point at the dropper, or on top of it; a dropper isnotactivated by adjacent powered redstone dust that is configured to point in another direction.

In addition to the methods above, droppers inJava Editioncan also be activated byquasi-connectivity. A dropper activates if one of the methods abovewouldactivate a mechanism component in the block above the dropper, even if there is no mechanism component there (even if the block above the dropper isairor a transparent block), but only when the dropper receives a block update (including a redstone update within two blocks of the dropper).
A dropper has a 2redstone tick(4 game ticks, or 0.2 seconds barring lag) delay between activation and a response. During this time, additional inputs are ignored.
** Behavior **
See also: Tutorials/Item elevator § Dropper

When activated, a dropper waits 2 redstone ticks (4 game ticks, or 0.2 seconds barring lag) and then ejects one item from its inventory. The dropper does not continue to eject items while activated — ejection occurs only on the initial activation (therising edgeof an input signal). To eject multiple items, repeatedly activate the dropper with aclock circuit.
If multiple slots are occupied by items, a random occupied slot is chosen for ejection. The slot is chosen when an item is ejected, not when the dropper is initially activated, thus it is possible to move items into or out of a dropper between its activation and item dispensing.
If the dropper is facing a container, the ejected item is transferred into the container. If the container it is facing is full, or the item cannot be inserted into the container, the dropper does not activate.
Otherwise, the item is ejected in the direction the dropper is facing, as if a player had used thedropcontrol. Even items that would be treated differently by adispenser(such asarrows) are simply ejected by a dropper.
A dropper makes a clicking noise (therandom.clicksound event) when activated empty or when ejecting items into air. It is silent when it successfully transfers an item into any kind of chest or barrel, or another dropper.
A dropper is an opaque block, so powering it directly can cause adjacent mechanism components (including other droppers) to activate as well.

A line of droppers, each pushing items into the next dropper, is known as a dropper pipe. A dropper pipe must be clocked to move items, but can be clocked to move items faster than a hopper pipe's transfer rate. When a dropper pipe pushes items upward, it is known as a droppervator (short for "dropper elevator").

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
