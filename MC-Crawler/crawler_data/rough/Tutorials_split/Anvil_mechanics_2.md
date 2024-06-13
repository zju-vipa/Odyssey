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

