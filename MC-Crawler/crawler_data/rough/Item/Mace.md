# Mace
A mace is a melee weapon that deals more damage the farther a player falls before hitting an entity with it, with successful hits completely negating the user's fall damage. It requires a heavy core to craft, only obtainable from ominous vaults, and a breeze rod dropped from breezes.

## Contents
- 1 Obtaining
	- 1.1 Crafting
	- 1.2 Repairing
		- 1.2.1 Combining
		- 1.2.2 Unit repair
- 2 Usage
	- 2.1 Attacking
	- 2.2 Base damage
		- 2.2.1 Java Edition
		- 2.2.2 Bedrock Edition
	- 2.3 Mining
	- 2.4 Enchantments
- 3 Sounds
- 4 Data values
	- 4.1 ID
- 5 Advancements
- 6 Video
- 7 History
- 8 Issues
- 9 Gallery
	- 9.1 Screenshots
- 10 References

## Obtaining
### Crafting
| Ingredients                | Crafting recipe | Description                      |
|----------------------------|-----------------|----------------------------------|
| Heavy Core+<br/>Breeze Rod |                 | ‌[upcoming: JE 1.21 & BE 1.21.0] |

### Repairing
#### Combining
| Ingredients     | Crafting recipe | Description                                                                           |
|-----------------|-----------------|---------------------------------------------------------------------------------------|
| 2× Damaged Mace |                 | Thedurabilityof the two maces is added together, plus an extra 5% durability.[verify] |

| Ingredients     | Grinding recipe | Description                                                                             |
|-----------------|-----------------|-----------------------------------------------------------------------------------------|
| 2× Damaged Mace |                 | The durability of the two maces is added together, plus an extra 5% durability.[verify] |

#### Unit repair
Main article: Anvil mechanics § Unit repair
Repair & NameDamaged Mace
A mace can be repaired in an anvil by adding breeze rods or another mace. One breeze rod restores 25% of the mace's durability.[verify]

## Usage
### Attacking
Pressing attack while holding a mace inflicts damage on both mobs and other players. Upon damaging a mob or player, the mace's durability decreases by 1.

If the player hits an entity while falling, a smash attack is performed. Note that "entity" is not restricted to mobs only. Armour stands also count as entities that a smash attack can be performed on. The smash attack is activated when the player falls more than 1.5 blocks. Upon a smash attack being performed, extra damage is dealt to the mob hit based on the distance fallen, and entities within 2.5 blocks of the player are knocked back.

When a smash attack is performed, the damage is increased by 3 plus the level of Density per block of falling distance before critical damage calculation. Smash attacks are almost always critical hits, as long as the mace has full attack cooldown, doing 50% extra damage. The amount of damage a mace can accumulate from falling is unlimited,[1] allowing a single hit from a mace to kill a player wearing full Protection IV netherite armor after falling 17 blocks, and a warden after falling 109 blocks. The damage increase from falling distance is not applied while in elytra flight.[2]

After successfully attacking a target with the mace, the player's fall damage is reset. From the height the player hit the mob, the player begins accumulating fall damage again.

Attacking a boat or a minecart with a mace instantly destroys it without decreasing the mace's durability.‌[Java Edition  only]

An interactive widget is being loaded. If this does not work for you, please reload the page or check if JavaScript is enabled.
### Base damage
Main article: Damage
#### Java Edition
Maces have an attack speed of 1.6 and take 0.625 seconds to recover. 

| Attack                            | Melee     | Melee (critical) |
|-----------------------------------|-----------|------------------|
| Attack damage                     | 7         | 10.5× 5.25       |
| Attack speed                      |           | 1.6              |
| Damage per second (DPS)           | 11.2      | 16.8             |
| Durability                        |           | 250              |
| Lifetime damage inflicted[note 1] | 1750× 875 | 2500× 1250       |

1. ↑The formula to find the total lifetime damage is Lifetime damage minimum = Durability × Damage per hit. It excludes enchantments, assumes no fall distance, and assumes the mace is at maximum charge.

#### Bedrock Edition
In Bedrock Edition, maces have no attack cooldown, and deal the following damage:

| Attack                            | Melee      | Melee (critical) |
|-----------------------------------|------------|------------------|
| Attack damage                     | 8          | 12 × 6           |
| Durability                        |            | 251              |
| Lifetime damage inflicted[note 1] | 2008× 1004 | 3012× 1506       |

1. ↑The formula to find the total lifetime damage is Durability × Damage per hit = Lifetime damage minimum. It excludes enchantments, and assumes no fall distance.

### Mining
Using a mace breaks all blocks faster than when using an empty hand. This includes blocks that do not have an assigned tool like glass, beacons, and glowstone.[more information needed]

### Enchantments
A mace can receive the following enchantments:

| Name                       | Description                                                                                                                                                                                                                           | Max level | Method                     | Weight |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|----------------------------|--------|
| Density                    | Increases the damage dealt per block fallen, increasing by 1 per level.                                                                                                                                                               | V         | Enchanting Table<br/>Anvil | 5      |
| Breach                     | Reduces the effectiveness of thearmoron the target. The armor's effectiveness is reduced by 15% per level.                                                                                                                            | IV        | Enchanting Table<br/>Anvil | 4      |
| Wind Burst                 | Emits a burst of wind (like that of awind charge) upon executing a mace smash attack on an entity, launching the attacker upward. It can be used to chain smash attacks together, and the strength of the launch increases per level. | III       | Anvil                      | 3      |
| Smite[note 1]              | Increases the damage dealt toundead.                                                                                                                                                                                                  | V         | Enchanting Table<br/>Anvil | 5      |
| Bane of Arthropods[note 1] | Increases the damage dealt toarthropods.                                                                                                                                                                                              | V         | Enchanting Table<br/>Anvil | 5      |
| Fire Aspect                | Ignites any targets hit by the mace. InBedrock Edition, it also lights unlitcandles,campfires, and blocks ofTNTwhen used.                                                                                                             | II        | Enchanting Table<br/>Anvil | 2      |
| Unbreaking                 | Grants a chance to negate durability consumption.                                                                                                                                                                                     | III       | Enchanting Table<br/>Anvil | 5      |
| Mending                    | Repairs the mace when obtainingexperience.                                                                                                                                                                                            | I         | Anvil                      | 2      |
| Curse of Vanishing         | The mace vanishes on death, not dropping as an item.                                                                                                                                                                                  | I         | Anvil                      | 1      |

1. ↑ a bSmite and Bane of Arthropods are mutually exclusive.

## Data values
### ID
Java Edition:

| Name | Identifier | Form | Translation key       |
|------|------------|------|-----------------------|
| Mace | `mace`     | Item | `item.minecraft.mace` |

Bedrock Edition:

| Name | Identifier | Numeric ID | Form | Translation key  |
|------|------------|------------|------|------------------|
| Mace | `mace`     | `322`      | Item | `item.mace.name` |

