# Jigsaw structure
Jigsaw structures are structures that generate using Jigsaw Blocks.
They are used to generate pillager outposts, villages, bastion remnants, ancient cities, trail ruins, and trial chambers‌[upcoming: JE 1.21 & BE 1.21].
The Jigsaw structure generation can be customized using data packs.‌[Java Edition  only]

## Contents
- 1 Generation
	- 1.1 Step 1: Starting piece
	- 1.2 Step 2: Connecting pieces
		- 1.2.1 Connecting piece selection
		- 1.2.2 Connecting piece try
		- 1.2.3 Piece placement condition
	- 1.3 Step 3: Processing
- 2 Pool aliases
	- 2.1 direct
	- 2.2 random
	- 2.3 random_group
- 3 Data values
	- 3.1 ID
	- 3.2 Config

## Generation
The generation places a number of pieces. A piece is usually a structure template, but can also be a placed feature. The pieces are organized into template pools. During generation pieces are randomly selected from a given template pool.

When a structure is generated starting from a given chunk, it generates in a number of steps, detailed below. 

### Step 1: Starting piece
A jigsaw structure defines a  start_pool. A piece is selected from this pool and placed in a random rotation at the starting position. The starting position is the 0, 0 chunk coordinate of the starting chunk. If the  project_start_to_heightmap is set, the start height is based on the specified heightmap, offset by the values result of  start_height. Otherwise,  start_height is used to determine the start height.

If the structure defines as  start_jigsaw_name, then a jigsaw block with that name is randomly selected and in the placed at the starting position. If no matching jigsaw block is found, the whole structure fails to generate. 

If the structure has  start_jigsaw_name unset, the north west corner of the (unrotated) piece is placed at the starting position.

Finally, the starting piece is put into a generation queue.

### Step 2: Connecting pieces
The generation queue is processed sequentially. A piece is removed from the queue when is processed. Of the processed (parent) piece all jigsaw blocks are then used to generate a connecting piece. The jigsaw blocks are handled in order from high to low selection priority set in each jigsaw block and a random order of jigsaw blocks with equal selection priority. 

#### Connecting piece selection
The jigsaw block is referencing a "target pool". The "target pool" is used as an alias by the pool aliases referenced in  pool_aliases to determine which template pool to use. If no pool alias is used then the "target pool" directly references the template pool to use.

The connecting piece is determined using that template pool in following order:

1. All the pieces from the template pool — in random order according to their weight.
2. All the pieces from the fallback pool specified in the template pool — in random order according to their weight.

If the maximum depth (defined by  size) is reached, point 1 is skipped.

#### Connecting piece try
From the tried piece a random jigsaw block is selected, that

1. is facing outside of the bounds of the connecting piece
2. has a "name" that matches the "target name" of the parent jigsaw block,
3. has an orientation that is compatible with the parent jigsaw orientation (pieces can be rotated horizontally only).

The piece is placed in the world such that the jigsaw blocks connect to each other. If the currently handled piece or the newly selected piece is set to terrain matching, the piece is moved vertically to align with the terrain.

#### Piece placement condition
The placement is then checked for validity. A piece has to:

1. Not exceed the outer bounding box. If it is placed within another piece, then the bounding box of that piece is the outer bounding box[note 1], otherwise the outer bounding box is determined bymax_distance_from_center.
2. Not intersect with any other piece (except those that it is placed inside of)

If the piece can't be placed, then the placement is retried with the next piece (see #Connecting piece selection). If all pieces can't be placed than no piece is placed for this jigsaw block.

If the piece can be placed, then the newly placed piece is added to the generation queue according to the placement priority specified in the parent jigsaw block, but behind elements of equal placement priority already in the queue. The generation continues with the next jigsaw block of the parent piece.

Notes:

1. ↑When  use_expansion_hack is set to true, the bounding box of the pieces is extended to the height of the highest possible child piece.

### Step 3: Processing
Finally, each piece is processed, changing or removing blocks from the template.

