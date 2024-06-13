### Weapon
A pickaxe loses 2 points of durability when used as a weapon. Pickaxes may be used as a weapon, and in Java Edition, they have an attack speed higher than that of an axe, shovel, or trident, but lower than that of a sword or mace.

#### Java Edition
Pickaxes have an attack speed of 1.2 and take 0.83 seconds to recover.

| Material                          | Wooden   | Gold   | Stone        | Iron     | Diamond         | Netherite    |
|-----------------------------------|----------|--------|--------------|----------|-----------------|--------------|
| Attack Damage                     | 2        | 2      | 3            | 4        | 5               | 6            |
| Attack Speed                      | 1.2      | 1.2    | 1.2          | 1.2      | 1.2             | 1.2          |
| Damage/Second (DPS)               | 2.4      | 2.4    | 3.6          | 4.8      | 6               | 7.2          |
| Durability                        | 59       | 32     | 131          | 250      | 1561            | 2031         |
| Lifetime damage inflicted[note 1] | 59× 29.5 | 32× 16 | 196.5× 98.25 | 500× 250 | 3902.5× 1951.25 | 6093× 3046.5 |

1. ↑The formula to find the total lifetime damage is ceil(durability ÷ 2) × damage per hit. The durability is halved then ceiled because hoes take double durability when used as a weapon, and the last 1 durability can also deal damage. The formula also ignores enchantments and critical hits, and assumes each attack is performed at maximum charge.

#### Bedrock Edition
In Bedrock Edition, pickaxes have no attack cooldown, and deal the following damage:

| Material                          | Wooden | Gold   | Stone    | Iron       | Diamond    | Netherite  |
|-----------------------------------|--------|--------|----------|------------|------------|------------|
| Attack Damage                     | 3      | 3      | 4        | 5          | 6          | 7          |
| Durability                        | 60     | 33     | 132      | 251        | 1562       | 2032       |
| Lifetime damage inflicted[note 1] | 90× 45 | 48× 24 | 264× 132 | 625× 312.5 | 4686× 2343 | 7112× 3556 |

### Enchantments
A pickaxe can receive the following enchantments:

| Name               | Description                                             | Max Level | Method                     | Weight |
|--------------------|---------------------------------------------------------|-----------|----------------------------|--------|
| Efficiency         | Increases the mining speed.                             | V         | Enchanting Table<br/>Anvil | 10     |
| Fortune[note 2]    | Increases the amount ofdropswhen mining.                | III       | Enchanting Table<br/>Anvil | 2      |
| Silk Touch[note 2] | Causes blocks to drop themselves when mined.            | I         | Enchanting Table<br/>Anvil | 1      |
| Unbreaking         | Grants a chance to negate durability consumption.       | III       | Enchanting Table<br/>Anvil | 5      |
| Mending            | Repairs the pickaxe when obtainingexperience.           | I         | Anvil                      | 2      |
| Curse of Vanishing | The pickaxe vanishes on death, not dropping as an item. | I         | Anvil                      | 1      |

1. ↑The formula to find the total lifetime damage is ceil(durability ÷ 2) × damage per hit. The durability is halved then ceiled because hoes take double durability when used as a weapon, and the last 1 durability can also deal damage. The formula also ignores enchantments and critical hits, and assumes each attack is performed at maximum charge.
2. ↑ a bSilk Touch and Fortune are mutually exclusive

### Fuel
Wooden pickaxes can be used as a fuel in furnaces, smelting 1 item per wooden pickaxe.

### Smelting ingredient
| Name                          | Ingredients                                    | Smelting recipe |
|-------------------------------|------------------------------------------------|-----------------|
| Iron Nuggetor<br/>Gold Nugget | Iron Pickaxeor<br/>Golden Pickaxe+<br/>Anyfuel | 0.1             |

### Piglins
Piglins are attracted to golden pickaxes and run toward any golden pickaxes on the ground, and inspect it for 6 to 8 seconds before putting it in their inventory.

## Data values
### ID
Java Edition:

| Name              | Identifier          | Form | Translation key                    |
|-------------------|---------------------|------|------------------------------------|
| Wooden Pickaxe    | `wooden_pickaxe`    | Item | `item.minecraft.wooden_pickaxe`    |
| Stone Pickaxe     | `stone_pickaxe`     | Item | `item.minecraft.stone_pickaxe`     |
| Iron Pickaxe      | `iron_pickaxe`      | Item | `item.minecraft.iron_pickaxe`      |
| Diamond Pickaxe   | `diamond_pickaxe`   | Item | `item.minecraft.diamond_pickaxe`   |
| Golden Pickaxe    | `golden_pickaxe`    | Item | `item.minecraft.golden_pickaxe`    |
| Netherite Pickaxe | `netherite_pickaxe` | Item | `item.minecraft.netherite_pickaxe` |

Bedrock Edition:

| Name              | Identifier          | Numeric ID | Form | Translation key               |
|-------------------|---------------------|------------|------|-------------------------------|
| Wooden Pickaxe    | `wooden_pickaxe`    | `310`      | Item | `item.wooden_pickaxe.name`    |
| Stone Pickaxe     | `stone_pickaxe`     | `314`      | Item | `item.stone_pickaxe.name`     |
| Iron Pickaxe      | `iron_pickaxe`      | `297`      | Item | `item.iron_pickaxe.name`      |
| Diamond Pickaxe   | `diamond_pickaxe`   | `318`      | Item | `item.diamond_pickaxe.name`   |
| Golden Pickaxe    | `golden_pickaxe`    | `324`      | Item | `item.golden_pickaxe.name`    |
| Netherite Pickaxe | `netherite_pickaxe` | `606`      | Item | `item.netherite_pickaxe.name` |


