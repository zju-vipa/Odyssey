# Vault
A vault is a block found in trial chambers. It dispenses loot when unlocked using a trial key. Each vault can be looted by an unlimited number of players, but each player can unlock a specific vault only once.[1]

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
- 2 Usage
	- 2.1 Activation
	- 2.2 Unlocking
	- 2.3 Loot
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
	- 4.3 Block data
- 5 Advancements
- 6 Video
- 7 History
- 8 Issues
- 9 Trivia
- 10 Gallery
	- 10.1 Renders
		- 10.1.1 Before 24w13a
		- 10.1.2 Before 24w11a/1.20.80.22
		- 10.1.3 Before 24w09a/1.20.80.20
		- 10.1.4 Before 24w06a/1.20.70.22
	- 10.2 Screenshots
	- 10.3 Development images
- 11 References

## Obtaining
Vaults cannot be obtained in Survival, even with Silk Touch, and cannot be moved with a piston.

### Breaking
A vault can be broken but it does not drop itself as an item and takes an extended amount of time to break. It can be obtained only via the Creative inventory or the /give command.

Due to their high blast resistance, vaults are immune to explosions, but can still be destroyed by the wither's block-breaking attack and blue wither skulls.

| Block    | Vault               |
|----------|---------------------|
| Hardness | 50                  |
|          | Breakingtime (secs) |
| Default  | 250                 |

### Natural generation
In trial chambers, vaults can generate naturally in all rooms that also contain trial spawners, as well as the entrance room. They are found generated on small pedestals made of waxed cut copper blocks and cut copper slabs.

## Usage
### Activation
When a player is within 4.0 blocks of a vault, it becomes active and begins emitting flame particles inside of it. If the player has not unlocked the vault before (i.e. if the player is not in its list of players), a stream of orange particles flows from the player to the vault's keyhole when the player is within 4.5 blocks. The vault becomes inactive if there are no players within 4.5 blocks who have not unlocked the vault.

When active, a vault idly cycles between items once every second, visually displaying the current item inside the block. Each time the vault cycles to a new item, the item is randomly chosen from the loot table (§ Loot). Small orange particles also appear in front of the vault as if they were being sucked into the keyhole.

### Unlocking
A vault in the process of ejecting loot.
When a trial key is used on a vault, it ejects items. Items are ejected one stack at a time with a burst of particles for each stack.

When the vault is done ejecting items, it becomes inactive until another player approaches it.

Each vault can be unlocked only once per player. The vault is intended to reward each player for completing each trial chamber one time. This gives every player in a world the opportunity to find their own loot without having to travel substantial distances to find undiscovered loot at a fresh structure.


In Java Edition, each vault keeps track of up to 128 unique players that have opened it. If the list of players is full and another opens the vault, the new player is added to the end of the list while the first known player is forgotten and becomes able to open the vault again. Because of this, any item dropped by vaults is functionally renewable with enough players.[more information needed for Bedrock Edition]

### Loot
The vault ejects 3 to 6 stacks of loot, which can sometimes include a few unstackable items.

‌In Java Edition 1.21‌[upcoming][more information needed], the vault ejects a combination of loot from three different loot tables. The following information describes the loot ejected for a single player when a single trial key is used.

- Common loot
	- A set of common loot is 3 sets of the loot in the 2nd and 5th columns of the loot table below.
	- Every vault has at least one set of common loot.
	- A vault that does not give rare loot gives a 4th set of the loot in the 3rd and 6th columns below.
- Rare loot
	- Every vault has an 80% chance to include a set of rare loot.
	- The loot listed in the 2nd and 5th columns below corresponds with the 80% chance of one set of rare loot, plus the 20% chance of the one set of common loot that can be used in its place.
- Unique loot
	- Every vault has a 25% chance to also include one set of unique loot.
	- This loot, and the 75% chance for each vault to not have this loot, corresponds with the 4th and 7th columns below.

In Java Edition and Bedrock Edition, each trial chambers reward container contains  items drawn from 3 pools,  with the following distribution: 

