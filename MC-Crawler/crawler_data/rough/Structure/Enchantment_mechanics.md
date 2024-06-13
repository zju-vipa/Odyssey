# Enchanting mechanics
This article is about the mechanics of enchanting.

## Contents
- 1 Basic mechanics
- 2 Bookshelf placement
	- 2.1 Bedrock Edition
	- 2.2 Java Edition
	- 2.3 Selecting an enchantment level
		- 2.3.1 Bedrock Edition
		- 2.3.2 Java Edition
- 3 How enchantments are chosen
	- 3.1 Step one – Applying modifiers to the enchantment level
		- 3.1.1 Enchantability
		- 3.1.2 Step one pseudocode
	- 3.2 Step two – Find possible enchantments
		- 3.2.1 Treasure
	- 3.3 Step three – Select a set of enchantments from the list
	- 3.4 Conflicting enchantments
- 4 Enchanting seed
	- 4.1 Deterministic initial enchantment
- 5 History
- 6 References
- 7 External links

## Basic mechanics
Whenever the player places an eligible item on the enchanting table, the enchantment levels available are randomly generated for each slot using the formula below. The enchantment level is dependent upon the number of nearby bookshelves (capped at 15) and which slot position it is in.

Base enchantment level available (base) = (randomInt(1,8) + floor(b/ 2) + randomInt(0,b)),
where b is the number of nearby bookshelves (maximum of 15) and randomInt(x,y) generates a uniformly distributed random integer between x and y, inclusive. This is then modified according to the slot position:

Top slot enchantment level = floor(max(base/ 3, 1))
Middle slot enchantment level = floor((base× 2) / 3 + 1)
Bottom slot enchantment level = floor(max(base,b× 2))
where max(x,y) returns the greater of two values x and y. 

| # of bookshelves           | 0 | 1 | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  | 10 | 11 | 12 | 13 | 14 | 15 |
|----------------------------|---|---|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| Min level (in top slot)    | 1 | 1 | 1  | 1  | 1  | 1  | 1  | 1  | 1  | 1  | 2  | 2  | 2  | 2  | 2  | 2  |
| Max level (in bottom slot) | 8 | 9 | 11 | 12 | 14 | 15 | 17 | 18 | 20 | 21 | 23 | 24 | 26 | 27 | 29 | 30 |

| # of bookshelves           | 0   | 1   | 2    | 3    | 4    | 5     | 6     | 7     | 8     | 9     | 10    | 11    | 12    | 13    | 14    | 15   |
|----------------------------|-----|-----|------|------|------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|------|
| Level range of top slot    | 1–2 | 1–3 | 1–3  | 1–4  | 1–4  | 1–5   | 1–5   | 1–6   | 1–6   | 1–7   | 2–7   | 2–8   | 2–8   | 2–9   | 2–9   | 2–10 |
| Level range of middle slot | 1–6 | 1–7 | 2–8  | 2–9  | 3–10 | 3–11  | 3–12  | 3–13  | 4–14  | 4–15  | 5–16  | 5–17  | 5–18  | 5–19  | 6–20  | 6–21 |
| Level range of bottom slot | 1–8 | 2–9 | 4–11 | 6–12 | 8–14 | 10–15 | 12–17 | 14–18 | 16–20 | 18–21 | 20–23 | 22–24 | 24–26 | 26–27 | 28–29 | 30   |

Note that a higher experience cost for a specific slot does not necessarily mean that the enchantments from that slot are better than the others with less cost.

In Creative mode, no levels of experience are necessary for enchantments.

## Bookshelf placement
Nearby bookshelves raise the available enchantment levels; without any bookshelves, the experience level requirement never exceeds 8. The maximum number of bookshelves effecting enchantment is 15.

In order to have an effect, a bookshelf must be placed exactly 2 blocks, laterally, off the enchanting table and be on the same level or one block height above the table. Additionally, the bookshelf must not be blocked. The meaning of "blocked" differs in both Java and Bedrock editions.

### Bedrock Edition
The 2-high space between the bookshelf and table must be air (even a torch, snow cover or carpet blocks the effect), where "between" is as shown in the following diagrams (the white spaces are air, and the  do not matter):

|  |  |  |
|--|--|--|
|  |  |  |
|  |  |  |

|  |  |  |
|--|--|--|
|  |  |  |
|  |  |  |

|  |  |  |
|--|--|--|
|  |  |  |

|  |  |  |
|--|--|--|
|  |  |  |

