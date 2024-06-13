# Crafter
A crafter is a low-capacity storage block used for automatic crafting. Its inventory acts as a crafting table that crafts when it is powered, ejecting the crafted item (or items) from its "mouth" into the world or into a container it is facing. Its inventory slots can be individually locked to prevent hoppers, droppers, etc. from filling them; crafting recipes treat locked slots as empty of items.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Crafting
- 2 Usage
	- 2.1 Container
	- 2.2 Redstone component
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
	- 4.3 Block data
- 5 Advancements
- 6 History
- 7 Issues
- 8 Gallery
	- 8.1 Screenshots
	- 8.2 Development images
	- 8.3 Concept artwork
- 9 References

## Obtaining
### Breaking
| Block     | Crafter               |
|-----------|-----------------------|
| Hardness  | 1.5                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 2.25                  |
| Wooden    | 1.15                  |
| Stone     | 0.6                   |
| Iron      | 0.4                   |
| Diamond   | 0.3                   |
| Netherite | 0.25                  |
| Golden    | 0.2                   |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


### Crafting
| Ingredients                                     | Crafting recipe |
|-------------------------------------------------|-----------------|
| Iron Ingot+Crafting Table+Redstone Dust+Dropper |                 |

## Usage
Crafters cannot be moved by pistons.‌[Java Edition  only]

The crafter's GUI in Java Edition.
A simple contraption for crafting cake using the crafter
### Container
A crafter has nine slots of inventory space, arranged in a 3-by-3 grid like a crafting table. Its GUI can be accessed by using it.

A slot can be enabled or disabled, which can be toggled by clicking on it when empty. Disabled slots cannot have items put in them.

Hoppers, droppers and other crafters interact with crafters by inserting items into its inventory; hoppers can remove ingredients as well. The added items are distributed from the top left to the bottom right of the enabled slots if there is an empty slot, if the crafter has all item slots filled then items are added to the lowest count item stack of the same type.[1] Hoppers and droppers can interact with all sides of the crafter, and prioritize filling empty spaces, followed by the smallest stack of the item.

### Redstone component
When a crafter receives a redstone signal, it waits for 2 redstone ticks (4 game ticks, or 0.2 seconds barring lag) before ejecting one crafted item using the ingredients from the nine inventory slots. The crafted items are subsequently spit out from the front of the crafter. If the front of a crafter is facing a container (including another crafter), the crafted items are transferred into the container. If the container it is facing is full, or the item cannot be inserted into the container, the crafter spits out the item instead. Crafters interact with containers similar to droppers. If a recipe has byproducts (e.g. empty bottles for honey blocks or empty buckets for cake) those are ejected after the crafted item.

For shaped recipes, the position of the items in the inventory matters. Because disabled slots prevent items from entering the slot, crafters can be used to craft any item in the game automatically without any input from the player, using a series of hoppers and/or droppers and the correct configuration of disabled slots for the recipe.

A hopper placed below a crafter collects the ingredients from the crafting grid, not the resulting item.

In Java Edition, unlike dispensers and droppers, crafters aren't affected by quasi-connectivity.

Comparators can emit a redstone signal when reading from a crafter. The signal strength is equal to the number of crafting slots that are either disabled or occupied by an item. [2] The stack size of the item has no effect on the comparators output signal e.g. having 1 stick in a slot vs having 64 sticks in that same slot both output the same comparator signal. An empty crafter with no disabled slots does not output any signal through a comparator. A crafter with every slot being disabled or containing an item (of any stack size) outputs a signal strength of nine through a comparator.

