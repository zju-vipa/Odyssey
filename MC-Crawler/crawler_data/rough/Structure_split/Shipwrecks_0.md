# Shipwreck
A shipwreck is a structure found in oceanic biomes that resembles a sunken sailing ship.

## Contents
- 1 Generation
- 2 Structure
- 3 Loot
	- 3.1 Supply chests
	- 3.2 Treasure chests
	- 3.3 Map chests
- 4 Data values
	- 4.1 ID
	- 4.2 Config
- 5 Achievements
- 6 History
- 7 Issues
- 8 Gallery
	- 8.1 Screenshots
- 9 References

## Generation
Shipwrecks generate in all ocean biomes rarely. On rarer occasions, they generate above sea level nearby the water, in beaches, snowy beaches or inside an iceberg,[1] underwater ruin, monument or ravine.

## Structure
Main article: Shipwreck/Structure
Shipwrecks generate in one of three ways: upright, keeled sideways or upside-down. In many cases, they are missing their bow (front) or stern (rear), mast or multiple other blocks, giving them a damaged appearance; however, it is also possible, but rare, to find them completely intact. They consist solely of wooden materials, including logs‌[JE  only]/stripped logs‌[BE  only], planks, fences, slabs, stairs, trapdoors, a door (if the ship is upright), and up to 3 chests, depending on rotation and intact sections of the ship. The bow is supposed to generate one chest (unless upside-down) while the stern should generate two, and the whole ship generates a maximum of three chests, regardless of the ship's rotation or condition. However, there are some instances in which chests that usually generate in a shipwreck section are missing. Only two wood types are used per ship (one is the primary type, which is used by the logs and exterior, and the other the secondary type), but only 8‌[JE  only] combinations are possible: Primary dark oak with secondary jungle and spruce, primary jungle with secondary spruce, primary oak with secondary birch and spruce, primary spruce with secondary dark oak, jungle, and oak. Acacia is a possible secondary type on bedrock edition.

