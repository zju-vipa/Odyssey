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

