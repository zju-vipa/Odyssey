### Captains
In Java Edition, when a wave captain is killed, other nearby illagers in the raid try to pick up any ominous banners on the ground until a new wave captain is made; the illager that retrieves the banner becomes the new wave captain. 

A player does not receive the Bad Omen effect when killing the patrol captain within a village. The captain is always a vindicator upon spawning, if possible.

### Raid wave spawning
The raid spawns several waves of raider mobs. If a raid wave begins while an illager is somehow already present inside the village, the wave does not spawn at all and entirely fills up with however many existing illagers there are; When these illagers are defeated, the raid resumes as normal. In Java Edition, to find a valid spawn target location at the beginning of each raid wave, there are 3 spawn attempt phases with 20 attempts per phase. For each attempt, a random location is chosen a certain radius away from the raid center (64 blocks in the first phase, 32 in the second, and 0 in the third) at a random horizontal angle, with fractional results rounded down. Additionally, a random 0–4 is added to X and Z coordinates. In Bedrock Edition, the exact spawning mechanics are unknown, but the raid can spawn in the 128×32×128 region around the village center. In effect, the three spawn attempt areas are two rings and a 5×5 square. The target height is always on top of the topmost non-air block. For spawn location to be valid, the block underneath must have a solid opaque top face or be snow. 

Valid spawn blocks in Java include full blocks, upside-down slabs/stairs, soul sand, and packed/blue ice, but not glass, leaves, some light-emitting blocks (they do spawn on crying obsidian and jack-o-lantern), trapdoors, regular ice, bottom slabs, or carpet. In Bedrock Edition the raid can spawn on any block except leaves and scaffolding. Any light level is fine and player proximity does not matter. Waves tend to spawn near or at the last location they spawned at. The location must be in an entity-ticking chunk. If the game is unable to find a spawn location, the raid ends. Once a valid location is found, the horn sounds and all raider mobs for that wave spawn there at once. They then spread out and move toward the village. Once all raiders are killed, there is a 15-second cooldown before the next wave. However, if the last raider happens to move outside a spherical radius of 112 blocks from raid center, or the entire wave spawns outside that radius (which can happen with large differences in Y-level), then the next wave spawns immediately. Raiders that are part of a raid do not despawn naturally and do not contribute to the mob cap, but resume despawning once the raid is over or they leave it.

### Raid wave composition
#### Java Edition
The number of waves depends on difficulty. There are 3 waves in Easy difficulty, 5 in Normal, and 7 in Hard. In Hard, there is a chance of 1 additional pillager and/or vindicator spawning for each wave.  If the player's Bad Omen effect is level II or higher, one additional wave spawns (e.g. 4 in Easy, 6 in Normal, and 8 in Hard) with the same strength as the final wave. Raiders have an increased chance of spawning with enchanted items with higher Bad Omen levels; a 10% chance starting at Bad Omen II and up to a 75% chance at Bad Omen V.

** Easy difficulty **
When triggered with Bad Omen I, illager weapons are unenchanted. Bad Omen levels II through V each increases the possibility of low-level enchantments. There is a 25% chance of spawning an additional pillager from 3 pillagers each wave, totaling 4 pillagers on waves 2, 3, and the extra wave. There is a 25% chance of spawning a vindicator each wave, starting wave 3.

| Mob           | Wave 1 | Wave 2 | Wave 3  | Extra Wave |
|---------------|--------|--------|---------|------------|
| Pillager      | 4 - 5  | 3 - 4  | 3 - 4   | 3 - 4      |
| Vindicator    |        | 2 - 3  | 0 - 1   | 0 - 1      |
| Ravager       |        |        | 1       | 1          |
| Total mobs    | 4 - 5  | 5 - 7  | 4 - 6   | 4 - 6      |
| Overall total |        |        | 13 - 18 | 17 - 24    |

** Normal difficulty **
There's a 50% chance of spawning either a additional pillager from 3 pillagers per wave, and/or a vindicator on each wave. Witches can also spawn with a 50% chance on waves 3 and 5, and 3 witches on wave 4. A ravager also spawns at wave 3, but if there is an extra wave, there's a chance of 2 ravagers in the extra wave. Only wave 5 spawns a pillager-ravager jockey.

| Mob              | Wave 1 | Wave 2 | Wave 3 | Wave 4 | Wave 5  | Extra Wave |
|------------------|--------|--------|--------|--------|---------|------------|
| Pillager         | 4 - 5  | 3 - 4  | 3 - 4  | 4 - 5  | 4 - 5   | 4 - 5      |
| Vindicator       | 0 - 1  | 2 - 3  | 0 - 1  | 1 - 2  | 4 - 5   | 4 - 5      |
| Ravager          |        |        | 1      |        |         | 1 - 2      |
| Witch            |        |        | 0 - 1  | 3      | 0 - 1   | 0 - 1      |
| Evoker           |        |        |        |        | 1       | 1          |
| Ravager+Pillager |        |        |        |        | 1       |            |
| Total mobs       | 4 - 6  | 5 - 7  | 4 - 7  | 8 - 10 | 10 - 13 | 10 - 14    |
| Overall total    |        |        |        |        | 31 - 43 | 41 - 57    |

** Hard difficulty or Hardcore gamemode **
There are at least 3 pillagers each wave except wave 7 on. However, waves 1, 4, 5, and 6 spawn at least 4 pillagers, but each wave has a 50% chance to spawn additional pillagers. A different minimum number of pillagers spawn from wave 5 onward, and they have a 50% chance to spawn extras on each wave also. At least 1 vindicator spawns starting at wave 4, but there is a range from as few as 0 to up to 7 across the waves.  Wave 4 spawns 3 witches, and from wave 7 on, at least one witch spawns. Waves 3, 5, and 6 also have a 50% chance to spawn witches. There are also ravager-illager jockeys spawning in wave 5, and wave 7 on.

| Mob                | Wave 1 | Wave 2 | Wave 3 | Wave 4 | Wave 5  | Wave 6 | Wave 7  | Extra Wave |
|--------------------|--------|--------|--------|--------|---------|--------|---------|------------|
| Pillager           | 4 - 6  | 3 - 5  | 3 - 5  | 4 - 6  | 4 - 6   | 4 - 6  | 2 - 4   | 2 - 4      |
| Vindicator         | 0 - 2  | 2 - 4  | 0 - 2  | 1 - 3  | 4 - 6   | 2 - 4  | 5 - 7   | 5 - 7      |
| Ravager            |        |        | 1      |        |         |        |         |            |
| Witch              |        |        | 0 - 1  | 3      | 0 - 1   | 0 - 1  | 1 - 2   | 1 - 2      |
| Evoker             |        |        |        |        | 1       | 1      | 2       | 2          |
| Ravager+Pillager   |        |        |        |        | 1       |        |         |            |
| Ravager+Vindicator |        |        |        |        |         |        | 1       | 1 - 2      |
| Ravager+Evoker     |        |        |        |        |         |        | 1       | 1          |
| Total mobs         | 4 - 8  | 5 - 9  | 4 - 9  | 8 - 12 | 10 - 15 | 7 - 12 | 13 - 18 | 13 - 19    |
| Overall total      |        |        |        |        |         |        | 51 - 83 | 64 - 102   |



