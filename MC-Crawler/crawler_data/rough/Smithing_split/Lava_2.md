#### Flow arrangement tables
##### Overworld and the End
|   |   |   | 4 |   |   |   |
|---|---|---|---|---|---|---|
|   |   | 4 | 3 | 4 |   |   |
|   | 4 | 3 | 2 | 3 | 4 |   |
| 4 | 3 | 2 | 1 | 2 | 3 | 4 |
|   | 4 | 3 | 2 | 3 | 4 |   |
|   |   | 4 | 3 | 4 |   |   |
|   |   |   | 4 |   |   |   |

| Range |        | Height in blocks |
|-------|--------|------------------|
| 1     | block  | 1                |
| 2     | blocks | 0.75-1           |
| 3     | blocks | 0.5-0.75         |
| 4     | blocks | 0.25-0.5         |

##### The Nether
|   |   |   |   |   |   |   | 8 |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   | 8 | 7 | 8 |   |   |   |   |   |   |
|   |   |   |   |   | 8 | 7 | 6 | 7 | 8 |   |   |   |   |   |
|   |   |   |   | 8 | 7 | 6 | 5 | 6 | 7 | 8 |   |   |   |   |
|   |   |   | 8 | 7 | 6 | 5 | 4 | 5 | 6 | 7 | 8 |   |   |   |
|   |   | 8 | 7 | 6 | 5 | 4 | 3 | 4 | 5 | 6 | 7 | 8 |   |   |
|   | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |   |
| 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|   | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |   |
|   |   | 8 | 7 | 6 | 5 | 4 | 3 | 4 | 5 | 6 | 7 | 8 |   |   |
|   |   |   | 8 | 7 | 6 | 5 | 4 | 5 | 6 | 7 | 8 |   |   |   |
|   |   |   |   | 8 | 7 | 6 | 5 | 6 | 7 | 8 |   |   |   |   |
|   |   |   |   |   | 8 | 7 | 6 | 7 | 8 |   |   |   |   |   |
|   |   |   |   |   |   | 8 | 7 | 8 |   |   |   |   |   |   |
|   |   |   |   |   |   |   | 8 |   |   |   |   |   |   |   |

| Range |        | Height in blocks |
|-------|--------|------------------|
| 1     | block  | 1                |
| 2     | blocks | 0.75-1           |
| 3     | blocks | 0.625-0.75       |
| 4     | blocks | 0.5-0.625        |
| 5     | blocks | 0.375-0.5        |
| 6     | blocks | 0.25-0.375       |
| 7     | blocks | 0.125-0.25       |

### Lava and water
Main article: Fluid § Mixing
Water and lava can produce stone, cobblestone, or obsidian based on how they interact. Lava can also generate basalt when above soul soil and touching blue ice.

### Light source
Lava blocks emit a light level of 15.

### Other
If there is lava flowing above a block, the lava seeps through.
Lava above a non-transparent block (does not include stairs, fences, and slabs) produces dripping particles on the underside of that block. These droplets do not do anything other than warn the player that a deluge of lava lies above that block. The particles function identically to their water counterparts, except that they drip slower.

Flowing lava can set off tripwires because it breaks placed string. Lava triggers a tripwire only once.

Any item dropped into lava is immediately destroyed, except for netherite-related items. Lodestones, however, can be destroyed by lava despite containing netherite.[1]

Lava can be placed in an empty cauldron.

If lava is above a non-transparent block supporting pointed dripstone, dripping particles are created on the end. These can fill cauldrons with lava.

## Farming
Main article: Tutorials/Lava farming
Lava farms can be created by placing a lava source block on top of a solid block and placing a pointed dripstone and a cauldron underneath it.

## Data values
### ID
Java Edition:

| Lava  | Identifier | Form  | Block tags            | Translation key        |
|-------|------------|-------|-----------------------|------------------------|
| Block | `lava`     | Block | `strider_warm_blocks` | `block.minecraft.lava` |

| Lava          | Identifier     | Fluid tags |
|---------------|----------------|------------|
| Fluid         | `lava`         | `lava`     |
| Flowing Fluid | `flowing_lava` | `lava`     |

Bedrock Edition:

| Lava       | Identifier     | Numeric ID | Form                         | Item ID[i 1]   | Translation key          |
|------------|----------------|------------|------------------------------|----------------|--------------------------|
| Flowing    | `flowing_lava` | `10`       | Block & Ungiveable Item[i 2] | Identical[i 3] | `tile.flowing_lava.name` |
| Stationary | `lava`         | `11`       | Block & Ungiveable Item[i 2] | Identical[i 3] | `tile.lava.name`         |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑ a bUnavailable with /give command
3. ↑ a bThe block's direct item form has the same id as the block.

Lava spends most of its time as stationary, rather than 'flowing' – regardless of its level, or whether it contains a current downward or to the side.  When specifically triggered by a block update, lava changes to 'flowing', update its level, then change back to stationary.  Lava springs are generated as flowing, and lava lakes are generated as stationary.

