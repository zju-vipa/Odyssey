# Far Lands
The Far Lands[1] were a terrain generation bug that appeared when the noise generators responsible for creating the shape of terrain stopped functioning properly. This resulted in a large, spongy wall of terrain appearing around 12,550,821 blocks from the origin of the Minecraft world. 

The Far Lands still retain a legacy as one of the franchise's most famous glitches, even being referenced in other official games such as Minecraft: Story Mode and Super Smash Bros. Ultimate.

## Contents
- 1 General information
	- 1.1 What the Far Lands are not
	- 1.2 Types of Far Lands
	- 1.3 Walking to the Far Lands
- 2 Trivia
- 3 References

## General information
### What the Far Lands are not
Due to many occurrences at high distance being lumped together with each other, confusion often arises as to what is related to or caused by the Far Lands, and what is not. The following is a list of things which are commonly misattributed to being a product, effect or even type of the Far Lands, despite not being so.

** Precision loss errors are not caused by the Far Lands **
The position where the world appears to render is considerably offset at the point where the Far Lands begin in Beta 1.7.3 and earlier, with a magnitude of one block, with the player appearing to be at the edges and corners of blocks at all times.

However, this is purely a floating-point bug, and exists whether or not the Far Lands themselves do. This can be demonstrated by the following:

- Noticing that the precision loss is a gradual change, which increases at each power of 2. This is in stark contrast to the Far Lands, which happen immediately due to integer overflow.
- Backporting a Superflat world (with flat terrain where the Far Lands would be) from 1.1 to Beta 1.7.3, and noticing that the effect persists in said version, proving that it's clearly not linked to terrain. While Far Lands chunks still generate outside of what superflat chunks were generated in 1.1, these still are unrelated.
- Modding the game can be done to either patch out this precision loss issue or the Far Lands individually. This proves their existence to be completely independent.
- Generating the Far Lands in any version between the March 27 and June 18 builds of Infdev inclusive. Whereas the Far Lands clearly generate in these versions, the precision loss bug was first introduced in the June 24th build.

This is also true of every other precision loss bug, especially those which were not fixed in Beta 1.8 and persisted into later versions after the Far Lands were removed in said version, demonstrating that they are two completely different things which are associated with each other due to happening at high distances.

** The Stripe Lands are not a type of Far Lands **
The Stripe Lands, a mostly Bedrock Edition-exclusive phenomenon which can be seen in Java Edition only through extensive modding, are another example of floating-point precision loss, and are not a terrain bug.

** Fake chunks are not caused by the Far Lands **
"Fake" chunks at the world boundary are another anomaly that happens at high distances. Occurring considerably past the Far Lands' beginning, they are commonly said to be a "part" or "layer" of the Far Lands. While they are among the interesting effects which can be experienced when moving high distances from the world origin, their occurrence is a distinct phenomenon, and, to an extent, actually intended. This is further reinforced by them being at a rather round number (32 million), rather than the seemingly overall arbitrary 12,550,824 of the Far Lands, or power-of-two values such as 16,777,216 where precision loss worsens.

** Hard limits are not caused by the Far Lands **
While the Far Lands themselves are technically a hard limit due to arising from integer overflow, they are treated solely as a terrain phenomenon, and the game still functions fine with them. Integer overflows in other cases such as player position are much more dangerous and much harder to reach, and are considered separately.

### Types of Far Lands
The Far Lands comprise a very, very wide array of terrain generation bugs. The effects vary depending on which noise generator breaks (for traditional Far Lands, "low noise" and "high noise" are jointly responsible), as well as the player's distance on each axis (the "Edge Far Lands" refer to when noise breaks on only one axis, the "Corner Far Lands" on two, and the "Vertex Far Lands" on three).

Other noise generators are capable of breaking down. Selector noise, a noise generator which determines whether low noise or high noise is used at a given position in the world, breaks down 80 times further than low and high noise by default, giving rise to what is known as the "Farther Lands".

A full list of Java Edition noise generators known to break down and give rise to their own unique effects is as follows. Note that it assumes that the X and Z axes are identical, and ignores the Y axis; in many cases, the Y axis has a different value from the X and Z axes, whereas in other cases the noise generator is entirely 2D.

| Noise generator     | Breaks down at...(32-bit) | Version range             |              | Notes                                                                                                                                                           |
|---------------------|---------------------------|---------------------------|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                     |                           | First                     | Last         |                                                                                                                                                                 |
| Low noise           | 12,550,824                | inf-20100327              | present[n 1] | Jointly responsible for the Far Lands                                                                                                                           |
| High noise          |                           |                           |              |                                                                                                                                                                 |
| Selector noise      | 1,004,065,924             | inf-20100327              | present[n 1] | Responsible for the Farther Lands                                                                                                                               |
| Depth noise         | 42,949,672                | [more information needed] | present[n 1] | Causes the terrain to rise up several blocks.<br/>"Stretching effects" are rare.<br/>Impossible to see unless made to start before low and high noise overflow. |
| Scale noise         | 7,662,742,722             | [more information needed] | Beta 1.7.3   | Superseded by biome-based terrain height in Beta 1.8.                                                                                                           |
| Classic world noise | 33,554,432                | [more information needed] | inf-20100325 | Causes the famous "stone wall" of Infdev.                                                                                                                       |
| Island carver noise | 933,688,542               | [more information needed] | in-20100223  | Used to create Floating maps in Indev.<br/>Due to their limited world size,<br/>this breaks far beyond what can generate.                                       |
| Soil depth          | 34,359,738,368            | [more information needed] | present[n 1] | Causes large regions of exposed stone in earlier versions,<br/>or gravel in later versions.                                                                     |
| Sand beaches        | 68,719,476,736            | [more information needed] | Beta 1.7.3   | Determines whether beaches use sand or not.<br/>In the Nether, this controls soul sand.                                                                         |
| Gravel beaches      | 68,719,476,736            | [more information needed] | Beta 1.7.3   | Determines whether beaches use gravel or not.<br/>Also exists in the Nether for gravel.                                                                         |

1. ↑ a b c dNo longer overflows within vanilla bounds as of Beta 1.8 Pre-release

### Walking to the Far Lands
Walking to the Far Lands is the time-consuming challenge involving a terrestrial journey 12.5M blocks out of spawn. The most common version used is b1.7.3 as this is the last version to contain the Far Lands and has the conveniences such as beds that some previous versions don't have.

Over 30 players have attempted the feat legitimately, with about 1/3 completing the journey, 1/3 currently walking (as of October 2023) and 1/3 having gone inactive (including one death, TinfoilChef). The first player to complete the journey (without using the Nether as a means of shortcut) was KilloCrazyMan between 2019-20. Notch awarded him $6,000 through two separate donations. The most famous is the ongoing Far Lands or Bust with KurtJMac, through which he donated over $460,000 to charity in over 10 years.[2]

Time-wise, the walking (not sprinting) speed is 4.3 blocks per second. Walking for 6 hours per day is equal to 21,600 seconds, giving a travelled distance of 92,880 blocks every day. Walking to the 12.5M Far Lands would take just under 136 days at this pace.

Furthermore, one person, Xelanater, has reached the Nether Far Lands legitimately.[2]

