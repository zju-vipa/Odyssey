# Chain
Chains are metallic decoration blocks.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Chest loot
	- 1.4 Crafting
- 2 Usage
	- 2.1 Crafting ingredient
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Trivia
- 8 Gallery
	- 8.1 Renders
	- 8.2 Screenshots
- 9 References

## Obtaining
### Breaking
Chains can be mined using any pickaxe. If mined without a pickaxe, they drop nothing.

| Block     | Chain                 |
|-----------|-----------------------|
| Hardness  | 5                     |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 25                    |
| Wooden    | 3.75                  |
| Stone     | 1.9                   |
| Iron      | 1.25                  |
| Diamond   | 0.95                  |
| Netherite | 0.85                  |
| Golden    | 0.65                  |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
Chains generate in bastion remnants and sometimes in ruined portals that generate in the Nether. They always generate above magma cube spawners, also found in bastions.

Chains can also generate in mineshafts. They generate on the sides of a wooden bridge (a mid-air corridor) when the distance between the bridge and the highest solid block below it is higher than the distance to the lowest solid block above it. Chains here generate vertically in a pillar between the bridge and the ceiling. The lowest block of the pillar, connecting the chain to the bridge, is always an oak fence.

### Chest loot
| Item  | Structure       | Container     | Quantity | Chance                         |
|-------|-----------------|---------------|----------|--------------------------------|
|       |                 |               |          | Java EditionandBedrock Edition |
| Chain | Bastion Remnant | Generic chest | 2–10     | 24.4%                          |

### Crafting
| Ingredients                 | Crafting recipe |
|-----------------------------|-----------------|
| Iron Nugget+<br/>Iron Ingot |                 |

## Usage
Chains can be used to suspend bells, hanging signs, lanterns, and soul lanterns, as the chain texture connects to the chain of the lantern seamlessly as if it were part of it, and it connects the hanging sign chains together. Chains do not require a supporting block to be placed whether it is on the top, next to it or at the bottom. It can exist completely free-standing in mid air[1] and it can be rotated. Chains connect horizontally or vertically, but not across different orientations (so a chain with N orientation does not connect to a chain with E orientation in the adjacent block).
Horizontal chains one block above a surface may be walked over. Horizontal chains two blocks above a surface prevent players from traveling past them. Vertical chains block travel if targeted directly, but may be skirted.

Precision is required, but chains can be walked on, allowing for inconspicuous, although somewhat costly, bridges.

Chains can be pushed by pistons without being broken.

in Bedrock Edition chain is not conductive, but the comparator can work in being separated from the measured block by a chain.

### Crafting ingredient
| Name         | Ingredients                                                                                | Crafting recipe |
|--------------|--------------------------------------------------------------------------------------------|-----------------|
| Hanging Sign | Chain+<br/>MatchingStripped Logor<br/>Block of Stripped Bambooor<br/>MatchingStripped Stem | 66666666666     |

## Data values
### ID
Java Edition:

| Name  | Identifier | Form         | Translation key         |
|-------|------------|--------------|-------------------------|
| Chain | `chain`    | Block & Item | `block.minecraft.chain` |

Bedrock Edition:

| Chain | Identifier | Numeric ID | Form                         | Item ID[i 1] | Translation key   |
|-------|------------|------------|------------------------------|--------------|-------------------|
| Block | `chain`    | `541`      | Block & Ungiveable Item[i 2] | `item.chain` | `tile.chain.name` |
| Item  | `chain`    | `619`      | Item                         | —            | `tile.chain.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Unavailable with /give command

### Block states
See also: Block states

Java Edition:

| Name        | Default value | Allowed values     | Description                                                   |
|-------------|---------------|--------------------|---------------------------------------------------------------|
| axis        | `y`           | `x`                | The chain is oriented east–west.                              |
|             |               | `y`                | The chain is oriented vertically.                             |
|             |               | `z`                | The chain is oriented north–south.                            |
| waterlogged | `false`       | `false`<br/>`true` | Whether or not there's water in the same place as this chain. |

Bedrock Edition:

| Name        | Metadata Bits   | Default value | Allowed values | Values forMetadata Bits | Description                        |
|-------------|-----------------|---------------|----------------|-------------------------|------------------------------------|
| pillar_axis | `0x1`<br/>`0x2` | `y`           | `x`            | `1`                     | The chain is oriented east–west.   |
|             |                 |               | `y`            | `0`                     | The chain is oriented vertically.  |
|             |                 |               | `z`            | `2`                     | The chain is oriented north–south. |




