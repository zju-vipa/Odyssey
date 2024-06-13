# Nether Fortress
A nether fortress is a large structure found in the Nether, consisting of bridges, corridors and towers. Nether fortresses are the only place where wither skeletons and blazes spawn, the latter's blaze rods being required to craft and fuel brewing stands and craft eyes of ender to access the End. It also features nether wart as loot, which is a key ingredient in brewing.

## Contents
- 1 Generation
- 2 Structure
	- 2.1 Blocks
- 3 Mobs
	- 3.1 Java Edition
	- 3.2 Bedrock Edition
- 4 Loot
- 5 Data values
	- 5.1 ID
	- 5.2 Config
- 6 Advancements
- 7 Video
- 8 History
- 9 Issues
- 10 Trivia
- 11 Gallery
	- 11.1 Screenshots
	- 11.2 Development images
- 12 References

## Generation
Nether fortresses generate in all Nether biomes. To do so, the game splits the Nether into regions in which one of either a fortress or a bastion remnant can generate. The regions are 432×432 blocks in Java Edition and 480×480 blocks in Bedrock Edition. 

The Nether structure generation in Java Edition. The black lines represent each region and the dots represent coordinates. The green color is where they can generate and red is where they cannot.
Each region has a four chunk separation located on the south and east borders of the region in which neither a fortress nor a bastion can generate. 

The Nether structure generation in Bedrock Edition. The black lines represent each region and the dots represent coordinates. The green color is where they can generate and red is where they cannot.
This leaves only a 368×368 block section in Java Edition or 416×416 block section in Bedrock Edition where a structure can generate. 

Two structures never generate in the same region, although they might overlap if they generate close to the separation border. In Java Edition, the chance of a fortress generating instead of a bastion is 2⁄5 (40%), while in Bedrock Edition the chance of a fortress generating instead of a bastion is 1⁄3 (33.3%).

Nether fortresses can generate buried in netherrack. In such a case, the interior is not filled with netherrack; all hallways and passages are clear except for open walkways and bridges. It is possible but rare for glowstone or crimson and warped huge fungi to generate inside the fortress pathways.

## Structure
Main article: /Structure
Nether fortresses are large complexes composed of nether bricks supported by pillars that tower high above the lava seas.

Segments of a nether fortress that are fully enclosed.
The fortress generation starts with a plain four-way crossing centered at chunk coordinates 11, ~, 11 of the designated chunk.

A crossroad found where walkways intersect.
A fortress has two areas, an exterior area of open bridges and an interior area of enclosed corridors. Both the bridges and corridors can end in an unfinished passageway structure or may simply end without elaboration. Fortresses can tunnel through netherrack, giving the "exterior" areas an appearance of tunnels with nether brick floor and netherrack walls and ceilings. At broken sections the terrain is not cleared, which may create a tunnel that leads straight into a wall of netherrack.

The general pattern of the walkways.
A lava well found inside a nether fortress.
The exterior consists of:

- Straight bridges.
- Up to five plain four-way crossings.
- Up to four four-way crossings with arches made of nether brick and nether brick fences.
- Up to four small rooms with a single entrance and full-block "stairs" leading to the roof, which may have a single path leading out.
- Up to 2 blaze monster spawner platforms: structures consisting of three full-block "stairs" leading to a small platform fenced with nether brick fence, with ablazemonster spawnerin the center.

Stairs in a nether fortress, with nether wart growing next to them.
The interior of the structures have 1×2 windows with nether brick fences as the windowpanes. The fences also form gate-like structures at the entrances of some rooms and corridors. Rooms include:

- The lava well room, which is the connection between the interior and exterior areas.
- Straight corridors.
- Up to five four-way crossings.
- Up to 20 corridor turns (10 right-turns and 10 left-turns), each with a1⁄3chance of having aloot chestin the corner.
- Up to three stairways made from actual stair blocks, leading downward.
- Up to two three-way intersections with a small exterior balcony.
- Up to two stairways leading up to a garden ofsoul sandandnether wartat the base of the stairs, a corridor leading away from the upper landing and a corridor behind the stairs. If the room is generated embedded in netherrack, only one block above the landing is cleared.

An outline of the "bounding boxes".
### Blocks
| Block                 |
|-----------------------|
| Nether Bricks         |
| Nether Brick Fence    |
| Nether Brick Stairs   |
| Soul Sand             |
| Nether Wart           |
| Chest                 |
| Blaze Monster Spawner |
| Lava                  |

The structure bounding box for the 4-way intersection is pictured above (top-down view), and consists of a 19×11×19 volume centered on the floor block in the center of the intersection. This contrasts many of the other structure bounding boxes as their outlines tend to tightly follow the physical bounds of the structure.

## Mobs
Fortresses use a list of possible mobs to spawn that is separate from the rest of the Nether, regardless of the biome the fortress generates in. This includes zombified piglins, skeletons and magma cubes, as well as two exclusive mobs not found anywhere else: blazes and wither skeletons.

A blaze monster spawner generated in the nether fortress.
Mobs spawn at a much higher rate if the fortress is surrounded by soul sand valley or warped forest biomes, as hostile mobs in these biomes (ghasts, skeletons or endermen) spawn much less frequently, allowing most hostile mobs to spawn in the fortress.[1]

### Java Edition
In Java Edition, the spawning algorithm has two checks:

1. It checks if the spawn coordinates are within the "bounding box" of a single piece (e.g. corridor or walkway) of the fortress.(referred as "structure bounding box" above)In this case the block type of the ground does not matter.
2. It checks if the spawn coordinates are within the "bounding box"(referred as "area bounding box" above)of the entire fortress and whether the ground consists ofnether bricks.

