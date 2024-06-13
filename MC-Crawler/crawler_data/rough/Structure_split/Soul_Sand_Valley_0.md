# Soul Sand Valley
A soul sand valley is a dry biome located in the Nether. It is formed of large caverns with nether fossils and different blocks, mainly including soul sand and soul soil.

## Contents
- 1 Description
- 2 Sounds
	- 2.1 Music
	- 2.2 Ambience
- 3 Data values
	- 3.1 ID
- 4 History
- 5 Issues
- 6 Trivia
- 7 Gallery
	- 7.1 Screenshots
- 8 See also
- 9 References
- 10 External links

## Description
The soul sand valley is mostly composed of soul sand and soul soil, with gravel found on its coastlines. Soul fire is scattered throughout the valley and nether fossils poke out of the terrain. It lacks a diverse set of plants, with the only native vegetation being crimson roots and mushrooms, although fungi, nether sprouts, crimson roots, warped roots, and huge fungi may spawn where the valley borders a crimson forest or warped forest. Its fog is cyan and the air particles are gray as the sounds of winds and the voices of ghosts fill the air. Giant columns of basalt called basalt pillars can be found stretching from the floor to the ceiling. Caverns, fortresses and even bastions can also be found in the soul sand valley.

Glowstone blobs can be found in this biome, although they are significantly rarer than in other Nether biomes,[1] since the ceiling of this biome is made of soul sand or soul soil below which glowstone blobs cannot generate; they can still occasionally generate in caves and canyons in this biome,[2] because the ceiling is made of netherrack.

The following mobs are naturally spawned here：

| Mob           | Spawn weight    | Group size | Charge[note 1] | Budget[note 1]    |
|---------------|-----------------|------------|----------------|-------------------|
|               |                 |            |                | Monster category  |
| Skeleton      | $\frac{20}{71}$ | 5          | 0.7            | 0.15              |
| Ghast[note 2] | $\frac{50}{71}$ | 4          | 0.7            | 0.15              |
| Enderman      | $\frac{1}{71}$  | 4          | 0.7            | 0.15              |
|               |                 |            |                | Creature category |
| Strider       | 1               | 1–2        | 0.7            | 0.15              |

1. ↑ a bWhen spawning a mob with a budget, take the sum of the charge of each existing mob divided by the distance to that mob. If the total times the new mob's charge is greater than the new mob's budget, the spawn fails. See Spawn#Spawn costs for details.
2. ↑Only 5% of spawn attempts succeed.

{ "monster": { "mobs": [ { "charge": "0.7", "mob": "Skeleton", "weight": 20, "budget": "0.15", "size": "5" }, { "charge": "0.7", "mob": "Ghast", "weight": 50, "budget": "0.15", "note": "Only 5% of spawn attempts succeed.", "size": "4" }, { "charge": "0.7", "mob": "Enderman", "weight": 1, "budget": "0.15", "size": "4" } ], "totalWeight": 71 }, "creature": { "mobs": [ { "charge": "0.7", "mob": "Strider", "weight": 60, "budget": "0.15", "size": "1&ndash;2" } ], "totalWeight": 60 } }
| Mob      | Spawn weight     | Group size        |
|----------|------------------|-------------------|
|          |                  | Monster category  |
| Skeleton | $\frac{80}{126}$ | 1–2               |
| Ghast    | $\frac{40}{126}$ | 1                 |
| Enderman | $\frac{6}{126}$  | 1                 |
|          |                  | Creature category |
| Strider  | 1                | 2–4               |

{ "monster": { "mobs": [ { "size": "1&ndash;2", "mob": "Skeleton", "weight": 80 }, { "size": "1", "mob": "Ghast", "weight": 40 }, { "size": "1", "mob": "Enderman", "weight": 6 } ], "totalWeight": 126 }, "creature": { "mobs": [ { "size": "2&ndash;4", "mob": "Strider", "weight": 20 } ], "totalWeight": 20 } }
## Data values
### ID
Java Edition:

| Name             | Identifier         | Numeric ID | Translation key                    |
|------------------|--------------------|------------|------------------------------------|
| Soul Sand Valley | `soul_sand_valley` | `170`      | `biome.minecraft.soul_sand_valley` |

Bedrock Edition:

| Name             | Identifier        | Numeric ID |
|------------------|-------------------|------------|
| Soul Sand Valley | `soulsand_valley` | `178`      |


