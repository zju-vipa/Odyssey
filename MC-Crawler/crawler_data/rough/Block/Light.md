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

## Internal light level
Internal sky light versus time and sky light
The internal light level is used for calculations within the game. The game uses the internal light level of one block to compute aspects of the game, which include mob spawning, plant growth, and daylight detector outputs.

The game uses sky light, time, and weather to calculate an internal sky light value (also known as darkening sky light), then uses the maximum level of the block light and the internal sky light to calculate the internal light (formula: (max(internal sky light,block light))). This value is an integer with a maximum level of 15; it can also be negative.

Here are the levels of internal sky light at a sky light of level 15:


| Internal sky light | Clear                                                                                          |                                                        | Rain or snowfall |                                                                             | Thunder                                   |                                                                                                                            |
|--------------------|------------------------------------------------------------------------------------------------|--------------------------------------------------------|------------------|-----------------------------------------------------------------------------|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
|                    | Time↓                                                                                          | Time↑                                                  | Time↓            | Time↑                                                                       | Time↓                                     | Time↑                                                                                                                      |
| 4                  |                                                                                                | 13,670–(Midnight/18,000)-22,330(8,660 Gtk/7:13)        |                  | 13,670–(Midnight/18,000)-22,330(8,660 Gtk/7:13)                             |                                           | 13,670–(Midnight/18,000)-22,330(8,660 Gtk/7:13)                                                                            |
| 5                  | 22,331–22,491(160 Gtk/8 sec)                                                                   | 13,509–13,669(160 Gtk/8 sec)                           | 22,331–22,565()  | 13,436–13,669()                                                             | 22,331–22,671()                           | 13,330–13,669()                                                                                                            |
| 6                  | 22,492–22,652(160 Gtk/8 sec)                                                                   | 13,348–13,508(160 Gtk/8 sec)                           | 22,566–22,798()  | 13,203–13,435()                                                             | 22,672–23,010()                           | 12,990–13,329()                                                                                                            |
| 7                  | 22,653–22,812‌[JE  only]<br/>22,653–22,813‌[BE  only]J: (159 Gtk/7.95 sec)B: (160 Gtk/8 sec)   | 13,188–13,347(159 Gtk/7.95 sec)                        | 22,799–23,031()  | 12,969–13,202()                                                             | 23,011–23,352()                           | 12,648–12,989()                                                                                                            |
| 8                  | 22,813‌[JE  only]–22,973<br/>22,814‌[BE  only]–22,973J: (160 Gtk/8 sec)B: (159 Gtk/7.95 sec)   | 13,027–13,187(160 Gtk/8 sec)                           | 23,032–23,266()  | 12,734–12,968()                                                             | 23,353–23,700()                           | 12,300–12,647()                                                                                                            |
| 9                  | 22,974–23,134(160 Gtk/8 sec)                                                                   | 12,867–13,026(159 Gtk/7.95 sec)                        | 23,267–23,504()  | 12,497–12,733()                                                             | 23,701-(Dawn/24,000/0)–59(240 Gtk/12 sec) | 11,941‌[JE  only]–(Dusk/12,000)-12,299<br/>11,942‌[BE  only]–(Dusk/12,000)-12,299J:(358 Gtk/17.9 sec)B:(357 Gtk/17.85 sec) |
| 10                 | 23,135–23,296(161 Gtk/8.05 sec)                                                                | 12,705–12,866(161 Gtk/8.05 sec)                        | 23,505–23,745()  | 12,256–12,496()                                                             |                                           | 60–(Noon/6,000)-11,940‌[JE  only]<br/>60–(Noon/6,000)-11,941‌[BE  only]J: (11,880 Gtk/9:54)B: (11,881 Gtk/9:54)            |
| 11                 | 23,297–23,459(162 Gtk/8.1 sec)                                                                 | 12,542–12,704(162 Gtk/8.1 sec)                         | 23,746–23,991()  | 12,010–12,255()                                                             |                                           | N/A                                                                                                                        |
| 12                 | 23,460–23,623‌[JE  only]<br/>23,460–23,624‌[BE  only]J: (163 Gtk/8.15 sec)B: (164/8.2 sec)     | 12,377–12,541(164 Gtk/8.2 sec)                         |                  | 23,992–(Dawn/24,000/0)(Noon/6,000)(Dusk/12,000)-12,009(12,017 Gtk/10:00.85) |                                           | N/A                                                                                                                        |
| 13                 | 23,624‌[JE  only]–23,790<br/>23,625‌[BE  only]–23,790J: (166 Gtk/8.3 sec)B: (165 Gtk/8.25 sec) | 12,210–12,376(166 Gtk/8.3 sec)                         |                  | N/A                                                                         |                                           | N/A                                                                                                                        |
| 14                 | 23,791–23,960(169 Gtk/8.45 sec)                                                                | 12,041–12,209(168 Gtk/8.4 sec)                         |                  | N/A                                                                         |                                           | N/A                                                                                                                        |
| 15                 |                                                                                                | 23,961–(Dawn/24,000/0)(Noon/6,000)(Dusk/12,000)-12,040 |                  | N/A                                                                         |                                           | N/A                                                                                                                        |

