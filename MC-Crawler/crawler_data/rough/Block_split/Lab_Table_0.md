# Lab Table
The lab table is a block used in chemistry to design one's own experiments by combining substances and observing the results.

## Contents
- 1 Obtaining
	- 1.1 Breaking
- 2 Usage
	- 2.1 Successful recipes
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Trivia
- 8 Gallery
	- 8.1 Screenshots
- 9 References

## Obtaining
Lab tables can be obtained from the Creative inventory in Minecraft Education. They cannot be obtained in Survival without commands. In Bedrock Edition, the world must also have "Education Edition" enabled.

### Breaking
A pickaxe is required to collect a lab table. If broken using a fist or any other tool, it drops nothing.

| Block     | Lab Table             |
|-----------|-----------------------|
| Hardness  | 2.5                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 12.5                  |
| Wooden    | 1.9                   |
| Stone     | 0.95                  |
| Iron      | 0.65                  |
| Diamond   | 0.5                   |
| Netherite | 0.45                  |
| Golden    | 0.35                  |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

## Usage
Using the lab table opens a 1×9 grid, where elements and compounds can be inserted to perform experiments. The locations of the items in the grid do not affect the outcome. When ready to conduct an experiment, clicking the Combine button initiates the process.

Beaker
Flask
Jar
If the result is a viable product, the top images animate to indicate whether a liquid, gas, or solid has been produced. Shortly after, the menu closes, and the successful product appears on the table. If the combined materials did not create a viable product, the process results in a garbage item and one of few animations involving fire and/or explosions. In Bedrock Edition, the table sometimes catches fire when garbage is made, burning all items and flammable blocks, so not building it near trees is recommended.

### Successful recipes
| Result                | Materials needed                 |
|-----------------------|----------------------------------|
| <br/>Bleach           |                                  |
|                       | Water x3, Sodium Hypochlorite x3 |
| <br/>Heat Block       |                                  |
|                       | Iron, Water, Charcoal, Salt      |
| <br/>Ice Bomb         |                                  |
|                       | Sodium Acetate x4                |
| <br/>Super Fertilizer |                                  |
|                       | Ammonia, Phosphorus              |

## Data values
### ID
| Name      | Identifier        | Numeric ID | Form                       | Item ID[i 1]   | Translation key      |
|-----------|-------------------|------------|----------------------------|----------------|----------------------|
| Lab Table | `chemistry_table` | `238`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.labtable.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

| Name                 | Metadata Bits   | Default value      | Allowed values              | Values forMetadata Bits     | Description                                                                           |
|----------------------|-----------------|--------------------|-----------------------------|-----------------------------|---------------------------------------------------------------------------------------|
| chemistry_table_type | `0x1`<br/>`0x2` | `compound_creator` | `compound_creator`          | `0`                         | Compound Creator                                                                      |
|                      |                 |                    | `element_constructor`       | `2`                         | Element Constructor                                                                   |
|                      |                 |                    | `lab_table`                 | `3`                         | Lab Table                                                                             |
|                      |                 |                    | `material_reducer`          | `1`                         | Material Reducer                                                                      |
| direction            | `0x4`<br/>`0x8` | `0`                | `0`<br/>`1`<br/>`2`<br/>`3` | `0`<br/>`1`<br/>`2`<br/>`3` | The direction the block's front is.0: north<br/>1: east<br/>2: south<br/>3: west<br/> |




