# Minecart
A minecart is a train-like vehicle entity that runs on rails.

## Contents
- 1 Obtaining
	- 1.1 Crafting
	- 1.2 Entity loot
- 2 Usage
	- 2.1 Crafting ingredient
	- 2.2 Transportation
	- 2.3 Dismounting
- 3 Behavior
	- 3.1 Speed
	- 3.2 Merged minecarts
	- 3.3 Distance traveled by empty carts starting on a downward slope
	- 3.4 Collision
	- 3.5 Mobs
	- 3.6 Boats
	- 3.7 Saddled pigs
- 4 Sounds
- 5 Data values
	- 5.1 ID
	- 5.2 Entity data
- 6 Achievements
- 7 History
- 8 Issues
- 9 Trivia
- 10 Gallery
	- 10.1 Screenshots
	- 10.2 In other media
- 11 References
- 12 External links

## Obtaining
Minecarts can be retrieved by attacking them for some time. One attack from a pickaxe, sword or axe is enough for a minecart to drop in item form, provided the player's attack cooldown is reset. A minecart is also destroyed if it makes contact with a cactus, or if shot with a bow/crossbow. Critical hits are not applied to minecarts, although the particles suggest otherwise.

### Crafting
| Ingredients | Crafting recipe |
|-------------|-----------------|
| Iron Ingot  |                 |

### Entity loot
Minecart with command blocks can be given to the player with the /give command or through the Creative inventory under certain conditions‌[Java Edition  only]; minecart with spawners‌[Java Edition  only] are available only via the /summon command. Each drop 1 minecart when broken.

## Usage
A rideable minecart on rails surrounded by wood slabs
A minecart can be placed in the same manner as most blocks, but only on top of a rail. Once placed, it may be derailed by pushing it off the end of the track. After this, it can be railed again by placing a rail directly below it or pushing it onto a track.

### Crafting ingredient
Anything crafted with the minecart functions similar to a regular minecart, but cannot be ridden.

| Name                  | Ingredients      | Crafting recipe |
|-----------------------|------------------|-----------------|
| Minecart with Chest   | Chest+Minecart   |                 |
| Minecart with Furnace | Furnace+Minecart |                 |
| Minecart with Hopper  | Hopper+Minecart  |                 |
| Minecart with TNT     | TNT+Minecart     |                 |

### Transportation
Steve riding a minecart
See also: Transportation and Riding

Minecarts can be ridden by pressing the "use" control on them. Once inside, an external impulse may be needed to make the minecart start moving. The player can slowly move the minecart forward while riding it, by pressing forward. If a mob walks in front of a moving empty minecart, it is pulled into the cart.

After rolling off of the end of a track, a minecart can be pushed around on open blocks. If a minecart is pushed onto or falls onto tracks, it "snaps" to those tracks. When riding a minecart, if the minecart lands on a rail, the player does not take any fall damage. 

Unlike with beds, there is no message above the hotbar for attempting to enter a fully occupied minecart.[1]

### Dismounting
Players can exit the minecart by pressing sneak. When a player or mob dismounts a minecart, either by choice, by breaking the minecart, or by passing over a powered activator rail, the minecart tries to find a safe ejection destination for the player one block away. First it checks the eight horizontally adjacent blocks in the following order of priority relative to direction of travel: right, left, rear right, rear left, front right, front left, rear, front. A valid destination has a block underneath with a solid (not necessarily full) top surface and a space with enough headroom and width for the passenger to fit in when standing at the center. The space can even contain liquid or have open trapdoors if the mob is slim enough, and presence of other mobs doesn't matter. If no valid destination exists on same horizontal level, the minecart then checks the blocks one above, then one below. For a player, the minecart also checks for crawlable destinations. If still none, the minecart chooses its own location. Once the minecart picks a destination, it actually ejects the passenger one block up in the air and the passenger settles down on its own. Under a low ceiling this may cause one tick of suffocation damage. The air drop exists to allow passengers to land on carpet or bottom slabs.

## Behavior
### Speed
Minecarts have a predefined speed limit of exactly 8 blocks per second per axis of travel. A minecart traveling diagonally can, therefore, travel up to 11.314 blocks per second.[2] When a minecart comes to a turn it moves diagonally across that turn.

Powered rails powered by redstone give minecarts a boost of speed. Speed is gradually decreased if there are no powered rails to assist its movement, and an unpowered powered rail slows down a minecart rapidly. The speed decreases at a faster rate when going uphill, compared to when moving horizontally. A minecart does not need powered rails to assist its movement down a hill.

Anything in the way of the minecart brings it to a stop. Once a minecart has left the track, it rapidly decelerates within one or two blocks. When mobs touch a minecart, they affect it in the same way a player would, i.e. mobs that move up against a still cart set it in motion.

If a minecart is moving fast enough, it can skip across one block without a track and reattach to track on the other side, at significantly reduced energy and speed. A minecart's hitbox can skip turns if the minecart is boosted using enough powered rails.[3]

The speed and momentum of a minecart can differ depending on whether or not it is empty, and in the case where a minecart has a container, the speed can differ depending on the quantity and type of items inside.

### Merged minecarts
In Java Edition, two or more minecarts can be merged by pushing them into each other so that they overlap. Merged minecarts move as a collective, like a train, and can be useful for long-distance transport because while moving in a straight line, they do not need powered rails to keep their speed.

To summarize:

- Minecarts can also be merged bydroppinga minecart on another minecart.
- Merged minecarts do not lose speed while traveling on straight rails
- Cornersin the rails might cause merged minecarts to unmerge.
- Minecarts withchest(even fully filled) can also be merged and also donotrequire powered rails.

