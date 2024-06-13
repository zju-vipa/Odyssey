### Hoppers
Campfires do not have an external inventory. Raw food cannot be loaded into the campfire with a hopper.

A hopper placed directly underneath a campfire pulls through any items dropped into the campfire. Any drops from a mob that dies in the campfire get pulled into the hopper.

### Bees
Placing a campfire under a beehive or bee nest allows players to harvest honey bottles or honeycomb without provoking the bees.
There must be unobstructed air between the campfire and the beehive or bee nest. Carpets are an exception.‌[Java Edition  only]

### Light source
Standard lit campfires emit a light level of 15. Like most other sources of light, campfires melt nearby snow and ice.

### Note blocks
Campfires can be placed under note blocks to produce "bass" sounds.

### Piston interactivity
In Bedrock Edition, pushing a campfire with a piston or sticky piston breaks it. Campfires cannot be pulled by sticky pistons.

In Java Edition, pistons do not interact with campfires. Campfires neither move nor break when pushed or pulled by pistons.

## Data values
### ID
Java Edition:

| Name     | Identifier | Form         | Block tags  | Translation key            |
|----------|------------|--------------|-------------|----------------------------|
| Campfire | `campfire` | Block & Item | `campfires` | `block.minecraft.campfire` |

| Name         | Identifier |
|--------------|------------|
| Block entity | `campfire` |

Bedrock Edition:

| Campfire | Identifier | Numeric ID | Form                         | Item ID[i 1]    | Translation key      |
|----------|------------|------------|------------------------------|-----------------|----------------------|
| Block    | `campfire` | `464`      | Block & Ungiveable Item[i 2] | `item.campfire` | `tile.campfire.name` |
| Item     | `campfire` | `589`      | Item                         | —               | `tile.campfire.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Unavailable with /give command

| Name         | Savegame ID |
|--------------|-------------|
| Block entity | `Campfire`  |

### Block states
See also: Block states

Java Edition:

| Name        | Default value | Allowed values                            | Description                                                                                                            |
|-------------|---------------|-------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| facing      | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the campfire is facing.<br/>The opposite from the direction the player faces while placing the campfire. |
| lit         | `true`        | `false`<br/>`true`                        | Whether the campfire is lit.                                                                                           |
| signal_fire | `false`       | `false`<br/>`true`                        | Whether the campfire has ahay balebelow it.                                                                            |
| waterlogged | `false`       | `false`<br/>`true`                        | Whether or not there's water in the same place as this campfire.                                                       |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values                            | Values forMetadata Bits | Description                                                                                                            |
|------------------------------|---------------|---------------|-------------------------------------------|-------------------------|------------------------------------------------------------------------------------------------------------------------|
| extinguished                 | `0x4`         | `false`       | `false`<br/>`true`                        | `0`<br/>`1`             | Whether the campfire is put out.                                                                                       |
| minecraft:cardinal_direction | Not Supported | `south`       | `east`<br/>`north`<br/>`south`<br/>`west` | `Unsupported`           | The direction the campfire is facing.<br/>The opposite from the direction the player faces while placing the campfire. |



### Block data
A campfire has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format

- Block entity data
	- 
	- Tags common to all block entities
	- CookingTimes: How long each item has been cooking, first index is slot 0, etc.
	- CookingTotalTimes: How long each item has to cook, first index is slot 0, etc.
	- Items: List of up to 4 items currently cooking.
		- 
		- Tags common to all items

Bedrock Edition:

SeeBedrock Edition level format/Block entity format.