The processing is done using the processor list specified for each piece in the template pool. Additionally, jigsaw blocks are replaced with the specified "Turns into" final state using the minecraft:jigsaw_replacement processor. For pieces set to terrain matching, a minecraft:gravity, processor is applied to make each column of blocks match the terrain.

## Pool aliases
Pool aliases are used to redirect the alias "target pool" referenced in jigsaw blocks to a (different) template pools. The redirections are determined before the generation starts, so in a single structure all references to a specific alias template pool are rewired to the same target template pool. Any alias that is not redirected by a pool alias is used directly as reference to a template pool.

### direct
All references to  alias are rewired to  target.

- : a pool alias
	- type:direct
	- alias:ID— alias to be redirected
	- target:template pool(referenced byID) — target for redirection

### random
A target selected from  targets per structure. All references to  alias are rewired that target.

- : a pool alias
	- type:random
	- alias:ID
	- targets: list of possible rewiring targets
		- : a rewiring target
			- weight: The chance of this target to be selected
			- data:template pool(referenced byID) — target for redirection if selected

### random_group
A alias group is selected from  groups per structure. All pool aliases in that group are used.

- : a pool alias
	- type:random_group
	- groupslist of possible rewiring groups. One group is selected per structure generation.
		- : a group
			- weight: The chance of this group to be selected
			- data: list of pool aliases to be used if the group is selected
				- : any pool alias

## Data values
### ID
Java Edition:

| Structure type | Identifier |
|----------------|------------|
| Jigsaw         | `jigsaw`   |

### Config
Java Edition:

- Structure configuration
	- type:jigsaw
	- 
	- Fields common to all structures
	- start_pool:template pool(referenced byID orinlined) — The template pool the structure starts from.
	- size: Value between 0 and 20 (inclusive) — The depth of jigsaw structures to generate.
	- start_height: Ifproject_start_to_heightmapis unset, the structure will start at the value provided. Otherwise, the value acts as an offset from theheightmap.
		- 
		- Height provider
	- project_start_to_heightmap: (optional) Theheightmapthe start height should project to. Can beWORLD_SURFACE_WG,WORLD_SURFACE,OCEAN_FLOOR_WG,OCEAN_FLOOR,MOTION_BLOCKING, orMOTION_BLOCKING_NO_LEAVES.
	- start_jigsaw_name: (optional) The name of the jigsaw block the structure start attaches to.
	- max_distance_from_center: The maximum 3D Chebyshev distance from the jigsaw pieces to the structure start. Value between 1 and 128 (inclusive) whenterrain_adaptationis "none", otherwise from 1 to 116 (inclusive).
	- use_expansion_hack: Only used in villages.
	- pool_aliases: (optional) used to rewire jigsaw pool connections by redirecting pool references on individual structure instances.
		- :pool alias



| Terrain features |                                                                                                                                                                                          |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Overworld        | Terrain   Floating island Hill Mountain Noise cave   Surface   Erosion Hoodoo Strip Surface layer   Carver   Canyon Carver cave   Water bodies   Aquifer Ocean River   Others   Ore vein |
| Terrain          | Floating island<br/>Hill<br/>Mountain<br/>Noise cave<br/>                                                                                                                                |
| Surface          | Erosion<br/>Hoodoo<br/>Strip<br/>Surface layer<br/>                                                                                                                                      |
| Carver           | Canyon<br/>Carver cave<br/>                                                                                                                                                              |
| Water bodies     | Aquifer<br/>Ocean<br/>River<br/>                                                                                                                                                         |
| Others           | Ore vein<br/>                                                                                                                                                                            |
| The Nether       | Carver cave<br/>Lava sea<br/>                                                                                                                                                            |
| The End          | Central island<br/>Obsidian platform<br/>Outer islands<br/>                                                                                                                              |
| Removed          | Beach (world feature) Gravel<br/>Gravel<br/>Clay blob<br/>Far Lands<br/>Underwater cave<br/>Underwater ravine<br/>Java Edition only   Monolith                                           |
| Java Editiononly | Monolith<br/>                                                                                                                                                                            |

