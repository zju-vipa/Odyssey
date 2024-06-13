# Tutorials/Hitboxes
This tutorial seeks to teach you how to make use of hitboxes.

## Contents
- 1 Hitboxes
- 2 Usage
	- 2.1 Damage
		- 2.1.1 Ender Dragon
	- 2.2 Suffocation
	- 2.3 Farms
	- 2.4 Ejecting Mobs
	- 2.5 Line of Sight
		- 2.5.1 Breaking Line of Sight

## Hitboxes
Hitboxes are regions that describe how much space an entity takes up, which can be shown by pressing the F3 + B keys.‌[Java Edition  only] When they are shown, a white outline will be seen showing the location of the entity and the space it takes up. There is also a flat red rectangle near its "eyes". This is the "line of sight", which is where its in-game eyes are, which could be independent of where they appear to be. Notice how the line of sight wraps all the way around the entity. This explains how it is impossible to sneak up behind a mob without it seeing the player. There is also a straight blue line that extends away from the line of sight. This line points in the direction the mob is facing.

## Usage
They are crucially important for a lot of purposes.

### Damage
Hitboxes are areas where the mob can be damaged. This includes all types of damage, except for void, fall, and effect-related damage. It is important because it can help the player shoot a mob such as ghast. The hitbox of a ghast does not include the tentacles, so shooting one in its tentacles does nothing.

#### Ender Dragon
The ender dragon has a unique hitbox. It has green boxes around its different body parts, but there is also a giant white box and the line of sight lines. The green boxes are places where you can deal damage to the dragon.

### Suffocation
The mechanics of suffocation is best explained using hitboxes. If a solid block enters the "head" of the mob, then it begins to suffocate. The location of the "head" is marked with an extremely thin red box, so that is where a mob can be suffocated. If the mob does not have a separate outline for its head, such as a ghast, then it is assumed that the entire mob is a head. Therefore, a player can easily suffocate a ghast by pushing a block anywhere into its hitbox.

### Farms
Sizes of hitboxes can be used for farms. For example, the hitbox of a baby chicken is shorter than the hitbox of an adult chicken. If you wanted to build an automatic chicken farm, you must ensure that only the adult chicken will be killed, since baby chickens don't drop anything.

Blocks that are shorter than a full block are best to use for building a farm. These include enchanting tables, slabs, daylight sensors, and snow layers. These can be used to manipulate the line of sight, as was used in a wither skeleton farm shown in the video:




They can also be used to manipulate when mobs can see other mobs, which can help make vindicator-powered passive mob farms:




### Ejecting Mobs
Since every entity has a visible hitbox, it can be used to more easily break a minecart or boat that is carrying another mob. By making hitboxes appear, you can see where the mob's hitbox starts. So, you can break a minecart or boat with a passenger without harming the passenger.

### Line of Sight
Have you ever heard somebody telling you to "break line of sight"? They are referring to making it so the mob can no longer see the player. The player has their own line of sight (red rectangle). The "line of sight" between mobs exists when the red rectangle of the player is visible from the red rectangle of the mob, and they are in range. This range varies from 20 blocks for most hostile mobs to a hundred blocks for ghasts and blazes, and is affected by factors like Blindness effect and wearing skulls.

Line of sight affects how mobs attack the player. If a hostile mob has a line of sight, it will begin attacking. For guardians, the player must maintain a line of sight for the entire charge-up of the attacking beam for it to do any damage. If the player's blue line is aiming towards an enderman's red rectangle and not wearing a pumpkin, the enderman will get angry at the player.

