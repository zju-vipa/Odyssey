# Minecart with TNT
A minecart with TNT is a minecart with TNT inside. Unlike normal TNT, it can detonate instantly, and its blast radius and damage is increased by its speed at detonation.

## Contents
- 1 Obtaining
	- 1.1 Crafting
- 2 Usage
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Entity data
- 5 Video
- 6 History
- 7 Issues
- 8 Gallery
	- 8.1 Screenshots
- 9 References

## Obtaining
Minecarts with TNT can be retrieved by attacking them, and doing so drops them as an item. Critical hits are not applied to them, although the particles suggest otherwise.

### Crafting
| Ingredients  | Crafting recipe |
|--------------|-----------------|
| TNT+Minecart |                 |

## Usage
When the minecart with TNT passes over the powered activator rail, it explodes after four seconds.
Placing two minecarts with TNT on the rail and powering it (here, by flicking the lever) creates an instant explosion.
Destroying the block of gold causes the minecart with TNT to fall down and instantly explode.
A minecart with TNT detonates after a delay on these conditions:

- It moves over a poweredactivator rail.
- It is destroyed while in motion (except by a player in Creative mode).
- It is destroyed by fire, lava, or an explosion.
- It is hit by afire charge‌[Java Edition  only].

The delay is 4 seconds (80 game ticks) for an activator rail, like the TNT block. For other causes there is a random delay between 0 and 1.9 seconds.

It detonates instantly on these conditions:

- It hits the ground with a downward velocity of it falling more than three blocks, unless landing on any form of rail.
- It turns on a curved track too fast, with a solid block or entity located beside the track (in the previous movement direction).
- It is hit by a flaming arrow.
- It is pressed into a block or entity and has velocity.

Upon detonation it acts as normal TNT, exploding and damaging nearby blocks, players, and entities. Upon detonation after activating on activator rail, it does not destroy its rails and the blocks the rail is on, however other nearby minecarts can.‌[Java Edition  only] More than one minecart can be placed on the same rail block, allowing many of them to fit into a single block. They explode when touched, dealing large amounts of damage.

The explosion has a base power of 4, the same as regular TNT, but the game also adds a random bonus value up to 1.5 times velocity, but no higher than 7.5. This means that with a speed of 5 or higher the power is a random value between 4 and 11.5. When triggered by an activator rail or by damage, the bonus value is calculated using the horizontal velocity of the minecart. When hit by a flaming arrow the velocity of the arrow is used instead. When triggered by fall damage, the fall distance divided by 10 is used.

Minecarts with TNT bounce off of other minecarts and cannot be linked to minecarts with furnaces.

## Data values
### ID
Java Edition:

| Item              | Identifier   | Form | Translation key             |
|-------------------|--------------|------|-----------------------------|
| Minecart with TNT | tnt_minecart | Item | item.minecraft.tnt_minecart |

| Entity            | Identifier   | Translation key               |
|-------------------|--------------|-------------------------------|
| Minecart with TNT | tnt_minecart | entity.minecraft.tnt_minecart |

Bedrock Edition:

| Item              | Identifier   | Numeric ID | Form | Translation key        |
|-------------------|--------------|------------|------|------------------------|
| Minecart with TNT | tnt_minecart | 525        | Item | item.tnt_minecart.name |

| Entity            | Identifier   | Numeric ID | Translation key          |
|-------------------|--------------|------------|--------------------------|
| Minecart with TNT | tnt_minecart | 97         | entity.tnt_minecart.name |

### Entity data
Minecarts with TNT have entity data associated with them that contain various properties of the entity.

Java Edition:

Main article: Entity format

 Entity data
Tags common to all entities
Tags common to all minecarts
 TNTFuse: Time until explosion or -1 if deactivated.

Bedrock Edition:

See Bedrock Edition level format/Entity format.
