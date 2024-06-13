# Trapped Chest
A trapped chest is a variant of the chest that functions similarly, but has a red-tinted latch, and produces redstone power while open.

Like normal chests, two trapped chests can merge into a large trapped chest if placed next to each other.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
- 2 Usage
	- 2.1 Container
	- 2.2 Redstone component
	- 2.3 Piglins
	- 2.4 Fuel
	- 2.5 Note blocks
- 3 Christmas chest
- 4 Sounds
	- 4.1 Generic
	- 4.2 Unique
- 5 Data values
	- 5.1 ID
	- 5.2 Block states
	- 5.3 Block data
- 6 Video
- 7 History
- 8 Issues
- 9 Trivia
- 10 References

## Obtaining
### Breaking
Trapped chests can be broken with any tool, but axes are the fastest. Items contained in the chest are dropped when the chest is broken. If one half of a large trapped chest is destroyed, the corresponding items from the destroyed trapped chest are dropped and the remaining trapped chest continues to function as a small trapped chest.

| Block     | Trapped Chest         |
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

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
Trapped chests naturally generate in "fake end portal rooms" in woodland mansions.

### Crafting
| Ingredients              | Crafting recipe |
|--------------------------|-----------------|
| Tripwire Hook+<br/>Chest |                 |

## Usage
Trapped chests can be used as containers and as redstone components.

To place a trapped chest, place the face of a block adjacent to the space the trapped chest should occupy.

Placing two adjacent trapped chests side-by-side typically joins them to create a large trapped chest. To avoid them joining and instead place two single trapped chests side by side, the player may sneak while placing the second trapped chest‌[Java Edition  only] ,or place the second trapped chest facing a different direction from the first one. Alternately, normal chests do not combine with trapped chests.

Trapped chests can be moved by pistons.‌[Bedrock Edition  only] Water and lava flow around without affecting them. Lava can create fire in air blocks next to trapped chests as if they were flammable, but the chests do not burn (and cannot be burned by other methods either).

Trapped chests can also activate buried TNT, destroying themselves, their contents and any mobs or players near them. They need to be opened twice for the TNT to be activated.

### Container
The GUI of a trapped chest.
The GUI of a large trapped chest.
A single trapped chest has 27 slots of inventory space, and a large trapped chest has 54 slots of inventory space. In a large trapped chest, the top three rows in the interface correspond to the western or northern chest block and the bottom three to the southern or eastern chest block.

To open the trapped chest GUI, use the Use Item control. To move items between the trapped chest inventory and the player inventory or hotbar while the trapped chest GUI is open, drag or shift-click the items. To exit the trapped chest GUI, use the Esc control.

By default, the GUI of a trapped chest is labeled "Chest" and the GUI of a large trapped chest is labeled "Large Chest." A trapped chest's GUI label can be changed by naming the trapped chest in an anvil before placing it, or by using the /data command‌[Java Edition  only] (for example, to label a trapped chest at (0,64,0) "Loot!", use /data merge block 0 64 0 {CustomName:'"Loot!"'}). If half of a large trapped chest is renamed, that name is used to label the GUI of the entire large trapped chest, but if the named half is destroyed, the other half reverts to the default label. If both halves of a large trapped chest have different names, the GUI label takes the name of the northernmost or westernmost half of the large trapped chest depending on its orientation (the half with the lowest coordinate in the appropriate axis).

A trapped chest can be "locked" by setting the trapped chest's Lock tag. If a trapped chest's Lock tag is not blank, the trapped chest cannot be opened except by players holding an item with the same name as the Lock tag's text. A trapped chest's Lock tag can be set or unset with the data command. For example, to lock a trapped chest at (0,64,0) so that only players holding an item named "Alice's Key" can open the trapped chest, use data merge block 0 64 0 {Lock:"Alice's Key"}.

### Redstone component
Chests (left) and trapped chests (right) can be placed next to each other. Redstone dust configures itself to point toward trapped chests, but not toward regular chests.
See also: Redstone circuit

Trapped chests can be used to detect when their inventory is accessed by players.

