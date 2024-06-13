### Fuel
Scaffolding can be used as a fuel in furnaces, smelting 0.25 items per block.

## Data values
### ID
Java Edition:

| Name        | Identifier    | Form         | Block tags  | Translation key               |
|-------------|---------------|--------------|-------------|-------------------------------|
| Scaffolding | `scaffolding` | Block & Item | `climbable` | `block.minecraft.scaffolding` |

Bedrock Edition:

| Name        | Identifier    | Numeric ID | Form                       | Item ID[i 1]   | Translation key         |
|-------------|---------------|------------|----------------------------|----------------|-------------------------|
| Scaffolding | `scaffolding` | `420`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.scaffolding.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:

| Name        | Default value | Allowed values                                              | Description                                                                                         |
|-------------|---------------|-------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| bottom      | `false`       | `false`<br/>`true`                                          | If this scaffolding is floating.                                                                    |
| distance    | `7`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7` | The distance from a center scaffolding horizontally. If it is 7, it becomes a falling block entity. |
| waterlogged | `false`       | `false`<br/>`true`                                          | Whether or not there's water in the same place as this scaffolding.                                 |

Bedrock Edition:

| Name            | Metadata Bits             | Default value | Allowed values                                              | Values forMetadata Bits                                     | Description                                                                                         |
|-----------------|---------------------------|---------------|-------------------------------------------------------------|-------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| stability       | `0x2`<br/>`0x4`<br/>`0x8` | `7`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7` | The distance from a center scaffolding horizontally. If it is 7, it becomes a falling block entity. |
| stability_check | `0x1`                     | `false`       | `false`<br/>`true`                                          | `0`<br/>`1`                                                 | If a scaffolding block has been checked for stability.[more information needed]                     |

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


