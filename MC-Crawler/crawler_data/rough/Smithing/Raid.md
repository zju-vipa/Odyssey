# Raid
A raid is an ominous event in which waves of various mobs, mainly illagers, spawn and attack a village. It is triggered when a player with the Raid Omen stays in a village and the effect ends.

## Contents
- 1 Spawning
- 2 Behavior
	- 2.1 Starting
	- 2.2 Joining
	- 2.3 Illager
	- 2.4 Captains
	- 2.5 Raid wave spawning
	- 2.6 Raid wave composition
		- 2.6.1 Java Edition
		- 2.6.2 Bedrock Edition
	- 2.7 Loot
		- 2.7.1 In Java Edition
		- 2.7.2 In Bedrock Edition
	- 2.8 Raid Omen
	- 2.9 Ending
	- 2.10 Villagers
		- 2.10.1 Gifts
	- 2.11 Witches
	- 2.12 Mobs not counted
	- 2.13 Expiring
- 3 Sounds
- 4 NBT structure
- 5 Achievements
- 6 Advancements
- 7 History
- 8 Issues
- 9 Trivia
- 10 Gallery
	- 10.1 Renders
	- 10.2 Textures
	- 10.3 Screenshots
- 11 See also
- 12 References

## Spawning
A player with the Bad Omen status effect triggers a raid upon entering a chunk with at least one villager and a claimed bed, or one of the 8 chunks surrounding it in a square. In Java Edition, a villager with a claimed bell or job site block can also trigger a raid, even if no claimed beds are present.

Bad Omen is obtained when a player kills an illager captain, which can be found at pillager outposts, woodland mansions, in patrols or during raids, as long as they are killed outside the raid range. If a player kills multiple captains in Java Edition, the Bad Omen accumulates up to Bad Omen V, causing members of the raiding party to have an increased chance of having enchanted weapons. Killing a patrol captain gives 1–5 Bad Omen levels, while killing an outpost captain always gives 1 level. In Bedrock Edition, the Bad Omen effect does not stack by killing multiple captains.

Raids can be triggered in the Overworld and the End, but in Java Edition, raids cannot be triggered in the Nether.[1]

In Java Edition, raids can be disabled by setting the game rule disableRaids to true.

## Behavior
### Starting
In Java Edition, any subchunk containing a claimed POI (point of interest: a bed, job site, or bell) counts as a village. When a player with Bad Omen enters a 3×3×3 subchunk region around a village, the effect disappears and the raid starts. The raid center is initially the average position of all claimed POIs within 64 block radius of the player when the raid triggers. A bossbar labeled "Raid" appears and begins charging taking 15 seconds to complete; a villager runs to ring the bell and all other villagers within 96 blocks (spherical) from the raid center start panicking untill the bar is full. The bossbar is visible to players up to 96 blocks away (spherical) from the raid center. The bar is red and represents the total remaining health of the raid mobs (each segment is 1/10 of the bar). The number of mobs still alive displays when there are fewer than three. Raid waves spawn some distance away from the raid center and navigate toward it. A horn sounds at the start of each wave, from the direction of the wave spawn and 13 blocks away from the player. Raid waves try to spawn in the same place, unless a player is too close. Each subsequent wave is larger, with more mobs, including pillagers, witches, evokers, ravagers, and vindicators. If during the course of the raid, all the POIs inside the subchunk around the raid center are lost (either because the villagers are killed or the blocks themselves are somehow destroyed), the raid center moves to the center of the nearest subchunk that still counts as a village within the surrounding 5×5×5 subchunk region (if there are none, the raid ends in defeat for the player).

In Bedrock Edition, when a player with Bad Omen enters a 64×23×64 region around a village center (technically 1.12 blocks below the center), the effect disappears and the raid starts. A bossbar labeled "Raid" appears and begins charging. The bossbar is visible in a 128×88×128 region around the village center (technically 1.12 blocks below the center). The bar is red, and represents the number of remaining mobs. While a wither is already present in the village and a raid starts, the bar is red and black. The number of mobs still alive displays when there are fewer than three. A horn sounds at the start of each wave, and plays again at intervals until the wave has been defeated, or the player has lost. The horn plays from the direction of one of the illagers, which can help players locate it. The bell rings while the bossbar charges. Each subsequent wave is larger, with more mobs, including pillagers, witches, evokers, ravagers, and vindicators.

### Joining
Illagers, ravagers and witches not spawned as part of the raid (e.g. from a patrol) may join the raid and be counted by the bossbar, provided they are within 96 blocks of the raid center. 

