# Hoglin
A hoglin is a breedable hostile mob found in the Nether, and a source of porkchops and leather. Hoglins are repelled by warped fungi that is placed in the world as well as active nether portals and respawn anchors. It attacks by thrusting its tusks upward, which can also launch its target a short distance into the air.

Baby hoglins behave similarly, but have a much weaker attack (the weakest attack in the game) with normal knockback, and flee when hit.

## Contents
- 1 Spawning
- 2 Drops
	- 2.1 On death
- 3 Behavior
	- 3.1 Hostility
	- 3.2 Baby hoglins
	- 3.3 Zombification
	- 3.4 Breeding
- 4 Sounds
- 5 Data values
	- 5.1 ID
	- 5.2 Entity data
- 6 Achievements
- 7 Advancements
- 8 History
- 9 Issues
- 10 Trivia
- 11 Gallery
	- 11.1 Renders
		- 11.1.1 Zombification
	- 11.2 Screenshots
	- 11.3 Development images
	- 11.4 In other media
- 12 See also
- 13 References
- 14 External links

## Spawning
Hoglins are found in herds of 3–4 in crimson forests, respawning over time. They can spawn at any light level and on most solid blocks other than nether wart blocks and shroomlights. 

Hoglins spawn in certain types of bastion remnants upon structure generation. They spawn frequently in the hoglin stable variant (specifically the large and small stables in the "lower" area, but never in the "upper" area with ramparts), and sometimes in the main "bridge entrance" at the upper half of the rampart in the bridge variant. Similar to the piglins and piglin brutes there, these hoglins never despawn.

20% of hoglins spawn as babies.

Hoglins spawn in Peaceful mode, but are passive to players.

## Drops
### On death
| Item |                   | Roll Chance | Quantity (Roll Chance) |           |            |             |
|------|-------------------|-------------|------------------------|-----------|------------|-------------|
|      |                   |             | Default                | Looting I | Looting II | Looting III |
|      | Raw Porkchop[d 1] | 100%        | 2–4                    | 2–5       | 2–6        | 2–7         |
|      | Leather           | 100%        | 0–1                    | 0–2       | 0–3        | 0–4         |

1. ↑Dropped as cooked porkchop if on fire when killed.

- 5‌[JE  only]or1–3‌[BE  only]if killed by aplayeror tamedwolf.

Baby hoglins drop only experience when killed, at the same rate as adult hoglins. They are also the only baby animals that drop experience.

## Behavior
Hoglins avoid being within 7 blocks of warped fungi (including in a flower pot), nether portals and respawn anchors. They naturally sink in water and eventually drown.[1] They also sink in lava and are vulnerable to fire damage.[2] Hoglins can be led with a lead despite the fact they are hostile.

### Hostility
Hoglins attack any player within 16 blocks with a reach of 1.9 blocks. An adult knocks its target upward. Players can still be flung even if they block with a shield. Hoglins do not attack a player standing near a block that repels them, but run away from the block unless they have already chosen to attack. Hoglins are 60% resistant to knockback. Unlike other hostile mobs, they do not prevent a player from sleeping.

Similar to piglins and zombified piglins, a player or mob attacking a hoglin provokes all nearby hoglins. Attacking a baby hoglin does not trigger this behavior.

If a piglin attacks a hoglin, all the hoglins in the area retaliate. Hoglins also flee if outnumbered and make retreating sounds. If the piglins are outnumbered by hoglins, they flee and make retreating sounds.

Hoglins that spawn upon generation of bastion remnants are not hunted by piglins.

### Baby hoglins
Baby hoglins also attack the player, dealing much less damage and normal knockback. If the player attacks a baby hoglin, it temporarily flees.

Baby piglins run near and ride baby hoglins. If there are more baby piglins than baby hoglins, the baby piglins occasionally jump on other baby piglins already riding a baby hoglin, with a maximum of 3 stacked on a single baby hoglin.

### Zombification
A hoglin turning into a zoglin. Notice the hair is flattened down.
If a hoglin spawns in or moves to the Overworld or the End, it shakes and then transforms into a zoglin after 15 seconds. The newly-created zoglin gets Nausea I for 10 seconds. This Nausea effect is only decorative and has no effect on the zoglin's behavior. In Java Edition, any lead attached to the hoglin breaks when it converts, even though zoglins are leashable.[3]

### Breeding
Main article: Breeding
Hoglins can be bred with crimson fungi. It takes 5 minutes before the parents can be bred again, and it takes 20 minutes for baby hoglins to mature. Baby hoglins stay near their parents unless they see a player or get attacked, in which case they attack or run away. Feeding a crimson fungus to a baby hoglin reduces the remaining time for it to mature by 10%.

Hoglins cannot be bred when they are running away from warped fungi, respawn anchors or nether portals.

Feeding crimson fungi to a hoglin prevents it from despawning, no matter the breeding is successful or not. The baby hoglin produced by breeding does not despawn either.

Like the killer bunny‌[Java Edition  only], the hoglin is a hostile mob that can be bred.

## Data values
### ID
Java Edition:

| Name   | Identifier | Translation key           |
|--------|------------|---------------------------|
| Hoglin | `hoglin`   | `entity.minecraft.hoglin` |

Bedrock Edition:

| Name   | Identifier | Numeric ID | Translation key      |
|--------|------------|------------|----------------------|
| Hoglin | `hoglin`   | `124`      | `entity.hoglin.name` |

### Entity data
Hoglins have entity data associated with them that contains various properties.

Java Edition:

Main article: Entity format
- Entity data
	- 
	- Additional fields for mobs that can breed
	- 
	- Tags common to all entities
	- 
	- Tags common to all mobs
	- CannotBeHunted: 1 or 0 (true/false) - if true, piglins do not attack the hoglin. Set to true for hoglins spawned as a part of bastion remnants.
	- IsImmuneToZombification: 1 or 0 (true/false) – if true, the hoglin does not transform to a zoglin when in the Overworld andTimeInOverworlddoes not increment.
	- TimeInOverworld: The number of ticks that the hoglin has existed in the Overworld; the hoglin converts to a zoglin when this is greater than 300.

Bedrock Edition:

SeeBedrock Edition level format/Entity format.
