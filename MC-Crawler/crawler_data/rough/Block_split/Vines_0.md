# Vines
Vines are climbable non-solid vegetation blocks that grow on walls.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Trading
	- 1.4 Post-generation
- 2 Behavior
- 3 Usage
	- 3.1 Crafting ingredient
	- 3.2 Composting
	- 3.3 Color
		- 3.3.1 Biome colors
- 4 Sounds
- 5 Data values
	- 5.1 ID
	- 5.2 Block states
- 6 History
- 7 Issues
- 8 Gallery
	- 8.1 Screenshots
- 9 References
- 10 External links

## Obtaining
### Breaking
Vines can be destroyed with any item, but using shears is the only way to collect them. Shears enchanted with Efficiency are more efficient when used on vines; Efficiency II and above allows vines to be instantly broken.[1] Using an axe on vines can also increase efficiency, but does not allow for collection, even with Silk Touch. If multiple vines exist within the same block space, breaking one of them breaks all of them instead of just the one targeted[2] and results in only a single vine dropping[3]. Shears used by a dispenser cannot break vines.

| Block     | Vines                 |
|-----------|-----------------------|
| Hardness  | 0.2                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 0.3                   |
| Wooden    | 0.15                  |
| Stone     | 0.1                   |
| Iron      | 0.05                  |
| Diamond   | 0.05                  |
| Netherite | 0.05                  |
| Golden    | 0.05                  |
| Shears    | 0.3                   |
| Sword     | 0.2                   |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
Vines are naturally generated in jungles, swamps and lush caves. Jungle trees of both sizes have vines on their trunks and canopy edges, and vines grow on the sides of jungle terrain. Vines are also naturally generated on oak trees in swamps and mangrove trees. In Bedrock Edition, vines can also generate on dying oak, spruce, jungle and dark oak trees. 

Vines are found in jungle temples and the allium room in woodland mansions. They can also generate in watchtower walls in pillager outposts.


### Trading
Vines are sold by wandering traders for an emerald.

### Post-generation
Vines generate on 2×2 jungle trees grown from saplings, or mangrove trees grown from propagules.

In Bedrock Edition, vines generate on dying trees, which can sometimes be grown from saplings.

## Behavior
On each block tick, the vine block has a 25% chance to spread in a randomly selected direction. Their spreading can be toggled by the doVinesSpread game rule‌[Java Edition  only]. Vines spread to adjacent blocks under certain conditions:

- Downward:
	- If the block below is air, each side (north, south, east, and west) with vines has a 50% chance to spread downward.
	- If the block below is a block, each side of that block with vines on the ticked block has a 50% chance of gaining vines.

- Upward:
	- If the block above is air and there are fewer than 4 other vine blocks in a 9×9×3 area surrounding the ticked vine block, each side (north, south, east, and west) with vines has a 50% chance to spread upward if that side is backed by a block that vines can be placed on.

- Horizontally:
	- If the current vine block isn't covering the target direction and there are fewer than 4 other vine blocks in a 9×9×3 area surrounding the ticked vine block, then:
		- If the block in the target direction is air, then it tries:

|   |   |
|---|---|
| ↑ | ? |

|  |   |
|--|---|
|  | ? |

If the vine block has vines to the right and that side of the air block is backed by something vines can be placed on, spread to the right side of the air block.

|   |   |
|---|---|
| ? | ↑ |

|   |  |
|---|--|
| ? |  |

If the vine block has vines to the left and that side of the air block is backed by something vines can be placed on, spread to the left side of the air block.

|   |  |
|---|--|
| ↑ |  |

|  |  |
|--|--|
|  |  |

[more information needed]

If the vine block has vines to the right, and that side of the air block is backed by another air block, and the right side of the vine block is backed by something vines can be placed on, spread around the corner.

|  |   |
|--|---|
|  | ↑ |

|  |  |
|--|--|
|  |  |

If the vine block has vines to the left, and that side of the air block is backed by another air block, and the left side of the vine block is backed by something vines can be placed on, spread around the corner.

If the air block in the target direction has something vines could be placed on above it, spread to the top side of the air block.
If the block in the target direction is opaque and fills its whole cube, spread to that side of the ticked vine block.
Vines cannot be grown using bone meal.

Vines do not need light when growing.

