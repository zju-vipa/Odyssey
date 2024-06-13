# Armor materials
Armor materials refer to the material that an armor item uses.

## Contents
- 1 Materials
- 2 Affected items
- 3 Other mechanics
- 4 See also

## Materials
There are currently seven armor materials in the game: leather, chainmail, iron, gold, diamond, netherite, and turtle. The armor material of an item determines its durability multiplier, armor values, enchantability, sound events, toughness, knockback resistance, and repair items.

| Material Name  | Durability Multiplier[n 1] | Defense Points |       |      |      | Enchantability | Sound Event Type             |        | Toughness | Knockback Resistance | Repair Item     |
|----------------|----------------------------|----------------|-------|------|------|----------------|------------------------------|--------|-----------|----------------------|-----------------|
|                |                            | Head           | Chest | Legs | Feet |                | ID                           | Sounds |           |                      |                 |
| Leather        | 5                          | 1              | 3     | 2    | 1    | 15             | `item.armor.equip_leather`   |        | 0         | 0                    | Leather         |
| Chainmail[n 2] | 15                         | 2              | 5     | 4    | 1    | 12             | `item.armor.equip_chain`     |        | 0         | 0                    | Iron Ingot      |
| Iron           | 15                         | 2              | 6     | 5    | 2    | 9              | `item.armor.equip_iron`      |        | 0         | 0                    | Iron Ingot      |
| Turtle[n 3]    | 25                         | 2              | 6     | 5    | 2    | 9              | `item.armor.equip_turtle`    |        | 0         | 0                    | Scute           |
| Gold           | 7                          | 2              | 5     | 3    | 1    | 25             | `item.armor.equip_gold`      |        | 0         | 0                    | Gold Ingot      |
| Diamond        | 33                         | 3              | 8     | 6    | 3    | 10             | `item.armor.equip_diamond`   |        | 2         | 0                    | Diamond         |
| Netherite      | 37                         | 3              | 8     | 6    | 3    | 15             | `item.armor.equip_netherite` |        | 3         | 0.1                  | Netherite Ingot |

1. ↑The durability multiplier multiplies each item slot's base durability. The base values are: 11 for head, 16 for chest, 15 for legs, 13 for feet.
2. ↑Referred to as both "chain" and "chainmail" in the code.
3. ↑Although the turtle material is currently used only by turtle shells, it has unused protection values for other armor slots.

## Affected items
All helmets, chestplates, leggings, and boots use their respective armor materials. Turtle shells use the turtle material.

## Other mechanics
Other mechanics in the game use these materials for various purposes.

- Piglinsare neutral towards players wearing gold armor.
- Players and other entities wearing leather armor do not freeze when inpowdered snow, and do not fall through powdered snow when wearing leather boots.

