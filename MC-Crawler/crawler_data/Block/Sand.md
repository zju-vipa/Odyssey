# Sand
Sand is a gravity-affected block found abundantly in deserts and beaches, and less commonly in or near surface water.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Chest loot
	- 1.4 Trading
	- 1.5 Post-generation
	- 1.6 Renewability
- 2 Usage
	- 2.1 Crafting ingredient
	- 2.2 Smelting ingredient
	- 2.3 Construction
	- 2.4 Farms
	- 2.5 Hatching
	- 2.6 Note Blocks
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
	- 4.3 Falling block entity
- 5 History
	- 5.1 Data history
- 6 Issues
- 7 Trivia
- 8 Gallery
	- 8.1 Java Edition
- 9 See also
- 10 References
- 11 External links

## Obtaining
### Breaking
Sand can be broken without tools, but a shovel is the fastest method of obtaining it.

| Block     | Sand                  |
|-----------|-----------------------|
| Hardness  | 0.5                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 0.75                  |
| Wooden    | 0.4                   |
| Stone     | 0.2                   |
| Iron      | 0.15                  |
| Diamond   | 0.1                   |
| Netherite | 0.1                   |
| Golden    | 0.1                   |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


### Natural generation
Sand generates naturally in many biomes of the Overworld, in disk-like formations near ponds and rivers. It generates in abundance in deserts and beaches, generally in four-block-deep layers, supported by sandstone below. Sand also generates as the ocean floor of lukewarm oceans, deep lukewarm oceans and warm oceans, in a single layer not supported by sandstone. It usually generates in quantities of 545 blocks per chunk on average in non-desert biomes.[verify]

Sand is also used to cover up buried treasure chests depending on where the chest generates in. (In this case, sand is used to cover up buried treasure chests that generate in beaches and ocean floors that are composed of sand, but in some cases stone or sandstone might be used instead).

Sand also generates as part of warm ocean ruins, some desert village houses, desert wells, and desert pyramids.

Both types of sand can spawn floating in the air. The floating cluster of sand falls when one of the sand blocks receives an update (e.g. when a block is placed near it or when a block near it is broken).


### Chest loot
| Item | Structure      | Container | Quantity | Chance                         |
|------|----------------|-----------|----------|--------------------------------|
|      |                |           |          | Java EditionandBedrock Edition |
| Sand | Desert Pyramid | Chest     | 1–8      | 59%                            |

### Trading
Wandering traders sell 8 sand for one emerald.‌

### Post-generation
After brushing suspicious sand, the suspicious sand turns into regular sand.

### Renewability
The only renewable method of obtaining either type of sand is through the wandering trader. Due to its low spawning rate and limited number of trades per spawn, it is more practical to obtain it through other means.

## Usage
Main article: Falling Block
If the supporting block below a block of sand is removed, it falls until it lands on the next available block. More specifically, the sand block turns into a "falling block" entity, which is affected by gravity; when the falling block lands on a block with a solid top surface, it becomes a block again. More information about the falling block entity is available in the main article listed above.

If falling sand lands and covers the head of a mob or the player, the mob or player buried in it continuously receives suffocation damage. If falling sand lands in the space occupied by a non-solid block (such as torch, rail, or redstone dust) or a block less than a full block tall (such as slab or soul sand[1]), the sand drops and turns into an item. If it falls onto a cobweb, it falls slowly until it has gone through completely; if it touches the ground while still inside the cobweb, the sand becomes an item. Sand that falls onto a lifting bubble column floats on top of the water until the bubble column is blocked or removed.

Though TNT does not break any blocks if it explodes underwater, if sand, concrete powder (in one-block-deep water only), or gravel falls and covers the TNT before it explodes, blocks are broken as normal. This trick can be used to collect blocks underwater, or break into underwater structures such as the ocean monument without mining.

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