| Item                              | Stack Size  [A] |      |    | Weight   [B]     |                |                 | Chance   [C] | Avg.per container   [D] | Avg. # containersto loot   [E] |
|-----------------------------------|-----------------|------|----|------------------|----------------|-----------------|--------------|-------------------------|--------------------------------|
|                                   | 1×              | 1–3× | 1× | 1×               | 1–3×           | 1×              |              |                         |                                |
| Nothing[F]                        | —               | —    | 1  | —                | —              | $\frac{36}{48}$ | 75.0%        | 0.750                   | 1.3                            |
| Emerald                           | 2–4             | 2–4  | —  | $\frac{12}{110}$ | $\frac{4}{22}$ | —               | 39.6%        | 1.418                   | 2.5                            |
| Arrow                             | 2–8             | 2–8  | —  | $\frac{4}{110}$  | $\frac{4}{22}$ | —               | 34.6%        | 2.000                   | 2.9                            |
| Arrow of Poison                   | 2–8             | 2–8  | —  | $\frac{4}{110}$  | $\frac{4}{22}$ | —               | 34.6%        | 2.000                   | 2.9                            |
| Iron Ingot                        | 1–4             | 1–4  | —  | $\frac{3}{110}$  | $\frac{3}{22}$ | —               | 26.9%        | 0.750                   | 3.7                            |
| Honey Bottle                      | 1–2             | 1–2  | —  | $\frac{3}{110}$  | $\frac{3}{22}$ | —               | 26.9%        | 0.450                   | 3.7                            |
| Ominous Bottle I - II[G]          | 1               | 1    | —  | $\frac{2}{110}$  | $\frac{2}{22}$ | —               | 18.6%        | 0.200                   | 5.4                            |
| Golden Apple                      | —               | —    | 1  | —                | —              | $\frac{6}{48}$  | 12.5%        | 0.125                   | 8.0                            |
| Damaged Shield[H]                 | 1               | —    | —  | $\frac{12}{110}$ | —              | —               | 10.9%        | 0.109                   | 9.2                            |
| Enchanted Bow[I]                  | 1               | —    | —  | $\frac{12}{110}$ | —              | —               | 10.9%        | 0.109                   | 9.2                            |
| Wind Charge                       | 4–12            | 4–12 | —  | $\frac{1}{110}$  | $\frac{1}{22}$ | —               | 9.6%         | 0.800                   | 10.4                           |
| Diamond                           | 1–2             | 1–2  | —  | $\frac{1}{110}$  | $\frac{1}{22}$ | —               | 9.6%         | 0.150                   | 10.4                           |
| Golden Carrot                     | 1–2             | —    | —  | $\frac{8}{110}$  | —              | —               | 7.3%         | 0.109                   | 13.7                           |
| Enchanted Book[J]                 | 1               | —    | —  | $\frac{8}{110}$  | —              | —               | 7.3%         | 0.073                   | 13.7                           |
| Enchanted Book[K]                 | 1               | —    | —  | $\frac{8}{110}$  | —              | —               | 7.3%         | 0.073                   | 13.7                           |
| Enchanted Crossbow[L]             | 1               | —    | —  | $\frac{8}{110}$  | —              | —               | 7.3%         | 0.073                   | 13.7                           |
| Enchanted Iron Axe[I]             | 1               | —    | —  | $\frac{8}{110}$  | —              | —               | 7.3%         | 0.073                   | 13.7                           |
| Enchanted Iron Chestplate[I]      | 1               | —    | —  | $\frac{8}{110}$  | —              | —               | 7.3%         | 0.073                   | 13.7                           |
| Bolt Armor Trim Smithing Template | —               | —    | 1  | —                | —              | $\frac{3}{48}$  | 6.2%         | 0.062                   | 16.0                           |
| Guster Banner Pattern             | —               | —    | 1  | —                | —              | $\frac{2}{48}$  | 4.2%         | 0.042                   | 24.0                           |
| Enchanted Diamond Axe[I]          | 1               | —    | —  | $\frac{4}{110}$  | —              | —               | 3.6%         | 0.036                   | 27.5                           |
| Enchanted Diamond Chestplate[I]   | 1               | —    | —  | $\frac{4}{110}$  | —              | —               | 3.6%         | 0.036                   | 27.5                           |
| Trident                           | —               | —    | 1  | —                | —              | $\frac{1}{48}$  | 2.1%         | 0.021                   | 48.0                           |



↑ The size of stacks (or for unstackable items, number) of this item on any given roll.

↑ The weight of this item relative to other items in the pool.

↑ The odds of finding any of this item in a single chest.

↑ The number of items expected per chest, averaged over a large number of chests.

↑ The average number of chests the player should expect to search to find any of this item.

↑ 'Nothing' does not refer to the chance of an empty chest.  Instead, it refers to the chance that the random loot generator does not add any loot on a single roll.

↑ Ominous bottle level between I and II

↑ The item has between 50% and 100% of its total durability.

↑ a b c d e Enchantment probabilities are the same as a level-5 to level-15 enchantment would be on an enchantment table that was able to apply treasure enchantments (except Soul Speed, and Swift Sneak), and where the chance of multiple enchantments is not reduced.

↑ Enchanted with a random level of Mending, Riptide, Loyalty, Channeling, or Impaling.

↑ Enchanted with a random level of Sharpness, Bane of Arthropods, Efficiency, Fortune, Silk Touch, or Feather Falling.

↑ Enchantment probabilities are the same as a level-5 to level-20 enchantment would be on an enchantment table that was able to apply treasure enchantments (except Soul Speed, and Swift Sneak), and where the chance of multiple enchantments is not reduced.



