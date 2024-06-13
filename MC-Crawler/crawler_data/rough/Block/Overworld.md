# Overworld
The Overworld is the dimension in which all players begin their Minecraft world. It is the dimension with the most biomes, blocks, and mobs, and is where most players spend the majority of their time.

## Contents
- 1 Creation
	- 1.1 Seeds
- 2 Environment
	- 2.1 Biomes
	- 2.2 Natural structures
	- 2.3 Daylight cycle
	- 2.4 Mobs
		- 2.4.1 Passive mobs
		- 2.4.2 Neutral mobs
		- 2.4.3 Hostile mobs
- 3 Generation
	- 3.1 Limitations
	- 3.2 Terrain features
	- 3.3 Blocks
		- 3.3.1 Naturally generated
		- 3.3.2 Naturally created
		- 3.3.3 Structures
- 4 Technical information
	- 4.1 ID
	- 4.2 Folder
- 5 Achievements
- 6 Advancements
- 7 History
- 8 Issues
- 9 Gallery
	- 9.1 Screenshots
	- 9.2 In other media
- 10 Trivia
- 11 See also
- 12 References

## Creation
Main article: World generation
The Overworld is the only dimension created when the player creates a new world. The other dimensions (The Nether and The End) aren't created until a player enters the corresponding dimension for the first time.

### Seeds
Main article: Seed (world generation)
A new world in Minecraft is generated through the use of a randomly generated seed, which is an integer used as a starting point for the world generation formula. The player can specify a seed or allow the game to generate one randomly. If given a non-integer input (such as the word "Glacier"), the game converts it into a corresponding integer (such as 1772835215). 

A given seed generates almost exactly the same world every time, provided the same edition, game version, and world type are used. Although the exact spawn point varies, the coordinates of all terrain features are the same. All seeds within the 32-bit integer limit in Java and Bedrock editions may also generate worlds with the same terrain shape and biome map, but the placement of terrain features, structures, and carver caves may differ.

## Environment
The Overworld is an incredibly complex environment with a wide variety of features.

### Biomes
A river biome running through a badlands biome. A ruined portal can also be seen in the distance.
Main article: Biome
The Overworld is divided into biomes of various types. A biome's type determines the basic characteristics of the terrain within it, such as the blocks composing the surface or the plants that thrive in it. The biome type also determines which mobs can spawn within it and affects how environmental behaviors such as weather are expressed within it.

### Natural structures
A village, one of many naturally generated structures in the Overworld.
Main article: Generated structures
The Overworld is composed of a large number of terrain patterns, called generated structures, whose arrangement varies widely from one seed to another. The exact structures are unique to each world, while the types of structures that can be generated at a given place are determined by the biome type. Structures are meant to represent real-world equivalents such as mountains, caves, and lakes. "Impossible" (in the real world) formations, such as floating islands, can also be found throughout the Overworld.

Along with terrain features, natural structures include naturally-generated buildings, such as villages, dungeons, mineshafts, and ruined portals.

### Daylight cycle
A view of the day-night cycle.
Main article: Daylight cycle
The Overworld is the only dimension with a daylight cycle and the only one where the environment reflects the passage of time. In contrast to time zones in the real world, Overworld time is universal; it is always the same time for every player in the dimension regardless of how far apart they might be, even in an "infinite" world.

During the daytime, the sun acts as a powerful light source, with a light level of 15, the maximum. Sunlight is strong enough to grow plants and affect the way mobs spawn, among other interesting effects. During the nighttime, the moon is the only natural light source. However, moonlight is comparatively dim; the light level falls to a minimum of 4, allowing hostile mobs to spawn. Other than during thunderstorms, nighttime is the only time players may sleep in a bed.

The daylight cycle can effectively be measured using a clock, which allows players to determine the approximate Minecraft time anywhere in the Overworld. Time can also be changed or stopped with the use of the /time command.

The sun rises in the east and sets in the west, just as it does in the real world. Observing its motion is a simple method of telling direction without a compass.

