# Ominous Vault
An ominous vault is a variant of the vault found in trial chambers. It dispenses valuable loot when unlocked using an ominous trial key.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
- 2 Usage
	- 2.1 Loot
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
- 5 Advancements
- 6 History
- 7 Issues
- 8 Gallery
	- 8.1 Renders
	- 8.2 Screenshots
- 9 References

## Obtaining
Ominous vaults cannot be obtained as items in Survival, even with Silk Touch, and cannot be moved with a piston.

It cannot be obtained via the Creative inventory or by using pick block, because it is technically a block state of the vault, not a separate block. It can only be obtained by using commands, such as /give @s minecraft:vault[minecraft:block_state={ominous:"true"}]‌[Java Edition  only] or /setblock x y z minecraft:vault[ominous=true]‌[Java Edition  only] / /setblock x y z vault ["ominous"=true].‌[Bedrock Edition  only]

### Breaking
An ominous vault can be broken but it does not drop itself as an item and takes a long time to break.

Due to their high blast resistance, ominous vaults are immune to explosions, but can still be destroyed by the wither's block-breaking attack and blue wither skulls.

| Block    | Ominous Vault       |
|----------|---------------------|
| Hardness | 50                  |
|          | Breakingtime (secs) |
| Default  | 250                 |

### Natural generation
Ominous vaults can be found throughout trial chambers. Unlike ominous trial spawners, ominous vaults don't replace normal vaults when a player with the Trial Omen effect is nearby.

An ominous vault can be distinguished from a normal vault by its texture and location in harder to find places. An ominous vault is always surrounded by red candles and red glazed terracotta.

## Usage
A player can unlock an ominous vault using an ominous trial key.

Like the normal vault, the ominous vault has 3 loot tables. These loot tables correspond to the columns below.

- Common: corresponds with the 2nd and 5th columns.
- Rare: corresponds with the 3rd and 6th columns.
- Unique: corresponds with the 4th and 7th columns.

### Loot
The ominous vault ejects 3 to 6 stacks of loot, like the vault, but the ominous vault's loot is significantly better.

‌In Java Edition 1.21‌[upcoming][more information needed], the ominous vault ejects a combination of loot from three different loot tables. The following information describes the loot ejected for a single player when a single ominous trial key is used.

- Common loot
	- A set of common loot is 3 sets of the loot in the 2nd and 5th columns of the loot table below.
	- Every ominous vault has at least one set of common loot.
	- An ominous vault that does not give rare loot gives a 4th set of the loot in the 3rd and 6th columns below.
- Rare loot
	- Every ominous vault has an 80% chance to include a set of rare loot.
	- The loot listed in the 2nd and 5th columns below corresponds with the 80% chance of one set of rare loot, plus the 20% chance of the one set of common loot that can be used in its place.
- Unique loot
	- Every ominous vault has a 75% chance to also include one set of unique loot.
	- This loot, and the 25% chance for each ominous vault to not have this loot, corresponds with the 4th and 7th columns below.

In Java Edition 1.21, each trial chambers ominous vault contains  items drawn from 3 pools,  with the following distribution: 

