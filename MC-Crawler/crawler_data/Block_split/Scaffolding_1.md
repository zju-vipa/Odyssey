### Fuel
Scaffolding can be used as a fuel in furnaces, smelting 0.25 items per block.

## Data values
### ID
Java Edition:

| Name        | Identifier  | Form         | Block tags | Translation key             |
|-------------|-------------|--------------|------------|-----------------------------|
| Scaffolding | scaffolding | Block & Item | climbable  | block.minecraft.scaffolding |

Bedrock Edition:

| Name        | Identifier  | Numeric ID | Form                       | Item ID[i 1]   | Translation key       |
|-------------|-------------|------------|----------------------------|----------------|-----------------------|
| Scaffolding | scaffolding | 420        | Block & Giveable Item[i 2] | Identical[i 3] | tile.scaffolding.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block states

Java Edition:

| Name        | Default value | Allowed values | Description                                                                                         |
|-------------|---------------|----------------|-----------------------------------------------------------------------------------------------------|
| bottom      | false         | falsetrue      | If this scaffolding is floating.                                                                    |
| distance    | 7             | 01234567       | The distance from a center scaffolding horizontally. If it is 7, it becomes a falling block entity. |
| waterlogged | false         | falsetrue      | Whether or not there's water in the same place as this scaffolding.                                 |

Bedrock Edition:

| Name            | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                                                                         |
|-----------------|---------------|---------------|----------------|-------------------------|-----------------------------------------------------------------------------------------------------|
| stability       | 0x20x40x8     | 7             | 01234567       | 01234567                | The distance from a center scaffolding horizontally. If it is 7, it becomes a falling block entity. |
| stability_check | 0x1           | false         | falsetrue      | 01                      | If a scaffolding block has been checked for stability.[more information needed]                     |

### Falling block entity
Main article: Falling Block

Falling Block




Hitbox size


Height: 0.98 BlocksWidth: 0.98 Blocks 




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

 Dynamic block entity data
Tags common to all entities
 BlockState: The falling block represented by this entity.
 Name: The resource location of the block.
 Properties: Optional. The block states of the block.
 Name: The block state name and its value.
 CancelDrop: 1 or 0 (true/false) - true if the block should be destroyed instead of placed after landing on a solid block. When true, the block is not dropped as an item, even if the DropItem tag is set to true. However, if the entity is deleted due to its Time value being too high, this tag is ignored and an item is dropped depending on the DropItem tag. CancelDrop defaults to 1 for falling suspicious sand and suspicious gravel, and 0 for the other vanilla falling blocks and any summoned falling block.
 DropItem: 1 or 0 (true/false) – true if the block should drop as an item when it breaks. Any block that does not have an item form with the same ID as the block does not drop even if this is set.
 FallHurtAmount: Multiplied by the FallDistance to calculate the amount of damage to inflict. By default this value is 2 for anvils, and 6 for pointed dripstone.
 FallHurtMax: The maximum hit points of damage to inflict on entities that intersect this falling block. For vanilla falling blocks, always 40 × 20.
 HurtEntities: 1 or 0 (true/false) – true if the block should hurt entities it falls on. Defaults to 1 for anvils and pointed dripstone and to 0 for the other vanilla falling blocks and any summoned falling block.
 TileEntityData: Optional. The tags of the block entity for this block.
 Time: The number of ticks the entity has existed. When Time goes above 600, or above 100 while the block is at Y=-64 or is outside building height, the entity is deleted.