In Java Edition, illusioners can also join the raid. Raid captains may also join and can trigger a new raid when killed far enough from the village. Raiders leave the raid if they are more than 112 blocks away from the raid center or haven't seen action in a while.

### Illager
Illagers have exclusive behavior during raids. 

In Java Edition, vindicators in a raid take the initiative to open and close doors to search for villagers. They can sometimes break a wooden door in Normal [verify] or Hard difficulty if they cannot open the door normally. Evokers and illusioners gain extra movement speed without any effects. This causes evokers to sprint much faster than the player. Evokers exhibit normal attack behavior, but if they do not have a target, they sprint back and forth.

In Bedrock Edition, a vindicator spawned in a raid gains the ability to break doors in Normal difficulty, but does not actively seek doors. They try to break the door only when passing by.

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



#### Bedrock Edition
In Bedrock Edition, the number of waves depends on difficulty, regardless of Bad Omen level without any additional waves. There are three waves in Easy difficulty, five in Normal, and seven in Hard. They spawn with enchanted weapons at level 5 on Easy and at levels 5-19 in other difficulties. There are no attempts to spawn additional mobs in any difficulty.

| Mobs             | Wave 1 | Wave 2 | Wave 3    | Wave 4 | Wave 5      | Wave 6 | Wave 7    |
|------------------|--------|--------|-----------|--------|-------------|--------|-----------|
| Pillager         | 4      | 3      | 3         | 3      |             | 5      |           |
| Vindicator       |        | 2      |           |        | 4           | 2      | 6         |
| Ravager          |        |        | 1         |        | 1           |        |           |
| Witch            |        |        |           | 3      |             |        | 1         |
| Evoker           |        |        |           |        | 1           | 1      | 2         |
| Ravager+Pillager |        |        |           |        | 1           |        | 1         |
| Ravager+Evoker   |        |        |           |        |             |        | 1         |
| Total mobs       | 4      | 5      | 4         | 6      | 7           | 8      | 11        |
| Overall total    |        |        | 13 (Easy) |        | 26 (Normal) |        | 45 (Hard) |

### Loot
All mobs in a raid drop their own regular loot.

** Special Drops **
The raid captain drops

- 1Ominous Banner

#### In Java Edition
Pillagers, vindicators, and evokers drop their regular loot.

#### In Bedrock Edition
In addition to regular loot, pillagers and vindicators can drop:

- 0-1Emerald

Additionally, depending on difficulty, they have a 65% chance of dropping on Easy and Normal, while 80% chance of dropping on Hard:

- 0-1Emerald(10⁄39chance)
- 2-3Emerald(5⁄39chance)
- 4-5Emerald(2⁄39chance)
- 1Enchanted Book(2⁄39chance)
- 1Iron Axe(5⁄78chance)
- 1Iron Shovel(5⁄78chance)
- 1Iron Pickaxe(5⁄78chance)
- 1Iron Sword(5⁄78chance)
- 1Iron Helmet(5⁄78chance)
- 1Iron Chestplate(5⁄78chance)
- 1Iron Leggings(5⁄78chance)
- 1Iron Boots(5⁄78chance)

Note:

- Iron equipment from raider drops has 50% chance of being enchanted with random enchantment(s) at a low-to-medium level.[more information needed]
- Iron equipment from raider drops is always damaged.
- Enchanted books from raider drops have random enchantments at a high level, including treasure enchantments (but notSoul SpeedorSwift Sneak).[more information needed]
- Emerald is both a regular raid drop and an additional drop.
	- Only emerald drops are affected by looting enchantment, increased by 1% per looting level.

In Java Edition, villagers give the player extra loot (gifts) after the raid, while in Bedrock Edition, the illagers drop extra loot when killed.

### Raid Omen
Main articles: Bad Omen and Raid Omen
In Java Edition, the Bad Omen status effect level of the player who triggered the raid also affects the raid mechanism. When the Bad Omen level is higher than one, an additional wave spawns with the same strength as the final wave. With a higher level of Bad Omen to a raid, the illagers in the raid have a higher chance of being equipped with enchanted weapons. The Bad Omen transforms into Raid Omen in which players can drink milk to remove the Raid Omen effect or leave the village before the effect ends. In Bedrock Edition, Bad Omen does not affect the enchanted weapons.

### Ending
If the attacked village no longer registers as a village (i.e. all villagers were killed or all claimed bed, bell, and profession blocks were destroyed), the raid ends, the Raid bar displays "Raid - Defeat", and all of the illagers celebrate: the evokers, pillagers and vindicators raise their hands, the pillagers jump up and down‌[JE  only] or raise their hands,‌[BE  only] and all of them emit "celebration sounds".

