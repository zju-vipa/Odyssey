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

## Combining items
The anvil can be used to combine two items of the same type and material, or an item with an enchanted book. This applies only to items with durability: weapons, shields, tools, and armor, as well as enchanted books. The first (left) item is the target item, the second (right) item is the sacrifice item. The sacrifice item is destroyed upon combination of the two items. Combining two similar items does either or both of two things; each of which cost levels, though part of the cost is shared if they're both done at once:

- If thetargetitem is damaged it is repaired, adding thedurabilityof thesacrificeitem plus a bonus of 12% of the maximum durability. This repairs up to the item's maximum durability. The cost for this repair is 2 levels.
- If thesacrificeitem hasenchantments, it also tries to combine thesacrificeitem's enchantments onto thetargetitem. Regardless of whether any enchantments on thetargetitem are actually changed, the cost is based on the total enchantments on thetargetitem and thesacrificeitem. For each enchantment on thesacrificeitem:
	- If thetargetitem has the enchantment:
		- and the level of the enchantment on thesacrificeitem isgreater, the enchantment level on thetargetitem is raised to match it.
		- and the level of the enchantment on thesacrificeitem isequalAND the enchantment is not already at the maximum level, the enchantment on thetargetitem gains one level.
		- and the level of the enchantment on thesacrificeitem isless, the enchantment level on thetargetitem is unaffected.
	- If the target doesnothave the enchantment, it gains all levels of that enchantment,unlessit already has an incompatible enchantment, resulting in the anvil refusing to combine the items and a red "X" displaying on top of the arrow in the anvil GUI. Enchantments are incompatible if both are in one of the following groups:
		- Sword:Sharpness,Smite, andBane of Arthropods
		- Tool:FortuneandSilk Touch(as of Java version 1.12.2 one can combine these; thesacrificeitem's enchantment is lost)
		- Armor:Protection,Fire Protection,Blast Protection,Projectile Protection
		- Boots:Depth StriderandFrost Walker
		- Bow:InfinityandMending
		- Crossbow:MultishotandPiercing
		- Trident:LoyaltyandRiptideorChannelingandRiptide
		- Books: Silk Touch andLootingor Silk Touch andLuck of the Sea[2](and all of the above).

The total cost for combining two similar items is the sum of:

- Prior Work penaltiesofbothtarget and sacrifice.
- Ifrenaming, the renaming cost of 1 level.
- If the target item is not at full durability, the repair cost of 2 levels.
- If the sacrifice hasenchantments, theenchantment cost.

If the sacrifice is a book, there is no repair, but the anvil tries to combine the book's enchantments onto the target. The item can also be renamed at the same time. The enchantment cost is generally less than for combining two similar items.

If the target item is at full durability and the sacrifice does not have any enchantments, the anvil also refuses to combine the items, unless if renaming the item to a valid name.

### Costs for combining enchantments
(This is just the enchanting cost. The total cost outline is in Combining items.)

- For each enchantment on the sacrifice:
	- Ignore any enchantment that cannot be applied to the target (e.g. Protection on a sword).
	- Add one level for every incompatible enchantment on the target (inJava Edition).
	- If the enchantment is compatible with the existing enchantments on the target:
		- ForJava Edition, add the final level of the enchantment on the resulting item multiplied by the multiplier from the table below.
		- ForBedrock Edition, add the difference between the final level and the initial level on the target item multiplied by the multiplier from the table below.

| Enchantment cost multipliers |                               |           |             |                                                 |                                                 |
|------------------------------|-------------------------------|-----------|-------------|-------------------------------------------------|-------------------------------------------------|
| ID[note 1]                   | Enchantment                   | Max level | Applies to  | Multiplier from item                            | Multiplier from book                            |
| 0                            | Protection[note 2]            | IV        |             | 1                                               | 1                                               |
| 1                            | Fire Protection[note 2]       | IV        |             | 2                                               | 1                                               |
| 2                            | Feather Falling               | IV        |             | 2                                               | 1                                               |
| 3                            | Blast Protection[note 2]      | IV        |             | 4                                               | 2                                               |
| 4                            | Projectile Protection[note 2] | IV        |             | 2                                               | 1                                               |
| 5                            | Thorns                        | III       |             | 8                                               | 4                                               |
| 6                            | Respiration                   | III       |             | 4                                               | 2                                               |
| 7                            | Depth Strider[note 3]         | III       |             | 4                                               | 2                                               |
| 8                            | Aqua Affinity                 | I         |             | 4                                               | 2                                               |
| 9                            | Sharpness[note 4]             | V         |             | 1                                               | 1                                               |
| 10                           | Smite[note 4]                 | V         |             | 2                                               | 1                                               |
| 11                           | Bane of Arthropods[note 4]    | V         |             | 2                                               | 1                                               |
| 12                           | Knockback                     | II        |             | 2                                               | 1                                               |
| 13                           | Fire Aspect                   | II        |             | 4                                               | 2                                               |
| 14                           | Looting                       | III       |             | 4                                               | 2                                               |
| 15                           | Efficiency                    | V         |             | 1                                               | 1                                               |
| 16                           | Silk Touch[note 5]            | I         | ‌[BE  only] | 8                                               | 4                                               |
| 17                           | Unbreaking                    | III       |             | 2                                               | 1                                               |
| 18                           | Fortune[note 5]               | III       |             | 4                                               | 2                                               |
| 19                           | Power                         | V         |             | 1                                               | 1                                               |
| 20                           | Punch                         | II        |             | 4                                               | 2                                               |
| 21                           | Flame                         | I         |             | 4                                               | 2                                               |
| 22                           | Infinity[note 6]              | I         |             | 8                                               | 4                                               |
| 23                           | Luck of the Sea               | III       |             | 4                                               | 2                                               |
| 24                           | Lure                          | III       |             | 4                                               | 2                                               |
| 25                           | Frost Walker[note 3]          | II        |             | 4                                               | 2                                               |
| 26                           | Mending[note 6]               | I         |             | 4                                               | 2                                               |
| 27                           | Curse of Binding              | I         |             | 8                                               | 4                                               |
| 28                           | Curse of Vanishing            | I         | ‌[BE  only] | 8                                               | 4                                               |
| 29                           | Impaling                      | V         |             | 4‌[Java Edition  only]2‌[Bedrock Edition  only] | 2‌[Java Edition  only]1‌[Bedrock Edition  only] |
| 30                           | Riptide[note 7]               | III       |             | 4                                               | 2                                               |
| 31                           | Loyalty[note 7]               | III       |             | 1                                               | 1                                               |
| 32                           | Channeling[note 7]            | I         |             | 8                                               | 4                                               |
| 33                           | Multishot[note 8]             | I         |             | 4                                               | 2                                               |
| 34                           | Piercing[note 8]              | IV        |             | 1                                               | 1                                               |
| 35                           | Quick Charge                  | III       |             | 2                                               | 1                                               |
| 36                           | Soul Speed                    | III       |             | 8                                               | 4                                               |
| 37                           | Swift Sneak                   | III       |             | 8                                               | 4                                               |
| NA[note 9]                   | Sweeping Edge                 | III       |             | 4                                               | 2                                               |

** Examples **
- Dealing with equal enchantments:
	- In the first slot, the target is a sword withSharpnessIII,KnockbackII andLootingIII.
	- In the second slot, the sacrifice is a sword with Sharpness III and Looting III.
	- For the Sharpness III enchantment on the sacrifice: Since the target has an equal level, add one to the target's Sharpness level giving Sharpness IV. In Java, Add 4 (multiplier 1 times 4 levels) and in Bedrock, add 1 (multiplier 1 times the increase in levels 1) to the level cost for Sharpness IV.
	- For the Looting III enchantment on the sacrifice: Since the maximum level for Looting is III, the target remains at Looting III. In Java 12 (multiplier 4 times 3 levels) is still added to the level cost while in Bedrock, 0 is added since the level did not change.
	- Thus, the enchanting cost is 16 in Java and 1 in Bedrock. The total cost for the work includes any prior work penalties, repair costs, and rename costs.
	- If combined in the other order (the sword having three enchantments as the sacrifice), there would also be a cost of 4 (level 2 times multiplier 2) for the Knockback II enchantment for both Java and Bedrock (since the target has zero levels in Knockback), giving a total enchantment cost of 20 levels in Java and 5 levels in Bedrock.
- Dealing with unequal enchantments:
	- In the first slot, the target is a sword with Sharpness III, Knockback II, and Looting I.
	- In the second slot, the sacrifice is a sword with Sharpness I and Looting III.
	- For the Sharpness I enchantment on the sacrifice: Since the target has a higher level, the target keeps Sharpness III. But in Java, 3 (multiplier 1 times 3 levels) is still added to the level cost. In Bedrock, since the level on the target is unchanged, the cost added is 0.
	- For the Looting III enchantment on the sacrifice: Since the target has a lower level, it is upgraded to Looting III. In Java, add 12 (multiplier 4 times 3 levels) to the level cost. In Bedrock, add 8 (multiplier 4 times the increase in levels 2)
	- Thus, the enchanting cost is 15 in Java and 8 in Bedrock. The total cost for the work includes any prior work penalties, repair costs, and rename costs.
	- If combined in the other order (the sword having three enchantments as the sacrifice), there would also be a cost of 4 (multiplier 2 times 2 levels) for adding the Knockback II enchantment, giving a total enchantment cost of 19 levels in Java. In Bedrock, the looting level would be unchanged, the sharpness cost would be 2 (multiplier 1 times the increase in levels 2) plus the Knockback cost gives a total enchantment cost of 6 levels.
- Dealing with conflicting enchantments:
	- In the first slot, the target is a sword with Sharpness II and Looting II.
	- In the second slot, the sacrifice is a sword withSmiteV and Looting II.
	- For the Smite V enchantment on the sacrifice: Since Smite is incompatible with Sharpness, add 1 level in Java, nothing for Bedrock. The target keeps Sharpness II.
	- For the Looting II enchantment on the sacrifice: Since the target has an equal level, add one to the target's Looting level giving Looting III. In Java, add 12 (multiplier 4 times 3 levels) to the level cost for Looting III. In Bedrock, add 4 (multiplier 4 times the increase in levels 1) to the level cost for Looting.
	- Thus, the enchanting cost is 13 in Java and 4 for Bedrock. The total cost for the work includes any prior work penalties, repair costs, and rename costs.
	- If combined in the other order (the Sharpness sword as the sacrifice), the cost would again be 13 in Java and 4 in Bedrock with the result having Smite V and Looting III.
- Using books:
	- In the first slot, the target is a sword with Looting II.
	- In the second slot, the sacrifice is a book withProtectionIII, Sharpness I, and Looting II.
	- For the Protection III enchantment on the sacrifice: Since Protection is incompatible with swords, ignore it.
	- For the Sharpness I enchantment on the sacrifice: Since the target has no Sharpness, it gets Sharpness I. Add 1 level (multiplier 1 times 1 level) for Sharpness I.
	- For the Looting II enchantment on the sacrifice: Since the target has an equal level, add one to the target's Looting level giving Looting III. In Java, add 6 (multiplier 2 times 3 levels) to the level cost for Looting III. In Bedrock, add 2 (multiplier 2 times the increase in levels 1) to the level cost for Looting.
	- Thus, the enchanting cost is 7 in Java and 3 in Bedrock. The total cost for the work includes any prior work penalties and rename costs.

#### Planning the enchanting order
There are two important things to notice about the anvil mechanics when planning the order of multiple enchantments to the same item:

- When combining two items with prior work penalties, while the penalties for both items apply to the cost, only the higher of the penalties of the two items is considered when determining the penalty of the resulting item. For example, when combining two items with 2 workings each, the resulting item has only 3 workings with the fourth consumed by the penalty.
- The choice of which item to use as the sacrifice matters. For example having a Soul Speed III book in the first slot and a Mending book in the second slot has a cost of 2 levels, but reversing the order of the books results in a cost of 12, even though the resulting book is the same in the two cases.

Minimal prior work penalty enchantment order.
Prior work penalties are minimized by combining two items with equal penalties if possible. For example, it is possible to have 7 different enchantments on a single pair of boots. Starting with an unenchanted pair of boots and the 7 enchantments on individual books, the limit on the cost permitted by the anvil is exceeded if trying to combine the books one at a time with the boots. However, it is possible to avoid this by properly pairing up the items. First combine the boots with one of the books, plus the remaining 6 books in 3 pairs. Then combine the boots with one of the books and the other two books that have 2 enchantments each. Finally combine the boots with the book that has 4 enchantments. This results in a pair of boots with 3 workings on it, although in practice 7 workings have taken place.

It is also possible to minimize the cost of combining by carefully pairing up the items for combination. The enchantment with the highest cost should be in the sacrifice slot the least amount of times. For example, the 7 boots enchantments can be combined using the pairing method in the following order:

- Soul Speed III (12), Thorns III (12), Feather Falling IV (4), Depth Strider III (6), Protection IV (4), Unbreaking III (3), Mending (2)
- Combining the items pairwise (with the boots in the first slot) the cost is 12+4+4+2=22.
- The resulting items are: Boots (Soul Speed III), Thorns III+Feather Falling IV (16), Depth Strider III+Protection IV (10), Unbreaking III+Mending (5).
- The cost of the second round of combination is 16+5=21, plus 4 for the penalties, totalling 25.
- The resulting items are: Boots (Soul Speed III+Thorns III+Feather Falling IV), Depth Strider III+Protection IV+Unbreaking III+Mending (15).
- The cost of the last step is 15 plus the two penalties of 3 each, totalling 21.
- The overall cost is 22+25+21=68 levels.

Minimal XP cost enchantment order.
However, at times it's better to avoid a pairing so as to avoid paying the enchantment cost multiple times. For example, in the above we pay the costs of Protection IV, Feather Falling IV, and Unbreaking III twice, and Mending three times. If we combine the items this way instead, we spend an extra 4 levels on prior work penalties but pay for Protection IV only once and Mending only twice, saving 6 levels, for a net savings of 2 levels:

- Soul Speed III (12), Thorns III (12), Mending (2), Depth Strider III (6), Feather Falling IV (4), Protection IV (4), Unbreaking III (3)
- Combining the items pairwise (with the boots in the first slot) the cost is 12+2+4+3=21.
- The resulting items are: Boots (Soul Speed III), Thorns III+Mending (14), Depth Strider III+Feather Falling IV (10), Protection IV+Unbreaking III (7).
- If we then combine the remaining books onto the boots in order, we pay
	- For the Thorns III+Mending book: 14, plus 2 for the penalties, totalling 16.
	- For the Depth Strider III+Feather Falling IV book: 10, plus 4 for the penalties, totalling 14.
	- For the Protection IV+Unbreaking III book: 7, plus 8 for the penalties, totalling 15.
- The overall cost is 21+16+14+15=66 levels.

#### Enchantment equation
The equation to calculate an enchantment is as follows:

Experience cost = [Value of sacrificed (right placed) item] + [Work Penalty of target (left placed) item] + [Work Penalty of sacrificed (right placed) item] + [Renaming Cost] + [Refilling Durability] + [Incompatible Enchantments (Java Edition)]

The equation to calculate the new value of an item to be enchanted:

New value = [Value of target (left placed) item] + [Value of sacrificed (right placed) item]. 

Using the 7 enchantment pairing method shown, and looking at just the first enchantment (Diamond Boots + Soul Speed III) as an example: 

- Experience Cost = [Value of Sacrificed item - Soul Speed III (12)] + [Work Penalty of Diamond Boots (0)] + [Work Penalty of Soul Speed III (0)] = 12 Levels.
- New Value of resulting item = [Value of Diamond Boots (0)] + [Value of Soul Speed III (12)] = 12 Value.

Going to the next level of enchanting with Diamond Boots (Soul Speed III) and Thorns III + Feather Falling IV book: 

- Experience Cost = [Value of Sacrificed item - Thorns III + Feather Falling IV (16)] + [Work Penalty of Diamond Boots (Soul Speed III) (1)] + [Work Penalty of Thorns III + Feather Falling IV book (1)] = 18 Levels.
- New Value of resulting item = [Value of Diamond Boots (Soul Speed III) (12)] + [Value of Thorns III + Feather Falling IV book (16)] = 28 Value.
- Remember that the Work Penalty for each item here is a value of 1 because each has been used only once on the anvil previously.

## Notes
1. ↑Numeral IDs are Bedrock Edition only
2. ↑ a b c dThe different kinds of Protection are not compatible
3. ↑ a bDepth Strider and Frost Walker are not compatible
4. ↑ a b cSharpness, Smite, and Bane of Arthropods are not compatible
5. ↑ a bSilk Touch and Fortune are not compatible
6. ↑ a bInfinity and Mending are not compatible
7. ↑ a b cRiptide is not compatible with Loyalty or Channeling, although Loyalty and Channeling are compatible
8. ↑ a bMultishot and Piercing are not compatible
9. ↑Sweeping Edge has no numeral ID since it is not in Bedrock Edition

