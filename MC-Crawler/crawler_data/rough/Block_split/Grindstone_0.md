# Grindstone
A grindstone is a block that repairs items and tools as well as removing enchantments from them, except for curses. It also serves as a weaponsmith's job site block.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
- 2 Usage
	- 2.1 Repairing and disenchanting
	- 2.2 Changing profession
	- 2.3 Piston interactivity
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 Achievements
- 6 History
- 7 Issues
- 8 Trivia
- 9 Gallery
	- 9.1 Screenshots
- 10 References

## Obtaining
### Breaking
Grindstones can be obtained using any pickaxe. If mined without a pickaxe, it drops nothing.

| Block     | Grindstone            |
|-----------|-----------------------|
| Hardness  | 2                     |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 10                    |
| Wooden    | 1.5                   |
| Stone     | 0.75                  |
| Iron      | 0.5                   |
| Diamond   | 0.4                   |
| Netherite | 0.35                  |
| Golden    | 0.25                  |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
A grindstone generated inside a weaponsmith shelter structure.
Grindstones naturally generate at village weaponsmiths and trail ruins.

### Crafting
| Ingredients                          | Crafting recipe | Description                                                                                                                                                                                            |
|--------------------------------------|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Stick+<br/>Stone Slab+<br/>AnyPlanks |                 | InBedrock Edition, grindstone recipes built with crimson, warped, or mangrove planks can use a slab of almost any of the stone types including sandstone, quartz, and bricks.[more information needed] |

## Usage
A grindstone can be oriented in different directions. In Java Edition it doesn't need a supporting block. In Bedrock Edition it breaks if unsupported.

### Repairing and disenchanting
Interface for the grindstone
When used, an interface is displayed with two input slots and one output slot.

It resets the repair cost for items.

When one enchanted item is placed in either input slot, a disenchanted copy of the item appears in the output slot. The output item has the same durability, if it is a piece of armor or a tool. If an enchanted book is placed in the input, a normal book appears in the output. Removing the item from the output slot deletes the input item and causes the grindstone to drop some experience. If the input item has a custom name, given by renaming it, the output item will adopt the name.

Placing two tools or pieces of armor (enchanted or not) of the same type in the input slots causes a non-enchanted item of the same type to appearn in the output slot. The output item has the same durability as what the player would get form using the item repair crafting recipe if the 2 input items were unenchanted. This means the output durability is the sum of the durabilities of the two input items, plus 5% of the maximum durability of the output item (rounded down), capped so it does not exceed the maximum durability of the output item. Both input items are deleted in this process of disenchanting them and repairing them. If either input item was enchanted, then removing the output item drops some experience. The output item has the same armor trim (if any) and name (if any) as the input item in the top slot.

The amount of experience dropped by the grindstone scales based on the modified enchantment levels of all the enchantments on both input items, and is somewhat random.[more information needed]

As with all non-enchanted items, the output item has no prior work penalty, even if it is cursed. Disenchanting an item in the grindstone cannot remove a curse, and cannot remove an item's custom name.

If the action is not applicable (e.g. only one non-enchanted item, or the two inputs are different items), the arrow displays a red cross like that of an anvil and no item appears in the output slot.

The following tables show the durability bonuses of various items:[more information needed]

| Tier         | Helmet | Chestplate | Leggings | Boots |
|--------------|--------|------------|----------|-------|
| Leather      | 2      | 4          | 3        | 3     |
| Gold         | 3      | 5          | 5        | 4     |
| Chainmail    | 8      | 12         | 11       | 9     |
| Iron         | 8      | 12         | 11       | 9     |
| Turtle Shell | 13     | –          | –        | –     |
| Diamond      | 18     | 26         | 24       | 21    |
| Netherite    | 20     | 29         | 27       | 24    |


| Wood      | 3   |
|-----------|-----|
| Gold      | 1   |
| Stone     | 6   |
| Iron      | 12  |
| Diamond   | 78  |
| Netherite | 101 |

| Bow                      | 19                             |
|--------------------------|--------------------------------|
| Crossbow                 | 23                             |
| Trident                  | 12                             |
| Shield                   | 16                             |
| Elytra                   | 21                             |
| Carrot on a stick        | 1                              |
| Warped fungus on a stick | 5                              |
| Fishing rod              | 3‌[JE  only]<br/>19‌[BE  only] |
| Shears                   | 11                             |
| Flint and steel          | 3                              |
| Brush                    | 3                              |


