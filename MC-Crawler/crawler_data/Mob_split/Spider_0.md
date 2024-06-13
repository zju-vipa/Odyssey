# Spider
A spider is a neutral mob that attacks the player in dark areas. Spiders attack by biting the target, and they can also climb walls and lunge at them.

## Contents
- 1 Spawning
	- 1.1 Monster spawners
	- 1.2 Trial spawners
	- 1.3 Status effects
	- 1.4 Spider jockeys
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
	- 11.1 Renders
	- 11.2 Screenshots
	- 11.3 In other media
- 12 References

## Spawning
Up to four spiders may spawn in a 3×1×3 space centered on an opaque block in the Overworld at a light level of 0, except in mushroom fields and deep dark biomes. 
In Java Edition, the block above the spawning space cannot be a full solid block, including transparent ones such as leaves or glass, but non-full blocks, such as soul sand or slabs, are allowed.[2]
In Bedrock Edition, spiders do not spawn in groups.

### Monster spawners
Spiders spawn from monster spawners found in monster rooms (25% chance) as well as in secret rooms surrounded by cobwebs in woodland mansions.

### Trial spawners
‌In Java Edition 1.21 and Bedrock Edition 1.21.0‌[upcoming], spiders have a chance to be selected as the "small melee" mob for trial spawners in trial chambers.

### Status effects

  

This feature is exclusive to  Java Edition. 


Spiders occasionally spawn with status effects in Hard difficulty. For each pack spawn, there is a (10×clamped regional difficulty)% chance of the game applying a status effect. This does not apply to cave spiders. These spiders can spawn with following effects:

- Speed(40% chance)
- Strength(20% chance)
- Regeneration(20% chance)
- Invisibility(20% chance)

The effect is then applied to all entities within the pack, lasting forever. If the Invisibility status effect is applied to a spider, its eyes remain visible.

### Spider jockeys
Main article: Spider Jockey
There is a 1% chance for a spider to spawn with a skeleton riding it, forming a spider jockey. In Java Edition, a spider jockey can also be spawned by the command /summon spider ~ ~ ~ {Passengers: [{id:skeleton}]}.

The skeleton controls how both mobs move. The spider can still climb walls, but the skeleton will suffocate if the spider runs into a ceiling. The skeleton and the spider cannot damage each other.

## Drops
### On death
| Item |            | Roll Chance | Quantity (Roll Chance) |           |            |              |
|------|------------|-------------|------------------------|-----------|------------|--------------|
|      |            |             | Default                | Looting I | Looting II | Looting III  |
|      | String     | 100%        | 0–2                    | 0–3       | 0–4        | 0–5          |
|      | Spider Eye | 1[d 1]      | 1 (33.33%)             | 1–2 (50%) | 1–3 (60%)  | 1–4 (66.67%) |


↑ Dropped only when kill credit is given to the player


5 experience orbs are dropped by a spider when it is killed by a player or tamed wolf.

## Behavior
A spider stays hostile toward the player and an iron golem as long as the light level immediately around the spider is 11 or less; otherwise, it does not attack unless attacked first. 

Hostile spiders see up to 16 blocks, continuing to chase even when exposed to well-lit locations. If a spider sustains damage from a source other than a direct attack, such as falling, its hostility resets to a neutral state.

An aggressive spider pounces at close range. They can attack when their Y-axis position is changed, biting in mid-air, or while climbing.

Spiders can climb up over solid blocks that are not magma blocks‌[Bedrock Edition  only], but do not climb on underside surfaces. A spider pursuing a player can detect a player through blocks. If a spider cannot find an ideal path to the player due to a wall barring the way, it approaches as close as possible to the player's position and proceeds to climb the wall vertically until it gets to the top, even if it loses its aggression toward the player. When a spider loses its aggression, it continues moving forward blindly for 2 seconds; this behavior causes the spider to climb up any walls in its path.

‌In Java Edition 1.20.5‌[upcoming], spiders are scared of armadillos that are not in a rolled up state.

If a spider tries to go through the world border, it starts climbing the world border instead.‌[JE  only]

Spider can also climb on full boats, full boats with chests and shulkers.

Even though normal spiders do not inflict the Poison status effect, they are immune to it. They are also immune to the slowing applied to most mobs when walking through cobwebs.

Spiders flip onto their backs when they die, unlike all other mobs, which land on their sides.

The Bane of Arthropods enchantment inflicts Slowness IV and deals more damage to spiders.

## Data values
### ID
Java Edition:

| Name   | Identifier | Entity tags                                                                           | Translation key         |
|--------|------------|---------------------------------------------------------------------------------------|-------------------------|
| Spider | spider     | arthropoddismounts_underwaterno_anger_from_wind_chargesensitive_to_bane_of_arthropods | entity.minecraft.spider |

Bedrock Edition:

| Name   | Identifier | Numeric ID | Translation key    |
|--------|------------|------------|--------------------|
| Spider | spider     | 35         | entity.spider.name |

### Entity data
Spiders have entity data associated with them that contains various properties.

Java Edition:

Main article: Entity format

 Entity data
Tags common to all entities
Tags common to all mobs

Bedrock Edition:

See Bedrock Edition level format/Entity format.

