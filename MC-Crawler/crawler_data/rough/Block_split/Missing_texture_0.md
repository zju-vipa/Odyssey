# Missing textures and models
Minecraft makes use of missing textures and missing models to handle potential errors present in the game's resources as well as resource packs.

## Contents
- 1 Missing texture
	- 1.1 History
		- 1.1.1 History of the texture itself
		- 1.1.2 General history
- 2 Missing model
	- 2.1 History
		- 2.1.1 History of the model itself
			- 2.1.1.1 Block
			- 2.1.1.2 Item
		- 2.1.2 General history
- 3 Notable bugs
	- 3.1 Examples of cases where the missing model is not used
	- 3.2 Translucency ordering
	- 3.3 Unloading the default resources
- 4 Trivia
- 5 Gallery
- 6 References
- 7 See also

## Missing texture

  

This section is missing information about A solid magenta texture may be possible somehow:
https://youtu.be/q1UC2-6vtIw?t=4m16s
https://github.com/rwtema/DietHopper/issues/4. 
Please expand the section to include this information. Further details may exist on the talk page.



The missing texture is a placeholder texture used by Minecraft for handling cases where a suitable texture cannot be found. Outside of its use in missing models, this is almost always due to a texture being referenced which simply does not exist under that name.

The texture uses a prominent black  #000000 and magenta  #f800f8 checkerboard in Java Edition or a black  #000000 and magenta  #fc00ff checkerboard in Bedrock Edition, in order to stand out as much as possible in most cases. Using bright colors is industry standard, and black and magenta is employed by other game development studios, notably Valve.[1]

The texture is not intended to appear in vanilla gameplay, and cases where it does are due to misconfigured resource packs.

As of Java Edition 21w42a, there are six ways in which the missing texture can appear without using a resource pack, all of which require commands:

- By creatingminecraft:block_markerparticles associated with eitherair,cave airorvoid air:[2]
	- /particle minecraft:block_marker minecraft:air
	- /particle minecraft:block_marker minecraft:cave_air
	- /particle minecraft:block_marker minecraft:void_air
- By creatingminecraft:itemparticles associated with either air or aspyglass:[3][4]
	- /particle minecraft:item minecraft:air
	- /particle minecraft:item minecraft:spyglass
- By summoning apandaeating a spyglass.[4]
	- /summon minecraft:panda ~ ~ ~ {HandItems:[{id:"minecraft:spyglass", Count:1b},{}]}

When the game has to use the missing texture, such uses are generally announced in the game's output log:

- References to nonexistent textures results inUsing missing texture, unable to load [NAMESPACE]:textures/[TEXTURE].png : java.io.FileNotFoundException: [NAMESPACE]:textures/[TEXTURE].png
- Absent texture references for model elements results inUnable to resolve texture reference: #texture in [NAMESPACE]:block/[MODEL]
- Cases where no particle texture is specified does not output anything to the log at all.[5]This is why the air and spyglass items' use of the missing texture for particles goes unreported in the game logs.

### History
For cases where the missing texture was used in-game, see Java Edition missing texture and model uses § Missing texture and Bedrock Edition missing texture and model uses § Missing texture.

#### History of the texture itself
| Java Edition Beta |         |  |  |         |                                                                                                                                                                                                                                                                                                                       |
|-------------------|---------|--|--|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                   |         |  |  | 1.4     | The missing texture has been implemented. It differs depending on the system - see the subsection below.                                                                                                                                                                                                              |
|                   |         |  |  |         | Java Edition                                                                                                                                                                                                                                                                                                          |
|                   | 1.5     |  |  | 13w02a  | The missing texture has changed to display more descriptive text.                                                                                                                                                                                                                                                     |
|                   | 1.6.1   |  |  | 13w18a  | The missing texture generated has changed to a magenta and black checkerboard texture.                                                                                                                                                                                                                                |
|                   | 1.7.2   |  |  | 13w38a  | When anisotropic filtering is enabled, the missing texture has a 4x4 checker instead of a 2x2 checker.[6][7][8]This is due to the option replacing each texture with a 3x3 grid of the texture and selecting the middle 32x32 of it, which for the missing texture specifically gives the appearance of a 4x4 tiling. |
|                   | 1.8     |  |  | 14w25a  | Removed the anisotropic filtering option, meaning that the 2x2 checker is once again the only missing texture.                                                                                                                                                                                                        |
|                   | 1.13    |  |  | 17w43a  | The missing texture generated has changed.                                                                                                                                                                                                                                                                            |
|                   |         |  |  |         | Pocket Edition Alpha                                                                                                                                                                                                                                                                                                  |
|                   | v0.16.0 |  |  | build 5 | The missing texture has been implemented.                                                                                                                                                                                                                                                                             |

