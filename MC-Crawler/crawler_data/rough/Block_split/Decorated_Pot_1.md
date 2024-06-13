### Storage
A decorated pot can store up to a stack of a single type of item. Unlike other containers, decorated pots have no GUI; items are inserted by interacting with the pot or by using droppers or hoppers. The only ways to retrieve stored items is by breaking the pot or by using hoppers and minecarts with hopper.

Decorated pots crafted without sherds can also serve as compact storage for bricks, as they are stackable, each can be crafted from four bricks and can be broken down into four bricks.

A redstone comparator can be used to measure the number of stored items.

## Data values
### ID
Java Edition:

| Name          | Identifier      | Form         | Translation key                 |
|---------------|-----------------|--------------|---------------------------------|
| Decorated Pot | `decorated_pot` | Block & Item | `block.minecraft.decorated_pot` |

| Name         | Identifier      |
|--------------|-----------------|
| Block entity | `decorated_pot` |

Bedrock Edition:

| Name          | Identifier      | Numeric ID | Form                       | Item ID[i 1]   | Translation key           |
|---------------|-----------------|------------|----------------------------|----------------|---------------------------|
| Decorated Pot | `decorated_pot` | `-551`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.decorated_pot.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

| Name         | Savegame ID    |
|--------------|----------------|
| Block entity | `DecoratedPot` |

### Block states
See also: Block states

Java Edition:

| Name        | Default value | Allowed values                            | Description                                                                                                                            |
|-------------|---------------|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| facing      | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction a decorated pot faces in.                                                                                                |
| cracked     | `false`       | `false`<br/>`true`                        | If true, the pot always makes shatter sounds upon breaking.<br/>The value is set to true immediately before being shattered by a tool. |
| waterlogged | `false`       | `false`<br/>`true`                        | Whether or not there's water in the same place as this decorated pot.                                                                  |

Bedrock Edition: [more information needed]



### Block data
A decorated pot has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format

- Block entity data
	- 
	- Tags common to all block entities
	- sherds: List ofsherdson this decorated pot.
		- :Item IDof this face. Each value defaults tobricks's ID, and can be either a brick or any sherd.
	- item: The item stored within the pot. A decorated pot does not useSlotto describe its contents, even though it functionally has 1 item slot.
		- 
		- Tags common to all items
	- 
	- Tags common to all objects that use loot tables to produce items

Bedrock Edition:

SeeBedrock Edition level format/Block entity format.

