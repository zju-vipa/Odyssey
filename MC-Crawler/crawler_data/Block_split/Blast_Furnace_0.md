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


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


### Natural generation
Blast furnaces can generate in any armorer house; these can be found in a village. They can also generate in trail ruins.

### Crafting
| Ingredients                     | Crafting recipe |
|---------------------------------|-----------------|
| Iron Ingot+Furnace+Smooth Stone |                 |

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