### Java Edition
The space between the bookshelf and table at the height of the bookshelf must be air or a replaceable block like snow or grass. For corner bookshelves, the space between is 1 block diagonal from the enchanting table; for all other bookshelves, the gap must be to the side of the enchanting table. This is illustrated in the following diagrams (the blank spaces are air, and the  do not matter):

|  |  |  |
|--|--|--|
|  |  |  |
|  |  |  |

|  |  |  |
|--|--|--|
|  |  |  |
|  |  |  |

|  |  |  |
|--|--|--|
|  |  |  |

|  |  |  |
|--|--|--|
|  |  |  |

The glyph particles, which fly from bookshelves, follow different rules and may appear even if the bookshelves are not enhancing the table.

There are many possible bookshelf arrangements that can reach the enchantment limit. A simple method is to surround the enchanting table with a 1-block high square of bookshelves with an empty space anywhere on the perimeter:

|  |  |  |  |  |
|--|--|--|--|--|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

Another alternative that is now available is to build a 'library corner' where each bookshelf is two blocks high, as in the plan below. This arrangement gives space for 16 shelves, which is one more than needed, so if the corner bookshelf column cannot be seen, removing one of the two bookshelves in that does not have any effect, either technically or visually.

|  |  |  |  |  |
|--|--|--|--|--|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

### Selecting an enchantment level
As enchantments offered depend on the enchantment level and the enchantment level depends on the number of active bookshelves, an easy way to change the enchantments offered is to disable bookshelves by placing torches between them and the enchanting table. That way one can still have the entire 'ring' of bookshelves around the table but get lower-level enchantments. Breaking the torches restores the effect of the bookshelves.

#### Bedrock Edition

With the layout shown here, enchantments with any number of bookshelves from 0 to 15 may be easily obtained:

|  |  |  |  | Active bookshelves |
|--|--|--|--|--------------------|
|  |  |  |  | 0                  |
|  |  |  |  | 1                  |
|  |  |  |  | 2                  |
|  |  |  |  | 3                  |
|  |  |  |  | 4                  |
|  |  |  |  | 5                  |
|  |  |  |  | 6                  |
|  |  |  |  | 7                  |
|  |  |  |  | 8                  |
|  |  |  |  | 9                  |
|  |  |  |  | 10                 |
|  |  |  |  | 11                 |
|  |  |  |  | 12                 |
|  |  |  |  | 13                 |
|  |  |  |  | 14                 |
|  |  |  |  | 15                 |

#### Java Edition

With the layout shown here, enchantments with any number of bookshelves from 0 to 15 may be easily obtained:

|  |  |  | Active bookshelves |
|--|--|--|--------------------|
|  |  |  | 0                  |
|  |  |  | 1                  |
|  |  |  | 2                  |
|  |  |  | 3                  |
|  |  |  | 4                  |
|  |  |  | 5                  |
|  |  |  | 6                  |
|  |  |  | 7                  |
|  |  |  | 8                  |
|  |  |  | 9                  |
|  |  |  | 10                 |
|  |  |  | 11                 |
|  |  |  | 12                 |
|  |  |  | 13                 |
|  |  |  | 14                 |
|  |  |  | 15                 |

## How enchantments are chosen
"Enchantment level" is the required experience level (the green number on the bottom-right).
"Enchantment power" is the strength of the particular enchantment. For example, "Sharpness IV" has a power of 4.
The enchantment algorithm uses a three-step process.

### 
The first thing that Minecraft does is apply two modifiers to the base enchantment level. Each modifier is restricted to a certain range, with numbers close to the middle of the range more common than those near the ends.

The first modifier is based on the item's "enchantability," which depends on the material and the type of the item (see the table below). Other enchantable items such as books, bows, crossbows, tridents, and fishing rods have an enchantability of 1 for this purpose. Minecraft picks a number between 0 and half the enchantability, then adds that number plus one to the enchantment level.  This random value follows a triangular distribution (like rolling a pair of dice and adding) so results close to a quarter of the enchantability are much more likely than results at the extremes.

The modified enchantment level is calculated with the following formula:

Modified enchantment level =B+R1+R2+ 1
Where:

- R1andR2are two individual randomly generated integers:
	- R1= randomInt(0, E / 4)
	- R2= randomInt(0, E / 4)
- Bis the base enchantment level.
- Eis the enchantability of the item.

Division is rounded down.