If either check passes, it uses the special mob list for fortresses rather than the list for the biome when choosing the mob to spawn. The actual mob spawning proceeds as normal for the mob chosen from this list.

| Mob              | Spawn weight    | Group size       |
|------------------|-----------------|------------------|
|                  |                 | Monster category |
| Blaze            | $\frac{10}{28}$ | 2–3              |
| Wither Skeleton  | $\frac{8}{28}$  | 5                |
| Zombified Piglin | $\frac{5}{28}$  | 4                |
| Magma Cube       | $\frac{3}{28}$  | 4                |
| Skeleton         | $\frac{2}{28}$  | 5                |

{ "monster": { "mobs": [ { "size": "2&ndash;3", "mob": "Blaze", "weight": 10 }, { "size": "5", "mob": "Wither Skeleton", "weight": 8 }, { "size": "4", "mob": "Zombified Piglin", "weight": 5 }, { "size": "4", "mob": "Magma Cube", "weight": 3 }, { "size": "5", "mob": "Skeleton", "weight": 2 } ], "totalWeight": 28 } }
### Bedrock Edition
In Bedrock Edition, instead of spawning anywhere within a structural bounding box, most mobs spawn only in structure spawn locations along varied-length lines spaced apart 4-11 blocks throughout the fortress. They are not set to a particular Y level other than "inside the structure" and are indeed columns several blocks high. They do not require any special type of block, any regular spawnable block suffices. 

To identify these spawning columns, glass panes can be placed all over the fortress, 1 block above surface blocks. This keeps the mobs stationary. (This technique works in Bedrock due to mobs spawning in the northwest corner of blocks.) Note that these spots may be on top of the raised side blocks, so these side blocks have to be removed before a glass pane grid can be placed. 

Zombified Piglin spawns do not obey structure spawn locations; they can spawn anywhere in the fortress.

## Loot
See also: Chest loot

A chest that generated in a nether fortress.
Fortresses generate nether fortress loot with chests in the indoor sections placed at some corridor turns.

In Java Edition and Bedrock Edition, each nether fortress chest contains  items drawn from 2 pools,  with the following distribution: 

| Item                             | Stack Size  [A] |    | Weight   [B]    |                 | Chance   [C] | Avg.per chest   [D] | Avg. # cheststo search   [E] |
|----------------------------------|-----------------|----|-----------------|-----------------|--------------|---------------------|------------------------------|
|                                  | 2–4×            | 1× | 2–4×            | 1×              |              |                     |                              |
| Nothing[F]                       | —               | 1  | —               | $\frac{14}{15}$ | 93.3%        | 0.933               | 1.1                          |
| Gold Ingot                       | 1–3             | —  | $\frac{15}{73}$ | —               | 49.0%        | 1.233               | 2.0                          |
| Saddle                           | 1               | —  | $\frac{10}{73}$ | —               | 35.3%        | 0.411               | 2.8                          |
| Golden Horse Armor               | 1               | —  | $\frac{8}{73}$  | —               | 29.1%        | 0.329               | 3.4                          |
| Nether Wart                      | 3–7             | —  | $\frac{5}{73}$  | —               | 19.0%        | 1.027               | 5.3                          |
| Iron Ingot                       | 1–5             | —  | $\frac{5}{73}$  | —               | 19.0%        | 0.616               | 5.3                          |
| Diamond                          | 1–3             | —  | $\frac{5}{73}$  | —               | 19.0%        | 0.411               | 5.3                          |
| Flint and Steel                  | 1               | —  | $\frac{5}{73}$  | —               | 19.0%        | 0.205               | 5.3                          |
| Iron Horse Armor                 | 1               | —  | $\frac{5}{73}$  | —               | 19.0%        | 0.205               | 5.3                          |
| Golden Sword                     | 1               | —  | $\frac{5}{73}$  | —               | 19.0%        | 0.205               | 5.3                          |
| Golden Chestplate                | 1               | —  | $\frac{5}{73}$  | —               | 19.0%        | 0.205               | 5.3                          |
| Diamond Horse Armor              | 1               | —  | $\frac{3}{73}$  | —               | 11.8%        | 0.123               | 8.5                          |
| Obsidian                         | 2–4             | —  | $\frac{2}{73}$  | —               | 8.0%         | 0.247               | 12.5                         |
| Rib Armor Trim Smithing Template | —               | 1  | —               | $\frac{1}{15}$  | 6.7%         | 0.067               | 15.0                         |



↑ The size of stacks (or for unstackable items, number) of this item on any given roll.

↑ The weight of this item relative to other items in the pool.

↑ The odds of finding any of this item in a single chest.

↑ The number of items expected per chest, averaged over a large number of chests.

↑ The average number of chests the player should expect to search to find any of this item.

↑ 'Nothing' does not refer to the chance of an empty chest.  Instead, it refers to the chance that the random loot generator does not add any loot on a single roll.



## Data values
### ID
Java Edition:

| Structure type  | Identifier |
|-----------------|------------|
| Nether Fortress | `fortress` |

| Structure       | Identifier |
|-----------------|------------|
| Nether Fortress | `fortress` |

Bedrock Edition:

| Structure       | Identifier | Translation key    |
|-----------------|------------|--------------------|
| Nether Fortress | `fortress` | `feature.fortress` |

### Config
Java Edition:

- Structure configuration
	- type:minecraft:fortress
	- 
	- Fields common to all structures

