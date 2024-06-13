#### Java Edition
Shovels have an attack speed of 1 and take 1 second to recover.

| Material                          | Wooden      | Gold      | Stone         | Iron          | Diamond           | Netherite         |
|-----------------------------------|-------------|-----------|---------------|---------------|-------------------|-------------------|
| Attack Damage                     | 2.5× 1.25   | 2.5× 1.25 | 3.5× 1.75     | 4.5× 2.25     | 5.5× 2.75         | 6.5× 3.25         |
| Attack Speed                      | 1           | 1         | 1             | 1             | 1                 | 1                 |
| Damage/Second (DPS)               | 2.5         | 2.5       | 3.5           | 4.5           | 5.5               | 6.5               |
| Durability                        | 59          | 32        | 131           | 250           | 1561              | 2031              |
| Lifetime damage inflicted[note 1] | 72.5× 36.25 | 40× 20    | 227.5× 113.75 | 562.5× 281.25 | 4292.75× 2146.375 | 6600.75× 3300.375 |

1. ↑The formula to find the total lifetime damage is ceil(durability ÷ 2) × damage per hit. The durability is halved then ceiled because hoes take double durability when used as a weapon, and the last 1 durability can also deal damage. The formula also ignores enchantments and critical hits, and assumes each attack is performed at maximum charge.

#### Bedrock Edition
In Bedrock Edition, shovels have no attack cooldown, and deal the following damage:

| Material                          | Wooden | Gold     | Stone   | Iron     | Diamond      | Netherite  |
|-----------------------------------|--------|----------|---------|----------|--------------|------------|
| Attack Damage                     | 2      | 2        | 3       | 4        | 5            | 6          |
| Durability                        | 60     | 33       | 132     | 251      | 1562         | 2032       |
| Lifetime damage inflicted[note 1] | 60× 30 | 33× 16.5 | 198× 99 | 502× 251 | 3905× 1952.5 | 6096× 3048 |

### Enchantments
A shovel can receive the following enchantments:

| Name               | Description                                            | Max Level | Method                     | Weight |
|--------------------|--------------------------------------------------------|-----------|----------------------------|--------|
| Efficiency         | Increases the mining speed.                            | V         | Enchanting Table<br/>Anvil | 10     |
| Fortune[note 2]    | Increases the amount ofdropswhen mining.               | III       | Enchanting Table<br/>Anvil | 2      |
| Silk Touch[note 2] | Causes blocks to drop themselves when mined.           | I         | Enchanting Table<br/>Anvil | 1      |
| Unbreaking         | Grants a chance to negate durability consumption.      | III       | Enchanting Table<br/>Anvil | 5      |
| Mending            | Repairs the shovel when obtainingexperience.           | I         | Anvil                      | 2      |
| Curse of Vanishing | The shovel vanishes on death, not dropping as an item. | I         | Anvil                      | 1      |

1. ↑The formula to find the total lifetime damage is ceil(durability ÷ 2) × damage per hit. The durability is halved then ceiled because hoes take double durability when used as a weapon, and the last 1 durability can also deal damage. The formula also ignores enchantments and critical hits, and assumes each attack is performed at maximum charge.
2. ↑ a bSilk Touch and Fortune are mutually exclusive

### Fuel
Wooden shovels can be used as a fuel in furnaces, smelting 1 item per shovel.

### Smelting ingredient
| Name                          | Ingredients                                  | Smelting recipe |
|-------------------------------|----------------------------------------------|-----------------|
| Iron Nuggetor<br/>Gold Nugget | Iron Shovelor<br/>Golden Shovel+<br/>Anyfuel | 0.1             |

### Piglins
Piglins are attracted to golden shovels and run toward any golden shovels on the ground, and inspect it for 6 to 8 seconds before putting it in their inventory.

## Data values
### ID
Java Edition:

| Name             | Identifier         | Form | Translation key                   |
|------------------|--------------------|------|-----------------------------------|
| Wooden Shovel    | `wooden_shovel`    | Item | `item.minecraft.wooden_shovel`    |
| Stone Shovel     | `stone_shovel`     | Item | `item.minecraft.stone_shovel`     |
| Iron Shovel      | `iron_shovel`      | Item | `item.minecraft.iron_shovel`      |
| Diamond Shovel   | `diamond_shovel`   | Item | `item.minecraft.diamond_shovel`   |
| Golden Shovel    | `golden_shovel`    | Item | `item.minecraft.golden_shovel`    |
| Netherite Shovel | `netherite_shovel` | Item | `item.minecraft.netherite_shovel` |

Bedrock Edition:

| Name             | Identifier         | Numeric ID | Form | Translation key              |
|------------------|--------------------|------------|------|------------------------------|
| Wooden Shovel    | `wooden_shovel`    | `309`      | Item | `item.wooden_shovel.name`    |
| Stone Shovel     | `stone_shovel`     | `313`      | Item | `item.stone_shovel.name`     |
| Iron Shovel      | `iron_shovel`      | `296`      | Item | `item.iron_shovel.name`      |
| Diamond Shovel   | `diamond_shovel`   | `317`      | Item | `item.diamond_shovel.name`   |
| Golden Shovel    | `golden_shovel`    | `323`      | Item | `item.golden_shovel.name`    |
| Netherite Shovel | `netherite_shovel` | `605`      | Item | `item.netherite_shovel.name` |


