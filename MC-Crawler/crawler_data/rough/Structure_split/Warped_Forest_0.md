# Warped Forest
The warped forest is a biome found in the Nether. It is a relatively safe biome because no hostile mobs spawn there naturally.

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
- 9 External links

## Description
The warped forest is dense and has a cyan color scheme. The forest's fog and particles have a dark royal blue tone, and the fog appears lilac with Night Vision.

The floor of the biome is composed mostly of warped nylium, with some netherrack and warped wart blocks generating on the surface. The vegetation of the biome includes fungi, warped roots, huge warped fungi, and twisting vines growing from the ground. Large overhangs extend over the oceans of lava. Blobs of glowstone generate in the ceiling, and shroomlights generate on the huge fungus scattered around the forest.


In general, the warped forest is much safer than other Nether biomes. Endermen spawn most commonly here, making it a good place for the player to obtain ender pearls. The only other mob that can spawn naturally here are striders, however, hostile mobs may still spawn in fortresses and bastion remnants. Endermen also spawn at much lower density than in the End.
The following mobs are naturally spawned here：

| Mob      | Spawn weight | Group size | Charge[note 1] | Budget[note 1]    |
|----------|--------------|------------|----------------|-------------------|
|          |              |            |                | Monster category  |
| Enderman | 1            | 4          | 1.0            | 0.12              |
|          |              |            |                | Creature category |
| Strider  | 1            | 1–2        | —              | —                 |

1. ↑ a bWhen spawning a mob with a budget, take the sum of the charge of each existing mob divided by the distance to that mob. If the total times the new mob's charge is greater than the new mob's budget, the spawn fails. See Spawn#Spawn costs for details.

{ "monster": { "mobs": [ { "charge": "1.0", "mob": "Enderman", "weight": 1, "budget": "0.12", "size": "4" } ], "totalWeight": 1 }, "creature": { "mobs": [ { "charge": "—", "mob": "Strider", "weight": 60, "budget": "—", "size": "1&ndash;2" } ], "totalWeight": 60 } }
| Mob      | Spawn weight | Group size        |
|----------|--------------|-------------------|
|          |              | Monster category  |
| Enderman | 1            | 1                 |
|          |              | Creature category |
| Strider  | 1            | 2–4               |

{ "monster": { "mobs": [ { "size": "1", "mob": "Enderman", "weight": 16 } ], "totalWeight": 16 }, "creature": { "mobs": [ { "size": "2&ndash;4", "mob": "Strider", "weight": 20 } ], "totalWeight": 20 } }
## Data values
### ID
Java Edition:

| Name          | Identifier      | Numeric ID | Translation key                 |
|---------------|-----------------|------------|---------------------------------|
| Warped Forest | `warped_forest` | `172`      | `biome.minecraft.warped_forest` |

Bedrock Edition:

| Name                | Identifier      | Numeric ID |
|---------------------|-----------------|------------|
| [No displayed name] | `warped_forest` | `180`      |