To obtain an internal sky light for a sky light level s less than 15, take the internal level L at 15 and subtract from it the difference between 15 and s: L−(15−s).

| Icon  | Time                           | Internal sky light when sky light is 15 |
|-------|--------------------------------|-----------------------------------------|
|       | noon, during clear weather     | 15                                      |
| <br/> | noon, duringrainorsnowfall     | 12                                      |
|       | noon, during athunderstorm     | 10[storm 1]                             |
|       | midnight, during clear weather | 4                                       |

1. ↑During thunderstorms, hostile mobs are allowed to spawn as if the internal sky light level were actually 5.

### Effects of internal light
Keep in mind that the internal light level is only one of the considerations that apply to mob spawning and plant growth.

#### Mobs
| Light level > Mob v                         | 0                             | 1 | 2 | 3                | 4 | 5 | 6 | 7                                                                          | 8 | 9 | 10 | 11                                         | 12 | 13 | 14 | 15                                                            |
|---------------------------------------------|-------------------------------|---|---|------------------|---|---|---|----------------------------------------------------------------------------|---|---|----|--------------------------------------------|----|----|----|---------------------------------------------------------------|
| Bats                                        |                               |   |   | Spawn at y: 0–62 |   |   |   | Spawn at y: 0–62 from October 20 to November 3‌[JE  only]                  |   |   |    |                                            |    |    |    | Do not spawn                                                  |
| Blazes                                      |                               |   |   |                  |   |   |   |                                                                            |   |   |    | Spawn innether fortresses                  |    |    |    | Do not spawn                                                  |
| Wither skeletons                            |                               |   |   |                  |   |   |   | Spawn innether fortresses                                                  |   |   |    |                                            |    |    |    | Do not spawn                                                  |
| Zombified piglins                           |                               |   |   |                  |   |   |   |                                                                            |   |   |    | Spawn inthe Nether                         |    |    |    | Do not spawn                                                  |
| Slimes(slime chunk)                         |                               |   |   |                  |   |   |   |                                                                            |   |   |    |                                            |    |    |    | Spawn in slime chunks at Y: -64–40                            |
| Slimes(swamp)                               |                               |   |   |                  |   |   |   | Spawn in swamp biomes at Y: 50–70                                          |   |   |    |                                            |    |    |    | Do not spawn                                                  |
| Skeletons                                   | Spawn in theOverworld         |   |   |                  |   |   |   | Spawn in the Nether                                                        |   |   |    | Do not spawn                               |    |    |    | Do not spawn, burn insunlight                                 |
| Zombies<br/>Chicken jockeys                 | Spawn in theOverworld         |   |   |                  |   |   |   |                                                                            |   |   |    | Do not spawn                               |    |    |    | Do not spawn, burn insunlight                                 |
| Drowned                                     | Spawn inoceansandrivers       |   |   |                  |   |   |   |                                                                            |   |   |    | Hostile, do not spawn                      |    |    |    | Burn insunlight, ignore player outside water when in sunlight |
| Creepers<br/>Witches                        | Spawn in the Overworld        |   |   |                  |   |   |   |                                                                            |   |   |    |                                            |    |    |    | Do not spawn                                                  |
| Phantoms                                    |                               |   |   |                  |   |   |   | Spawn in the Overworld if player hasn't entered abedin over 3 in-game days |   |   |    | Do not spawn                               |    |    |    | Burn insunlight                                               |
| Spiders<br/>Cave spiders<br/>Spider jockeys | Spawn in the Overworld        |   |   |                  |   |   |   |                                                                            |   |   |    | Hostile, do not spawn                      |    |    |    | Do not spawn,neutralunless provoked                           |
| Silverfish                                  |                               |   |   |                  |   |   |   |                                                                            |   |   |    | Spawn frommonster spawnersin the Overworld |    |    |    | Hostile, do not spawn                                         |
| Endermen                                    | Spawn in all three dimensions |   |   |                  |   |   |   | Spawn inthe Nether                                                         |   |   |    |                                            |    |    |    | Do not spawn, teleport randomly in Overworld                  |