** b1.4-13w17a platform differences **

  

This section is missing information about 
MC-7225 OS X
MC-5094 OS X
MC-8997 OS X
include info on the exact match
find out what the exact match actually is
(it's probably the thing from github). 
Please expand the section to include this information. Further details may exist on the talk page.


The missing texture used in these versions would be generated differently depending on the operating system and Java version.[9]

| Texture       |                 | Operating system      | Java version                                                                                                                   | Notes                                                                                                              |
|---------------|-----------------|-----------------------|--------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| b1.4 - 13w01b | 13w02a - 13w17a |                       |                                                                                                                                |                                                                                                                    |
|               |                 | Windows XP            | 6.0.370.6[10]<br/>                                                                                                             | Appears standard across all Windows versions.<br/>No smoothing.                                                    |
|               |                 | Windows 7[11]         | 7[12] Update 11[13] Update 13[14] r15[15] Update 17[16]<br/>Update 11[13]<br/>Update 13[14]<br/>r15[15]<br/>Update 17[16]<br/> |                                                                                                                    |
|               |                 | Windows 10            | 1.8.0_51[17]<br/>                                                                                                              |                                                                                                                    |
|               |                 | Solaris 10[18]        | * 1.6.0_37[19]                                                                                                                 |                                                                                                                    |
|               |                 | Windows 10            | 11.0.10[17]<br/>16.0.2<br/>                                                                                                    | Minor differences in the x and u. No smoothing.                                                                    |
|               |                 | MacOS 10.3.9[20]      | 4[20]<br/>                                                                                                                     | No smoothing - standard for non-Retina systems.[17]                                                                |
|               |                 | MacOS 10.5.8          | 1.5.0_30[21]<br/>                                                                                                              |                                                                                                                    |
|               |                 | MacOS 10.6.8[22]      | 6[22]<br/>                                                                                                                     |                                                                                                                    |
|               |                 | MacOS 10.14.6[17]     | Apple legacy Java runtime 1.6.0_65-b14-468[17]<br/>                                                                            |                                                                                                                    |
|               |                 | MacOS 10.14.6[17]     | Apple legacy Java runtime 1.6.0_65-b14-468[17]<br/>                                                                            | Monochromatic smoothing - standard for Retina systems.[17]                                                         |
|               |                 | MacOS 10.14.6         | Apple legacy Java runtime 1.6.0_65-b14-468[23]<br/>                                                                            | Uses polychromatic smoothing instead of monochromatic smoothing like above.                                        |
|               |                 | MacOS 10.3.9[24]      | 4[24]<br/>                                                                                                                     | Monochromatic smoothing. Almost identical to the above version, with almost unnoticeable single-pixel differences. |
|               |                 | MacOS 10.5.8[25]      | Unknown                                                                                                                        |                                                                                                                    |
|               |                 | MacOS 10.4.11         | 1.5.0_19[26]<br/>                                                                                                              | Polychromatic smoothing.                                                                                           |
|               |                 | MacOS 10.14.6[17]     | 1.7.0 80-b15[17]<br/>1.8.0_51[17]<br/>                                                                                         | No smoothing.                                                                                                      |
|               |                 | MacOS 10.14.6[17]     | 1.8.0_301, GraalVM EE 21.2.0<br/>11.0.12, GraalVM EE 21.2.0<br/>16.0.2, GraalVM EE 21.2.0<br/>                                 | Monochromatic smoothing.                                                                                           |
|               |                 | MacOS 12.3.0[27]      | 1.8.0_74 (64-bit)[27]<br/>                                                                                                     | Appears to have been smoothed monochromatically with all non-white pixels subsequently set to black.               |
|               |                 | Debian[28]            | 1.8.0_351<br/>                                                                                                                 | No smoothing.                                                                                                      |
|               |                 | Debian[28]            | Zulu OpenJDK 1.8.0_352<br/>                                                                                                    | No smoothing.                                                                                                      |
|               |                 | Debian under WSL2[29] | 11.0.11<br/>                                                                                                                   |                                                                                                                    |
|               |                 | Ubuntu                | 16.0.1[30]<br/>                                                                                                                |                                                                                                                    |
|               |                 | FreeBSD               | 16.0.2<br/>                                                                                                                    |                                                                                                                    |
|               |                 | OpenBSD               | 16.0.2<br/>                                                                                                                    |                                                                                                                    |
|               |                 | Solaris 11[31]        | * 1.8.0_311[32]                                                                                                                |                                                                                                                    |
|               |                 | Arch[33]              | Temurin-17.0.3+7<br/>                                                                                                          | No smoothing.                                                                                                      |
|               |                 | Arch 6.1.1[34]        | 1.8.0_352 (64-bit)<br/>                                                                                                        | No smoothing.                                                                                                      |

