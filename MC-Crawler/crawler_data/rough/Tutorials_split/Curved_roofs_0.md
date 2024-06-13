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

