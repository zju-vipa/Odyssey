# Creeper
A creeper is a common hostile mob that quietly approaches players and then explodes, which can destroy blocks and deal massive amounts of damage. Creepers are a major source of gunpowder as well as the only way to obtain most music discs.

## Contents
- 1 Spawning
- 2 Drops
	- 2.1 On death
- 3 Behavior
	- 3.1 Charged creeper
	- 3.2 Farming
- 4 Sounds
- 5 Data values
	- 5.1 ID
	- 5.2 Entity data
- 6 Achievements
- 7 Advancements
- 8 History
- 9 Issues
- 10 Trivia
	- 10.1 Publicity
		- 10.1.1 Merchandise
		- 10.1.2 Appearances
- 11 Gallery
	- 11.1 Textures
	- 11.2 Screenshots
	- 11.3 In other media
		- 11.3.1 Official media
		- 11.3.2 Merchandise
		- 11.3.3 Other appearances
- 12 References
- 13 External links

## Spawning
Creepers naturally spawn in the Overworld on solid blocks with a light level of 0, except in mushroom fields and deep dark biomes. They spawn individually in Bedrock Edition and in groups of up to four in Java Edition.

In Bedrock Edition, there is a density limit of five creepers in the Overworld's surface.

## Drops
### On death
| Item |                 | Roll Chance | Quantity (Roll Chance) |           |            |             |
|------|-----------------|-------------|------------------------|-----------|------------|-------------|
|      |                 |             | Default                | Looting I | Looting II | Looting III |
|      | Gunpowder       | 100%        | 0–2                    | 0–3       | 0–4        | 0–5         |
|      | Music Disc[d 1] | 100%[d 2]   | 1                      | 1         | 1          | 1           |
|      | Creeper Head    | 100%[d 3]   | 1                      | 1         | 1          | 1           |


↑ The disc is randomly selected from 13, cat, blocks, chirp, far, mall, mellohi, stal, strad, ward, 11, and wait.

↑ Only dropped when killed by a skeleton or stray.

↑ Only dropped when killed by a charged creeper.


- 5experiencepoints, if killed by theplayeror a tamedwolf.

## Behavior
A creeper giving chase.
Creepers chase any player within a 16-block radius. They do not attack any other mob without provocation by being attacked first.

When within 3 blocks of a player, a creeper stops moving, hisses, flashes and expands, and explodes after 1.5 seconds (30 ticks), destroying (and dropping as items) blocks in the area as well as significantly damaging the player. A creeper's detonation can be halted if the player leaves the blast radius, including by knocking it back, going out of the creeper's sight, or if the creeper is killed before the explosion. Assuming the player stays within line of sight, the distance that the player must move in order for a creeper cancel its explosion is 7 blocks, regardless of difficulty. Normal creeper explosions have a power of 3.

In Java Edition, the if the game rule mobExplosionDropDecay is set to false, blocks have a 100% chance of dropping as items instead of being destroyed.

A creeper explodes only if it has an uninterrupted line of sight with the player throughout the entire 1.5-second countdown. As a result, if the creeper does not have line-of-sight with the player, it does not start hissing even at close range, even if the player is attacking it, and a detonation is canceled if it has started. The hissing sound plays in its entirety regardless of whether the explosion happens or not.

Unlike most mobs, the creeper does not have an idle sound, nor does it have unique step sounds. Although it does make normal stepping and swimming sounds, it is hard for players to distinguish those from sounds they make themselves. This makes the approach of a creeper difficult for an unwary player to notice until it starts hissing. 

A creeper jumps down to a player if it can survive the fall. A creeper taking fall damage adds to its swell according to fallDistance * 1.5, up to a maximum of 5 less than the fuse of the creeper. The creeper explodes when the swell equals the fuse, so an explosion occurs soon after landing with higher falls. For example, a creeper falling from greater than 16 blocks can explode 5 ticks after it lands. 

