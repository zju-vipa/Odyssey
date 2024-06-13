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

