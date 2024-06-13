# Minecart with Hopper
A minecart with hopper is a minecart with a hopper inside. Unlike a normal hopper, it pulls items from containers much more quickly, cannot push items into containers, can collect item entities through a single layer of solid blocks, and is locked and unlocked via activator rails.

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
### Crafting
| Ingredients     | Crafting recipe |
|-----------------|-----------------|
| Hopper+Minecart |                 |

Minecarts with hoppers can be retrieved by attacking them. By doing so, it drops as an item along with the contents of the hopper. Critical hits are not applied to them although the particles suggest otherwise.

## Usage
The GUI of a minecart with hopper.
Minecarts with hoppers are placed similarly to other minecarts.

A minecart with hopper pulls in items lying nearby (within a range slightly larger than the cart itself), or inside a container directly above the minecart, at a rate of one item every game tick (20 items per second), eight times as fast as a normal hopper. It also picks up items that are lying on a block directly above the track. It does not push items into containers, but a hopper underneath the track can remove items from a minecart with hopper on the track. Ordinary hoppers can also drop items into a minecart with hopper like other containers, at the normal speed of 2.5 items per second. In Bedrock Edition, a minecart with hopper on a curved rail pulls in items in a hopper lying in front of its moving direction and one block above if the hopper's output funnel is pointed downward and no block is below that hopper.[1]

The minecart with hopper can be disabled by passing over a powered activator rail, and can be reenabled by an inactive activator rail.

An empty minecart with hopper can travel more than 85 blocks without stopping (as opposed to a normal cart going less than 12 blocks) from a dead stop using a two-powered track starter, even with another minecart in front of it. However, the distance traveled by a minecart with hopper depends on the hopper's load. Using a one-powered rail starter track, a minecart with an empty hopper travels 64 blocks until it stops (as opposed to an empty normal minecart going 8 blocks). The distance traveled diminishes non-linearly with increased hopper load; a minecart with a full hopper can travel only 16 blocks in this setup.

See also: Tutorials/Storage minecarts

## Data values
### ID
Java Edition:

| Item                 | Identifier      | Form | Translation key                |
|----------------------|-----------------|------|--------------------------------|
| Minecart with Hopper | hopper_minecart | Item | item.minecraft.hopper_minecart |

| Entity               | Identifier      | Translation key                  |
|----------------------|-----------------|----------------------------------|
| Minecart with Hopper | hopper_minecart | entity.minecraft.hopper_minecart |

Bedrock Edition:

| Item                 | Identifier      | Numeric ID | Form | Translation key           |
|----------------------|-----------------|------------|------|---------------------------|
| Minecart with Hopper | hopper_minecart | 526        | Item | item.hopper_minecart.name |

| Entity               | Identifier      | Numeric ID | Translation key             |
|----------------------|-----------------|------------|-----------------------------|
| Minecart with Hopper | hopper_minecart | 96         | entity.hopper_minecart.name |

### Entity data
Minecarts with hoppers have entity data associated with them that contain various properties of the entity.

Java Edition:

Main article: Entity format

 Entity data
Tags common to all container entities
Tags common to all entities
Tags common to all minecarts
 Enabled: Determines whether or not the minecart hopper picks up items into its inventory.

Bedrock Edition:

See Bedrock Edition level format/Entity format.
