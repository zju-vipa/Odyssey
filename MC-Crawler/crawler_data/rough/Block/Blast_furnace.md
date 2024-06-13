# Blast Furnace
A blast furnace is a block that smelts ores, raw metals and metal armor and tools twice as quickly as a furnace, but cannot smelt anything else. It also serves as job site block for armorers.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
- 2 Usage
	- 2.1 Smelting
	- 2.2 Changing profession
	- 2.3 Light source
	- 2.4 Custom name
	- 2.5 Lock
	- 2.6 Note blocks
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
	- 4.3 Block data
- 5 History
	- 5.1 Lit blast furnace "item"
		- 5.1.1 Appearances
		- 5.1.2 Names
- 6 Gallery
	- 6.1 Renders
	- 6.2 Screenshots
- 7 Issues
- 8 See also
- 9 External links

## Obtaining
### Breaking
A blast furnace can be picked up using any pickaxe. If mined without a pickaxe, it does not drop.

Blast furnaces drop their contents when broken.

| Block     | Blast Furnace         |
|-----------|-----------------------|
| Hardness  | 3.5                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 17.5                  |
| Wooden    | 2.65                  |
| Stone     | 1.35                  |
| Iron      | 0.9                   |
| Diamond   | 0.7                   |
| Netherite | 0.6                   |
| Golden    | 0.45                  |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
Blast furnaces can generate in any armorer house; these can be found in a village. They can also generate in trail ruins.

### Crafting
| Ingredients                               | Crafting recipe |
|-------------------------------------------|-----------------|
| Iron Ingot+<br/>Furnace+<br/>Smooth Stone |                 |

## Usage
Blast furnaces can be pushed by pistons.‌[Bedrock Edition  only]

### Smelting
The GUI for the blast furnace, same as the ordinary furnace's.
Main article: Smelting
Blast furnaces are similar to furnaces, but can smelt only raw metal, ore blocks and tools/armor made of iron, gold or chainmail. Blast furnaces serve as the counterpart to smokers, which are used mainly to cook food faster. Smelting equipment yields one iron or gold nugget from their respective materials. Once an item and a fuel are placed into the blast furnace, the block state changes to lit and the item is smelted twice as fast as a regular furnace. Fuel is also used at double the rate of regular furnaces, so the number of items smelted per fuel stays the same. The product can then be collected by using the output. Like normal furnaces, a hopper can be used to feed items into or collect items from a blast furnace.

### Changing profession
If a village has a blast furnace that has not been claimed by a villager, any nearby villager who has not chosen a job site block has a chance to change their profession to armorer.

### Light source
Blast furnaces emit a light level of 13 when active, similar to normal furnaces.

### Custom name
By default, the interface of a blast furnace is labeled "Blast Furnace", but this name can be customized by naming it in an anvil before placing it, or by changing the CustomName tag using the /data command.‌[Java Edition  only]

### Lock
In Java Edition, a blast furnace can be "locked" by setting its Lock tag using the /data command. If a blast furnace's Lock tag is not blank, the blast furnace cannot be opened unless the player is holding an item with the same name as the Lock tag's text. For example, to lock a blast furnace at (0,64,0) so that the blast furnace cannot be opened unless the player is holding an item named "Blast Furnace Key", use /data merge block 0 64 0 {Lock:"Blast Furnace Key"}.

### Note blocks
Blast furnace can be placed under note blocks to produce "bass drum" sounds.

## Data values
### ID
Java Edition:

| Name          | Identifier      | Form         | Translation key                 |
|---------------|-----------------|--------------|---------------------------------|
| Blast Furnace | `blast_furnace` | Block & Item | `block.minecraft.blast_furnace` |

| Name         | Identifier      |
|--------------|-----------------|
| Block entity | `blast_furnace` |

Bedrock Edition:

| Name        | Identifier          | Numeric ID | Form                         | Item ID[i 1]   | Translation key           |
|-------------|---------------------|------------|------------------------------|----------------|---------------------------|
| Unlit block | `blast_furnace`     | `451`      | Block & Giveable Item[i 2]   | Identical[i 3] | `tile.blast_furnace.name` |
| Lit block   | `lit_blast_furnace` | `469`      | Block & Ungiveable Item[i 4] | Identical[i 3] | —                         |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑ a bThe block's direct item form has the same id as the block.
4. ↑Unavailable with /give command

| Name         | Savegame ID    |
|--------------|----------------|
| Block entity | `BlastFurnace` |

### Block states
See also: Block states

Java Edition:

| Name   | Default value | Allowed values                            | Description                                                                                                                            |
|--------|---------------|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the blast furnace's opening faces.<br/>The opposite from the direction the player faces while placing the blast furnace. |
| lit    | `false`       | `false`<br/>`true`                        | If the blast furnace is lit.                                                                                                           |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values                            | Values forMetadata Bits | Description                                                                                                                            |
|------------------------------|---------------|---------------|-------------------------------------------|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| minecraft:cardinal_direction | Not Supported | `south`       | `east`<br/>`north`<br/>`south`<br/>`west` | `Unsupported`           | The direction the blast furnace's opening faces.<br/>The opposite from the direction the player faces while placing the blast furnace. |



### Block data
A blast furnace has a block entity associated with it that holds additional data about the block.

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
		- : An item in the blast furnace, including the slot tag:Slot 0: The item(s) being smelted.Slot 1: The item(s) to use as the next fuel source.Slot 2: The item(s) in the result slot.
			- 
			- Tags common to all items
	- 
	- Lock: Optional. When not blank, prevents the container from being opened unless the opener is holding an item whose name matches this string.
	- RecipesUsed: Recipes that have been used since the last time a recipe result item was manually removed from the GUI. Used to calculate experience given to the player when taking out the resulting item.
		- recipe ID: How many times this specific recipe has been used. Therecipe IDis the identifier of the smeltingrecipe, as aresource location, as used in the/recipecommand.

Bedrock Edition:

SeeBedrock Edition level format/Block entity format.