### Mobs
Main article: Mob
The Overworld is home to a wide variety of mobs. Mobs vary greatly in behavior and the level of danger they present to the player. Different mobs spawn at different times and places depending on the light level and the biome, among other factors. On occasion, a mob can move between the Overworld and another dimension, such as The Nether, by using a portal, but this is uncommon. Boss mobs like the ender dragon and the wither cannot enter portals.

#### Passive mobs
- Allay
- Armadillo‌[upcoming]
- Axolotl
- Bat
- Camel
- Cat
- Chicken
- Cod
- Cow
- Donkey
- Frog
- Glow Squid
- Horse
- Mooshroom
- Ocelot
- Parrot
- Pig
- Pufferfish
- Rabbit
- Salmon
- Sheep
- Skeleton Horse
- Snow Golem
- Squid
- Tropical Fish
- Turtle
- Villager
- Wandering Trader

#### Neutral mobs
- Bee
- Cave Spider
- Dolphin
- Drowned
- Enderman
- Fox
- Goat
- Iron Golem
- Llama
- Panda
- Polar Bear
- Spider
- Trader Llama
- Wolf
- Zombified Piglin

#### Hostile mobs
- Bogged‌[upcoming]
- Breeze‌[upcoming]
- Creeper
- Elder Guardian
- Evoker
- Guardian
- Husk
- Phantom
- Pillager
- Ravager
- Silverfish
- Skeleton
- Slime
- Stray
- Vex
- Vindicator
- Warden
- Witch
- Zombie
- Zombie Villager

## Generation
As with all other dimensions in the game, the Overworld can generate infinitely. However, there are some limitations, as detailed below. Like the other dimensions, it is divided into 16×384×16 block sections called chunks.

The Overworld encompasses a three-dimensional volume that extends vertically from the Void up to the build limit (y=-64 to 320), and horizontally for a virtually infinite distance in each direction. This volume is filled (virtually speaking) with air, terrain, and structures. Technically, the terrain is formed by generating multiple noise maps to produce differing elevations, general land shapes, and complex mountain and cave systems.

### Limitations
Visual cutoff point of an old Minecraft map (Left is normal Minecraft generation, the right is after limitation.)
Main article: World boundary
While the world is virtually infinite, the number of blocks a player may physically reach is limited with where the limits are depending on the edition of the game and the world type being played.

In Java Edition, the map contains a world border located by default at X/Z coordinates ±29,999,984. The world border is an animated wall of blue stripes. Standing near the border results in a red vignette appearing around the screen. Most entities are unable to pass the border, except by teleporting. Players who breach the border receive constant damage unless they are in creative or spectator mode. The player can teleport past the world border and continue as far as X/Z ±29,999,999, where there is an invisible wall. However, the player can travel a few chunks further by riding horses, pigs, and minecarts through it.[verify]

In Bedrock Edition, Infinite-type worlds have no fixed horizontal limits, but either generation stops or normal game behavior begins to break down at extreme distances; the exact details depend on the platform. However, experiments suggest that players can generally reach at least X/Z ±30,000,000 before such problems occur.


### Terrain features
Main article: Terrain features
The Overworld contains numerous terrain features, at a wide variety of scales.

### Blocks
#### Naturally generated
"Naturally generated" includes blocks that are created through the world seed.

