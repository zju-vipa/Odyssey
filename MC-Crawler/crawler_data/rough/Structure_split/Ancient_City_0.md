# Ancient City
An ancient city is a palatial structure found in deep dark biomes at layer -51, harboring chests containing some items that cannot be found anywhere else.

## Contents
- 1 Structure
	- 1.1 Environment aesthetics
		- 1.1.1 Overall view
		- 1.1.2 Redstone circuits
	- 1.2 File structure
	- 1.3 Components
		- 1.3.1 Entrance
		- 1.3.2 Center
		- 1.3.3 Ruins
		- 1.3.4 Walls
	- 1.4 Blocks
- 2 Loot
	- 2.1 Normal
	- 2.2 Ice boxes
- 3 Data values
	- 3.1 ID
- 4 History
- 5 Issues
- 6 Trivia
- 7 Gallery
	- 7.1 Screenshots
	- 7.2 Development images
	- 7.3 Concept artwork
	- 7.4 In other media
- 8 See also
- 9 References

## Structure
### Environment aesthetics
An ancient city features a very large palace with a footprint of around 220 blocks on each horizontal axis, stretching throughout a deep dark biome. The floor of the city always generates at the Y level of -51. The palace is made up of long corridors with 2-block-deep layers of gray wool on the floor, and some rugs made of blue, light blue and cyan wool or carpet floors to prevent vibrations, as well as some smaller ruins off to the side of the main corridors, which contain either one or two loot chests. The city has statues and the center features a frame resembling a warden's head, where there are reinforced deepslate blocks, which is an unobtainable material in Survival mode. Other unique blocks such as soul lanterns and candles as well as different forms of deepslate and sculk can be found here. Sculk shriekers generate much more frequently in ancient cities than in the normal deep dark biome. The city generates always at the same places in chunks (for example, the blocks that make up the center structure made of reinforced deepslate in the middle are always on the western edge of a chunk).

Some structures resemble elements of the game. The city center bears a resemblance to early iterations of the warden's design, and other structures resemble pillager outposts and woodland mansion rooms.

#### Overall view
The following three renders are the same instance of ancient city.

- The view from the direction of the entrance.
- Another direction.
- The vertical view. The entrance is in the lower part of this picture.

#### Redstone circuits
Underneath the frame at the city center lies a series of hidden basements with naturally generating redstone circuitry.

The secret entrance is located at the base of the structure, underneath the wooden bridge between the city center and the wall. There's a piston door that is controlled by a sculk sensor in the redstone circuits in the basement.

- Basement of city_center_1.
- Basement of city_center_2.
- Basement of city_center_3.
- Piston door circuit in the basement of city_center_3.
- Furnace in the basement of city_center_2.

For city_center_1, there is a chiseled deepslate block in front of the frame. Making a vibration around it can activate the sculk sensor and then open the piston door. There's also a pulse extender between the sculk sensor and piston door, which makes the piston door close 180 game ticks after the sculk sensor is deactivated.

The circuit in city_center_2 is similar to the former, but with a signal strength filter. Only vibrations with a frequency equal to 8 (mob interactions, projectile hits, eating, entity damage) can activate the piston door. Creating these vibrations on the path in the front of the frame in the city center activates the door.

For city_center_3, making a vibration on the path in front of the frame on the city center can activate the sculk sensor. Additionally, there's a T flip-flop between the sculk sensor and piston door. After the sculk sensor is activated, the piston door remains open until the sculk sensor is activated again.

There are three basic redstone circuits in the basement:

- Circuit of the target block.
- Circuit of lectern block.
- Circuit to show that some blocks can transfer a signal with a repeater while some cannot.

### File structure
All ancient city structures found below are located in the folder client.jar/data/minecraft/structures/ancient_city‌[JE  only], data/structures/ancient_city‌[BE  only].

| List                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ancient_city city entrance entrance_connector.nbt entrance_path_1.nbt entrance_path_2.nbt entrance_path_3.nbt entrance_path_4.nbt entrance_path_5.nbt city_center city_center_1.nbt city_center_2.nbt city_center_3.nbt walls bottom_1.nbt bottom_2.nbt bottom_left_corner.nbt bottom_right_corner.nbt bottom_right_corner_1.nbt bottom_right_corner_2.nbt left.nbt right.nbt top_left_corner.nbt top_right_corner.nbt top.nbt structures barracks.nbt camp_1.nbt camp_2.nbt camp_3.nbt chamber_1.nbt chamber_2.nbt chamber_3.nbt ice_box_1.nbt large_pillar_1.nbt large_ruin_1.nbt medium_pillar_1.nbt medium_ruin_1.nbt medium_ruin_2.nbt sauna_1.nbt small_ruin_1.nbt small_ruin_2.nbt small_statue.nbt tall_ruin_1.nbt tall_ruin_2.nbt tall_ruin_3.nbt tall_ruin_4.nbt walls intact_corner_wall_1.nbt intact_horizontal_wall_1.nbt intact_horizontal_wall_2.nbt intact_horizontal_wall_bridge.nbt intact_horizontal_wall_passage_1.nbt intact_horizontal_wall_stairs_1.nbt intact_horizontal_wall_stairs_2.nbt intact_horizontal_wall_stairs_3.nbt intact_horizontal_wall_stairs_4.nbt intact_intersection_wall_1.nbt intact_lshape_wall_1.nbt ruined_corner_wall_1.nbt ruined_corner_wall_2.nbt ruined_horizontal_wall_stairs_1.nbt ruined_horizontal_wall_stairs_2.nbt ruined_horizontal_wall_stairs_3.nbt ruined_horizontal_wall_stairs_4.nbt |

