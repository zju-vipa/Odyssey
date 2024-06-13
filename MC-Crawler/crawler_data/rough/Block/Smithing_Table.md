# Smithing Table
A smithing table is a utility block used to alter tools and armor at the cost of a smithing template and the appropriate material. This process keeps all enchantments of the altered item. This is the only way to obtain trimmed armor or upgrade diamond equipment with netherite. It also serves as a toolsmith's job site block.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
- 2 Usage
	- 2.1 Placement
	- 2.2 Smithing
	- 2.3 Changing profession
	- 2.4 Fuel
	- 2.5 Note blocks
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
- 5 Achievements
- 6 Advancements
- 7 History
- 8 Issues
- 9 Trivia
- 10 References
- 11 External links

## Obtaining
Smithing tables can be either found or crafted.

### Breaking
Smithing tables can be broken using any tool or by hand, but an axe is the fastest.

| Block     | Smithing Table        |
|-----------|-----------------------|
| Hardness  | 2.5                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 3.75                  |
| Wooden    | 1.9                   |
| Stone     | 0.95                  |
| Iron      | 0.65                  |
| Diamond   | 0.5                   |
| Netherite | 0.45                  |
| Golden    | 0.35                  |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
Smithing tables can spawn naturally within toolsmith houses in villages. They may also spawn in trail ruins.

### Crafting
| Ingredients               | Crafting recipe |
|---------------------------|-----------------|
| Iron Ingot+<br/>AnyPlanks |                 |

## Usage
### Placement
Regardless of the player's position during placement, the different textures of the block are always facing in the same position (the textures with the hammers are facing west and east, while the dark grey side is always facing up).

### Smithing
The GUI for the smithing table.
Main article: Smithing
A smithing table is primarily used for upgrading diamond gear to netherite gear and for trimming armor. The smithing interface is accessed by pressing use on a smithing table.

Each time working a smithing table, the player must provide a smithing template in the left-most slot, armor/tool in the central slot, and an augmenting material in the right-most slot. Working at smithing table costs no experience, and item data such as durability, enchantments, and custom names are preserved. 

Upgrading to netherite requires a netherite upgrade smithing template, a diamond tool or a piece of diamond armor, and a netherite ingot.

| Ingredients                                          | Smithing recipe |
|------------------------------------------------------|-----------------|
| Netherite Upgrade +Any Diamond Gear +Netherite Ingot | Upgrade Gear    |

Decorative trims can be applied to any piece of armor - including turtle shells - by using an armor trim smithing template and a trim material. After trimming, the armor will show a decorative pattern corresponding to the smithing template with the color determined by the used material. A preview of this pattern can be seen on an armor stand model, located on the right side of smithing table's GUI.

| Ingredients                                        | Smithing recipe |
|----------------------------------------------------|-----------------|
| Any Armor Trim +Any Armor Piece +Any trim material | Upgrade Gear    |

### Changing profession
If a village contains a smithing table that has not been claimed by a villager, any villager who hasn't already chosen a job site block has a chance to change their profession to toolsmith. If a villager with this profession has already been traded with, it cannot change jobs.

### Fuel
Smithing tables can be used as fuel in furnaces, smelting 1.5 items per block.

### Note blocks
Smithing tables can be placed under note blocks to produce "bass" sounds.

## Data values
### ID
Java Edition:

| Name           | Identifier       | Form         | Translation key                  |
|----------------|------------------|--------------|----------------------------------|
| Smithing Table | `smithing_table` | Block & Item | `block.minecraft.smithing_table` |

Bedrock Edition:

| Name           | Identifier       | Numeric ID | Form                       | Item ID[i 1]   | Translation key            |
|----------------|------------------|------------|----------------------------|----------------|----------------------------|
| Smithing Table | `smithing_table` | `457`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.smithing_table.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

