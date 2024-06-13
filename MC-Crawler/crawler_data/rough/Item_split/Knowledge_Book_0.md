# Knowledge Book
A knowledge book is a utility item that reveals available crafting recipes to the player when used.

## Contents
- 1 Obtaining
- 2 Usage
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Item data
- 5 History
- 6 Issues
- 7 See also

## Obtaining
Knowledge books can be obtained only by using commands, as they are not found in the creative inventory.

For example, to give oneself a knowledge book that reveals the recipes for buckets and flower pots, use: /give @s minecraft:knowledge_book{Recipes:["minecraft:bucket", "minecraft:flower_pot"]}.

## Usage
Knowledge books are used to reveal recipes to the player who uses it, by adding it to their recipe book. Using a knowledge book consumes it, removing it from the player's inventory.

Knowledge books are especially useful to mapmakers in conjunction with /gamerule doLimitedCrafting true, because then any item is craftable only if its recipe is unlocked first.

## Data values
### ID
| Name           | Identifier       | Form | Translation key                 |
|----------------|------------------|------|---------------------------------|
| Knowledge Book | `knowledge_book` | Item | `item.minecraft.knowledge_book` |

### Item data
Java Edition:

Main article: Item format
Recipe books use the NBT tag Recipes to indicate the recipes they contain.

- tag: Thetagtag.

- 
	- Recipes: The list of recipes this book contains.
		- : The name of a recipe, for instanceminecraft:gold_nuggetorminecraft:gold_ingot_from_nuggets.


