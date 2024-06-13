# Tutorials/TNT cannons
A TNT cannon is a mechanism that launches entities using TNT. They can be used in survival to mine, fast travel and destroy. Cannons build in survival often follow premade blueprints. In creative, on the other hand, cannons might be build to experiment with one's redstone skills or have fun in general.

Over the years communities have emerged around cannon-PVP and created constraints on the cannons to increase fun when fighting. A limit on the use of blocks, especially those with high blast resistance, is the most common constraint. In WarGear and Slime Block Robot Battles, the fighting machines are built in creative and then are copied to an arena where combat takes place in survival. The size of both is constrained. Dispensers and some entities (and for WarGear also duplication bugs) are prohibited. SBRT requires the whole fighting machine to be movable. Factions bases, on the other hand, are built in survival, though they might be designed in creative. Dispenser cannons and water shielding are allowed here. Those constraints and the absence of constraints have caused a great amount of cannon diversity, which is discussed in this article.

Topic specific speech is used for this page and the sub-pages. It is either explained on this page or under the according headlines.

## Contents
- 1 Loading types
	- 1.1 Manual cannons
	- 1.2 Automatic cannons
- 2 Damage types
- 3 Course types
	- 3.1 Mid-air maneuvering
	- 3.2 Straight trajectories
- 4 Launch types
- 5 Special purposes
	- 5.1 Other projectiles
- 6 General implementation strategies
	- 6.1 Intel
	- 6.2 Signals
		- 6.2.1 Converting signals
		- 6.2.2 Synchronization
	- 6.3 Moving TNT
	- 6.4 Increasing efficiency
	- 6.5 Lag reduction
- 7 Armor and Shielding
	- 7.1 Armor
	- 7.2 Shielding
- 8 Missiles and flying machines
	- 8.1 Missiles
	- 8.2 Flying machines

## Loading types
One game tick Tunnler Machine gun (1gt TMg).
### Manual cannons
As the name suggest, in manual cannons everything is loaded by hand. This includes TNT and might include other entities such as sand.

### Automatic cannons
An automatic cannon can shoot without player interaction (excepting activation).

## Damage types
Comparison of different damage types.
Instead of just exploding all TNT at the same position, like in a Shotgun, many different ways to damage the enemy on multiple positions were found. Tunnler cannons stood out as being the most effective in a lot of situations but there are also some other important damage types, listed here.

## Course types
### Mid-air maneuvering
A Flank Tunnler (FT).
Mid-air maneuvering  is mostly achieved using injectors that explode near the projectiles.

It may be used used to hit the enemy from unexpected angles, to shift around freely or to reduce barrel size.

### Straight trajectories
Straight trajectories describe all trajectories that are not influenced by TNT after leaving the cannon or barrel.

Techniques

The most important techniques to achieve the above are listed on this page: Techniques

## Launch types
Trace of a Nether cannon's launch point.
The place where the Boosters explode is called the launch point. There are two general variants of launch points. Either the Boosters sit on blocks, such a launch point is called a platform or they are in mid-air - such launch points are found in Ejector cannons.

## Special purposes
A Hybrid cannon piercing water armor.
Piercing

A cannon is Piercing when it can penetrate enemy shielding. If it can only penetrate certain shielding types <shielding type>-Piercing is used.

Hybrid

A Hybrid is a combination of sand- and TNT cannon, that uses sand entities wich are transferred to their block form to replace water and penetrate water armor this way.

Instant (I)

To counter Active armor, an Instant cannon penetrates the enemy defense in one shot or in a fast burst of shots so that it cannot replenish itself in time.

Anti Tech-KO (At)

An Anti Tech-KO cannon is small and placed at locations where the enemy might not be able to hit it at all.

It is mostly used when the other cannons are destroyed or to cheat the Tech-KO (that the enemy has no living cannons) win condition.

Anti cannon (!<cannon type>, Scraper)

An Anti cannon is a counter for specific cannons or strategies.

The most common type of Anti cannon is a Shotgun that scrapes the side or back of the enemy. It should be noted that most Anti cannons are just an additional mode for other cannons that can be easily modified for this purpose.

A Scraper does not counter any specific cannon but instead any cannons in (almost) exposed parts of the target. It is often found in the form of Scatter- or Multi impact cannons.

Playerkill

As with Anti cannon, cannons sometimes can easily get modified to specialize on killing players or to prevent players from just moving out of the trajectory. Those modes are named Playerkill.

Moving cannon

Some fighting machines are fully movable so a movable cannon is a no-brainer there.

Extender cannon

Extender cannons move outside the fighting machine and then stay there.

Most cannons are tailored to a specific area of interest. Extender cannons exploit that by moving out of this area of interest. Sometimes that can turn them into almost unbeatable AntiTKOs that don't even need to be compact. But if the enemy is prepared, moving out of the safety of the fighting machine's armor can be devastating.

