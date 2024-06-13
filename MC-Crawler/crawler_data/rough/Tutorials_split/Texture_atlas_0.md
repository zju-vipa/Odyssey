# Texture atlas
A texture atlas, also known as a spritesheet, is an arrangement of game sprites on a single image file, used by the game to store and access associated sprites more efficiently than with individual files.

Minecraft uses both procedurally-generated and predefined texture atlases for different purposes, however all but a very small handful of predefined atlases have since been split into individual files for compilation into larger atlases.

## Contents
- 1 Procedurally-generated texture atlases
- 2 Trivia
- 3 Predefined texture atlases
	- 3.1 Current
		- 3.1.1 experience_orb.png
		- 3.1.2 moon_phases.png
		- 3.1.3 map_icons.png
	- 3.2 Removed
		- 3.2.1 items.png
		- 3.2.2 terrain.png
	- 3.3 Removed from Java Edition, still present in Bedrock Edition
		- 3.3.1 bars.png
		- 3.3.2 icons.png
		- 3.3.3 inventory.png
		- 3.3.4 kz.png
		- 3.3.5 particles.png
		- 3.3.6 widgets.png
- 4 History
	- 4.1 Additions
	- 4.2 Removals
- 5 See also

## Procedurally-generated texture atlases
Block and item textures are combined into the same atlas, minecraft_textures_atlas_blocks.png_0.png. This texture atlas is generated via F3 + S and is saved into a folder titled “debug” in .minecraft's screenshots folder.

All other textures are also available in their own respective texture atlases in said .minecraft/screenshots/debug folder. For example, the particle atlas is minecraft_textures_atlas_particles.png_0.png, while the chest atlas is minecraft_textures_atlas_chest.png_0.png, minecraft_textures_atlas_decorated_pot.png_0.png.

## Predefined texture atlases
### Current
The following texture atlas files are still in use as of Java Edition 1.20.4. It is not known if Mojang plans to split these into their constituent textures in the future, potentially replacing them with a procedurally-generated atlas.

Fonts also use a texture atlas system, however this is data-driven, unlike the following cases, which are hardcoded.

#### experience_orb.png
This file is used for each size of experience orb. The five last textures are unused. The changing coloration used for experience orbs is done via a hardcoded tint system, rather than proper animation as is done for most animated textures, and the translucency is also hardcoded instead of being controlled by the texture's alpha channel.

| Java Edition Beta |       |  |  |                  |                                       |
|-------------------|-------|--|--|------------------|---------------------------------------|
|                   | 1.8   |  |  | Pre-release      | Addedxporb.png.                       |
|                   |       |  |  | Pre-release 2 ;) | Updatedxporb.png.                     |
|                   |       |  |  |                  | Java Edition                          |
|                   | 1.6.1 |  |  | 13w24a           | Renamedxporb.pngtoexperience_orb.png. |

#### moon_phases.png
This file stores all eight phases of the moon. The sun's texture is a separate file.

| Java Edition Indev |       |  |  |                       |                                                                                                                              |
|--------------------|-------|--|--|-----------------------|------------------------------------------------------------------------------------------------------------------------------|
|                    |       |  |  | 20100211              | The moon has been implemented.<br/>At this point, there is only one moon phase, and therefore only one texture file:moon.png |
|                    |       |  |  |                       | Java Edition                                                                                                                 |
|                    | 1.0.0 |  |  | Beta 1.9 Prerelease 4 | Addedmoon_phases.pngwith the addition of different moon phases.<br/>The filemoon.pngstill remains, but is no longer used.    |
|                    |       |  |  | Beta 1.9 Prerelease 6 | Updatedmoon_phases.png.                                                                                                      |
|                    |       |  |  |                       | Java Edition                                                                                                                 |
|                    | 1.6.1 |  |  | 13w24a                | The unusedmoon.pngfile has beenremoved.                                                                                      |

#### map_icons.png
This file is used for static icons on maps. Interestingly, it has many unused icons which have existed for many years.

| Java Edition Beta |         |  |  |                    |                                                                                |
|-------------------|---------|--|--|--------------------|--------------------------------------------------------------------------------|
|                   | 1.6     |  |  | Test Build 3       | Addedmapicons.png.                                                             |
|                   | 1.8     |  |  | Pre-release        | Updatedmapicons.png.                                                           |
|                   |         |  |  |                    | Java Edition                                                                   |
|                   | 1.6.1   |  |  | 13w24a             | Renamedmapicons.pngtomap_icons.png.                                            |
|                   | 1.11    |  |  | 16w39a             | Updatedmap_icons.png.                                                          |
|                   | 1.13    |  |  | 18w10a             | Updatedmap_icons.png.                                                          |
|                   | 1.20.2  |  |  | Pre-release 1      | Updatedmap_icons.png.                                                          |
|                   | 1.20.5  |  |  | 24w12a             | map_icons.pnghas been split into its constituent sprites and has been removed. |
|                   |         |  |  |                    | Pocket Edition Alpha                                                           |
|                   | v0.14.0 |  |  | build 1            | Addedmap_icons.png.                                                            |
|                   |         |  |  |                    | Pocket Edition                                                                 |
|                   | 1.1.0   |  |  | alpha 1.1.0.0      | Updatedmap_icons.png.                                                          |
|                   |         |  |  | alpha 1.1.0.5      | Updatedmap_icons.png.                                                          |
|                   |         |  |  |                    | Bedrock Edition                                                                |
|                   | 1.4.0   |  |  | beta 1.2.14.2      | Updatedmap_icons.png.                                                          |
|                   | 1.5.0   |  |  | beta 1.5.0.7       | Updatedmap_icons.png.                                                          |
|                   |         |  |  | beta 1.5.0.10      | Updatedmap_icons.png.                                                          |
|                   | 1.20.40 |  |  | Preview 1.20.40.20 | Updatedmap_icons.png.                                                          |

### Removed
#### items.png
Main article: items.png
items.png was used for storing the textures of items.

#### terrain.png
Main article: terrain.png
terrain.png was used for storing the textures of blocks.

### 

  

This feature is exclusive to  Bedrock Edition. 


#### bars.png
bars.png was used for storing boss bar textures and their overlays.

The file was compressed in 15w49a, 1.11-pre1 and 19w41a.

| Java Edition |        |  |  |        |                                                                              |
|--------------|--------|--|--|--------|------------------------------------------------------------------------------|
|              | 1.9    |  |  | 15w31a | bars.pnghas been implemented.                                                |
|              | 1.20.2 |  |  | 23w31a | bars.pnghas been removed, with each bar texture split into individual files. |

#### icons.png
Main article: icons.png
icons.png was used for storing the textures of certain UI elements.

#### inventory.png
Main article: inventory.png
This file still exists as of Java Edition 1.20.4, but only houses the inventory window; it was formerly an atlas containing further sprites, and before that housed several status effect textures.

#### kz.png
Main article: kz.png
kz.png is used for storing the textures of paintings.

#### particles.png
Main article: particles.png
particles.png is used for storing the textures of most particles. Two other atlases, explosion.png and sweep.png, were used for respectively storing explosion and sweeping attack particles.‌[Java Edition  only]

#### widgets.png
Main article: widgets.png
widgets.png (previously known as gui.png) was used for defining several types of menu buttons and icons.


