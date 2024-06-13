# Damage
Damage represents injury from attacks or natural causes.

## Contents
- 1 Health
- 2 Damage
	- 2.1 Storage and display
- 3 Dealing damage
	- 3.1 Attack cooldown
	- 3.2 Critical hit
	- 3.3 Maximum damage dealt
- 4 Immunity
- 5 Inflicted by mobs
	- 5.1 Knockback
- 6 Natural damage
	- 6.1 Lightning damage
	- 6.2 Fall damage
		- 6.2.1 Fall damage resistance
			- 6.2.1.1 Sound
		- 6.2.2 Fall damage reduction
	- 6.3 Falling block
	- 6.4 Thorns enchantment
	- 6.5 Suffocation
		- 6.5.1 Entity cramming
	- 6.6 Drowning
	- 6.7 Starvation
	- 6.8 Cactus
	- 6.9 Berry bush
	- 6.10 Fire
	- 6.11 Lava
	- 6.12 Burning
	- 6.13 Magma block
	- 6.14 Campfire
	- 6.15 Status effects
		- 6.15.1 Instant damage
		- 6.15.2 Poison
		- 6.15.3 Wither
	- 6.16 Void
	- 6.17 Explosions
	- 6.18 Firework rocket explosion
	- 6.19 Freezing
- 7 Sounds
- 8 Achievements
- 9 Advancements
- 10 History
- 11 Issues
- 12 Trivia
- 13 References

## Health
Main article: Health
Players and mobs have a supply of health points, which are reduced when they are injured. Each health point is "half a heart," shown as 1.

Players have 20 × 10 health points, but that may vary by status effects. Mobs have varying numbers of health points, but these are not generally visible to players, with some exceptions: a player can see the health of a mount being ridden, a tamed wolf's health is indicated by its tail angle (90 degrees indicates it's at full health), the wither and ender dragon have boss bars that display their health, and an iron golem's body shows cracks as its health declines.

## Damage
Damage from attacks or natural causes subtracts from a player or mob's current health. When their health reaches zero, they die. Players can also recover health naturally by having their hunger at least 18 ( × 9) and the gamerule naturalRegeneration is set to true, or through status effects. Most mobs do not recover health except through status effects, but tamed horses, wolves, and cats can be healed by feeding them.

Armor absorbs some of the damage that would have been done to its wearer, but takes damage itself in the process.

Damage to tools and armor can be viewed in the item's tooltip by pressing the debug key combination F3 + H in Java Edition. If the player is playing on a Mac, they have to press fn + F3 + H.

### Storage and display
Health and damage are stored as floating-point numbers in units of half-hearts. When displaying the HUD, fractional values are rounded up to the next integer.

## Dealing damage
Players can deal damage by hitting most entities with targets at close (melee) range. Attacking without any tool (or with items not intended for attacking) does 1 damage, but weapons and certain tools do more:

- Swordsare crafted for this purpose. While swords do not extend attack range, they deal significantly more damage than any other item or tool except tridents and, inJava Edition, axes.
- Axes,pickaxesandshovels, as well ashoesinBedrock Edition, also deal more damage than bare fists. Axes deal the most damage; inJava Edition, axes deal more damage than swords, but have a slower attack speed.
- Tridentscan be used melee or ranged. They cannot be crafted.
- Any other item is equivalent to fists and does the same damage. This includes hitting something directly with a bow or held arrow, as well as hoes inJava Edition.
- While falling, melee attacks deal acritical hit(150% of the weapon's damage including potion effects, but beforeenchantmentsare applied, rounded down to the nearest hit point).

There are a few ranged weapons in the game:

- Arrowsare shot by holding and releasingusewhen wielding abow, and deal a certain amount of damage depending on the "charge" of the bow. Forcrossbows, it does a random factor between 6–11.
- Snowballsinflict damage only onblazes, whileeggsdon't deal any damage to mobs. Both still knock mobs back as if they had been damaged.
- Splash potionscan be thrown, inflicting various effects depending on the potion.
- Lingering potionscan be thrown, creating a cloud that inflicts various effects depending on the potion.
- Ender pearlsdon't deal damage to mobs or players other than the player throwing it.
- Fishing rodscannot be used to damage mobs directly. However, fishing rods can reel entities in and, inBedrock Edition, knock them back.
- Firework rocketscan be charged in acrossbow, dealing a range of damage depending on the amount offirework starsused to craft them, whether the crossbow has themultishotenchantment, and a random factor. At its highest, it deals 11–18 damage per firework.
- Tridentsare thrown similar to firing an arrow, by holding and releasingusewhile wielding the trident.

The values below show the base damage dealt per hit using various weapons. Critical hits do 50% extra damage.

Java Edition: Damage calculation starts with the weapon's base damage, then adds damage from effects, then multiplies by 1.5 if it's a critical hit, and then adds damage from enchantments.

| Tool    | Attack speed |   |     |     |   |     | Attack damage |           |           |           |           |           | Damage/Second (DPS) |     |     |           |           |           |
|---------|--------------|---|-----|-----|---|-----|---------------|-----------|-----------|-----------|-----------|-----------|---------------------|-----|-----|-----------|-----------|-----------|
| Sword   |              |   |     |     |   | 1.6 | 4             | 4         | 5         | 6         | 7         | 8         | 6.4                 | 6.4 | 8   | 9.6       | 11.2      | 12.8      |
| Trident |              |   |     |     |   | 1.1 |               |           |           |           |           | 9         |                     |     |     |           |           | 9.9       |
| Shovel  |              |   |     |     |   | 1   | 2.5× 1.25     | 2.5× 1.25 | 3.5× 1.75 | 4.5× 2.25 | 5.5× 2.75 | 6.5× 3.25 | 2.5                 | 2.5 | 3.5 | 4.5       | 5.5       | 6.5       |
| Pickaxe |              |   |     |     |   | 1.2 | 2             | 2         | 3         | 4         | 5         | 6         | 2.4                 | 2.4 | 3.6 | 4.8       | 6         | 7.2       |
| Axe     | 0.8          | 1 | 0.8 | 0.9 | 1 | 1   | 7             | 7         | 9         | 9         | 9         | 10        | 5.6                 | 7   | 7.2 | 8.1       | 9         | 10        |
| Hoe     | 1            | 1 | 2   | 3   | 4 | 4   |               |           |           |           |           | 1         | 1                   | 1   | 2   | 3[note 1] | 4[note 1] | 4[note 1] |
| Other   |              |   |     |     |   | 4   |               |           |           |           |           | 1         |                     |     |     |           |           | 4[note 1] |

1. ↑ a b c dAgainst a single target, DPS is effectively limited to 2 due to damage immunity.

Bedrock Edition:

| Tool    | Attack damage |       |      |      |         |           |
|---------|---------------|-------|------|------|---------|-----------|
|         | Wood          | Stone | Iron | Gold | Diamond | Netherite |
| Sword   | 5             | 6     | 7    | 5    | 8       | 9         |
| Trident |               |       |      |      |         | 9         |
| Shovel  | 2             | 3     | 4    | 2    | 5       | 6         |
| Pickaxe | 3             | 4     | 5    | 3    | 6       | 7         |
| Axe     | 4             | 5     | 6    | 4    | 7       | 8         |
| Hoe     | 3             | 4     | 5    | 3    | 6       | 7         |
| Other   |               |       |      |      |         | 1         |