- Air
- Cave Air‌[JE  only]
- Void Air‌[JE  only]
- Bedrock
- Stone
- Deepslate
- Granite
- Diorite
- Andesite
- Tuff
- Calcite
- Dripstone Block
- Pointed Dripstone
- Smooth Basalt
- Coal Ore
- Deepslate Coal Ore
- Iron Ore
- Deepslate Iron Ore
- Copper Ore
- Deepslate Copper Ore
- Gold Ore
- Deepslate Gold Ore
- Redstone Ore
- Deepslate Redstone Ore
- Emerald Ore
- Deepslate Emerald Ore
- Lapis Lazuli Ore
- Deepslate Lapis Lazuli Ore
- Diamond Ore
- Deepslate Diamond Ore
- Block of Raw Iron
- Block of Raw Copper
- Block of Amethyst
- Budding Amethyst
- Small Amethyst Bud
- Medium Amethyst Bud
- Large Amethyst Bud
- Amethyst Cluster
- Grass Block
- Mycelium
- Podzol
- Dirt
- Coarse Dirt
- Rooted Dirt
- Moss Block
- Moss Carpet
- Clay
- Mud
- Water
- Lava
- Sand
- Red Sand
- Gravel
- Sandstone
- Red Sandstone
- Snow
- Snow Block
- Powder Snow
- Ice
- Packed Ice
- Blue Ice
- Oak Log
- Spruce Log
- Birch Log
- Jungle Log
- Acacia Log
- Dark Oak Log
- Mangrove Log
- Cherry Log
- Oak Leaves
- Spruce Leaves
- Birch Leaves
- Jungle Leaves
- Acacia Leaves
- Dark Oak Leaves
- Azalea Leaves
- Flowering Azalea Leaves
- Mangrove Leaves
- Mangrove Propagule
- Mangrove Roots
- Muddy Mangrove Roots
- Cherry Leaves
- Short Grass
- Tall Grass
- Fern
- Large Fern
- Dead Bush
- Dandelion
- Poppy
- Blue Orchid
- Allium
- Azure Bluet
- Red Tulip
- Orange Tulip
- White Tulip
- Pink Tulip
- Oxeye Daisy
- Cornflower
- Lily of the Valley
- Pink Petals
- Sunflower
- Lilac
- Rose Bush
- Peony
- Brown Mushroom
- Red Mushroom
- Brown Mushroom Block
- Red Mushroom Block
- Mushroom Stem
- Cactus
- Sugar Cane
- Pumpkin
- Melon
- Vines
- Lily Pad
- Cocoa
- Bamboo
- Sweet Berry Bush
- Infested Stone
- Infested Deepslate
- Terracotta
- Red Terracotta
- Orange Terracotta
- Yellow Terracotta
- Brown Terracotta
- White Terracotta
- Light Gray Terracotta
- Magma Block
- Kelp
- Kelp Plant
- Seagrass
- Tall Seagrass
- Sea Pickle
- Bubble Column
- Tube Coral
- Tube Coral Fan
- Tube Coral Block
- Dead Tube Coral‌[BE  only][needs testing]
- Dead Tube Coral Fan‌[BE  only]
- Dead Tube Coral Block‌[BE  only]
- Brain Coral
- Brain Coral Fan
- Brain Coral Block
- Dead Brain Coral‌[BE  only][needs testing]
- Dead Brain Coral Fan‌[BE  only]
- Dead Brain Coral Block‌[BE  only]
- Bubble Coral
- Bubble Coral Fan
- Bubble Coral Block
- Dead Bubble Coral‌[BE  only][needs testing]
- Dead Bubble Coral Fan‌[BE  only]
- Dead Bubble Coral Block‌[BE  only]
- Fire Coral
- Fire Coral Fan
- Fire Coral Block
- Dead Fire Coral‌[BE  only][needs testing]
- Dead Fire Coral Fan‌[BE  only]
- Dead Fire Coral Block‌[BE  only]
- Horn Coral
- Horn Coral Fan
- Horn Coral Block
- Dead Horn Coral‌[BE  only][needs testing]
- Dead Horn Coral Fan‌[BE  only]
- Dead Horn Coral Block‌[BE  only]
- Bee Nest
- Glow Lichen
- Cave Vines
- Cave Vines Plant
- Azalea
- Flowering Azalea
- Small Dripleaf
- Big Dripleaf
- Big Dripleaf Stem
- Hanging Roots
- Sculk
- Sculk Sensor
- Sculk Catalyst
- Sculk Shrieker
- Sculk Vein
- Bone Block
- Cobblestone
- Mossy Cobblestone
- Monster Spawner
- Chest
- Suspicious Sand
- Sandstone Slab

#### Naturally created
Naturally created means a combination of events that cause a new block to be placed by natural causes, not the player. Some of these blocks may also be created as part of world generation.

