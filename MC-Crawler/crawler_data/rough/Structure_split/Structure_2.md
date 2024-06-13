## Removed structures
These are structures that have been removed or exist only in older versions of Minecraft.

| Structure               | Biome(s)                                             | Description                                                                                                                                                                                                                                                                                                                        |
|-------------------------|------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Brick Pyramid           | Anywhere, since biomes didn't exist back then.       | A giant pyramid that had no interior and was made solely out of bricks. The official name for this structure is unknown. Was removed inJava Edition Infdev 20100327.                                                                                                                                                               |
| Glass Pillar            | AnyOverworldbiome.                                   | A tall, 1×1 glass pillar that stretched from the end portal room in the stronghold all the way to the build limit. According to Jeb, it was a debug feature that he forgot to remove. It was removed in the versionJava Edition Beta 1.9 Prerelease 4.                                                                             |
| Starting House          | Anywhere on theJava Edition Indevworld.              | It used to serve as the spawn location for the player during the Indev phase. The first edition of this house was made of mossy cobblestone, but later it was changed to wooden planks. It also included two chests with various items, which was later removed.                                                                   |
| Monolith                | Anywhere duringInfdev.                               | These were chunk-sized patches of terrain that would generate up to the height limit. They were never intended to be in the game as they were just aglitch. Monoliths were patched in the versionAlpha v1.2.0 Preview.                                                                                                             |
| Nether Spire‌[BE  only] | Anywhere where theNether Reactorwas built.           | It was a tall and round structure that spawned over the Nether Reactor. It was made out of obsidian, which was later changed to netherrack. It would spawn variousZombie Pigmenand items fromThe Nether. Its purpose was to enable the players on Pocket Edition to obtain certain items, since The Nether wasn't implemented yet. |
| Obsidian Wall           | Anywhere, since it stretched toward every direction. | A 2 block tall obsidian wall that was present during some versions of the Infdev phase. It started in the middle of the world, and stretched toward north, south, west and east. This structure doesn't have an official name.                                                                                                     |

## Generation
Main article: World generation § Features and structures
Structures are generated for a given chunk after the terrain has been formed. The chunk format includes a tag called TerrainPopulated that indicates whether structures whose point of origin is in that chunk have been generated. If it is false or missing, it generates again. Structure generation is based on what is already in the chunk, so (for example) flagging a chunk that has already been populated for repopulation approximately doubles the amount of ore in it. When structures are generated, they can spill over into neighboring chunks that have been previously generated.

## Data values
### ID
The following table lists configured structure features' IDs in Java Edition and structure features' IDs in Bedrock Edition. These IDs can be used in /locate command.

| Structure name   | Java Edition                                                                                                                                                                      | Bedrock Edition                          | Dimension            |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|----------------------|
| Ancient city     | `ancient_city`                                                                                                                                                                    | `ancientcity`<br/>`ancient_city`         | Overworld            |
| Bastion remnant  | `bastion_remnant`                                                                                                                                                                 | `bastionremnant`<br/>`bastion_remnant`   | The Nether           |
| Buried treasure  | `buried_treasure`                                                                                                                                                                 | `buriedtreasure`<br/>`buried_treasure`   | Overworld            |
| End city         | `end_city`                                                                                                                                                                        | `endcity`<br/>`end_city`                 | The End              |
| Fortress         | `fortress`                                                                                                                                                                        | `fortress`                               | The Nether           |
| Woodland mansion | `mansion`                                                                                                                                                                         | `mansion`                                | Overworld            |
| Mineshaft        | `mineshaft`<br/>`mineshaft_mesa`                                                                                                                                                  | `mineshaft`                              | Overworld            |
| Monument         | `monument`                                                                                                                                                                        | `monument`                               | Overworld            |
| Nether fossil    | `nether_fossil`                                                                                                                                                                   | Not a Structure                          | The Nether           |
| Ocean ruins      | `ocean_ruin_cold`<br/>`ocean_ruin_warm`                                                                                                                                           | `ruins`                                  | Overworld            |
| Pillager outpost | `pillager_outpost`                                                                                                                                                                | `pillageroutpost`<br/>`pillager_outpost` | Overworld            |
| Ruined portal    | `ruined_portal`<br/>`ruined_portal_desert`<br/>`ruined_portal_jungle`<br/>`ruined_portal_mountain`<br/>`ruined_portal_nether`<br/>`ruined_portal_ocean`<br/>`ruined_portal_swamp` | `ruinedportal`<br/>`ruined_portal`       | Overworld,The Nether |
| Shipwreck        | `shipwreck`<br/>`shipwreck_beached`                                                                                                                                               | `shipwreck`                              | Overworld            |
| Stronghold       | `stronghold`                                                                                                                                                                      | `stronghold`                             | Overworld            |
| Desert pyramid   | `desert_pyramid`                                                                                                                                                                  | `temple`                                 | Overworld            |
| Igloo            | `igloo`                                                                                                                                                                           |                                          |                      |
| Jungle pyramid   | `jungle_pyramid`                                                                                                                                                                  |                                          |                      |
| Swamp hut        | `swamp_hut`                                                                                                                                                                       |                                          |                      |
| Trail ruins      | `trail_ruins`                                                                                                                                                                     | `trail_ruins`                            | Overworld            |
| Village          | `village_desert`<br/>`village_plains`<br/>`village_savanna`<br/>`village_snowy`<br/>`village_taiga`                                                                               | `village`                                | Overworld            |

### Tags

  

This feature is exclusive to  Java Edition. 


In Java Edition, there are some structure tags in vanilla game.

| Tag                                         | Structure(s)                   |
|---------------------------------------------|--------------------------------|
| `#cats_spawn_as_black`<br/>`#cats_spawn_in` | Swamp hut                      |
| `#dolphin_located`                          | Shipwreck<br/>Underwater ruins |
| `#eye_of_ender_located`                     | Stronghold                     |
| `#mineshaft`                                | Mineshaft                      |
| `#ocean_ruin`                               | Underwater ruins               |
| `#on_ocean_explorer_maps`                   | Ocean monument                 |
| #on_treasure_maps                           | Buried treasure                |
| `#on_woodland_explorer_maps`                | Woodland mansion               |
| `#ruined_portal`                            | Ruined portal                  |
| `#shipwreck`                                | Shipwreck                      |
| `#village`                                  | Village                        |


