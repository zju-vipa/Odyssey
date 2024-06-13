# Budding Amethyst
Budding amethyst is a fragile block found in amethyst geodes that grows amethyst clusters over time. It cannot be obtained as an item or moved by a piston, necessitating that it be returned to in order to harvest more clusters from it.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
- 2 Usage
	- 2.1 Growing into amethyst clusters
	- 2.2 Sound
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
- 5 History
- 6 Trivia
- 7 Gallery
- 8 Issues
- 9 References

## Obtaining
Budding amethysts can only be obtained via the Creative inventory or with commands, as they are unobtainable by Survival means, even using a tool enchanted with Silk Touch.

### Breaking
Budding amethyst cannot be obtained when mined, even using a tool enchanted with Silk Touch. It breaks immediately if pushed by a piston or sticky piston, and cannot be pulled by sticky pistons.

| Block     | Budding Amethyst      |
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
Budding amethyst generates naturally as part of amethyst geodes replacing some blocks of amethyst in the innermost layer of the geode.


## Usage
### Growing into amethyst clusters
An amethyst bud placed on a budding amethyst (rather than any other block) regardless whether it was placed by the player or spawned by the budding amethyst itself grows over time, going through three growth stages – small, medium, and large – before reaching its 4th and final growth stage as an amethyst cluster, which drops amethyst shards when mined.

In Java Edition, the below logic can be applied:

1. Perrandom tick, updates will occur to any given block in the loaded chunk every68.27seconds on average if the chunk center is within 128 blocks of a player's location.
2. Each random tick assigned to the budding amethyst block has a 20% chance of creating a new amethyst bud or incrementing the growth stage ononerandomly-selected side of the six-sided block.
3. There are 4 growth stages.

As such, the math can be applied if a player is within random tick range as:

(68.27 seconds average for random ticks) x (20% chance of growth for any given single side) x (6 sides) x (4 growth stages) = 68.27×5×6×4 = 8192 seconds average, also 2 hours 16 minutes 32 seconds, also 6.827 in-game days.

### Sound
Uniquely among other blocks a budding amethyst makes a quiet overlay sound when generally interacted with as well as its block breaking sound when hit with a projectile.

## Data values
### ID
Java Edition:

| Name             | Identifier         | Form         | Block tags                                    | Translation key                    |
|------------------|--------------------|--------------|-----------------------------------------------|------------------------------------|
| Budding Amethyst | `budding_amethyst` | Block & Item | `crystal_sound_blocks`<br/>`mineable/pickaxe` | `block.minecraft.budding_amethyst` |

Bedrock Edition:

| Name             | Identifier         | Numeric ID | Form                       | Item ID[i 1]   | Translation key              |
|------------------|--------------------|------------|----------------------------|----------------|------------------------------|
| Budding Amethyst | `budding_amethyst` | `583`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.budding_amethyst.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.


