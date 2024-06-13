# Anvil mechanics
This page explains the mechanics of the anvil. The anvil is primarily used to repair tools, armor and weapons, which it can do without stripping their enchantments, unlike the grindstone and crafting table. It can also be used to combine the enchantments of two items, to give an item a custom name, or to crush enemies, mobs or other players that walk beneath it while it is falling, with more damage inflicted upon the target from each block fallen. All its functions, except for damaging mobs and players, cost experience levels, and some have material costs.

The anvil has five basic functions:

## Contents
- 1 Anvil uses
- 2 Renaming
- 3 Unit repair
- 4 Combining items
	- 4.1 Costs for combining enchantments
		- 4.1.1 Planning the enchanting order
		- 4.1.2 Enchantment equation
- 5 Notes
- 6 External links
- 7 References

## Anvil uses
Anvil uses are the number of times an item has been used in an anvil. 

Every time an item is used in an anvil, except for being renamed, it gets one anvil use. If the player adds an enchanted book that has never been used in an anvil with a sword that has never been used in an anvil, then the sword gains 1 anvil use.

As an item gets more anvil uses, the experience required to use the item in the anvil increases to the point where it says "Too expensive!" From there the player must use creative mode to repair/enchant/rename items using an anvil. 

Combining items of the same or different number of anvil uses takes the greater number and adds 1 for the final product. For example, two items with 2 anvil uses are combined into one with 3 anvil uses. For another example, an item with 3 anvil uses and an item with 2 anvil uses yields one with 4 anvil uses. 

Using an enchantment table on an item does not affect anvil uses.

| Anvil use count | Penalty (RepairCost) |
|-----------------|----------------------|
| 0               | 0                    |
| 1               | 1                    |
| 2               | 3                    |
| 3               | 7                    |
| 4               | 15                   |
| 5               | 31                   |

The formula for prior use penalty is:

 (prior use penalty) = 2^(Anvil use count) - 1

Item repair on a crafting grid removes all prior work penalties, enchantments, and custom names. If a grindstone is used, the item instead keeps its custom name while losing all its prior work penalties and enchantments (except for curses), returning some XP from enchantments in the process.

## Renaming
Any item or stack of items can be renamed. If only renaming an item or stack of items (instead of enchanting or repairing), renaming costs a single level in addition to any prior work penalty. There is no extra cost to renaming a stack of items as opposed to renaming a single item. The maximum level cost is 39 levels even if the prior work penalty is higher. Renaming does not increase the prior work penalty. However, if the penalty reaches or exceeds 2147483647, further renames become impossible.

An item can be renamed at the same time it is repaired or enchanted. In those cases, renaming adds 1 level of cost to the total enchanting or repair cost.

If the item name field is left blank, or is only whitespace or non-breaking spaces (or a combination of both), the default name for that item is used instead. Also, if the item name is unchanged from its current name (which can occur when renaming an item for the first time and using any of the aforementioned blank parameters), a red "X" appears on top of the arrow in the GUI.

Renamed items can stack only with renamed items that share exactly the same name and work penalty. Renaming an item that doesn't have a work penalty gives it a work penalty of 0, making it stackable only with renamed items, even if it's custom name is reset. The custom name of a renamed item can be reset by renaming it to a name that consists of spaces. However, that item's repair cost is not reset. Therefore, it cannot be stacked with other items of the same type with different repair costs or with items that have never been renamed.

Because prior work penalty is charged for any rename, it is most economical to rename a weapon either before or while repairing or enchanting it, minimizing the penalty the player must pay for the rename.

Renamed blocks that do not normally store block entity data lose their name and repair cost when placed. Blocks such as chests and shulker boxes, which do have associated block entity data, retain their custom names (but do not retain their repair cost).

## Unit repair
Some items are "tiered" and can be repaired using units of its repair material, each unit restores up to 25% total durability of the item (rounded down) and costs 1 level per unit of material used in addition to any applicable prior work penalties.

- The material to use is specific for each item (see the table below). For many items, this is determined by itstierorarmor material.
- Due to the rapid increase in prior work penalty for each repair, it is generally most effective to use an item almost to the breaking point and then repair using four units of raw material at once (or bycombiningwith a newly crafted instance of the item).
- If enchantments are added to raw materials (for example, using commands to give Sharpness to an iron ingot), these enchantments are ignored when doing unit repair.
- Doing so costs 1 level per unit used plus any prior work penalty.

** Repairable items **
Anything not listed below does not have a unit repair item, and can be repaired only by consuming another instance of itself.

| Item                                                                                                                                                                                | Material                                                         |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| Wooden Sword Wooden Pickaxe Wooden Axe Wooden Shovel Wooden Hoe Shield                                                                                                              | Planks                                                           |
| Leather Cap Leather Tunic Leather Pants Leather Boots                                                                                                                               | Leather                                                          |
| Stone Sword Stone Pickaxe Stone Axe Stone Shovel Stone Hoe                                                                                                                          | Cobblestone Cobbled Deepslate Blackstone‌[Java Edition  only][1] |
| Iron Helmet Iron Chestplate Iron Leggings Iron Boots Chainmail Helmet Chainmail Chestplate Chainmail Leggings Chainmail Boots Iron Sword Iron Pickaxe Iron Axe Iron Shovel Iron Hoe | Iron Ingot                                                       |
| Golden Helmet Golden Chestplate Golden Leggings Golden Boots Golden Sword Golden Pickaxe Golden Axe Golden Shovel Golden Hoe                                                        | Gold Ingot                                                       |
| Diamond Helmet Diamond Chestplate Diamond Leggings Diamond Boots Diamond Sword Diamond Pickaxe Diamond Axe Diamond Shovel Diamond Hoe                                               | Diamond                                                          |
| Netherite Helmet Netherite Chestplate Netherite Leggings Netherite Boots Netherite Sword Netherite Pickaxe Netherite Axe Netherite Shovel Netherite Hoe                             | Netherite Ingot                                                  |
| Turtle Shell                                                                                                                                                                        | Scute                                                            |
| Elytra                                                                                                                                                                              | Phantom Membrane                                                 |
| Mace‌[upcoming: JE 1.21 & BE 1.21.0]                                                                                                                                                | Breeze Rod                                                       |

Anvils cannot be repaired by any iron item or block.

