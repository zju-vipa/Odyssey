# Furnace
A furnace is a utility block used for the smelting of blocks and items.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Chest loot
	- 1.4 Crafting
- 2 Usage
	- 2.1 Smelting
	- 2.2 Light source
	- 2.3 Crafting ingredient
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
- 5 Achievements
- 6 Advancements
- 7 History
	- 7.1 Lit furnace "item"
		- 7.1.1 Names
- 8 Issues
- 9 Trivia
- 10 Gallery
	- 10.1 Renders
		- 10.1.1 Java Edition
		- 10.1.2 Bedrock Edition
	- 10.2 Screenshots
	- 10.3 In other media
- 11 See also
- 12 References
- 13 External links

## Obtaining
### Breaking
A furnace can be mined using any pickaxe. A furnace also drops all of its contents when broken, including XP from smelting items that were extracted by hoppers.

In Java Edition, a furnace mined without a pickaxe drops nothing. In Bedrock Edition, a furnace drops itself when mined by hand or with any tool.

| Block     | Furnace               |
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
Furnaces can be found in plains, desert, and some savanna village weaponsmiths. Furnaces also generate in some houses in snowy tundra villages, and in one of the taiga/snowy taiga‌[BE  only] village houses. They also appear in ancient cities and trail ruins, and one furnace generates in every igloo.

### Chest loot
| Item    | Structure | Container         | Quantity | Chance                         |
|---------|-----------|-------------------|----------|--------------------------------|
|         |           |                   |          | Java EditionandBedrock Edition |
| Furnace | Village   | Snowy house chest | 1        | 9.9%                           |

### Crafting
| Ingredients         | Crafting recipe | Description                                                 |
|---------------------|-----------------|-------------------------------------------------------------|
| Anystone-tier block |                 | Can use cobblestone and its other variants interchangeably. |

The lit furnace can be obtained in Java Edition only with commands such as /give @s minecraft:furnace{BlockStateTag:{lit:"true"}}, although it does not appear lit in the inventory. In Bedrock Edition, the lit furnace block can be obtained only by inventory editing. It always stays lit, despite containing no items.

## Usage
Furnaces cannot be pushed by pistons in Java Edition.

### Smelting
Main article: Smelting
Interface for the furnace.
The main purpose of a furnace is smelting. Its interface can be opened by pressing the use item button on it. A fuel source (up to one stack of fuel items) is placed in the lower slot, and the items (up to one stack) to be smelted are placed in the upper slot. A furnace smelts items at a speed of one item every 200 game ticks (10 seconds) or six items per minute.

The number of items that a fuel source can smelt depends on the type of fuel. As soon as smelting begins, the fuel slot is decremented immediately and that unit of fuel begins burning. The fuel continues burning until it is consumed, regardless of whether the upper slot has any items remaining to smelt. For example, a piece of coal burns for 80 seconds and can smelt eight items, but if only one item is smelted (or if the item is pulled out before smelting is complete), the coal still continues burning for the full 80 seconds, wasting seven items worth of smelting. After it burns out, no additional fuel is decremented from the fuel slot if the upper slot is empty. If the fuel slot is empty and the burning fuel is consumed before an item completes smelting, the smelting stops, the smelted item is unchanged, and smelting must be restarted with new fuel.

| Smelting recipe |
|-----------------|
|                 |

### Light source
Lit furnace
Furnaces emit a light level of 13 when active, as well as smoke and flame particles.

### Crafting ingredient
| Name                  | Ingredients                                                                            | Crafting recipe |
|-----------------------|----------------------------------------------------------------------------------------|-----------------|
| Blast Furnace         | Iron Ingot+Furnace+Smooth Stone                                                        |                 |
| Minecart with Furnace | Furnace+Minecart                                                                       |                 |
| Smoker                | AnyLogorStemorAnyStripped LogorStemorAnyWoodorHyphaeorAnyStripped WoodorHyphae+Furnace |                 |

### Custom name
By default, the GUI of a furnace is labeled "Furnace", but this name can be customized by naming it in an anvil before placing it, or by changing the CustomName tag using the /data command‌[Java Edition  only].

### Lock
In Java Edition, a furnace can be "locked" by setting its Lock tag using the /data command. If a furnace's Lock tag is not blank, the furnace cannot be opened unless the player is holding an item with the same name as the Lock tag's text. For example, to lock a furnace at (0,64,0) so that the furnace cannot be opened unless the player is holding an item named "Furnace Key", use /data merge block 0 64 0 {Lock:"Furnace Key"}.

### Note blocks
A furnace can be placed under note blocks to produce "bass drum" sounds.

## Data values
### ID
Java Edition:

| Name    | Identifier | Form         | Translation key         |
|---------|------------|--------------|-------------------------|
| Furnace | furnace    | Block & Item | block.minecraft.furnace |

| Name         | Identifier |
|--------------|------------|
| Block entity | furnace    |

Bedrock Edition:

| Name        | Identifier  | Numeric ID | Form                         | Item ID[i 1]   | Translation key   |
|-------------|-------------|------------|------------------------------|----------------|-------------------|
| Furnace     | furnace     | 61         | Block & Giveable Item[i 2]   | Identical[i 3] | tile.furnace.name |
| Lit Furnace | lit_furnace | 62         | Block & Ungiveable Item[i 4] | Identical[i 3] | —                 |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ a b The block's direct item form has the same id as the block.

↑ Unavailable with /give command


| Name         | Savegame ID |
|--------------|-------------|
| Block entity | Furnace     |

### Block states
See also: Block states

Java Edition:

| Name   | Default value | Allowed values     | Description                                                                                                           |
|--------|---------------|--------------------|-----------------------------------------------------------------------------------------------------------------------|
| facing | north         | eastnorthsouthwest | The direction the furnace's opening faces.The opposite from the direction the player faces while placing the furnace. |
| lit    | false         | falsetrue          | If the furnace is lit.                                                                                                |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values     | Values forMetadata Bits | Description                                                                                                           |
|------------------------------|---------------|---------------|--------------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------|
| minecraft:cardinal_direction | Not Supported | south         | eastnorthsouthwest | Unsupported             | The direction the furnace's opening faces.The opposite from the direction the player faces while placing the furnace. |



### Block data
A furnace has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format


 Block entity data
Tags common to all block entities
 BurnTime: Number of ticks left before the current fuel runs out.
 CookTime: Number of ticks the item has been smelting for. The item finishes smelting when this value reaches 200 (10 seconds). Is reset to 0 if BurnTime reaches 0.
 CookTimeTotal: Number of ticks It takes for the item to be smelted.
Tags common to all objects that can be renamed
 Items: List of items in this container.
: An item in the furnace, including the slot tag:Slot 0: The item(s) being smelted.Slot 1: The item(s) to use as the next fuel source.Slot 2: The item(s) in the result slot.
Tags common to all items
Tags common to all containers that can be locked
 RecipesUsed: Which recipes have been used since the last time a recipe result item was manually removed from the GUI. Used to calculate experience given to the player when taking out the resulting item.
 recipe ID: How many times this specific recipe has been used. The recipe ID is the identifier of the smelting recipe, as a resource location, as used in the /recipe command.

Bedrock Edition:

See Bedrock Edition level format/Block entity format.
## See also
- Blast Furnace
- Smoker
- Minecart with Furnace

