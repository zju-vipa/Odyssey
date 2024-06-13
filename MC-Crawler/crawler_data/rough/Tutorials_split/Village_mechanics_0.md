# Village mechanics
This page describes mechaics relating to villages and villagers.

## Contents
- 1 Village definition
	- 1.1 Java villages
		- 1.1.1 Gathering site
	- 1.2 Bedrock village
		- 1.2.1 House
		- 1.2.2 Gathering site
		- 1.2.3 Initial Size of Villages
		- 1.2.4 Expansion of Villages
		- 1.2.5 Village Origin Point
		- 1.2.6 Village Center
		- 1.2.7 Distinct Villages
		- 1.2.8 Overlap Potential
- 2 Housing
- 3 Job site
- 4 Breeding and population cap
	- 4.1 Willingness
- 5 Curing zombie villagers
- 6 Popularity
- 7 Cats
- 8 Iron golems
- 9 Zombie sieges
- 10 Raids

## Village definition
As used in this article, the term village means a "logical village", which is an area of a world where village mechanics governs villager behavior. This is in contrast to a "physical village", which is a set of buildings, crop fields, etc. created as part of world generation. Although the two kinds of villages most often coincide, this is not obligatory:

- A physical village that has no villagers cannot have village mechanics. Examples includeabandoned villages, villages that were generated whilegame ruledoMobSpawningis set tofalse, and villages where all the villagers have died or were taken somewhere else.
- A logical village is most often generated when the chunks of a physical village are generated, but one can also be created where no physical village exists by placing certain kinds of blocks near a villager, or by moving or spawning a villager near such a block.

This article describes the behavior of villagers in a logical village, whether or not they are in a physical village.

### Java villages
Villages do not have a defined center or radius. Rather, a village is defined by proximity to a village subchunk.

Any chunk section (aka. "subchunk") containing a claimed bed, bell, or job site block is considered to be a village center, and all 26 sections in a 3×3×3 cube around it are also considered part of the village, as used in raids, zombie sieges and some pathfinding. Cats spawn within the 5×5×5 cube around a village center, and patrols do not spawn when the player is in the same range.

Subchunks in a 17×17×17 cube from village subchunks define degrees of proximity to a village.

Mob AI uses these definitions in various cases. For example, when a villager is not in a village and needs to return to one, it sets out in the direction of increasing proximity. When an iron golem patrols the village, it frequently looks for a village subchunk within a 5×5×5 cube of itself to walk to.

Population of a village is never measured. Villager breeding succeeds if the birthing parent can path to an unclaimed bed with at least two empty blocks over its head. Iron golem spawning happens if enough villagers haven't seen a golem recently, when gathered near a bell or panicked by zombies. Cats spawn around players in or near villages if enough beds (and few enough cats) are nearby.

#### Gathering site
A gathering site is where villagers spend their mingling time during the day and can be anywhere in a village, even if it is not located in the center. It is defined by claimed bells. When a bell is claimed, green particles appear above the bell and the bell is registered as a gathering site. 

During a raid, a villager goes to gathering sites and rings the bell to warn other villagers.

Adding a bell establishes a new potential gathering site, even if the village already has one. Villagers remember their specific gathering site and go to it during mingling time, even if another gathering site is closer. However, new or unregistered villagers may choose this new site.

If the player is within 48 blocks of a bell (claimed or not) when a wandering trader is being spawned, the trader spawns within 48 blocks of the bell rather than the player.

### Bedrock village
A village is defined through several mechanics: the village gathering sites, village radius, number of job sites, number of houses, villager population, population cap (maximum number of villagers that can live in the village based on available housing), cat population, and Iron Golem population. Players can use these mechanics to build artificial villages.

#### House
A village needs at least one house and one villager to be considered a village. A house is defined as a bed. The game utilizes villager breeding to try to maintain a 100% population level, so long as there are at least two villagers occupying it.

#### Gathering site
A gathering site is where villagers spend their mingling time during the day and can be anywhere in a village, even if it is not located in the center. It is defined as a claimed bell. When a bell is claimed, green particles appear above the bell and the bell is registered as a gathering site. If a player is in the village, a wandering trader can spawn from a claimed bell.

The bell must be within the village boundary to be considered a centerpoint of the village, therefore it needs to be located near at least one villager and one bed. If villagers and a bell are present but without housing, the villagers search for unclaimed beds rather than mingle.

During a raid, the bell rings automatically.

Adding a bell at a location near claimed beds establishes a new gathering site, even if the village already has one. Each villager remembers their specific gathering site and goes there during mingling time, even if another gathering site is closer. However, new or unregistered villagers may choose this new location if it is closer.

