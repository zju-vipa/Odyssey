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

