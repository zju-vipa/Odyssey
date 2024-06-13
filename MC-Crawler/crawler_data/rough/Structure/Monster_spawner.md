# Monster Spawner
A monster spawner is a type of spawner found in a variety of structures. It contains a miniature mob, and constantly spawns instances of that mob as long as a player is nearby and, if applicable for the mob it spawns, if there are valid dark areas nearby. It cannot be obtained as an item in survival mode or moved by a piston, and it drops only experience orbs when broken.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
- 2 Usage
	- 2.1 Mechanics
		- 2.1.1 Spawning requirements
	- 2.2 Disabling
	- 2.3 Custom monster spawners
	- 2.4 Note blocks
	- 2.5 Piston interactivity
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block data
- 5 Video
- 6 History
- 7 Issues
- 8 Trivia
- 9 Gallery
	- 9.1 Renders
		- 9.1.1 Spawner
		- 9.1.2 Structure
	- 9.2 Screenshots
- 10 See also
- 11 Notes
- 12 References
- 13 External links

## Obtaining
Monster spawners cannot be obtained in Survival, even with Silk Touch.

A monster spawner can be obtained in Creative mode by taking it from Creative inventory, by using the /give command, or by using pick block. It is initially empty and inert, but can be configured to spawn a desired mob by using a spawn egg on the placed block.

A /setblock, /clone or /fill command can also be used to obtain a monster spawner.

### Breaking
If broken with a pickaxe, a monster spawner drops 15-43 experience. When mined with anything else, it drops nothing.

| Block     | Monster Spawner       |
|-----------|-----------------------|
| Hardness  | 5                     |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 25                    |
| Wooden    | 3.75                  |
| Stone     | 1.9                   |
| Iron      | 1.25                  |
| Diamond   | 0.95                  |
| Netherite | 0.85                  |
| Golden    | 0.65                  |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
Monster spawners can generate naturally in the following places:

** Monster room **
One in the center of the monster room spawning one of the following mobs with the indicated frequency:zombie(50%),skeleton(25%), orspider(25%).
** Mineshaft **
Any number ofcave spidermonster spawners, densely surrounded bycobwebs, scattered throughout.
** Woodland Mansions **
Optionally onespidermonster spawner, densely surrounded bycobwebs, in a rarely generated secret room on the 2nd or 3rd floor. It is sometimes visible through the windows from outside.
** Stronghold **
Onesilverfishmonster spawner in theend portalroom.
** Nether fortress **
One or twoblazemonster spawners on fenced platforms with full-block "stairs" leading up to them. Normally two are generated per fortress, but there can be fewer.
** Bastion remnant **
Onemagma cubemonster spawner hanging from achainunderneath a bridge in treasure rooms.
## Usage
The monster spawner spawns mobs in an (at most) 9×3×9 volume (see § Mechanics) around it when the player is within 16 blocks. Suitable spawning locations for the block's mob type are provided in or around the spawning volume. The monster spawner attempts to spawn four mobs around it, then waits from 10 to 39.95 seconds before attempting to spawn more.

In Peaceful difficulty, monster spawners still activate but do not spawn monsters in Bedrock Edition. In Java Edition, zombified piglins, magma cubes, and ghasts do not spawn at all and other hostile mobs disappear immediately after spawning.

Monster spawners are transparent, but they behave like leaves in that they diffuse sky light coming from directly above. 

In Bedrock Edition, they have a hitbox slightly smaller than a full block, and therefore, one can walk on the edge of a supporting full block directly below the monster spawner.

### Mechanics
A monster spawner activates when a player (that's not in Spectator mode) comes within a spherical radius of 16 blocks from the center point of the block; i.e. 15.5 blocks from the monster spawner itself. The player's presence is determined by coordinates at their foot level, meaning that a player standing exactly 15.5 blocks below the spawner don't activate it, even though their head is in range. In Java Edition an active monster spawner attempts to spawn mobs within a 4-block horizontal and 1-block vertical range; that is, in a 9×3×9 volume centered on the monster spawner. In Bedrock Edition, the horizontal spawning range is 4 blocks taxicab distance, creating spawning volume extending 4 blocks in each cardinal horizontal direction from the sides of the monster spawner; its horizontal cross-section is therefore diamond-shaped. Mobs can spawn anywhere in this range that is suitable, with mobs more likely to spawn closer to the monster spawner than farther away.

While mobs are spawned at fractional x and z-coordinates (i.e. not aligned to blocks), they are spawned at an integer y-coordinate. Horizontally, a mob can spawn with its center point anywhere within range, but vertically, mobs spawn with their legs at either the same layer as the monster spawner block, one block above it, or one block below it.  (Note that when there are other blocks slightly intersecting the mob's hitbox, they can sometimes glitch further away - often up - but this does not make it a true spawning point.)

The monster spawner attempts to spawn 4 mobs at randomly chosen points within the spawning volume, then waits anywhere from 200 to 799 ticks (10 to 39.95 seconds) before spawning again. As it waits, the mob model inside the block spins faster and faster. Except for the normal solid-block spawning requirement, all the remaining ones must be met (not in a solid block, correct light level, etc.), so the monster spawner often produces fewer than 4 mobs. When it does spawn, it emits a "poof", and more flame particles temporarily appear around it. If the monster spawner fails to spawn any mobs because it did not pick any suitable locations, it repeats this process every tick until it succeeds. It starts the next wait cycle only after successfully spawning at least one mob.

If 6 or more mobs of the monster spawner's type have their hitbox intersecting a 9×9×9 volume centered on the monster spawner block in Java Edition or a 16×10×16 volume centered on the lower northwest corner of the monster spawner block in Bedrock Edition, the monster spawner "poofs" without creating any mobs and then waits for the next cycle. [needs testing in Bedrock Edition] This is checked before each of the four spawn attempts.

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

### Note blocks
Monster spawner can be placed under note blocks to produce "bass drum" sounds.

### Piston interactivity
Monster spawners cannot be pushed by pistons. They also cannot be pushed nor pulled by sticky pistons.

## Data values
### ID
Java Edition:

| Name            | Identifier | Form         | Translation key           |
|-----------------|------------|--------------|---------------------------|
| Monster Spawner | `spawner`  | Block & Item | `block.minecraft.spawner` |

| Name         | Identifier    |
|--------------|---------------|
| Block entity | `mob_spawner` |

Bedrock Edition:

| Name            | Identifier    | Numeric ID | Form                       | Item ID[i 1]   | Translation key         |
|-----------------|---------------|------------|----------------------------|----------------|-------------------------|
| Monster Spawner | `mob_spawner` | `52`       | Block & Giveable Item[i 2] | Identical[i 3] | `tile.mob_spawner.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

| Name         | Savegame ID  |
|--------------|--------------|
| Block entity | `MobSpawner` |

### Block data
A monster spawner has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format

- Block entity data
	- 
	- Tags common to all block entities
	- 
	- Tags common to monster spawner and minecart with monster spawner

Bedrock Edition:

SeeBedrock Edition level format/Block entity format.
## Notes
1. ↑Like leaves, this block diffuses sky light only from directly above.

