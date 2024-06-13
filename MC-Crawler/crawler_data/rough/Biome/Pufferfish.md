# Pufferfish
Pufferfish are bucketable aquatic mobs found in oceans. Although they never seek out mobs to attack, they defensively inflate themselves when approached too closely by players, axolotls, or non-aquatic mobs, dealing damage and inflicting Poison on them.

## Contents
- 1 Spawning
- 2 Drops
	- 2.1 On death
- 3 Behavior
	- 3.1 Weaknesses
	- 3.2 Defenses
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
	- 11.1 Textures
	- 11.2 Screenshots
	- 11.3 In other media
- 12 See also
- 13 References

## Spawning
In Java Edition, pufferfish spawn in groups of 1-3 in warm, lukewarm, and deep lukewarm ocean biomes, subject to fish spawning requirements. If trying to spawn inside a waterlogged solid block, the pufferfish uses the bigger "puffed" size to determine if it collides with anything solid.

In Bedrock Edition, fish spawn underwater at around 12–32 blocks away from the player in groups of 3–5 in warm ocean biomes, and only on the surface; that is, there must not be a spawnable block above the spawn location with a non-solid block on top. They are considerably rarer than tropical fish, with only 1⁄5 of fish groups or 2⁄9 individual fish (within the warm ocean biome) spawning as pufferfish.

## Drops
### On death
| Item |               | Roll Chance | Quantity (Roll Chance) |           |            |             |
|------|---------------|-------------|------------------------|-----------|------------|-------------|
|      |               |             | Default                | Looting I | Looting II | Looting III |
|      | Pufferfish    | 100%        | 1                      | 1         | 1          | 1           |
|      | Bone Meal(JE) | 5%          | 1                      | 1         | 1          | 1           |
|      | Bone(BE)      | 25%         | 1–2                    | 1–2       | 1–2        | 1–2         |

- 1–3 when killed by aplayeror a tamedwolf.

## Behavior
Pufferfish inflate themselves when approached by the player, most mobs,‌[JE  only] including tripod cameras‌[BE & edu  only] and armor stands.[1][2]

The player may collect a fish by using a water bucket on it, giving the player a bucket of pufferfish. Fish placed with buckets do not despawn naturally. When that fish bucket is used against a block, it empties the bucket, placing water with that fish swimming in it. An empty bucket may be used as well.‌[Bedrock Edition  only]

Unlike other fish, pufferfish don't swim in schools.

### Weaknesses
Like other fish, pufferfish cannot survive out of water. Outside of water, they flop around like guardians for a while until they start suffocating, and then die like squid. In Bedrock Edition they rotate when flopping. Fish cannot swim or breathe in cauldron water.[3]

The Impaling enchantment affects pufferfish due to being aquatic‌[Java Edition  only] or simply being in water‌[Bedrock Edition  only].

### Defenses
A pufferfish inflates when approached by a player in Survival or Adventure mode, a drowned, an axolotl, or any non-water mob within a 5×5×5 volume around the fish, going from unpuffed, then semi-puffed, to fully puffed. Pufferfish are technically passive mobs but going near one when semi-puffed or fully puffed inflicts the player/mob with three or six seconds of Poison based on the inflation level, and touching one in its puffed or semi-puffed form deals damage separate from the Poison. 

Pufferfish also instantly inflate to their fullest form after taking any kind of damage.‌[Bedrock Edition  only] After inflating, they slowly deflate to their normal shape as long as a threat is out of range. If the player/mob leaves the radius while the pufferfish is in its semi-puffed stage, it deflates back to normal.  

Undead mobs are unaffected by the Poison effect, but still, take damage when they come into contact with pufferfish.

A pufferfish inflicting damage to a mob other than creeper and ghast via touching provokes that mob to retaliate.

In Peaceful difficulty, pufferfish do not inflict damage or Poison to player.‌[Java Edition  only]

Pufferfish deal damage to players at a longer distance than to mobs.[4]

## Data values
### ID
Java Edition:

| Name       | Identifier   | Entity tags                                                                                                                   | Translation key               |
|------------|--------------|-------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
| Pufferfish | `pufferfish` | `aquatic`<br/>`axolotl_hunt_targets`<br/>`can_breathe_under_water`<br/>`not_scary_for_pufferfish`<br/>`sensitive_to_impaling` | `entity.minecraft.pufferfish` |

Bedrock Edition:

| Name       | Identifier   | Numeric ID | Translation key          |
|------------|--------------|------------|--------------------------|
| Pufferfish | `pufferfish` | `108`      | `entity.pufferfish.name` |

### Entity data
Pufferfish have entity data associated with them that contains various properties.

Java Edition:

Main article: Entity format
- Entity data
	- 
	- Tags common to all entities
	- 
	- Tags common to all mobs
	- FromBucket: 1 or 0 (true/false) - iftrue, the fish has been released from a bucket.
	- PuffState: A value from 0–2.
		- 0means the fish is deflated
		- 1means it is halfway puffed-up
		- 2means it is fully puffed-up


Bedrock Edition:

SeeBedrock Edition level format/Entity format.
