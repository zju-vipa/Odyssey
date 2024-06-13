# Gravel
Gravel is a gravity-affected block found in the Overworld and the Nether. It is a source of flint, which has a chance to drop when gravel is broken.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Mob loot
	- 1.4 Bartering
- 2 Usage
	- 2.1 Crafting ingredient
	- 2.2 Trading
	- 2.3 Note blocks
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Falling block entity
- 5 History
	- 5.1 Data history
- 6 Issues
- 7 Trivia
- 8 Gallery
	- 8.1 Screenshots
- 9 References
- 10 External links

## Obtaining
### Breaking
Gravel can be broken using any tool, but a shovel is the quickest. When broken, it has a 10% chance of dropping flint instead of the gravel itself. The flint received can be controlled with enchantments: Silk Touch removes the chance of dropping flint; Fortune increases the chance to 14% at the level I, 25% at level II, and 100% at level III.[1][2]

| Block     | Gravel                |
|-----------|-----------------------|
| Hardness  | 0.6                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 0.9                   |
| Wooden    | 0.45                  |
| Stone     | 0.25                  |
| Iron      | 0.15                  |
| Diamond   | 0.15                  |
| Netherite | 0.1                   |
| Golden    | 0.1                   |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


If gravel falls onto a non-full block, it drops as an item and does not drop flint.[3][4]

### Natural generation
Gravel is generated in disks in rivers, shallow oceans and small pools of water; in windswept gravelly hills biomes covering most of the surface; underwater covering the bottom of sufficiently deep rivers and normal, cold, and frozen ocean biomes, as well as their deep variants; and in the form of strips in stony shores.

Gravel can generate in the Overworld in the form of ore features. Gravel attempts to generate 14 times per chunk in ore features of size 0-160, at all levels and in all biomes. It can replace stone, granite, andesite, diorite, polished granite‌[BE  only], polished andesite‌[BE  only], polished diorite‌[BE  only], tuff‌[JE  only], and deepslate‌[JE  only].

Gravel can also generate as part of cold ocean ruins and trail ruins.

In the Nether, gravel generates naturally in layers along the shores of the lava sea, in all biomes except crimson and warped forests. The layers are one block deep in nether wastes, and 3-5 blocks deep in soul sand valley and basalt deltas.

Ore features of gravel in the Nether attempt to replace netherrack 2 times per chunk in blobs of size 0-160, from levels 5 to 41‌[JE  only] or 36‌[BE  only], in all Nether biomes except basalt deltas.


### Mob loot
An enderman holding gravel always drops the block upon death.

### Bartering
Piglins may barter 8-16 gravel when given a gold ingot.

## Usage
Main article: Falling Block
If the supporting block below a block of gravel is removed, it falls until it lands on the next available block. More specifically, the gravel block turns into a "falling block" entity, which is affected by gravity; when the falling block lands on a block with a solid top surface, it becomes a block again. More information about the falling block entity are available in the main article listed above.

When gravel falls on a player or mob, it can engulf the head, resulting in suffocation inside gravel until destroying the block, moving out of it, or dying. If falling gravel lands in a space occupied by a non-solid block (such as torches, rails, or redstone dust) or non-full block (such as slabs or soul sand[5]), it breaks and turns into a gravel item. Gravel falls slowly through a cobweb until it passes completely through, or until it touches any block, at which point it drops and becomes a gravel item.

Gravel can be placed on a non-solid block without falling.

Bamboo can be placed and grown on gravel.

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