#### Enchantability
| Material  | Armor enchantability | Sword/Tool enchantability |
|-----------|----------------------|---------------------------|
| Wood      | N/A                  | 15                        |
| Leather   | 15                   | N/A                       |
| Stone     | N/A                  | 5                         |
| Chain     | 12                   | N/A                       |
| Iron      | 9                    | 14                        |
| Gold      | 25                   | 22                        |
| Diamond   | 10                   | 10                        |
| Turtle    | 9                    | N/A                       |
| Netherite | 15                   | 15                        |
| Other     | 1                    | 1                         |

Next, Minecraft picks a value between 0.85 and 1.15, again with a triangular distribution. The modified enchantment level is multiplied by this value (so it could increase or decrease by up to 15%) and then rounded to the nearest integer.

#### Step one pseudocode
// Returns a uniformly distributed random integer between 0 and n–1, inclusive
function randomInt(n);

// Returns a uniformly distributed random real (fractional) number between 0 (inclusive) and 1 (exclusive)
function randomFloat();

// Returns the real number n rounded to the nearest integer.
function round(n);


// Generate a random number between 1 and 1+(enchantability/2), with a triangular distribution
int rand_enchantability = 1 + randomInt(enchantability / 4 + 1) + randomInt(enchantability / 4 + 1);

// Choose the enchantment level
int k = chosen_enchantment_level + rand_enchantability;

// A random bonus, between .85 and 1.15
float rand_bonus_percent = 1 + (randomFloat() + randomFloat() - 1) * 0.15;

// Finally, we calculate the level
int final_level = round(k * rand_bonus_percent);
if ( final_level < 1 ) final_level = 1

The source is Minecraft 1.8 source code.

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

### Conflicting enchantments
Some enchantments conflict with other enchantments and thus both can't be enchanted into the same item, effectively taking down the possibility for one to get an overpowered weapon.

The rules for enchantment conflicts are:

- Every enchantment conflicts with itself. (The player can't get a tool with two copies of the Efficiency enchantment)
- All melee damage enchantments (Sharpness,Smite, andBane of Arthropods) conflict with each other. This does not includeImpaling.
- All protection enchantments (Protection,Blast Protection,Fire Protection,Projectile Protection) conflict with each other.
- Silk Touchconflicts withFortune,Looting, andLuck of the Sea, and vice versa. However, Fortune, Looting and Luck of the Sea, does not conflict with each other.
- Depth StriderandFrost Walkerconflict with each other.
- MendingandInfinityconflict with each other.
- Riptideconflicts withLoyaltyandChanneling, but Loyalty does not conflict with Channeling.
- MultishotandPiercingconflict with each other.

Conflicting enchantments may appear on an item with specially-crafted /give commands. The behavior of such items should not be relied upon, but in general:

- An item with multiple copies of the same enchantment uses the level of the first copy of that enchantment in the list.
- For armor with conflicting protection enchantments, all enchantments take effect individually.
- For weapons with conflicting damage enchantments, all enchantments take effect individually.
- For tools with both Silk Touch and Fortune, Silk Touch takes priority over Fortune on blocks affected by both enchantments. Fortune still applies to blocks such as crops that are not affected by Silk Touch.
- For bows with both Mending and Infinity, both enchantments work individually.
- For tridents with both Loyalty and Riptide, Riptide still functions normally but the trident can no longer be thrown by the player. However, tridents can still be thrown using dispensers.‌[Bedrock Edition  only]
- For crossbows with both Multishot and Piercing, both enchantments work individually.

A chart showing all possible enchantments on diamond tools.[needs updating]
## Enchanting seed
The enchantments that the enchanting table offers to a player do not usually change until the player enchants an item.
After each applied enchant, the player gets offered different enchantments for any type of enchantable item.

This is controlled by the enchanting seed XpSeed in the player data.

### Deterministic initial enchantment
This enchantment seed is initialized to 0 on world creation, and whenever the last enchantment seed was 0 on loading into a world it is re-rolled.[1]
Hence, when a new world is played until the player performs their first enchant without closing and re-joining the world in between, the offered enchantments are always the same.
They still depend on the enchanted item and the enchantment level.

These deterministic enchantments with the XpSeed equal to 0, colloquially know as first enchants, can be used to guarantee certain enchantments, e.g. a diamond sword enchanted with 3 lapis lazuli and 15 bookshelves always gets Unbreaking 3 and Looting 2.

Due to the fact that enchanting an item changes the enchanting seed, only one such first enchant can be chosen per world.

