# Stone
Stone is a block found underground in the Overworld or on the surface of mountains.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Chest loot
	- 1.4 Smelting
	- 1.5 Post-generation
- 2 Usage
	- 2.1 Silverfish
	- 2.2 Smelting ingredient
	- 2.3 Crafting ingredient
	- 2.4 Stonecutting
	- 2.5 Trading
	- 2.6 Note blocks
	- 2.7 Brewing ingredient
- 3 Sounds
- 4 Data values
	- 4.1 ID
- 5 History
	- 5.1 Data history
- 6 Issues
- 7 Gallery
- 8 References
- 9 External links

## Obtaining
### Breaking
Stone can be mined using a pickaxe, in which case it drops cobblestone. When mined without a pickaxe, it drops nothing. If a stone is mined with a Silk Touch enchanted pickaxe, it drops itself.

| Block     | Stone                 |
|-----------|-----------------------|
| Hardness  | 1.5                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 7.5                   |
| Wooden    | 1.15                  |
| Stone     | 0.6                   |
| Iron      | 0.4                   |
| Diamond   | 0.3                   |
| Netherite | 0.25                  |
| Golden    | 0.2                   |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
Stone makes up the majority of the solid blocks generated in the Overworld above Y=0. From Y=8 downwards, stone gradually transitions into deepslate, until it is completely replaced by deepslate at and below Y=0.

When chunks generate, stone can be found under 1-5 layers of grass blocks, dirt, gravel, clay, coarse dirt, podzol, mycelium, sand, sandstone, red sand, red sandstone or terracotta, depending on the biome. 

When the world is generating new chunks, some stone is replaced with ore features of other blocks. They may also be revealed on the side of small hills.

Stone also generates in igloo basements, some Overworld ruined portals, and in trail ruins.

Stone also makes up most of the blocks on the void start platform, in Superflat worlds created with the Void biome preset.‌[Java Edition  only]


### Chest loot
| Item  | Structure | Container     | Quantity | Chance                         |
|-------|-----------|---------------|----------|--------------------------------|
|       |           |               |          | Java EditionandBedrock Edition |
| Stone | Village   | Mason's chest | 1        | 37.7%                          |

### Smelting
Stone can be smelted from cobblestone.

| Ingredients              | Smelting recipe |
|--------------------------|-----------------|
| Cobblestone+<br/>Anyfuel | 0.1             |

### Post-generation
A simple stone generator.
Main article: Tutorials/Cobblestone farming § Stone generation
Stone can also be made by lava flowing on top of water blocks (both flowing and source). The water is replaced by stone.

## Usage
### Silverfish
Silverfish can enter and hide in stone, creating an infested block.

### Smelting ingredient
| Name         | Ingredients        | Smelting recipe |
|--------------|--------------------|-----------------|
| Smooth Stone | Stone+<br/>Anyfuel | 0.1             |

### Crafting ingredient
| Name                 | Ingredients                                  | Crafting recipe | Description                                                                         |
|----------------------|----------------------------------------------|-----------------|-------------------------------------------------------------------------------------|
| Redstone Comparator  | Redstone Torch+<br/>Nether Quartz+<br/>Stone |                 |                                                                                     |
| Redstone Repeater    | Redstone Torch+<br/>Redstone Dust+<br/>Stone |                 |                                                                                     |
| Stone Bricks         | Stone                                        | 4               |                                                                                     |
| Stone Button         | Stone                                        |                 |                                                                                     |
| Stone Pressure Plate | Stone                                        |                 |                                                                                     |
| Stone Slab           | Stone                                        | 6               |                                                                                     |
| Stone Stairs         | Stone                                        | 4               |                                                                                     |
| Stonecutter          | Iron Ingot+<br/>Stone                        |                 | Can use stone and its three other variants interchangeably.‌[Bedrock Edition  only] |
| Stonecutter          | Iron Ingot+<br/>Stone                        |                 | Can use stone only, no variants.‌[Java Edition  only]                               |

### Stonecutting
| Ingredients | Cutting recipe |
|-------------|----------------|
| Stone       | 22             |

### Trading
Apprentice-level stone mason villagers offer to buy 20 stone for an emerald.

### Note blocks
Stone can be placed under note blocks to produce "bass drum" sounds.

### Brewing ingredient
| Name                  | Ingredients               | Brewing recipe |
|-----------------------|---------------------------|----------------|
| Potion of Infestation | Stone+<br/>Awkward Potion |                |

## Data values
### ID
Java Edition:

| Name  | Identifier | Form         | Block tags                                                                                                                                                         | Translation key         |
|-------|------------|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| Stone | `stone`    | Block & Item | `base_stone_overworld`<br/>`dripstone_replaceable_blocks`<br/>`lush_ground_replaceable`<br/>`moss_replaceable`<br/>`mineable/pickaxe`<br/>`stone_ore_replaceables` | `block.minecraft.stone` |

Bedrock Edition:

| Name  | Identifier | Alias ID    | Numeric ID | Form                       | Item ID[i 1]   | Translation key         |
|-------|------------|-------------|------------|----------------------------|----------------|-------------------------|
| Stone | `stone`    | `stone / 0` | `1`        | Block & Giveable Item[i 2] | Identical[i 3] | `tile.stone.stone.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

