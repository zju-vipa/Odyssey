# Pillager Outpost
A pillager outpost is an assortment of structures inhabited by pillagers.

## Contents
- 1 Generation
- 2 Mobs
	- 2.1 Bad Omen
- 3 Structure
	- 3.1 Technical structures
- 4 Loot
- 5 Data values
	- 5.1 ID
- 6 History
- 7 Issues
- 8 Gallery
	- 8.1 Screenshots
- 9 References

## Generation
Pillager outposts are semi-rare structures, generating every several hundred to couple thousand blocks.[1] This makes them rarer than villages[2] but less rare than woodland mansions.

Pillager outposts can generate naturally in any village-generating biome, including:

- Plains
- Desert
- Savanna
- Taiga
- Snowy Plains
- Snowy Taiga‌[BE  only]
- Sunflower Plains‌[BE  only]
- Meadow

Pillager outposts also generate in the following biomes, where villages do not spawn:

- Grove
- Snowy Slopes
- Jagged Peaks
- Frozen Peaks
- Stony Peaks
- Cherry Grove

In Java Edition, pillager outposts never generate too close to, or within, villages. They can do so in Bedrock Edition as well as generate far away from villages.

In Java Edition, if an outpost spawns in the water or in the air (e.g., spawning near a savanna plateau), then a platform of grass (or sand), dirt, and stone spawns underneath it in a circular shape. This also applies to the smaller structures such as tents, targets, log piles, and cages. On occasion, the smaller structures still spawn in the air despite having a platform below them, depending on how high up they are.

In Bedrock Edition, pillager outposts generate with foundations similar to that of a woodland mansion: watchtowers use cobblestone, birch planks, and dark oak logs as their foundation; tents and cages generate dark oak planks as their foundation; log piles use horizontal dark oak logs as their foundation; and targets generate cobblestone as a foundation.

The outpost tower generates each time. Up to 4 other smaller structures may spawn around the periphery of the main outpost structure.

Eight extra air blocks also generate around the outpost.[3]

## Mobs
|       |            |          |
|-------|------------|----------|
| Allay | Iron Golem | Pillager |

Iron golems and allays spawn only during the generation of the outpost structures. An iron golem has a 85% chance of spawning. Meanwhile, the allay has a 50% chance of spawning. These mobs spawn in cages. The iron golem can punch pillagers who are one block away from the fences of the cage. 

Both regular pillagers and pillager captains can continuously spawn around the structure. Pillagers can still spawn if a player is inside the tower. In Java Edition they spawn in a 72×54×72 area centered on the top level of the watchtower, the same level as the chest.

In Bedrock Edition, pillagers spawn at the highest available position in up to 4 columns depending on which direction the structure generates. The number of spawning locations vary based on the orientation of the structure: 2 spots when the door is facing east/west (50%), 4 for north (25%), and 1 for south (25%). The first spawning column is one block diagonally toward the chest at the top from the center of the structure; the other possible 3 are 8 blocks east, south, and southeast of the first. Pillagers can spawn in these columns, beginning from the bottom floor and extending vertically up to 18 blocks. Pillagers spawn on the northwest corner of a block and require a clear 2×2×2 area for spawning. Any solid block in this region will inhibit spawning, while transparent blocks like leaves or glass won't impede spawning if they're not positioned on the actual spawning spot.

In Java Edition, only pillagers may spawn within a pillager outpost spawn area. Pillagers may naturally spawn on any valid opaque block (except leaves) as long as the block light level is 8 or less. They cannot, however, spawn on blocks that emit a light level of 14 or greater. There is a 6% chance for a pillager to spawn as a patrol leader.

In Java Edition, there are 15 jigsaw blocks that can generate the structures around the tower. Each structure has a 1 in 13 chance of being generated, including allay and iron golem cages. When generated, iron golem cages spawn one golem, and allay cages spawn two allays.

A total of eight pillagers, including the pillager captain, spawns in a pillager outpost.

### Bad Omen
Upon killing an outpost captain, the player receives 1 level of the Bad Omen effect applied to them for 100 minutes (5 in-game days).

## Structure
Main article: /Structure
A pillager outpost consists of a 4 level watchtower with other smaller structures around it.

Structure blocks can be used to manually load pieces of the pillager outpost from the /data/minecraft/structures/pillager_outpost folder in minecraft.jar. To do so, set a structure block to Load mode, enter pillager_outpost/<structure_name>, and press LOAD.

| Structure name                                                        | Description                                                         | Consists of                                                                                                                                                                                                                                                                  | Images |
|-----------------------------------------------------------------------|---------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| `pillager_outpost/watchtower`                                         | A large tower with a lootcheston the top level.                     | 347 Dark Oak Planks 290 Birch Planks 207 Cobblestone 144 Dark Oak Log 48 Dark Oak Fence 45 Dark Oak Slab 33 Cobblestone Stairs 16 Dark Oak Stairs 8 Cobblestone Wall 4 Cobblestone Slab 4 Torch 1 Chest (random loot) 8  Ominous Banner‌[JE  only]/Illager Banner‌[BE  only] |        |
| `pillager_outpost/feature_cage1`<br/>`pillager_outpost/feature_cage2` | A wooden cage, with cage_2 having aniron golem.                     | 24 Dark Oak Fence 12 Dark Oak Log 8 Dark Oak Stairs 4 Dark Oak Slab 0~1 Iron Golem                                                                                                                                                                                           |        |
| `pillager_outpost/feature_cage_with_allays`                           | A wooden cage, with someallaystrapped inside.                       | 28 Dark Oak Fence 12 Dark Oak Log 8 Dark Oak Stairs 4 Dark Oak Slab 0~3 Allay                                                                                                                                                                                                |        |
| `pillager_outpost/feature_logs`                                       | A pile of dark oaklogs.                                             | 21 Dark Oak Log                                                                                                                                                                                                                                                              |        |
| `pillager_outpost/feature_targets`                                    | Two scarecrow-like targets.                                         | 6 Dark Oak Fence2 Carved Pumpkin2 Hay Bale                                                                                                                                                                                                                                   |        |
| `pillager_outpost/feature_tent1`                                      | A small tent  made ofwool, with acrafting tableinside.              | 20 White Wool10 Dark Oak Fence1 Crafting Table                                                                                                                                                                                                                               |        |
| `pillager_outpost/feature_tent2`                                      | A small tent made of wool, with a crafting table andpumpkinsinside. | 20 White Wool10 Dark Oak Fence4 Pumpkin1 Crafting Table                                                                                                                                                                                                                      |        |

