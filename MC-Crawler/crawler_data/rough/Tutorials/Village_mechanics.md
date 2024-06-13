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

#### Initial Size of Villages
The village boundary and expansion area

A village forms when a villager claims the first bed, indicated by green particles emitting from the bed and villager. Initially, the village spans a rectangular space with the bed's pillow at its center, extending outward 32 blocks in all horizontal directions and 12 blocks vertically from that point, resulting in a total volume of 65 blocks wide, 65 blocks deep, and 25 blocks high. New Points of Interest (POIs) like beds, bells, or workstations added within this area don't affect the village's size.
A village expands it's borders to include new claimed points of interest outside it's boundaries.
#### Expansion of Villages
However, villages can expand further. Beyond the initial borders, within an additional range of 32 blocks horizontally and 52 blocks vertically, lies the potential for expansion. If new POIs are added within this extended area, the village will expand accordingly, growing the minimum amount needed to include the new POI. This expansion occurs when a villager claims the new POI, again indicated by green particles.

#### Village Origin Point
The village Origin Point serves as the center of smaller villages and determines the area where iron golems and cats spawn. In villages that have expanded, it serves as the starting point from which village expansions are calculated (see Village Center).

This point is marked by a bed, bell, or villager's job site. The leading villager’s bed pillow, if he has one, determines this point. To identify the leading villager, remove all the job sites in the village and notice which villager claims a new one first, indicated by green particles over his head. Villagers claim job sites based on village hierarchy, not proximity.

The origin point prioritizes the leader’s claimed POIs in the following order: bed pillow, bell, then job site. Specifically, the northwest bottom corner of the POI serves as the origin point. If the leading villager unlinks from all his POIs or perishes, the second villager in the hierarchy is considered, and so forth until a POI is designated the origin.

However, as of April 11, 2024, a bug (MCPE-54183) causes the hierarchy order to reverse when logging out and back in on certain platforms like Nintendo Switch. This bug also means that on certain platforms, adding new villagers can alter the hierarchy order, as they may not always join at the end of the list. The new villager could become the leader or be positioned elsewhere in the hierarchy.
In expanded villages, the center shifts from the first bed to the geometric center of the village boundaries.
#### Village Center

If the village borders expand, the center shifts to the geometric center to accommodate this growth, affecting where iron golems and cats spawn. While the origin point may still influence the bounding box to some extent, it will no longer correlate with the village center.
Shows the distance between beds necessary to establish two distinct villages.
#### Distinct Villages
To create two separate villages, the new village must exist beyond the expansion range of the original one. The border of the second village must be at least 33 blocks away horizontally or 53 blocks vertically from the first border. This means that two basic villages each made up of a single claimed bed must be at least 97 blocks apart horizontally to be considered separate. This calculation considers the initial border of 32 blocks from the first bed's pillow, an additional 33 blocks for shared expansion area, and finally, the village border for the second bed's pillow.

#### Overlap Potential
Village expansion ranges can overlap. When two villages share the same expansion space, any claimed POIs within this area belong to the village whose border is closest to the POI. This means that both villages may expand into the shared space until their borders touch.

## Housing
A "house" is defined as a claimed bed. If the bed is obstructed by a solid block, villagers cannot pathfind to it and therefore cannot claim the bed.‌[Java Edition  only] This causes anger particles to emit from the villager's head and from on top of the bed. If a villager succeeds in sleeping in an obstructed bed, the villager suffocates and dies, leaving the bed unclaimed.

Once a villager has claimed a bed, that bed is registered as a house in the village.‌[Bedrock Edition  only] The villager remembers their bed location, even when underground. In the evening, villagers return to their beds. However, if a villager cannot reach their bed and then loses ownership of it, other villagers can claim it. In this case the previous bed owner forgets the bed location and searches for another unclaimed bed.

## Job site
Naturally spawned villagers spawn either as unemployed or (in Bedrock Edition) as a nitwit. The unemployed can then change their profession by seeking and claiming an unclaimed job site block. 

Naturally generated villages consist of two main types of buildings: houses (any building with beds) and job sites (a building with job site blocks). No villagers spawn in job site buildings. Therefore if a naturally generated village consists of only job site buildings, no villagers can spawn and (in Bedrock Edition) the structures are never registered as a village.

Employed villagers spend their time working at their job site block, starting in the morning. Unemployed villagers, nitwits, and baby villagers have no job site and do not work. Once a villager chooses a job site block, the villager remembers its location. They go to work in the morning, mingle at their gathering point, and return to work in the afternoon.

