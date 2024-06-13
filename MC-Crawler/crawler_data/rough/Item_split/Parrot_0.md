# Parrot
A parrot is a tameable passive mob that spawns in jungle biomes. Parrots imitate sounds of nearby monsters and can perch on the player's shoulders.

## Contents
- 1 Spawning
- 2 Drops
	- 2.1 On death
- 3 Behavior
	- 3.1 Sitting on a shoulder
	- 3.2 Imitating sounds
	- 3.3 Dancing
- 4 Sounds
	- 4.1 Generic
	- 4.2 Imitations
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
		- 11.1.1 Sitting
		- 11.1.2 Dancing
		- 11.1.3 Sitting on the player
	- 11.2 Screenshots
	- 11.3 In other media
- 12 References
- 13 External links

## Spawning
Parrots naturally spawn in groups of 1–2 in jungles, sparse jungles‌[BE  only] and bamboo jungles above logs, leaves or grass blocks.

Unlike most passive mobs, parrots cannot be bred.

## Drops
### On death
| Item |         | Roll Chance | Quantity (Roll Chance) |           |            |             |
|------|---------|-------------|------------------------|-----------|------------|-------------|
|      |         |             | Default                | Looting I | Looting II | Looting III |
|      | Feather | 100%        | 1–2                    | 1–3       | 1–4        | 1–5         |

1–3 experience orbs are dropped when parrots are killed by a player or a tamed wolf.

## Behavior
Parrots fly around idly under normal circumstances, landing frequently to rest.[1] They take interest in any nearby mobs, including those that are hostile to them, and follow them around closely. When attacked, they rapidly fly upward several blocks to flee.

Parrots also flap their wings to swim, and to slow their falls and prevent fall damage.

Parrots can be tamed by feeding them wheat seeds, melon seeds, pumpkin seeds, beetroot seeds or torchflower seeds, with each item fed having a 1⁄10 chance of successfully taming them. Once tamed, interacting with a parrot makes it sit down and stand up.

A tamed parrot follows the player unless told to sit, and teleports if there is a distance of 12 blocks between it and the player. A death message is displayed to a parrot's owner upon its death. 

In Java Edition, attempting to feed a parrot a cookie instantly kills it, emitting Poison particles as it dies. In Bedrock Edition, feeding a cookie to a parrot gives it Fatal Poison instead. This is a reference to the fact that chocolate is toxic to parrots.

### Sitting on a shoulder
Kai with a parrot on their shoulder.
A tamed parrot on the ground can be made to perch on its player's shoulder by moving through the parrot. On its own, a tamed parrot can also fly to and perch on the player's shoulder, unless it has been told to sit. A player can have one parrot on each shoulder. Parrots always prefer a player's left shoulder first, if it is empty.

A parrot dismounts its player when the player:

- does not land on a high-enough surface (1⁄2block up or higher)
- drops off a ledge of higher than3⁄4of a block
- takes damage
- submerges the player's feet into water of any height
- starts drowning
- sleeps on a bed
- submerges the player's head inlava(the parrot dismounts and burns even if the player hasFire Resistance)

Parrots on a shoulder always look in the same direction the player's head is looking.

A parrot on a shoulder cannot take any damage but may get hurt as soon as it dismounts, as when dismounting a player submerged in lava.

A parrot sitting on the shoulder appears in the inventory interface.

In Bedrock Edition, a parrot sitting on a shoulder prevents the player from entering a nether portal.[2]

### Imitating sounds
Parrots imitate the idle sounds of nearby hostile mobs and certain neutral mobs (including the hiss of creepers but excluding guardians and elder guardians); they have a detection range of 20 blocks. The sound produced by the parrots is simply the same sound as the mob being mimicked at a higher pitch. Occasionally, a parrot may imitate sounds of mobs that are not in the area.[3]

### Dancing
Parrots dance near a jukebox if a music disc is inside it. Parrots even have the ability to dance while on a player's shoulder.‌[BE  only] This is a reference to the Party Parrot meme.[4] The game does not seem to have any real way to determine when the music ends, though; as long as the disc remains in the jukebox, the parrot continues dancing even after the music stops.[5]

The dancing radius is 3 blocks from the jukebox. If they dance and then fly beyond this radius, they stop dancing. A parrot does not dance if the music disc was inserted prior to it spawning, dismounting or being within the 3 blocks range.[6]

## Data values
### ID
Java Edition:

| Name   | Identifier | Entity tags          | Translation key           |
|--------|------------|----------------------|---------------------------|
| Parrot | `parrot`   | `fall_damage_immune` | `entity.minecraft.parrot` |

Bedrock Edition:

| Name   | Identifier | Numeric ID | Translation key      |
|--------|------------|------------|----------------------|
| Parrot | `parrot`   | `30`       | `entity.parrot.name` |

### Entity data
Parrots have entity data associated with them that contain various properties.

Java Edition:

Main article: Entity format
- Entity data
	- 
	- Additional fields for mobs that can be tamed by players
	- 
	- Tags common to all entities
	- 
	- Tags common to all mobs
	- Variant: Specifies the color variant of the parrot, default is 0.


Parrot Variant
Main article: Parrot/DV[edit]

When a parrot is resting on the player's shoulder, it ceases to be a distinct entity and its entity data is stored in the player's ShoulderEntityLeft or ShoulderEntityRight NBT. See also Player.dat format.

Bedrock Edition:

SeeBedrock Edition level format/Entity format.

