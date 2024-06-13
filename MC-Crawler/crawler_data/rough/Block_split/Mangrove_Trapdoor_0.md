# Wooden Trapdoor
A wooden trapdoor is a variant of the trapdoor that can be opened and closed by the player without redstone.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
- 2 Usage
	- 2.1 Properties
	- 2.2 Barrier
	- 2.3 Redstone component
	- 2.4 Fuel
	- 2.5 Note blocks
- 3 Sounds
	- 3.1 Generic
		- 3.1.1 Normal wood
		- 3.1.2 Cherry wood
		- 3.1.3 Bamboo wood
		- 3.1.4 Nether wood
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 Video
- 6 History
- 7 Issues
- 8 Gallery
	- 8.1 Screenshots
	- 8.2 Concept art
- 9 External links

## Obtaining
### Breaking
Wooden trapdoors can be mined with any tool, but an axe is the fastest. Trapdoors remain in place if their attachment block is moved, removed, or destroyed.

| Block     | Wooden Trapdoor       |
|-----------|-----------------------|
| Hardness  | 3                     |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 4.5                   |
| Wooden    | 2.25                  |
| Stone     | 1.15                  |
| Iron      | 0.75                  |
| Diamond   | 0.6                   |
| Netherite | 0.5                   |
| Golden    | 0.4                   |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
Some types of wooden trapdoors can be found in shipwrecks. Specifically:

- Oaktrapdoors generate as invillages,igloos, andshipwrecks.
- Sprucetrapdoors generate in taigavillagesandshipwrecks.
- Jungletrapdoors generate in desertvillages(aroundcomposters) andshipwrecks.
- Acaciatrapdoors generate inshipwrecks.‌[Bedrock Edition  only][needs testing in Bedrock Edition]
- Dark oaktrapdoors generate inshipwrecks.

### Crafting
| Ingredients    | Crafting recipe |
|----------------|-----------------|
| MatchingPlanks | 22222222222     |

## Usage
Main articles: Trapdoor § Usage and Tutorials/Trapdoor uses
### Properties
Wooden trapdoors can be opened and closed by players or a redstone signal. Wooden trapdoors are also affected by the wind burst of thrown wind charges‌[upcoming: JE 1.21 & BE 1.21.0], causing them to open if closed, or vice versa.

Lava can create fire in air blocks next to wooden trapdoors as if they were flammable, but the trapdoors do not burn (and cannot be burned by other methods either).

### Barrier
A wooden trapdoor can be opened or closed by pressing the Use Item/Place Block control.

### Redstone component
Wooden trapdoors can be controlled with redstone power. When activated, the wooden trapdoor immediately opens. When deactivated, it immediately closes.

An activated wooden trapdoor can still be closed by a player, and does not re-open until it receives a new activation signal (if a trapdoor has been closed "by hand", it still needs to be deactivated and then reactivated to open by redstone). 

### Fuel
Overworld wooden trapdoors can be used as a fuel in furnaces, smelting 1.5 items per block.

### Note blocks
Wooden trapdoors can be placed under note blocks to produce "bass" sounds.

## Data values
### ID
Java Edition:

