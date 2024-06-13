# Suspicious Sand
Suspicious sand is a fragile gravity-affected block found in various Overworld structures. They can be brushed to extract structure-dependent loot, and are the only source of pottery sherds alongside suspicious gravel. Suspicious sand drops nothing if broken, and break if they fall from any height or are moved with a piston.

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
Suspicious sand is unobtainable by mining, even using a tool enchanted with Silk Touch. They are much softer than normal sand, and can be instantly broken with merely an unenchanted diamond shovel. They are affected by gravity, but they always break with no drop after falling. They break immediately if pushed by a piston or sticky piston, and cannot be pulled by sticky pistons or slime blocks. They also break immediately without drop when affected by explosion.

In Java Edition, suspicious sand drops as an item if it falls for more than 30 seconds, which can be achieved by falling into an upward bubble column, or through two cobwebs stacked on top of each other.[1] However, it does not retain its loot. It is also not clear if this block is intended to be obtained this way.

In Creative mode, the player can obtain suspicious sand while retaining its loot by using Ctrl + pick block on the block.

| Block     | Suspicious Sand       |
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
Suspicious sand generates naturally in buried rooms under desert pyramids, as well as in the bottom of desert wells. It also generates within warm ocean ruins.


## Usage
### Brushing
When a brush is used on a suspicious sand, cracks start to appear on all sides of the block as the dusted block state of the block starts to increase. If the suspicious sand being brushed is naturally generated, an item gradually emerges from the side where the player starts brushing. After 96 (6+20+30+40 per stage) game ticks (4.8 seconds), the item is extracted, and the suspicious sand is converted into sand.

If the player stops brushing a suspicious sand, the block remains in its half-excavated state for a few seconds, before gradually returning to its unexcavated state one stage at a time.

### Loot
The item obtained and the loot table of suspicious sand is dependent on which structure it has generated in. Items can be extracted only from naturally generated suspicious sand. When placed by the player, nothing is produced after brushing.

In Java Edition and Bedrock Edition, each warm ocean ruin's suspicious sand contains 1 item stack,  with the following distribution: 

| Item                  | Stack Size  [A] | Weight   [B]   | Chance   [C] | Avg.per block   [D] | Avg. # blocksto brush   [E] |
|-----------------------|-----------------|----------------|--------------|---------------------|-----------------------------|
| Coal                  | 1               | $\frac{2}{15}$ | 13.3%        | 0.133               | 7.5                         |
| Emerald               | 1               | $\frac{2}{15}$ | 13.3%        | 0.133               | 7.5                         |
| Wheat                 | 1               | $\frac{2}{15}$ | 13.3%        | 0.133               | 7.5                         |
| Wooden Hoe            | 1               | $\frac{2}{15}$ | 13.3%        | 0.133               | 7.5                         |
| Gold Nugget           | 1               | $\frac{2}{15}$ | 13.3%        | 0.133               | 7.5                         |
| Angler Pottery Sherd  | 1               | $\frac{1}{15}$ | 6.7%         | 0.067               | 15.0                        |
| Shelter Pottery Sherd | 1               | $\frac{1}{15}$ | 6.7%         | 0.067               | 15.0                        |
| Sniffer Egg           | 1               | $\frac{1}{15}$ | 6.7%         | 0.067               | 15.0                        |
| Snort Pottery Sherd   | 1               | $\frac{1}{15}$ | 6.7%         | 0.067               | 15.0                        |
| Iron Axe              | 1               | $\frac{1}{15}$ | 6.7%         | 0.067               | 15.0                        |



↑ The size of stacks (or for unstackable items, number) of this item on any given roll.

↑ The weight of this item relative to other items in the pool.

↑ The odds of finding any of this item in a single chest.

↑ The number of items expected per chest, averaged over a large number of chests.

↑ The average number of chests the player should expect to search to find any of this item.



In Java Edition and Bedrock Edition, each desert temple's suspicious sand contains 1 item stack,  with the following distribution: 

| Item                 | Stack Size  [A] | Weight   [B]  | Chance   [C] | Avg.per block   [D] | Avg. # blocksto brush   [E] |
|----------------------|-----------------|---------------|--------------|---------------------|-----------------------------|
| Archer Pottery Sherd | 1               | $\frac{1}{8}$ | 12.5%        | 0.125               | 8.0                         |
| Emerald              | 1               | $\frac{1}{8}$ | 12.5%        | 0.125               | 8.0                         |
| Gunpowder            | 1               | $\frac{1}{8}$ | 12.5%        | 0.125               | 8.0                         |
| Miner Pottery Sherd  | 1               | $\frac{1}{8}$ | 12.5%        | 0.125               | 8.0                         |
| Prize Pottery Sherd  | 1               | $\frac{1}{8}$ | 12.5%        | 0.125               | 8.0                         |
| Skull Pottery Sherd  | 1               | $\frac{1}{8}$ | 12.5%        | 0.125               | 8.0                         |
| TNT                  | 1               | $\frac{1}{8}$ | 12.5%        | 0.125               | 8.0                         |
| Diamond              | 1               | $\frac{1}{8}$ | 12.5%        | 0.125               | 8.0                         |



↑ The size of stacks (or for unstackable items, number) of this item on any given roll.

↑ The weight of this item relative to other items in the pool.

↑ The odds of finding any of this item in a single chest.

↑ The number of items expected per chest, averaged over a large number of chests.

↑ The average number of chests the player should expect to search to find any of this item.



In Java Edition and Bedrock Edition, each desert well's suspicious sand contains 1 item stack,  with the following distribution: 

| Item                  | Stack Size  [A] | Weight   [B]  | Chance   [C] | Avg.per block   [D] | Avg. # blocksto brush   [E] |
|-----------------------|-----------------|---------------|--------------|---------------------|-----------------------------|
| Arms Up Pottery Sherd | 1               | $\frac{2}{8}$ | 25.0%        | 0.250               | 4.0                         |
| Brewer Pottery Sherd  | 1               | $\frac{2}{8}$ | 25.0%        | 0.250               | 4.0                         |
| Brick                 | 1               | $\frac{1}{8}$ | 12.5%        | 0.125               | 8.0                         |
| Emerald               | 1               | $\frac{1}{8}$ | 12.5%        | 0.125               | 8.0                         |
| Stick                 | 1               | $\frac{1}{8}$ | 12.5%        | 0.125               | 8.0                         |
| Suspicious Stew[F]    | 1               | $\frac{1}{8}$ | 12.5%        | 0.125               | 8.0                         |



↑ The size of stacks (or for unstackable items, number) of this item on any given roll.

↑ The weight of this item relative to other items in the pool.

↑ The odds of finding any of this item in a single chest.

↑ The number of items expected per chest, averaged over a large number of chests.

↑ The average number of chests the player should expect to search to find any of this item.

↑ The stew grants one of the following effects: 5–7 seconds of Blindness, 7–10 seconds of Jump Boost, 7-10 seconds of Night Vision, 10–20 seconds of Poison, 0.35-0.5 seconds of Saturation, or 6–8 seconds of Weakness.



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

