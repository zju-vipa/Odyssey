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


