### Jumps
Jumps are used to add excitement while bridging gaps between rails or increasing the rider's elevation. Detector rails need to be connected to specifically-timed slime blocks attached to pistons. Depending on the timing, the player can be "thrown" anywhere with slime blocks.

### Vertical Loops
An expansion on that idea involves making the jump up circular and bringing the player down to the starting point. This is the closest that the player can get to a vertical loop, since minecarts cannot go upside-down.

### Corkscrews
An expansion on the vertical loop idea turns it into a corkscrew. These are even more complicated to build as there is forward motion brought into the equation.

The only known corkscrews that currently work were built by The Duke MC.




However, Javamonk expanded the idea to the height limits of the world.




### Portals
Minecarts and other transport vehicles in portals will not react to the portal blocks. The only way to make use of the portals is to force the player to dismount the vehicle. This can be done with a powered activator rail or a command block set to kill minecart entities upon activation. (Too many activator rails will kill the minecart.)

### Water Skiing
"Water Skiing" is a part of the roller coaster which uses uplift bubble columns (by putting soul sand at the seabed) to cause the minecart to quickly traverse a body of water like a boat (but bouncier!). You should have a slime block on a sticky piston to launch the minecart for more speed. There should also be a sloped waterlogged powered rail to prevent the minecart from hitting the side of the landing block. (Build a small platform below if you have to.) There should also be a "landway" of nine rails with above blocks cleared to a great height to prevent the minecart from inadvertently landing on a trackless block.

### Skating
Skating is a part in a coaster where you are on ice and sliding around. Advanced users can utilize redstone alongside a slime block and sticky piston to change the other player's direction.

### Water Flows
Water flows can be used as a much slower alternative to rails. The water should not flow backwards. To make a flow faster, add soul sand below (see Water Skiing, above).

### Teleportation
Use a Command Block to target the minecart and teleport it to the destination with /tp @e[c=1,type=minecart] DESTINATION in Bedrock Edition, or /tp @e[limit=1,sort=nearest,type=minecart] DESTINATION in Java Edition.

## Rider Protection
It is critical that your rider doesn't die during the journey! Use these additions to make the rider safer.

### Partial Protection
#### Fences
Flank the rails with fences and remove blocks right next to or above the fences.

Pros: Easy to build; looks nice; easy to integrate with other protection methods. Mobs can't step on the tracks by accident when riding the rollercoaster.

Cons: Does not fully protect the player against evokers (and their vexes), skeletons, phantoms, spiders, and boss mobs.

#### Glass
Surround the rails with glass.

Pros: Easy to integrate with other protection methods; provides total protection against non-boss mobs unless broken or exploded.

Cons: Obstructs the player's vision; fragile against explosions; a single gap can let a baby zombie or cave spider inside the track.

#### Armor
Equip enchanted diamond or netherite armor to the rider.

Pros: Good protection, against hostile mobs or fire damage.

Cons: Strong attacks can still kill the player; the armor will eventually break; the Curse of Binding will be needed; the player's armor does not look nice unless trimmed with smithing templates to match the rollercoaster design (colors, shape, ect).

#### Beacons and Conduits
Set up fully powered beacons and conduits along the track. The beacons should provide Resistance, Regeneration, and Strength (the latter may be omitted in some instances). The conduits will let the player breathe underwater.

Pros: Long range, just one is needed for a short ride.

Cons: Regeneration may not be fast enough in some instances; you will need to build multiple for longer rides. Conduits also have a range so if you are building a long underwater section, you will need a lot of conduits.

#### Resistance 5
Resistance 5 makes the player completely immune to all damage. It is available through an upgraded Potion of the Turtle Master or Commands.

Pros: Player cannot take any damage; easily accessible with commands

Cons: Minecart can still be destroyed; resistance 5 may only be applied with the potion in non-Java/Bedrock editions, leading to additional cons below

Potion Cons: Must be reapplied frequently; drastically decreases FOV

#### 
Set a Repeating Command Block to automatically kill, teleport, or immobilize entities that get too close with one of the below commands:

- Kill:/execute @e[type=player] ~ ~ ~ /kill @e[TARGETOR]
- Teleport:/execute @e[type=player] ~ ~ ~ /tp @e[TARGETOR] DESTINATION
- Freeze:/execute @e[type=player] ~ ~ ~ /execute @e[TARGETOR] ~ ~ ~ /tp @s @s

The targetor will depend on the edition of Minecraft you play on.

- Java:[IGNORELIST,distance=...DESIREDDISTANCE]
- Bedrock:[IGNORELIST,x=~-X1,y=~-Y1,z=~-Z1,dx=X2,dy=Y2,dz=Z2]
	- This equation should be used for the dn values: 2N1+1=N2(for example, an X of 2 would become 5 from the equation)

The ignore list is also dependent and is what entities you want to spare.

- [type=!player,type=!minecart]is the bare minimum you need.

- [type=!player,type=!minecart,type=!painting,type=!item_frame,type=!fireworks_rocket,type=!leash_knot,


type=!armor_stand,type=!falling_block] is a good kit that covers a wide variety of mobs that you likely want to spare or pose no threat

- [type=!player,type=!minecart,name=!SPARENAME]will ignore the minimum needed entities as well as entities with the nameSPARENAME.
- You can expand targetors to other entities with,type=!ENTITY

Example: To freeze entities that get within 5 blocks of players, with the exception of mobs named Jeff: /execute @e[type=player] ~ ~ ~ /execute @e[type=!player,type=!minecart,name=!Jeff] ~ ~ ~ /tp @s @s

Pros: Works every tick; variable range; deflects boss mobs

Cons: ‌[Java and Bedrock editions  only]; laggy; fills operators' chat menus if the gamerule commandBlockOutput is true; does not protect rider against non-entity hazards (lava, fire, cacti...); the simple mistake of forgetting the ! in type=!player will make worlds unplayable and uneditable

