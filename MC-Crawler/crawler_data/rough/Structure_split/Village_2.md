## Mechanics
Main article: Village mechanics
### Java Edition
A subchunk is a "village center" if it contains at least one claimed bed, bell, or job site block. The 26 subchunks in a 3×3×3 cube around such a subchunk are also considered part of a village.

Villages as a whole have no defined "center", "size", or "radius", it's all based on proximity to any "village center" subchunk.

### Bedrock Edition
A village always consists of at least one acceptable bed and one villager. Rarely, a village structure can generate without beds, thus not qualifying as a village. Upon creation, a village center is defined as a bed claimed by the first villager (a village leader), or the gathering site block (a bell), and the village's size is the greater of 32 blocks or the distance to the furthest bed from the center. Any villager, village golem, or raid-spawned illagers can pathfind back into the village if they find themselves farther than that many blocks from the center.

Villages are established by the number of valid beds in the village. 

The maximum population of a village is the number of valid beds. If the population drops below that point (due to death or removal), but there are at least two villagers left who can reach each other, the villagers mate and breed until the population is at the maximum.

A village is created when at least one villager links to one bed. The village continues to exist as long as one of its villagers remains linked to one of its beds. If all beds are unlinked (by being destroyed, by players sleeping in them, or by villagers failing to pathfind to them), then the village ceases to exist. When this happens the villagers lose all links to job site blocks and bells, and cannot use them.

When the first villager links to a bed a village of size 65×25×65 blocks is created, centered on the pillow of that bed. The boundaries, and consequently the center (which is important because it defines where cats and iron golems can spawn), may change as other villagers link or unlink from point of interest (POI) blocks. When the boundaries change the center usually shifts to the location of POI block near the midpoint between the farthest out POI in each direction. In naturally generated villages there is usually a bell near the village center, but aside from that bells have no special role distinct from other POI in how the game defines and manages the village center and boundaries.

### Gathering site
Villages have gathering sites where villagers may mingle. A gathering site is defined as a bell located within the village boundary. A wandering trader may spawn at a gathering site, accompanied by trader llamas. A villager also rings the bell when a raid starts. 

### Job site blocks
Job site blocks are blocks such as grindstones, smithing tables, and lecterns, which are used by villagers. Villagers with the corresponding professions spend their time in front of their job site block, except for nitwits, baby villagers and unemployed villagers (villagers without profession overlays). Upon claiming a job site block, green particles appear above both the villager and the job site block, and the villager takes up the profession of the job site block if unemployed. Villagers that have already been traded with can claim only job site blocks related to their profession. Employed villagers that are not linked to a job site block are unable to restock their trades. Villagers cannot link to a job site block that has already been claimed by another villager. There are thirteen job site blocks in the game, each linking to their respective villager profession.

## Data values
### ID
Java Edition:

| Structure type | Identifier |
|----------------|------------|
| Jigsaw         | `jigsaw`   |

| Structure       | Identifier        |
|-----------------|-------------------|
| Desert Village  | `village_desert`  |
| Plains Village  | `village_plains`  |
| Savanna Village | `village_savanna` |
| Snowy Village   | `village_snowy`   |
| Taiga Village   | `village_taiga`   |

Bedrock Edition:

| Structure | Identifier | Translation key   |
|-----------|------------|-------------------|
| Village   | `village`  | `feature.village` |