| Structure name                             | Description                                                                                                 | Consists of                                                                                                                                                          | Images |
|--------------------------------------------|-------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| `shipwreck/rightsideup_backhalf`           | The stern of a ship, upright, intact.                                                                       | 166 Oak Planks 112 Oak Stairs 67 Spruce Planks 20 Spruce Slab 15 Spruce Fence 13 Spruce Stairs 6 Oak Fence 4 Oak Log 3 Oak Trapdoor 2 Oak Slab 2 Chest 1 Oak Door    |        |
| `shipwreck/rightsideup_backhalf_degraded`  | The stern of a ship, upright, with a degraded appearance.                                                   | 153 Oak Planks 109 Oak Stairs 59 Spruce Planks 20 Spruce Slab 14 Spruce Fence 10 Spruce Stairs 6 Oak Fence 4 Oak Log 4 Oak Slab 2 Oak Trapdoor 2 Chest 1 Oak Door    |        |
| `shipwreck/rightsideup_fronthalf`          | The bow of a ship, upright, intact.                                                                         | 128 Oak Planks 108 Oak Stairs 58 Spruce Planks 20 Spruce Stairs 18 Spruce Fence 11 Oak Trapdoor 8 Oak Log 1 Chest 1 Oak Door                                         |        |
| `shipwreck/rightsideup_fronthalf_degraded` | The bow of a ship, upright, with a degraded appearance.                                                     | 111 Oak Planks 100 Oak Stairs 44 Spruce Planks 12 Spruce Stairs 10 Spruce Fence 11 Oak Trapdoor 7 Oak Log 1 Chest 1 Oak Door                                         |        |
| `shipwreck/rightsideup_full`               | A whole ship, upright, intact.                                                                              | 252 Oak Planks 178 Oak Stairs 104 Spruce Planks 31 Spruce Fence 31 Spruce Slab 26 Spruce Stairs 14 Oak Trapdoor 10 Oak Log 6 Oak Fence 3 Chest 2 Oak Slab 1 Oak Door |        |
| `shipwreck/rightsideup_full_degraded`      | A whole ship, upright, with a degraded appearance.                                                          | 243 Oak Planks 171 Oak Stairs 89 Spruce Planks 31 Spruce Slab 27 Spruce Fence 23 Spruce Stairs 10 Oak Log 9 Oak Trapdoor 6 Oak Fence 3 Chest 2 Oak Slab 1 Oak Door   |        |
| `shipwreck/sideways_backhalf`              | The stern of a ship, capsized, intact.                                                                      | 143 Oak Planks 105 Oak Stairs 101 Spruce Planks 10 Spruce Fence 6 Oak Fence 5 Spruce Stairs 4 Oak Log 3 Oak Trapdoor 2 Chest                                         |        |
| `shipwreck/sideways_backhalf_degraded`     | The stern of a ship, capsized, with a degraded appearance.                                                  | 123 Oak Planks 99 Oak Stairs 88 Spruce Planks 10 Spruce Fence 6 Oak Fence 4 Oak Log 3 Oak Trapdoor 3 Spruce Stairs 2 Chest                                           |        |
| `shipwreck/sideways_fronthalf`             | The bow of a ship, capsized, intact.                                                                        | 117 Oak Planks 104 Oak Stairs 60 Spruce Planks 13 Spruce Stairs 11 Spruce Fence 7 Oak Log 7 Oak Trapdoor 1 Chest                                                     |        |
| `shipwreck/sideways_fronthalf_degraded`    | The bow of a ship, capsized, with a degraded appearance.                                                    | 83 Oak Planks 81 Oak Stairs 46 Spruce Planks 13 Spruce Stairs 8 Spruce Fence 7 Oak Trapdoor 6 Oak Log 1 Chest                                                        |        |
| `shipwreck/sideways_full`                  | A whole ship, capsized, intact.                                                                             | 223 Oak Planks 171 Oak Stairs 159 Spruce Planks 30 Spruce Fence 22 Spruce Stairs 14 Oak Trapdoor 10 Oak Log 6 Oak Fence 3 Chest                                      |        |
| `shipwreck/sideways_full_degraded`         | A whole ship, capsized, with a degraded appearance.                                                         | 206 Oak Planks 150 Spruce Planks 149 Oak Stairs 24 Spruce Fence 21 Spruce Stairs 11 Oak Trapdoor 10 Oak Log 6 Oak Fence 3 Chest                                      |        |
| `shipwreck/upsidedown_backhalf`            | The stern of a ship, turtled, intact.                                                                       | 176 Oak Planks 107 Oak Stairs 60 Spruce Planks 10 Spruce Fence 10 Spruce Stairs 7 Spruce Slab 4 Oak Trapdoor 4 Oak Log 3 Oak Slab 2 Oak Fence 2 Chest                |        |
| `shipwreck/upsidedown_backhalf_degraded`   | The stern of a ship, turtled, with a degraded appearance.                                                   | 167 Oak Planks 98 Oak Stairs 55 Spruce Planks 10 Spruce Fence 8 Spruce Stairs 7 Spruce Slab 4 Oak Trapdoor 4 Oak Log 3 Oak Slab 2 Oak Fence 2 Chest                  |        |
| `shipwreck/upsidedown_fronthalf`           | The bow of a ship, turtled, intact.                                                                         | 123 Oak Planks 93 Oak Stairs 60 Spruce Planks 21 Spruce Stairs 14 Oak Trapdoor 9 Oak Log 8 Spruce Fence 2 Chest                                                      |        |
| `shipwreck/upsidedown_fronthalf_degraded`  | The bow of a ship, turtled, with a degraded appearance.                                                     | 112 Oak Planks 82 Oak Stairs 54 Spruce Planks 20 Spruce Stairs 11 Oak Trapdoor 9 Oak Log 8 Spruce Fence 2 Chest                                                      |        |
| `shipwreck/upsidedown_full`                | A whole ship, turtled, intact.                                                                              | 219 Oak Planks 153 Oak Stairs 116 Spruce Planks 30 Spruce Fence 28 Spruce Stairs 19 Spruce Slab 14 Oak Trapdoor 10 Oak Log 4 Oak Fence 3 Chest 2 Oak Slab            |        |
| `shipwreck/upsidedown_full_degraded`       | A whole ship, turtled, with a degraded appearance.                                                          | 194 Oak Planks 133 Oak Stairs 109 Spruce Planks 28 Spruce Stairs 27 Spruce Fence 19 Spruce Slab 14 Oak Trapdoor 10 Oak Log 4 Oak Fence 3 Chest 2 Oak Slab            |        |
| `shipwreck/with_mast`                      | The most complete shipwreck structure. A whole ship, upright, with all components, and three masts, intact. | 209 Oak Planks 182 Oak Stairs 108 Spruce Planks 70 Spruce Slab 67 Oak Log 35 Spruce Fence 24 Spruce Stairs 16 Oak Trapdoor 6 Oak Fence 4 Oak Slab 3 Chest 1 Oak Door |        |
| `shipwreck/with_mast_degraded`             | A whole ship, upright, with all components, three masts, and a degraded appearance.                         | 201 Oak Planks 172 Oak Stairs 107 Spruce Planks 63 Spruce Slab 28 Spruce Fence 24 Oak Log 23 Spruce Stairs 16 Oak Trapdoor 6 Oak Fence 4 Oak Slab 3 Chest 1 Oak Door |        |

