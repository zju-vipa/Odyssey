# Thunderstorm
A thunderstorm is a somewhat uncommon and dangerous weather condition.

## Contents
- 1 Behavior
- 2 Effects
	- 2.1 Lightning
		- 2.1.1 Effects on mobs
		- 2.1.2 Lightning mechanics
		- 2.1.3 Thunder
		- 2.1.4 Lightning rods
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Entity data
- 5 Advancements
- 6 History
- 7 Issues
- 8 Trivia
- 9 Gallery
	- 9.1 Screenshots
- 10 References

## Behavior
Thunderstorms are an uncommon temporary, global occurrence[1] that can happen randomly at any time, within the Overworld. The exact type of precipitation during a thunderstorm varies depending on the temperature of the current biome, as well as the current altitude.

- While the clear counter is counting down, the weather is always clear. This counter is used only when the "/weather clear" command is issued, setting the counter to a value given by the player or 5 minutes (seeCommands/weather)
- The rain counter counts down to zero, and each time it reaches zero, the rain is toggled on or off. When the rain is turned on, the counter is reset to a value between 12,000-24,000 ticks (0.5-1 game days), and when the rain is turned off the counter is reset to a value of 12,000-180,000 ticks (0.5-7.5 game days).
- Like the rain counter, the thunder counter also toggles thunder on and off when it reaches zero, but clear weather overrides the "on" state. When thunder is turned on, the thunder counter is reset to 3,600-15,600 ticks (3-13 minutes), and when thunder is turned off the counter resets to 12,000-180,000 ticks (0.5-7.5 days).
- Thunder can occur in the game only when the rain and thunder states both happen to be "on" at the same time. The random combinations of the states toggled by the rain and thunder counters result in a 1.44% chance for a thunderstorm to occur, or an approximate average real-time duration of 9 hours between thunderstorms.
- The values in each range are uniformly distributed.

Thunderstorms can be skipped entirely with the use of a bed, regardless of the time of day.

## Effects
As with rain and snow, the sky is darkened and the sun, moon, and stars are no longer visible. Thunderstorms darken the world, causing the light level from the sky to visually decrease to 10. The clouds darken from white to dark gray, although clouds themselves do not precipitate or create lightning. While the sun is not visible during rain, the glow associated with sunrise and sunset is still visible.

Unlike during regular rainstorms or snowstorms, the light level from the sky is treated as if it were 0 for the purposes of hostile mob spawning, which allows hostile mobs to spawn at any time of the day.

### Lightning
Not to be confused with Lighting.



Lightning is a lethal element to thunderstorms. Lightning momentarily increases the sky light's brightness to slightly greater than full daylight.

The fire that a lightning bolt creates.
Lightning strikes randomly and creates fires (only on normal and hard difficulty) in a 2 block radius where it strikes. Such fires act normally, igniting all flammable materials, detonating TNT, and even activating nether portals. The lightning itself, however, is not destructive and does not destroy blocks. While most fires are extinguished by the rain, areas that block rain can allow the fire to spread, and any netherrack, magma blocks, soul sand, or soul soil lit by lightning is not extinguished by the rain.

Most entities struck by lightning are dealt 5 damage (sometimes twice in succession) and are set on fire, which may cause additional damage.

If the player is killed by a lightning strike, the death message appears: "<player> was struck by lightning". This message does not display if the player was killed by the fire created by a lightning bolt.

Lightning in Bedrock Edition changes color from white to orange at sunset, and appears brighter during the daytime.

Lightning may be manually summoned with the /summon lightning_bolt command. It is summoned as an entity, and it can be referred to by commands or selectors. 

A group of skeletal horsemen spawned during a thunderstorm.
Charged Creeper
A villager gets struck by lightning.
Lightning is also spawned when a trident enchanted with Channeling is thrown and strikes a mob or a lightning rod during a thunderstorm.

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