### Components
#### Entrance
| Structure name                                  | Description | Consists of                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Image |
|-------------------------------------------------|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|
| `ancient_city/city/entrance/entrance_connector` |             | 3 Candle (1 candle in one block) 6 Candle (2 candles in one block) 6 Candle (3 candles in one block) 5 Candle (4 candles in one block) 72 Chiseled Deepslate 928 Deepslate 21 Deepslate Brick Slab 9 Deepslate Brick Stairs 96 Deepslate Bricks 299 Deepslate Tile Stairs 595 Deepslate Tiles 138 Polished Basalt 416 Polished Deepslate 12 Polished Deepslate Wall 40 Smooth Basalt 6 Soul Lantern                                                                                                                                                               |       |
| `ancient_city/city/entrance/entrance_path_1`    |             | 12 Candle (1 candle in one block) 5 Candle (2 candles in one block) 5 Candle (3 candles in one block) 2 Candle (4 candles in one block) 78 Chiseled Deepslate 3 Cobbled Deepslate Slab 899 Deepslate 25 Deepslate Brick Slab 6 Deepslate Brick Stairs 41 Deepslate Bricks 305 Deepslate Tile Stairs 731 Deepslate Tiles 138 Polished Basalt 437 Polished Deepslate 3 Polished Deepslate Slab 14 Polished Deepslate Wall 48 Smooth Basalt 7 Soul Lantern                                                                                                           |       |
| `ancient_city/city/entrance/entrance_path_2`    |             | 10 Candle (1 candle in one block) 4 Candle (2 candles in one block) 4 Candle (3 candles in one block) 2 Candle (4 candles in one block) 59 Chiseled Deepslate 21 Dark Oak Planks 810 Deepslate 22 Deepslate Brick Slab 6 Deepslate Brick Stairs 39 Deepslate Bricks 9 Deepslate Tile Slab 254 Deepslate Tile Stairs 2,357 Deepslate Tiles 12 Ladder 113 Polished Basalt 348 Polished Deepslate 15 Polished Deepslate Wall 39 Smooth Basalt 7 Soul Lantern                                                                                                         |       |
| `ancient_city/city/entrance/entrance_path_3`    |             | 8 Candle (1 candle in one block) 3 Candle (2 candles in one block) 3 Candle (3 candles in one block) 2 Candle (4 candles in one block) 36 Chiseled Deepslate 4 Cobbled Deepslate 12 Cobbled Deepslate Wall 21 Dark Oak Fence 26 Dark Oak Log 93 Dark Oak Planks 566 Deepslate 20 Deepslate Brick Slab 4 Deepslate Brick Stairs 50 Deepslate Bricks 4 Deepslate Tile Slab 153 Deepslate Tile Stairs 2,163 Deepslate Tiles 18 Ladder 90 Polished Basalt 210 Polished Deepslate 8 Polished Deepslate Wall 31 Smooth Basalt 4 Soul Lantern 4 Torch                    |       |
| `ancient_city/city/entrance/entrance_path_4`    |             | 8 Candle (1 candle in one block) 3 Candle (2 candles in one block) 3 Candle (3 candles in one block) 2 Candle (4 candles in one block) 28 Chiseled Deepslate 2 Cobbled Deepslate 9 Cobbled Deepslate Wall 13 Dark Oak Fence 20 Dark Oak Log 81 Dark Oak Planks 548 Deepslate 20 Deepslate Brick Slab 4 Deepslate Brick Stairs 56 Deepslate Bricks 3 Deepslate Tile Slab 139 Deepslate Tile Stairs 2,137 Deepslate Tiles 18 Ladder 4 Light Blue Carpet 91 Polished Basalt 184 Polished Deepslate 4 Polished Deepslate Wall 28 Smooth Basalt 2 Soul Lantern 1 Torch |       |
| `ancient_city/city/entrance/entrance_path_5`    |             | 5 Candle (1 candle in one block) 3 Candle (2 candles in one block) 1 Candle (3 candles in one block) 2 Candle (4 candles in one block) 13 Chiseled Deepslate 3 Dark Oak Log 18 Dark Oak Planks 373 Deepslate 13 Deepslate Brick Slab 2 Deepslate Brick Stairs 39 Deepslate Bricks 2 Deepslate Tile Slab 76 Deepslate Tile Stairs 1,924 Deepslate Tiles 12 Ladder 3 Light Blue Carpet 72 Polished Basalt 93 Polished Deepslate 19 Smooth Basalt                                                                                                                    |       |