| Item                              | Stack Size  [A] |      |    | Weight   [B]     |                |                | Chance   [C] | Avg.per container   [D] | Avg. # containersto loot   [E] |
|-----------------------------------|-----------------|------|----|------------------|----------------|----------------|--------------|-------------------------|--------------------------------|
|                                   | 1×              | 1–3× | 1× | 1×               | 1–3×           | 1×             |              |                         |                                |
| Emerald                           | 4–10            | 4–10 | —  | $\frac{5}{132}$  | $\frac{5}{15}$ | —              | 54.9%        | 4.932                   | 1.8                            |
| Wind Charge                       | 8–12            | 8–12 | —  | $\frac{4}{132}$  | $\frac{4}{15}$ | —              | 46.2%        | 5.636                   | 2.2                            |
| Arrow of Slowness IV              | 4–12            | 4–12 | —  | $\frac{3}{132}$  | $\frac{3}{15}$ | —              | 36.4%        | 3.382                   | 2.7                            |
| Diamond                           | 2–3             | 2–3  | —  | $\frac{2}{132}$  | $\frac{2}{15}$ | —              | 25.5%        | 0.705                   | 3.9                            |
| Nothing[F]                        | —               | —    | 1  | —                | —              | $\frac{3}{12}$ | 25.0%        | 0.250                   | 4.0                            |
| Flow Armor Trim Smithing Template | —               | —    | 1  | —                | —              | $\frac{3}{12}$ | 25.0%        | 0.250                   | 4.0                            |
| Enchanted Golden Apple            | —               | —    | 1  | —                | —              | $\frac{3}{12}$ | 25.0%        | 0.250                   | 4.0                            |
| Block of Emerald                  | 1               | —    | —  | $\frac{24}{132}$ | —              | —              | 18.2%        | 0.182                   | 5.5                            |
| Flow Banner Pattern               | —               | —    | 1  | —                | —              | $\frac{2}{12}$ | 16.7%        | 0.167                   | 6.0                            |
| Ominous Bottle III - V[G]         | 1               | 1    | —  | $\frac{1}{132}$  | $\frac{1}{15}$ | —              | 13.4%        | 0.141                   | 7.5                            |
| Enchanted Crossbow[H]             | 1               | —    | —  | $\frac{16}{132}$ | —              | —              | 12.1%        | 0.121                   | 8.2                            |
| Block of Iron                     | 1               | —    | —  | $\frac{16}{132}$ | —              | —              | 12.1%        | 0.121                   | 8.2                            |
| Golden Apple                      | 1               | —    | —  | $\frac{16}{132}$ | —              | —              | 12.1%        | 0.121                   | 8.2                            |
| Enchanted Diamond Axe[I]          | 1               | —    | —  | $\frac{12}{132}$ | —              | —              | 9.1%         | 0.091                   | 11.0                           |
| Enchanted Diamond Chestplate[I]   | 1               | —    | —  | $\frac{12}{132}$ | —              | —              | 9.1%         | 0.091                   | 11.0                           |
| Heavy Core                        | —               | —    | 1  | —                | —              | $\frac{1}{12}$ | 8.3%         | 0.083                   | 12.0                           |
| Enchanted Book[J]                 | 1               | —    | —  | $\frac{8}{132}$  | —              | —              | 6.1%         | 0.061                   | 16.5                           |
| Enchanted Book[K]                 | 1               | —    | —  | $\frac{8}{132}$  | —              | —              | 6.1%         | 0.061                   | 16.5                           |
| Enchanted Book[L]                 | 1               | —    | —  | $\frac{4}{132}$  | —              | —              | 3.0%         | 0.030                   | 33.0                           |
| Block of Diamond                  | 1               | —    | —  | $\frac{1}{132}$  | —              | —              | 0.8%         | 0.008                   | 132.0                          |



↑ The size of stacks (or for unstackable items, number) of this item on any given roll.

↑ The weight of this item relative to other items in the pool.

↑ The odds of finding any of this item in a single chest.

↑ The number of items expected per chest, averaged over a large number of chests.

↑ The average number of chests the player should expect to search to find any of this item.

↑ 'Nothing' does not refer to the chance of an empty chest.  Instead, it refers to the chance that the random loot generator does not add any loot on a single roll.

↑ Ominous bottle level between III and V

↑ Enchantment probabilities are the same as a level-5 to level-20 enchantment would be on an enchantment table that was able to apply treasure enchantments (except Soul Speed, and Swift Sneak), and where the chance of multiple enchantments is not reduced.

↑ a b Enchantment probabilities are the same as a level-5 to level-15 enchantment would be on an enchantment table that was able to apply treasure enchantments (except Soul Speed, and Swift Sneak), and where the chance of multiple enchantments is not reduced.

↑ Enchanted with a random level of Breach, or Density.

↑ Enchanted with a random level of Sharpness, Bane of Arthropods, Efficiency, Fortune, Silk Touch, or Feather Falling.

↑ Enchanted with a random level of Wind Charge.



