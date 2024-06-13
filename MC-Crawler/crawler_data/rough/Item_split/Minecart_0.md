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

| Name                  | Ingredients           | Crafting recipe |
|-----------------------|-----------------------|-----------------|
| Minecart with Chest   | Chest+<br/>Minecart   |                 |
| Minecart with Furnace | Furnace+<br/>Minecart |                 |
| Minecart with Hopper  | Hopper+<br/>Minecart  |                 |
| Minecart with TNT     | TNT+<br/>Minecart     |                 |

### Transportation
Steve riding a minecart
See also: Transportation and Riding

Minecarts can be ridden by pressing the "use" control on them. Once inside, an external impulse may be needed to make the minecart start moving. The player can slowly move the minecart forward while riding it, by pressing forward. If a mob walks in front of a moving empty minecart, it is pulled into the cart.

After rolling off of the end of a track, a minecart can be pushed around on open blocks. If a minecart is pushed onto or falls onto tracks, it "snaps" to those tracks. When riding a minecart, if the minecart lands on a rail, the player does not take any fall damage. 

Unlike with beds, there is no message above the hotbar for attempting to enter a fully occupied minecart.[1]

### Dismounting
Players can exit the minecart by pressing sneak. When a player or mob dismounts a minecart, either by choice, by breaking the minecart, or by passing over a powered activator rail, the minecart tries to find a safe ejection destination for the player one block away. First it checks the eight horizontally adjacent blocks in the following order of priority relative to direction of travel: right, left, rear right, rear left, front right, front left, rear, front. A valid destination has a block underneath with a solid (not necessarily full) top surface and a space with enough headroom and width for the passenger to fit in when standing at the center. The space can even contain liquid or have open trapdoors if the mob is slim enough, and presence of other mobs doesn't matter. If no valid destination exists on same horizontal level, the minecart then checks the blocks one above, then one below. For a player, the minecart also checks for crawlable destinations. If still none, the minecart chooses its own location. Once the minecart picks a destination, it actually ejects the passenger one block up in the air and the passenger settles down on its own. Under a low ceiling this may cause one tick of suffocation damage. The air drop exists to allow passengers to land on carpet or bottom slabs.