| Name              | Identifier          | Form         | Block tags                                                  | Item tags                                                   | Translation key                     |
|-------------------|---------------------|--------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------|
| Spruce Trapdoor   | `spruce_trapdoor`   | Block & Item | `trapdoors`<br/>`wooden_trapdoors`                          | `trapdoors`<br/>`wooden_trapdoors`                          | `block.minecraft.spruce_trapdoor`   |
| Birch Trapdoor    | `birch_trapdoor`    | Block & Item | `trapdoors`<br/>`wooden_trapdoors`                          | `trapdoors`<br/>`wooden_trapdoors`                          | `block.minecraft.birch_trapdoor`    |
| Jungle Trapdoor   | `jungle_trapdoor`   | Block & Item | `trapdoors`<br/>`wooden_trapdoors`                          | `trapdoors`<br/>`wooden_trapdoors`                          | `block.minecraft.jungle_trapdoor`   |
| Acacia Trapdoor   | `acacia_trapdoor`   | Block & Item | `trapdoors`<br/>`wooden_trapdoors`                          | `trapdoors`<br/>`wooden_trapdoors`                          | `block.minecraft.acacia_trapdoor`   |
| Dark Oak Trapdoor | `dark_oak_trapdoor` | Block & Item | `trapdoors`<br/>`wooden_trapdoors`                          | `trapdoors`<br/>`wooden_trapdoors`                          | `block.minecraft.dark_oak_trapdoor` |
| Mangrove Trapdoor | `mangrove_trapdoor` | Block & Item | `trapdoors`<br/>`wooden_trapdoors`                          | `trapdoors`<br/>`wooden_trapdoors`                          | `block.minecraft.mangrove_trapdoor` |
| Cherry Trapdoor   | `cherry_trapdoor`   | Block & Item | `trapdoors`<br/>`wooden_trapdoors`                          | `trapdoors`<br/>`wooden_trapdoors`                          | `block.minecraft.cherry_trapdoor`   |
| Bamboo Trapdoor   | `bamboo_trapdoor`   | Block & Item | `trapdoors`<br/>`wooden_trapdoors`                          | `trapdoors`<br/>`wooden_trapdoors`                          | `block.minecraft.bamboo_trapdoor`   |
| Crimson Trapdoor  | `crimson_trapdoor`  | Block & Item | `non_flammable_wood`<br/>`trapdoors`<br/>`wooden_trapdoors` | `non_flammable_wood`<br/>`trapdoors`<br/>`wooden_trapdoors` | `block.minecraft.crimson_trapdoor`  |
| Warped Trapdoor   | `warped_trapdoor`   | Block & Item | `non_flammable_wood`<br/>`trapdoors`<br/>`wooden_trapdoors` | `non_flammable_wood`<br/>`trapdoors`<br/>`wooden_trapdoors` | `block.minecraft.warped_trapdoor`   |

Bedrock Edition:

| Name              | Identifier          | Numeric ID | Form                       | Item ID[i 1]   | Block tags  | Translation key               |
|-------------------|---------------------|------------|----------------------------|----------------|-------------|-------------------------------|
| Oak Trapdoor      | `trapdoor`          | `96`       | Block & Giveable Item[i 2] | Identical[i 3] | `trapdoors` | `tile.trapdoor.name`          |
| Spruce Trapdoor   | `spruce_trapdoor`   | `404`      | Block & Giveable Item[i 2] | Identical[i 3] | `trapdoors` | `tile.spruce_trapdoor.name`   |
| Birch Trapdoor    | `birch_trapdoor`    | `401`      | Block & Giveable Item[i 2] | Identical[i 3] | `trapdoors` | `tile.birch_trapdoor.name`    |
| Jungle Trapdoor   | `jungle_trapdoor`   | `403`      | Block & Giveable Item[i 2] | Identical[i 3] | `trapdoors` | `tile.jungle_trapdoor.name`   |
| Acacia Trapdoor   | `acacia_trapdoor`   | `400`      | Block & Giveable Item[i 2] | Identical[i 3] | `trapdoors` | `tile.acacia_trapdoor.name`   |
| Dark Oak Trapdoor | `dark_oak_trapdoor` | `402`      | Block & Giveable Item[i 2] | Identical[i 3] | `trapdoors` | `tile.dark_oak_trapdoor.name` |
| Mangrove Trapdoor | `mangrove_trapdoor` | `-496`     | Block & Giveable Item[i 2] | Identical[i 3] | `trapdoors` | `tile.mangrove_trapdoor.name` |
| Cherry Trapdoor   | `cherry_trapdoor`   | `-543`     | Block & Giveable Item[i 2] | Identical[i 3] | `trapdoors` | `tile.cherry_trapdoor.name`   |
| Bamboo Trapdoor   | `bamboo_trapdoor`   | `-520`     | Block & Giveable Item[i 2] | Identical[i 3] | `trapdoors` | `tile.bamboo_trapdoor.name`   |
| Crimson Trapdoor  | `crimson_trapdoor`  | `501`      | Block & Giveable Item[i 2] | Identical[i 3] | `trapdoors` | `tile.crimson_trapdoor.name`  |
| Warped Trapdoor   | `warped_trapdoor`   | `502`      | Block & Giveable Item[i 2] | Identical[i 3] | `trapdoors` | `tile.warped_trapdoor.name`   |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑ a b c d e f g h i j kAvailable with /give command.
3. ↑ a b c d e f g h i j kThe block's direct item form has the same id as the block.

### Block states
Main article: Trapdoor § Block states

