# Dolphin
Dolphins are neutral mobs  that live in non-frozen oceans, which grant a speed boost to players that swim near them.

## Contents
- 1 Spawning
- 2 Drops
	- 2.1 On death
- 3 Behavior
	- 3.1 Weaknesses
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
	- 11.2 In other media
- 12 References
- 13 External links

## Spawning
Dolphins are found in groups (pods) of 3–5 in all ocean biomes, except frozen oceans and cold oceans. They spawn exclusively between levels 50 and 64.
Dolphins continuously spawn as long as their spawn requirements are met, and naturally despawn if no players are near by, similar to squid. 

In Java Edition, dolphins and squids together make up the water creatures mob cap.

10% of dolphins spawn as babies.‌[Bedrock Edition  only]

## Drops
### On death
| Item |              | Roll Chance | Quantity (Roll Chance) |           |            |             |
|------|--------------|-------------|------------------------|-----------|------------|-------------|
|      |              |             | Default                | Looting I | Looting II | Looting III |
|      | Raw Cod[d 1] | 100%        | 0–1                    | 0–2       | 0–3        | 0–4         |

1. ↑Dropped as Cooked Cod if on fire when killed.

- 1–3, if kill credit is given to the player.

Killing a baby dolphin yields neither items nor experience.

## Behavior
Dolphins jumping in water.
Dolphins normally swim in pods, occasionally leaping out of the water to get air. They are also able to jump from one body of water to another. Additionally, they chase after players in boats.

A player who sprint-swims within a 9 block spherical radius of a dolphin receive Dolphin's Grace for 5 seconds‌[Java Edition  only], replenished as long as the player continues to sprint-swim within a 15 block spherical radius of a dolphin. Invisibility reduces both of these ranges like normal, based on the amount of armor the player is wearing. The dolphin keeps following the player as long as they are sprint-swimming, allowing the player to swim under the speed boost for long distances. In Bedrock Edition, the player simply gets a swimming speed boost without a status effect.

Dolphins are lured by dropped items that are inside nearby water blocks, knocking them around and chasing them.‌[Java Edition  only] If the dolphin can not find a path to a dropped item, the dolphin may stay underwater to the point of drowning.[1] If the dolphin is in, or on, a waterlogged bottom slab or chest with an air block above, or a bubble column, the dolphin is prevented from drowning. 

Should the player or another mob hit a dolphin (unless the dolphin is killed within one hit‌[Java Edition  only]), the whole pod retaliates, attacking all at once similar to wolves and zombified piglins. Hostile dolphins remain hostile even if they are fed fish. Hostile dolphins are far more vicious in Bedrock Edition.

Feeding dolphins raw cod or raw salmon improves their "trust" and interactions with the player, depending on the amount of fish fed. 

When dolphins are fed raw cod or raw salmon, they swim to the nearest shipwreck, buried treasure, or ocean ruins. Because they are locating the chest in the structures rather than the structures themselves, breaking the chests causes the dolphin to locate a new structure with intact chests. Dolphins also avoid guardians and elder guardians.

Dolphins do not deal any damage in Peaceful difficulty and are completely passive.

### Weaknesses
If a dolphin leaves the water in dry weather, it starts taking suffocation damage after two minutes, and eventually dies. It takes no damage out of water during rain. Regardless of weather, a dolphin on land actively seeks out a body of water, or seeks its target if in a hostile state.

They cannot survive without getting air every once in a while, so if they stay submerged for about four minutes they begin drowning. The water breathing effect prevents them from drowning.

Like most other aquatic mobs, dolphins cannot ride boats.

Dolphins can be towed by a lead.

Because the dolphin is an aquatic mob, it is affected by the Impaling enchantment.‌[Java Edition  only]

## Data values
### ID
Java Edition:

| Name    | Identifier | Entity tags                                                          | Translation key            |
|---------|------------|----------------------------------------------------------------------|----------------------------|
| Dolphin | `dolphin`  | `aquatic`<br/>`not_scary_for_pufferfish`<br/>`sensitive_to_impaling` | `entity.minecraft.dolphin` |

Bedrock Edition:

| Name    | Identifier | Numeric ID | Translation key       |
|---------|------------|------------|-----------------------|
| Dolphin | `dolphin`  | `31`       | `entity.dolphin.name` |

### Entity data
Dolphins have entity data associated with them that contains various properties.

Java Edition:

Main article: Entity format
- Entity data
	- 
	- Tags common to all entities
	- 
	- Tags common to all mobs
	- CanFindTreasure: 1 or 0 (true/false) - if true, this dolphin can lead a player to treasure.
	- GotFish: 1 or 0 (true/false) - if true, this dolphin got fish from a player.
	- TreasurePosX: This dolphin's X coordinate destination when leading a player to treasure, 0 ifCanFindTreasureis false.
	- TreasurePosY: This dolphin's Y coordinate destination when leading a player to treasure, 0 ifCanFindTreasureis false.
	- TreasurePosZ: This dolphin's Z coordinate destination when leading a player to treasure, 0 ifCanFindTreasureis false.

Bedrock Edition:

SeeBedrock Edition level format/Entity format.

