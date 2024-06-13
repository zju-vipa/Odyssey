# Compound Creator
A compound creator is a block used in chemistry. It allows over thirty compounds to be created by combining elements. This includes certain items which are available in the game normally.

## Contents
- 1 Obtaining
- 2 Usage
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Gallery
	- 7.1 Screenshots
- 8 References

## Obtaining
A compound creator can be mined using a pickaxe. Mining without a pickaxe is slow, but the compound creator still drops as an item.

| Block     | Compound Creator      |
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

Compound creators cannot be obtained in Survival without commands. In Bedrock Edition, the world must also have “Education Edition” enabled.

## Usage
Main article: Compound
Using the compound creator opens up a 3×3 grid, where elements can be inserted to create compounds. By inputting the appropriate type and number of elements, the creator outputs the component in the slot to the right of the grid. All compound recipes are shapeless, and unlike the crafting table, the stack sizes are taken into consideration. Also, unlike with most blocks with an interface, the elements are not consumed.

## Data values
### ID
| Name             | Identifier        | Numeric ID | Form                       | Item ID[i 1]   | Translation key             |
|------------------|-------------------|------------|----------------------------|----------------|-----------------------------|
| Compound Creator | `chemistry_table` | `238`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.compoundcreator.name` |

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



