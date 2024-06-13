### Breeding
Like other seeds, pumpkin seeds can be used to breed chickens, lead chickens around, and make baby chickens grow up faster by 10% of the remaining time.

### Taming
Like other seeds, pumpkin seeds can be used to tame parrots.

### Composting
Placing pumpkin seeds into a composter has a 30% chance of raising the compost level by 1.

## Pumpkin stem
A pumpkin stem is the block that is planted on farmland when pumpkin seeds are used on it. It starts underground, and rises up as the plant grows. The stem is colored green when young, and then yellow once fully grown.

The stem curves once a pumpkin has grown from it. A fully-grown single stem connects to any pumpkin in an adjacent square, thus there are 5 possible appearances to a stem. If there are multiple pumpkins it can connect to, it favors the east, then west, north, and south. When the pumpkin is removed, the stem returns to its straight shape.

## Data values
### ID
Java Edition:

| Name                  | Identifier            | Form  | Block tags         | Translation key                       |
|-----------------------|-----------------------|-------|--------------------|---------------------------------------|
| Pumpkin Stem          | pumpkin_stem          | Block | bee_growablescrops | block.minecraft.pumpkin_stem          |
| Attached Pumpkin Stem | attached_pumpkin_stem | Block | None               | block.minecraft.attached_pumpkin_stem |
| Pumpkin Seeds         | pumpkin_seeds         | Item  | —                  | item.minecraft.pumpkin_seeds          |

Bedrock Edition:

| Name          | Identifier    | Numeric ID | Form                         | Item ID[i 1]   | Translation key         |
|---------------|---------------|------------|------------------------------|----------------|-------------------------|
| Pumpkin Stem  | pumpkin_stem  | 104        | Block & Ungiveable Item[i 2] | Identical[i 3] | tile.pumpkin_stem.name  |
| Pumpkin Seeds | pumpkin_seeds | 292        | Item                         | —              | item.pumpkin_seeds.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Unavailable with /give command

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block states

Java Edition:
Growing

| Name | Default value | Allowed values | Description                                         |
|------|---------------|----------------|-----------------------------------------------------|
| age  | 0             | 0              | A newly planted stem.                               |
|      |               | 123456         | Intermediate growth stages of the stem.             |
|      |               | 7              | A fully mature stem, capable of producing pumpkins. |

Attached

| Name   | Default value | Allowed values     | Description                                 |
|--------|---------------|--------------------|---------------------------------------------|
| facing | north         | eastnorthsouthwest | The direction from the stem to the pumpkin. |

Bedrock Edition:

| Name             | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                         |
|------------------|---------------|---------------|----------------|-------------------------|-----------------------------------------------------|
| growth           | 0x10x20x4     | 0             | 0              | 0                       | A newly planted stem.                               |
|                  |               |               | 123456         | 123456                  | Intermediate growth stages of the stem.             |
|                  |               |               | 7              | 7                       | A fully mature stem, capable of producing pumpkins. |
| facing_direction | Not Supported | 0             | 01             | Unsupported             | Unused                                              |
|                  |               |               | 2              | Unsupported             | Stem pointing north.                                |
|                  |               |               | 3              | Unsupported             | Stem pointing south.                                |
|                  |               |               | 4              | Unsupported             | Stem pointing west.                                 |
|                  |               |               | 5              | Unsupported             | Stem pointing east.                                 |




