### How to construct a segmented dome
- 
- 

1. Choose an even larger circle than is strictly needed for the size of the building.
2. Work upwards from the halfway point until you find the pixel width that does match the size of the building.
3. Read off a list of the widths of the circle from that point upwards. This gives you the list of ring diameters to use.
4. From this point, follow the dome construction guidelines given above.

For example, if you choose the top three rows of a diameter-22 circle, you get 14, 12, 6. That would be a usable set of widths for a size-14 building. The resulting segmented dome would have a diameter of 14 meters but would only need to be three blocks high.

### How to construct a surmounted dome
- 
- 

1. Generate a diameter list as you would for either a standard or a segmented dome (or, for advanced users, any other dome type you may wish to use).
2. Insert one or more repeats of thelowermostdiameter.
3. Follow the dome construction guidelines for a standard dome, but using the adjusted diameter list.

Example 1: The diameter-17 standard dome can be made into a surmounted dome by altering its diameter list to 17, 17, 17, 17, 15, 15, 13, 11, 9, 5 and building accordingly. The more 17's you add to the list, the greater the height of the mount.

Example 2: In the right-hand image the top three layers of a diameter-22 segmented dome have been used for a surmounted dome. The diameter list was adjusted to 14, 14, 14, 14, 14, 12, 6, producing a surmounted segmented dome.

## Barrel roofs
A barrel roof. These curves are barely visible as curves unless built at a very large scale.
A roof with a cylindrical section, as might be seen for the roof of a barn, a warehouse, a hangar or many other large, comparatively simple structures, is termed a barrel roof. The barrel part does not necessarily have to use a full half-circle curve; this picture shows a diameter-18 curve with a height of seven blocks.


## Arched roofs
A gothic roof.
A roman arch is simply a semicircle. An arched roof that uses a roman arch is simply a barrel roof. A gothic arch is pointier. You can generate a gothic arch by drawing two circles of the same radius so that they overlap. To make a pointier arch, move the centers of the two circles further apart. Gothic roofs are rare on residential buildings, and are much more likely to be found on larger buildings such as meeting halls, churches and other such structures. Even barns may have gothic roofs, although they tend to have quite 'fat' arches rather than the much sharper curves seen for churches. There are many technical terms for other types of arches, but they are usually used for openings inside a building, not as its main roof shape.  


## Conical roofs
An approximation to a conical spire.
A cone-shaped roof, as might be seen atop a circular tower or for a church spire, can be constructed in a similar way to the method used for domes. As for domes it's also possible, in principle, to 'smooth' the curve a bit using stairs or slabs, but this is still fiddly and is not recommended except for practiced builders. Recognizable cones are very hard to model except at large scales, or possibly by using Minecraft plugins to tweak the shape of the curve.

### How to construct a conical roof
For a conical roof, a workable manual construction procedure is as follows:

1. Choose the cone's diameter and center. If you want the roof to come to a sharper point, it should have an odd diameter.
2. Find the 'pixel pattern' either from the reference image above, which goes up to diameter 18, or by using a bitmap painting tool of your own.
3. Chose a 'height step'. For example, your conical roof might go up three blocks before its radius shrinks.
	- As for constructing a dome, this gives a diameter list. For example, if you had chosen a diameter 8 cone, the list might be 8, 8, 8, 6, 6, 6, 4, 4, 4, 2, 2, 2.
4. Place a hollow ring of blocks matching the pixel pattern for the lowest ring.
	- e.g. Select the bold italic entry from the list:8, 8, 8, 6, 6, 6, 4, 4, 4, 2, 2, 2
5. Place a hollow ring of blocks for the roof layer above with a diameter matchingitspixel pattern.
	- 8,8, 8, 6, 6, 6, 4, 4, 4, 2, 2, 2
6. Place another hollow ring for the roof layer above that.
	- 8, 8,8, 6, 6, 6, 4, 4, 4, 2, 2, 2
7. Continue placing smaller and smaller concentric rings one atop the other until you reach the end of the list.
	- 8, 8, 8,6, 6, 6, 4, 4, 4, 2, 2, 2
	- 8, 8, 8, 6,6, 6, 4, 4, 4, 2, 2, 2
	- 8, 8, 8, 6, 6,6, 4, 4, 4, 2, 2, 2
	- 8, 8, 8, 6, 6, 6,4, 4, 4, 2, 2, 2
	- …
	- 8, 8, 8, 6, 6, 6, 4, 4, 4, 2,2, 2
	- 8, 8, 8, 6, 6, 6, 4, 4, 4, 2, 2,2
	- Done!

This example produces a conical roof which shrinks from diameter 8 to 2 while rising 12 meters. It's not uncommon for a sharp spire to rise 3−5 blocks, sometimes more, before its radius reduces. You can also change the rate at which the cone reduces in size to give give it a slightly curved profile. For example, instead of a radius reduction every 5 meters, you might start at 4, then increase to 6, 8, 10 as you work up the spire.

Tip: Note that, as for domes, successive rings of a conical roof will always have odd diameters, or always have even diameters. Unless you are using a different construction method of your own, if you ever switch from odd to even or vice versa you have made a mistake.

Tip: You can make an odd-diameter spire look pointier by adding fence posts of some kind as additional levels above the topmost block, and by replacing the diameter 3 circle with four blocks arranged in a diamond rather than eight blocks forming a hollow square.


