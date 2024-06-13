# Chest
A chest is a block used to store items.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
		- 1.2.1 Bonus chest
	- 1.3 Crafting
- 2 Usage
	- 2.1 Container
	- 2.2 Donkey, mule, or llama pack
	- 2.3 Piglins
	- 2.4 Crafting ingredient
	- 2.5 Fuel
	- 2.6 Note blocks
- 3 Christmas chest
- 4 Sounds
	- 4.1 Generic
	- 4.2 Unique
- 5 Data values
	- 5.1 ID
	- 5.2 Block states
	- 5.3 Block data
- 6 Achievements
- 7 Advancements
- 8 History
- 9 Issues
- 10 Trivia
- 11 Gallery
	- 11.1 Screenshots
	- 11.2 In other media
- 12 See also
- 13 References
- 14 External links

## Obtaining
### Breaking
A chest can be broken using anything, but an axe is the fastest. Chests always drop themselves when mined. If the chest contains items, the items are also dropped when the chest is broken. If one half of a large chest is destroyed, the corresponding items from the destroyed chest are dropped and the remaining half continues to function as a small chest.

in Java Edition, a chest will produce oak plank particles when breaking, walking or falling on this block, in Bedrock Edition,  a chest will produce particles of the block itself.[1]

| Block     | Chest                 |
|-----------|-----------------------|
| Hardness  | 2.5                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 3.75                  |
| Wooden    | 1.9                   |
| Stone     | 0.95                  |
| Iron      | 0.65                  |
| Diamond   | 0.5                   |
| Netherite | 0.45                  |
| Golden    | 0.35                  |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


### Natural generation
See also: Chest loot

Chests generate naturally in all three dimensions. They generate in monster rooms, strongholds, villages, jungle temples, desert temples, nether fortresses, end cities, igloos, woodland mansions, shipwrecks, ocean ruins, buried treasure, pillager outposts, bastion remnants, ruined portals, and ancient cities.

Large chests can occasionally generate in monster rooms by one single chest generating next to the other. They can also generate in certain types of bastion remnants.

#### Bonus chest
Main article: Bonus chest
The bonus chest is a chest that appears near the player's spawn if the "Bonus chest" option is toggled on the main menu. It generates with a semi-random collection of basic items to help the player survive early on and gather necessary resources, including wood, tools, blocks, and food.


### Crafting
| Ingredients | Crafting recipe |
|-------------|-----------------|
| AnyPlanks   |                 |

## Usage
Chests can be used as containers and as crafting ingredients.

To place a chest, use the Place Block control on the face of a block adjacent to the space the chest should occupy.

A chest placed adjacent to another chest joins to create a large chest. A player can prevent this, and place two small chests side by side, by sneaking while placing the second chest‌[JE  only], pushing a chest into place with a piston‌[BE  only], or placing the second chest facing a different direction from the first chest. Alternatively, trapped chests do not combine with normal chests.

Chests can be moved by pistons,‌[BE  only] and water and lava flow around chests without affecting them. Lava can create fire in air blocks next to chests as if the chests were flammable, but the chests do not actually catch fire and cannot be burned.

### Container
The GUI of a chest.
The GUI of a large chest.
A small chest has 27 slots of inventory space, and a large chest has twice that amount, at 54 slots. In the Java Edition interface, the top three rows for a large chest correspond to the left half of the chest when facing it, and the bottom three rows correspond to the right half. In Bedrock Edition, the top three rows correspond to whichever half was placed first and the bottom three to the other half.

Chests open when used. To move items between the chest inventory and the player inventory or hotbar while the chest GUI is open, drag or shift-click the items. Holding Shift and double-clicking while holding an item moves all items of the type clicked on in or out of the chest, to the extent that space is available for them.‌[Java Edition  only] To exit the chest GUI, use the Esc control.

A chest cannot be opened if there is an opaque block above it (in Bedrock Edition, bottom-half slabs prevent chests from being opened). Solid faces do not prevent chests from opening, so the lid of the chest can phase through blocks such as bottom-half slabs, stairs, and transparent full cubes such as glass and ice. Ocelots and cats sitting on chests prevent them from opening. Because chests themselves are functionally transparent, two chests can be stacked on top of one another while still allowing the lower chest to be opened. Players can open chests when they are being hurt (effect of Instant Damage, Poison, Wither, on fire, damaged by other players or mobs, etc.).

By default, the GUI of a chest is labeled "Chest" and the GUI of a large chest is labeled "Large Chest". A chest's GUI label can be changed by naming the chest in an anvil before placing it, or by using the /data command‌[Java Edition  only] (for example, to label a chest at (0,64,0) as "Bonus Chest!", use /data merge block 0 64 0 {CustomName:'"Bonus Chest!"'}). If half of a large chest is renamed, that name is used to label the GUI of the entire large chest, but if the named half is destroyed the other half reverts to the default label. If both halves of a large chest have different names, the GUI uses the name of the northernmost or westernmost half.

