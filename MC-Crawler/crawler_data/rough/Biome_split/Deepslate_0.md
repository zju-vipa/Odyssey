# Deepslate
Deepslate is a stone type found deep underground in the Overworld that functions similarly to regular stone, but is significantly more difficult to break.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Chest loot
	- 1.4 Smelting
	- 1.5 Post-generation
- 2 Usage
	- 2.1 Note blocks
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Trivia
- 8 Gallery
	- 8.1 Screenshots
- 9 References
- 10 External links

## Obtaining
### Breaking
Deepslate can only be obtained by mining it using a pickaxe with the Silk Touch enchantment, otherwise it drops cobbled deepslate. If broken with any other tool, it drops nothing. The breaking time for deepslate is twice the time for stone.

| Block     | Deepslate             |
|-----------|-----------------------|
| Hardness  | 3                     |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 15                    |
| Wooden    | 2.25                  |
| Stone     | 1.15                  |
| Iron      | 0.75                  |
| Diamond   | 0.6                   |
| Netherite | 0.5                   |
| Golden    | 0.4                   |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
Deepslate makes up the majority of the solid blocks generated below Y=0 in the Overworld. Stone is gradually replaced from Y=8 to Y=0 until it is completely replaced by deepslate.

Deepslate also generates in ancient cities.


### Chest loot
On ancient_city/city_center/city_center_2, they generate a furnace with 24 deepslate inside of it.

### Smelting
Deepslate can be smelted from cobbled deepslate.

| Ingredients                    | Smelting recipe |
|--------------------------------|-----------------|
| Cobbled Deepslate+<br/>Anyfuel | 0.1             |

### Post-generation
If a world generated before Caves & Cliffs: Part II is loaded after the update, the bedrock layer between Y=0 and Y=4 is replaced with deepslate.

## Usage
Deepslate can be placed in three orientations, similarly to logs. Silverfish can enter and hide in deepslate, creating an infested block.

### Note blocks
Deepslate can be placed under note blocks to produce the "bass drum" sound.

## Data values
### ID
Java Edition:

| Name      | Identifier  | Form         | Block tags                                                                                                                                                             | Translation key             |
|-----------|-------------|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|
| Deepslate | `deepslate` | Block & Item | `base_stone_overworld`<br/>`deepslate_ore_replaceables`<br/>`dripstone_replaceable_blocks`<br/>`lush_ground_replaceable`<br/>`moss_replaceable`<br/>`mineable/pickaxe` | `block.minecraft.deepslate` |

Bedrock Edition:

| Name      | Identifier  | Numeric ID | Form                       | Item ID[i 1]   | Translation key       |
|-----------|-------------|------------|----------------------------|----------------|-----------------------|
| Deepslate | `deepslate` | `633`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.deepslate.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:

| Name | Default value | Allowed values | Description                            |
|------|---------------|----------------|----------------------------------------|
| axis | `y`           | `x`            | The deepslate is oriented east–west.   |
|      |               | `y`            | The deepslate is oriented vertically.  |
|      |               | `z`            | The deepslate is oriented north–south. |

Bedrock Edition:

| Name        | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                            |
|-------------|---------------|---------------|----------------|-------------------------|----------------------------------------|
| pillar_axis | Not Supported | `y`           | `x`            | `Unsupported`           | The deepslate is oriented east–west.   |
|             |               |               | `y`            | `Unsupported`           | The deepslate is oriented vertically.  |
|             |               |               | `z`            | `Unsupported`           | The deepslate is oriented north–south. |




