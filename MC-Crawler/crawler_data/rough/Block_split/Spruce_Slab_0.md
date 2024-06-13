# Wooden Slab
A wooden slab is a wooden variant of a slab, crafted from the respective planks.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
- 2 Usage
	- 2.1 Crafting ingredient
	- 2.2 Fuel
	- 2.3 Note blocks
- 3 Sounds
	- 3.1 Normal wood
	- 3.2 Cherry wood
	- 3.3 Bamboo wood
	- 3.4 Nether wood
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Gallery
	- 7.1 Renders
	- 7.2 Screenshots
- 8 References

## Obtaining
### Breaking
Wooden slabs can be broken with anything, but axes are fastest.

| Block     | Wooden Slab           |
|-----------|-----------------------|
| Hardness  | 2                     |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 3                     |
| Wooden    | 1.5                   |
| Stone     | 0.75                  |
| Iron      | 0.5                   |
| Diamond   | 0.4                   |
| Netherite | 0.35                  |
| Golden    | 0.25                  |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
Oak slabs generate as part of:

- Plainsvillages
- Woodland mansions
- Shipwrecks

Spruce slabs generate as part of:

- Igloobasements
- Woodland mansions
- Shipwrecks
- Taiga and snowy taigavillages

Birch slabs generate as part of:

- Woodland mansions
- Shipwrecks

Jungle and dark oak slabs generate as part of shipwrecks.

Acacia slabs generate as part of:

- Shipwrecks
- Savannavillages

### Crafting
| Ingredients    | Crafting recipe |
|----------------|-----------------|
| MatchingPlanks | 66666666666     |

## Usage
For information about the placement mechanics of all slabs, see Slab § Usage.

### Crafting ingredient
| Name               | Ingredients                                  | Crafting recipe |
|--------------------|----------------------------------------------|-----------------|
| Bamboo Mosaic      | Bamboo Slab                                  |                 |
| Barrel             | AnyPlanks+<br/>AnyWooden Slab                |                 |
| Chiseled Bookshelf | AnyPlanks+<br/>AnyWooden Slab                |                 |
| Composter          | AnyWooden Slab                               |                 |
| Daylight Detector  | Glass+<br/>Nether Quartz+<br/>AnyWooden Slab |                 |
| Lectern            | AnyWooden Slab+<br/>Bookshelf                |                 |

### Fuel
Overworld wooden slabs can be used as fuel in furnaces, smelting 0.75 items per slab in Java Edition, and 1.5 items per slab in Bedrock Edition.[1]

### Note blocks
Wooden slabs can be placed under note blocks to produce "bass" sounds.

## Data values
### ID
Java Edition:

| Name          | Identifier      | Form         | Block tags                                                             | Item tags                                           | Translation key                 |
|---------------|-----------------|--------------|------------------------------------------------------------------------|-----------------------------------------------------|---------------------------------|
| Oak Slab      | `oak_slab`      | Block & Item | `slabs`<br/>`wooden_slabs`<br/>`mineable/axe`                          | `slabs`<br/>`wooden_slabs`                          | `block.minecraft.oak_slab`      |
| Spruce Slab   | `spruce_slab`   | Block & Item | `slabs`<br/>`wooden_slabs`<br/>`mineable/axe`                          | `slabs`<br/>`wooden_slabs`                          | `block.minecraft.spruce_slab`   |
| Birch Slab    | `birch_slab`    | Block & Item | `slabs`<br/>`wooden_slabs`<br/>`mineable/axe`                          | `slabs`<br/>`wooden_slabs`                          | `block.minecraft.birch_slab`    |
| Jungle Slab   | `jungle_slab`   | Block & Item | `slabs`<br/>`wooden_slabs`<br/>`mineable/axe`                          | `slabs`<br/>`wooden_slabs`                          | `block.minecraft.jungle_slab`   |
| Acacia Slab   | `acacia_slab`   | Block & Item | `slabs`<br/>`wooden_slabs`<br/>`mineable/axe`                          | `slabs`<br/>`wooden_slabs`                          | `block.minecraft.acacia_slab`   |
| Dark Oak Slab | `dark_oak_slab` | Block & Item | `slabs`<br/>`wooden_slabs`<br/>`mineable/axe`                          | `slabs`<br/>`wooden_slabs`                          | `block.minecraft.dark_oak_slab` |
| Mangrove Slab | `mangrove_slab` | Block & Item | `slabs`<br/>`wooden_slabs`<br/>`mineable/axe`                          | `slabs`<br/>`wooden_slabs`                          | `block.minecraft.mangrove_slab` |
| Cherry Slab   | `cherry_slab`   | Block & Item | `slabs`<br/>`wooden_slabs`<br/>`mineable/axe`                          | `slabs`<br/>`wooden_slabs`                          | `block.minecraft.cherry_slab`   |
| Bamboo Slab   | `bamboo_slab`   | Block & Item | `slabs`<br/>`wooden_slabs`<br/>`mineable/axe`                          | `slabs`<br/>`wooden_slabs`                          | `block.minecraft.bamboo_slab`   |
| Crimson Slab  | `crimson_slab`  | Block & Item | `non_flammable_wood`<br/>`slabs`<br/>`wooden_slabs`<br/>`mineable/axe` | `non_flammable_wood`<br/>`slabs`<br/>`wooden_slabs` | `block.minecraft.crimson_slab`  |
| Warped Slab   | `warped_slab`   | Block & Item | `non_flammable_wood`<br/>`slabs`<br/>`wooden_slabs`<br/>`mineable/axe` | `non_flammable_wood`<br/>`slabs`<br/>`wooden_slabs` | `block.minecraft.warped_slab`   |

