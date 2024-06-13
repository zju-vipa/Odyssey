#### The Farther Lands
The Edge Far Lands are on the right, with the comparatively featureless Edge Farther Lands on the left.
The Farther Lands is the name given to another noise overflow which, by default, happens at a greater distance than the normal Far Lands. Whereas the usual Far Lands arise from the overflowing of "low noise" and "high noise", the Farther Lands sees "selector noise" break down instead. Low noise and high noise are two different noise generators which the game uses to generate the potential fundamental shape of terrain, whereas selector noise chooses whether low noise or high noise is used to actually generate the terrain at that given point. When the conventional Far Lands start, despite both low noise and high noise overflowing simultaneously, selector noise still functions normally, meaning that there is still a large amount of possible variation in the shape of the Far Lands.

When selector noise does eventually break, which happens at roughly 1,004,065,920 blocks from the world origin, it follows that the variation between low and high noise also breaks down. Like how the usual Far Lands is a series of straight tunnels, the Farther Lands divides the world into a series of straight regions, with low noise used exclusively in one region and high noise in others. As such, the variation usually seen in the Far Lands vanishes after the Farther Lands.

The Corner Farther Lands take this effect to an extreme: while the normal Corner Far Lands are rich in nuance, the Corner Farther Lands are almost devoid of it. The beginning of the corner makes this all the more obvious, and also highlights edge Farther Lands-corner Far Lands intersections, making the aforementioned straight line regions clear to see.

#### Before inf-20100327
The stone wall at 33,554,432 blocks from the origin in inf-20100227-2.
Terrain generation was much simpler in versions before March 27, 2010. While in modern versions, the noise generator used for terrain is 3D, earlier versions used a purely 2D noise generator for the world instead. The resulting terrain was much more cliff-based as a result, and overhangs were an impossibility. In addition, noise incremented much slower than the modern noise generator does, resulting in it overflowing at 33,554,432 blocks out (coincidentally a power of 2).

Rather than featuring a series of holes, this noise generator instead created a huge, featureless wall as it broke, as the purely 2D nature of the noise forbids any overhangs from generating. This wall is completely solid stone and extends infinitely outwards when it starts. Occasionally, the faces of this wall may appear ridged like a radiator or heat sink, resulting in a slightly more gradual transformation of the terrain.

#### Further investigations
While largely removed as of Beta 1.8, simple modifications to the game can effectively reintroduce them, in which case they behave effectively identically to how they did before, but much more stable due to the fixing of the vast majority of high-distance precision loss effects in earlier versions which caused lag and hindered movement. In addition, several aspects of the Far Lands persisted into later versions:

- The Far Lands also existed on the y-axis at twice the distance as they did on the x-axis. While obviously unobservable due to blocks not being able to exist at all outside of a certain height range, abuse of theOld Customizedworld type in which the height scale is increased to absurd values could allow for the positive Y-axis Far Lands, or "Sky Far Lands", to generate within vanilla bounds without modding.
- Beta 1.8 fixed the Far Lands by adding code to the noise generator to have it repeat after a certain amount of units. It is possible to have the amount of times the generator repeats to itself overflow, although the effects of this are not possible to see in vanilla worlds (it would only break down after almost 54 quadrillion blocks). However, further exploitation of Old Customized to set the coordinate scale to even more ludicrous values will bring this overflow point into vanilla bounds once more. As setting it to values like these causes normal terrain to become incredibly chaotic, the point at where it breaks is difficult to see.
	- For low and high noise, these overflowed regions are called the Fartherer Lands, and for selector noise, the Farthest Lands.

Modding has allowed for y-axis Far and Farther Lands, the Fartherer and Farthest Lands, and 64-bit versions of the Far and Farther Lands (distinct from the Fartherer and Farthest Lands in while they appear at the same locations as them, they result from 64-bit noise breaking normally rather than the modulo that prevents 32-bit noise from breaking itself) to be seen in their natural habitats.


## Generated structures
### Brick pyramid
Main article: Brick pyramid
Brick pyramids were tall experimental generated structures made up exclusively of bricks. They were added in Java Edition Infdev 20100227-1 and they were removed from the game in Java Edition Infdev 20100327.

These were entirely composed of bricks - the pyramids did not have any rooms inside, however caves could generate through them Java Edition Infdev 20100325 due to caves being able to generate through any blocks at the time (including trees and other structures they should not be able to).

These were most likely intended for testing structure generation in infinite worlds. As blocks did not drop items at the start of Infdev due to entity code still being reworked, brick blocks could not be collected from pyramids for most of their existence.

