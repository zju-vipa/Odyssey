# Tutorials/Shulker farming
Shulker farming is the process of using the mechanic where if a shulker is hit by a shulker bullet, there is a chance for a new shulker to form, allowing a renewable source of Shulker Shells.
(In 1.17 and 1.18, this mechanic is only available for Java Edition, but from 1.19 onwards you can farm shulkers on Bedrock Edition.)

## Contents
- 1 Mechanics
	- 1.1 Shulker Teleporting Mechanics
		- 1.1.1 Scaffolding Interaction
- 2 Moving Shulkers to the Overworld
	- 2.1 Making shulkers ride Minecarts
	- 2.2 Making shulkers teleport to End Portal
		- 2.2.1 Notes
- 3 Videos
	- 3.1 Mechanics
	- 3.2 Portal-based Designs
		- 3.2.1 Ultra Efficient Designs
	- 3.3 Single Dimension Designs
		- 3.3.1 Reactor
		- 3.3.2 Scaffolding-based
		- 3.3.3 Minecart-based
- 4 See also

## Mechanics
See also: Shulker § Spawning

There is a chance that a new shulker of the same color will spawn when one shulker hits another shulker (or itself) with a shulker bullet. The hit shulker must have its lid open to spawn a new shulker. The shulker spawns where the old shulker was before it teleported. The chance of this happening decreases with the amount of shulkers in an 8-block radius; when more than 5 shulkers are present in the area, no shulkers will spawn. The probability is reduced for shulkers with less than half their health remaining.

There are two main approaches to shulker farming: cell-based designs, and reactors. Cell based designs maintain a shulker in a breeding cell, removing the duplicated shulkers from around the breeding cell as quickly as possible. On the other hand, reactors rely on having a large number of effective breeding cells, and just let the number of shulkers naturally saturate, collecting drops from within the reactor as shulkers gradually die off. Both designs have their strengths and weaknesses, with reactors tending to be a lot simpler, but being larger, and usually requiring significantly more blocks placed for the same rates. In both cases, these farms are reliant on having a large number of teleportable spaces for the breeding shulker(s). However, cell-based farms also need a way of moving shulkers away from the region around the breeding shulker.

Another key consideration is 2-dimension (2D) versus single dimension (1D) farms. 2D farms make use of portals, which are a highly effective way of removing shulkers from the region around the breeding shulker, and also provide for a large number of teleportable spaces (with relatively few blocks). However, 2D farms can only be built in the overworld, meaning a shulker has to be transported from the end through the main portal gateway. Additionally, portal-based farms can often be unsuitable for busy servers, and diagnosing portal-linking issues can be a headache for less technical or less experienced players.

On the other hand, 1D farms tend to be slightly more complicated and have lower rates (although this is changing with newer 1D farm designs). Early iterations made use of a few different methods of removing shulkers, such as minecarts, and trapdoors. However, newer and better farms take advantage of an interesting interaction between shulker teleporting and scaffolding.



### Shulker Teleporting Mechanics
When a shulker tries to teleport (including when it is hit by a shulker bullet), it will try up to 5 random locations in a 17×17×17 region around itself and test if they are valid spots for it to sit on. For a spot to be valid, it needs to be an air block, have a solid face for a shulker to sit on, and have a collisionless block opposite the solid face for the shulker to extend its head into.

Since duplicating requires the shulker to successfully teleport, ensuring an abundance of valid teleport targets around the shulker(s) is usually important to ensure good rates. However, since the shulker tries multiple times per teleport attempt, there are diminishing returns.

Most farms also require teleport-proofing other parts of the farm to ensure shulkers can't end up where they shouldn't. For this, there are a number of blocks with some solid surfaces, but not others, which includes slabs, stairs, trapdoors, and soul sand (which is only solid on the base due to not being a full block).

