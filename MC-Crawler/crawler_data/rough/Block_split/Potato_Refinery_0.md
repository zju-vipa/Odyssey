# Potato Refinery
A potato refinery is a block used for extracting oil from potatoes and poisonous potatoes as well as lubricating items in 24w14potato.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Crafting
- 2 Usage
	- 2.1 Refining
		- 2.1.1 Oil extraction
		- 2.1.2 Lubrication
	- 2.2 Piston interactivity
	- 2.3 Note blocks
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

## Obtaining
### Breaking
Potato refineries have no assigned tool and never drop as an item, even with Silk Touch.

| Block    | Potato Refinery     |
|----------|---------------------|
| Hardness | 3.5                 |
|          | Breakingtime (secs) |
| Default  | 5.25                |

### Crafting
| Ingredients         | Crafting recipe |
|---------------------|-----------------|
| Baked Potato Bricks |                 |

## Usage
### Refining
The interface in-game
A potato refinery has four slots: a fuel slot, two item slots, and an output slot. In the fuel slot, up to a stack of any fuel can be placed. The two item slots can hold up to a stack of any item.

Like furnaces, different types of fuel smelt a different number of items. If the refinery is not currently using a piece of fuel and is ready to refine, a new piece of fuel is used.

#### Oil extraction
If the refinery has fuel, nothing in the output slot, a potato in the first item slot, and at least one empty glass bottle in the second item slot, the refining process begins. After 100 game ticks (5 seconds), a potato and glass bottle are used, and a bottle of potato oil is produced. If a poisonous potato was used in the first item slot, a bottle of poisonous potato oil is created.

#### Lubrication
If the refinery has fuel, nothing in the output slot, a bottle of regular (non-poisonous) potato oil in the first item slot, and any item in the second item slot, the refinery is activated. After 125 game ticks (6.25 seconds), the bottle of potato oil and the item are used. The output is an item with a lubrication factor. The higher the lubrication factor, the more the item slides around when on the ground. An item can be lubricated multiple times, but with diminishing returns.

### Piston interactivity
Potato refineries cannot be pushed or pulled by pistons.

### Note blocks
Potato refineries can be placed under note blocks to produce "base drum" sounds.

## Data values
### ID
| Name            | Identifier        | Translation key                   |
|-----------------|-------------------|-----------------------------------|
| Potato Refinery | `potato_refinery` | `block.minecraft.potato_refinery` |

### Block states
See also: Block states

| Name   | Default value | Allowed values                            | Description                                                                                                                                |
|--------|---------------|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the potato refinery's opening faces.<br/>The opposite from the direction the player faces while placing the potato refinery. |
| lit    | `false`       | `false`<br/>`true`                        | If the potato refinery is lit.                                                                                                             |

### Block data
A potato refinery has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format

- Block entity data
	- 
	- Tags common to all block entities
	- BurnTime: Number of ticks left before the current fuel runs out.
	- CookTime: Number of ticks the item has been refining for. An item being lubricated finishes when CookTime reaches 20 ticks (1 second), while oil extraction takes 100 ticks (5 seconds). Is reset to 0 if BurnTime reaches 0.
	- CookTimeTotal: Number of ticks It takes for the item to be cooked.
	- 
	- Tags common to all objects that can be renamed
	- Items: List of items in this container.
		- : An item in the potato refinery, including the slot tag:Slot 0: The item(s) in the top left slot.Slot 1: The item(s) to use as the next fuel source.Slot 2: The item(s) in the top right slot.Slot 3: The item(s) in the output slot.
			- 
			- Tags common to all items
	- 
	- Tags common to all containers that can be locked


