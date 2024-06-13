# Hopper
A hopper is a low-capacity storage block that can be used to collect item entities directly above it, as well as to transfer items into and out of other containers. A hopper can be locked with redstone power to stop it from moving items into or out of itself.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Crafting
- 2 Usage
	- 2.1 Container
	- 2.2 Crafting ingredient
	- 2.3 Redstone component
		- 2.3.1 Redstone signals
		- 2.3.2 Collecting items
		- 2.3.3 Pushing and pulling items
		- 2.3.4 Container interactions
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
	- 4.3 Block data
- 5 Achievements
- 6 Video
- 7 History
- 8 Issues
- 9 Trivia
- 10 Gallery
	- 10.1 Renders
		- 10.1.1 Java Edition
		- 10.1.2 Bedrock Edition
	- 10.2 Screenshots
- 11 References

## Obtaining
### Breaking
To obtain a hopper, mine it with a pickaxe. Using any other item to mine a hopper drops only its contents.

| Block     | Hopper                |
|-----------|-----------------------|
| Hardness  | 3                     |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 15                    |
| Wooden    | 2.25                  |
| Stone     | 1.15                  |
| Iron      | 0.75                  |
| Diamond   | 0.6                   |
| Netherite | 0.5                   |
| Golden    | 0.4                   |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Crafting
A hopper can be crafted from 5 iron ingots and a chest.

| Ingredients           | Crafting recipe |
|-----------------------|-----------------|
| Iron Ingot+<br/>Chest |                 |

## Usage
See also: Tutorials/Hopper

Hoppers can face down or sideways.
A hopper can be used as a container, as a crafting ingredient, and as a redstone component.

A hopper has an "output" tube at its bottom that can face down or sideways and provides a visual indication of which block the hopper is set up to drop its items into, if that block has an inventory. To place a hopper, use the Place Block control while aiming at the surface to which its output should face (Hoppers do not orient themselves automatically). To place a hopper directly on the face of an already interactable block, the player can sneak while placing the hopper. Attempting to place a hopper aimed on the bottom face of a block instead faces downward. With some blocks, such as the furnace and brewing stand, the hopper has multiple uses. A hopper does not change direction after placement, and it is not attached to the container it faces; the container can be removed or replaced, and the hopper remains unchanged.

Hoppers cannot be moved by pistons.‌[Java Edition  only] Despite not being a solid block, attached blocks such as rails, levers, tripwire and redstone dust can be placed on top of hoppers, but not on their sides.

### Container
Hopper GUI showing the hopper's five slots of inventory at the top and the player's inventory below.
A hopper can be used as a container and has 5 slots of inventory space.

To open the hopper GUI, use it. To move items between the hopper inventory and the player inventory or hotbar while the hopper GUI is open, drag or shift-click the items. To exit the hopper GUI, use the Esc key, B button or circle button, depending on the device.

By default, the GUI of a hopper is labeled "Item Hopper". A hopper's GUI label can be changed by naming the hopper in an anvil before placing it, or, in Java Edition, by using the data command (for example, to label a hopper at (0,64,0) "Steve's Hopper", use /data merge block 0 64 0 {CustomName:'"Steve's Hopper"'}).

In Java Edition, a hopper's GUI can be "locked" (or subsequently unlocked) by setting the hopper's Lock tag with the data command. If a hopper's Lock tag is not blank, the hopper cannot be accessed except by players holding an item with the same name as the Lock tag's text. For example, to lock a hopper at (0,64,0) so that only players holding an item named "Steve's Key" can access the hopper, use /data merge block 0 64 0 {Lock:"Steve's Key"}.

### Crafting ingredient
| Name                 | Ingredients          | Crafting recipe |
|----------------------|----------------------|-----------------|
| Minecart with Hopper | Hopper+<br/>Minecart |                 |

### Redstone component
See also: Redstone circuit and Redstone components § Hopper

Flowchart of hopper logic
While a hopper is not powered by redstone signals, it operates with three functions:

- Collectitem entities(free-floating items in the world) into its inventory from the space above it
- Pulla single item into its inventory from a container above it
- Pusha single item from its own inventory into a container it faces

A hopper first attempts to push any items inside it. Afterward, it checks if the block above it is a type of container. If so, it attempts to pull from it. Otherwise, the hopper attempts to collect item entities. Notably, hoppers can push to and pull from other hoppers, forming hopper pipes or hopper chains, which allow transporting items across several blocks and are further discussed below.

