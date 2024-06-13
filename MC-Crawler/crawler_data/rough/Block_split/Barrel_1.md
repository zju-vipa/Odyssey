### Changing profession
If a village has a barrel that has not been claimed by a villager, any villager who does not have a chosen job site block has a chance to change their profession into a fisherman.

### Fuel
Barrels can be used as a fuel in furnaces, smelting 1.5 items per block.

### Note Blocks
Barrels can be placed under note blocks to produce "bass" sounds.

### Piglins
Piglins become hostile toward players who open or break barrels.

## Data values
### ID
Java Edition:

| Name   | Identifier | Form         | Block tags           | Translation key          |
|--------|------------|--------------|----------------------|--------------------------|
| Barrel | `barrel`   | Block & Item | `guarded_by_piglins` | `block.minecraft.barrel` |

| Name         | Identifier |
|--------------|------------|
| Block entity | `barrel`   |

Bedrock Edition:

| Name   | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key    |
|--------|------------|------------|----------------------------|----------------|--------------------|
| Barrel | `barrel`   | `458`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.barrel.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

| Name         | Savegame ID |
|--------------|-------------|
| Block entity | `Barrel`    |

### Block states
See also: Block states

Java Edition:

| Name   | Default value | Allowed values                                                | Description                                                                                       |
|--------|---------------|---------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| facing | `north`       | `down`<br/>`east`<br/>`north`<br/>`south`<br/>`up`<br/>`west` | The direction the barrel is facing.                                                               |
| open   | `false`       | `false`<br/>`true`                                            | Whether the barrel is currently being looked at by a player; changes the texture on the top face. |

Bedrock Edition:

| Name             | Metadata Bits             | Default value | Allowed values                              | Values forMetadata Bits                     | Description                                                                                                                                                                               |
|------------------|---------------------------|---------------|---------------------------------------------|---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing_direction | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | The direction the barrel is facing.0:Down facing barrel<br/>1:Up facing barrel<br/>2:East facing barrel<br/>3:West facing barrel<br/>4:South facing barrel<br/>5:North facing barrel<br/> |
| open_bit         | `0x8`                     | `0`           | `0`<br/>`1`                                 | `0`<br/>`1`                                 | Whether the barrel is currently being looked at by a player; changes the texture on the top face.                                                                                         |



### Block data
A barrel has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format

- Block entity data
	- 
	- Tags common to all block entities
	- 
	- CustomName: Optional. The name of this container in JSON text component, which appears in its GUI where the default name ordinarily appears.
	- Items: List of items in the container.
		- : An item, including the slot tag. Barrel slots are numbered 0-26, 0 starts in the top left corner.
			- 
			- Tags common to all items
	- 
	- Lock: Optional. When not blank, prevents the container from being opened unless the opener is holding an item whose name matches this string.
	- 
	- LootTable: Optional. Name of the loot table to use. If this is used in a chest-like container, the loot table generates its content when it is opened. Generating the items in the container removes both loot table tags (LootTableandLootTableSeed).
	- LootTableSeed: Optional. Seed for generating the loot table. The default value works similarly to the seeds for worlds, where value of0or an omitted value causes the game to use a random seed.

Bedrock Edition:

SeeBedrock Edition level format/Block entity format.

