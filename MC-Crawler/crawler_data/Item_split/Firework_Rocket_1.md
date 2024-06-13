### Duration and direction
Fireworks travel different heights based on the amount of gunpowder added. The number is displayed as a tag on the item's tooltip with the description of "Flight Duration".

Each firework determines its lifetime in ticks by 10 × (number of gunpowder + 1) + random value from 0 to 5 + random value from 0 to 6, after which it explodes.

When spawned by player or command, the height it rises is between 8 and 20 blocks with 1 gunpowder, 18 to 34 blocks with 2 gunpowder, and 32 to 52 blocks with 3 gunpowder. 
(Note: In Java Edition, it is possible to use commands to create firework rockets with higher durations. These rockets go higher and keep accelerating with virtually no terminal velocity. If the duration is long enough, the firework rocket could reach heights of over 1,000,000 blocks and speeds of over 10,000 m/s in a matter of minutes. Such fireworks with significant X and Z motions speed up sideways exponentially and reach outside the world boundary in a matter of seconds.)

When spawned,  fireworks have a vertical speed of .05 and a random small X and Z speed (random value near zero with a standard deviation of .001). Each tick, the firework accelerates horizontally by multiplying its X and Z velocities by 1.15, and vertically by adding a constant factor of 0.04.

When shot from a dispenser, it travels 9 to 10 blocks with 1 gunpowder, 14 to 15 blocks with 2 gunpowder, and 19 to 20 blocks with 3 gunpowder in the direction it was dispensed. When dispensed, the firework has a random velocity close to 0.5 (with a maximum deviation of .009) in the direction it was dispensed and a random small velocity in both other directions (random value near zero with a maximum deviation of .009). The fireworks velocity does not change over the lifetime of the rocket.

Fireworks can be made to travel different directions by being dispensed or launched under flowing water. The firework's direction combines with the flow of the water to go diagonally.

## Data values
### ID
Java Edition:

| Item            | Identifier      | Form | Translation key                |
|-----------------|-----------------|------|--------------------------------|
| Firework Rocket | firework_rocket | Item | item.minecraft.firework_rocket |

| Entity          | Identifier      | Translation key                  |
|-----------------|-----------------|----------------------------------|
| Firework Rocket | firework_rocket | entity.minecraft.firework_rocket |

Bedrock Edition:

| Item            | Identifier      | Alias ID  | Numeric ID | Form | Translation key     |
|-----------------|-----------------|-----------|------------|------|---------------------|
| Firework Rocket | firework_rocket | fireworks | 519        | Item | item.fireworks.name |

| Entity          | Identifier       | Numeric ID | Translation key              |
|-----------------|------------------|------------|------------------------------|
| Firework Rocket | fireworks_rocket | 72         | entity.fireworks_rocket.name |

### Item data
Java Edition:

Main article: Item format

 tag: The item's tag tag.
 Fireworks: One of these may appear on a firework rocket.
 Explosions: List of compounds representing each explosion this firework causes.
: A firework explosion.
Tags common to all firework explosion effects
 Flight: Indicates the flight duration of the firework (equals the amount of gunpowder used in crafting the rocket). Can be anything from -128 to 127.

Bedrock Edition:

See Bedrock Edition level format/Item format.
### Entity data
Java Edition:

Main article: Entity format

 Entity data
Tags common to all entities
Tags common to all projectiles
 FireworksItem: The crafted firework rocket.
 Count: The item count, typically 1.
 id: The id of the item, should be minecraft:firework_rocket.
 tag: The tag tag.
 Fireworks: One of these may appear on a firework rocket.
 Explosions: List of compounds representing each explosion this firework causes.
: A firework explosion.
Tags common to all firework explosion effects
 Flight: Indicates the flight duration of the firework (equals the amount of gunpowder used in crafting the rocket). Can be anything from -128 to 127.
 Life: The number of ticks this fireworks rocket has been flying for.
 LifeTime: The number of ticks before this fireworks rocket explodes. This value is randomized when the firework is launched: ((Flight + 1) * 10 + random(0 to 5) + random(0 to 6))
 ShotAtAngle: 1 or 0 (true/false) - true if this firework was shot from a crossbow or dispenser.

Bedrock Edition:

See Bedrock Edition level format/Entity format.

