### Fuel
Lecterns can be used as fuel in furnaces to smelt 1.5 items.

### Note blocks
Lecterns can be placed under note blocks to produce "bass" sound.

## Data values
### ID
Java Edition:

| Name    | Identifier | Form         | Translation key         |
|---------|------------|--------------|-------------------------|
| Lectern | lectern    | Block & Item | block.minecraft.lectern |

| Name         | Identifier |
|--------------|------------|
| Block entity | lectern    |

Bedrock Edition:

| Name    | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key   |
|---------|------------|------------|----------------------------|----------------|-------------------|
| Lectern | lectern    | 449        | Block & Giveable Item[i 2] | Identical[i 3] | tile.lectern.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


| Name         | Savegame ID |
|--------------|-------------|
| Block entity | Lectern     |

### Block states
See also: Block states

Java Edition:

| Name     | Default value | Allowed values     | Description                                                                                                     |
|----------|---------------|--------------------|-----------------------------------------------------------------------------------------------------------------|
| facing   | north         | eastnorthsouthwest | The direction the lectern is facing.The opposite from the direction the player faces while placing the lectern. |
| has_book | false         | falsetrue          | If the lectern currently has a book.                                                                            |
| powered  | false         | falsetrue          | If the lectern is currently outputting a redstone signal.                                                       |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values     | Values forMetadata Bits | Description                                                                                                     |
|------------------------------|---------------|---------------|--------------------|-------------------------|-----------------------------------------------------------------------------------------------------------------|
| minecraft:cardinal_direction | Not Supported | south         | eastnorthsouthwest | Unsupported             | The direction the lectern is facing.The opposite from the direction the player faces while placing the lectern. |
| powered_bit                  | 0x4           | false         | falsetrue          | 01                      | If the lectern is currently outputting a redstone signal.                                                       |



### Block data
A lectern has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format


 Block entity data
Tags common to all block entities
 Book: The book item, without the slot tag, currently on the lectern, may not exist.
Tags common to all items
 Page: The page the book is currently on, starting from 0, does not exist if there's no book. Value is clamped between 0 and the last page - 1.

Bedrock Edition:

See Bedrock Edition level format/Block entity format.