The amount of swell added to creepers upon falling a certain distance
Creepers can climb up ladders, vines, and similar blocks like any other mob, but do not do so intentionally. 

Using a flint and steel or fire charge‌[Java Edition  only] on a creeper forces an explosion.

In Java Edition, the detection range of creepers is reduced by 50% when the player is wearing a creeper head.

Creepers flee from ocelots and cats within a 6-block radius, with faster movement than when pursuing a player. Cats and ocelots do not attack creepers. A creeper that has begun a detonation does not flee unless the player leaves its blast radius. 

Creepers are not targeted by tamed wolves, iron golems or zoglins. However, they are still attacked by withers, snow golems,[1] vindicators named "Johnny", wardens and goats. When hit by a stray projectile (like a drowned's trident), a creeper retaliates if not already chasing a player, unless said projectile is a skeleton's arrow. If a creeper is attacked by any mob except a goat, the creeper moves toward the mob that attacked it and explodes.

When a creeper is inflicted with a status effect, its explosion creates an area effect cloud of the effect.‌[Java Edition  only]

### Charged creeper

Two creepers' explosion damage radius in the dirt. Comparison between a charged creeper's (left) and a normal creeper's (right). Notice that the charged creeper's explosion is much bigger than the normal creeper's explosion.
A charged creeper is created only when lightning strikes within four blocks of a normal creeper. The lightning can be created in any way, including naturally, with the /summon command, by a trident with the Channeling enchantment, or attracted to a lightning rod. Charged creepers are distinguished from normal creepers by their blue aura surrounding them, and their explosion power is significantly increased.

In Java Edition, a charged creeper can be summoned with the following command: /summon creeper ~ ~ ~ {powered:1}.

In Bedrock Edition, a charged creeper can be summoned by: /summon creeper ~ ~ ~ minecraft:become_charged.

Their countdown timers are the same as normal creepers, both in terms of range and time. With a power of 6, an explosion caused by a charged creeper is twice as powerful as the explosion caused by a creeper. Charged creepers' explosions are 50% more powerful than an explosion of TNT. How close the creeper was to the lightning strike does not affect the size or power of the explosion.

Charged creepers have the same entity ID as normal creepers. The only difference is that the value of the boolean powered tag is set to 1 (true).

In Java Edition, a charged creeper explosion that kills zombies, skeletons, wither skeletons, piglins, or other creepers causes one[2] of those mobs to drop its corresponding mob head. If multiple valid mobs are killed in the explosion, the one that drops a head is chosen at random. In Bedrock Edition, a charged creeper explosion that kills zombies, skeletons, wither skeletons, or other creepers causes all the killed mobs to drop their corresponding heads.[3]

A charged creeper does not drop its own head when it explodes, although any other charged creepers or creepers killed in the explosion drop a creeper head. Players and ender dragons do not drop their heads,[4] nor do mobs without corresponding mob heads, such as livestock animals.

### Farming
Main article: Tutorials/Creeper farming
## Data values
### ID
Java Edition:

| Name    | Identifier | Translation key          |
|---------|------------|--------------------------|
| Creeper | creeper    | entity.minecraft.creeper |

Bedrock Edition:

| Name    | Identifier | Numeric ID | Translation key     |
|---------|------------|------------|---------------------|
| Creeper | creeper    | 33         | entity.creeper.name |

### Entity data
Creepers have entity data associated with them that contains various properties.

Java Edition:

Main article: Entity format

 Entity data
Tags common to all entities
Tags common to all mobs
 ExplosionRadius: The radius of the explosion itself, default 3.
 Fuse: States the initial value of the creeper's internal fuse timer (does not affect creepers that fall and explode upon impacting their victim). The internal fuse timer returns to this value if the creeper is no longer within attack range. Default 30.
 ignited: 1 or 0 (true/false) - Whether the creeper has been ignited by flint and steel.
 powered: 1 or 0 (true/false) - May not exist. True if the creeper is charged from being struck by lightning.

Bedrock Edition:

See Bedrock Edition level format/Entity format.
