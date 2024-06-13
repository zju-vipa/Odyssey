# Entity
Entities encompass all dynamic, moving objects throughout the Minecraft world.

## Contents
- 1 General behavior
	- 1.1 Further notes
		- 1.1.1 Boats, boat with chests and minecarts
		- 1.1.2 Gravity-affected blocks
		- 1.1.3 Interactions with "use" control
		- 1.1.4 Riding
- 2 Types of entities
- 3 Motion of entities
- 4 Data values
- 5 Video
- 6 History
- 7 Issues
- 8 See also
- 9 References

## General behavior
Properties all entities have are:

- A position, rotation, and velocity
- A volume consisting of one or more non-rotating, three-dimensionalboxeswith a fixed height and width
- Whether they are onfire, displayed as flames on or around the entity
- Whether they have anystatus effect, such as frompotions
- Aview point, even if it has no eyes

Most entities can be pushed around by water currents, and some can have their trajectory altered by explosions if already traveling at speed. Some entities can be renamed by using a name tag on them. Entity tiles, items, shot or thrown projectiles, area effect clouds, and experience orbs do not have health. Entities that do have a health status include mobs, players, armor stands, boats, boat with chests and minecarts.

Entities cannot pass through solid blocks, excluding vexes and ender dragons. Most types of entities prevent blocks from being placed in the space they occupy, except for dropped items and experience orbs, which are automatically pushed out of the block to open air. If a solid block enters an entity's space, such as falling sand or a swinging door, then it is free to move out of the solid block but not back in. For example, if a door is closed on the player, player can jump up and stand on top of the bottom-half door block, if there is air above the door.

Entities are lit according to the light level of the block their position is in. For example, if a minecart runs over a non-straight track directly into a solid block, it turns black because solid blocks always have a light level of 0; arrows are also sometimes seen to turn black, especially if fired shallowly into the ceiling.

### Further notes
Item frames, glow item frames, paintings, and lead knots, unlike most entities, align to the block grid, and are completely immobile.

Arrows, TNT and falling blocks are assumed to have infinite health, because they are neither destroyed by explosions (although they can be moved by explosions, and they can also be fired out of TNT cannons), nor by being on fire for long periods. However, they can still be "killed" with the use of the /kill command.

#### 
See also: Transportation (contains information about speed)
Boats, boats with chests and minecarts appear to recover health over time. For example, they can be broken by hitting them quickly, but cannot be destroyed by hits with unarmed hand with a pause after each hit. The amount of wobbling displayed by boats and minecarts when struck appears to indicate their current health. All minecart, boat and boat with chest variants have 6.

#### Gravity-affected blocks
Main article: Falling Block
Falling sand that collapsed into a dungeon.
Gravity-affected blocks include sand, gravel, anvils, red sand, dragon eggs, concrete powder, scaffolding, and pointed dripstone, along with snow layers in Bedrock Edition.

A gravity-affected block normally exists as a block, but when its support is removed, it becomes a falling block entity and falls down until hitting the top surface of another block. If there is valid space, it places itself as a block at the nearest on-grid position, or drops as an item if that position is occupied by a block without a solid top surface, such as a torch or a bottom slab.

While a falling block ordinarily falls straight down, its trajectory can be affected by explosions, bubble columns, pistons, reeling it in, and moving slime blocks, and can slide down the side of honey blocks. It is also possible to modify the velocity and direction of a falling block by using commands such as /data‌[Java Edition  only] or third-party programs. A falling block despawns and drops as an item if it does not land after existing for 600 ticks (30 seconds), or 100 ticks (5 seconds) if falling into the void[verify].

If a cave generates underneath sand, gravel, or red sand, the blocks remain stationary until it receives a block update. If a single block is updated and falls down, neighboring blocks are updated in a chain reaction that can cause the collapse of an entire region of gravity-affected blocks.

#### 
Entities with use interactions (such as boats, boat with chests, minecarts, cats, villagers, tamed parrots, and tamed wolves) do not stop the use action of a tool the player is holding. For example, using a water bucket on a tamed wolf causes the wolf to sit, but also empties the bucket near or onto the wolf.

