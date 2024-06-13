# Drops
Drops are items that appear when mobs and some other entities die or when most kinds of blocks are broken.

## Contents
- 1 Types of drops
	- 1.1 Common drops
		- 1.1.1 Looting
	- 1.2 Rare drops
	- 1.3 Equipped items
	- 1.4 Experience orbs
- 2 Mob drops
	- 2.1 Passive mobs
	- 2.2 Neutral mobs
	- 2.3 Hostile mobs
- 3 Entity drops
	- 3.1 Projectiles
	- 3.2 Stationary
	- 3.3 Vehicles
- 4 Block drops
	- 4.1 Materials and building blocks
	- 4.2 Ores
	- 4.3 Plants, corals and mushrooms
	- 4.4 Other
- 5 Video
- 6 History
- 7 Issues
- 8 See also
- 9 References

## Types of drops
Mobs do not drop any of the following if the game rule doMobLoot is set to false.

### Common drops
Common drops may appear at the location of a mob at the moment it receives fatal damage. Most mobs have certain items that they may drop when killed. Some common drops, such as leather, don't always drop, but have a large chance (at least 50%, depending on the drop range) to do so. Some common drops, such as blaze rods, don't drop at all if the mob was not killed by the player.

Each of these items has a drop range, which is a random uniform distribution of numbers of items that drop. For example, a cow drops 0–2 leather items and 1–3 raw beef items. Because the range for leather includes 0, there is a 1⁄3 chance of no leather being dropped.

A baby animal does not drop any common drops upon death. 

#### Looting
Some common and uncommon drops are affected by the Looting enchantment. At most, a number of additional items equal to enchantment level are dropped.

More specifically, the game generates a fractional number ranging from 0 to the Looting level, which is then rounded to the nearest integer. This causes the numbers in the middle of drop range to occur twice as often. The probabilities are as follows:

| Looting level | No items      | 1 item        | 2 items       | 3 items       |
|---------------|---------------|---------------|---------------|---------------|
| Looting I     | $\frac{1}{2}$ | $\frac{1}{2}$ | --            | --            |
| Looting II    | $\frac{1}{4}$ | $\frac{1}{2}$ | $\frac{1}{4}$ | --            |
| Looting III   | $\frac{1}{6}$ | $\frac{1}{3}$ | $\frac{1}{3}$ | $\frac{1}{6}$ |

A stray's tipped arrow is a special case: while Looting can attempt to increase arrow drop amount, the final number of dropped arrows is capped at 1. So, Looting effectively increases arrow dropping odds, up to 11⁄12 with Looting III.

### Rare drops
Rare drops normally appear if the monster is killed by a player, although some rare drops can also be obtained by other means. Rare drops are always a single item, but may appear in conjunction with other common drops. A drop is considered rare if they are accompanied by the random_chance_with_looting condition in the mob's loot table.

Rare drops typically have a 2.5% chance of dropping, plus 1 percentage point per level of Looting on the weapon used (up to a maximum of 5.5% with Looting III). An exception to this is that a rabbit drops a rabbit's foot with a 10% chance, plus 3 percentage points per level of Looting (to a maximum of 19% with Looting III). in Bedrock Edition there are other exceptions: a wither skeleton drops a wither skeleton skull with a 2.5% chance plus 2 percentage points per level of Looting (to a maximum of 8.5% with Looting III), and a drowned drops a copper ingot with an 11% chance plus 2 percentage points per level of looting (to a maximum of 17% with Looting III).

Note that in case of multiple rare drops (guardian and zombie types) the 2.5% chance is split between them, instead of being rolled for each item.

The shulker shell is technically also a rare drop, only ever dropping in singles from shulkers, although they don't require a player kill, have a 50% base chance, and increase by 6.25% per Looting level.‌[JE  only]

### Equipped items
An enchanted bow received from a skeleton's drops.
When killed by a player or a tamed wolf, a monster can drop equipment and armor that it spawned with. Each piece of equipment the monster was spawned with is dropped with an 8.5% chance‌[JE  only] or 25% chance‌[BE  only],[1] except pumpkins, jack o'lanterns, and a vex's iron sword, which have a 0% chance. This value is determined by the mob's HandDropChances and ArmorDropChances tags. The Looting enchantment increases this chance by 1% per level (up to 11.5% with Looting III, and 3% for pumpkins, jack o'lanterns, and said sword)‌[JE  only] or 5% per level in some cases‌[BE  only]. The chance is rolled for each piece of equipment, so it is possible for a monster to drop more than one piece of equipment upon death.

There are also some equipped items that are guaranteed to drop:

- All items the mob picked up after spawning are always dropped, even when it isn't killed by a player and even if it is a babyzombie.
	- This is the case only for hostile mobs, not forvillagers.
- An ominous banner is always dropped byillagerswearing it.
- Horses,donkeys,mules,llamasandpigs, andstridersdrop anyitemsequipped to them by players, likesaddles,carpetorchests.
- Ravagersdrop their saddle.
- Drowneddropnautilus shellsspawned in the offhand.