Bedrock Edition:

| Name                 | Identifier             | Alias ID                 | Numeric ID | Form                         | Item ID[i 1]   | Item tags                | Translation key                 |
|----------------------|------------------------|--------------------------|------------|------------------------------|----------------|--------------------------|---------------------------------|
| Oak Double Slab      | `oak_double_slab`      | `double_wooden_slab / 0` | `157`      | Block & Ungiveable Item[i 2] | Identical[i 3] | —                        | —                               |
| Oak Slab             | `oak_slab`             | `wooden_slab / 0`        | `158`      | Block & Giveable Item[i 4]   | Identical[i 3] | `minecraft:wooden_slabs` | `tile.wooden_slab.oak.name`     |
| Spruce Double Slab   | `spruce_double_slab`   | `double_wooden_slab / 1` | `-809`     | Block & Ungiveable Item[i 2] | Identical[i 3] | —                        | —                               |
| Spruce Slab          | `spruce_slab`          | `wooden_slab / 1`        | `-804`     | Block & Giveable Item[i 4]   | Identical[i 3] | `minecraft:wooden_slabs` | `tile.wooden_slab.spruce.name`  |
| Birch Double Slab    | `birch_double_slab`    | `double_wooden_slab / 2` | `-810`     | Block & Ungiveable Item[i 2] | Identical[i 3] | —                        | —                               |
| Birch Slab           | `birch_slab`           | `wooden_slab / 2`        | `-805`     | Block & Giveable Item[i 4]   | Identical[i 3] | `minecraft:wooden_slabs` | `tile.wooden_slab.birch.name`   |
| Jungle Double Slab   | `jungle_double_slab`   | `double_wooden_slab / 3` | `-811`     | Block & Ungiveable Item[i 2] | Identical[i 3] | —                        | —                               |
| Jungle Slab          | `jungle_slab`          | `wooden_slab / 3`        | `-806`     | Block & Giveable Item[i 4]   | Identical[i 3] | `minecraft:wooden_slabs` | `tile.wooden_slab.jungle.name`  |
| Acacia Double Slab   | `acacia_double_slab`   | `double_wooden_slab / 4` | `-812`     | Block & Ungiveable Item[i 2] | Identical[i 3] | —                        | —                               |
| Acacia Slab          | `acacia_slab`          | `wooden_slab / 4`        | `-807`     | Block & Giveable Item[i 4]   | Identical[i 3] | `minecraft:wooden_slabs` | `tile.wooden_slab.acacia.name`  |
| Dark Oak Double Slab | `dark_oak_double_slab` | `double_wooden_slab / 5` | `-813`     | Block & Ungiveable Item[i 2] | Identical[i 3] | —                        | —                               |
| Dark Oak Slab        | `dark_oak_slab`        | `wooden_slab / 5`        | `-808`     | Block & Giveable Item[i 4]   | Identical[i 3] | `minecraft:wooden_slabs` | `tile.wooden_slab.big_oak.name` |
| Mangrove Double Slab | `mangrove_double_slab` | None                     | `-499`     | Block & Ungiveable Item[i 2] | Identical[i 3] | —                        | —                               |
| Mangrove Slab        | `mangrove_slab`        | None                     | `-489`     | Block & Giveable Item[i 4]   | Identical[i 3] | `minecraft:wooden_slabs` | `tile.mangrove_slab.name`       |
| Cherry Double Slab   | `cherry_double_slab`   | None                     | `-540`     | Block & Ungiveable Item[i 2] | Identical[i 3] | —                        | `tile.cherry_double_slab.name`  |
| Cherry Slab          | `cherry_slab`          | None                     | `-539`     | Block & Giveable Item[i 4]   | Identical[i 3] | `minecraft:wooden_slabs` | `tile.cherry_slab.name`         |
| Bamboo Double Slab   | `bamboo_double_slab`   | None                     | `-521`     | Block & Ungiveable Item[i 2] | Identical[i 3] | —                        | —                               |
| Bamboo Slab          | `bamboo_slab`          | None                     | `-513`     | Block & Giveable Item[i 4]   | Identical[i 3] | `minecraft:wooden_slabs` | `tile.bamboo_slab.name`         |
| Crimson Double Slab  | `crimson_double_slab`  | None                     | `521`      | Block & Ungiveable Item[i 2] | Identical[i 3] | —                        | `tile.crimson_double_slab.name` |
| Crimson Slab         | `crimson_slab`         | None                     | `519`      | Block & Giveable Item[i 4]   | Identical[i 3] | `minecraft:wooden_slabs` | `tile.crimson_slab.name`        |
| Warped Double Slab   | `warped_double_slab`   | None                     | `522`      | Block & Ungiveable Item[i 2] | Identical[i 3] | —                        | `tile.warped_double_slab.name`  |
| Warped Slab          | `warped_slab`          | None                     | `520`      | Block & Giveable Item[i 4]   | Identical[i 3] | `minecraft:wooden_slabs` | `tile.warped_slab.name`         |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑ a b c d e f g h i j kUnavailable with /give command
3. ↑ a b c d e f g h i j k l m n o p q r s t u vThe block's direct item form has the same id as the block.
4. ↑ a b c d e f g h i j kAvailable with /give command.

