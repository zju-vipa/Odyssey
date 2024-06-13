### 
A chest can be added to a donkey, a mule, or a llama by pressing use on the respective animal.

A chest attached to a donkey or mule has only 15 slots. A chest attached to a llama has anywhere from 3 to 15 slots depending upon its "Strength" value (see Llama § Data values). The chest cannot be removed except by killing the carrier. The chest can be opened by holding sneak and pressing use, or by riding the carrier and pressing inventory.

If shulker boxes are again used, each donkey, mule or strength value 5 llamas with a chest attached to it can carry up to 405 stacks of items (up to 25920 items), and with strength value 5 llamas, each caravan of 10 llamas with inventories full of shulker boxes can carry up to 4050 stacks of items (up to 259200 items).

### Piglins
Piglins become hostile toward players who open or mine chests.

### Crafting ingredient
| Name                | Ingredients              | Crafting recipe |
|---------------------|--------------------------|-----------------|
| Boat with Chest     | Chest+<br/>MatchingBoat  |                 |
| Hopper              | Iron Ingot+<br/>Chest    |                 |
| Minecart with Chest | Chest+<br/>Minecart      |                 |
| Shulker Box         | Shulker Shell+<br/>Chest |                 |
| Trapped Chest       | Tripwire Hook+<br/>Chest |                 |

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

| Name  | Identifier | Form         | Block tags           | Translation key         |
|-------|------------|--------------|----------------------|-------------------------|
| Chest | `chest`    | Block & Item | `guarded_by_piglins` | `block.minecraft.chest` |

| Name         | Identifier |
|--------------|------------|
| Block entity | `chest`    |

Bedrock Edition:

| Name  | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key   |
|-------|------------|------------|----------------------------|----------------|-------------------|
| Chest | `chest`    | `54`       | Block & Giveable Item[i 2] | Identical[i 3] | `tile.chest.name` |

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
A chest has a block entity associated with it that holds additional data about the block.

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

