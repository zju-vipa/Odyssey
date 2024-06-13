# Sponge
A sponge is a block that can be placed to remove water in an area around itself. This turns it into a wet sponge, which can be smelted or placed in the Nether to dry it to be reused. Sponges can only be found in ocean monuments.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Mob loot
		- 1.3.1 Elder guardians
	- 1.4 Smelting
	- 1.5 Drying
- 2 Usage
- 3 Sounds
	- 3.1 Generic
		- 3.1.1 Sponge
		- 3.1.2 Wet sponge
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 Achievements
- 6 History
	- 6.1 Data history
- 7 Issues
- 8 Gallery
	- 8.1 Screenshots
- 9 References
- 10 External links

## Obtaining
Dry sponge does not generate in the world.

### Breaking
Either type of sponge can be mined by hand, or with any tool, dropping itself as an item; however, hoes break sponges the fastest compared to other tools.

| Block     | SpongeWet Sponge      |
|-----------|-----------------------|
| Hardness  | 0.6                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 0.9                   |
| Wooden    | 0.45                  |
| Stone     | 0.25                  |
| Iron      | 0.15                  |
| Diamond   | 0.15                  |
| Netherite | 0.1                   |
| Golden    | 0.1                   |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
Ocean monuments can generate "sponge rooms." Each room contains an average of 30 wet sponges. See Ocean Monument/Structure for details.

### Mob loot
#### Elder guardians
An elder guardian always drops one wet sponge when killed by the player.

| Source         | Roll Chance | Quantity (Roll Chance) |           |            |             |
|----------------|-------------|------------------------|-----------|------------|-------------|
|                |             | Default                | Looting I | Looting II | Looting III |
| Elder Guardian | 100%[d 1]   | 1                      | 1         | 1          | 1           |

1. ↑Only dropped when kill credit is given to the player

### Smelting
A wet sponge can be dried in a furnace, making the sponge reusable. 

| Ingredients          | Smelting recipe | Description                                                                                                                                                                                      |
|----------------------|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Wet sponge + anyfuel | 0.15            | If a bucket is in the fuel slot at the time the sponge completes its drying, the water drains into the bucket, leaving a bucket of water in the fuel slot. Otherwise, the water just evaporates. |

### Drying
A wet sponge placed in the Nether dries out instantly with a puff of steam and turns into a normal sponge.

In Bedrock Edition, a wet sponge placed in any dry biome in the Overworld dries out after a few minutes and turns into a normal sponge.

In Bedrock Edition, if a normal sponge comes into contact with water in a dry biome, it absorbs the water and immediately dries out with a puff of steam.

## Usage
A sponge absorbing water in a pond.
A sponge can be used to turn water into air by "absorbing" the water. A sponge instantly absorbs nearby water when it is placed next to water or when water comes into contact with it. Sponges immediately turn wet upon absorption and do not absorb any more water afterward. Wet sponges drip small water particles. Sponges in item form do not absorb water or become wet.

A sponge absorbs both flowing and source blocks of water up to 7 blocks away (taken as a taxicab distance) in all six directions around itself. Instead of a cube or a sphere, this effectively encloses the volume of an octahedron with vertices placed 7 units away from the center in each direction due to the game's extensive use of taxicab distance. A sponge does not absorb more than 135 blocks of water however, and water closest to the sponge is absorbed first. The absorption propagates only between adjacent water blocks and does not "jump over" non-water blocks, including air.

## Data values
### ID
Java Edition:

| Name       | Identifier   | Form         | Block tags     | Translation key              |
|------------|--------------|--------------|----------------|------------------------------|
| Sponge     | `sponge`     | Block & Item | `mineable/hoe` | `block.minecraft.sponge`     |
| Wet Sponge | `wet_sponge` | Block & Item | `mineable/hoe` | `block.minecraft.wet_sponge` |

Bedrock Edition:

| Name   | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key                                   |
|--------|------------|------------|----------------------------|----------------|---------------------------------------------------|
| Sponge | `sponge`   | `19`       | Block & Giveable Item[i 2] | Identical[i 3] | `tile.sponge.dry.name`<br/>`tile.sponge.wet.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

In Bedrock Edition, sponges use the following block states:

Bedrock Edition:

| Name        | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description |
|-------------|---------------|---------------|----------------|-------------------------|-------------|
| sponge_type | `0x1`         | `dry`         | `dry`          | `0`                     | Sponge      |
|             |               |               | `wet`          | `1`                     | Wet Sponge  |



