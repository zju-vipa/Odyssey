# Element Constructor
The element constructor is a block used in chemistry. It allows the construction of elements by adjusting the number of protons, electrons and neutrons.

## Contents
- 1 Breaking
- 2 Usage
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Gallery
	- 7.1 Screenshots
- 8 References

## Breaking
An element constructor can be mined using a pickaxe. Mining without a pickaxe is very slow, but the element constructor still drops as an item.[1]

| Block     | Element Constructor   |
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

Element constructors cannot be obtained in Survival without commands. In Bedrock Edition, the world must also have “Education Edition” enabled.

## Usage
The interface of an element constructor.
Main article: Elements
Using the element constructor opens up an interface with a large display and three adjustable sliders for protons, neutrons and electrons, as well as optional text inputs for each. By moving the sliders or typing in numbers into the text inputs, the large display shows the selected numbers of particles. There is a microscope icon at the left of the interface, and the inventory is shown at the bottom right of the user interface.

Constructed elements and isotopes can be removed from the output slot to the right of the element display. Additionally, elements from the inventory can be inserted into the output slot to view its numbers of protons, electrons and neutrons. There are 118 elements and 400 isotopes available for construction.

## Data values
### ID
| Name                | Identifier        | Numeric ID | Form                       | Item ID[i 1]   | Translation key                |
|---------------------|-------------------|------------|----------------------------|----------------|--------------------------------|
| Element Constructor | `chemistry_table` | `238`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.elementconstructor.name` |

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



