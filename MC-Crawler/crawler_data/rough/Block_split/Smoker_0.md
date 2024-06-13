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

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
Smokers can generate in butcher houses in villages.

### Crafting
| Ingredients                                                                                                | Crafting recipe |
|------------------------------------------------------------------------------------------------------------|-----------------|
| AnyLogorStemor<br/>AnyStripped LogorStemor<br/>AnyWoodorHyphaeor<br/>AnyStripped WoodorHyphae+<br/>Furnace |                 |

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

