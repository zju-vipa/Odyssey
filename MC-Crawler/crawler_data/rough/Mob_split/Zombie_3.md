### Reinforcements

  

This feature is exclusive to  Java Edition. 


On all difficulty levels, damaged zombie mobs (including husks, drowned and even zombified piglins[3]) call all other zombies within a 67×21×67 to 111×21×111 area[n 1] centered on the attacked zombie to target the attacker.

In Hard difficulty, zombies can spawn additional zombies to "help" when damaged. Each zombie has a "likeliness to call reinforcements" statistic ranging from 0–10%, and "leader" zombies (0–5% depending on regional difficulty) get a bonus of 50–75 percentage points to the stat. When the zombie is damaged by an entity or is damaged while targeting an entity, up to 50 attempts are made to randomly choose a spawn location (0 or ±7–40 blocks away in all three axes) that is above a block with a solid top surface, has light level 0, has no players within 7 blocks, and has no colliding entities or blocks at which to spawn the reinforcement. Both the damaged zombie and the new zombie has a 5 percentage point penalty to their "likeliness to call reinforcement" stat, preventing infinite zombies from spawning this way.  Zombie reinforcements can spawn even in locations where naturally spawned zombies can't spawn, like mushroom fields, the End, and the Nether[4], although they still cannot spawn on blocks where other items like redstone dust or pressure plates are placed.

These effects can be negated by killing the zombie in as few hits as possible, by using environmental damage such as cactus or lava, or by avoiding them completely. That is, if the zombified mob drops experience, it has a chance to spawn reinforcements. Additionally, reinforcements do not spawn at all, even on Hard difficulty, if the game rule doMobSpawning is set to false.

Leader zombies are a special type of zombie that spawn with an added 50-75% chance to spawn reinforcements. The chance of a leader zombie spawning increases with clamped regional difficulty, up to a 5% chance of spawning.

Reinforcements zombies spawn regardless of the hostile mob cap. They also spawn on the north-west corner of the designated block, instead of the center of the block like natural mob spawning does.[5] Zombies spawned as reinforcements cannot be zombie villagers, but they can be babies, including chicken jockeys.

### Becoming drowned
A husk that suffocates in water converts to a zombie.
A zombie that suffocates in water converts into a drowned.
If a zombie's head is submerged in water for 30 seconds, it begins converting into a drowned. The zombie shakes, similar to a zombie villager being cured and, after 15 seconds, the zombie becomes drowned. Once this process starts, it cannot be stopped even if the zombie leaves water. This time is not affected by the Respiration enchantment or the Water Breathing status effect. 

A newly-converted drowned always has full health even if converted from a damaged zombie.

An item being held or worn by a zombie when it becomes drowned, whether it was picked up or naturally spawned, has a 100% drop rate, which includes any naturally spawned equipment dropping with full durability‌[BE  only].

Only normal zombies can become drowned; zombie villagers and zombified piglins cannot be converted.[6] Husks, however, convert into zombies if they drown, and then this zombie converts into a drowned as does a normal zombie.

Any husks that convert into zombies also have full health, even if the drowned husk is damaged.

## Data values
### ID
Java Edition:

| Name   | Identifier | Entity tags                                                                                                                                                              | Translation key           |
|--------|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| Zombie | `zombie`   | `can_breathe_under_water`<br/>`ignores_poison_and_regen`<br/>`inverted_healing_and_harm`<br/>`no_anger_from_wind_charge`<br/>`undead`<br/>`wither_friends`<br/>`zombies` | `entity.minecraft.zombie` |

Bedrock Edition:

| Name   | Identifier | Numeric ID | Translation key      |
|--------|------------|------------|----------------------|
| Zombie | `zombie`   | `32`       | `entity.zombie.name` |

### Entity data
Zombies have entity data associated with them that contain various properties.

Java Edition:

Main article: Entity format
- Entity data
	- 
	- Tags common to all entities
	- 
	- Tags common to all mobs
	- 
	- Tags common to all zombies

Bedrock Edition:

SeeBedrock Edition level format/Entity format.
## Notes
1. ↑The inradius is based on the followRange stat: base value is 35, ±5% random spawn bonus, then plus 0–50% random zombie-spawn bonus


