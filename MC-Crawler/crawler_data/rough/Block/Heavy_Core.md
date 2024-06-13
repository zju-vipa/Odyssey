# Heavy Core
A heavy core is a dense[1] block found in trial chambers that can be combined with breeze rods to craft a mace.

## Contents
- 1 Obtaining
	- 1.1 Vault loot
	- 1.2 Breaking
- 2 Usage
	- 2.1 Crafting ingredient
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Gallery
- 8 References

## Obtaining
### Vault loot
| Item       | Structure      | Container     | Quantity | Chance            |
|------------|----------------|---------------|----------|-------------------|
|            |                |               |          | Java Edition 1.21 |
| Heavy Core | Trial Chambers | Ominous Vault | 1        | 8.3%              |

### Breaking
A heavy core can be mined successfully only with a pickaxe. When mined without a pickaxe, it drops nothing.

| Block     | Heavy Core            |
|-----------|-----------------------|
| Hardness  | 10                    |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 15                    |
| Wooden    | 7.5                   |
| Stone     | 3.75                  |
| Iron      | 2.5                   |
| Diamond   | 1.9                   |
| Netherite | 1.7                   |
| Golden    | 1.25                  |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

The above table applies to Java Edition. In Bedrock Edition, heavy cores have a base hardness of 30 and are mined significantly slower.

## Usage
### Crafting ingredient
Sounds[edit | edit source]
Java Edition:

| v t e heavy_core sound type |                |                  |                                                   |                          |                                     |        |       |                          |
|-----------------------------|----------------|------------------|---------------------------------------------------|--------------------------|-------------------------------------|--------|-------|--------------------------|
| Sound                       | Subtitles      | Source           | Description                                       | Resource location        | Translation key                     | Volume | Pitch | Attenuation<br/>distance |
|                             | Block broken   | Blocks           | Once the block has broken                         | `block.heavy_core.break` | `subtitles.block.generic.break`     | 1.0    | 0.8   | 16                       |
|                             | Block placed   | Blocks           | When the block is placed                          | `block.heavy_core.place` | `subtitles.block.generic.place`     | 1.0    | 0.8   | 16                       |
|                             | Block breaking | Blocks           | While the block is in the process of being broken | `block.heavy_core.hit`   | `subtitles.block.generic.hit`       | 0.25   | 0.5   | 16                       |
|                             | None[sound 1]  | Entity-Dependent | Falling on the block with fall damage             | `block.heavy_core.fall`  | None[sound 1]                       | 0.5    | 0.75  | 16                       |
|                             | Footsteps      | Entity-Dependent | Walking on the block                              | `block.heavy_core.step`  | `subtitles.block.generic.footsteps` | 0.15   | 1.0   | 16                       |

1. ↑ a bMC-177082

Bedrock Edition:

| v t e heavy_core sound type |        |                                                   |                    |        |       |
|-----------------------------|--------|---------------------------------------------------|--------------------|--------|-------|
| Sound                       | Source | Description                                       | Resource location  | Volume | Pitch |
|                             | Blocks | Once the block has broken                         | `break.heavy_core` | 1.0    | 0.8   |
|                             | Blocks | When the block is placed                          | `break.heavy_core` | 1.0    | 0.8   |
|                             | Blocks | While the block is in the process of being broken | `step.heavy_core`  | 1.0    | 0.5   |
|                             | Blocks | Falling on the block with fall damage             | `step.heavy_core`  | 1.0    | 1.0   |
|                             | Blocks | Walking on the block                              | `step.heavy_core`  | 1.0    | 1.0   |
|                             | Blocks | Jumping from the block                            | `step.heavy_core`  | 0.12   | 1.1   |
|                             | Blocks | Falling on the block without fall damage          | `step.heavy_core`  | 1.0    | 1.0   |

## Data values
### ID
Java Edition:

| Name       | Identifier   | Form         | Translation key              |
|------------|--------------|--------------|------------------------------|
| Heavy Core | `heavy_core` | Block & Item | `block.minecraft.heavy_core` |

Bedrock Edition:

| Name       | Identifier   | Numeric ID | Form                       | Item ID[i 1]   | Translation key        |
|------------|--------------|------------|----------------------------|----------------|------------------------|
| Heavy Core | `heavy_core` | `-316`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.heavy_core.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:

| Name        | Default value | Allowed values     | Description                                                        |
|-------------|---------------|--------------------|--------------------------------------------------------------------|
| waterlogged | `false`       | `false`<br/>`true` | Whether or not there's water in the same place as this heavy core. |