## Breeding and population cap
Main articles: Villager § Breeding and Breeding
Villagers can breed without player intervention, but there must be at least two adult villagers who can reach one another.

Villagers go into love mode (indicated by red heart particles above both their heads) if they have enough food to make themselves and their partner willing. They enter love mode based on their amount of food and not the population cap, but can produce a baby only if they have their own beds plus an available bed for the baby, and the beds have two empty blocks above them (there needs to be room for the baby to jump on the bed). If the population cap is met,‌[Bedrock Edition  only] or the beds are obstructed, this prevents them from mating, and angry particles appear above their heads (along with the heart particles, note that when this happen, they still use up their food points). Much like with farm animals, when two villagers are in love mode and can see each other, they go to each other and stare for a few seconds, after which a baby villager spawns next to them. Breeding villagers does not drop experience. The baby villager spawns wearing clothing dependent on the biome the village is in (with a small chance to inherit one of its parents' outfits, if different). It acquires a job after it has grown up and if there is a valid, unclaimed job site.

### Willingness
Villagers must be  willing in order to breed. 

Villagers can become willing by having 12 food points, which are gained by consuming food in the villager's inventory. Bread provides 4 points, while carrots, potatoes, and beetroots each provide only 1. Farmer villagers occasionally throw harvested crops at villagers, allowing them to pick them up to obtain enough food to become willing.

Breeding consumes 12 food points.

Villagers do not accept food or farm food themselves if gamerule 'mobgriefing' is set to false. This makes villager breeding possible only with 'mobgriefing' set to true, because villagers cannot become fully willing without food.

In Bedrock Edition, villagers can become willing if the player trades with them. Willingness is granted the first time a new offer is traded, or at a one-in-five chance on subsequent trades. This does not cause them to immediately seek out a mate, however.[verify]

## Curing zombie villagers
See also: Tutorials/Curing a zombie villager

5% of zombies are zombie villagers. Additionally, when a villager is attacked by any zombie they have a chance (50% on Normal difficulty, and 100% on hard) of turning into a zombie villager instead of just being killed.

Players can cure zombie villagers by using a golden apple on them while they are affected by weakness. Players can usually apply weakness by brewing potions. In nether-disabled servers, a witch and a zombie villager, or Weakness tipped arrows from a master fletcher are needed. Witches sometimes throw a splash potion of Weakness if a player is within 3 meters, which players can use to their advantage.

After the player uses the splash potion of Weakness and a golden apple, the zombie makes a loud sizzling sound, emits orange swirly particles, and shakes. During the conversion time (up to 5 minutes), they still behave as zombies, so they should be protected from sunlight and kept away from nearby villagers. After a few minutes, they turn into regular villagers.

A zombie villager who has been cured gives a permanent discount on trades to the curing player.

## Popularity

  

This section describes content that exists only in outdated versions of Java Edition. 
Village popularity was removed in Java Edition 1.14 in favor of per-villager reputation.


A player's popularity starts at zero and ranges between −30 and 30. The following can alter a player's popularity:

| Popularity of Actions                                                                                                                                             |                                     |  |  |  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|--|--|--|
| Action                                                                                                                                                            | Popularity Change inBedrock Edition |  |  |  |
| Curing azombie villager                                                                                                                                           | +10                                 |  |  |  |
| Present when a villager joins its first village (This includes curing the first zombie villager in a abandoned village or spawning villagers in an empty village) | +5                                  |  |  |  |
| Upgrading a Villager to Expert/Master                                                                                                                             | +1                                  |  |  |  |
| Upgrading a Villager to Journeyman                                                                                                                                | +1                                  |  |  |  |
| Upgrading a Villager to Apprentice                                                                                                                                | +1                                  |  |  |  |
| Spending time in a village (does not increase popularity above 0)                                                                                                 | +1                                  |  |  |  |
| Attacking a villager (hitting the villager with anything or using a fishing rod on the villager. Projectiles like arrows, snowballs, and eggs, also count)        | −1 per hit                          |  |  |  |
| Killing a villager                                                                                                                                                | −2                                  |  |  |  |
| Attacking a baby villager                                                                                                                                         | −3 per hit                          |  |  |  |
| Killing a baby villager                                                                                                                                           | −2                                  |  |  |  |
| Killing a village'siron golem(Building an iron golem or spawning an iron golem using commands does not increase the player's popularity)                          | −5                                  |  |  |  |

