## Chebyshev distance
Chebyshev distance, also know as the chessboard distance or maximum metric, is the maximum absolute difference between two points in one of three axes:

d=max⁡(|x1−x2|,|y1−y2|,|z1−z2|)
A "circle" drawn with a Chebyshev-distance radius would appear as a square, and a "sphere" would appear as a cube.

### Usages
Computationally, Chebyshev distance is roughly as efficient as taxicab distance, but it is useful for effects that need to happen in a square area or cuboid volume from a center coordinate.

Situations in which Minecraft calculates Chebyshev distance:

- Determining whetherfarmlandis hydrated by a block ofwaterin range of 4 blocks.
- A villager inJava Editiondetects aniron golemwithin ±16 blocks on any axis, and and iron golem inBedrock Editionspawns within ±8 blocks horizontally and ±6 blocks vertically from the village center block.
- The horizontal range of abeacon, which is 20, 30, 40 or 50 blocks depending on the size of the beacon pyramid.
- The spawning range ofwardensfrom naturally generatedsculk shriekersis ±5 blocks horizontally and ±6 blocks vertically from the shrieker.
- InJava Edition, the load level of achunkdecreases in a square pattern, creating a 23 by 23‌[until JE 1.20.5]chunk area around theworld spawnknown as thespawn chunks.

- Farmland gets hydrated within 4 blocks from water, otherwise remains dehydrated.
- A beacon's horizontal range is a square centered on the beacon itself.
- The spawn chunks in Java Edition is a square 23 chunks by 23 chunks wide.‌[until JE 1.20.5]


