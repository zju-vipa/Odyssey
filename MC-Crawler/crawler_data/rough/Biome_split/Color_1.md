### Dyed sheep
Sheep colors do not seem to match dye colors or firework star colors directly one to one, they differ slightly.[more information needed]

### Wolf and cat collar
Both wolf and cat collars use the dye colors directly one to one.

### Experience orbs
For the colors applied to the world border, see Miscellaneous colors § Experience orbs.

Experience orb textures are mostly white, gray, and red; a gradient is applied afterward to make them green and yellow.

### Other
#### Particles

  

This section is missing information about Create a full list of particles that actually use colors. 
Please expand the section to include this information. Further details may exist on the talk page.


Alongside potion particles, several other particles are stored as gray textures with colors applied to them after the fact. Notable examples are the various dripping particles (water, lava, honey, crying obsidian, spore blossom), critical hit (which has a white texture but an orange color is later applied), and magic crit (same).

Note blocks also emit particles, whose base texture is gray, that change color through the spectrum.

Commands can be used to set the colors of some but not all particles.

#### Banners
Banners are colored according to default  dye colors.

#### Beacon Beam
Beacon beams are colored according to default  dye colors. Without any stained class, it defaults to the color for white dye.

#### End gateway beam
For the colors applied to end gateway beams, see Miscellaneous colors § End Gateway beam.

The end gateway creates a beam under certain circumstances which is colored different colors depending on why said beam is created.

#### Guardian beam
For the colors applied to guardian beams, see Miscellaneous colors § Guardian beam.

When attacking, guardians shoot a ranged beam which follows a gradient dependent on time.

#### World border
For the colors applied to the world border, see Miscellaneous colors § World border.

The world border in Java Edition has several colors. A blue color is applied if the border is stationary. If expanding, the world border takes on a green hue. If the world border is shrinking, the world border turns red. In the Nether, the world border is always red no matter if it is expanding, stationary, or shrinking. The world border becomes more opaque the closer the player is to it, and more transparent if the player is further away.

## Biome colors
grass.png
grass.png with all used pixels with respective temperature and downfall values.
foliage.png
foliage.png with all used pixels with respective temperature and downfall values.
swamp_foliage.png in bedrock resource. All pixels colored  #6A7039.
The temperature and downfall values of a biome are used when determining the colors of a selection of blocks: grass, grass blocks, some leaves, vines, sugar cane, and other features such as water and the sky. Blocks such as mossy cobblestone, mossy stone bricks, and the stems of flowers are not affected by biome coloration.[1]

Biome grass and foliage colors are selected from two 256×256 colormap images: grass.png and foliage.png. Both colormaps can be found in assets\minecraft\textures\colormap‌[JE  only] or textures\colormap.‌[BE  only] The grass.png colormap sets the colors for the grass block top and overlay sides, grass, tall grass, fern, tall fern. Meanwhile, the foliage.png colormap sets the colors for oak, jungle, acacia, dark oak, and mangrove leaves.

Biome colormaps use a triangular gradient by default. However, only the colors in the lower-left half of the image are used, even though the upper-right side of foliage.png is colored. Furthermore, as shown in the template image to the left, a select few pixels are considered when the colormap is read by the game, and are determined by the code below.

The temperature and downfall values are used when determining the biome color to select from the colormap. Treating the bottom-right corner of the colormap as temperature = 0.0 and downfall = 0.0, the adjusted temperature increases to 1.0 along the X-axis, and the adjusted downfall increases to 1.0 along the Y-axis. The clamp limits the range of the temperature and downfall to 0.0–1.0. The clamped downfall value is then multiplied by the 0.0–1.0 adjusted temperature value, bringing its value to be inside the lower left triangle. Some biomes' ranges are shown in the template above; the multiplication makes all the line segments point toward the lower right corner.

At borders between or among biomes, the colors of the block and its eight neighbors are computed and the average is used for the final block color.

In Bedrock Edition, biome colors are also visible on maps.[2]

### Hard-coded colors
Certain biome colors are hard-coded, which means they are locked into the Minecraft code and are not retrievable from any texture file. Thus, they cannot be modified without the use of mods or shaders.

#### Swamp color
Swamp temperature, which starts at 0.8, is not affected by altitude. Rather, a Perlin noise function is used to gradually vary the temperature of the swamp. When this temperature goes below −0.1, a lush green color is used ( #4C763C); otherwise it is set to a sickly brown ( #6A7039).

#### Dark forest color
The dark forest biomes' grass color is retrieved normally, then bit masked with the number #FEFEFE, and averaged with a dark green color ( #28340A) to produce the final color.

#### Badlands color
All badlands biomes' grass and foliage have hard-coded colors, which are two tan colors ( #90814D and  #9E814D respectively). These are not modifiable by grass.png and foliage.png, and are unaffected by temperature.

#### Other colors
Several other biome colors are set into the game and currently require external tools in order to be changed. This includes blocks such as birch and spruce leaves and water (which have a hard-coded overlay set onto them), and other features such as the sky and fog.[more information needed]


