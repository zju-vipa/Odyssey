# Suspicious Gravel
Suspicious gravel is a fragile gravity-affected block found in various Overworld structures. They can be brushed to extract structure-dependent loot, and are the only source of pottery sherds alongside suspicious sand. Suspicious gravel drops nothing if broken, and break if they fall from any height or are moved with a piston.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
- 2 Usage
	- 2.1 Brushing
	- 2.2 Loot
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
	- 4.3 Block data
	- 4.4 Falling block entity
- 5 Advancements
- 6 History
- 7 Issues
- 8 Gallery
	- 8.1 Development Images
- 9 References

## Obtaining
### Breaking
Suspicious gravel is unobtainable by mining, even using a tool enchanted with Silk Touch. They are much softer than normal gravel, and can be instantly broken with merely an unenchanted diamond shovel. They are affected by gravity, but they always break with no drop after falling. They break immediately if pushed by a piston or sticky piston, and cannot be pulled by sticky pistons or slime blocks. They also break immediately without drop when affected by explosion.

In Java Edition, suspicious gravel drops as an item if it falls for more than 30 seconds, which can be achieved by falling into an upward bubble column, or through two cobwebs stacked on top of each other.[1] However, it does not retain its loot.

In Creative mode, the player can obtain suspicious gravel while retaining its loot by using Ctrl + pick block on the block.

| Block     | Suspicious Gravel     |
|-----------|-----------------------|
| Hardness  | 0.25                  |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 0.4                   |
| Wooden    | 0.2                   |
| Stone     | 0.1                   |
| Iron      | 0.1                   |
| Diamond   | 0.05                  |
| Netherite | 0.05                  |
| Golden    | 0.05                  |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
Suspicious gravel generates naturally in cold ocean ruins. Additionally, some of the gravel within trail ruins is replaced with suspicious gravel upon generation.


## Usage
### Brushing
When a brush is used on suspicious gravel, cracks start to appear on all sides of the block as the dusted block state of the block starts to increase. If the suspicious gravel being brushed is naturally generated, an item gradually emerges from the side where the player starts brushing. After 96 (6+20+30+40 per stage) game ticks (4.8 seconds), the item is extracted, and the suspicious gravel is converted into gravel.

If the player stops brushing a suspicious gravel, the block remains in its half-excavated state for a few seconds, before gradually returning to its unexcavated state one stage at a time.

### Loot
The item obtained and the loot table of suspicious gravel is dependent on which structure it has generated in. Items can be extracted only from naturally generated suspicious gravel. When placed by the player, nothing is produced after brushing.

In Java Edition, each trail ruin's suspicious gravel contains 1 item stack,  with the following distribution: 