#### Blocks
| Block                                                    | Level 0–3                                                          | Level 4–7 | Level 8         | Level 9 | Level 10                        | Level 11                        | Level 12 | Level 13–15                                                           |
|----------------------------------------------------------|--------------------------------------------------------------------|-----------|-----------------|---------|---------------------------------|---------------------------------|----------|-----------------------------------------------------------------------|
| Snow[note 1]                                             |                                                                    |           |                 |         | Forms                           | Neither forms nor melts[note 2] |          | Melts                                                                 |
| Ice[note 1]                                              |                                                                    |           |                 | Forms   | Neither forms nor melts[note 3] |                                 |          | Melts                                                                 |
| Mushrooms                                                |                                                                    |           |                 |         |                                 |                                 | Spread   | Uproot unless onmycelium,podzol, ornylium                             |
| Saplings<br/>Pumpkinormelonstems<br/>Bamboo<br/>[note 4] |                                                                    |           | Does not grow   |         |                                 |                                 |          | Grows                                                                 |
| Wheat<br/>Carrots<br/>Potatoes<br/>Beetroots[note 5]     |                                                                    | Uproot    | Does not grow   |         |                                 |                                 |          | Grows                                                                 |
| Grass Block<br/>Mycelium[note 6]                         | Becomes dirt if opaque block or partially transparent block on top |           | Does not spread |         |                                 |                                 |          | Spreads to nearby dirt (see below)                                    |
| Dirt[note 6]                                             | Does not accept spread                                             |           |                 |         |                                 |                                 |          | Accepts spread if there is no opaque or semi-transparent block on top |
| Frosted ice                                              |                                                                    |           |                 |         |                                 |                                 |          | See Frosted Ice for details                                           |
| Daylight detector                                        |                                                                    |           |                 |         |                                 |                                 |          | Output                                                                |

1. ↑ a bSunlight does not affect snow or ice melting.
2. ↑"[MC-217420] Snow neither forms nor melts at block light level 11 - Jira"     – Mojira, March 1, 2021.
3. ↑"[MC-217424] Ice neither forms nor melts at block light level 10 - Jira"     – Mojira, March 1, 2021.
4. ↑For growth, the relevant light level is that in the block above the plant. The growth of pumpkins or melons from a stem checks the light above the stem, not the block where the pumpkin or melon grows.
5. ↑For growth, the relevant light level is that in the block above the plant. For uprooting, the relevant light level is the plant block itself.
6. ↑ a bThe relevant light level is that in the air block above it.

