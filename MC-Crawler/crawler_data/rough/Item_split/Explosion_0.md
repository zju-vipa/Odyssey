# Explosion
An explosion is a physical event, generally destructive, that occurs in several different circumstances. It can destroy nearby blocks, propel and damage nearby entities, and cause fires in some cases. Explosions produce a "shockwave" particle effect.

The propulsion effect of explosions is often used for TNT cannons.

## Contents
- 1 Interaction with entities
	- 1.1 Exposure and impact calculation
	- 1.2 Velocity
	- 1.3 Damage
- 2 Block destruction
	- 2.1 Calculating which blocks to destroy
	- 2.2 Dropping blocks
- 3 Causes
- 4 Blast resistance
- 5 Sounds
- 6 History
- 7 Trivia
- 8 References

## Interaction with entities

  

This feature is exclusive to  Java Edition. 


### Exposure and impact calculation
The sample points for the exposure calculation of TNT.
The explosion impact is used to calculate entity knockback and damage, and it depends on exposure. Impact is stronger the closer and less obstructed the entity is to the explosion. 

To calculate the exposure of an entity, rays are cast from the explosion center to a

⌈2⋅width+1⌉ by ⌈2⋅height+1⌉ by ⌈2⋅length+1⌉ grid of points, spaced by

[width2⋅width+1height2⋅height+1length2⋅length+1]

With the negative corner at

[12(1−⌊2⋅width+1⌋2⋅width+1)012(1−⌊2⋅length+1⌋2⋅length+1)]

For each ray, the game checks if it intersects with any block-hitbox. The exposure is the proportion of rays that remain unobstructed, and ranges from 0 to 1. These rays go from the entity to the explosion, so scaffolding blocks exposure when the explosion is below and the entity is above. Note that exposure is currently directionally biased (and the ray targets can sometimes be outside the entity) due to bug MC-232355.

The impact for an entity can then be calculated with the following formula:

(1−distance2⋅power)⋅exposure⋅(1−0.15⋅highest blast protection level)

With the distance measured from the explosion to the entity's feet position. See the Causes subsection for a list of explosion powers, and see Blast Protection for more information about blast protection.

### Velocity
Each entity within range of an explosion is propelled away from it along the ray from the explosion center to the eyes of the entity, except TNT entities, where the ray goes to the feet of the TNT entity. The magnitude of this applied velocity is the impact.

Each affected entity is accelerated by between 0 and 1 blocks per game tick (0 to 20 blocks per second), added to its current velocity. This effect can accumulate over multiple explosions, even within a single tick.

### Damage
Entities are damaged differently depending on difficulty. At the end of each game tick the highest amount of damage from all explosions is chosen.

The following term can be used to calculate the damage inflicted on an entity:

(Easy:3.5Normal:7Hard:10.5)⋅power⋅(impact+impact2)+1

The Blast Protection enchantment and Resistance effect are handled separately. Explosions don't damage players in Peaceful difficulty. Nether stars cannot be destroyed by explosions.

## Block destruction
The rays from the explosion center to points that are uniformly distributed on the surface of a cube. (this defines only their directions)
On a small scale explosions form a roughly spherical crater. The size of that crater is dependent on the power of the explosion and the blast resistance of the destroyed blocks.

### Calculating which blocks to destroy
To calculate the blocks affected, "rays" are created from the explosion center to the outer points of a 16 by 16 by 16 grid. Each of those rays gets an intensity of power⋅(random value from 0.7 to 1.3).

For each ray, with the position starting at the explosion center:

1. The game checks the block at the currentposition(note that this ignores block shape).
2. If the block isn't air,intensityis reduced by(blast resistance+0.3)⋅0.3.
3. If the remainingintensityis above 0 and the block can be blown up, it gets added to the list of blocks to blow up.
4. Positionis moved 0.3 blocks along the ray.
5. Intensityis reduced by0.22500001.
6. If the remainingintensityis above 0, repeat from step 1. Otherwise, continue with the next ray.

After the process is done, the list of blocks to blow up is shuffled. For explosions that can cause fires, the game attempts to generate fire in 1⁄3 of the blocks in the list. This fire is successfully placed only when above an opaque block.

Due to the fact that the game ignores block shapes when checking blast resistance, explosions happening inside a non-full block get dampened heavily. Sufficiently weak explosions happening on ender chests, enchanting tables, or any height of water or lava do no block damage.

### Dropping blocks
In Java Edition, the drop chance of blocks in explosions can be customized via three game rules: blockExplosionDropDecay (includes end crystals), mobExplosionDropDecay and tntExplosionDropDecay. Only tntExplosionDropDecay is set to false by default. If an explosion's drop decay is set to false, items have a 100% chance of dropping. Otherwise, items have a 1⁄power chance of dropping. However, dragon eggs, beacons, conduits, heads, shulker boxes and decorated pots[1] always drop from explosions.

In Bedrock Edition, explosions all have a <100% chance of dropping blocks.[citation needed]

