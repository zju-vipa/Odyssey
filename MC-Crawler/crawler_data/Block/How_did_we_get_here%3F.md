# How did we get here? (block)
How did we get here? is a joke block introduced in 22w13oneBlockAtATime. This block takes the place of all items in 22w13oneBlockAtATime, as the inventory (and by extension, items) are disabled in that version.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Post-generation
		- 1.2.1 Debug mode
- 2 Usage
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
	- 4.3 Display
- 5 History
- 6 Issues
- 7 Trivia

## Obtaining
### Breaking
A how did we get here? block can be broken with any tool, but does not drop. It goes directly to the player's hand like any other block in this version.

### Post-generation
Whenever an item would be otherwise dropped on the ground, a How did we get here? blocks spawns instead, displaying the item that it replaced and represents.

They are also spawned when an item is crafted with a crafting table.

#### Debug mode
Every item that can be displayed by How did we get here? blocks are seen in debug mode, as well as their waterlogged versions.

## Usage
A How did we get here? block can be used as the item it displays and can be thrown by the player like any other block. 

- It will increase your attack damage, if it displays a sword or axe.
- It will increase block breaking speed, if it displays the corresponding tool.
- It can be thrown onto a player to equip, if it displays a piece of armor.
- It can be thrown on acrafting tableto craft the appropriate items.
	- Or a crafting table can be thrown onto it, and the items will be crafted together if possible.
	- More information: Java_Edition_22w13oneBlockAtATime § Items.

They are also waterloggable.

## Data values
### ID
| Name                 | Identifier         | Form         | Translation key                    |
|----------------------|--------------------|--------------|------------------------------------|
| How did we get here? | generic_item_block | Block & Item | block.minecraft.generic_item_block |

### Block states
See also: Block states

| Name        | Default value | Allowed values | Description                                                                      |
|-------------|---------------|----------------|----------------------------------------------------------------------------------|
| item        | 0             | 012...1104     | The number display the item ID on it. SeeHow did we get here? (block)/Display.   |
| waterlogged | false         | falsetrue      | Whether or not there's water in the same place as thishow did we get here?block. |

### Display
Main article: How did we get here? (block)/Display
They have an item block state that specifies the internal ID of the item to display with (0-1104).

