### Far Lands
Main article: Java Edition Far Lands
#### Basic theory
The Far Lands were a complex terrain phenomenon which arise due to a major bug in terrain generation works. Generally, "far lands" are the result of what happens when a given noise generator exceeds the largest value it can handle, resulting in an integer overflow and resulting in the generated values reaching unnatural magnitudes. The term "Far Lands" in isolation most commonly refers to what results from "low noise" and "high noise" overflowing simultaneously.

##### What the Far Lands are not
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

#### The Far Lands
The "corner" of the Far Lands, at ±12,550,821 on both X and Z axes.
In their most well-known iteration, the Far Lands manifested as a sort of "wall" which would extend from the lowest point of the world to the very top. This wall contained a series of holes in it, with these holes reaching back almost infinitely, with only minor changes even after millions of blocks. The density of a cross-section of this wall was roughly 50%, with solid portions and hollow portions being around equal. Given their positions at the four sides of a world, there regions are often referred to as the "Edge Far Lands" when distinction from other regions of a world is necessary, and, due to their "Swiss cheese"-like formation, informally as "The Loop". 

Since the Far Lands existed on both the X and Z axes, it is entirely possible for them to "intersect" each other when surpassing their starting point on both axes. The resulting terrain, named the "Corner Far Lands" in analogy to the vertices of a square, is markedly different from that of the edge regions: the world appears to be solid layers of terrain arranged on top of each other with air gaps in between. Due to this distinctive morphology, the Corner Far Lands are also informally referred to as "The Stack". The terrain seen in these regions is comparable to that which is seen in the Nether. Often, major diagonal or oblique patterns can be seen within the generated terrain, which, if they exist, are especially obvious at the beginning of the corner Far Lands.

In the unmodified game, only four sets each of the edge and corner Far Lands can exist in a world, from the noise overflowing on the X and Z axes. However, game modifications can modify aspects of either chunk saving or terrain generation in ways that ultimately allows for noise to overflow on the Y axis as well. Such modifications reveal two more sets of Edge Far Lands for a total of six sets (corresponding to the faces of a cube), eight sets of Corner Far Lands from these Y axis Edge Far Lands intersecting X and Z axis Edge Far Lands for a total of twelve sets (corresponding to the edges of a cube), and new regions in which all three axes simultaneously overflow due to Y axis Edge Far Lands intersecting the existing Corner Far Lands, with eight of these regions in total (corresponding to the vertices of a cube). These regions, referred to as the "Vertex Far Lands", are incredibly unstable; sometimes these regions are completely solid, other times are completely empty, and other times still feature incredibly strange terrain atypical of even "The Loop" or "The Stack".

With default settings, the noise would overflow at twice the distance on the Y axis as it does on the X and Z axes, at around 25,101,640 blocks.

