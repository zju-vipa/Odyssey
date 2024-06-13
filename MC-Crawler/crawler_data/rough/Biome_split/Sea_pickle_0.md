# Sea Pickle
A sea pickle is a small block that emits light underwater, and is typically found in colonies of up to four sea pickles.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Trading
	- 1.4 Post-generation
- 2 Usage
	- 2.1 Smelting ingredient
	- 2.2 Composting
	- 2.3 Placing
- 3 Sounds
- 4 Achievements
- 5 Data values
	- 5.1 ID
	- 5.2 Block states
- 6 History
- 7 Issues
- 8 Trivia
- 9 Gallery
	- 9.1 Renders
	- 9.2 Textures
	- 9.3 Screenshots
- 10 See also
- 11 References
- 12 External links

## Obtaining
### Breaking
Sea pickles can be broken instantly with any tool including hands. Each colony drops 1-4 sea pickles, depending on how many are in the colony (so a colony of 3 pickles drops 3 pickles).

### Natural generation
Sea pickle colonies generate on the bottom of warm oceans and are found on top of coral blocks in coral reefs. Each chunk has 1⁄6 chance to generate sea pickle colonies. They can be found in groups of 1 up to 4.

Sea pickles may also be found in desert village houses as decorative blocks that resemble pottery.


### Trading
Sea pickles are sold by wandering traders for 2 emeralds.

### Post-generation
Using bone meal on an underwater sea pickle placed on top of a living coral block creates more sea pickles. Specifically, the colony to which bone meal is applied increases in size, and any living coral block within a taxicab distance of 2 blocks (horizontally from either the coral block or the sea pickle itself) can generate 1-3 sea pickles. They do not grow or spread naturally, and do not require light. In Java Edition, sea pickles can also be created by simply bone mealing a coral block.

## Usage
Sea pickles can be placed on top of most solid blocks, as well as non-solid blocks, up to four per block, similar to turtle eggs or candles. More information regarding placement on transparent blocks can be found at Opacity/Placement. 

Sea pickles produce light when underwater. A single pickle produces a light level of 6, and a colony produces an additional 3 levels per pickle (so 4 sea pickles produces a light level of 15). When they produce light, there is a pale green glow at the end of the pickle.

Bone meal can be used on sea pickles if they are underwater, and planted on living coral blocks. This increases their number on that block, and they spread to empty areas underwater above other living coral blocks. They can spread to the original sea pickle's level or one level below, out to a horizontal taxicab distance of 2. Bone meal can be used on sea pickles planted on other blocks, or outside of water, but nothing happens and the bone meal is still consumed.[1]

### Smelting ingredient
| Name     | Ingredients             | Smelting recipe |
|----------|-------------------------|-----------------|
| Lime Dye | Sea Pickle+<br/>Anyfuel | 0.1             |

### Composting
Placing a sea pickle into a composter has a 65% chance of raising the compost level by 1.

### Placing
In Bedrock Edition, unlike turtle eggs, sea pickles can only be placed on complete blocks.

## Data values
### ID
Java Edition:

| Name       | Identifier   | Form         | Translation key              |
|------------|--------------|--------------|------------------------------|
| Sea Pickle | `sea_pickle` | Block & Item | `block.minecraft.sea_pickle` |

Bedrock Edition:

| Name       | Identifier   | Numeric ID | Form                       | Item ID[i 1]   | Translation key        |
|------------|--------------|------------|----------------------------|----------------|------------------------|
| Sea Pickle | `sea_pickle` | `411`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.sea_pickle.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:

| Name        | Default value | Allowed values              | Description                                                      |
|-------------|---------------|-----------------------------|------------------------------------------------------------------|
| pickles     | `1`           | `1`<br/>`2`<br/>`3`<br/>`4` | Number of pickles.                                               |
| waterlogged | `true`        | `false`<br/>`true`          | Whether or not there's water in the same place as these pickles. |

Bedrock Edition:

| Name          | Metadata Bits   | Default value | Allowed values              | Values forMetadata Bits     | Description                                                  |
|---------------|-----------------|---------------|-----------------------------|-----------------------------|--------------------------------------------------------------|
| cluster_count | `0x1`<br/>`0x2` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3` | `0`<br/>`1`<br/>`2`<br/>`3` | Number of additional pickles.                                |
| dead_bit      | `0x4`           | `false`       | `false`<br/>`true`          | `0`<br/>`1`                 | True if there's no water in the same place as these pickles. |


