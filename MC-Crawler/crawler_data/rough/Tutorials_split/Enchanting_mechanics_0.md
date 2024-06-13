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

