# Smoker
A smoker is a block that cooks food twice as quickly as a furnace, but cannot smelt anything else. It also serves as a butcher's job site block.

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
	- 5.1 Lit smoker "item"
		- 5.1.1 Appearances
		- 5.1.2 Names
- 6 Issues
- 7 Trivia
- 8 Gallery
	- 8.1 Renders
	- 8.2 Screenshots
- 9 See also
- 10 External links

## Obtaining
### Breaking
A smoker can be picked up using any pickaxe. If mined without a pickaxe, it does not drop itself.

Smokers drop their contents when broken.

| Block     | Smoker                |
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


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


### Natural generation
Smokers can generate in butcher houses in villages.

### Crafting
| Ingredients                                                                            | Crafting recipe |
|----------------------------------------------------------------------------------------|-----------------|
| AnyLogorStemorAnyStripped LogorStemorAnyWoodorHyphaeorAnyStripped WoodorHyphae+Furnace |                 |

## Usage
Smokers cannot be pushed by pistons.‌[Java Edition  only]

### Smelting
The GUI for the smoker.
Main article: Smelting
Smokers are used to cook food items twice as fast as a regular furnace. It is the counterpart to the blast furnace, which is used to quickly smelt ores, metal tools and armor. When a food item and a fuel item are placed into the smoker, the block state changes to lit and the item cooks. Fuel is used at double the rate of regular furnaces, so the number of items cooked per fuel stays the same. The product can then be taken out of the output slot in the smoker's interface, or be collected using a hopper.

Smokers cannot cook chorus fruit, as popped chorus fruit is not edible.

### Changing profession
If a village has a smoker that has not been claimed by a villager, any nearby villager who hasn't chosen a job site block has a chance to change their profession to butcher.

### Light source
Smokers emit a light level of 13 when active, just like normal furnaces.

### Custom name
By default, the interface of a smoker is labeled "Smoker", but this name can be customized by naming it in an anvil before placing it, or by changing the CustomName tag using the /data command‌[Java Edition  only].

### Lock
In Java Edition, a smoker can be "locked" by setting its Lock tag using the /data command. If a smoker's Lock tag is not blank, the smoker cannot be opened unless the player is holding an item with the same name as the Lock tag's text. For example, to lock a smoker at (0,64,0) so that the smoker cannot be opened unless the player is holding an item named "Smoker Key", use /data merge block 0 64 0 {Lock:"Smoker Key"}.

### Note blocks
Smoker can be placed under note blocks to produce "bass drum" sounds.

## Data values
### ID
Java Edition:

| Name   | Identifier | Form         | Translation key        |
|--------|------------|--------------|------------------------|
| Smoker | smoker     | Block & Item | block.minecraft.smoker |

| Name         | Identifier |
|--------------|------------|
| Block entity | smoker     |

Bedrock Edition:

| Name       | Identifier | Numeric ID | Form                         | Item ID[i 1]   | Translation key  |
|------------|------------|------------|------------------------------|----------------|------------------|
| Smoker     | smoker     | 453        | Block & Giveable Item[i 2]   | Identical[i 3] | tile.smoker.name |
| Lit Smoker | lit_smoker | 454        | Block & Ungiveable Item[i 4] | Identical[i 3] | —                |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ a b The block's direct item form has the same id as the block.

↑ Unavailable with /give command


| Name         | Savegame ID |
|--------------|-------------|
| Block entity | Smoker      |

### Block states
See also: Block states

Java Edition:

| Name   | Default value | Allowed values     | Description                                                                                                         |
|--------|---------------|--------------------|---------------------------------------------------------------------------------------------------------------------|
| facing | north         | eastnorthsouthwest | The direction the smoker's opening faces.The opposite from the direction the player faces while placing the smoker. |
| lit    | false         | falsetrue          | If the smoker is lit.                                                                                               |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values     | Values forMetadata Bits | Description                                                                                                         |
|------------------------------|---------------|---------------|--------------------|-------------------------|---------------------------------------------------------------------------------------------------------------------|
| minecraft:cardinal_direction | Not Supported | south         | eastnorthsouthwest | Unsupported             | The direction the smoker's opening faces.The opposite from the direction the player faces while placing the smoker. |



### Block data
A smoker has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format


 Block entity data
Tags common to all block entities
 BurnTime: Number of ticks left before the current fuel runs out.
 CookTime: Number of ticks the item has been smelting for. The item finishes smelting when this value reaches 200 (10 seconds). Is reset to 0 if BurnTime reaches 0.
 CookTimeTotal: Number of ticks It takes for the item to be smelted.

 CustomName: Optional. The name of this container in JSON text component, which appears in its GUI where the default name ordinarily appears.
 Items: List of items in this container.
: An item in the smoker, including the slot tag:Slot 0: The item(s) being smelted.Slot 1: The item(s) to use as the next fuel source.Slot 2: The item(s) in the result slot.
Tags common to all items

 Lock: Optional. When not blank, prevents the container from being opened unless the opener is holding an item whose name matches this string.
 RecipesUsed: Which recipes have been used since the last time a recipe result item was manually removed from the GUI. Used to calculate experience given to the player when taking out the resulting item.
 recipe ID: How many times this specific recipe has been used. The recipe ID is the identifier of the smelting recipe, as a resource location, as used in the /recipe command.

Bedrock Edition:

See Bedrock Edition level format/Block entity format.
## See also
- Furnace
- Blast Furnace