A trapped chest is inactive while not being accessed, but activates when accessed by a player (see above). Accessing either part of a large trapped chest activates both halves of the large trapped chest. Mobs cannot access/activate a trapped chest, and a trapped chest is not activated by items moving into or out of it by droppers or hoppers.

While active, a trapped chest:

- powers any adjacentredstone dust, including beneath the trapped chest, to apower levelequal to the number of players accessing the trapped chest (maximum 15)
- powers any adjacentredstone repeatersfacing away from the trapped chest to power level 15
- strongly powers any full solid opaque block (stone, dirt, block of gold, etc.) beneath the trapped chest to a power level equal to the number of players accessing the trapped chest (maximum 15)
- activates any adjacentmechanism components, including above or below, such aspistons,redstone lamps, etc. Due to hoppers being locked by redstone activation, hoppers below a trapped chest do not take items from it while it is open.

An active trapped chest does not power any adjacent redstone comparators facing away from it. Redstone comparators can measure the block state of the trapped chest, producing a power level from 0 to 15 proportional to how full the trapped chest is. Anything else powered by an active trapped chest (including a block beneath it) can power redstone comparators normally.

### Piglins
Piglins become hostile toward players who open, break or interact with trapped chests.

### Fuel
Trapped chests can be used as a fuel in furnaces, smelting 1.5 items per chest.

### Note blocks
Trapped chests can be placed under note blocks to produce "bass" sound.

##  Christmas chest

  

This feature is exclusive to  Java Edition. 


As with normal chests, on December 24, 25, and 26, trapped chests and large trapped chests have their textures changed to Christmas chests that look like presents.

- 
- 

## Data values
### ID
Java Edition:

| Name          | Identifier      | Form         | Block tags           | Translation key                 |
|---------------|-----------------|--------------|----------------------|---------------------------------|
| Trapped Chest | `trapped_chest` | Block & Item | `guarded_by_piglins` | `block.minecraft.trapped_chest` |

| Name         | Identifier      |
|--------------|-----------------|
| Block entity | `trapped_chest` |

Bedrock Edition:

| Name          | Identifier      | Numeric ID | Form                       | Item ID[i 1]   | Translation key           |
|---------------|-----------------|------------|----------------------------|----------------|---------------------------|
| Trapped Chest | `trapped_chest` | `146`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.trapped_chest.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

| Name         | Savegame ID |
|--------------|-------------|
| Block entity | `Chest`     |

### Block states
See also: Block states

Java Edition:

| Name        | Default value | Allowed values                            | Description                                                                                                       |
|-------------|---------------|-------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| facing      | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the chest's latch is on.<br/>The opposite from the direction the player faces when placing a chest. |
| type        | `single`      | `left`<br/>`right`<br/>`single`           | The direction the chest has a connection with.                                                                    |
| waterlogged | `false`       | `false`<br/>`true`                        | Whether or not there's water in the same place as this chest.                                                     |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values                            | Values forMetadata Bits | Description                                                                                                       |
|------------------------------|---------------|---------------|-------------------------------------------|-------------------------|-------------------------------------------------------------------------------------------------------------------|
| minecraft:cardinal_direction | Not Supported | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | `Unsupported`           | The direction the chest's latch is on.<br/>The opposite from the direction the player faces when placing a chest. |



### Block data
Every trapped chest has a block entity associated with it that holds additional data about the trapped chest.

Java Edition:

See also: Block entity format

- Block entity data
	- 
	- Tags common to all block entities
	- 
	- Tags common to all objects that can be renamed
	- Items: List of items in this container.
		- : An item, including the slot tag. Chest slots are numbered 0-26, 0 starts in the top left corner.
			- 
			- Tags common to all items
	- 
	- Tags common to all containers that can be locked
	- 
	- Tags common to all objects that use loot tables to produce items
	- gold: Exists only in the april fools snapshot23w13a_or_b. Optional. When set to anything but 0, turns the chest into a golden chest.

Bedrock Edition:

SeeBedrock Edition level format/Block entity format.