A player's popularity does not reset on death, and players cannot alter other players' popularity. Popularity is stored per village; a player's popularity may be high in one village and low in another. When a player acts directly on a villager, particles around that villager indicate the change in popularity. Conversely, because popularity is stored per village, if the entire village is destroyed, any accumulated popularity, positive or negative, is also eliminated.

If a player has -15 popularity or less, the village's naturally-spawned iron golems act hostile to that player until the player's popularity is increased by trading. Golems constructed by the player, however, are always passive toward the player.
Summoning golems, trading, and healing increase popularity.

## Cats
In Java Edition, cats are spawned around players in or near villages. A random position is chosen near the player, and a cat is spawned if that position is within a 5×5×5 subchunk cube around a village center subchunk, and the position is within 48 blocks of at least 4 claimed beds and fewer than 5 cats are within a 97×17×97 box centered around the spawn position.

Cats spawned in this way may despawn if not tamed.

In Bedrock Edition, the number of cats spawned in a village is based on the number of beds in that village. Cats require only one villager, and one cat can spawn for every four beds, claimed or not. Up to 40 beds can be present for a maximum of 10 cats, and cats respawn based on the number of beds.

If there are two villages, each already with 10 cats, merging the villages into a single village does not cause any cats to despawn. However, the number of cats is still capped at 10, so no new cats spawn until the number of cats is below 10.

The player can run cats out of the village, thus allowing for more cats to spawn.

## Iron golems
See also: Tutorials/Iron golem farm

In Java Edition, iron golems are spawned when villagers are talking. Their spawning requirements are:

1. The villager must be gossiping with another villager or panicking
2. The villager has not seen an iron golem recently
3. The villager has slept in the past day
4. 5 villagers (3 if panicking) within 10 blocks meet those requirements (other than #1)
5. The random location chosen for the iron golem isn't air or liquid that blocks light.

Random location choosing is attempted 10 times within 16 blocks of the villager, and is attempted once from 6 blocks above the chosen x and z, to 6 blocks below it.

In Bedrock Edition, iron golems are spawned in villages meeting these requirements:

1. The village has at least 20 beds and at least 10 villagers
2. 75% of the villagers must have worked in the past day
3. All of the villagers must be linked to a bed
4. The village must be within a player'ssimulation distancevolume
5. There must be space to spawn an iron golem within a 16×6×16 volume around thevillage center

To clarify, iron golems can spawn as long as the player is within simulation range of the village's boundaries; being near the village center is not necessary. Simulation distance remains consistent both horizontally and vertically. The formula for calculating simulation range is as follows:

SimulationRange=8×SimulationDistance

Iron golems will spawn within a 16×6×16 volume around the village center. A spawn is attempted on average once every 35 seconds and an iron golem can spawn when the 2×4×2 volume above the spawn point contains only non-solid blocks and the spawn block is solid.

## Zombie sieges
Main article: Zombie siege

  

This feature is exclusive to  Java Edition. 


At midnight, there is a 10% chance that a zombie siege might occur. This is when a large number of zombies spawn in or near a village, attacking what villagers they can reach, crowding around and pounding on the doors of those they can't. On Hard or Hardcore mode, they can actually break down the wooden doors (this is true of all zombies, not just during sieges). They'll attempt to beat them down on other difficulties, but not succeed.

Zombies in sieges ignore the 24-block minimum distance from the player, but other than that, behave absolutely normally (i.e., they do not spawn on glowstone or any other transparent or half block, need a 2×1×1 minimum space, etc.). Houses can be zombie-proofed by taking out one ground block from directly in front of the door, and if necessary, rehanging the door such that the outside is flush with the outside wall. This is because zombies can break only the top half of a door, and if they have to jump, they cannot get through. In addition, players can fill the hole with two layers of carpet to achieve the same effect as zombies cannot pathfind into the door.

## Raids
Main article: Raids
When a player with the 'Bad Omen' debuff enters a village, the Bad Omen effect disappears and a raid occurs. Raids are groups of illagers (pillagers, vindicators, evokers, ravagers, and witches) attacking the village with the intent of killing villagers. They can remove the 'Bad Omen' debuff by drinking milk before entering a village to prevent raids; however, the player can also defend a village from a raid, at which point the player gains the 'Hero of the Village' buff. This causes villagers to give the player steep discounts during trading, as well as bestow various gifts upon the player.‌[Java Edition  only]

In Java Edition 1.21, the 'Bad Omen' debuff will be replaced with 'Raid Omen'.

