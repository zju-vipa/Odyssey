#### Spawning requirements
The monster spawner performs a relaxed version of the ordinary spawning check: the general solid block requirement is removed, but the volume (hitbox of the mob) is kept along with some other checks according to mob specifics. As a result, for some types of mobs to spawn in the outer planes of the spawning volume, some planes outside the volume may also need to be free of solid blocks to conform with the mobs' height, width, or other rules governing their individual spawn volumes. Examples:

- For mobs that are two or more blocks tall such as zombies, skeletons, or blazes to spawn in the top y-layer, the layer above that must contain only a transparent block such asair,glass,leaves, etc.
- InJava Edition, a turtle monster spawner can spawn turtles only onsandblocks less than 4 blocks above sea level (typically at Y=62). InBedrock Editionno biome/light/height conditions apply for turtles in monster spawners.
- InBedrock Edition, some animals require light level 7+, e.g. chicken, sheep, cow, rabbit. Others ignore the light level condition given in the spawning rules json files, e.g. parrot, turtle. This suggests that some of the early animals have hard-coded requirements when used in monster spawners.

|  |
|--|
|  |
|  |

|  |
|--|
|  |
|  |

|  |
|--|
|  |
|  |

|  |
|--|
|  |
|  |
|  |

|  |
|--|
|  |
|  |
|  |

|  |
|--|
|  |
|  |
|  |

|  |
|--|
|  |
|  |

|  |
|--|
|  |
|  |
|  |
|  |

1. ↑Pig monster spawners do not appear naturally in vanilla Minecraft.

For all of the volumes listed in the table, the horizontal plane is centered on the center of the monster spawner block. While the spawning volume for pigs is 8.9×2.9×8.9, the requirement of grass blocks that are necessary for pigs to spawn reduces the actual volume in which they successfully spawn to 8.9×1.0×8.9. Other mobs can spawn in mid-air, ignoring general rules about spawning on solid ground.

The spawn conditions do not include biomes for most mobs. As such, monster spawners can place mobs where they normally wouldn't generate. For example, a mooshroom monster spawner can operate in a plains biome as long as there are mycelium blocks within the spawn area because the mooshroom's spawning code checks only for mycelium. The reason mooshrooms are not actually spawned elsewhere is that the game does not normally try to spawn them in other biomes: only the mushroom field biome has mooshroom on the list of things to spawn.

### Disabling
Disabling a blaze monster spawner with nine blocks. Glowstone can be replaced with other light sources of light level 15.
Blaze monster spawner disabled by four jack o'Lanterns. This works only in Bedrock Edition in small rooms.
With the clever placement of nine solid blocks, a magma cube monster spawner can be completely disabled. Only the cobblestone is needed, glass is just for distance marking.
See also: Light § Mobs

The way a monster spawner can be disabled depends on the entity it tries to spawn.

For a monster spawner that generates mobs that spawn only in dark conditions (light level = 0), a torch placed on any side or top of the monster spawner is sufficient to disable it for the whole 9×3×9 volume.

For a blaze or silverfish monster spawner, a light level of 12 is required to prevent spawning. This can be achieved by:

- Laying 9 blocks in the pattern shown on the right using blocks having a luminance value of 15
- Laying a dense 7×7 grid of torches on the monster spawner's Y level
- InBedrock Edition, placing a light source of level 15 on four surfaces

A monster spawner is also disabled by filling the spawning volume with solid blocks. This is often used to disable magma cube monster spawners, as magma cubes can spawn in any light level. However, since all magma cubes require the space of a large magma cube in order to spawn, a clever placement of as little as 9 solid blocks a layer above the monster spawner (see right image) can completely disable it.

### Custom monster spawners
A monster spawner in a monster room that produces spiders.
In Java Edition, using commands, monster spawners can be customized:

- They can be made to spawn any kind of entity.
- A single monster spawner can spawn multiple different entities, chosen at random from a list.
- Properties can be set on the spawned entities.
- Various range and timing properties of the monster spawner can be changed.

Detailed technical information about custom monster spawners can be found below.

In Bedrock Edition, monster spawner customization can not be done in the base game (i.e. without addons/behavior packs).

