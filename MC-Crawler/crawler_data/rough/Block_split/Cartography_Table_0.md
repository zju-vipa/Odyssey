# Cartography Table
A cartography table is a utility block used for cloning, zooming out and locking maps. It also serves as a cartographer's job site block.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
- 2 Usage
	- 2.1 Placement
	- 2.2 Zooming out, cloning, locking maps
	- 2.3 Changing profession
	- 2.4 Fuel
	- 2.5 Note blocks
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
- 5 History
- 6 Issues
- 7 Gallery
	- 7.1 Screenshots
- 8 External links

## Obtaining
### Breaking
A cartography table can be obtained using any tool or by hand, although an axe is fastest.

| Block     | Cartography Table     |
|-----------|-----------------------|
| Hardness  | 2.5                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 3.75                  |
| Wooden    | 1.9                   |
| Stone     | 0.95                  |
| Iron      | 0.65                  |
| Diamond   | 0.5                   |
| Netherite | 0.45                  |
| Golden    | 0.35                  |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
Cartography tables can generate naturally inside cartographer houses in villages. They can also generate in trail ruins.

### Crafting
| Ingredients          | Crafting recipe |
|----------------------|-----------------|
| Paper+<br/>AnyPlanks |                 |

## Usage
### Placement
Regardless of the player's position during placement, the different textures of the block are always facing the same direction (the texture with the globe in the right corner always faces west, while the one with the compass and map faces up).

### 
The GUI of cartography table in Java Edition.
The GUI of cartography table in Bedrock Edition.
Cartography tables are used for zooming out, cloning, and locking maps (making them unable to be altered). They can also be used for adding pointers to maps, creating empty maps, and renaming maps.‌[Bedrock Edition  only]

Below is a list of brief descriptions of all available functions of the cartography table:

For more detailed information of each of these function, see Map § Usage.

| First slot | Second slot | Result                                    |
|------------|-------------|-------------------------------------------|
| Map        | Paper       | Zoomed out map (1 zoom level higher)      |
| Map        | Empty map   | Two identical maps                        |
| Map        | Glass Pane  | Locked map                                |
| Map        | Compass     | Locator map‌[Bedrock Edition  only]       |
| Empty map  | Compass     | Empty Locator map‌[Bedrock Edition  only] |
| Paper      |             | Empty map‌[Bedrock Edition  only]         |
| Paper      | Compass     | Empty Locator map‌[Bedrock Edition  only] |

Zooming out a map always starts with an existing map, not a blank map. Zooming it out makes the map aligned to the grid that would include the area of the original map. To build a set of maps such as for a map wall, a player cannot create several level 0 (base) maps at one location then zoom them out before going out into the world to fill them in; the player must start with a base map created in each area to be covered by the zoomed out map. See more discussion of map alignment at Map.

### Changing profession
If a village has a cartography table that has not been claimed by a villager, any nearby villager who hasn't chosen a job site block has a chance to change their profession to a cartographer.

### Fuel
A cartography table can be used as a fuel in furnaces, smelting 1.5 items per block.

### Note blocks
Cartography tables can be placed under note blocks to produce "bass" sounds.

## Data values
### ID
Java Edition:

| Name              | Identifier          | Form         | Translation key                     |
|-------------------|---------------------|--------------|-------------------------------------|
| Cartography Table | `cartography_table` | Block & Item | `block.minecraft.cartography_table` |

Bedrock Edition:

| Name              | Identifier          | Numeric ID | Form                       | Item ID[i 1]   | Translation key               |
|-------------------|---------------------|------------|----------------------------|----------------|-------------------------------|
| Cartography Table | `cartography_table` | `455`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.cartography_table.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.


