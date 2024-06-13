### Crafting ingredient
| Name                                                                                      | Ingredients                                               | Crafting recipe  | Description                                      |
|-------------------------------------------------------------------------------------------|-----------------------------------------------------------|------------------|--------------------------------------------------|
| Coarse Dirt                                                                               | Dirt+Gravel                                               | 4                |                                                  |
| Concrete Powder                                                                           | MatchingDye+Sand+Gravel                                   | 8888888888888888 | Red sand cannot be used in place of sand.[6][7]  |
| White Concrete PowderorBlue Concrete PowderorBrown Concrete PowderorBlack Concrete Powder | Bone MealorLapis LazuliorCocoa BeansorInk Sac+Sand+Gravel | 8888             | ‌[Bedrock Edition and Minecraft Education  only] |

### Trading
Novice-level fletcher villagers have a 50%‌[Bedrock Edition  only] or 2⁄3‌[Java Edition  only] chance to buy 10 gravel and one emerald for 10 flint as part of their trade.

### Note blocks
Gravel can be placed under note blocks to produce snare drum sounds.

## Data values
### ID
Java Edition:

| Name   | Identifier | Form         | Block tags                                                                  | Translation key        |
|--------|------------|--------------|-----------------------------------------------------------------------------|------------------------|
| Gravel | gravel     | Block & Item | bamboo_plantable_onenderman_holdablelush_ground_replaceable‌mineable/shovel | block.minecraft.gravel |

Bedrock Edition:

| Name   | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key  |
|--------|------------|------------|----------------------------|----------------|------------------|
| Gravel | gravel     | 13         | Block & Giveable Item[i 2] | Identical[i 3] | tile.gravel.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


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