#### Redstone signals
When a hopper receives a redstone signal (and is considered to be "activated"), all three functions stop. To avoid confusion over the terms "activated" and "deactivated", powered hoppers are often described as being locked and unpowered hoppers described as being unlocked. Hoppers can be powered by soft powered blocks, meaning a redstone dust trail pointing into a block touching the hopper locks it just as effectively as a block of redstone or any other power component touching the hopper. When the hopper is unlocked during a redstone tick, it does not push or pull/collect during the same tick, but has a delay of 1 redstone tick instead.

While a locked hopper does not push or pull/collect items, it may still receive items from dispensers, droppers and other hoppers, and may have its items pulled out by another hopper beneath it. Hence, the item flow in a horizontal hopper pipe may be stopped by locking just one of the hoppers, but stopping a vertical hopper pipe requires locking two adjacent hoppers at the same time, such that both the pushing of the top one and the pulling of the bottom one are stopped.

A hopper does not output any redstone signals by itself, but its fullness can be read using a redstone comparator, which needs to be placed next to it and facing away from it. An empty hopper outputs a signal strength of 0 and a completely full hopper outputs a signal strength of 15. Notably, a single stackable item (16 or 64) outputs a signal strength of 1 and a single non-stackable item outputs a signal strength of 3.

In Java Edition, if the hopper being read is part of a horizontal hopper pipe, the comparator can individually read each item passing through the chain, because items are pushed through the hoppers one by one at a speed that is manageable by the comparator. If there is an uninterrupted stream of items, the comparator does not switch off in between items. On the other hand, in a vertical hopper pipe, some of the hoppers may never produce a reading above 0, even with a continuous stream of items, because pushes and pulls both occur in the same game tick: The hoppers' items get pulled out a single game tick after they're pushed in and this isn't measurable by a comparator, because comparators need measurements lasting at least 1.5 redstone ticks to produce a reading.

#### Collecting items
A hopper collects items dropped on top of it if the space above the hopper not occupied by a storage block, as well as items landing inside the hopper block itself, regardless of the block above. Items are gathered from the entire 1 block space above the hopper, meaning that items sitting on partial blocks such as soul sand directly above a hopper can be collected.[1] It is also possible for a hopper to collect items from inside a full, solid block, a situation that might come from items rising up through solid blocks or being summoned. Item entities are not collected when they are outside of the collection area however; for example, items on top of a stone block directly above a hopper are not collected. Collected items are placed in the leftmost empty slot of a hopper's inventory.

In Java Edition, if there is no container above the hopper, then the hopper collects dropped items in the order in which they landed on the hopper. This order is remembered even while a hopper is locked. For instance, if a hopper is locked under a carpet while a fully equipped armor stand is broken above it, then it always collects items in this order when it is unlocked: armor stand, boots, leggings, chestplates, helmets. This is due to the order in which these items land.[verify] In Bedrock Edition, hoppers do not remember the order in which items land on the hopper. Instead, hoppers with multiple dropped items above them collect the items in the order in which they entered the chunk in which the hopper is located. Items that drop from a broken armor stand are collected in a random order.[2]

Hoppers usually check for dropped items every game tick and they can collect items even before they are picked up by a player[verify] or destroyed by lava. However, in Bedrock Edition hoppers have a "collection cooldown" time. After collecting an item (or stack of items), a hopper waits 4 redstone ticks (0.4 seconds, barring lag) before attempting to collect again.

Hoppers collect groups of items all at once rather than collecting them as single items one at a time. As a result, hoppers can collect item entities much faster than they can pull items from a container. Pulling from a moving minecart with chest or minecart with hopper is even slower, since the minecart is not always above the hopper.

#### Pushing and pulling items
A hopper with a storage container above it (such as a furnace, chest, dropper, composter, or another hopper) attempts to pull from the container instead of checking for floating items above it, and hence can not collect dropped items. A hopper always tries to push or pull items using the leftmost available slot. When a hopper is removing items from a chest, the items disappear from left to right. Similarly, when filling up a chest, the chest fills up from left to right. Hoppers prioritize pulling from the first slot of a container over pulling into the first hopper slot. If a hopper has stone in its first slot and nothing in its second while the container it is pulling from has chicken in its first slot but stone in the second, the hopper pulls the chicken from the first slot of the container into its empty second slot. However, if the hopper is unable to pull the chicken, such as if all slots are filled with stone, the hopper pulls the stone from the second slot of the container instead. Similarly, hoppers prioritize pushing from their first slot over pushing into the first slot of a container. If a hopper has stone in its first slot and chicken in its second while the container it is pushing to has chicken it its first slot but stone in the second, the hopper pushes stone from its first slot into the second slot of the container.

