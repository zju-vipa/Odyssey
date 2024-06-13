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

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Crafting
| Ingredients                                                    | Crafting recipe |
|----------------------------------------------------------------|-----------------|
| Iron Ingot+<br/>Crafting Table+<br/>Redstone Dust+<br/>Dropper |                 |

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

## Data values
### ID
Java Edition:

| Name    | Identifier | Form         | Block tags                                | Translation key           |
|---------|------------|--------------|-------------------------------------------|---------------------------|
| Crafter | `crafter`  | Block & Item | `mineable/pickaxe`<br/>`needs_stone_tool` | `block.minecraft.crafter` |

| Name         | Identifier |
|--------------|------------|
| Block entity | `crafter`  |

Bedrock Edition:

| Name    | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key     |
|---------|------------|------------|----------------------------|----------------|---------------------|
| Crafter | `crafter`  | `-313`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.crafter.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

| Name         | Savegame ID |
|--------------|-------------|
| Block entity | `Crafter`   |

### Block states
See also: Block states

Java Edition:

| Name        | Default value | Allowed values                                                                                                                                                                    | Description                                                           |
|-------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| crafting    | `false`       | `false`<br/>`true`                                                                                                                                                                | Whether the crafter's mouth is open and top is glowing.               |
| orientation | `north_up`    | `down_east`<br/>`down_north`<br/>`down_south`<br/>`down_west`<br/>`east_up`<br/>`north_up`<br/>`south_up`<br/>`up_east`<br/>`up_north`<br/>`up_south`<br/>`up_west`<br/>`west_up` | The direction the crafter'sfaceis facing and which way it is rotated. |
| triggered   | `false`       | `false`<br/>`true`                                                                                                                                                                | Whether the crafter is activated.                                     |

Bedrock Edition:

| Name          | Metadata Bits | Default value | Allowed values                                                                                                                                                                    | Values forMetadata Bits | Description                                                           |
|---------------|---------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|-----------------------------------------------------------------------|
| crafting      | Not Supported | `false`       | `false`<br/>`true`                                                                                                                                                                | `Unsupported`           | Whether the crafter's mouth is open and top is glowing.               |
| orientation   | Not Supported | `down_east`   | `down_east`<br/>`down_north`<br/>`down_south`<br/>`down_west`<br/>`east_up`<br/>`north_up`<br/>`south_up`<br/>`up_east`<br/>`up_north`<br/>`up_south`<br/>`up_west`<br/>`west_up` | `Unsupported`           | The direction the crafter'sfaceis facing and which way it is rotated. |
| triggered_bit | Not Supported | `false`       | `false`<br/>`true`                                                                                                                                                                | `Unsupported`           | Whether the crafter is activated.                                     |



### Block data
A crafter has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format

- Block entity data
	- 
	- Tags common to all block entities
	- crafting_ticks_remaining: Set to 6 when the crafter crafts something.[more information needed]
	- triggered: Set to 1 when it is powered. It is otherwise 0.
	- disabled_slots: Indexes of slots that are disabled.
	- Items: List of items in this container.
		- : An item in the crafter, including the slot tag. Crafter slots are numbered 0-8. 0 starts in the top left corner.
			- 
			- Tags common to all items
	- 
	- Lock: Optional. When not blank, prevents the container from being opened unless the opener is holding an item whose name matches this string.
	- 
	- LootTable: Optional. Name of the loot table to use. If this is used in a chest-like container, the loot table generates its content when it is opened. Generating the items in the container removes both loot table tags (LootTableandLootTableSeed).
	- LootTableSeed: Optional. Seed for generating the loot table. The default value works similarly to the seeds for worlds, where value of0or an omitted value causes the game to use a random seed.

Bedrock Edition:

SeeBedrock Edition level format/Block entity format.
