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

### Attack cooldown
"Cooldown" redirects here.  For the enchantment in Minecraft Dungeons, see MCD:Cool Down.

  

This feature is exclusive to  Java Edition. 


Attack indicator (crosshair), empty and charged
Attack indicator (hotbar), empty and charged
When a player swings a weapon or switches to a weapon, they are locked into a cooldown meter that limits how much damage they can deal and requires them to wait before being able to deal maximum damage again. The base damage done depends on the time between attacks, and is also reflected in the height of the held weapon on screen and the attack indicator bar. The fill-level of the attack indicator bar (as a proportion of it's total width) is exactly equal to the damage the held weapon would deal if it was used now in proportion of its maximum damage. Therefore, the attack indicator appears fully charged when the damage dealt after cooldown reaches 100% of the maximum. There are settings for the attack indicators in the options menu. At 84.8% attack cooldown charge, critical hits, sweep attacks, and sprint-knockback attacks become possible.

| Item |         | Time (seconds) |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |      |
|------|---------|----------------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|------|
|      |         | 0.00           | 0.05   | 0.10   | 0.15   | 0.20   | 0.25   | 0.30   | 0.35   | 0.40   | 0.45   | 0.50   | 0.55   | 0.60   | 0.65   | 0.70   | 0.75   | 0.80   | 0.85   | 0.90   | 0.95   | 1.00   | 1.05   | 1.10   | 1.15   | 1.20   | 1.25 |
|      | Sword   | 20.13%         | 21.15% | 23.20% | 26.27% | 30.37% | 35.49% | 41.63% | 48.80% | 56.99% | 66.21% | 76.45% | 87.71% |        |        |        |        |        |        |        |        |        |        |        |        |        | 100% |
|      | Trident | 20.06%         | 20.54% | 21.51% | 22.96% | 24.90% | 27.32% | 30.22% | 33.61% | 37.48% | 41.84% | 46.68% | 52.00% | 57.81% | 64.10% | 70.88% | 78.14% | 85.88% | 94.11% |        |        |        |        |        |        |        | 100% |
|      | Shovel  | 20.05%         | 20.45% | 21.25% | 22.45% | 24.05% | 26.05% | 28.45% | 31.25% | 34.45% | 38.05% | 42.05% | 46.45% | 51.25% | 56.45% | 62.05% | 68.05% | 74.45% | 81.25% | 88.45% | 96.05% |        |        |        |        |        | 100% |
|      | Pickaxe | 20.07%         | 20.65% | 21.80% | 23.53% | 25.83% | 28.71% | 32.17% | 36.20% | 40.81% | 45.99% | 51.75% | 58.09% | 65.00% | 72.49% | 80.55% | 89.19% | 98.41% |        |        |        |        |        |        |        |        | 100% |
| Axe  |         | 20.03%         | 20.29% | 20.80% | 21.57% | 22.59% | 23.87% | 25.41% | 27.20% | 29.25% | 31.55% | 34.11% | 36.93% | 40.00% | 43.33% | 46.91% | 50.75% | 54.85% | 59.20% | 63.81% | 68.67% | 73.79% | 79.17% | 84.80% | 90.69% | 96.83% | 100% |
|      |         | 20.05%         | 20.45% | 21.25% | 22.45% | 24.05% | 26.05% | 28.45% | 31.25% | 34.45% | 38.05% | 42.05% | 46.45% | 51.25% | 56.45% | 62.05% | 68.05% | 74.45% | 81.25% | 88.45% | 96.05% |        |        |        |        |        | 100% |
|      |         | 20.04%         | 20.36% | 21.01% | 21.98% | 23.28% | 24.90% | 26.84% | 29.11% | 31.70% | 34.62% | 37.86% | 41.42% | 45.31% | 49.52% | 54.06% | 58.92% | 64.10% | 69.61% | 75.44% | 81.60% | 88.08% | 94.88% |        |        |        | 100% |
| Hoe  |         | 20.05%         | 20.45% | 21.25% | 22.45% | 24.05% | 26.05% | 28.45% | 31.25% | 34.45% | 38.05% | 42.05% | 46.45% | 51.25% | 56.45% | 62.05% | 68.05% | 74.45% | 81.25% | 88.45% | 96.05% |        |        |        |        |        | 100% |
|      |         | 20.20%         | 21.80% | 25.00% | 29.80% | 36.20% | 44.20% | 53.80% | 65.00% | 77.80% | 92.20% |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        | 100% |
|      |         | 20.45%         | 24.05% | 31.25% | 42.05% | 56.45% | 74.45% | 96.05% |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        | 100% |
|      |         | 20.80%         | 27.20% | 40.00% | 59.20% | 84.80% |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        | 100% |
|      | Other   | 20.80%         | 27.20% | 40.00% | 59.20% | 84.80% |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        | 100% |

The attackSpeed attribute controls the length of the cooldown time, with the time taken being T = 20 / attackSpeed ticks. The damage multiplier is then 0.2 + ((t + 0.5) / T) ^ 2 * 0.8, restricted to the range 0.2 – 1, where t is the number of ticks since the last attack or item switch.

Damage done by enchantments (Sharpness, Smite, and Bane of Arthropods) is also reduced, but not as severely (the multiplier is not squared):



| Item |         | Time (seconds) |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |      |
|------|---------|----------------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|------|
|      |         | 0.00           | 0.05   | 0.10   | 0.15   | 0.20   | 0.25   | 0.30   | 0.35   | 0.40   | 0.45   | 0.50   | 0.55   | 0.60   | 0.65   | 0.70   | 0.75   | 0.80   | 0.85   | 0.90   | 0.95   | 1.00   | 1.05   | 1.10   | 1.15   | 1.20   | 1.25 |
|      | Sword   | 4.00%          | 12.00% | 20.00% | 28.00% | 36.00% | 44.00% | 52.00% | 60.00% | 68.00% | 76.00% | 84.00% | 92.00% |        |        |        |        |        |        |        |        |        |        |        |        |        | 100% |
|      | Trident | 2.75%          | 8.25%  | 13.75% | 19.25% | 24.75% | 30.25% | 35.75% | 41.25% | 46.75% | 52.25% | 57.75% | 63.25% | 68.75% | 74.25% | 79.75% | 85.25% | 90.75% | 96.25% |        |        |        |        |        |        |        | 100% |
|      | Shovel  | 2.50%          | 7.50%  | 12.50% | 17.50% | 22.50% | 27.50% | 32.50% | 37.50% | 42.50% | 47.50% | 52.50% | 57.50% | 62.50% | 67.50% | 72.50% | 77.50% | 82.50% | 87.50% | 92.50% | 97.50% |        |        |        |        |        | 100% |
|      | Pickaxe | 3.00%          | 9.00%  | 15.00% | 21.00% | 27.00% | 33.00% | 39.00% | 45.00% | 51.00% | 57.00% | 63.00% | 69.00% | 75.00% | 81.00% | 87.00% | 93.00% | 99.00% |        |        |        |        |        |        |        |        | 100% |
| Axe  |         | 2.00%          | 6.00%  | 10.00% | 14.00% | 18.00% | 22.00% | 26.00% | 30.00% | 34.00% | 38.00% | 42.00% | 46.00% | 50.00% | 54.00% | 58.00% | 62.00% | 66.00% | 70.00% | 74.00% | 78.00% | 82.00% | 86.00% | 90.00% | 94.00% | 98.00% | 100% |
|      |         | 2.50%          | 7.50%  | 12.50% | 17.50% | 22.50% | 27.50% | 32.50% | 37.50% | 42.50% | 47.50% | 52.50% | 57.50% | 62.50% | 67.50% | 72.50% | 77.50% | 82.50% | 87.50% | 92.50% | 97.50% |        |        |        |        |        | 100% |
|      |         | 2.25%          | 6.75%  | 11.25% | 15.75% | 20.25% | 24.75% | 29.25% | 33.75% | 38.25% | 42.75% | 47.25% | 51.75% | 56.25% | 60.75% | 65.25% | 69.75% | 74.25% | 78.75% | 83.25% | 87.75% | 92.25% | 96.75% |        |        |        | 100% |
| Hoe  |         | 2.50%          | 7.50%  | 12.50% | 17.50% | 22.50% | 27.50% | 32.50% | 37.50% | 42.50% | 47.50% | 52.50% | 57.50% | 62.50% | 67.50% | 72.50% | 77.50% | 82.50% | 87.50% | 92.50% | 97.50% |        |        |        |        |        | 100% |
|      |         | 5.00%          | 15.00% | 25.00% | 35.00% | 45.00% | 55.00% | 65.00% | 75.00% | 85.00% | 95.00% |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        | 100% |
|      |         | 7.50%          | 22.50% | 37.50% | 52.50% | 67.50% | 82.50% | 97.50% |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        | 100% |
|      |         | 10.00%         | 30.00% | 50.00% | 70.00% | 90.00% |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        | 100% |
|      | Other   | 10.00%         | 30.00% | 50.00% | 70.00% | 90.00% |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        |        | 100% |

### Critical hit
"Critical hit" redirects here.  For the enchantment in Minecraft Dungeons, see Critical Hit.
A critical hit performed on a sheep.
A critical hit is an attack that deals extra damage compared to a regular attack. Critical melee strikes, regardless of the weapon used, cause small star, cross shaped particles to fly out of the target who was critically hit. Critical hits can only be performed if the attack cooldown of the weapon is at 84.8% or higher. Arrows shot from crossbows and fully charged bows leave a trail of the same small star particles as they fly through the air. Critical hits affect all damageable entities including players, mobs, and armor stands, but excluding paintings, boats, minecarts or the ender dragon‌[Java Edition  only].

In melee combat, a critical hit occurs when a player attacks a mob while falling, including while coming down from a jump, but not while jumping up. The attack deals 150% of the attack's base damage (after strength is applied and before‌[JE  only] / after‌[BE  only] enchantments or armor are applied).

Ordinarily, players cannot perform critical hits while sprinting, because a sprint-knockback attack is performed instead. However, by continuing to hold down the sprint key after performing a sprint-knockback attack, all successive hits can be critical hits, and sprint-knockback attacks become impossible until the sprint key is released.‌[Java Edition  only] In Bedrock Edition and the Java Edition Combat Tests, players can perform critical hits and sprint-knockback attacks simultaniously.

The requirements for a melee critical hit are:

- A player must befalling.
- A player must not be on the ground.
- A player must not be on aladderor any type ofvine.
- A player must not be inwater.
- A player must not be affected byBlindness.
- A player must not be affected bySlow Falling.
- A player must not be riding anentity.
- A player must not beflying.
- The attack cooldown must not be below 84.8%.‌[Java Edition  only]

### Maximum damage dealt
In Survival mode, the maximum damage that can be dealt by a player depends on various factors as described below.

** Melee attack **
- InJava Edition
	- 36.5× 18.25damage, consisting of 10from a netheriteaxe+ 6fromStrengthII, all × 1.5 from a critical hit (+ 8damage), + 12.5× 6.25damage fromSmiteV on an undead target, orBane of ArthropodsV on an arthropod.
	- The maximum on a non-undead non-arthropod target is only 27× 13.5: 10from a netherite axe + 6fromStrengthII, all × 1.5 from a critical hit (+ 8damage), + 3damage fromSharpnessV. A full set ofProtectionIV netheritearmorwould reduce the 27× 13.5damage to 4.044× 2.022.
	- By use of amacesmash attack, the maximum damage that can be dealt by a player is infinite.
- InBedrock Edition
	- Maximum damage to undeads or arthropods is 41.25× 20.625damage, consisting of 8from netherite sword + 12.5× 6.25from Smite V for undead mobs or Bane of Arthropods V for arthropod mobs + 7from strength II, all × 1.5 from a critical hit (+ 13.75× 6.875damage).
	- Maximum damage to non-undead and non-arthropod on land is 31.875× 15.9375damage, consisting of 8from netherite sword + 6.25× 3.125from Sharpness V + 7from Strength II, all × 1.5 from a critical hit (+ 10.625× 5.3125damage).
	- Maximum damage to players and mobs on water or during rain is 42.75× 21.375damage, consisting of 9of melee trident + 12.5× 6.25from Impaling V + 7from strength II, all × 1.5 from a critical hit (+ 14.25× 7.125damage). (Also work withRiptide)
	- By use of amacesmash attack, the maximum damage that can be dealt by a player is infinite.

** Ranged attack **
- With bow:
	- Maximum damage to players and mobs is 25× 12.5damage from a critical shot from a bow with thePowerV enchantment. Because the instantaneous effects of arrows don't stack with arrow damage and apply during immunity phase, using harming (or healing arrows to undead mobs) doesn't add bonus damage unless the target has enough armor or Projectile Protection levels so the damage dealt by the arrow is lower than the magical damage effect after Protection/Resistance reduction. This is sufficient to kill most mobs in one hit though.
- With crossbow:
	- Maximum damage to players and non-undead mobs is 64× 32damage, consisting of a single shot of three arrows of harming II from multishot enchantment that hit single mobs. Two of the arrows deal 9damage while one of them deals 10+ 36× 18damage from instant damage II effect (12× 6per arrow).
	- Maximum damage to undead mobs is 52× 26damage, consisting of a single shot of three arrows of healing II from multishot enchantment that hit single mobs. Two of the arrows deal 9damage while one of them deals 10+ 24× 12damage from instant health II effect (8per arrow).

## Immunity
After sustaining damage from any source, a mob/player turns red for half a second. During this period, it is immune to most kinds of further damage. For instance, if the player attacks a mob by repeatedly hitting the attack button, attacks that land while the mob is immune deal no damage, and does not reduce the durability of a melee weapon. Unsuccessful attacks also do not anger neutral mobs.

During the immunity period, any damage which is equal to or less than the original damage that caused the immunity is ignored. However, any higher damage (before accounting for armor, enchantments, or status effects) causes only the difference between the original and new damage amounts to be dealt. For example, if a mob is attacked with a weapon dealing 7 damage and then attacked with another weapon dealing 12 × 6 damage during the immunity period, the second hit deals 5 damage (resulting in 12 × 6 total). This does not reset the immunity period.

When an attack deals a fatal amount of damage to a mob, so that it dies while immune, its death sound is not triggered. ‌[Java Edition  only]

## Inflicted by mobs
The damage mobs deal to players is affected by the difficulty setting of the world they are in. The below values represent the amount of damage taken per hit.

- A mob attackinganother mobalways deals the damage it would deal to a player on Normal difficulty, even if the current value of the difficulty setting is different.
- The values for acreeperand aghastassume the player is directly adjacent to the respective explosion.
- The damage ofslimesandmagma cubesdepends on their size. Tiny slimes, while hostile, are unable to do damage directly.
- Mobs deal no damage to players on peaceful.

| Mob                                    | Difficulty                 |                              |                                    | Status effect(s)                                                                                                                |
|----------------------------------------|----------------------------|------------------------------|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
|                                        | Easy                       | Normal                       | Hard                               |                                                                                                                                 |
| Axolotl                                |                            |                              | 2                                  | No                                                                                                                              |
| Bee                                    | 2                          | 2                            | 3                                  | Poisonfor 10 seconds on Normal difficulty and for 18 seconds on Hard difficulty                                                 |
| Blaze(melee)                           | 4                          | 6                            | 9                                  | No                                                                                                                              |
| Blaze fireball                         |                            |                              | 5+firefor 5 seconds                | No                                                                                                                              |
| Bogged arrow                           |                            |                              | 3to 5                              | Poisonfor 4 seconds                                                                                                             |
| Bogged(melee)                          |                            | 2                            | 3                                  | No                                                                                                                              |
| Breeze wind charge                     |                            | 1                            | 1.5× 0.75                          | No                                                                                                                              |
| Cat                                    |                            |                              | 3                                  | No                                                                                                                              |
| Cave Spider                            | 2                          | 2                            | 3                                  | Poisonfor 7 seconds on Normal difficulty and for 15 seconds on Hard difficulty                                                  |
| Creeper explosion(normal)              | 22.5× 11.25                | 43× 21.5                     | 64.5× 32.25                        | When exploding: NoIf having a potion effect when exploding, it leaves an effect cloud with the effect, like a lingering potion. |
| Creeper explosion(charged)             | 43.5× 21.75                | 85× 42.5                     | 127.5× 63.75                       |                                                                                                                                 |
| Dolphin                                | 2.5× 1.25                  | 3                            | 4.5× 2.25                          | No                                                                                                                              |
| Drowned                                |                            |                              |                                    | No                                                                                                                              |
| Drowned trident(Ranged)                | 7                          | 9                            | 12× 6                              | No                                                                                                                              |
| Drowned trident(Melee)‌[BE  only]      | 6                          | 11× 5.5                      | 16× 8                              | No                                                                                                                              |
| Elder Guardian(Laser)                  | 5                          | 8                            | 12× 6                              | InflictsMining FatigueIII for 5 minutes on nearby players                                                                       |
| Elder Guardian(Spikes)                 |                            | 2                            | 3                                  |                                                                                                                                 |
| Elder Guardian Ghost(Spikes)           |                            |                              | 2                                  |                                                                                                                                 |
| Ender Dragon(Melee)                    | 6                          | 10                           | 15× 7.5                            | No                                                                                                                              |
| Ender Dragon(Wings)                    | 3                          | 5                            | 7                                  | No                                                                                                                              |
| Ender Dragon(Breath)                   |                            |                              | 3per second                        | Area effect cloudofInstant Damage                                                                                               |
| Ender DragonDragon Fireball            |                            |                              | 6per second                        |                                                                                                                                 |
| Enderman                               | 4.5× 2.25                  | 7                            | 10.5× 5.25                         | No                                                                                                                              |
| Endermite                              |                            | 2                            | 3                                  | No                                                                                                                              |
| Evoker fangs‌[JE  only]                | 4                          | 6                            | 9                                  | No                                                                                                                              |
| Evoker fangs‌[BE  only]                |                            |                              | 6                                  | No                                                                                                                              |
| Fox                                    |                            | 2                            | 3                                  | No                                                                                                                              |
| Frog                                   |                            |                              | Target despawns after being pulled | No                                                                                                                              |
| Ghast fireball(Impact)                 | 4                          | 6                            | 9                                  | No                                                                                                                              |
| Ghast fireball(Explosion)              | 9.5× 4.75                  | 17× 8.5                      | 25.5× 12.75                        | No                                                                                                                              |
| Giant‌[JE  only]                       | 26× 13                     | 50× 25                       | 75× 37.5                           | No                                                                                                                              |
| Goat                                   |                            | 2                            | 3                                  | No                                                                                                                              |
| Goat(baby)                             |                            | 1                            | 1.5× 0.75                          | No                                                                                                                              |
| Guardian(Laser)                        | 4                          | 6                            | 9                                  | No                                                                                                                              |
| Guardian(Spikes)                       |                            | 2                            | 3                                  | No                                                                                                                              |
| Hoglin‌[JE  only]                      | 2.5× 1.25to 5              | 3to 8                        | 4.5× 2.25to 12× 6                  | No                                                                                                                              |
| Hoglin‌[BE  only]                      | 3                          | 6                            | 9                                  | No                                                                                                                              |
| Hoglin(baby)                           |                            | 0.5× 0.25                    | 0.75× 0.375                        | No                                                                                                                              |
| Husk                                   | 2.5× 1.25                  | 3                            | 4.5× 2.25                          | Hungerwhen attacking any mob for 7 × floor ofRDseconds                                                                          |
| Illusioner arrow‌[JE  only]            |                            | 2to 5                        | 3to 5                              | ThrowsBlindnessspells on the player, ifregional difficultyis 2 or greater                                                       |
| Iron Golem                             | 4.75× 2.375to 11.75× 5.875 | 7.5× 3.75to 21.5× 10.75      | 11.25× 5.625to 32.25× 16.125       | No                                                                                                                              |
| The Killer Bunny                       | 5                          | 8                            | 12× 6                              | No                                                                                                                              |
| Llama spit                             |                            | 1                            | 1.5× 0.75                          | No                                                                                                                              |
| Magma Cube(big)                        | 4                          | 6                            | 9                                  | No                                                                                                                              |
| Magma Cube(medium)                     | 3                          | 4                            | 6                                  | No                                                                                                                              |
| Magma Cube(small)                      | 2.5× 1.25                  | 3                            | 4.5× 2.25                          | No                                                                                                                              |
| Ocelot                                 |                            |                              | 3                                  | No                                                                                                                              |
| Old Zombie Villager                    | 2.5× 1.25                  | 3                            | 4.5× 2.25                          | No                                                                                                                              |
| Panda                                  | 4                          | 6                            | 9                                  | No                                                                                                                              |
| Phantom‌[JE  only]                     |                            | 2                            | 3                                  | No                                                                                                                              |
| Phantom‌[BE  only]                     | 4                          | 6                            | 9                                  | No                                                                                                                              |
| Piglin arrow‌[JE  only]                |                            | 2to 5                        | 3to 5                              | No                                                                                                                              |
| Piglin arrow‌[BE  only]                |                            | 2- 4                         | 2to 5                              | No                                                                                                                              |
| Piglin(Melee with Sword)‌[JE  only]    | 5                          | 8                            | 12× 6                              | No                                                                                                                              |
| Piglin(Melee with Sword)‌[BE  only]    | 5                          | 9                            | 13× 6.5                            | No                                                                                                                              |
| Piglin(Melee without Sword)‌[JE  only] | 3.5× 1.75                  | 5                            | 7.5× 3.75                          | No                                                                                                                              |
| Piglin Brute‌[JE  only]                | 7.5× 3.75                  | 13× 6.5                      | 19.5× 9.75                         | No                                                                                                                              |
| Piglin Brute‌[BE  only]                | 6                          | 10                           | 15× 7.5                            | No                                                                                                                              |
| Piglin Brute(Unarmed)                  | 4.5× 2.25                  | 7                            | 10.5× 5.25                         | No                                                                                                                              |
| Pillager arrow                         | 3.5× 1.75                  | 4                            | 5                                  | No                                                                                                                              |
| Pillager(Melee)‌[BE  only]             | 2                          | 3                            | 5                                  | No                                                                                                                              |
| Polar Bear                             | 4                          | 6                            | 9                                  | No                                                                                                                              |
| Pufferfish(Semi-puffed)                |                            | 2                            | 3                                  | Poisonfor 3 seconds                                                                                                             |
| Pufferfish(Fully Puffed)‌[JE  only]    | 2.5× 1.25                  | 3                            | 4.5× 2.25                          | Poisonfor 6 seconds                                                                                                             |
| Pufferfish(Fully Puffed)‌[BE  only]    |                            | 2                            | 3                                  | Poisonfor 10 seconds                                                                                                            |
| Ravager(Melee)                         | 7                          | 12× 6                        | 18× 9                              | No                                                                                                                              |
| Ravager(Roar)                          | 4                          | 6                            | 9                                  | No                                                                                                                              |
| Shulker bullet                         | 3                          | 4                            | 6                                  | Levitationfor 10 seconds                                                                                                        |
| Silverfish                             |                            | 1                            | 1.5× 0.75                          | No                                                                                                                              |
| Skeleton arrow‌[JE  only]              | 2to 4                      | 3to 4                        | 4to 5                              | No                                                                                                                              |
| Skeleton arrow‌[BE  only]              |                            | 1to 4, varies with proximity | 1to 5, varies with proximity       | No                                                                                                                              |
| Skeleton(melee)                        |                            | 2                            | 3                                  | No                                                                                                                              |
| Slime(big)                             | 3                          | 4                            | 6                                  | No                                                                                                                              |
| Slime(medium)                          |                            | 2                            | 3                                  | No                                                                                                                              |
| Slime(small)                           |                            |                              | 0                                  | No                                                                                                                              |
| Snow Golem snowball                    |                            |                              | 3toblazes                          | No                                                                                                                              |
| Spider                                 |                            | 2                            | 3                                  | No, but can spawn with effects                                                                                                  |
| Stray arrow‌[JE  only]                 |                            |                              | 3to 5                              | Slownessfor 30 seconds when their tipped arrow hits any mob (including another stray)                                           |
| Stray arrow‌[BE  only]                 |                            |                              | Damage varies with proximity       |                                                                                                                                 |
| Stray(melee)                           |                            | 2                            | 3                                  | No                                                                                                                              |
| Trader Llama spit                      |                            | 1                            | 1.5× 0.75                          | No                                                                                                                              |
| Vex                                    | 5.5× 2.75                  | 9                            | 13.5× 6.75                         | No                                                                                                                              |
| Vex(Unarmed)                           | 3                          | 4                            | 5                                  | No                                                                                                                              |
| Villager's firework rocket             | 5                          | 8                            | 12× 6                              | No                                                                                                                              |
| Vindicator                             | 7.5× 3.75                  | 13× 6.5                      | 19.5× 9.75                         | No                                                                                                                              |
| Vindicator(Unarmed)                    | 3.5× 1.75                  | 5                            | 7.5× 3.75                          | No                                                                                                                              |
| Warden(Melee)                          | 16× 8                      | 30× 15                       | 45× 22.5                           | No                                                                                                                              |
| Warden(Ranged)                         | 6                          | 10                           | 15× 7.5                            | No                                                                                                                              |
| Witch                                  |                            |                              | Deals damage by throwingpotions    | Throws splash potions ofPoison,Instant Damage,Slowness, andWeakness                                                             |
| Wither Skeleton                        | 5                          | 8                            | 12× 6                              | Witherfor 10 seconds                                                                                                            |
| Wither Skeleton(Unarmed)               | 2                          | 2                            | 3                                  | Witherfor 10 seconds                                                                                                            |
| Wither(birth explosion)                | 35.5× 17.75                | 69× 34.5                     | 103.5× 51.75                       | No                                                                                                                              |
| Wither Skull                           | 5                          | 8                            | 12× 6                              | WitherII for 10 seconds on Normal difficulty and 40 seconds on Hard difficulty                                                  |
| Wither(dash attack)<br/>‌[BE  only]    |                            |                              | 15× 7.5                            | No                                                                                                                              |
| Wolf                                   | 3                          | 4                            | 6                                  | No                                                                                                                              |
| Zoglin                                 | 3to 5                      | 3to 8                        | 4.5× 2.25to 12× 6                  | No                                                                                                                              |
| Zoglin(baby)                           | 0.25× 0.125                | 0.5× 0.25                    | 0.75× 0.375                        | No                                                                                                                              |
| Zombie                                 | 2.5× 1.25                  | 3                            | 4.5× 2.25                          | No                                                                                                                              |
| Zombified Piglin                       | 5                          | 8                            | 12× 6                              | No                                                                                                                              |
| Zombified Piglin(Unarmed)              | 3                          | 5                            | 7                                  | No                                                                                                                              |
| Zombie Villager                        | 2.5× 1.25                  | 3                            | 4.5× 2.25                          | No                                                                                                                              |
| Wither Skull(explosion)                |                            |                              | 5                                  |                                                                                                                                 |



### Knockback
When receiving damage from players, mobs, most projectiles, or explosions, players and mobs are also knocked back. The resulting disorientation and loss of control should not be underestimated, as it is possible to be knocked back over a cliff or into lava, both of which are potentially fatal.

A sprinting attack causes extra knockback. A thrown egg or snowball also causes knockback, despite not damaging most mobs. Players whoever do not receive knockback from a thrown egg or snowball. Entities riding another entity never receive any knockback when attacked. Iron golems, shulkers, agents, NPCs,  wardens, and the ender dragon also don't receive knockback, and certain other mobs have varying levels of knockback resistance. Each piece of netherite armor adds 10% knockback resistance to its wearer, giving 40% knockback resistance with a full set.

Knockback resistance reduces knockback by multiplying the velocity a mob receives from knockback. If the velocity the mob would have without any knockback resistance is v, and the mob has a knockback resistance of r%, then the mob's actual velocity is determined by the formula A=v×(1−r100).

## Natural damage
Besides mob attacks, players can take damage from several other sources.

### Lightning damage
Lightning striking on or near the player inflicts 5 damage, which can be reduced with armor. Natural lightning strikes on the player are rare and occur only during thunderstorms. Players and mobs that get hit by lightning are set on fire, which is quickly extinguished by the rain during a thunderstorm.

### Fall damage
All players and most mobs receive damage when falling from great heights.

Fall damage is calculated based on change in the Y coordinate of the entity's position, rather than the entity's velocity when hitting the ground. This means that fall damage is also not based on the distance fallen, since an mid-air entity on a lead can travel a lot of distance as it bobs up and down.

Fall damage is 1 for each block of change in Y after the third. Thus, falling 4 blocks causes 1 damage, 2 damage for 5 blocks, and so forth:

fall damage = max(0, -(change in Y) − 3)
- Note that the change in Y needs to be negative, because falling upward is not normally possible and never does any damage. If the fall damage would be less than or equal to 0, then the entity simply does not take damage.

While a 23-block fall should be fatal for a player at full health (23 - 3 = 20 × 10 of damage), due to the way the change in Y is calculated, a 23.5-block fall is required instead, because the last half-block of change in Y usually isn't added in when calculating fall damage. For certain heights, including 23-block falls, this discrepancy is enough to avoid an entire 1 of damage.

Therefore, without Feather Falling or relevant status effects, or immunity to fall damage, the minimum guaranteed lethal change in Y for any mob is:

fatal change in Y = -(health + 3.5)
#### Fall damage resistance
Unenchanted Armor does not reduce fall damage. However, some echantments do reduce fall damage: Feather Falling and Protection.

Some status effects reduce fall damage:

- Slow Falling- Negates all fall damage. If the effect wears off mid-air, the entity only takes damage for the height difference between where the effect ended and where the entity lands.
- Resistance

Every player is immune to fall damage when the game rule fallDamage is set to false. Players who can fly are not immune to fall damage, and take fall damage for the change in Y from where they stop flying to where they land.

Hostile mobs that are immune to fall damage:

- Blaze
- Breeze
- Chicken Jockey
- Ender Dragon
- Ghast
- Magma Cube
- Phantom
- Shulker
- Vex
- Wither

Passive mobs that are immune to fall damage:

- Allay
- Agent
- Bat
- Bee
- Cat
- Chicken
- Iron Golem
- NPC
- Ocelot
- Parrot
- Snow Golem

Other mobs with resistance to fall damage:

- These mobs take damage as if they fell only half the distance:
	- Camel
	- Donkey
	- Horse
	- Mule
	- Skeleton Horse
	- Zombie Horse
	- Llama

- This mob always takes 10less fall damage:
	- Goat

- This mob always takes 5less fall damage:
	- Frog

- This mob takes damage for 5 blocks less than it fell, and its fall damage is not affected byJump Boost:
	- Fox

##### Sound
For most solid blocks, if a player of mob falls onto the blocks and takes damage, a sound plays and is transmitted to the environment. No sound is played or transmitted if the entity doesn't take damage. Falling from a small height (4–7 blocks) plays a thud sound, and falling from a larger height (8 or more blocks) give a click or cracking sound.

#### Fall damage reduction
In some cases, falling damage can be avoided:

- Sneakingprevents a player from falling off a drop of one block or greater.
- Entering or being inwater(when not in a boat) resets the change in Y. This includes falling into the water of any depth, as long as the entity collides with the water before colliding with the ground.
- Colliding with acobwebresets the entity's change in Y.
- Being inlavareduces the change in Y by half a block eachgame tick.
- Flying usingelytrasuch that the vertical movement is upward, level or less than 0.5 blocks per game tick downward resets change in Y to 1 block.
- Moving into aladderorvine's area of effect resets the fall damage. This also applies totrapdoorsacting as a ladder.
	- Falling onto the top of a ladder does not reset the change in Y and counts as hitting the ground.
	- Horses are unaffected by ladders and vines, and so their change in Y is not reset.
	- Spidersclimbing a block count the block as a "ladder" for this purpose.
- An entity riding another entity does not accumulate any change in Y. However, when the ridden entity takes fall damage it damages all riders for the same change in Y.
- Aminecart's change in Y is reset when landing on rails.
- Boatsdo not accumulate any change in Y while in water deeper than 1 block.
- Teleporting due to a thrownender pearlresets the change in Y, however, the teleportation itself causes 5fall damage to players.
- Eating achorus fruitresets the change in Y.[1]
- Wearing armor that isenchantedwithFeather FallingorProtectionreduces fall damage based on the level of the enchantment.
- Having theJump Booststatus effect reduces the effective change in Y by 1 block per level, e.g. falling 5 blocks with Jump Boost II counts as having fallen only 3.
- Slime blocksnegate all fall damage, but bounce the entity into the air. Both of these facts do not apply to sneaking players. Holding jump when hitting the slime block negates fall damage and stops most of the bounce
- Hay balesandhoney blocksdecrease fall damage to 20% of normal.
- Beds decrease fall damage to 50% of normal and cause the entity to bounce into the air.
- Sweet berry bushesnegate all fall damage.
- Holding sneak while landing on at least a two-block-high stack ofscaffoldingnegates fall damage from any height. Only 1 scaffolding block is needed to negate damage from smaller heights.
- Slow falling status effect completely negates all fall damage but causes the entity to fall slowly.
- Enteringpowder snowwhile falling resets the change in Y.

### Falling block
Falling block entities deal damage to players and mobs in the same block space where they land. The damage is dealt only on landing, and is not dealt to players and mobs that collide with falling block entities in mid-air.

A falling anvil deals 2 per block fallen after the first block (e.g., an anvil that falls 4 blocks deals 6 damage). A falling stalactite deals 6 per block fallen after the first block (e.g., a stalactite that falls 4 blocks deals 18 × 9 damage).

The damage is capped at 40 × 20, no matter how far the anvil or stalactite falls.

Helmets take twice as much durability damage as other armor pieces, but do not provide any special protection other than the normal armor damage reduction.[2]

If cheats are enabled, a falling block entity that deals damage can be summoned if its HurtEntities tag is set to true. The amount of damage dealt per block fallen can be customized via the FallHurtAmount tag, and the maximum damage dealt can be customized via the FallHurtMax tag.

### Thorns enchantment
When a player or mob deals melee or projectile damage to a player or mob that is wearing Thorns-enchanted armor, part of the damage is reflected back at the attacker. The amount varies with the enchantment level. (Level * 15% chance of inflicting 1–4 damage, or Level - 10 damage if level is over 10) however, thorns increases the amount of durability lost per hit on the enchanted armor.

### Suffocation
Suffocation occurs when a player or mob's eyeline is inside of certain blocks, receiving 1 damage every half-second. 

Blocks that are transparent or do not fill an entire block do not cause damage. This includes amethyst clusters, anvils, bamboo, banners, beds, bells, brewing stands, cakes, cauldrons, chains, chests, chorus flowers, chorus plants, cocoa beans, comparators, composters, daylight detectors, dragon eggs, enchanting tables, end portal frames, ender chests, fences, fence gates, flower pots, glass, grindstones, heads, honey blocks, hoppers, iron bars, leaves, lecterns, lightning rods, extended piston heads, repeaters, saplings, slabs that are not double, stairs, stonecutters, trapdoors, and walls. Despite being fully to partially transparent, barriers, beacons, ice, slime blocks, and monster spawner can cause suffocation. Dirt path and farmland can also cause suffocation, regardless of them not being full blocks.

The player's screen displays a darkened form of the block in which the player is suffocating. When the player is in third person, the view automatically switches to the first-person view.‌[Java Edition  only]

In Bedrock Edition, an oxygen bar is also present in the suffocation process. Water Breathing effects can prevent suffocation in Bedrock Edition.

The usual ways an entity can suffocate are:

- Sand,gravelorconcrete powderfalling into the space the entity occupies.
- Riding apig,boat, orminecartinto a one-block-high space.
- Riding ahorse,llama, orstriderinto a two-block-high space.
- Standing where atreejust grew from asapling, or where ahuge mushroomjust grew from amushroom.
- Standing where anend gatewayappeared after killing the dragon.
- Having a solid block pushed into the entity's head with apiston.
- Sleeping in abedsurrounded by blocks or having a solid block above it.‌[Bedrock Edition  only]
- Being teleported into a block or having one placed onto the entity viacommands(including/setblock,/fill, or/clone).
- When playing on a distant server, sometimes broken blocks can reappear due to lag, and if the player moves where the block respawned, it can provoke suffocation (for example, chopping down a tree by moving right below the trunk).
- When water and lava meet, and create acobblestone,stone, orobsidianblock on the entity's head.
- Standing a certain distance outside of theworld border, configurable with/worldborder damage buffer(default is 5 blocks).
- Summoning an entity inside a block throughspawn eggs, commands, or with agolemorwitherstructure lying down.
- Standing in 2 block deep water in snowy and cold biomes where the topmost layer of water freezes into ice
- Throwing anenderpearlin a way you end up inside a block you can suffocate in.

#### Entity cramming

  

This feature is exclusive to  Java Edition. 


In Java Edition, players and mobs take damage if too many entities are packed into the same block space. Specifically, the maxEntityCramming game rule defines the maximum number of entities that can be in a block without becoming crammed. Once the number of entities in the space of a single block exceeds this value, entity cramming occurs. When entity cramming occurs, a random selection of cram count = (entities in block) - maxEntityCramming living entities (players and mobs) become crammed. A living entity can be crammed by non-living entities, such as minecarts or armor stands, but not by block entities, such as item frames. The block space used for counting the number of entities is the axis and grid-aligned 1-meter cubic space containing the centers of the entities. An entity outside this space can collide with the entities within the space, but it can not become crammed by the entities within the space.

When crammed, a player or mob takes 6 suffocation damage every half-second, as long as that player or mob is pushing greater than that number of other entities. The default value for maxEntityCramming is 24 entities. This means that upto 24 entities can coexist in one block space without getting crammed.

If an entity is climbing, it does not count toward the number of entities in the block and does not contribute to cramming[3]. This means that climable blocks, such as ladders, vines, and scaffolding can prevent entity cramming. However, spiders and cave spiders are always counted toward the number of entities in the block when they are climbing. This can cause entities on climbable blocks to become crammed.

If a player is killed by entity cramming damage, the death message reads <player> was squished too much.

### Drowning
The oxygen bar.
A player who runs out of air underwater begins drowning, taking approximately 2 damage per second. Damage is taken when the air supply value reaches -20. Usually, the air supply value decreases each game tick. It resets to 0 after damaging. Respiration gives a chance for air supply to not decrease itself per game tick. Chance is x/(x + 1), where x is the level of enchantment.

When the game rule drowningDamage is set to false, the air supply of players deplete normally, but no drowning damage is inflicted when players run out of air.

Mobs can also drown, although most mobs that can drown attempt to swim upward. Normally, mobs can remain underwater for 15 seconds before their air supply fully depletes. They can remain underwater for 16 seconds before actually beginning to take damage.

- Asquid,glow squid,tadpole, or any kind offishsuffocates in air instead of drowning in water.
- Dolphinscan suffocate in air or drown in water and must be given access to both to survive.
- Aquatic mobs,undead mobs,iron golemsandfrogsare immune to drowning.
- Azombiedoes not take drowning damage; instead, it begins the process of converting to adrownedmob when continuously in water for 30 seconds.
- Similar to a zombie, ahuskdoes not take damage from drowning, but first converts into a zombie, which then converts to a drowned if it remains underwater.
- Piglins,piglin brutesandhoglinsdo not attempt to swim upward in water, and drown as a result.
	- Because these mobs normally zombify outside the Nether before they can start drowning, this can only happen if theirIsImmuneToZombificationtag set totrue, or that water is created in the Nether using commands.

When the player is no longer submerged in water or is in a bubble column, the air supply regenerates at a rate of 1 bubble every 0.2 seconds (4 game ticks). A Respiration helmet adds an additional on average 15 seconds duration underwater per enchantment level, and a turtle shell adds an additional 10 seconds. Water Breathing and Conduit Power regenerate the air supply. In Bedrock Edition, both effects affect squid and fish.

### Starvation
When the hunger bar becomes empty (), the player takes 1 damage every four seconds. The player stops taking starvation damage when the player eats food or the health bar drops to 10 on Easy difficulty or 1 on Normal difficulty. In Hard difficulty and on Hardcore mode, the player continues taking damage, which stops upon eating something or death by starvation.

All mobs are immune to starvation, because they do not have a hunger bar.

### Cactus
Players and mobs take 1 damage every half-second when they are touching or within the same tile-space as a cactus.

### Berry bush
Sweet berry bushes deal 1 damage for every half-second when a player or mob (besides foxes) is moving inside a sweet berry bush.

### Fire
When mobs and players without fire immunity stand on fire, they take 1 damage every half-second and get burned. Standing in soul fire does 2 damage every half-second instead. They continue burning after leaving the fire block. Fire damage can be prevented by the Fire Resistance effect. Fire duration can be decreased with the Fire Protection enchantment. Most Nether mobs are immune to fire, but they can still drown in lava.

Players do not take damage from fire if the game rule fireDamage is set to false.

### Lava
Lava is a dangerous natural occurrence. Players and mobs (except various Nether mobs) get burned and take damage from contact with lava at a rate of 4 every half-second, and they continue burning after they leave it. Fire Resistance nullifies both the direct damage from lava and the burning damage.

Players do not take damage from lava if the game rule fireDamage is set to false.

Ghasts sometimes take a dive into the lava seas in the Nether, magma cubes can hop around on lava, in a similar manner to floating. Striders can walk across lava.

### Burning
Players and many mobs burn when exposed to fire or lava or attacked by certain kinds of burning projectiles, Fire Aspect weapons, or burning zombies.‌[Java Edition  only] In addition, armor itself does not reduce burning damage; to do so, armor needs either the Fire Protection enchantment, Protection enchantment, or the Resistance status effect. Burning obstructs the player's view slightly and, unless the player or mob has Fire Resistance, inflicts damage at a rate of 1 per second. This is the same rate that the player gains health in Peaceful difficulty, so burning alone cannot kill the player in this mode. Burning lasts some amount of time depending on its cause, but it is extinguished by rain, water, or cauldrons.

Players do not take damage from burning if the game rule fireDamage is set to false.

Except for piglins, hoglins, skeletons, and endermen, mobs that spawn in the Nether do not burn and cannot be damaged by fire. Wardens also do not burn. Burning is not considered a status effect and therefore cannot be cured by milk.

### Magma block
Mobs without fire immunity and players take 1 damage every half-second if they are walking on magma blocks. This can be avoided by having the Fire Resistance effect, sneaking, or wearing Frost Walker-enchanted boots.

Players do not take damage from magma blocks if the game rule fireDamage is set to false.

### Campfire
Players or mobs standing on top of a campfire take 1 damage every half second. Standing in a Soul Campfire does 2 damage every half second instead. Unlike any other damage sources, armor itself does not reduce campfire and soul campfire damage; to do so, armor needs either the Fire Protection enchantment, Protection enchantment, or the Resistance status effect. In Bedrock Edition, it also inflicts damage for 160 game ticks (8 seconds) after the player exits the block.

Players do not take damage from campfires if the game rule fireDamage is set to false.

### Status effects
Main article: Status effect
Status effects are either helpful or harmful conditions that can be given to players and mobs alike. They can be given in different ways: being in range of thrown splash potions or lingering potions, being afflicted by certain mobs' attacks, simply being near certain mobs, being near conduits and beacons, and eating specific types of food (such as rotten flesh or raw chicken). Status effects can last for a certain amount of time, or can happen instantaneously.

Entities under a status effect emit colored particles, with the color of the particles resembling the type of status effect. Having multiple status effects combines the respective colors.

#### Instant damage
Main article: Instant Damage
Instant Damage caused by potions or tipped arrows can damage the player 6 at level I and 12 × 6 at level II.  This damage occurs instantaneously.  Undead mobs are instead healed, but are similarly damaged by the Healing effect.  Zombified piglins that are splashed by a instant damage potion do not attack the player who threw it, as it heals them.

#### Poison
Main article: Poison
Cave spiders, witches and bees poison players when they attack (except on easy difficulty). Pufferfish inflict poison as defense against players or certain mobs if they are nearby.  Poisoning also occurs upon eating a spider eye, poisonous potato, pufferfish, or suspicious stew made out of lily of the valley. Drinking or being hit by a potion or arrow of poison also results in poisoning. While poisoned, the hearts in the health meter turn from  × 10 ( × 10 on Hardcore) to an olive green ( × 10)( × 10 on Hardcore) and the player takes 1 every 25 ticks (1.25 seconds) on level I. See Poison for a table for higher levels. The Poison itself cannot kill the player, but it can reduce them to half a heart (), thus leaving them vulnerable to damage from other sources.

#### Wither
Main article: Wither (status effect)
Withers and wither skeletons inflict the Wither effect with their attacks (the wither skulls do not inflict the effect on easy difficulty). This darkens the health bar to  × 10 on Survival and  × 10 on Hardcore, while inflicting damage over time. The effect deals 1 every 2 seconds (40 ticks) for the wither skeleton's attack (level I), and every second for the Wither's skulls (level II). Wither roses also inflict the Wither effect to any mobs colliding it. Players also get the Wither effect after eating suspicious stew made out of wither rose or when hit by potion or arrow of decay.‌[Bedrock Edition and Minecraft Education  only] Unlike Poison, withering can kill on any difficulty level, and the darkened health bar makes it harder to keep track of the damage, which the only way is seeing the white spark on the left of the heart.

### Void
Main article: Void
If one were to break through the bedrock barrier found at the bottom of worlds, the void can be seen. Players in the void below the Y-axis of -64‌[Bedrock Edition  only] or -128‌[Java Edition  only] take damage at a rate of about 4 per half-second. The player usually dies from falling in the void, even in Creative or Spectator modes,‌[Java Edition  only] but the player may be saved by throwing an ender pearl before falling below the Y-axis of -64‌[Bedrock Edition  only] or -128‌[Java Edition  only].

Falling into the void in the End is more likely, and is the only way to access the void in Survival mode without exploiting glitches.

By using /effect to give the player Regeneration 5+ or Instant Health, they can fall infinitely into the void without dying until the effect wears off or the game crashes.‌[Java Edition  only]

In Bedrock Edition, the player can survive in the void in Creative mode, but there is a one-way barrier at Y=-104 to prevent falling further into the void. However, this barrier can be teleported past by teleporting the player to any location with a Y value of -106 and below. The player continues falling until the player teleports away, flies back up, or crashes the game.

### Explosions
Main article: Explosion
Explosions cause varying amounts of damage based on the explosion strength, the entity's proximity to the explosion, and whether it is obstructed by solid blocks.

### Firework rocket explosion

Firework rocket explosions can deal damage to entities if crafted with a firework star.

The maximum damage about is 6 at the explosion's center with one firework star, decreasing to 1 at the edge of a radius of 5 blocks (exclusive). Each additional firework star adds 2 to the maximum.

If a rocket crafted with a firework star is used to provide a speed boost while gliding with elytra, it explodes as it is used, dealing 7 damage to the player.

### Freezing
Freezing hearts when the player is submerged in powder snow.
When an entity is inside a powder snow block, they begin to freeze, taking damage. 

A player submerged in powder snow sees a frosty frame slowly fade in at the sides of the screen and the FOV slowly decreases. After 7 seconds (140 game ticks), the player's hearts change to a cyan frosty texture (), and the player begins taking damage at a rate of 1 HP every two seconds (40 game ticks). If the player leaves the powder snow block, the vignette slowly fades away. A frozen player moves slower than usual until the vignette fully fades away. This is controlled by the TicksFrozen data tag, which increases by 1 every game tick (to a maximum of 300) for an entity within the powder snow block. It decreases at a rate of 2 per game tick after the entity leaves the powder snow block. This is currently not a separate effect when used with commands such as /effect give freezing, and does not have its own unique art, particles, or potion. 

Players do not take damage from powder snow if the game rule freezeDamage is set to false.

Mobs and players that are freezing have a shivering animation.

Wearing any piece of leather armor stops the freezing effect and damage. This applies to entities that can wear armor, such as zombies. Horses wearing leather horse armor also don’t take damage from freezing. 

Snow golems, strays, polar bears, and withers are immune to freezing damage. Fire-related mobs like striders, magma cubes, and blazes take extra damage from freezing. A skeleton can freeze but does not take damage; instead, it begins the process of converting to a stray when continuously in powder snow for 7 seconds.