In Java Edition, a chest can be "locked" by setting its  Lock tag using the /data command. If a chest's  Lock tag is not blank, the chest cannot be opened unless the player is holding an item with the same name as the Lock tag's text. For example, to lock a chest at (0,64,0) so that the chest cannot be opened unless the player is holding an item named "Chest Key", use /data merge block 0 64 0 {Lock:"Chest Key"}.

The capacity of a chest varies greatly, depending on its size, whether the items inside it are stackable, and whether shulker boxes are used. The minimum capacity is obtained when storing only non-stackable items while the maximum capacity can be achieved when storing items that stack to 64. Filled shulker boxes are not stackable, but each can hold 27 stacks of up to 64 items (excluding other shulker boxes), so filling a chest with them increases the maximum by a factor of 27.

| Chest size | Slots | Maximum number of items |                    |
|------------|-------|-------------------------|--------------------|
|            |       | Without shulker boxes   | With shulker boxes |
| Small      | 27    | 1,728                   | 46,656             |
| Large      | 54    | 3,456                   | 93,312             |

### 
A chest can be added to a donkey, a mule, or a llama by pressing use on the respective animal.

A chest attached to a donkey or mule has only 15 slots. A chest attached to a llama has anywhere from 3 to 15 slots depending upon its "Strength" value (see Llama § Data values). The chest cannot be removed except by killing the carrier. The chest can be opened by holding sneak and pressing use, or by riding the carrier and pressing inventory.

If shulker boxes are again used, each donkey, mule or strength value 5 llamas with a chest attached to it can carry up to 405 stacks of items (up to 25920 items), and with strength value 5 llamas, each caravan of 10 llamas with inventories full of shulker boxes can carry up to 4050 stacks of items (up to 259200 items).

### Piglins
Piglins become hostile toward players who open or mine chests.

### Crafting ingredient
| Name                | Ingredients         | Crafting recipe |
|---------------------|---------------------|-----------------|
| Boat with Chest     | Chest+MatchingBoat  |                 |
| Hopper              | Iron Ingot+Chest    |                 |
| Minecart with Chest | Chest+Minecart      |                 |
| Shulker Box         | Shulker Shell+Chest |                 |
| Trapped Chest       | Tripwire Hook+Chest |                 |

### Fuel
Chests can be used as fuel in furnaces, smelting 1.5 items per chest.

### Note blocks
Chests can be placed under note blocks to produce the "bass" sound.

##  Christmas chest

  

This feature is exclusive to  Java Edition. 


On December 24–26, chests, large chests, and their trapped chest counterparts have their textures changed to "Christmas chests" that look like wrapped Christmas presents. Since the game uses the date stored on the player's computer, players can apply the Christmas chest textures at any time by changing the date on their computer to December 24, 25, or 26.

- 
- 

## Data values
### ID
Java Edition:

| Name  | Identifier | Form         | Block tags         | Translation key       |
|-------|------------|--------------|--------------------|-----------------------|
| Chest | chest      | Block & Item | guarded_by_piglins | block.minecraft.chest |

| Name         | Identifier |
|--------------|------------|
| Block entity | chest      |

Bedrock Edition:

| Name  | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key |
|-------|------------|------------|----------------------------|----------------|-----------------|
| Chest | chest      | 54         | Block & Giveable Item[i 2] | Identical[i 3] | tile.chest.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


| Name         | Savegame ID |
|--------------|-------------|
| Block entity | Chest       |

### Block states
See also: Block states

Java Edition:

| Name        | Default value | Allowed values     | Description                                                                                                  |
|-------------|---------------|--------------------|--------------------------------------------------------------------------------------------------------------|
| facing      | north         | eastnorthsouthwest | The direction the chest's latch is on.The opposite from the direction the player faces when placing a chest. |
| type        | single        | leftrightsingle    | The direction the chest has a connection with.                                                               |
| waterlogged | false         | falsetrue          | Whether or not there's water in the same place as this chest.                                                |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values     | Values forMetadata Bits | Description                                                                                                  |
|------------------------------|---------------|---------------|--------------------|-------------------------|--------------------------------------------------------------------------------------------------------------|
| minecraft:cardinal_direction | Not Supported | north         | eastnorthsouthwest | Unsupported             | The direction the chest's latch is on.The opposite from the direction the player faces when placing a chest. |



### Block data
A chest has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format


 Block entity data
Tags common to all block entities
Tags common to all objects that can be renamed
 Items: List of items in this container.
: An item, including the slot tag. Chest slots are numbered 0-26, 0 starts in the top left corner.
Tags common to all items
Tags common to all containers that can be locked
Tags common to all objects that use loot tables to produce items
 gold: Exists only in the april fools snapshot 23w13a_or_b. Optional. When set to anything but 0, turns the chest into a golden chest.

Bedrock Edition:

See Bedrock Edition level format/Block entity format.
## See also
- Locked chest(The 2011 April Fools' joke that is no longer in the game)