| Item                          | Stack Size  [A] | Weight   [B]   | Chance   [C] | Avg.per block   [D] | Avg. # blocksto brush   [E] |
|-------------------------------|-----------------|----------------|--------------|---------------------|-----------------------------|
| Blue Dye                      | 1               | $\frac{2}{45}$ | 4.4%         | 0.044               | 22.5                        |
| Brick                         | 1               | $\frac{2}{45}$ | 4.4%         | 0.044               | 22.5                        |
| Brown Candle                  | 1               | $\frac{2}{45}$ | 4.4%         | 0.044               | 22.5                        |
| Emerald                       | 1               | $\frac{2}{45}$ | 4.4%         | 0.044               | 22.5                        |
| Green Candle                  | 1               | $\frac{2}{45}$ | 4.4%         | 0.044               | 22.5                        |
| Light Blue Dye                | 1               | $\frac{2}{45}$ | 4.4%         | 0.044               | 22.5                        |
| Orange Dye                    | 1               | $\frac{2}{45}$ | 4.4%         | 0.044               | 22.5                        |
| Purple Candle                 | 1               | $\frac{2}{45}$ | 4.4%         | 0.044               | 22.5                        |
| Red Candle                    | 1               | $\frac{2}{45}$ | 4.4%         | 0.044               | 22.5                        |
| Wheat                         | 1               | $\frac{2}{45}$ | 4.4%         | 0.044               | 22.5                        |
| White Dye                     | 1               | $\frac{2}{45}$ | 4.4%         | 0.044               | 22.5                        |
| Wooden Hoe                    | 1               | $\frac{2}{45}$ | 4.4%         | 0.044               | 22.5                        |
| Yellow Dye                    | 1               | $\frac{2}{45}$ | 4.4%         | 0.044               | 22.5                        |
| Beetroot Seeds                | 1               | $\frac{1}{45}$ | 2.2%         | 0.022               | 45.0                        |
| Blue Stained Glass Pane       | 1               | $\frac{1}{45}$ | 2.2%         | 0.022               | 45.0                        |
| Coal                          | 1               | $\frac{1}{45}$ | 2.2%         | 0.022               | 45.0                        |
| Dead Bush                     | 1               | $\frac{1}{45}$ | 2.2%         | 0.022               | 45.0                        |
| Flower Pot                    | 1               | $\frac{1}{45}$ | 2.2%         | 0.022               | 45.0                        |
| Lead                          | 1               | $\frac{1}{45}$ | 2.2%         | 0.022               | 45.0                        |
| Light Blue Stained Glass Pane | 1               | $\frac{1}{45}$ | 2.2%         | 0.022               | 45.0                        |
| Magenta Stained Glass Pane    | 1               | $\frac{1}{45}$ | 2.2%         | 0.022               | 45.0                        |
| Oak Hanging Sign              | 1               | $\frac{1}{45}$ | 2.2%         | 0.022               | 45.0                        |
| Pink Stained Glass Pane       | 1               | $\frac{1}{45}$ | 2.2%         | 0.022               | 45.0                        |
| Purple Stained Glass Pane     | 1               | $\frac{1}{45}$ | 2.2%         | 0.022               | 45.0                        |
| Red Stained Glass Pane        | 1               | $\frac{1}{45}$ | 2.2%         | 0.022               | 45.0                        |
| Spruce Hanging Sign           | 1               | $\frac{1}{45}$ | 2.2%         | 0.022               | 45.0                        |
| String                        | 1               | $\frac{1}{45}$ | 2.2%         | 0.022               | 45.0                        |
| Wheat Seeds                   | 1               | $\frac{1}{45}$ | 2.2%         | 0.022               | 45.0                        |
| Yellow Stained Glass Pane     | 1               | $\frac{1}{45}$ | 2.2%         | 0.022               | 45.0                        |
| Gold Nugget                   | 1               | $\frac{1}{45}$ | 2.2%         | 0.022               | 45.0                        |

In Bedrock Edition, each trail ruin's suspicious gravel contains 1 item stack,  with the following distribution: 

