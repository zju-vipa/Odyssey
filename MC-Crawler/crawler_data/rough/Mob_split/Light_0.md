# Light
Light (or lighting) in Minecraft affects visibility, mob spawning, and plant growth. There are three aspects of Minecraft's lighting system: light level, internal light level, and rendered brightness.

## Contents
- 1 Light level
	- 1.1 Block light
	- 1.2 Sky light
	- 1.3 Light-filtering blocks
	- 1.4 Light-emitting blocks
- 2 Internal light level
	- 2.1 Effects of internal light
		- 2.1.1 Mobs
		- 2.1.2 Blocks
- 3 Rendered brightness
	- 3.1 Smooth lighting
	- 3.2 Ambient occlusion in Minecraft
	- 3.3 AO texture pattern
- 4 History
- 5 Issues
- 6 Trivia
- 7 Gallery
	- 7.1 Screenshots
- 8 References

## Light level
Light levels can be found on the debug screen in Java Edition. Light may come from two sources: the sky and certain blocks. There are 16 light levels, specified by an integer from 0 (the minimum) through 15 (the maximum).

### Block light
Block light comes from light-emitting blocks, and spreads using a flood fill algorithm.

The block light level decreases by one for each meter (block) of taxicab distance from the light source. This applies to each of the 3 coordinate axes. In other words, the light level decreases diagonally by the sum of the distances along each axis. For example:

- If a torch with light level 14 is placed on the floor, the light level of the adjacent floor blocks in all four directions is 13, while the diagonal blocks in all four directions have a light level of 12 (14 minus 1 south, minus 1 east).
- If a torch with light level 14 is placed on a wall one block above the floor, then the block on the floor that is one block southeast of and below the torch has a light level of 11 (14 - 1(south)- 1(east)- 1(down)).

On a surface, this effect produces a diamond-shaped pattern of illumination around the light source.

In Java Edition, when calculating lighting, the shapes of some blocks are detected: pistons, daylight detectors, enchanting tables, farmland, lecterns, stonecutters, dirt paths, snow, end portal frames, slabs and stairs, so that the light passing through them can spread only in specific directions. For example, dirt paths prevents the light from propagating downward, but the light can propagate in other directions.

### Sky light
The sky light level for blocks exposed to broad daylight is 15. Sky light cast onto blocks can spread to darker areas using a flood fill algorithm. Sky light is not reduced at night; rather, the spawning of mobs is determined by internal light values.

Opaque blocks can prevent the spread of sky light. By contrast, transparent blocks such as glass and iron bars have no effect on the sky light level. All light-filtering blocks, however, reduce the spread of sky light.

When sky light of a level of 15 spreads down through a transparent block, the level remains unchanged. When it spreads horizontally or upward, it reduces 1 light level. However, when it spreads through a light-filtering block, it does not follow the above two rules and attenuates specific light levels. 

Sky light with a level less than 15 spreads as block light - when it propagates to adjacent (including top and bottom, six blocks in total) blocks, it is attenuated until it is 0.

In Java Edition, when calculating lighting, the shapes of some blocks are detected: piston, daylight detectors, enchanting table, farmland, lectern, stonecutter, grass path, snow, end portal frame, slabs, and stairs. They have directional opacity, so that the light passing through them can spread only in specific directions. For example, the dirt path prevents the light from propagating downward, but the light can propagate in other directions.

### Light-filtering blocks
In Java Edition, all of the following light-filtering blocks decrease sky light by 1 level (but do not affect block light).

| Icon | Block                            |
|------|----------------------------------|
|      | Water                            |
|      | All transparentwaterloggedblocks |
|      | Bubble column                    |
|      | Ice                              |
|      | Frosted ice                      |
|      | Cobweb                           |
|      | Leaves                           |
|      | Slime block                      |
|      | Honey block                      |
|      | Monster spawner                  |
|      | Lava                             |
|      | Beacon                           |
|      | End gateway                      |
|      | Chorus plant                     |
|      | Chorus flower                    |
|      | Shulker box                      |

In Bedrock Edition, light-filtering blocks can reduce more levels of block or sky light. The following values are the amounts by which each block decreases the light level.

| Icon | Block                      | Amount of decrease |
|------|----------------------------|--------------------|
|      | Beacon                     | 14                 |
|      | Anvil                      | 3                  |
|      | Hopper                     |                    |
|      | Brewing stand              |                    |
|      | Cauldron                   |                    |
|      | Ice                        |                    |
|      | Frosted ice                |                    |
|      | Water                      | 2                  |
|      | Cobweb                     | 1                  |
|      | Leaves                     |                    |
|      | Powder snow                |                    |
|      | Slabs(except double slabs) |                    |

### Light-emitting blocks
| Light level | Block                                                                                                                                                                                                                               |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 15          | Beacon,conduit,end gateway,end portal,fire,four waterloggedsea pickles,froglight,glowstone,jack o'lantern,lantern,lava,lava cauldron,litcampfire,litredstone lamp,respawn anchor(fully charged),sea lantern,shroomlight,copper bulb |
| 14          | Colored torches‌[edu & BE  only],cave vineswith berries,end rod,torch,underwater torch‌[edu & BE  only]                                                                                                                             |
| 13          | Blast furnacewhen lit,furnacewhen lit,smokerwhen lit                                                                                                                                                                                |
| 12          | Vault(active),four litcandles,glowing obsidian‌[edu & BE  only],three waterloggedsea pickles,exposed copper bulb                                                                                                                    |
| 11          | $,(\frac{3}{4}$charged)                                                                                                                                                                                                             |
| 10          | Crying obsidian,litsoul campfire,soul fire,soul lantern,soul torch                                                                                                                                                                  |
| 9           | Three litcandles,litdeepslate redstone ore,litredstone ore,two waterloggedsea pickles                                                                                                                                               |
| 8           | Weathered copper bulb,trial spawner(active)                                                                                                                                                                                         |
| 7           | $,,,lit,(\frac{1}{2}$charged)                                                                                                                                                                                                       |
| 6           | One waterloggedsea pickle,sculk catalyst,two litcandles,vault(inactive)                                                                                                                                                             |
| 5           | Amethyst cluster                                                                                                                                                                                                                    |
| 4           | Large amethyst bud,oxidized copper bulb,trial spawner(inactive)                                                                                                                                                                     |
| 3           | $,one lit,(\frac{1}{4}$charged)                                                                                                                                                                                                     |
| 2           | Medium amethyst bud                                                                                                                                                                                                                 |
| 1           | Brewing stand,brown mushroom,calibrated sculk sensor,dragon egg,end portal frame,sculk sensor,small amethyst bud                                                                                                                    |
| 0–15        | Light block                                                                                                                                                                                                                         |

Comparison of the different light levels that blocks emit.

