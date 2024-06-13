# Chorus Flower
Chorus flowers are blocks that grow on chorus plants found in the End. They can be planted on end stone where they grow into new chorus plants.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
- 2 Usage
	- 2.1 Farming
	- 2.2 Placement and growth
	- 2.3 Bee nests
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Trivia
- 8 References

## Obtaining
### Breaking
Chorus flowers can be mined with any tool and drop themselves when broken, but an axe is the quickest. They do not drop anything when pushed by a piston or water, destroyed by a ravager‌[Bedrock Edition  only], or when their supporting block (the chorus plant block or end stone) is destroyed.

| Block     | Chorus Flower         |
|-----------|-----------------------|
| Hardness  | 0.4                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 0.6                   |
| Wooden    | 0.3                   |
| Stone     | 0.15                  |
| Iron      | 0.1                   |
| Diamond   | 0.1                   |
| Netherite | 0.1                   |
| Golden    | 0.05                  |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


They drop themselves when broken by explosions, with the applicable drop chance for the various explosion types, or when hit by a wide variety of projectiles:

- Arrow
- Tipped arrow
- Spectral arrow
- Trident
- Firework rocket
- Snowball
- Egg
- Fireball
- Small fireball
- Dragon fireball
- Wither skull
- Wind charge‌[upcoming: JE 1.21 & BE 1.21.0]

### Natural generation
Chorus flowers are naturally generated in the End at the top of chorus trees, in their fully-grown state.


## Usage
Chorus flowers are used to grow chorus plants. They can be planted on end stone in any dimension.

Chorus flowers can also be pollinated by bees.

### Farming
Chorus flowers can be planted on end stone and grow in any dimension, regardless of light level. A flower stops growing once it has reached age 5 (appearing purple rather than white), but may be harvested and replanted to reset the age. Chorus flowers do not grow if planted 1 block below the surface of the ground.

### Placement and growth
Final heights of 500,000 chorus plants (blue) and heights of 500,000 chorus flowers from full-grown plants (orange).
Placement
Chorus flowers must be above end stone or chorus plant, or be above air and horizontally adjacent to exactly one chorus plant. If these conditions are not met, the block breaks without dropping anything.

Growth conditions and algorithm
Each block tick until the flower reaches age 5, the flower attempts to grow if the block above is air. The flower does not age if growth is not attempted due to lack of an air block above. Bone meal has no effect on growth.[1]

The flower may attempt to grow upward depending on the structure of chorus plant blocks directly beneath:

- 100% chance if zero or one plant block is directly beneath
- 60% if the flower is above a two-block unbranched plant (i.e. two plant blocks overend stone)
- 50% if above a two-block high branch (i.e. two plant blocks over air)
- 40% if above a three-block unbranched plant
- 25% if above a three-block high branch
- 20% if above a four-block unbranched plant

The growth attempt succeeds if the blocks horizontally adjacent to and above the target block above are all air, and results in the target block becoming a flower block with the same age while the existing flower block turns to chorus plant.

If upward growth does not occur and the flower's age is less than 4, the flower may attempt to branch horizontally. 1–4 branches are attempted on an unbranched plant or 0–3 on a branched plant. For each branch a horizontal direction is chosen at random, and if the block in that direction is an air block with more air blocks on all other horizontal sides and an air block below, it is replaced with a flower with age incremented by 1. If at least one branch succeeds, the original flower block is turned to chorus plant.

Upon a successful growth attempt, the chorus flower emits a low-pitched sound, similar to the sound endermen emit when teleporting.

If no growth occurs on a growth attempt, the flower's age is set to 5.

Flowers and plant height
The amount of chorus flowers a player gets from a fully and unrestricted grown chorus plant ranges from 1 to 8, averaging at around 3.7 flowers per plant. 

Plant heights range from 5 to (rarely) 22 above the end stone block on which the original chorus flower was planted, with over half falling in the range 13–16. Flower heights range from 3 to (rarely) 22, with over half falling in the range 11–16 above the end stone block.

