## Data values
### ID
Java Edition:

| Name    | Identifier | Form         | Block tags                                | Translation key           |
|---------|------------|--------------|-------------------------------------------|---------------------------|
| Crafter | `crafter`  | Block & Item | `mineable/pickaxe`<br/>`needs_stone_tool` | `block.minecraft.crafter` |

| Name         | Identifier |
|--------------|------------|
| Block entity | `crafter`  |

Bedrock Edition:

| Name    | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key     |
|---------|------------|------------|----------------------------|----------------|---------------------|
| Crafter | `crafter`  | `-313`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.crafter.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

| Name         | Savegame ID |
|--------------|-------------|
| Block entity | `Crafter`   |

### Block states
See also: Block states

Java Edition:

| Name        | Default value | Allowed values                                                                                                                                                                    | Description                                                           |
|-------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| crafting    | `false`       | `false`<br/>`true`                                                                                                                                                                | Whether the crafter's mouth is open and top is glowing.               |
| orientation | `north_up`    | `down_east`<br/>`down_north`<br/>`down_south`<br/>`down_west`<br/>`east_up`<br/>`north_up`<br/>`south_up`<br/>`up_east`<br/>`up_north`<br/>`up_south`<br/>`up_west`<br/>`west_up` | The direction the crafter'sfaceis facing and which way it is rotated. |
| triggered   | `false`       | `false`<br/>`true`                                                                                                                                                                | Whether the crafter is activated.                                     |

Bedrock Edition:

| Name          | Metadata Bits | Default value | Allowed values                                                                                                                                                                    | Values forMetadata Bits | Description                                                           |
|---------------|---------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|-----------------------------------------------------------------------|
| crafting      | Not Supported | `false`       | `false`<br/>`true`                                                                                                                                                                | `Unsupported`           | Whether the crafter's mouth is open and top is glowing.               |
| orientation   | Not Supported | `down_east`   | `down_east`<br/>`down_north`<br/>`down_south`<br/>`down_west`<br/>`east_up`<br/>`north_up`<br/>`south_up`<br/>`up_east`<br/>`up_north`<br/>`up_south`<br/>`up_west`<br/>`west_up` | `Unsupported`           | The direction the crafter'sfaceis facing and which way it is rotated. |
| triggered_bit | Not Supported | `false`       | `false`<br/>`true`                                                                                                                                                                | `Unsupported`           | Whether the crafter is activated.                                     |



### Block data
A crafter has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format

- Block entity data
	- 
	- Tags common to all block entities
	- crafting_ticks_remaining: Set to 6 when the crafter crafts something.[more information needed]
	- triggered: Set to 1 when it is powered. It is otherwise 0.
	- disabled_slots: Indexes of slots that are disabled.
	- Items: List of items in this container.
		- : An item in the crafter, including the slot tag. Crafter slots are numbered 0-8. 0 starts in the top left corner.
			- 
			- Tags common to all items
	- 
	- Lock: Optional. When not blank, prevents the container from being opened unless the opener is holding an item whose name matches this string.
	- 
	- LootTable: Optional. Name of the loot table to use. If this is used in a chest-like container, the loot table generates its content when it is opened. Generating the items in the container removes both loot table tags (LootTableandLootTableSeed).
	- LootTableSeed: Optional. Seed for generating the loot table. The default value works similarly to the seeds for worlds, where value of0or an omitted value causes the game to use a random seed.

Bedrock Edition:

SeeBedrock Edition level format/Block entity format.

