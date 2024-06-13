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

