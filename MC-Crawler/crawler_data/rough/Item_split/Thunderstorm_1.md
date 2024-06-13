#### Effects on mobs
A lightning strike affects certain mobs differently:

- Lightning may randomly spawn a"skeleton trap" horsewith a chance of 0.75–1.5% chance on Easy, 1.5–4% on Normal, and 2.8125–6.75% on Hard, depending on theregional difficulty. A player triggers the trap by moving within 10 blocks of the horse, whereupon the horse transforms into four skeletal horsemen. A non-triggered trap horse despawns after 15 minutes.
- Apigstruck by lightning turns into azombified piglin.
- Acreeperbecomescharged.
- Avillagergets replaced by awitch.
- A redmooshroomchanges into abrown mooshroomand vice versa.
- A lightning strike on aturtleinstantly kills it, and it drops 1bowlinstead of its normal drops.[2]

#### Lightning mechanics
For each loaded chunk, every tick there is a 1⁄100,000 chance of an attempted lightning strike during a thunderstorm. From this probability, if ≈201 chunks are loaded (from a radius of 128 blocks from the player to the center of each chunk) then 90% of the time up to 5 lightning strikes occur in the world each minute, with an average of approximately 2.4 lightning strikes each minute.

When lightning is to strike, random X and Z coordinates within the chunk are chosen, and the block just above the highest block that is liquid or obstructs movement is chosen for the lightning strike. If a lightning rod is nearby, it strikes the rod instead. Then if there are any living entities that can see the sky in a 3×h×3 region from 3 below the target block up to the world height, one such entity is selected at random and the lightning target is moved to the block the entity stands in.

The target block is checked again for the following conditions:

- Target block can see the sky.
- Rain (not snow) is falling in the target block.
	- Thus, lightning does not naturally strike within cold biomes or biomes where it does not rain.

If these conditions pass, lightning strikes.

When lightning strikes, all entities within a 6×12×6 region horizontally centered on the northwest corner of the target block with the bottom edge 3 below the target block are struck by lightning. Multiple passes are made over this region, so items dropped during an earlier pass may be destroyed during a subsequent pass; damage immunity usually prevents struck mobs from taking more than 5 damage. Non-solid blocks (such as redstone, torches, and snow layers) are not directly affected by lightning.

#### Thunder
"Thunder" redirects here.  For the Minecraft Dungeons enchantment, see MCD:Thundering.
Thunder is a sound event that occurs every time lightning strikes. Every player within 160 thousand blocks and in the same dimension hears the thunder. 

The ability to hear thunder affects multiplayer, as it is possible to hear lightning strike at someone else's base or use a modded Minecraft client to determine the direction of every strike in the world the player is in. Using the direction of strikes, it is possible to triangulate the coordinates of lightning strikes.

#### Lightning rods
Lightning strikes within a radius of 128 blocks (Java Edition) or 64 blocks (Bedrock Edition) of a lightning rod are redirected to the rod, emitting a Redstone signal. This can be used to prevent flammable structures from being struck by lightning, or intentionally direct lightning toward or away from mobs. During a thunderstorm, they emit spark-like particles, even in biomes where lightning doesn't strike.

## Data values
### ID
Java Edition:

| Name           | Identifier       | Translation key                   |
|----------------|------------------|-----------------------------------|
| Lightning Bolt | `lightning_bolt` | `entity.minecraft.lightning_bolt` |

Bedrock Edition:

| Name           | Identifier       | Numeric ID | Translation key              |
|----------------|------------------|------------|------------------------------|
| Lightning Bolt | `lightning_bolt` | `93`       | `entity.lightning_bolt.name` |

### Entity data
Lightning bolts have entity data associated with them that contain various properties.

Java Edition:

Main article: Entity format
- Entity data
	- 
	- Tags common to all entities

Bedrock Edition:

SeeBedrock Edition level format/Entity format.

