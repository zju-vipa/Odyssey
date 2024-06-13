### Crafting ingredient
| Name                                                                                      | Ingredients                                               | Crafting recipe  | Description                                                 |
|-------------------------------------------------------------------------------------------|-----------------------------------------------------------|------------------|-------------------------------------------------------------|
| Concrete Powder                                                                           | MatchingDye+Sand+Gravel                                   | 8888888888888888 | Red sand cannot be used in place of sand.[2][3]             |
| Sandstone                                                                                 | Sand                                                      |                  |                                                             |
| TNT                                                                                       | Gunpowder+Sand                                            |                  | It is possible to use any combination of sand and red sand. |
| White Concrete PowderorBlue Concrete PowderorBrown Concrete PowderorBlack Concrete Powder | Bone MealorLapis LazuliorCocoa BeansorInk Sac+Sand+Gravel | 8888             | ‌[Bedrock Edition and Minecraft Education  only]            |

### Smelting ingredient
| Name  | Ingredients  | Smelting recipe |
|-------|--------------|-----------------|
| Glass | Sand+Anyfuel | 0.1             |

### Construction
Sand can be used in the construction of airlocks and mob suffocation traps. Because sand falls, it can also be used for construction underwater while the player remains above the surface of the water.

### Farms
Sand is required for farming cactus, and can also be used for farming bamboo, sugar cane and kelp.

### Hatching
A turtle egg can hatch only if it's on sand.

### Note Blocks
Sand can be placed under note blocks to produce "snare drum" sound.

## Data values
### ID
Java Edition:

| Name | Identifier | Form         | Block tags                                                                     | Item tags | Translation key      |
|------|------------|--------------|--------------------------------------------------------------------------------|-----------|----------------------|
| Sand | sand       | Block & Item | bamboo_plantable_onenderman_holdablesandlush_ground_replaceablemineable/shovel | sand      | block.minecraft.sand |

Bedrock Edition:

| Name | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key        |
|------|------------|------------|----------------------------|----------------|------------------------|
| Sand | sand       | 12         | Block & Giveable Item[i 2] | Identical[i 3] | tile.sand.default.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block states

In Bedrock Edition, sand uses the following block states:

Bedrock Edition:

| Name      | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description |
|-----------|---------------|---------------|----------------|-------------------------|-------------|
| sand_type | 0x1           | normal        | normal         | 0                       | Sand        |
|           |               |               | red            | 1                       | Red Sand    |



### Falling block entity

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
Main article: Falling Block

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

## See also
- Explained physics offalling blocks.
- Desert
- Sandstone


