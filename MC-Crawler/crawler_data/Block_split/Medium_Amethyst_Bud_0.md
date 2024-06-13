# Amethyst Cluster
Amethyst buds are the first three stages of growth of amethyst clusters, which grow on budding amethyst.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Post-generation
- 2 Usage
	- 2.1 Growing into amethyst clusters
	- 2.2 Decoration
	- 2.3 Light
	- 2.4 Sound
- 3 Sounds
	- 3.1 Generic
		- 3.1.1 Cluster
		- 3.1.2 Large bud
		- 3.1.3 Medium bud
		- 3.1.4 Small bud
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Gallery
	- 7.1 Screenshots
	- 7.2 Development images
- 8 References

## Obtaining
### Breaking
The amethyst cluster block itself in any of its growth stages (rather than its amethyst shard drops) can be obtained by mining it with any tool with the Silk Touch enchantment.

When mined without Silk Touch or broken by being pushed off an attached block by a piston or sticky piston, only fully grown amethyst clusters drop amethyst shards, while amethyst buds drop nothing. Breaking an amethyst cluster with a pickaxe drops 4 shards while any other method of breaking it yields 2 shards. The maximum amount of amethyst shards dropped can be increased with Fortune; Fortune I gives a 1⁄3 chance for 8 shards (averaging 5.33 shards), Fortune II gives a 25% chance (each) to give 8 or 12 shards (averaging 7 shards), and Fortune III gives a 20% chance (each) to give 8, 12, or 16 shards (averaging 8.8 shards).

| Block     | Amethyst ClusterAmethyst Bud |
|-----------|------------------------------|
| Hardness  | 1.5                          |
| Tool      |                              |
|           | Breakingtime (sec)[A]        |
| Default   | 2.25                         |
| Wooden    | 1.15                         |
| Stone     | 0.6                          |
| Iron      | 0.4                          |
| Diamond   | 0.3                          |
| Netherite | 0.25                         |
| Golden    | 0.2                          |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


### Natural generation
Amethyst buds and clusters generate naturally as part of amethyst geodes, on exposed faces of budding amethysts.


### Post-generation
Every time a budding amethyst block receives a random tick, there is a 20% chance for a small amethyst bud to generate on any of its sides, as long as the block being replaced with the small amethyst bud is air or a water source block.

## Usage
### Growing into amethyst clusters
An amethyst bud placed on a budding amethyst (rather than any other block) regardless whether it was placed by the player or spawned by the budding amethyst itself, grows over time, going through three growth stages – small, medium, and large – before reaching its 4th and final growth stage as an amethyst cluster, which drops amethyst shards when mined.

In Java Edition, the below logic can be applied:

Per random tick, updates will occur to any given block in the loaded chunk every 68.27 seconds on average if the chunk center is within 128 blocks of a player's location.
Each random tick assigned to the budding amethyst block has a 20% chance of creating a new amethyst bud or incrementing the growth stage on one randomly-selected side of the six-sided block.
There are 4 growth stages.
As such, the math can be applied if a player is within random tick range as:

(68.27 seconds average for random ticks) × (20% chance of growth for any given single side) × (6 sides) × (4 growth stages) = 68.27×5×6×4 = 8192.4 seconds average, also 2 hours 16 minutes 32.4 seconds, also 6.827 in-game days.

