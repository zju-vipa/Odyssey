# Item repair
Item repair is a feature that allows players to repair damaged items with durability (tools, armor and weapons) by combining them in the crafting grid or a grindstone.

## Contents
- 1 Usage
- 2 Formula for uses restored
- 3 Anvil repair
	- 3.1 Combination
	- 3.2 Unit repair
- 4 Video
- 5 History
- 6 Trivia
- 7 Gallery
	- 7.1 Screenshots
- 8 See also
- 9 References

## Usage
Two items of the same type and material can be placed anywhere on the crafting grid or grindstone, which results in a single repaired item. The durability of the repaired item equals the sum of the old items' durability plus a 'repair bonus' of 5% of the item's maximum uses, up to a limit of the maximum durability for that item. Repairing gives a slight benefit in conserving inventory space, as it combines two non-stackable objects into one.[1]

The repaired object is never enchanted even if both items were to have the exact same enchantments, with the exception of curse enchantments, which are transferred to the repaired item. Therefore, using a "junk" item in a repair may sometimes be useful for removing an unwanted enchantment from an item prior to enchanting it again. Tools made of different materials (for example, a wood and a stone pickaxe) cannot be combined.

## Formula for uses restored
The formula for determining how many uses a repaired item can have restored to it in the crafting box, is as follows:

min(Item A uses + Item B uses + floor(Max uses / 20), Max uses)

where "floor" means round down to the smaller integer, and "min(x,y)" means the smallest of x or y.

Example: Two stone axes have 10 and 45 uses. A newly crafted stone axe would have 61 uses.

10 + 45 +131/20= 55 + 6.55 = 61
Or, in terms of percentage (approximated):

7.6% + 34% + 5% =  46.6%
The greatest benefit is gained when the two items have a combined durability of at most approximately 95%, in any combination, such as 47.5% + 47.5%, 94% + 1%, 10% + 10% or any other values that total 95% or less. The order in which items are combined does not matter; one sequence of repairs gives exactly the same durability as any other.

In the example, repairing a stone tool restores a bonus of 6 durability, which is actually only 6/132 = 4.5%. The precise combined durability for efficient repairs is shown in the following table.

| Item              | Actual bonus (%) | Actual bonus (uses) | Combined durability (%) | Combined durability (uses) |
|-------------------|------------------|---------------------|-------------------------|----------------------------|
| Golden tools      | 3.0%             | 1                   | 97.0%                   | 31                         |
| Wooden tools      | 5.0%             | 3                   | 95.0%                   | 56                         |
| Stone tools       | 4.5%             | 6                   | 95.5%                   | 125                        |
| Iron tools        | 4.8%             | 12                  | 95.2%                   | 238                        |
| Diamond tools     | 5.0%             | 78                  | 95.0%                   | 1483                       |
| Netherite tools   | 5.0%             | 101                 | 95.0%                   | 1930                       |
| Carrot on a stick | 3.8%             | 1                   | 96.2%                   | 24                         |
| Flint and steel   | 4.6%             | 3                   | 95.4%                   | 61                         |
| Fishing rod       | 4.6%             | 3                   | 95.4%                   | 61                         |
| Shears            | 4.6%             | 11                  | 95.4%                   | 227                        |
| Bow               | 4.9%             | 19                  | 95.1%                   | 365                        |

A perfect repair is theoretically possible, but unlikely in practice. Combining items whose combined durability is more than 100% actually wastes more resources than simply using tools until they break.

The precise combined durability for efficient repairs for all types of armor is shown in the following table.

| Armor piece         | Actual bonus (%) | Actual bonus (uses) | Combined durability (%) | Combined durability (uses) |
|---------------------|------------------|---------------------|-------------------------|----------------------------|
| Leatherhelmet       | 3.6%             | 2                   | 96.4%                   | 53                         |
| Leatherboots        | 4.6%             | 3                   | 95.4%                   | 59                         |
| Leatherleggings     | 4.0%             | 3                   | 96.0%                   | 72                         |
| Leatherchestplate   | 4.9%             | 4                   | 95.1%                   | 77                         |
| Goldhelmet          | 3.9%             | 3                   | 96.1%                   | 74                         |
| Goldboots           | 4.4%             | 4                   | 95.6%                   | 87                         |
| Goldleggings        | 4.8%             | 5                   | 95.2%                   | 100                        |
| Goldchestplate      | 4.4%             | 5                   | 95.6%                   | 108                        |
| Ironhelmet          | 4.8%             | 8                   | 95.2%                   | 157                        |
| Ironboots           | 4.6%             | 9                   | 95.4%                   | 186                        |
| Ironleggings        | 4.9%             | 11                  | 95.1%                   | 214                        |
| Ironchestplate      | 5.0%             | 12                  | 95.0%                   | 229                        |
| Diamondhelmet       | 5.0%             | 18                  | 95.0%                   | 327                        |
| Diamondboots        | 4.9%             | 21                  | 95.1%                   | 408                        |
| Diamondleggings     | 4.8%             | 24                  | 95.2%                   | 471                        |
| Diamondchestplate   | 4.9%             | 26                  | 95.1%                   | 502                        |
| Netheritehelmet     | 4.9%             | 20                  | 95.1%                   | 387                        |
| Netheriteboots      | 5.0%             | 24                  | 95.0%                   | 457                        |
| Netheriteleggings   | 4.9%             | 27                  | 95.1%                   | 528                        |
| Netheritechestplate | 4.9%             | 29                  | 95.1%                   | 563                        |

