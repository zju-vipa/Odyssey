### Light source
Lit furnace
Furnaces emit a light level of 13 when active, as well as smoke and flame particles.

### Crafting ingredient
| Name                  | Ingredients                                                                                                | Crafting recipe |
|-----------------------|------------------------------------------------------------------------------------------------------------|-----------------|
| Blast Furnace         | Iron Ingot+<br/>Furnace+<br/>Smooth Stone                                                                  |                 |
| Minecart with Furnace | Furnace+<br/>Minecart                                                                                      |                 |
| Smoker                | AnyLogorStemor<br/>AnyStripped LogorStemor<br/>AnyWoodorHyphaeor<br/>AnyStripped WoodorHyphae+<br/>Furnace |                 |

### Custom name
By default, the GUI of a furnace is labeled "Furnace", but this name can be customized by naming it in an anvil before placing it, or by changing the CustomName tag using the /data command‌[Java Edition  only].

### Lock
In Java Edition, a furnace can be "locked" by setting its Lock tag using the /data command. If a furnace's Lock tag is not blank, the furnace cannot be opened unless the player is holding an item with the same name as the Lock tag's text. For example, to lock a furnace at (0,64,0) so that the furnace cannot be opened unless the player is holding an item named "Furnace Key", use /data merge block 0 64 0 {Lock:"Furnace Key"}.

### Note blocks
A furnace can be placed under note blocks to produce "bass drum" sounds.

## Data values
### ID
Java Edition:

| Name    | Identifier | Form         | Translation key           |
|---------|------------|--------------|---------------------------|
| Furnace | `furnace`  | Block & Item | `block.minecraft.furnace` |

| Name         | Identifier |
|--------------|------------|
| Block entity | `furnace`  |

Bedrock Edition:

| Name        | Identifier    | Numeric ID | Form                         | Item ID[i 1]   | Translation key     |
|-------------|---------------|------------|------------------------------|----------------|---------------------|
| Furnace     | `furnace`     | `61`       | Block & Giveable Item[i 2]   | Identical[i 3] | `tile.furnace.name` |
| Lit Furnace | `lit_furnace` | `62`       | Block & Ungiveable Item[i 4] | Identical[i 3] | —                   |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑ a bThe block's direct item form has the same id as the block.
4. ↑Unavailable with /give command

| Name         | Savegame ID |
|--------------|-------------|
| Block entity | `Furnace`   |

### Block states
See also: Block states

Java Edition:

| Name   | Default value | Allowed values                            | Description                                                                                                                |
|--------|---------------|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the furnace's opening faces.<br/>The opposite from the direction the player faces while placing the furnace. |
| lit    | `false`       | `false`<br/>`true`                        | If the furnace is lit.                                                                                                     |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values                            | Values forMetadata Bits | Description                                                                                                                |
|------------------------------|---------------|---------------|-------------------------------------------|-------------------------|----------------------------------------------------------------------------------------------------------------------------|
| minecraft:cardinal_direction | Not Supported | `south`       | `east`<br/>`north`<br/>`south`<br/>`west` | `Unsupported`           | The direction the furnace's opening faces.<br/>The opposite from the direction the player faces while placing the furnace. |



### Block data
A furnace has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format

- Block entity data
	- 
	- Tags common to all block entities
	- BurnTime: Number of ticks left before the current fuel runs out.
	- CookTime: Number of ticks the item has been smelting for. The item finishes smelting when this value reaches 200 (10 seconds). Is reset to 0 if BurnTime reaches 0.
	- CookTimeTotal: Number of ticks It takes for the item to be smelted.
	- 
	- Tags common to all objects that can be renamed
	- Items: List of items in this container.
		- : An item in the furnace, including the slot tag:Slot 0: The item(s) being smelted.Slot 1: The item(s) to use as the next fuel source.Slot 2: The item(s) in the result slot.
			- 
			- Tags common to all items
	- 
	- Tags common to all containers that can be locked
	- RecipesUsed: Which recipes have been used since the last time a recipe result item was manually removed from the GUI. Used to calculate experience given to the player when taking out the resulting item.
		- recipe ID: How many times this specific recipe has been used. Therecipe IDis the identifier of the smeltingrecipe, as aresource location, as used in the/recipecommand.

Bedrock Edition:

SeeBedrock Edition level format/Block entity format.

