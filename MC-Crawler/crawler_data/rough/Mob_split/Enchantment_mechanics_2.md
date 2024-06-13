### 
A sword with several enchantments.
Now, based on the modified level, Minecraft makes a list of all enchantment types that can be applied to the target item along with the power that each enchantment has.

The power of each enchantment type is determined by the level and the values in the enchantments levels table. For each power value of an enchantment type, there is a minimum and maximum modified level that can produce the enchantment at that power. If the modified enchantment level (calculated at the first step) is within the range of an enchantment's possible power values, then the enchantment is assigned the modified enchantment level as power. If the modified level is within two overlapping ranges for the same enchantment type, the higher power value is used.

#### Treasure
Some enchantments are "treasure enchantments" (shown in the table below), meaning they can never be created by an enchanting table, and can be discovered only in certain situations: when generating chest loot (equipment and books), when fishing, when generating enchanted book trades, when bartering, and when an enchanted book is dropped by a raiding illager.‌[Bedrock Edition  only]


### 
Now that it has a list of the possible enchantments for the item, Minecraft must pick some of them to apply. Each enchantment has a statistical "weight". Enchantments with higher weights have a higher chance of being selected.

Minecraft uses the following weighted random selection algorithm:

1. Calculate the total weight of all enchantments in the list (T). The total of every enchantment is 137.
2. Pick a random integer from 0 toT– 1 as a numberw.
3. Iterate through each enchantment in the list, subtracting its weight fromw. Ifwis now negative, select the current enchantment.

This algorithm produces the same results as listing each enchantment the number of times given by its weight, then choosing a random entry from the combined list.

So, for each enchantment in the list, the probability of it being selected is:

P=w/T

Where:

- wis the enchantment's weight.
- Tis the total weight of all enchantments in the list.

| Type of enchantment                           | Enchantment           | Weight | Obtainable from an enchanting table |
|-----------------------------------------------|-----------------------|--------|-------------------------------------|
| Armor                                         | Protection            | 10     | Yes                                 |
|                                               | Feather Falling       | 5      | Yes                                 |
|                                               | Fire Protection       | 5      | Yes                                 |
|                                               | Projectile Protection | 5      | Yes                                 |
|                                               | Aqua Affinity         | 2      | Yes                                 |
|                                               | Blast Protection      | 2      | Yes                                 |
|                                               | Respiration           | 2      | Yes                                 |
|                                               | Depth Strider         | 2      | Yes                                 |
|                                               | Frost Walker          | 2      | No                                  |
|                                               | Thorns                | 1      | Yes                                 |
|                                               | Swift Sneak           | 1      | No                                  |
|                                               | Curse of Binding      | 1      | No                                  |
|                                               | Soul Speed            | 1      | No                                  |
| Sword                                         | Sharpness             | 10     | Yes                                 |
|                                               | Bane of Arthropods    | 5      | Yes                                 |
|                                               | Knockback             | 5      | Yes                                 |
|                                               | Smite                 | 5      | Yes                                 |
|                                               | Fire Aspect           | 2      | Yes                                 |
|                                               | Looting               | 2      | Yes                                 |
|                                               | Sweeping Edge         | 2      | Yes                                 |
| Pickaxe<br/>Shovel<br/>Axe<br/>Hoe<br/>Shears | Efficiency            | 10     | Yes                                 |
|                                               | Fortune               | 2      | Yes                                 |
|                                               | Silk Touch            | 1      | Yes                                 |
| Bow                                           | Power                 | 10     | Yes                                 |
|                                               | Flame                 | 2      | Yes                                 |
|                                               | Punch                 | 2      | Yes                                 |
|                                               | Infinity              | 1      | Yes                                 |
| Fishing rod                                   | Luck of the Sea       | 2      | Yes                                 |
|                                               | Lure                  | 2      | Yes                                 |
| Trident                                       | Loyalty               | 5      | Yes                                 |
|                                               | Impaling              | 2      | Yes                                 |
|                                               | Riptide               | 2      | Yes                                 |
|                                               | Channeling            | 1      | Yes                                 |
| Crossbow                                      | Piercing              | 10     | Yes                                 |
|                                               | Quick Charge          | 5      | Yes                                 |
|                                               | Multishot             | 2      | Yes                                 |
| All applicable                                | Unbreaking            | 5      | Yes                                 |
|                                               | Mending               | 2      | No                                  |
|                                               | Curse of Vanishing    | 1      | No                                  |

The player always gets at least one enchantment on an item, and there is a chance of receiving more. Additional enchantments are chosen by this algorithm:

1. With a(modifiedlevel+1)/50probability, pick an extra enchantment. Otherwise, stop.
2. Remove from the list of possible enchantments anything that conflicts with previously-chosen enchantments.
3. Pick one enchantment from the remaining possible enchantments (based on the weights, as before) and apply it to the item.
4. Divide the modified level in half, rounded down (this does not affect the possible enchantments themselves, because they were all pre-calculated in Step Two).
5. Repeat from the beginning.

When enchanting books using an enchanting table, if multiple enchantments were generated, then one selected at random is removed from the final list. This does not apply to other sources of enchanted books that use enchantment mechanics, such as fishing or chests in generated structures.