In Java Edition, the checks done by a hopper while pulling generally require less processing than the checks done by a hopper attempting collection. Therefore, a chain of hoppers topped with storage containers rather than air/solid blocks has better performance (measured as milliseconds of processing per tick) and lower potential for processing lag. [3] The performance improvement achieved is correlated with the number of storage slots the container has. Placing composters (with no storage slots but still with custom output logic) on top of hoppers provide the greatest efficiency‌[until JE 1.20.5], while double chests actually degrade performance, even when sharing each double chest across two hoppers.[3] In Bedrock Edition, a chain of hoppers with air or non-container blocks on top has better performance than a chain of hoppers topped by container blocks.[4] This may be because, even though hoppers with containers on top do not check for items, they do check for hopper-minecarts and chest-minecarts to pull from, and that involves scanning the chunk entity list.[5]




A






B


Push then pull

Chest A is full of items while the hopper and chest B are empty.
Item pushes and pulls are processed in the same game tick, but pushes are processed before pulls. In the schematic, the empty hopper first pulls an item from chest A as it cannot push anything into chest B. After the cooldown, the hopper first pushes its item into chest B before pulling another item from chest A, both pushing and pulling in the same tick, and the process repeats. The hopper stops pulling when A is empty, and stops pushing when B becomes full.

Hoppers also have a "transfer cooldown" time. After pulling and/or pushing items, a hopper waits 4 redstone ticks (0.4 seconds, barring lag) before pulling or pushing again (a transfer rate of 2.5 items per second, barring lag). A hopper that has an item pushed into it from another hopper also starts a 4 tick cooldown period, regardless of whether it pushed or pulled items itself. Item entities can be collected at any time without affecting the transfer cooldown time. The transfer cooldown and the Bedrock Edition collection cooldown are independent of each other.

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

| Name   | Identifier | Form         | Translation key          |
|--------|------------|--------------|--------------------------|
| Hopper | `hopper`   | Block & Item | `block.minecraft.hopper` |

| Name         | Identifier |
|--------------|------------|
| Block entity | `hopper`   |

Bedrock Edition:

| Hopper | Identifier | Numeric ID | Form                         | Item ID[i 1]  | Translation key    |
|--------|------------|------------|------------------------------|---------------|--------------------|
| Block  | `hopper`   | `154`      | Block & Ungiveable Item[i 2] | `item.hopper` | `tile.hopper.name` |
| Item   | `hopper`   | `527`      | Item                         | —             | `tile.hopper.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Unavailable with /give command

| Name         | Savegame ID |
|--------------|-------------|
| Block entity | `Hopper`    |

### Block states
See also: Block states

Java Edition:

| Name    | Default value | Allowed values                                       | Description                                                                                                                              |
|---------|---------------|------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| enabled | `true`        | `false`<br/>`true`                                   | True if hopper can move items to and from its inventory.<br/>When the hopper is being powered by redstone current, this is set to false. |
| facing  | `down`        | `down`<br/>`east`<br/>`north`<br/>`south`<br/>`west` | The direction the hopper's output points.<br/>The hopper pushes items into containers in this direction only.                            |

Bedrock Edition:

| Name             | Metadata Bits             | Default value | Allowed values                      | Values forMetadata Bits             | Description                                                                                                                                                                                                                                                       |
|------------------|---------------------------|---------------|-------------------------------------|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing_direction | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4` | The direction the hopper's output points.<br/>The hopper pushes items into containers in this direction only.0: Output facing down<br/>1: (unused)<br/>2: Output facing north<br/>3: Output facing south<br/>4: Output facing west<br/>5: Output facing east<br/> |
| toggle_bit       | `0x8`                     | `false`       | `false`<br/>`true`                  | `0`<br/>`1`                         | 1 if hopper cannot move items to and from its inventory.<br/>When the hopper is being powered by redstone current, this is set to true.                                                                                                                           |



### Block data
A hopper has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format

- Block entity data
	- 
	- Tags common to all block entities
	- 
	- Tags common to all objects that can be renamed
	- Items: List of items in this container.
		- : An item, including the slot tag.
			- 
			- Tags common to all items
	- 
	- Tags common to all containers that can be locked
	- 
	- Tags common to all objects that use loot tables to produce items
	- TransferCooldown: Time until the next transfer ingame ticks, naturally between 1 and 8 or 0 if there is no transfer.

Bedrock Edition:

SeeBedrock Edition level format/Block entity format.
