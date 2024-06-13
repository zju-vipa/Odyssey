### Cooking
The player can place normal potato peels and any dyed potato peel on a lit frying table by using the item on it, resulting in hash browns. Corrupted potato peels can't be fried.

Player can also bake normal potatoes using the frying table, but no other food can be cooked on it.

Up to four items can be placed on a frying table, which cooks them simultaneously. Frying tables do not require any kind of fuel to cook. On a frying table, foods produce small smoke particles, indicating they are being cooked. Items take 30 seconds (600 ticks) to cook. If the frying table is extinguished while cooking food, the remaining cooking time quickly counts back up. Food items can be placed on an unlit frying table. Any items cooking on a frying table always drop when the frying table block is broken.

### Hoppers
Frying tables do not have an external inventory. Raw food cannot be loaded into the frying table with a hopper.

A hopper placed directly underneath a frying table pulls through any items dropped into the frying table . Any drops from a mob that dies in the frying table get pulled into the hopper.

### Bees
Placing a frying table under a beehive or bee nest allows players to harvest honey bottles or honeycomb without provoking the bees.
There must be unobstructed air between the frying table and the beehive or bee nest. Carpets are an exception.

### Note blocks
Frying tables can be placed under note blocks to produce "bass" sounds.

### Piston interactivity
Pistons do not interact with frying tables. Frying tables neither move nor break when pushed or pulled by pistons.

## Data values
### ID
| Name         | Identifier     | Block tags  | Translation key                |
|--------------|----------------|-------------|--------------------------------|
| Frying Table | `frying_table` | `campfires` | `block.minecraft.frying_table` |

### Block states
See also: Block states

| Name        | Default value | Allowed values                            | Description                                                                                                                    |
|-------------|---------------|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| facing      | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the frying table is facing.<br/>The opposite from the direction the player faces while placing the frying table. |
| lit         | `true`        | `false`<br/>`true`                        | Whether the frying table is lit.                                                                                               |
| signal_fire | `false`       | `false`<br/>`true`                        | Whether the frying table has ahay balebelow it.                                                                                |
| waterlogged | `false`       | `false`<br/>`true`                        | Whether or not there's water in the same place as this frying table.                                                           |

### Block data
A frying table has a block entity associated with it that holds additional data about the block.

See also: Block entity format

- Block entity data
	- 
	- Tags common to all block entities
	- CookingTimes: How long each item has been cooking, first index is slot 0, etc.
	- CookingTotalTimes: How long each item has to cook, first index is slot 0, etc.
	- Items: List of up to 4 items currently cooking.
		- 
		- Tags common to all items


