##### watercolor.png
Java Edition Beta 1.6 Test Build 3 introduced this file to the /misc/ directory in the jar file. This image was a color map intended to be used depending on the biome, similarly to the existing grasscolor.png and foliagecolor.png, where a color would be selected from a point on the image depending on temperature and humidity.

Intended for use on water, with the game even containing unused code around the time of its introduction which would apply it to water,[28] it ultimately remained unused, with water maintaining a constant color regardless of biome at the time. This may or may not be due to water's texture being blue at the time, rather than the gray or white required for an effective tint, and as such multiplying it with a color would yield undesirable results (tinting already-blue water with another shade of blue would just make it much darker and unsightly); since water's texture was generated at runtime rather than defined as an image, actually making water's raw texture be gray would be a non-trivial task.





Biome-tinted water was first introduced in Java Edition Beta 1.9 Prerelease, but only to a very limited extent, as swamps were the only biome to have a tint defined, and as water's texture was still blue by default, swamp water had to be tinted green to make it appear browner.

When procedurally-generated animated textures were replaced by texture files in 13w02a, the water texture was still inherently blue, even though making it gray or white would have been an easy task at this point and would allow watercolor.png to be used for biome-dependent water colors.

watercolor.png was ultimately removed in 13w24a alongside many others due to it remaining unused.

When Java Edition 18w15a expanded on biome-dependent water tints (and made the water textures white to accommodate this), the subject biomes still remained limited, as swamps and different temperature oceans were the only[verify] biomes to have colors which differed from the default color specified. These colors were values explicitly specified per biome, rather than taken from a colormap like watercolor.png. As a result of this approach, there are currently several oversights in the current game where special water colors have not been defined for certain biomes even when they should be.[29]

Reimplementing and actually using this file for the majority of biomes, like is done for grass and foliage, with swamps and possibly a few other biomes being the only remaining special-cased biomes, would likely resolve this issue in its entirety, as there would no longer be a need to specify water colors in biome json files; a blank entry would cause the game to seek out a value from the color map, which is what happens currently for grass and foliage.


