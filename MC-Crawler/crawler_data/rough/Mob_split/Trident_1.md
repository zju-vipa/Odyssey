### Damage
Thrown tridents and splashes deal 8 damage. The damage remains the same regardless of the trident's speed. It has a faster charging speed than a bow or crossbow (barring the Quick Charge enchantment.)

#### Java Edition
In Java Edition, tridents have an attack speed of 1.1 and take ~0.91 seconds to recover.

| Attack                            | Melee      | Melee (critical) | Range      |
|-----------------------------------|------------|------------------|------------|
| Attack damage                     | 9          | 13.5× 6.75       | 8          |
| Attack Speed                      |            | 1.0              | N/A        |
| Damage/Second (DPS)               | 9.9        | 14.3             | ?          |
| Lifetime damage inflicted[note 1] | 2250× 1125 | 3375× 1687.5     | 2000× 1000 |
| Durability                        |            |                  | 250        |

1. ↑The formula to find the total lifetime damage is Durability × Damage per hit = Lifetime damage minimum (e.g., 250 × 9 = 2250). It ignores enchantments, and assumes the trident is at maximum charge

#### Bedrock Edition
In Bedrock Edition, tridents have no attack cooldown and do the following damage:

| Attack                            | Melee        | Melee (critical) | Range      |
|-----------------------------------|--------------|------------------|------------|
| Attack damage                     | 9            | 13.5× 6.75       | 8          |
| Lifetime damage inflicted[note 1] | 2259× 1129.5 | 3388× 1694       | 2008× 1004 |
| Durability                        |              |                  | 251        |

1. ↑The formula to find the total lifetime damage is Durability × Damage per hit = Lifetime damage minimum. It excludes enchantments and critical hits.

### Elytra
A trident with the Riptide enchantment can be used to propel a player with a pair of elytra, but only in rainy weather, during snowy weather in certain biomes[5] or while the player is in a body of water. A Riptide trident can boost the player to speeds as high as 125 blocks per second,[6] much faster than the 33.5 blocks-per-second speed achievable using firework rockets.

### Impaling damage
In Java Edition, the Impaling enchantment deals extra damage to all water mobs. In Bedrock Edition and in Java Edition Combat Test 3, it deals extra damage to all players and mobs in water or rain.

| Level | Increase        | Melee       | Ranged      |
|-------|-----------------|-------------|-------------|
| I     | adds 2.5× 1.25  | 11.5× 5.75  | 10.5× 5.25  |
| II    | adds 5          | 14× 7       | 13× 6.5     |
| III   | adds 7.5× 3.75  | 16.5× 8.25  | 15.5× 7.75  |
| IV    | adds 10         | 19× 9.5     | 18× 9       |
| V     | adds 12.5× 6.25 | 21.5× 10.75 | 20.5× 10.25 |


### Enchantments
Tridents have a base enchantability of 1 and can receive the following enchantments:

| Name               | Description                                                                                   | Max Level | Method                     | Weight |
|--------------------|-----------------------------------------------------------------------------------------------|-----------|----------------------------|--------|
| Loyalty[note 1]    | Causes the trident to return after landing.                                                   | III       | Enchanting Table<br/>Anvil | 5      |
| Channeling[note 1] | Releases a bolt of lightning when the trident lands during athunderstorm.                     | I         | Enchanting Table<br/>Anvil | 1      |
| Riptide[note 1]    | Replaces the throw with a charge that hurls the user forward when wet.                        | III       | Enchanting Table<br/>Anvil | 2      |
| Impaling           | Increases the damage dealt to aquatic‌[Java Edition  only]or wet‌[Bedrock Edition  only]mobs. | V         | Enchanting Table<br/>Anvil | 2      |
| Unbreaking         | Grants a chance to negate durability consumption.                                             | III       | Enchanting Table<br/>Anvil | 5      |
| Mending            | Repairs the trident when obtainingexperience.                                                 | I         | Anvil                      | 2      |
| Curse of Vanishing | The trident vanishes on death, not dropping as an item.                                       | I         | Anvil                      | 1      |

** Notes **
1. ↑ a b cLoyalty and Channeling are mutually exclusive with Riptide, but not from each other.

## Data values
### ID
Java Edition:

| Name    | Identifier | Form | Translation key          |
|---------|------------|------|--------------------------|
| Trident | `trident`  | Item | `item.minecraft.trident` |

| Name    | Identifier | Entity tags          | Translation key            |
|---------|------------|----------------------|----------------------------|
| Trident | `trident`  | `impact_projectiles` | `entity.minecraft.trident` |

Bedrock Edition:

| Name    | Identifier | Numeric ID | Form | Translation key     |
|---------|------------|------------|------|---------------------|
| Trident | `trident`  | `546`      | Item | `item.trident.name` |

| Name    | Identifier       | Numeric ID | Translation key              |
|---------|------------------|------------|------------------------------|
| Trident | `thrown_trident` | `73`       | `entity.thrown_trident.name` |

### Entity data
Tridents have entity data associated with them that contain various properties of the entity.

Java Edition:

Main article: Entity format
- Entity data
	- 
	- Tags common to all arrows
	- 
	- Tags common to all entities
	- 
	- Tags common to all projectiles
	- DealtDamage: 1 or 0 (true/false) - true if the trident has already damaged an entity or been stuck in the ground for more than 4 ticks, in which case subsequent collisions with entities deal no damage and Loyalty tridents begin to return to the player.
	- item: The tag representing the item that is given when the entity is picked up.
		- 
		- Tags common to all items

Bedrock Edition:

SeeBedrock Edition level format/Entity format.

