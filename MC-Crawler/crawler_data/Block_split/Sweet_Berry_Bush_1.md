### Trading
Master-level butcher villagers offer to buy 10 sweet berries for an emerald.

### Entity movement
A sweet berry bush (at any stage) slows down all entities (except items) passing through it. At stage 1 and higher, it causes damage. Foxes are immune to both characteristics, however. Sweet berry bushes deal 1 damage every 0.5 seconds, only if the entity is moving in the hitbox of the bush. Entities that move through sweet berry bushes slow down to about 34.05% of their normal speed, similar to how a cobweb slows down mobs to 15% of normal speed. This makes it impossible to jump a full block while inside the bush.

Mobs at standard block height in a minecart are not damaged when the minecart is pushed through sweet berries. Players in a sweet berry bush take no damage except from horizontal movement, but are unable to jump out of the bush, similar to a cobweb.

### Bees
Bees do not pollinate sweet berry bushes.

## Data values
### ID
Java Edition:

| Name             | Identifier       | Form  | Block tags                          | Item tags | Translation key                  |
|------------------|------------------|-------|-------------------------------------|-----------|----------------------------------|
| Sweet Berry Bush | sweet_berry_bush | Block | azalea_log_replaceablebee_growables | —         | block.minecraft.sweet_berry_bush |
| Sweet Berries    | sweet_berries    | Item  | —                                   | fox_food  | item.minecraft.sweet_berries     |

Bedrock Edition:

| Name             | Identifier       | Numeric ID | Form                         | Item ID[i 1]   | Translation key            |
|------------------|------------------|------------|------------------------------|----------------|----------------------------|
| Sweet Berry Bush | sweet_berry_bush | 462        | Block & Ungiveable Item[i 2] | Identical[i 3] | tile.sweet_berry_bush.name |
| Sweet Berries    | sweet_berries    | 287        | Item                         | —              | item.sweet_berries.name    |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Unavailable with /give command

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block states

Java Edition:

| Name | Default value | Allowed values | Description                                                                  |
|------|---------------|----------------|------------------------------------------------------------------------------|
| age  | 0             | 0              | Young plant                                                                  |
|      |               | 1              | No berries                                                                   |
|      |               | 2              | Some berries,usingthe bush gives 1–2sweet berriesand sets the age back to 1. |
|      |               | 3              | Full berries,usingthe bush gives 2–3sweet berriesand sets the age back to 1. |

Bedrock Edition:

| Name   | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                                                     |
|--------|---------------|---------------|----------------|-------------------------|---------------------------------------------------------------------------------|
| growth | 0x1           | 0             | 0              | 0                       | Young plant                                                                     |
|        |               |               | 1              | 1                       | No berries                                                                      |
|        |               |               | 2              | 2                       | Some berries,usingthe bush gives 1–2sweet berriesand sets the growth back to 2. |
|        |               |               | 3              | 3                       | Full berries,usingthe bush gives 2–3sweet berriesand sets the growth back to 2. |




