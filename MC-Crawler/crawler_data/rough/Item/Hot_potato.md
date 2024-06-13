# Hot potato
A hot potato is an item which damages players who hold it in 24w14potato.

## Contents
- 1 Obtaining
	- 1.1 Crafting
- 2 Usage
	- 2.1 Damage
	- 2.2 Food
	- 2.3 Crafting ingredient
- 3 Sounds
- 4 Data values
	- 4.1 ID
- 5 History

## Obtaining
Throwing a potato, poisonous potato, or a baked potato into lava turns it into hot potato. The hot potato retains data from the original potato, such as its custom name, or how many times it has been lubricated.

### Crafting
| Ingredients                   | Crafting recipe |
|-------------------------------|-----------------|
| Baked Potato+<br/>Lava Bucket |                 |

## Usage
### Damage
Each hot potato stores a heat value. This value starts from 0 and goes up by 1 every tick it is in a player's inventory to a maximum of 200. Once the heat value reaches 20 and the potato is in a player's inventory, the player begins taking damage. Based on the heat value, a player takes between 1 and 5 damage each tick. However, due to damage immunity, the player only actually takes damage every 10 game ticks (0.5 seconds).

Fire Resistance does not prevent the player from taking damage from happening. If there are multiple hot potatoes in a player's inventory, the effect is the same as if there was only one. Hot potatoes do not damage other entities if they hold the item.

### Food
When a hot potato is consumed, the player is set on fire for 16940 ticks, or 847 seconds.

### Crafting ingredient
| Ingredients                                    | Crafting recipe |
|------------------------------------------------|-----------------|
| Poisonous Potato+<br/>Floatato+<br/>Hot potato |                 |

## Data values
### ID
Java Edition:

| Name       | Identifier   | Form | Translation key             |
|------------|--------------|------|-----------------------------|
| Hot potato | `hot_potato` | Item | `item.minecraft.hot_potato` |

