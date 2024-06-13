### Farming
Main article: Tutorials/Cactus farming
Cacti naturally grow to a height of three blocks, adding a block of height when the top cactus block has received 16 random ticks (i.e. on average every 18 minutes, but the actual rate can vary widely). Bone meal does not work on cacti to speed their growth.[2] A cactus does not need light to grow and is non-flammable. If a cactus has space directly above it, it grows even if the newly-grown block would immediately break due to adjacent blocks.

### Smelting ingredient
| Name      | Ingredients    | Smelting recipe | Description              |
|-----------|----------------|-----------------|--------------------------|
| Green Dye | Cactus+Anyfuel | 1               | ‌[Java Edition  only][3] |
| Green Dye | Cactus+Anyfuel | 0.2             | ‌[Bedrock Edition  only] |

### Breeding
Cacti can be used to breed camels and reduce the remaining growth duration of baby camels by 10%. Camels also follow a player holding a cactus.

### Composting
Placing a cactus into a composter has a 50% chance of raising the compost level by 1.

## Data values
### ID
Java Edition:

| Name   | Identifier | Form         | Block tags        | Translation key        |
|--------|------------|--------------|-------------------|------------------------|
| Cactus | cactus     | Block & Item | enderman_holdable | block.minecraft.cactus |

Bedrock Edition:

| Name   | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key  |
|--------|------------|------------|----------------------------|----------------|------------------|
| Cactus | cactus     | 81         | Block & Giveable Item[i 2] | Identical[i 3] | tile.cactus.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block states

Java Edition

| Name | Default value | Allowed values         | Description                                                                                                                                                                                              |
|------|---------------|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| age  | 0             | 0123456789101112131415 | A freshly-planted cactus – and a cactus that has just grown cactus above it – each have an age of 0.The age is incremented at random intervals.At age 15, a cactus may try to grow more cactus above it. |

Bedrock Edition

| Name | Metadata Bits | Default value | Allowed values         | Values forMetadata Bits | Description                                                                                                                                                                                              |
|------|---------------|---------------|------------------------|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| age  | 0x10x20x40x8  | 0             | 0123456789101112131415 | 0123456789101112131415  | A freshly-planted cactus – and a cactus that has just grown cactus above it – each have an age of 0.The age is incremented at random intervals.At age 15, a cactus may try to grow more cactus above it. |




