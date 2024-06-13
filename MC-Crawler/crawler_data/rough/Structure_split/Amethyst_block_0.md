# Block of Amethyst
A block of amethyst is a block found in amethyst geodes or crafted from amethyst shards. It copies and 'repeats' vibrations recieved by adjacent sculk sensors.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
- 2 Usage
	- 2.1 Sound
	- 2.2 Vibration resonance
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
- 5 History
- 6 Issues
- 7 Gallery
	- 7.1 Development images

## Obtaining
### Breaking
A block of amethyst can be obtained by mining it with any pickaxe. When mined using any other tool, it drops nothing.

| Block     | Block of Amethyst     |
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
Blocks of amethyst generate naturally on the inner wall of amethyst geodes, with calcite and smooth basalt making up next two outer layers.


### Crafting
| Ingredients    | Crafting recipe |
|----------------|-----------------|
| Amethyst Shard |                 |

## Usage
### Sound
Uniquely among other blocks, a block of amethyst makes a quiet overlay sound when generally interacted with, as well as its block breaking sound when hit with a projectile.

### Vibration resonance
When a block of amethyst is placed adjacent to a sculk sensor or a calibrated sculk sensor, if that sculk sensor receives a vibration, the block of amethyst re-emits its frequency as a separate vibration at its location. This vibration can then be detected by another sculk sensor, allowing a chain of sculk sensors and amethyst blocks to be created, transmitting a signal wirelessly.

## Data values
### ID
Java Edition:

| Name              | Identifier       | Form         | Block tags                                    | Translation key                  |
|-------------------|------------------|--------------|-----------------------------------------------|----------------------------------|
| Block of Amethyst | `amethyst_block` | Block & Item | `crystal_sound_blocks`<br/>`mineable/pickaxe` | `block.minecraft.amethyst_block` |

Bedrock Edition:

| Name              | Identifier       | Numeric ID | Form                       | Item ID[i 1]   | Translation key            |
|-------------------|------------------|------------|----------------------------|----------------|----------------------------|
| Block of Amethyst | `amethyst_block` | `582`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.amethyst_block.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.


