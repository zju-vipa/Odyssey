# Concrete Powder
Concrete powder is a gravity-affected block that is converted to concrete when touching water. It comes in the sixteen dye colors.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Crafting
	- 1.3 Renewability
- 2 Usage
	- 2.1 Creating concrete
	- 2.2 Note blocks
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Falling block entity
- 5 History
- 6 Issues
- 7 References
- 8 External links

## Obtaining
### Breaking
Concrete powder can be mined with any tool or by hand, but using a shovel is the quickest method.

| Block     | Concrete Powder       |
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

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Crafting
The crafting recipe is shapeless; the order of ingredients does not matter.

| Ingredients                       | Crafting recipe  | Description                                     |
|-----------------------------------|------------------|-------------------------------------------------|
| MatchingDye+<br/>Sand+<br/>Gravel | 8888888888888888 | Red sand cannot be used in place of sand.[1][2] |

| Ingredients                                                                        | Crafting recipe | Description                                      |
|------------------------------------------------------------------------------------|-----------------|--------------------------------------------------|
| Bone Mealor<br/>Lapis Lazulior<br/>Cocoa Beansor<br/>Ink Sac+<br/>Sand+<br/>Gravel | 8888            | ‌[Bedrock Edition and Minecraft Education  only] |

### Renewability
Concrete powder is renewable as all of its crafting ingredients are themselves renewable. However, sand is only renewably obtained through the wandering trader, which spawns infrequently and only allows a limited number of trades per spawn, making it impractical to obtain it (and by extension, concrete powder) through only renewable means.

## Usage
Normal sand falls through the water, while one of the pink concrete powder blocks solidifies immediately on contact with the water.
Concrete powder falls when there is a non-solid block beneath it.

### Creating concrete
Main article: Concrete
If a concrete powder block comes into contact with water, it solidifies into a block of concrete. Specifically, the block has to be placed into, placed next to, or fall into flowing water, a water source block, or a waterlogged block. If placed next to a waterlogged block, it must be adjacent to the sides where water can flow out from, such as the open sides of stairs, but not the back side of stairs or any sides of waterlogged leaves. It does not solidify in midair falling past water. If it lands next to water, it solidifies only after a block update. Rain or splash water bottles also have no effect on concrete powder. Concrete powder in item form also does not become concrete. Concrete powder placed directly at water makes the placement sound of concrete.

### Note blocks
Concrete powder can be placed under note blocks to produce "snare drum" sound.

## Data values
### ID
Java Edition:

| Name                       | Identifier                   | Form         | Block tags        | Translation key                              |
|----------------------------|------------------------------|--------------|-------------------|----------------------------------------------|
| White Concrete Powder      | `white_concrete_powder`      | Block & Item | `concrete_powder` | `block.minecraft.white_concrete_powder`      |
| Orange Concrete Powder     | `orange_concrete_powder`     | Block & Item | `concrete_powder` | `block.minecraft.orange_concrete_powder`     |
| Magenta Concrete Powder    | `magenta_concrete_powder`    | Block & Item | `concrete_powder` | `block.minecraft.magenta_concrete_powder`    |
| Light Blue Concrete Powder | `light_blue_concrete_powder` | Block & Item | `concrete_powder` | `block.minecraft.light_blue_concrete_powder` |
| Yellow Concrete Powder     | `yellow_concrete_powder`     | Block & Item | `concrete_powder` | `block.minecraft.yellow_concrete_powder`     |
| Lime Concrete Powder       | `lime_concrete_powder`       | Block & Item | `concrete_powder` | `block.minecraft.lime_concrete_powder`       |
| Pink Concrete Powder       | `pink_concrete_powder`       | Block & Item | `concrete_powder` | `block.minecraft.pink_concrete_powder`       |
| Gray Concrete Powder       | `gray_concrete_powder`       | Block & Item | `concrete_powder` | `block.minecraft.gray_concrete_powder`       |
| Light Gray Concrete Powder | `light_gray_concrete_powder` | Block & Item | `concrete_powder` | `block.minecraft.light_gray_concrete_powder` |
| Cyan Concrete Powder       | `cyan_concrete_powder`       | Block & Item | `concrete_powder` | `block.minecraft.cyan_concrete_powder`       |
| Purple Concrete Powder     | `purple_concrete_powder`     | Block & Item | `concrete_powder` | `block.minecraft.purple_concrete_powder`     |
| Blue Concrete Powder       | `blue_concrete_powder`       | Block & Item | `concrete_powder` | `block.minecraft.blue_concrete_powder`       |
| Brown Concrete Powder      | `brown_concrete_powder`      | Block & Item | `concrete_powder` | `block.minecraft.brown_concrete_powder`      |
| Green Concrete Powder      | `green_concrete_powder`      | Block & Item | `concrete_powder` | `block.minecraft.green_concrete_powder`      |
| Red Concrete Powder        | `red_concrete_powder`        | Block & Item | `concrete_powder` | `block.minecraft.red_concrete_powder`        |
| Black Concrete Powder      | `black_concrete_powder`      | Block & Item | `concrete_powder` | `block.minecraft.black_concrete_powder`      |

