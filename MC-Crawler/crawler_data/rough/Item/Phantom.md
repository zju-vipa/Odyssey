# Phantom
Phantoms are flying undead hostile mobs that spawn in the night sky when the player has not laid in a bed or died for three or more in-game days. They attack by diving at the player from the sky to bite them.

## Contents
- 1 Spawning
	- 1.1 Bedrock Edition
	- 1.2 Java Edition
- 2 Drops
	- 2.1 On death
- 3 Behavior
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
	- 11.1 Screenshots
	- 11.2 Development images
	- 11.3 Concept artwork
	- 11.4 In other media
- 12 References
- 13 External links

## Spawning
Two phantoms at night.
Phantoms spawn unless the game rule doInsomnia is set to false. The spawning mechanics differ between Java and Bedrock editions. In both editions, they spawn in the Overworld above the player if the "Time Since Last Rest" statistic is at least 1 hour (72000 ticks or 3 in-game days).[verify] This statistic is reset when the player dies or enters a bed. Furthermore, the player must not have a block overhead that blocks light in any way; for example, leaves prevent phantoms from spawning as they have a light opacity of 2, but glass does not, as its light opacity is 0. Phantoms do not spawn in Spectator mode,‌[JE  only] but they do spawn in Creative mode.[1]

### Bedrock Edition
Phantom spawning is similar to other monsters spawning: the spawn location must have a light level of 7 or less, and spawns are limited by the monster population cap. Phantoms are also subject to a density cap of 5. Phantom spawn attempts are made on surface blocks throughout the same spawn radius as other monsters. However, when a phantom spawn attempt succeeds the phantom appears somewhere in a 21×15×21 cube centered 28 blocks above the player instead of at the block where the spawn attempt occurred.

### Java Edition
Phantoms attempt to spawn every 1–2 minutes. They spawn only if it is night or a thunderstorm is happening, the player is above sea level (y=64) with sky access, and the local difficulty is greater than a randomly chosen value between 0.0 and 3.0. The formula x−72000⁄x represents the chance of a successful spawn, where x is the number of ticks since the player last entered a bed or died. This roughly comes to a 1⁄4 (25.0%) chance on day 4, a 2⁄5 (40.0%) chance on day 5, a 3⁄6 (1⁄2) (50.0%) chance on day 6, 4⁄7 (about 57.1%) chance on day 7, and so on.

If all conditions are met, a group of phantoms attempt to spawn 20–34 blocks above the player, and off to the side by a taxicab distance of up to 10 blocks. The number of phantoms spawned is 1-2 in Easy difficulty, 1-3 in Normal, and 1-4 in Hard. Phantoms can spawn inside buildings, if the player is outside and the building is both near enough and the building has a large enough cavity for them to spawn inside.

Phantoms are counted toward the hostile mob cap, but they don't adhere to it when spawning.[2] Their spawning mechanic is based on the location of players in the world rather than by chance, unlike regular mob spawning. Phantom spawning is completely independent of the biome, meaning they can spawn in biomes that normally prevent hostile mob spawning such as mushroom fields[3] and the void.[4] The number of phantoms which spawn indirectly increase in number every consecutive night a player hasn't entered a bed as there is a higher chance that phantoms spawn every time there is a spawn attempt. They then stop spawning when the player lies down in bed.

## Drops
### On death
| Item |                  | Roll Chance | Quantity (Roll Chance) |           |            |             |
|------|------------------|-------------|------------------------|-----------|------------|-------------|
|      |                  |             | Default                | Looting I | Looting II | Looting III |
|      | Phantom Membrane | 100%[d 1]   | 0–1                    | 0–2       | 0–3        | 0–4         |

1. ↑Dropped only when kill credit is given to the player

- 5 when killed by the player or a tamed wolf.

## Behavior
A phantom swooping at the player. In addition, a spider is stalking the player and sheep can be seen in the background.
When idle, phantoms fly around in a roughly circular pattern within 15 to 25 blocks of a player horizontally and within 24 to 35 blocks of a player vertically. They leave a trail of gray smoke while they fly. Their movement speed is one of the fastest of any mob, up to 20 blocks per second. They have a large search radius, targeting and following players from 64 blocks away. Once every 10-20 seconds‌[BE  only] or every 8-12 seconds‌[JE  only] they swoop down or up quickly to attack. If stopped or hurt during this action, the phantom retreats back to its original elevation. When a path to its original elevation is obstructed by a block, the phantom continues attempting to return to its original elevation until it either attacks or moves out from under the block. Phantoms do not attack an exposed player sleeping in a bed. 

Phantoms can move through water at their normal speed. In Bedrock Edition, a phantom underwater attempts to fly to the surface, and dies from drowning after 20 seconds if trapped underwater. Phantoms do not drown in Java Edition.

A phantom's body disappears when under the Invisibility effect, but its eyes and smoke particles are still visible.

Cats hiss at phantoms that are currently attacking players, and phantoms try to stay at least 16 blocks away from them. In Bedrock Edition, phantoms also avoid ocelots in the same manner.

Being an undead mob, they are: 

- damaged by the status effectInstant Healthand healed by the status effectInstant Damage.
- unaffected by the status effectsRegenerationandPoison.
- ignored by thewither.
- affected by theSmiteenchantment.
- unable to swim inwater, but do not drown‌[JE  only].
- a threat toarmadillos, causing them to hide in their shell.‌[upcoming: JE 1.20.5 & BE 1.20.80]

Like zombies and skeletons, phantoms burn in sunlight. They burn even when equipped with helmets through commands.[5]

## Data values
### ID
Java Edition:

| Name    | Identifier | Entity tags                                                                                                                                         | Translation key            |
|---------|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|
| Phantom | `phantom`  | `can_breathe_under_water`<br/>`fall_damage_immune`<br/>`ignores_poison_and_regen`<br/>`inverted_healing_and_harm`<br/>`undead`<br/>`wither_friends` | `entity.minecraft.phantom` |

Bedrock Edition:

| Name    | Identifier | Numeric ID | Translation key       |
|---------|------------|------------|-----------------------|
| Phantom | `phantom`  | `58`       | `entity.phantom.name` |

### Entity data
Phantoms have entity data associated with them that contains various properties.

Java Edition:

Main article: Entity format
- Entity data
	- 
	- Tags common to all entities
	- 
	- Tags common to all mobs
	- AX: The phantom, when not actively attacking, attempts to circle around X,Y,Z =AX,AY,AZ. Appears to reset to a point above the target player every time the phantom flies up after a swoop. Set to spawn location if not specified.
	- AY: SeeAX.
	- AZ: SeeAX.
	- Size: The size of the phantom. Ranges from0to64, similar toslimes. Unlike slimes, phantoms always have a constant 20× 10HP, and deal 6+Sizedamage. Naturally spawned phantoms are always size 0.

Bedrock Edition:

SeeBedrock Edition level format/Entity format.
