### Potions
Using effects from potions or beacons, walking and sprinting speeds become competitive with other methods of transportation.

Each additional level of Speed allows the player to walk at nearly the sprinting speed of the previous level, and sprinting with Speed II is only slightly slower than a minecart at full speed or a boosted pig. With adequate food and potion supplies, sprinting may be more cost-effective than building high-speed transportation systems.

| Effect level | Walking speed (m/s) | Sprinting speed (m/s) |
|--------------|---------------------|-----------------------|
| none         | 4.317 m/s           | 5.612 m/s             |
| Speed        | 5.181 m/s           | 6.735 m/s             |
| SpeedII      | 6.044 m/s           | 7.857 m/s             |

### Commands
Using the /effect command, extremely high or low speeds become reachable. At exceedingly high levels (100+), the player moves faster than the chunks can load.

| Effect level | Sneaking speed (m/s) | Walking speed (m/s) | Sprinting speed (m/s) |
|--------------|----------------------|---------------------|-----------------------|
| Speed50      | 14.25 m/s            | 47.49 m/s           | 61.74 m/s             |
| Speed127     | 34.19 m/s            | 113.97 m/s          | 148.17 m/s            |
| Speed256     | 67.61 m/s            | 225.36 m/s          | 292.96 m/s            |

### Vertical transportation
See also: Tutorials/Elevators

There are some examples of purely vertical transportation methods:

| Method                                  | Conditions                                         | Average speed (m/s) |
|-----------------------------------------|----------------------------------------------------|---------------------|
| Jumping[note 1]                         | Climbing slope without stairs,pillar jumping, etc. | 2.0 m/s             |
| Stairs                                  | Ascending                                          | 3.2 m/s             |
|                                         | Descending                                         | 3.6 m/s             |
| #climbable(e.g. ladders, vines...)      | Ascending                                          | 2.35 m/s            |
|                                         | Descending                                         | 3.0 m/s             |
| Soul sand                               | Ascending in water                                 | 11 m/s              |
| Magma block                             | Descending in water                                | 4.9 m/s             |
| Waterfall                               | No adjacent blocks                                 | 2.0 m/s             |
|                                         | Ascending, with adjacent blocks                    | 0.6 m/s             |
|                                         | Descending, with adjacent blocks                   | 3.4 m/s             |
| Waterfall(measured inJava Edition)      | Ascending, by holdingjump                          | 2.23 m/s            |
|                                         | Sprint-swimming upward while holdingjump           | 6.98 m/s            |
| Lavafall                                | Using aPotion of Fire Resistance                   | 0.8 m/s             |
| Levitation                              | Level 1                                            | 0.9 m/s             |
| Flying                                  | Creative<br/>Spectator                             | 7.49 m/s            |
| Falling                                 | Player, terminal velocity                          | 78.4 m/s            |
|                                         | Item, terminal velocity                            | 40.0 m/s            |
|                                         | Arrow, terminal velocity                           | 100.0 m/s           |
|                                         | Falling block, terminal velocity                   | 40.0 m/s            |
| Swimming                                | Water                                              | 0.39 m/s            |
| Scaffolding(measured inBedrock Edition) | Ascending                                          | 1.2 m/s             |
|                                         | Descending                                         | 2.94 m/s            |
| Scaffolding(measured inJava Edition)    | Ascending                                          | 2.352 m/s           |
|                                         | Descending                                         | 3.000 m/s           |

1. ↑The player can jump up a distance of 1 1⁄4 blocks. With Jump Boost I, that increases to 1 15⁄16 blocks, and with Jump Boost II, that increases to 2 1⁄2 blocks.

Falling speed is more complex: Every tick (1⁄20 second), non-flying players and mobs have their vertical speed decremented (less upward motion, more downward motion) by 0.08 blocks per tick (1.6 m/s), then multiplied by 0.98.[note 1] This can be described as a formula: 

v(t)=0.98×(v(t−1)−0.08)

Where v(t)is the speed (in blocks/second) at the t-th tick. v(1) corresponds to the initial speed of the jump: v(1)={0Freefall0.42+0.1EJumpBoostJumping} where EJumpBoost is the level of the jump boost. Because "Speed" (in Minecraft) is defined as the Y coordinate difference between the current tick and the previous tick, the initial speed is v(1) instead of v(0).

This would produce a terminal velocity of 3.92 blocks per tick or 78.4 m/s. However, the sky isn't quite high enough for that: Falling from layer 256 to bedrock takes about 5.5 seconds, with impact at 3.5 blocks per tick (70 m/s). It is possible to fly higher in Creative mode, or by flying with elytra and then removing them, reaching terminal velocity falling from "above the sky".

1. ↑Horses have their vertical speed multiplied by 0.98 a second time in the same tick. This may or may not apply to some other mobs.

By solving the recurrence relation, it is possible to get an exact function to calculate the vertical speed of a falling player:

v(t)=0.98t−1(v(1)+3.92)−3.92

Where the velocity v is in blocks (meters) per tick, the time t is in ticks and downward motion is negative. Note that if the initial velocity is zero, the function can be simplified to v(t)=3.92×(0.98t−1).

An exact function to calculate the displacement of the player is the following:

d(t)=d(0)+50(v(1)+3.92)(1−0.98t)−3.92t

Where the displacement d is in blocks (meters), the time t is in ticks, d(0) is the initial displacement and downward displacement is negative. If the initial velocity and displacement is zero, it can be written as:

d(t)=3.92×(50×(1−0.98t)−t)

An approximate function to calculate the time it takes to fall from some height is the following:

t(d)=50−0.255102d+49.498316×W−1(−0.367861×1.005167d)

Where the height d is in blocks (meters), the time t is in ticks, initial velocity and displacement is zero, downward displacement is negative and W is the Lambert W function.

