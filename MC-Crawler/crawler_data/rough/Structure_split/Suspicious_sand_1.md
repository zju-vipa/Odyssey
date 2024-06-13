## Data values
### ID
Java Edition:

| Name            | Identifier        | Form         | Block tags                                                                                                   | Item tags | Translation key                   |
|-----------------|-------------------|--------------|--------------------------------------------------------------------------------------------------------------|-----------|-----------------------------------|
| Suspicious Sand | `suspicious_sand` | Block & Item | `bamboo_plantable_on`<br/>`enderman_holdable`<br/>`sand`<br/>`lush_ground_replaceable`<br/>`mineable/shovel` | `sand`    | `block.minecraft.suspicious_sand` |

| Name         | Identifier        |
|--------------|-------------------|
| Block entity | `brushable_block` |

Bedrock Edition:

| Name            | Identifier        | Numeric ID | Form                       | Item ID[i 1]   | Translation key             |
|-----------------|-------------------|------------|----------------------------|----------------|-----------------------------|
| Suspicious Sand | `suspicious_sand` | `-529`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.suspicious_sand.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

| Name         | Savegame ID      |
|--------------|------------------|
| Block entity | `BrushableBlock` |

### Block states
Java Edition:

| Name   | Default value | Allowed values              | Description                              |
|--------|---------------|-----------------------------|------------------------------------------|
| dusted | `0`           | `0`<br/>`1`<br/>`2`<br/>`3` | Increases as the block is being brushed. |

Bedrock Edition:

| Name             | Metadata Bits | Default value | Allowed values              | Values forMetadata Bits | Description                              |
|------------------|---------------|---------------|-----------------------------|-------------------------|------------------------------------------|
| brushed_progress | Not Supported | `0`           | `0`<br/>`1`<br/>`2`<br/>`3` | `Unsupported`           | Increases as the block is being brushed. |
| hanging          | Not Supported | `true`        | `true`<br/>`false`          | `Unsupported`           | [more information needed]                |



### Block data
Main article: Block entity format
- Block entity data
	- 
	- Tags common to all block entities
	- LootTable: Optional.Loot tableto be used to generate the hidden item when brushed.[note 1]
	- LootTableSeed: Optional. Seed for generating theloot table. 0 or omitted use a random seed.[note 1]
	- item: The item in the block. May not exist.
		- Seeitem format.

1. ↑ a bBoth loot table tags are removed once the items have been generated.

### Falling block entity
Main article: Falling Block
| Hitbox size | Height: 0.98 BlocksWidth: 0.98 Blocks |
|-------------|---------------------------------------|

{
    "title": "Falling Block",
    "rows": [
        {
            "field": "Height: 0.98 Blocks<br>Width: 0.98 Blocks",
            "label": "(link to Hitbox article, displayed as Hitbox size)"
        }
    ],
    "invimages": [],
    "images": []
}
- Dynamic block entity data
	- 
		- 
		- Tags common to all entities
	- BlockState: The falling block represented by this entity.
		- Name: Theresource locationof the block.
		- Properties: Optional. Theblock statesof the block.
			- Name: The block state name and its value.
	- CancelDrop: 1 or 0 (true/false) - true if the block should be destroyed instead of placed after landing on a solid block. When true, the block is not dropped as an item, even if theDropItemtag is set to true. However, if the entity is deleted due to itsTimevalue being too high, this tag is ignored and an item is dropped depending on theDropItemtag.CancelDropdefaults to 1 for fallingsuspicious sandandsuspicious gravel, and 0 for the other vanilla falling blocks and any summoned falling block.
	- DropItem: 1 or 0 (true/false) – true if the block should drop as an item when it breaks. Any block that does not have an item formwith the same ID as the blockdoes not drop even if this is set.
	- FallHurtAmount: Multiplied by theFallDistanceto calculate the amount of damage to inflict. By default this value is 2for anvils, and 6for pointed dripstone.
	- FallHurtMax: The maximum hit points of damage to inflict on entities that intersect this falling block. For vanilla falling blocks, always 40× 20.
	- HurtEntities: 1 or 0 (true/false) – true if the block should hurt entities it falls on. Defaults to 1 foranvilsandpointed dripstoneand to 0 for the other vanilla falling blocks and any summoned falling block.
	- TileEntityData: Optional. The tags of the block entity for this block.
	- Time: The number of ticks the entity has existed. WhenTimegoes above 600, or above 100 while the block is at Y=-64 or is outside building height, the entity is deleted.


