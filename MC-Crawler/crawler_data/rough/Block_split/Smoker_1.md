### Note blocks
Smoker can be placed under note blocks to produce "bass drum" sounds.

## Data values
### ID
Java Edition:

| Name   | Identifier | Form         | Translation key          |
|--------|------------|--------------|--------------------------|
| Smoker | `smoker`   | Block & Item | `block.minecraft.smoker` |

| Name         | Identifier |
|--------------|------------|
| Block entity | `smoker`   |

Bedrock Edition:

| Name       | Identifier   | Numeric ID | Form                         | Item ID[i 1]   | Translation key    |
|------------|--------------|------------|------------------------------|----------------|--------------------|
| Smoker     | `smoker`     | `453`      | Block & Giveable Item[i 2]   | Identical[i 3] | `tile.smoker.name` |
| Lit Smoker | `lit_smoker` | `454`      | Block & Ungiveable Item[i 4] | Identical[i 3] | —                  |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑ a bThe block's direct item form has the same id as the block.
4. ↑Unavailable with /give command

| Name         | Savegame ID |
|--------------|-------------|
| Block entity | `Smoker`    |

### Block states
See also: Block states

Java Edition:

| Name   | Default value | Allowed values                            | Description                                                                                                              |
|--------|---------------|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the smoker's opening faces.<br/>The opposite from the direction the player faces while placing the smoker. |
| lit    | `false`       | `false`<br/>`true`                        | If the smoker is lit.                                                                                                    |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values                            | Values forMetadata Bits | Description                                                                                                              |
|------------------------------|---------------|---------------|-------------------------------------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------|
| minecraft:cardinal_direction | Not Supported | `south`       | `east`<br/>`north`<br/>`south`<br/>`west` | `Unsupported`           | The direction the smoker's opening faces.<br/>The opposite from the direction the player faces while placing the smoker. |



### Block data
A smoker has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format

- Block entity data
	- 
	- Tags common to all block entities
	- BurnTime: Number of ticks left before the current fuel runs out.
	- CookTime: Number of ticks the item has been smelting for. The item finishes smelting when this value reaches 200 (10 seconds). Is reset to 0 if BurnTime reaches 0.
	- CookTimeTotal: Number of ticks It takes for the item to be smelted.
	- 
	- CustomName: Optional. The name of this container in JSON text component, which appears in its GUI where the default name ordinarily appears.
	- Items: List of items in this container.
		- : An item in the smoker, including the slot tag:Slot 0: The item(s) being smelted.Slot 1: The item(s) to use as the next fuel source.Slot 2: The item(s) in the result slot.
			- 
			- Tags common to all items
	- 
	- Lock: Optional. When not blank, prevents the container from being opened unless the opener is holding an item whose name matches this string.
	- RecipesUsed: Which recipes have been used since the last time a recipe result item was manually removed from the GUI. Used to calculate experience given to the player when taking out the resulting item.
		- recipe ID: How many times this specific recipe has been used. Therecipe IDis the identifier of the smeltingrecipe, as aresource location, as used in the/recipecommand.

Bedrock Edition:

SeeBedrock Edition level format/Block entity format.