| Terrain      | Floating island Hill Mountain Noise cave            |
|--------------|-----------------------------------------------------|
| Surface      | Erosion<br/>Hoodoo<br/>Strip<br/>Surface layer<br/> |
| Carver       | Canyon<br/>Carver cave<br/>                         |
| Water bodies | Aquifer<br/>Ocean<br/>River<br/>                    |
| Others       | Ore vein<br/>                                       |

| Java Edition only | Monolith |
|-------------------|----------|

| Structures       |                                                                                                                                                                                                                                                                                        |  |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| Overworld        | Ruined Portal<br/>Surface   Desert Pyramid Igloo Jungle Pyramid Pillager Outpost Swamp Hut Woodland Mansion Village Farm   Underwater   Ocean Monument Ocean Ruins Shipwreck   Underground   Ancient City Buried Treasure Mineshaft Stronghold Trail Ruins   Upcoming   Trial Chambers |  |
| Surface          | Desert Pyramid<br/>Igloo<br/>Jungle Pyramid<br/>Pillager Outpost<br/>Swamp Hut<br/>Woodland Mansion<br/>Village Farm<br/>Farm<br/>                                                                                                                                                     |  |
| Underwater       | Ocean Monument<br/>Ocean Ruins<br/>Shipwreck<br/>                                                                                                                                                                                                                                      |  |
| Underground      | Ancient City<br/>Buried Treasure<br/>Mineshaft<br/>Stronghold<br/>Trail Ruins<br/>Upcoming   Trial Chambers                                                                                                                                                                            |  |
| Upcoming         | Trial Chambers<br/>                                                                                                                                                                                                                                                                    |  |
| The Nether       | Bastion Remnant<br/>Nether Fortress<br/>Nether Fossil<br/>Ruined Portal<br/>                                                                                                                                                                                                           |  |
| The End          | End City<br/>                                                                                                                                                                                                                                                                          |  |
| Utility          | Jigsaw<br/>                                                                                                                                                                                                                                                                            |  |
| Joke             | 9x9.nbt<br/>Bonus barrel<br/>Bridge<br/>Colosseum<br/>command.com.nbt<br/>content.nbt<br/>desire.nbt<br/>house_of_bob.nbt<br/>library.nbt<br/>llama.nbt<br/>Lunar Base<br/>Potato Mineshaft<br/>Potato Village<br/>Ruined Portatol<br/>Shapes<br/>                                     |  |
| Removed          | Village (old)<br/>Java Edition only   Brick pyramid Glass Pillars Obsidian wall Starting house                                                                                                                                                                                         |  |
| Java Editiononly | Brick pyramid<br/>Glass Pillars<br/>Obsidian wall<br/>Starting house<br/>                                                                                                                                                                                                              |  |

| Surface     | Desert Pyramid Igloo Jungle Pyramid Pillager Outpost Swamp Hut Woodland Mansion Village Farm                |
|-------------|-------------------------------------------------------------------------------------------------------------|
| Underwater  | Ocean Monument<br/>Ocean Ruins<br/>Shipwreck<br/>                                                           |
| Underground | Ancient City<br/>Buried Treasure<br/>Mineshaft<br/>Stronghold<br/>Trail Ruins<br/>Upcoming   Trial Chambers |
| Upcoming    | Trial Chambers<br/>                                                                                         |

| Upcoming | Trial Chambers |
|----------|----------------|

| Java Edition only | Brick pyramid Glass Pillars Obsidian wall Starting house |
|-------------------|----------------------------------------------------------|