- Air
- Small Amethyst Bud
- Medium Amethyst Bud
- Large Amethyst Bud
- Amethyst Cluster
- Grass Block
- Dirt
- Mycelium
- Water
- Red Mushroom
- Brown Mushroom
- Kelp
- Kelp Plant
- Cave Vines
- Cave Vines Plant
- Pointed Dripstone
- Cobblestone
- Stone
- Obsidian
- Fire
- Snow
- Ice
- Cactus
- Sugar Cane
- Vines

#### Structures
These blocks are created only with the "Generate Structures" option enabled.

- Polished Granite
- Polished Diorite
- Polished Andesite
- Netherrack
- Soul Sand
- Soul Fire
- Oak Wood
- Spruce Wood
- Acacia Wood
- Stripped Oak Log
- Stripped Spruce Log
- Stripped Jungle Log‌[BE  only][needs testing]
- Stripped Acacia Log
- Stripped Dark Oak Log‌[BE  only][needs testing]
- Stripped Oak Wood
- Stripped Spruce Wood
- Oak Planks
- Spruce Planks
- Birch Planks
- Jungle Planks
- Acacia Planks
- Dark Oak Planks
- Acacia Sapling
- Dark Oak Sapling
- Chiseled Sandstone
- Cut Sandstone
- Smooth Stone
- Smooth Sandstone
- White Wool
- Red Wool
- Orange Wool
- Light Blue Wool
- Yellow Wool
- Lime Wool
- Gray Wool
- Light Gray Wool
- Cyan Wool
- Blue Wool
- Brown Wool
- Green Wool
- Black Wool
- White Carpet
- Orange Carpet
- Magenta Carpet
- Gray Carpet
- Light Blue Carpet
- Yellow Carpet
- Lime Carpet
- Pink Carpet
- Light Gray Carpet
- Cyan Carpet
- Purple Carpet
- Blue Carpet
- Brown Carpet
- Green Carpet
- Red Carpet
- Black Carpet
- Bricks
- Torch
- Lantern
- Soul Lantern
- Candle
- White Candle
- Brown Candle
- Green Candle
- Purple Candle
- Red Candle
- Block of Coal
- Block of Lapis Lazuli
- Block of Gold
- Block of Diamond
- Crying Obsidian
- Trapped Chest
- Furnace
- Crafting Table
- Farmland
- Ladder
- Bookshelf
- Cobweb
- Melon Stem
- Carved Pumpkin
- Jack o'Lantern
- Pumpkin Stem
- Rail
- Lever
- Stone Button
- Jungle Button
- Stone Pressure Plate
- Oak Pressure Plate
- Spruce Pressure Plate
- Acacia Pressure Plate
- Oak Fence
- Spruce Fence
- Jungle Fence
- Acacia Fence
- Dark Oak Fence
- Oak Fence Gate
- Spruce Fence Gate
- Jungle Fence Gate
- Acacia Fence Gate
- Dark Oak Fence Gate
- Oak Trapdoor
- Spruce Trapdoor
- Jungle Trapdoor
- Acacia Trapdoor‌[BE  only][needs testing]
- Dark Oak Trapdoor
- Iron Trapdoor
- Brick Wall
- Cobblestone Wall
- Diorite Wall
- Granite Wall
- Sandstone Wall
- Cobbled Deepslate Wall
- Polished Deepslate Wall
- Deepslate Brick Wall
- Deepslate Tile Wall
- Iron Bars
- Glass
- Glass Pane
- Brown Stained Glass Pane
- White Stained Glass Pane
- Orange Stained Glass Pane
- Yellow Stained Glass Pane
- Stone Bricks
- Cracked Stone Bricks
- Mossy Stone Bricks
- Chiseled Stone Bricks
- Infested Stone Bricks
- Infested Mossy Stone Bricks
- Infested Chiseled Stone Bricks
- Infested Cobblestone
- Cauldron
- Brewing Stand
- End Portal Frame
- End Portal
- Potted Dandelion
- Potted Poppy
- Potted Blue Orchid
- Potted Allium
- Potted Azure Bluet
- Potted Red Tulip
- Potted White Tulip
- Potted Oxeye Daisy
- Potted Dead Bush
- Potted Spruce Sapling
- Potted Birch Sapling
- Potted Red Mushroom
- Potted Cactus
- Anvil
- Damaged Anvil
- Hay Bale
- Light Blue Terracotta
- Lime Terracotta
- Gray Terracotta
- Cyan Terracotta
- Blue Terracotta
- Green Terracotta
- Black Terracotta
- Prismarine
- Prismarine Bricks
- Dark Prismarine
- Sea Lantern
- Wet Sponge
- Dirt Path
- Ominous Wall Banner
- Gray Wall Banner
- Light Gray Wall Banner
- Brown Wall Banner
- Black Wall Banner
- White Glazed Terracotta
- Orange Glazed Terracotta
- Light Blue Glazed Terracotta
- Yellow Glazed Terracotta
- Lime Glazed Terracotta
- Gray Glazed Terracotta
- Light Gray Glazed Terracotta
- Cyan Glazed Terracotta
- Purple Glazed Terracotta
- Blue Glazed Terracotta
- Brown Glazed Terracotta
- Red Glazed Terracotta
- Black Glazed Terracotta
- Iron Door
- Oak Door
- Spruce Door
- Jungle Door
- Acacia Door
- Dark Oak Door
- Oak Wall Sign
- Spruce Wall Sign
- Oak Stairs
- Birch Stairs
- Spruce Stairs
- Jungle Stairs
- Acacia Stairs
- Dark Oak Stairs
- Diorite Stairs
- Granite Stairs
- Sandstone Stairs
- Smooth Sandstone Stairs
- Cobblestone Stairs
- Mossy Cobblestone Stairs
- Stone Brick Stairs
- Mossy Stone Brick Stairs
- Cobbled Deepslate Stairs
- Polished Deepslate Stairs
- Deepslate Brick Stairs
- Deepslate Tile Stairs
- Brick Stairs
- Mud Brick Stairs
- Oak Slab
- Spruce Slab
- Jungle Slab
- Acacia Slab
- Dark Oak Slab
- Stone Slab
- Smooth Sandstone Slab
- Cobblestone Slab
- Mossy Cobblestone Slab
- Smooth Stone Slab
- Stone Brick Slab
- Mossy Stone Brick Slab
- Cobbled Deepslate Slab
- Polished Deepslate Slab
- Deepslate Brick Slab
- Deepslate Tile Slab
- Brick Slab
- Mud Brick Slab
- Tripwire Hook
- Tripwire
- Redstone Dust
- Redstone Repeater
- Redstone Comparator
- Redstone Torch
- Block of Redstone
- Sticky Piston
- Dispenser
- TNT
- Target
- Note Block
- Redstone Lamp
- Wheat
- Carrots
- Potatoes
- Beetroots
- White Bed
- Orange Bed
- Yellow Bed
- Cyan Bed
- Purple Bed
- Blue Bed
- Green Bed
- Red Bed
- Bell
- Loom
- Campfire
- Barrel
- Lectern
- Blast Furnace
- Smoker
- Cartography Table
- Composter
- Stonecutter
- Grindstone
- Smithing Table
- Fletching Table
- Skeleton Skull
- Cobbled Deepslate
- Reinforced Deepslate
- Chiseled Deepslate
- Deepslate Bricks
- Cracked Deepslate Bricks
- Deepslate Tiles
- Cracked Deepslate Tiles
- Polished Deepslate
- Polished Basalt
- Mud Bricks
- Cyan Concrete
- Red Concrete
- Packed Mud
- Suspicious Gravel

## Technical information
### ID
| Name      | Identifier  | Numeric ID |
|-----------|-------------|------------|
| Overworld | `overworld` | `0`        |

### Folder
In Java Edition, information on the Overworld is stored in the region folder of the .minecraft/saves/worldname directory, with "worldname" being the name of the player's world.

Deleting the region folder resets the Overworld so that all player-made changes and buildings in that dimension are undone.

