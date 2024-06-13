# Mega Spud
The mega spud is a boss mob found in colosseums in 24w14potato.

## Contents
- 1 Spawning
- 2 Drops
	- 2.1 On death
- 3 Behavior
	- 3.1 Peaceful difficulty
- 4 Sounds
- 5 Data values
	- 5.1 Entity data
- 6 History
- 7 Trivia
- 8 Gallery
	- 8.1 Screenshots

## Spawning
One mega spud spawns in each colosseum upon generation. If it can, mega spud always stays in proximity to the place it spawned at.

## Drops
### On death

On death, the mega spud always drops Potatiesh, Greatstaff of the Peasant. It drops 50 xp when killed by a player or tamed wolf.
| Item |                                      | Roll Chance | Quantity (Roll Chance) |           |            |             |
|------|--------------------------------------|-------------|------------------------|-----------|------------|-------------|
|      |                                      |             | Default                | Looting I | Looting II | Looting III |
|      | Potatiesh, Greatstaff of the Peasant | 100%        | 1                      | 1         | 1          | 1           |

## Behavior
Mega spud moves around similarly to a slime. When it detects a player, mega spud starts shooting fireballs at them, like a ghast.

Mega spud has 10 phases, plus the initial "zeroth" phase. When damaged for the first time, it instantly switches to the first phase, but its health remains the same. Each next phase requires dealing 102.4 × 51.2 points of damage to the mega spud.

Whenever a new phase begins, mega spud performs the following actions:

- Creates a shield around itself, similar towither's armor, and becomes invulnerable to all forms of damage, except forvoiddamage and the/killcommand.
- Shrinks by about half a block, and gets slightly faster.
- Drops a number ofcorrupted potato peels.
- Spawns some minions. Number of minions is equal to the number of the started phase. Each next phase has a stronger mob as a minion.
	- Minions are spawned around the spot that the mega spud spawned in. This mechanic uses the same particles and sounds astrial spawners.
- Changes name, as seen on top of the bossbar.

While in the invulnerable state, mega spud reflects every attack that the player does back at them. This is different from how the Thorns enchantment work, because mega spud reflects 100% of the incoming damage: for example, shooting the boss with a bow with Power V instantly kills an unarmored player. Attempting to damage the boss in this state also causes all of its minions to gain the Glowing effect for 10 seconds, which indicates that minions must be defeated first.

If the player dies, current phase is reset, and a new set of minions is spawned.

When all minions from a given phase are killed, mega spud roars angrily and loses its shields. It can then be damaged like a normal mob. Unlike the wither or the ender dragon, mega spud is not immune to status effects, fire, suffocation or drowning.

| Phase | Name                           | Health      | Hitbox size[1](blocks) | Mobs spawned                  | Combined health of all spawned mobs |
|-------|--------------------------------|-------------|------------------------|-------------------------------|-------------------------------------|
| 0     | Potatolord of the Fried Legion | 1024        | 5.20                   | -                             | -                                   |
| 1     | Clucky Contaminator            | 1024-921.6  | 4.68                   | Onechicken                    | 4                                   |
| 2     | Toxic Talon Talus              | 921.6-819.2 | 4.16                   | Twoarmadillos                 | 24                                  |
| 3     | Venomous Vagabond              | 819.2-716.8 | 3.64                   | Threepoisonous potato zombies | 60                                  |
| 4     | Arachnid Administrator         | 716.8-614.4 | 3.12                   | Fourspiders                   | 64                                  |
| 5     | Spud Scavenger Stray           | 614.4-512   | 2.60                   | Fivestrays                    | 100                                 |
| 6     | Creeper Kingpin                | 512-409.6   | 2.08                   | Sixcreepers                   | 120                                 |
| 7     | Poisonous Piglin Potentate     | 409.6-307.2 | 1.56                   | Sevenpiglin brutes            | 350                                 |
| 8     | Ghastly Ghoulmaster            | 307.2-204.8 | 1.04                   | Eightghasts                   | 80                                  |
| 9     | Plaguewhale Patriarch          | 204.8-102.4 | 0.52                   | Nineplaguewhale slabs         | 720                                 |
| 10    | Giant Green Globule            | 102.4-0     | 0.52[2]                | Tengiants                     | 1000                                |


↑ Hitbox is always a cube.

↑ Size does not change in the last phase.


Adding the 1024 points of boss health to combined health of all mobs that mega spud spawns, player must deal 3546 points of damage in order to defeat the boss.

Mega spud can enter minecarts, and from phase eight it can also enter boats.

### Peaceful difficulty
On Peaceful, mega spud does not despawn, but is harmless to the player. Any minions beyond phase 2 despawn immediately, so mega spud loses its shield quickly after gaining it.

## Data values
| Name                                      | Identifier | Translation key            |
|-------------------------------------------|------------|----------------------------|
| Mega Spud, Potatolord of the Fried Legion | mega_spud  | entity.minecraft.mega_spud |

### Entity data
Mega spuds have entity data associated with them that contain various properties.

Main article: Entity format

 Entity data
Tags common to all entities
Tags common to all mobs
 Size: How big the mega spud is. Mega spuds summoned using /summon default to 0, while naturally spawned mega spuds default to 8.
 wasOnGround: Whether this mega spud is on the ground. Is used in conjunction with OnGround to create landing sounds and particles.
 homeX: The X coordinate of this mega spud's home.
 homeY: The Y coordinate of this mega spud's home.
 homeZ: The Z coordinate of this mega spud's home.