| Features                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Overworld                      | Lava lake<br/>Spring<br/>Surface   Bonus Chest Desert well Disk Iceberg Blue Ice Ice Patch Ice spike Freeze top layer Forest rock Pile   Underground   Amethyst geode Pointed Dripstone Dripstone cluster Large dripstone Monster room Fossil Ore Underwater magma   Vegetation   Patched vegetations Bamboo Coral reef Kelp Sea Pickle Seagrass Glow Lichen Sculk Vein Sculk patch Huge mushroom Root system Tree Oak Spruce Birch Jungle Jungle Bush Acacia Dark oak Azalea tree Mangrove Cherry Vines Cave Vines Vegetation patch   Java EditionSuperflat only   Void start platform Fill layer |
| Surface                        | Bonus Chest<br/>Desert well<br/>Disk<br/>Iceberg<br/>Blue Ice<br/>Ice Patch<br/>Ice spike<br/>Freeze top layer<br/>Forest rock<br/>Pile<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Underground                    | Amethyst geode<br/>Pointed Dripstone Dripstone cluster Large dripstone<br/>Dripstone cluster<br/>Large dripstone<br/>Monster room<br/>Fossil<br/>Ore<br/>Underwater magma<br/>                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Vegetation                     | Patched vegetations<br/>Bamboo<br/>Coral reef<br/>Kelp<br/>Sea Pickle<br/>Seagrass<br/>Glow Lichen<br/>Sculk Vein<br/>Sculk patch<br/>Huge mushroom<br/>Root system<br/>Tree Oak Spruce Birch Jungle Jungle Bush Acacia Dark oak Azalea tree Mangrove Cherry<br/>Oak<br/>Spruce<br/>Birch<br/>Jungle<br/>Jungle Bush<br/>Acacia<br/>Dark oak<br/>Azalea tree<br/>Mangrove<br/>Cherry<br/>Vines<br/>Cave Vines<br/>Vegetation patch<br/>                                                                                                                                                            |
| Java Edition<br/>Superflatonly | Void start platform<br/>Fill layer<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| The Nether                     | Basalt columns<br/>Basalt pillar<br/>Blob<br/>Delta<br/>Glowstone blob<br/>Lava spring<br/>Fire patch<br/>Vegetation   Nether forest vegetation Twisting Vines Weeping Vines Huge fungus                                                                                                                                                                                                                                                                                                                                                                                                           |
| Vegetation                     | Nether forest vegetation<br/>Twisting Vines<br/>Weeping Vines<br/>Huge fungus<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| The End                        | Chorus plant<br/>Exit portal<br/>End gateway<br/>End spike<br/>Small island<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Utility                        | no_op<br/>Random boolean selector<br/>Random selector<br/>Replace single block<br/>Simple block<br/>Simple random selector<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Joke                           | Hash Well<br/>Potato Geode<br/>Potato Tree<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Removed                        | Water lake<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

| Surface                        | Bonus Chest Desert well Disk Iceberg Blue Ice Ice Patch Ice spike Freeze top layer Forest rock Pile                                                                                                                                                                                                                                                                                                                                     |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Underground                    | Amethyst geode<br/>Pointed Dripstone Dripstone cluster Large dripstone<br/>Dripstone cluster<br/>Large dripstone<br/>Monster room<br/>Fossil<br/>Ore<br/>Underwater magma<br/>                                                                                                                                                                                                                                                          |
| Vegetation                     | Patched vegetations<br/>Bamboo<br/>Coral reef<br/>Kelp<br/>Sea Pickle<br/>Seagrass<br/>Glow Lichen<br/>Sculk Vein<br/>Sculk patch<br/>Huge mushroom<br/>Root system<br/>Tree Oak Spruce Birch Jungle Jungle Bush Acacia Dark oak Azalea tree Mangrove Cherry<br/>Oak<br/>Spruce<br/>Birch<br/>Jungle<br/>Jungle Bush<br/>Acacia<br/>Dark oak<br/>Azalea tree<br/>Mangrove<br/>Cherry<br/>Vines<br/>Cave Vines<br/>Vegetation patch<br/> |
| Java Edition<br/>Superflatonly | Void start platform<br/>Fill layer<br/>                                                                                                                                                                                                                                                                                                                                                                                                 |

| Vegetation | Nether forest vegetation Twisting Vines Weeping Vines Huge fungus |
|------------|-------------------------------------------------------------------|