| Item                          | Stack Size  [A] | Weight   [B]   | Chance   [C] | Avg.per block   [D] | Avg. # blocksto brush   [E] |
|-------------------------------|-----------------|----------------|--------------|---------------------|-----------------------------|
| Brick                         | 1               | $\frac{4}{46}$ | 8.7%         | 0.087               | 11.5                        |
| Blue Dye                      | 1               | $\frac{2}{46}$ | 4.3%         | 0.043               | 23.0                        |
| Brown Candle                  | 1               | $\frac{2}{46}$ | 4.3%         | 0.043               | 23.0                        |
| Clay Ball                     | 1               | $\frac{2}{46}$ | 4.3%         | 0.043               | 23.0                        |
| Emerald                       | 1               | $\frac{2}{46}$ | 4.3%         | 0.043               | 23.0                        |
| Green Candle                  | 1               | $\frac{2}{46}$ | 4.3%         | 0.043               | 23.0                        |
| Light Blue Dye                | 1               | $\frac{2}{46}$ | 4.3%         | 0.043               | 23.0                        |
| Orange Dye                    | 1               | $\frac{2}{46}$ | 4.3%         | 0.043               | 23.0                        |
| Purple Candle                 | 1               | $\frac{2}{46}$ | 4.3%         | 0.043               | 23.0                        |
| Red Candle                    | 1               | $\frac{2}{46}$ | 4.3%         | 0.043               | 23.0                        |
| Wheat                         | 1               | $\frac{2}{46}$ | 4.3%         | 0.043               | 23.0                        |
| White Dye                     | 1               | $\frac{2}{46}$ | 4.3%         | 0.043               | 23.0                        |
| Wooden Hoe                    | 1               | $\frac{2}{46}$ | 4.3%         | 0.043               | 23.0                        |
| Yellow Dye                    | 1               | $\frac{2}{46}$ | 4.3%         | 0.043               | 23.0                        |
| Beetroot Seeds                | 1               | $\frac{1}{46}$ | 2.2%         | 0.022               | 46.0                        |
| Blue Stained Glass Pane       | 1               | $\frac{1}{46}$ | 2.2%         | 0.022               | 46.0                        |
| Dead Bush                     | 1               | $\frac{1}{46}$ | 2.2%         | 0.022               | 46.0                        |
| Flower Pot                    | 1               | $\frac{1}{46}$ | 2.2%         | 0.022               | 46.0                        |
| Lead                          | 1               | $\frac{1}{46}$ | 2.2%         | 0.022               | 46.0                        |
| Light Blue Stained Glass Pane | 1               | $\frac{1}{46}$ | 2.2%         | 0.022               | 46.0                        |
| Magenta Stained Glass Pane    | 1               | $\frac{1}{46}$ | 2.2%         | 0.022               | 46.0                        |
| Oak Hanging Sign              | 1               | $\frac{1}{46}$ | 2.2%         | 0.022               | 46.0                        |
| Pink Stained Glass Pane       | 1               | $\frac{1}{46}$ | 2.2%         | 0.022               | 46.0                        |
| Purple Stained Glass Pane     | 1               | $\frac{1}{46}$ | 2.2%         | 0.022               | 46.0                        |
| Red Stained Glass Pane        | 1               | $\frac{1}{46}$ | 2.2%         | 0.022               | 46.0                        |
| Spruce Hanging Sign           | 1               | $\frac{1}{46}$ | 2.2%         | 0.022               | 46.0                        |
| String                        | 1               | $\frac{1}{46}$ | 2.2%         | 0.022               | 46.0                        |
| Wheat Seeds                   | 1               | $\frac{1}{46}$ | 2.2%         | 0.022               | 46.0                        |
| Yellow Stained Glass Pane     | 1               | $\frac{1}{46}$ | 2.2%         | 0.022               | 46.0                        |
| Gold Nugget                   | 1               | $\frac{1}{46}$ | 2.2%         | 0.022               | 46.0                        |



↑ a b The size of stacks (or for unstackable items, number) of this item on any given roll.

↑ a b The weight of this item relative to other items in the pool.

↑ a b The odds of finding any of this item in a single chest.

↑ a b The number of items expected per chest, averaged over a large number of chests.

↑ a b The average number of chests the player should expect to search to find any of this item.



In Java Edition and Bedrock Edition, each trail ruin's rare suspicious gravel contains 1 item stack,  with the following distribution: 

| Item                                   | Stack Size  [A] | Weight   [B]   | Chance   [C] | Avg.per block   [D] | Avg. # blocksto brush   [E] |
|----------------------------------------|-----------------|----------------|--------------|---------------------|-----------------------------|
| Burn Pottery Sherd                     | 1               | $\frac{1}{12}$ | 8.3%         | 0.083               | 12.0                        |
| Danger Pottery Sherd                   | 1               | $\frac{1}{12}$ | 8.3%         | 0.083               | 12.0                        |
| Music Disc (Relic)                     | 1               | $\frac{1}{12}$ | 8.3%         | 0.083               | 12.0                        |
| Friend Pottery Sherd                   | 1               | $\frac{1}{12}$ | 8.3%         | 0.083               | 12.0                        |
| Heart Pottery Sherd                    | 1               | $\frac{1}{12}$ | 8.3%         | 0.083               | 12.0                        |
| Heartbreak Pottery Sherd               | 1               | $\frac{1}{12}$ | 8.3%         | 0.083               | 12.0                        |
| Host Armor Trim Smithing Template      | 1               | $\frac{1}{12}$ | 8.3%         | 0.083               | 12.0                        |
| Howl Pottery Sherd                     | 1               | $\frac{1}{12}$ | 8.3%         | 0.083               | 12.0                        |
| Raiser Armor Trim Smithing Template    | 1               | $\frac{1}{12}$ | 8.3%         | 0.083               | 12.0                        |
| Shaper Armor Trim Smithing Template    | 1               | $\frac{1}{12}$ | 8.3%         | 0.083               | 12.0                        |
| Sheaf Pottery Sherd                    | 1               | $\frac{1}{12}$ | 8.3%         | 0.083               | 12.0                        |
| Wayfinder Armor Trim Smithing Template | 1               | $\frac{1}{12}$ | 8.3%         | 0.083               | 12.0                        |