Bedrock Edition:

| Name                       | Identifier                   | Alias ID                               | Numeric ID | Form                       | Item ID[i 1]   | Translation key                      |
|----------------------------|------------------------------|----------------------------------------|------------|----------------------------|----------------|--------------------------------------|
| White Concrete Powder      | `white_concrete_powder`      | `concrete_powder, concretepowder / 0`  | `237`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.concretePowder.white.name`     |
| Orange Concrete Powder     | `orange_concrete_powder`     | `concrete_powder, concretepowder / 1`  | `-709`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.concretePowder.orange.name`    |
| Magenta Concrete Powder    | `magenta_concrete_powder`    | `concrete_powder, concretepowder / 2`  | `-710`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.concretePowder.magenta.name`   |
| Light Blue Concrete Powder | `light_blue_concrete_powder` | `concrete_powder, concretepowder / 3`  | `-711`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.concretePowder.lightBlue.name` |
| Yellow Concrete Powder     | `yellow_concrete_powder`     | `concrete_powder, concretepowder / 4`  | `-712`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.concretePowder.yellow.name`    |
| Lime Concrete Powder       | `lime_concrete_powder`       | `concrete_powder, concretepowder / 5`  | `-713`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.concretePowder.lime.name`      |
| Pink Concrete Powder       | `pink_concrete_powder`       | `concrete_powder, concretepowder / 6`  | `-714`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.concretePowder.pink.name`      |
| Gray Concrete Powder       | `gray_concrete_powder`       | `concrete_powder, concretepowder / 7`  | `-715`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.concretePowder.gray.name`      |
| Light Gray Concrete Powder | `light_gray_concrete_powder` | `concrete_powder, concretepowder / 8`  | `-716`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.concretePowder.silver.name`    |
| Cyan Concrete Powder       | `cyan_concrete_powder`       | `concrete_powder, concretepowder / 9`  | `-717`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.concretePowder.cyan.name`      |
| Purple Concrete Powder     | `purple_concrete_powder`     | `concrete_powder, concretepowder / 10` | `-718`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.concretePowder.purple.name`    |
| Blue Concrete Powder       | `blue_concrete_powder`       | `concrete_powder, concretepowder / 11` | `-719`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.concretePowder.blue.name`      |
| Brown Concrete Powder      | `brown_concrete_powder`      | `concrete_powder, concretepowder / 12` | `-720`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.concretePowder.brown.name`     |
| Green Concrete Powder      | `green_concrete_powder`      | `concrete_powder, concretepowder / 13` | `-721`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.concretePowder.green.name`     |
| Red Concrete Powder        | `red_concrete_powder`        | `concrete_powder, concretepowder / 14` | `-722`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.concretePowder.red.name`       |
| Black Concrete Powder      | `black_concrete_powder`      | `concrete_powder, concretepowder / 15` | `-723`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.concretePowder.black.name`     |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑ a b c d e f g h i j k l m n o pAvailable with /give command.
3. ↑ a b c d e f g h i j k l m n o pThe block's direct item form has the same id as the block.

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