## Rendered brightness
Examples of the internal lightmap texture (the game's brightness setting is at the default of 50). Horizontal axis is block light, vertical is sky light.
The game uses the light level (instead of internal light level), time, and weather to compute the rendered brightness of a given block or an entity. Light is completely monochromatic and cannot be truly colored.

As mentioned above, sky light is not reduced at night, instead, the brightness curve itself changes based on the time. Entities cast circular‌[Java Edition  only] or tridecagonal‌[Bedrock Edition  only] shadows; however, these are unrelated to the rendering of blocks.

In general, lighting due to blocks results in a higher brightness, which is balanced by the fact that light due to blocks effectively starts at 14 (solid light source blocks emit a level of 15, but that applies to the light source block itself) while sky light brightness is 15 outdoors. Light due to blocks also tends toward orange in the middle ranges, while sky light in the Overworld daytime is white.

In the Overworld with the "Moody" brightness setting, full daylight reaches 98% brightness,[luma 1] while at night brightness is reduced to about 17%[luma 1] and is shaded blue. Full darkness is about 5% brightness.[luma 1]

In the Nether, sky lighting doesn't play a role since there is no source of sky light (although if there were, it would reach about 99% brightness.[luma 1]) Full darkness with the "Moody" brightness setting is at about 25% brightness,[luma 1] slightly darker than a block light level of 7 and no sky light in the Overworld, and is shaded orange like block light.

In the End, sky lighting wouldn't play a role even if there were a source of sky light; this can also be seen if lightning is summoned in the End (there is no flash of brightness like there is in other dimensions). Full darkness in the End with the "Moody" brightness setting is about 28% brightness,[luma 1] and is shaded toward a bluish-green rather than the orange of the Nether and of block lighting.

In Java Edition 20w14∞, most unique dimensions have unique lighting system. However, most of the Easter egg dimensions do not have darkness at all. Instead, they are fully bright, but in an Easter egg dimension called gallery has the blue lighting nearly identical to the Overworld at night (only significantly brighter). Easter egg dimensions that resembles the Overworld with just world generation modifications (namely busy, chess, decay, holes, pillars, rooms, slime, and zone) have the same lighting as in the Overworld. blacklight has the inverted lighting system derived from the Overworld. colors, red, green, and blue dimensions resembles the Overworld with lighting mixed with dimensional tinting, and darkness is blended with darkness at higher distances far away from the origin. Its darkness cannot be fixed with Night Vision effect.

| Light level >Biome/time of day v | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|----------------------------------|---|---|---|---|---|---|---|---|---|---|----|----|----|----|----|----|
| Overworld (day)                  |   |   |   |   |   |   |   |   |   |   |    |    |    |    |    |    |
| Overworld (night, approximate)   |   |   |   |   |   |   |   |   |   |   |    |    |    |    |    |    |
| Blacklight(day)                  |   |   |   |   |   |   |   |   |   |   |    |    |    |    |    |    |
| Blacklight(night, approximate)   |   |   |   |   |   |   |   |   |   |   |    |    |    |    |    |    |

1. ↑ a b c d e fBrightness here refers to ITU-R BT.601 luminance value (luma)


### Smooth lighting
The difference between Smooth Lighting on and off.
Smooth lighting is a lighting engine that blends light levels across block faces and darkens corners using ambient occlusion to add semi-realistic shadows and glowing from light sources. It affects only rendered brightness, not the light level, so it has no effect on mob spawning or crop growth. It is set on by default. Paintings, item frames[1] and water surfaces[2] are unaffected.‌[Java Edition  only]

Smooth lighting can be turned on or off in the video settings.


### Ambient occlusion in Minecraft

  

This section needs cleanup to comply with the style guide. [discuss]
Please help improve this page. The talk page may contain suggestions.


In many newer games, ambient occlusion is mainly generated dynamically by the GPU.
But Minecraft calculates ambient occlusion in the code based on voxel placement and brightness levels. 

Ambient occlusion is responsible for adding shading to an ordinary texture. It is a layer of translucent textures, on top of the normal textures.
Overlaying these AO textures onto a texture is called AO mapping.
There are about five AO texture patterns used in Minecraft's smooth lighting, excluding flips and rotations, and only three patterns algorithmically. Strictly speaking, it's probably more than that. That's when the intensity changes with the brightness level. But they are solved by tint.

### AO texture pattern

  

This section needs cleanup to comply with the style guide. [discuss]
Please help improve this page. The talk page may contain suggestions.


If AO mapping is selected only to the northwest of the voxel, the following pattern is possible.

| Number | Image |
|--------|-------|
| 0      |       |
| 1      |       |
| 2      |       |
| 3      |       |

These classifications allow one the ability to deduce a pattern from the placement of each voxel.
The following function can then be used to compute the opacity of the voxels' vertices, depending on the presence of the side and corner voxels.

function vertexAO(side1, side2, corner) {
  return 3 - (side1 + side2 + corner)
}

This generates a 2×2 pixel image using the values of each vertex. The pixels are small, but when zoomed in using anti-aliasing, it gradates.

 

