### Note blocks
Blast furnace can be placed under note blocks to produce "bass drum" sounds.

## Data values
### ID
Java Edition:

| Name          | Identifier    | Form         | Translation key               |
|---------------|---------------|--------------|-------------------------------|
| Blast Furnace | blast_furnace | Block & Item | block.minecraft.blast_furnace |

| Name         | Identifier    |
|--------------|---------------|
| Block entity | blast_furnace |

Bedrock Edition:

| Name        | Identifier        | Numeric ID | Form                         | Item ID[i 1]   | Translation key         |
|-------------|-------------------|------------|------------------------------|----------------|-------------------------|
| Unlit block | blast_furnace     | 451        | Block & Giveable Item[i 2]   | Identical[i 3] | tile.blast_furnace.name |
| Lit block   | lit_blast_furnace | 469        | Block & Ungiveable Item[i 4] | Identical[i 3] | —                       |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ a b The block's direct item form has the same id as the block.

↑ Unavailable with /give command


| Name         | Savegame ID  |
|--------------|--------------|
| Block entity | BlastFurnace |

### Block states
See also: Block states

Java Edition:

| Name   | Default value | Allowed values     | Description                                                                                                                       |
|--------|---------------|--------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| facing | north         | eastnorthsouthwest | The direction the blast furnace's opening faces.The opposite from the direction the player faces while placing the blast furnace. |
| lit    | false         | falsetrue          | If the blast furnace is lit.                                                                                                      |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values     | Values forMetadata Bits | Description                                                                                                                       |
|------------------------------|---------------|---------------|--------------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| minecraft:cardinal_direction | Not Supported | south         | eastnorthsouthwest | Unsupported             | The direction the blast furnace's opening faces.The opposite from the direction the player faces while placing the blast furnace. |



### Block data
A blast furnace has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format


 Block entity data
Tags common to all block entities
 BurnTime: Number of ticks left before the current fuel runs out.
 CookTime: Number of ticks the item has been smelting for. The item finishes smelting when this value reaches 200 (10 seconds). Is reset to 0 if BurnTime reaches 0.
 CookTimeTotal: Number of ticks It takes for the item to be smelted.

 CustomName: Optional. The name of this container in JSON text component, which appears in its GUI where the default name ordinarily appears.
 Items: List of items in this container.
: An item in the blast furnace, including the slot tag:Slot 0: The item(s) being smelted.Slot 1: The item(s) to use as the next fuel source.Slot 2: The item(s) in the result slot.
Tags common to all items

 Lock: Optional. When not blank, prevents the container from being opened unless the opener is holding an item whose name matches this string.
 RecipesUsed: Recipes that have been used since the last time a recipe result item was manually removed from the GUI. Used to calculate experience given to the player when taking out the resulting item.
 recipe ID: How many times this specific recipe has been used. The recipe ID is the identifier of the smelting recipe, as a resource location, as used in the /recipe command.

Bedrock Edition:

See Bedrock Edition level format/Block entity format.
## See also
- Furnace
- Smoker


