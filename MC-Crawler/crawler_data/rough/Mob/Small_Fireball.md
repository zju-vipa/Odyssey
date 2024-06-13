# Small Fireball
A small fireball is a projectile produced by the ranged attack of blazes, and by fire charges when shot from dispensers.

## Contents
- 1 Behavior
- 2 Sounds
- 3 Data values
	- 3.1 ID
	- 3.2 Entity data
- 4 History
- 5 Issues
- 6 Trivia
- 7 References

## Behavior
Blazes shoot small fireballs in volleys of three at a time as their ranged attack. When a fire charge is fired from a dispenser, it also shoots a small fireball.

Small fireballs, when fired either by dispensers or blazes, fly in a straight line through the air. There is a random offset in a small fireball's trajectory due to a 'cone' of spread, which can cause small fireballs to miss their target or hit something else.[needs testing]

Fireballs shot from dispensers start out stationary and accelerate, while fireballs shot by blazes maintain the same speed.

A small fireball flies indefinitely until it hits a block or an entity, even if it is outside the player's render distance.

If a small fireball hits a block, fire is placed at that location if possible. It produces no explosive effect. Small fireballs can light campfires and nether portals and can prime minecarts with TNT.

If it hits an entity that is not immune to fire and does not have the Fire Resistance effect, the entity takes 5 of projectile damage regardless of difficulty level. The target is set on fire for 5 seconds, which does an additional 4 fire damage over time; it can deal up to 9 damage from these combined effects.

A small fireball cannot be deflected by melee attacks or arrows, unlike regular fireballs. However, it can be blocked by shields, which prevents the player from being damaged and lit on fire.

## Data values
### ID
Java Edition:

| Name           | Identifier       | Entity tags          | Translation key                   |
|----------------|------------------|----------------------|-----------------------------------|
| Small Fireball | `small_fireball` | `impact_projectiles` | `entity.minecraft.small_fireball` |

Bedrock Edition:

| Name           | Identifier       | Numeric ID | Translation key              |
|----------------|------------------|------------|------------------------------|
| Small Fireball | `small_fireball` | `94`       | `entity.small_fireball.name` |

### Entity data
Java Edition:

Main article: Entity format
Small fireballs have entity data associated with them that contains various properties.

- Entity data
	- 
	- Tags common to all entities
	- 
	- Tags common to all fireballs
	- 
	- Tags common to all projectiles
	- Item: The item to render as, may be absent.
		- 
		- Tags common to all items