↑ The size of stacks (or for unstackable items, number) of this item on any given roll.

↑ The weight of this item relative to other items in the pool.

↑ The odds of finding any of this item in a single chest.

↑ The number of items expected per chest, averaged over a large number of chests.

↑ The average number of chests the player should expect to search to find any of this item.



In Java Edition and Bedrock Edition, each cold ocean ruin's suspicious gravel contains 1 item stack,  with the following distribution: 

| Item                   | Stack Size  [A] | Weight   [B]   | Chance   [C] | Avg.per block   [D] | Avg. # blocksto brush   [E] |
|------------------------|-----------------|----------------|--------------|---------------------|-----------------------------|
| Coal                   | 1               | $\frac{2}{15}$ | 13.3%        | 0.133               | 7.5                         |
| Emerald                | 1               | $\frac{2}{15}$ | 13.3%        | 0.133               | 7.5                         |
| Wheat                  | 1               | $\frac{2}{15}$ | 13.3%        | 0.133               | 7.5                         |
| Wooden Hoe             | 1               | $\frac{2}{15}$ | 13.3%        | 0.133               | 7.5                         |
| Gold Nugget            | 1               | $\frac{2}{15}$ | 13.3%        | 0.133               | 7.5                         |
| Blade Pottery Sherd    | 1               | $\frac{1}{15}$ | 6.7%         | 0.067               | 15.0                        |
| Explorer Pottery Sherd | 1               | $\frac{1}{15}$ | 6.7%         | 0.067               | 15.0                        |
| Mourner Pottery Sherd  | 1               | $\frac{1}{15}$ | 6.7%         | 0.067               | 15.0                        |
| Plenty Pottery Sherd   | 1               | $\frac{1}{15}$ | 6.7%         | 0.067               | 15.0                        |
| Iron Axe               | 1               | $\frac{1}{15}$ | 6.7%         | 0.067               | 15.0                        |



↑ The size of stacks (or for unstackable items, number) of this item on any given roll.

↑ The weight of this item relative to other items in the pool.

↑ The odds of finding any of this item in a single chest.

↑ The number of items expected per chest, averaged over a large number of chests.

↑ The average number of chests the player should expect to search to find any of this item.



## Data values
### ID
Java Edition:

| Name              | Identifier          | Form         | Block tags                                                                                        | Item tags | Translation key                     |
|-------------------|---------------------|--------------|---------------------------------------------------------------------------------------------------|-----------|-------------------------------------|
| Suspicious Gravel | `suspicious_gravel` | Block & Item | `bamboo_plantable_on`<br/>`enderman_holdable`<br/>`lush_ground_replaceable`<br/>`mineable/shovel` | None      | `block.minecraft.suspicious_gravel` |

| Name         | Identifier        |
|--------------|-------------------|
| Block entity | `brushable_block` |

Bedrock Edition:

| Name              | Identifier          | Numeric ID | Form                       | Item ID[i 1]   | Translation key               |
|-------------------|---------------------|------------|----------------------------|----------------|-------------------------------|
| Suspicious Gravel | `suspicious_gravel` | `-573`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.suspicious_gravel.name` |

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

