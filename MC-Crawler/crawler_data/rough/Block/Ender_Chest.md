# Ender Chest
Ender chests are a type of chest whose contents are exclusive to each player, and can be accessed from anywhere in the world.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
- 2 Usage
	- 2.1 Light source
	- 2.2 Note blocks
	- 2.3 Piglins
	- 2.4 Piston interactivity
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
	- 4.3 Block data
	- 4.4 Inventory
- 5 History
- 6 Issues
- 7 Trivia
- 8 Gallery
	- 8.1 Screenshots
	- 8.2 In other media
- 9 References

## Obtaining
### Breaking
Ender chests require a pickaxe enchanted with Silk Touch to be mined, otherwise, they drop nothing. Unless the pickaxe is enchanted with Silk Touch, the ender chest drops only 8 obsidian with no eyes of ender. Any pickaxe allows the ender chest to drop 8 obsidian, despite obsidian itself only being obtainable with a diamond or netherite pickaxe.[1]

In Java Edition, an ender chest will produce obsidian particles when breaking, walking or falling on this block, while in Bedrock Edition, an ender chest will produce particles of the block itself.[2]

| Block     | Ender Chest           |
|-----------|-----------------------|
| Hardness  | 22.5                  |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 112.5                 |
| Wooden    | 16.9                  |
| Stone     | 8.45                  |
| Iron      | 5.65                  |
| Diamond   | 4.25                  |
| Netherite | 3.75                  |
| Golden    | 2.85                  |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
Ender chests naturally generate alongside a chest in certain end city treasure rooms.

### Crafting
| Ingredients                | Crafting recipe |
|----------------------------|-----------------|
| Obsidian+<br/>Eye of Ender |                 |

## Usage
GUI of the ender chest.
Ender chests can be opened by pressing the use control. If a solid block is placed above an ender chest, it cannot be opened.

Ender chests can be used like normal chests, except all ender chests in the world are interconnected, including in different dimensions. The ender chest's inventory is also separate for each player; consequently, items stored in an ender chest cannot be seen or taken by other players. Also, items stored inside of an ender chest retain even if the player dies. Even if every single ender chest is destroyed in the world, the items inside the ender chest are still secure, and can be retrieved by placing another ender chest. Because of this player-specific property, ender chests are extremely useful on multiplayer servers to secure player's most valuable items.

Donkeys, mules, and llamas cannot be equipped with ender chests; they support only normal chests.

Ender chests contain 27 slots for storage and can be placed next to other ender chests without joining; they cannot be combined into double chests. It is possible to greatly increase the space of an ender chest by pairing it with shulker boxes (i.e. filling the shulker boxes with desired items, then placing them inside the ender chest). Placing 27 shulker boxes in the ender chest increases the storage space to 729 slots.

Ender chests do not interact with hoppers, droppers, or comparators.

Despite its high obsidian content, an ender chest is not immune to destruction by the ender dragon.[3]

### Light source
Ender chests emit a light level of 7.

### Note blocks
Ender chests can be placed under note blocks to produce "bass drum" sounds.

### Piglins
Piglins become hostile toward players who open or mine an ender chest.[4]

### Piston interactivity
Ender chests cannot be pushed by pistons. They also cannot be pushed nor pulled by sticky pistons.

## Data values
### ID
Java Edition:

| Name        | Identifier    | Form         | Block tags           | Translation key               |
|-------------|---------------|--------------|----------------------|-------------------------------|
| Ender Chest | `ender_chest` | Block & Item | `guarded_by_piglins` | `block.minecraft.ender_chest` |

| Name         | Identifier    |
|--------------|---------------|
| Block entity | `ender_chest` |

Bedrock Edition:

| Name        | Identifier    | Numeric ID | Form                       | Item ID[i 1]   | Translation key         |
|-------------|---------------|------------|----------------------------|----------------|-------------------------|
| Ender Chest | `ender_chest` | `130`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.ender_chest.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

| Name         | Savegame ID  |
|--------------|--------------|
| Block entity | `EnderChest` |

### Block states
See also: Block states

Java Edition:

| Name        | Default value | Allowed values                            | Description                                                                                                                    |
|-------------|---------------|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| facing      | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the ender chest's latch is on.<br/>The opposite from the direction the player faces when placing an ender chest. |
| waterlogged | `false`       | `false`<br/>`true`                        | Whether or not there's water in the same place as this ender chest.                                                            |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values                            | Values forMetadata Bits | Description                                                                                                                    |
|------------------------------|---------------|---------------|-------------------------------------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| minecraft:cardinal_direction | Not Supported | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | `Unsupported`           | The direction the ender chest's latch is on.<br/>The opposite from the direction the player faces when placing an ender chest. |



### Block data
An ender chest has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format

- Block entity data
	- 
	- Tags common to all block entities

Bedrock Edition:

SeeBedrock Edition level format/Block entity format.
### Inventory
The contents of an ender chest are not stored in the block, but in the player-NBT under the tag EnderItems‌[Java Edition  only]/EnderChestInventory‌[Bedrock Edition  only]. Thus ender chests can be viewed as "portals" to a player's 27 additional slots of secure and exclusive inventory, which are not lost on death.

