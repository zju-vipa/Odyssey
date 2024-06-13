## Data values
### ID
Java Edition:

| Name      | Identifier | Form         | Translation key           |
|-----------|------------|--------------|---------------------------|
| Dispenser | dispenser  | Block & Item | block.minecraft.dispenser |

| Name         | Identifier |
|--------------|------------|
| Block entity | dispenser  |

Bedrock Edition:

| Name      | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key     |
|-----------|------------|------------|----------------------------|----------------|---------------------|
| Dispenser | dispenser  | 23         | Block & Giveable Item[i 2] | Identical[i 3] | tile.dispenser.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


| Name         | Savegame ID |
|--------------|-------------|
| Block entity | Dispenser   |

### Block states
See also: Block states

Java Edition:

| Name      | Default value | Allowed values           | Description                                                                                                                   |
|-----------|---------------|--------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| facing    | north         | downeastnorthsouthupwest | The direction in which contents are shot or dropped.The opposite from the direction the player faces while placing the block. |
| triggered | false         | falsetrue                | True if this block is activated.                                                                                              |

Bedrock Edition:

| Name             | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                                                                                                                   |
|------------------|---------------|---------------|----------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| facing_direction | 0x10x20x4     | 0             | 01234567       | 01234567                | The direction in which contents are shot or dropped.0: facing down 1: facing up 2: facing north 3: facing south 4: facing west 5: facing east |
| triggered_bit    | 0x8           | false         | falsetrue      | 01                      | True if this block is activated.                                                                                                              |



### Block data
A dispenser has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format


 Block entity data
Tags common to all block entities
Tags common to all objects that can be renamed
 Items: List of items in this container.
: An item, including the slot tag. Dispenser slots are numbered 0-8 with 0 in the top left corner.
Tags common to all items
Tags common to all containers that can be locked
Tags common to all objects that use loot tables to produce items

Bedrock Edition:

See Bedrock Edition level format/Block entity format.
## See also
Some other blocks can also be used to move items:

- Dropperscan throw items or push them into adjacent containers.
- Hopperscan push items into adjacent containers.
- Iceandpacked icehave reduced friction to the item entity movement.
- Slime blockscan impart velocity to item entities when pushed by a piston.
- Watercan push item entities.
- Quasi-connectivityapplies to dispensers.


