# Tutorials/Curved roofs
To get a roof that looks curved in Minecraft, you should generally expect to work on quite a large scale. If the curve radius is less than about six meters, the roof will tend to look like a normal pitched roof with a strange mixture of pitches. At smaller scales, it is easier to correctly interpret a dome structure as curved, but other curves may not even be recognizable.

## Contents
- 1 Curve Basics
- 2 Domes
	- 2.1 Segmented dome
	- 2.2 Surmounted dome
	- 2.3 Other dome types
	- 2.4 How to construct a hemispherical dome
	- 2.5 How to construct a segmented dome
	- 2.6 How to construct a surmounted dome
- 3 Barrel roofs
- 4 Arched roofs
- 5 Conical roofs
	- 5.1 How to construct a conical roof
- 6 Other complex curves
- 7 Concave curves
- 8 Circle and Dome Generators
- 9 See also

## Curve Basics
Pixel circles of diameters 1−18.
For reference, this image shows a set of pixel-perfect circles with diameters from 1 to 18 pixels. It was generated from a simple graphics program zoomed in to 800% and with the grid turned on. If you want to generate larger circles for yourself, or ellipses or other curves, Paintbrush (macOS), Microsoft Paint (Windows), and GIMP (free software available on most platforms including macOS, Windows, and Linux) are all useful tools. However, if you need to generate more sophisticated shapes, then you may begin to need more powerful tools than just a basic bitmap editing package.

When constructing a curve, one would usually treat one pixel as corresponding to one block. By using stairs and half-slabs it is sometimes possible to treat one pixel as a quarter of a block, but because no quarter-pixel blocks exist in the game as yet, it won't always be possible to match the desired curve perfectly.

We now consider the main curve options, in approximate order of how easy it is to make them look convincing.

## Domes
- Small domes
- Diameter-5 dome, built with blocks.
- Diameter-5 dome, built with blocks, slabs and stairs. Quartz slabs have been used as internal 'filler'.

- Large domes
- Diameter-16 dome, built with blocks. Quartz slabs have been used as internal 'filler'.
- Diameter-16 dome, built with full blocks, slabs and stairs.

Domes are often seen in temples and other large, 'monumental' or civic buildings. Domes 'work' because in Minecraft one tends to assume a small symmetrical blob is supposed to be a dome even if it is actually quite angular. By comparison, other curved shapes are a lot harder to interpret, and because of this, they must be of much better quality before they look acceptable.

Note that building domes by hand, especially using stairs and slabs, is very fiddly. It is strongly recommended that you use an external tool such as MCEdit to make these shapes.

### Segmented dome
A segmented dome.
A segmented dome can be created by taking just the top rows of a larger-than needed dome. The effect is to produce a dome that joins the building walls at a shallower angle, whereas a hemispherical dome would be fully vertical at the point it joins the walls. In this image, the top three layers (diameters 14, 12 and 6) of a diameter-22 dome were chosen.


Another segmented dome.
Another way to make a segmented dome is to use a normal dome 'recipe' but use slabs instead of stairs. You can also use both methods combined. The right-hand example uses diameters of 13, 11, 9 and 5 meters.


### Surmounted dome
A surmounted dome.
A segmented, surmounted dome.
A surmounted dome is a dome raised on a cylindrical base. It is shaped like a large cylinder with a rounded end. Shown on the left is a diameter-17 surmounted dome, with a four-block cylinder height, and on the right is a segmented, surmounted dome.


### Other dome types
Domes do not necessarily have to be circular domes. Other possibilities include ellipsoidal domes, bell domes, onion domes, surmounted domes, segmented domes, compound domes and more. With the exceptions of the surmounted and segmented domes, these other shapes tend to be harder to model well than a simple semi-circular dome, so unless you are working on a very large scale project and have computer assistance it's probably best to avoid them.

### How to construct a hemispherical dome


If you do want to make a dome by hand, the rough procedure is as follows:

1. Choose the dome's diameter and center.
2. Find the 'pixel pattern' either from the reference image above, which goes up to diameter 18, or by using a bitmap painting tool of your own.
3. Read off a list of the widths of the circle at various heights. It may be helpful to think of the image as showing a vertical cross-section through your dome.
	- For example, if you had chosen a diameter 17 dome, the list might be 17, 17, 15, 15, 13, 11, 9, 5.
4. Place a hollow ring of blocks matching the pixel pattern for the lowest ring.
	- e.g. Select the bold italic entry from the list:17, 17, 15, 15, 13, 11, 9, 5
5. Place a hollow ring of blocks for the roof layer above with a diameter matchingitspixel pattern.
	- 17,17, 15, 15, 13, 11, 9, 5
6. Place another hollow ring for the roof layer above that.
	- 17, 17,15, 15, 13, 11, 9, 5
	- (In this case, we now need to switch to using the diameter 15 pattern.)
7. Continue placing smaller and smaller concentric rings one atop the other until you reach the end of the list.
	- 17, 17, 15,15, 13, 11, 9, 5
	- 17, 17, 15, 15,13, 11, 9, 5
	- (Now we've switched to 13.)
	- 17, 17, 15, 15, 13,11, 9, 5
	- (And now 11…)
	- 17, 17, 15, 15, 13, 11,9, 5
	- Diameter 9 − nearly there…
	- 17, 17, 15, 15, 13, 11, 9,5
	- Finished!
8. Fill in any interior gaps.

Tip: Note that successive rings for a dome will always have odd diameters, or always have even diameters. If you ever switch from odd to even or vice versa you have made a mistake.

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


## Other complex curves

  

This page would benefit from the addition of more images. 
Please remove this notice once you've added  suitable images to the article.  The specific instructions are: example images are welcome


Complex curves, including saddle shapes and nested arches, may be seen in large modern buildings like the Sydney Opera House, many stadiums and skyscapers. Older buildings may have 'ogee roofs' − roofs whose profile follows an ogee curve.

These curves can be quite easy to do provided the building is sufficiently large that Minecraft's one-meter 'block resolution' is fine enough, but such structures tend to require a minimum building size of at least 20×20 blocks and often more. If you are working at this scale you will probably be using external computer programs or graphics tools to help with the design.

## Concave curves

  

This page would benefit from the addition of more images. 
Please remove this notice once you've added  suitable images to the article.  The specific instructions are: example images are welcome


Roofs with concave curves, as in the style of some traditional Japanese buildings made with bamboo are by far the hardest shapes to model well in Minecraft. At small scales − that is, at comparable sizes to NPC village buildings − it is probably best to approximate them using straight sections, possibly using fence posts, signs, or different materials to make the straight lines less obvious.

## Circle and Dome Generators
- Mineconics for 2D Curves
- Voxel for 3D Curved Structures