### Distance traveled by empty carts starting on a downward slope
This table shows the distance traveled by an unoccupied minecart, in meters, on a downward slope, with a boost (or no boost). The most efficient way is to use only 1 boost at the bottom of the incline on the flat surface. Using 2 increases distance by about 20% or 1.5 blocks. All distance trends based on the height seem to be logarithmic.
The carts started from rest, on a slope Height blocks up.

| Height | No boost | Bottom | Bottom and top | All boosts on incline and bottom |
|--------|----------|--------|----------------|----------------------------------|
| 1      | 2.77     | 8.77   | 10.8           | 10.8                             |
| 2      | 4.59     | 9.59   | 10.83          | 13.37                            |
| 3      | 5.81     | 9.81   | 11.66          | 15.12                            |
| 4      | 7.04     | 10.04  | 12.46          | 16.95                            |
| 5      | 7.87     | 10.87  | 12.29          | 17.95                            |
| 10     | 11.65m   | 13.38  | 15.12          | 21.68                            |
| 100    | 15.87m   | 17.05  | 17.54          | 25.34                            |

### Collision
Minecarts are about the same size as a block (1×1). Because of this, a ladder, door, or trapdoor prevents it from falling down a 1×1 hole. Carts on rails also ignore collision in certain situations. A cart traveling uphill, downhill, or on a curve with a block placed in front of it, goes through the block.[4]

A minecart that reaches the end of a rail up against an opaque solid block bounces back, but if the block is transparent then it stops. The minecart can even bounce against an opaque block from a standstill if the rail underneath is powered. A player or mob riding in a minecart does not collide with or suffocate in any transparent blocks but suffocates inside opaque blocks.

Minecarts are completely unaffected by ice, packed ice, and blue ice[5]; they can also be destroyed by coming in contact with lava or fire.

### Mobs

  

This section is missing information about some other mobs that cannot be picked up by minecarts. 
Please expand the section to include this information. Further details may exist on the talk page.


Minecart shaking due to being on top of an activator rail.
Mobs can ride minecarts, but cannot control them. Mobs cannot exit the minecart unless the minecart is destroyed or moves onto an active activator rail.[6] However, in Bedrock Edition, endermen are able to teleport out of minecarts.[7]

A mob can ride a minecart when pushing by a moving minecart on rails in Java Edition or when colliding with a minecart in Bedrock Edition. It is easier to pick up a mob when a minecart is turning. In Bedrock Edition, armor stands can also be picked up.

Most mobs (including cameras‌[BE & edu  only]) can be picked up by minecarts, except ender dragons, wardens, withers, NPCs, and agents. In Java Edition, iron golems and armor stands cannot be picked up either. This is much different from boats, which can be entered only by mobs smaller than the boats; even very large mobs like ghasts can enter minecarts.

A jockey riding a minecart automatically accelerates the minecart.[8] Mobs in minecarts don't despawn, and don't count toward the mob cap.‌[Java Edition  only][9]

### Boats

  

This feature is exclusive to  Java Edition. 





This section demonstrates the use of a bug to make a contraption. 
Bugs of this nature may be fixed at any time without warning, causing the contraption to stop working. Bug exploits may be disallowed on some multiplayer servers and lead to a ban if used.Use at your own risk.


Due to the bug MC-113871, boats can be captured by minecarts. When a boat is placed in a minecart, the minecart travels faster on rails, approximately as fast as on powered rails. The movement in the boat minecart is glitchy and moving forward with the W key moves the cart backward relative to the player, and vice versa for moving backward with the S key. The minecart also moves on the rail-less ground at a crawling speed, but it does not float in the water despite being in a boat. 

Using this glitch can be far more resource-efficient since the boat minecart can move at the speed of a powered rail track on flat ground and on slopes. Another physics glitch with the boat minecart is the extreme reduction in friction when the minecart is on rails, which is similar to the lack of friction when a boat is riding on ice. This glitch can be done in Survival without cheats simply by pushing a minecart into a boat on the track. This bug is now patched. 

### Saddled pigs

  

This feature is exclusive to  Java Edition. 





This section demonstrates the use of a bug to make a contraption. 
Bugs of this nature may be fixed at any time without warning, causing the contraption to stop working. Bug exploits may be disallowed on some multiplayer servers and lead to a ban if used.Use at your own risk.


Similar to the boat and due to a long-standing bug, a saddled pig can be captured by a minecart. Riding one allows the player to move as fast as on powered rails (including uphill), without the use of any powered rails. The movement is reversed as with the boat, such that pressing W moves the cart backward while S moves the cart forward (think like a real plane/train's thrust lever).

## Data values
### ID
Java Edition:

| Item     | Identifier | Form | Translation key         |
|----------|------------|------|-------------------------|
| Minecart | minecart   | Item | item.minecraft.minecart |

| Entity   | Identifier | Translation key           |
|----------|------------|---------------------------|
| Minecart | minecart   | entity.minecraft.minecart |

Bedrock Edition:

| Item     | Identifier | Numeric ID | Form | Translation key    |
|----------|------------|------------|------|--------------------|
| Minecart | minecart   | 370        | Item | item.minecart.name |

| Entity   | Identifier | Numeric ID | Translation key      |
|----------|------------|------------|----------------------|
| Minecart | minecart   | 84         | entity.minecart.name |

### Entity data
Minecarts have entity data associated with them that contain various properties of the entity.

Java Edition:

Main article: Entity format

 Entity data
Tags common to all entities
Tags common to all minecarts

Bedrock Edition:

See Bedrock Edition level format/Entity format
