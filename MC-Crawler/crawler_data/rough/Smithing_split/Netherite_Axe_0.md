# Netherite Axe
A netherite axe is the sixth tier of axe the player can obtain. It can be used to cut down trees faster, but also as a melee weapon, and it can disable shields.

## Contents
- 1 Obtaining
	- 1.1 Upgrading
	- 1.2 Repairing
		- 1.2.1 Combining
		- 1.2.2 Anvil repair
- 2 Usage
	- 2.1 Breaking
	- 2.2 Stripping
		- 2.2.1 Copper blocks
	- 2.3 Weapon
		- 2.3.1 Java Edition
		- 2.3.2 Bedrock Edition
	- 2.4 Enchantments
- 3 Sounds
- 4 Data values
	- 4.1 ID
- 5 Achievements
- 6 Advancements
- 7 History
- 8 Issues
- 9 References

## Obtaining
### Upgrading
Like other diamond tools, a diamond axe can be upgraded to a netherite axe, increasing its durability and slightly increasing its mining speed and attack damage, as well as granting resistance to fire and lava when dropped as an item.

| Ingredients                                     | Smithing recipe |
|-------------------------------------------------|-----------------|
| Netherite Upgrade +Diamond Axe +Netherite Ingot | Upgrade Gear    |

### Repairing
#### Combining
| Ingredients           | Crafting recipe | Description                                                                             |
|-----------------------|-----------------|-----------------------------------------------------------------------------------------|
| Damaged Netherite Axe |                 | The durability of the two axes is added together, plus an extra 3 points of durability. |

| Ingredients              | Grinding recipe | Description                                                                             |
|--------------------------|-----------------|-----------------------------------------------------------------------------------------|
| 2× Damaged Netherite Axe |                 | The durability of the two axes is added together, plus an extra 3 points of durability. |

#### Anvil repair
Main article: Anvil mechanics § Unit repair
Repair & NameNetherite Axe
A netherite axe can be repaired in an anvil by adding netherite ingots, with each ingot restoring 25% of the axe's maximum durability, rounded down. Two netherite axes can also be combined in an anvil. Both methods preserve the axe's enchantments.

## Usage
### Breaking
Netherite axes can break wood-related blocks faster than other tools. Breaking a block costs 1 durability.[note 1]

1. ↑Blocks that break instantly don't use up durability.

### Stripping
Using a netherite axe on a log, wood block, or block of bamboo turns it into a stripped log, stripped wood, or block of stripped bamboo, respectively. This costs 1 point of durability of the axe.

#### Copper blocks
Using a netherite axe on a waxed or oxidized copper block removes the wax if it has any, or otherwise remove a level of oxidization. This costs 1 point of durability.

### Weapon
When used as a weapon, a netherite axe loses 2 durability points.

#### Java Edition
Attacking a shield user with an axe disables the use of the shield for 5 seconds. Vindicators, piglin brutes, or other mobs with commands always disable the player's shield. Damage done when using an axe as a weapon is more than that of a sword of the same tier, though they take longer than a sword to recover, resulting in lower DPS.

| Attack Damage | Attack Speed | Recovery time           | DPS  | Lifetime damage inflicted[note 1] |
|---------------|--------------|-------------------------|------|-----------------------------------|
| 10            | 1.0          | 1 second (20game ticks) | 10.0 | 10160× 5080                       |

1. ↑The formula to find the total lifetime damage is ceil(durability ÷ 2) × damage per hit. The durability is halved then ceiled because axes take double durability when used as a weapon, and the last 1 durability can also deal damage. The formula also ignores enchantments and critical hits, and assumes each attack is performed at maximum charge.

#### Bedrock Edition
Netherite axes attack instantly with no cooldown and deal 8 damage, but they lower the durability of armor and shields faster than a sword would do.

### Enchantments
A netherite axe can receive the following enchantments:

| Name                                              | Description                                                                                    | Max Level | Method                                           | Weight |
|---------------------------------------------------|------------------------------------------------------------------------------------------------|-----------|--------------------------------------------------|--------|
| Efficiency                                        | Increases the mining speed.                                                                    | V         | Enchanting Table<br/>Anvil                       | 10     |
| Fortune[note 1]                                   | Increases the amount ofdropswhen mining.                                                       | III       | Enchanting Table<br/>Anvil                       | 2      |
| Silk Touch[note 1]                                | Causes blocks to drop themselves when mined.                                                   | I         | Enchanting Table<br/>Anvil                       | 1      |
| Sharpness[note 2]                                 | Increases the damage dealt.                                                                    | V         | Enchanting Table‌[upcoming: JE 1.20.5]<br/>Anvil | 10     |
| Smite[note 2]                                     | Increases the damage dealt toundead.                                                           | V         | Enchanting Table‌[upcoming: JE 1.20.5]<br/>Anvil | 5      |
| Bane of Arthropods[note 2]                        | Increases the damage dealt toarthropods.                                                       | V         | Enchanting Table‌[upcoming: JE 1.20.5]<br/>Anvil | 5      |
| Cleaving‌[upcoming: JE Combat Tests][note 2]      | Increases the damage and shield cooldown time dealt.                                           | III       | Enchanting Table<br/>Anvil                       |        |
| Looting‌[upcoming: JE Combat Tests][note 3]       | Increases the amount ofdropswhen killing an entity with the axe.                               | III       | Anvil                                            | 2      |
| Knockback‌[upcoming: JE Combat Tests][note 3]     | Increases the knockback dealt.                                                                 | II        | Anvil                                            | 5      |
| Fire Aspect‌[upcoming: JE Combat Tests][note 3]   | Ignites any targets hit by the axe and lights unlitcandles,campfires, andBlock of TNTwhenused. | II        | Anvil                                            | 2      |
| Sweeping Edge‌[upcoming: JE Combat Tests][note 3] | Increases the sweeping damage dealt.                                                           | III       | Anvil                                            | 2      |
| Unbreaking                                        | Grants a chance to negate durability consumption.                                              | III       | Enchanting Table<br/>Anvil                       | 5      |
| Mending                                           | Repairs the axe when obtainingexperience.                                                      | I         | Anvil                                            | 2      |
| Curse of Vanishing                                | The axe vanishes on death, not dropping as an item.                                            | I         | Anvil                                            | 1      |

1. ↑ a bSilk Touch and Fortune are mutually exclusive
2. ↑ a b c dSharpness, Smite, Bane of Arthropods, and Cleaving‌[upcoming: JE Combat Tests] are mutually exclusive.
3. ↑ a b c dFire Aspect, Looting, Knockback, and Sweeping Edge currently exist, but they can be used only for swords.

## Data values
### ID
Java Edition:

| Name          | Identifier      | Form | Translation key                |
|---------------|-----------------|------|--------------------------------|
| Netherite Axe | `netherite_axe` | Item | `item.minecraft.netherite_axe` |

Bedrock Edition:

| Name          | Identifier      | Numeric ID | Form | Translation key           |
|---------------|-----------------|------------|------|---------------------------|
| Netherite Axe | `netherite_axe` | `607`      | Item | `item.netherite_axe.name` |