Java Edition:

| Sounds |                   |                   |                               |                               |                                         |        |         |                          |
|--------|-------------------|-------------------|-------------------------------|-------------------------------|-----------------------------------------|--------|---------|--------------------------|
| Sound  | Subtitles         | Source            | Description                   | Resource location             | Translation key                         | Volume | Pitch   | Attenuation<br/>distance |
|        | Pillager cheers   | Hostile Creatures | When a pillager wins a raid   | `entity.pillager.celebrate`   | `subtitles.entity.pillager.celebrate`   | 1.0    | 0.8-1.2 | 16                       |
|        | Vindicator cheers | Hostile Creatures | When a vindicator wins a raid | `entity.vindicator.celebrate` | `subtitles.entity.vindicator.celebrate` | 1.0    | 0.8-1.2 | 16                       |
|        | Ravager cheers    | Hostile Creatures | When a ravager wins a raid    | `entity.ravager.celebrate`    | `subtitles.entity.ravager.celebrate`    | 1.0    | 0.8-1.2 | 16                       |
|        | Evoker cheers     | Hostile Creatures | When an evoker wins a raid    | `entity.evoker.celebrate`     | `subtitles.entity.evoker.celebrate`     | 1.0    | 0.8-1.2 | 16                       |
|        | Witch cheers      | Hostile Creatures | When a witch wins a raid      | `entity.witch.celebrate`      | `subtitles.entity.witch.celebrate`      | 1.0    | 0.8-1.2 | 16                       |

Bedrock Edition:

| Sounds |                   |                               |                                   |        |         |
|--------|-------------------|-------------------------------|-----------------------------------|--------|---------|
| Sound  | Source            | Description                   | Resource location                 | Volume | Pitch   |
|        | Hostile Creatures | When a pillager wins a raid   | `mob.pillager.celebrate`          | 1.0    | 0.8-1.2 |
|        | Hostile Creatures | When a vindicator wins a raid | `mob.vindicator.celebrate`        | 1.0    | 0.8-1.2 |
|        | Hostile Creatures | When a ravager wins a raid    | `mob.ravager.celebrate`           | 1.0    | 0.8-1.2 |
|        | Hostile Creatures | When an evoker wins a raid    | `mob.evocation_illager.celebrate` | 1.0    | 0.8-1.2 |
|        | Hostile Creatures | When a witch wins a raid      | `mob.witch.celebrate`             | 1.0    | 0.8-1.2 |

If all illagers are killed in the final wave, any player who has killed an illager in the raid receives the Hero of the Village effect at the same level as the Bad Omen level of the raid. The villagers shoot off fireworks, and the Raid bar displays "Raid - Victory". The Hero of the Village effect activates only when the player is in the village where the raid was defeated, and the effect wears off if the player leaves the village.

Raids cannot end naturally if at least one baby villager remains, because illagers are passive to baby villagers, except for the “Johnny” vindicator.‌[Bedrock Edition  only]

In some cases a raid ends after a set amount of time, if all left over raiders cannot move.

### Villagers
In Java Edition during a raid, villagers emit "sweat particles". At least one villager rushes to the village meeting point and rings the bell to alert other villagers to get inside their houses during the warmup of an upcoming raid wave. 

After successfully defending a village from a raid, the villagers emerge from their houses and celebrate, by setting off firework rockets and cheering, although villagers do not have a celebrate sound unlike the illagers.

#### Gifts
Villagers give players gifts after the raid in Java Edition. Villagers throw items at the player that are related to their profession. After throwing a gift a villager has a cooldown between 30 seconds and 5 minutes before they can throw another gift at the player. That means the more villagers the player has, the more gifts they receive.

### Witches
In Java Edition, witches participating in a raid often help other illagers by splashing a Potion of Regeneration or Healing. Witches do not attack villagers and do not throw harmful potions at them.[2]

In Bedrock Edition, witches participating in a raid do now heal other illagers and attack iron golems. Witches are passive toward villagers, but their harmful splash potions might hit a villager by accident.

### Mobs not counted
Vexes summoned by evokers do not count as part of the raid. Killing them has no effect on the raiding bar, and the raid can end in victory even if there are vexes remaining.

### Expiring
If a raid goes on for 48,000 ticks (40 minutes in real time) the raid bossbar disappears, and a message appears saying "raid expired". Although, any living illagers stay until they are killed.

## NBT structure
Main article: raids.dat format
