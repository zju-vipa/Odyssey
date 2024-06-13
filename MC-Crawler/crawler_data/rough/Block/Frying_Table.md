# Frying Table
A frying table is a block which is used to cook potatoes and fry potato peels, turning them into hash browns.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
- 2 Usage
	- 2.1 Particles and smoke signals
	- 2.2 Damage
	- 2.3 Cooking
	- 2.4 Hoppers
	- 2.5 Bees
	- 2.6 Note blocks
	- 2.7 Piston interactivity
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
	- 4.3 Block data
- 5 Trivia
- 6 History
- 7 Issues

## Obtaining
### Breaking
A frying table can be broken using any tool with equal efficiency, and always drops itself.

| Block     | Frying Table          |
|-----------|-----------------------|
| Hardness  | 2                     |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 3                     |
| Wooden    | 1.5                   |
| Stone     | 0.75                  |
| Iron      | 0.5                   |
| Diamond   | 0.4                   |
| Netherite | 0.35                  |
| Golden    | 0.25                  |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
Frying tables generate naturally as part of potato villages.

### Crafting
| Ingredients                                               | Crafting recipe |
|-----------------------------------------------------------|-----------------|
| Stick+<br/>Iron Ingot+<br/>Gold Nugget+<br/>Potato Planks |                 |

## Usage
Unlike campfires, frying tables do not produce light.

Frying tables are lit by default when placed. They can be manually lit using flint and steel (either by player or dispenser), fire charges, shooting it with a flaming arrow, or fireball projectiles when /gamerule mobGriefing is true.

A frying table can be extinguished by waterlogging it, throwing a splash water bottle at it, or using a shovel on it. Frying tables can not be lit from their bottom face. As with torches, rain does not extinguish frying tables.

Using flint and steel on the side of a lit or waterlogged frying table sets the adjacent air block on fire instead.

### Particles and smoke signals
Frying tables produce smoke particles that float up around 10 blocks before disappearing. If a hay bale is placed below, the frying table becomes a signal fire and the smoke floats up 24 blocks instead.

Frying table smoke particles can partially pass through a block directly above it, but do not pass through blocks more than one block directly above it.

Although a trap door is thinner than a slab, a trap door can block the smoke completely, preventing the smoke from floating up.

Frying tables emit extra smoke particles during rain, similar to lava.

Frying tables also emit occasional ember particles, similar to lava.

### Damage
Frying tables cannot damage players, but do damage mobs standing on top of them even if underwater (with exceptions such as shulkers, zombified piglins or guardians), but only if lit. Frying tables deal 1 (although damage immunity reduces this to once every half-second) Frying tables do not cause lasting burning or destroy items. Damage taken is considered fire damage and is reduced by armor (which loses durability), the Resistance effect, and the Protection and Fire Protection enchantments. The player can avoid being damaged at all, either by using a potion of Fire Resistance or wearing Frost Walker boots.

Regardless of height, all blocks prevent damage done to mobs or players above frying tables. The frying table deals damage only to entities occupying its block.

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

