# Amethyst Cluster
Amethyst buds are the first three stages of growth of amethyst clusters, which grow on budding amethyst.

Amethyst clusters are the fourth and final growth stage of amethyst buds, which drop amethyst shards when mined.

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

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
Amethyst buds and clusters generate naturally as part of amethyst geodes, on exposed faces of budding amethysts.


### Post-generation
Every time a budding amethyst block receives a random tick, there is a 20% chance for a small amethyst bud to generate on any of its sides, as long as the block being replaced with the small amethyst bud is air or a water source block.

## Usage
### Growing into amethyst clusters
An amethyst bud placed on a budding amethyst (rather than any other block) regardless whether it was placed by the player or spawned by the budding amethyst itself, grows over time, going through three growth stages – small, medium, and large – before reaching its 4th and final growth stage as an amethyst cluster, which drops amethyst shards when mined.

In Java Edition, the below logic can be applied:

1. Perrandom tick, updates occur to any given block in the loaded chunk every68.27seconds on average if the chunk center is within 128 blocks of a player's location.
2. Each random tick assigned to the budding amethyst block has a 20% chance of creating a new amethyst bud or incrementing the growth stage ononerandomly-selected side of the six-sided block.
3. There are 4 growth stages.

As such, the math can be applied if a player is within random tick range as:

(68.27 seconds average for random ticks) × (20% chance of growth for any given single side) × (6 sides) × (4 growth stages) = 68.27×5×6×4 = 8192.4 seconds average, also 2 hours 16 minutes 32.4 seconds, also 6.827 in-game days.

### Decoration
They can also be placed on certain other types of blocks for decoration. The block must be solid and have at least side sides that form a full surface: for example, they can be placed on the bottom of stairs (or top of upside down stairs), but not on their side, or top. They can also be placed on the bottom of bottom slabs and on the top of top slabs. Of blocks that meet these criteria, some are still excluded.

Amethyst clusters can't be placed on:

- allnon-solid blocks;
- blocks without any full surfaces, likefences,fence gates,walls,glass panes,iron bars,lightning rods,chains,heads,grindstones,bells,lanterns,cauldrons,anvils,conduits,decorated pots,chests,pointed dripstone;
- leaves;
- big dripleaf;
- honey blocks;
- chorus flowers.

### Light
Small, medium and large amethyst buds give off a light level of 1, 2 and 4 respectively, while amethyst clusters give off a light level of 5.

### Sound
Uniquely among other blocks an amethyst cluster in all its growth stages makes a quiet overlay sound when generally interacted with as well as its block breaking sound when hit with a projectile.

## Data values
### ID
Java Edition:

| Name                | Identifier            | Form         | Translation key                       |
|---------------------|-----------------------|--------------|---------------------------------------|
| Small Amethyst Bud  | `small_amethyst_bud`  | Block & Item | `block.minecraft.small_amethyst_bud`  |
| Medium Amethyst Bud | `medium_amethyst_bud` | Block & Item | `block.minecraft.medium_amethyst_bud` |
| Large Amethyst Bud  | `large_amethyst_bud`  | Block & Item | `block.minecraft.large_amethyst_bud`  |
| Amethyst Cluster    | `amethyst_cluster`    | Block & Item | `block.minecraft.amethyst_cluster`    |

Bedrock Edition:

| Name                | Identifier            | Numeric ID | Form                       | Item ID[i 1]   | Translation key                 |
|---------------------|-----------------------|------------|----------------------------|----------------|---------------------------------|
| Small Amethyst Bud  | `small_amethyst_bud`  | `587`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.small_amethyst_bud.name`  |
| Medium Amethyst Bud | `medium_amethyst_bud` | `586`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.medium_amethyst_bud.name` |
| Large Amethyst Bud  | `large_amethyst_bud`  | `585`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.large_amethyst_bud.name`  |
| Amethyst Cluster    | `amethyst_cluster`    | `584`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.amethyst_cluster.name`    |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑ a b c dAvailable with /give command.
3. ↑ a b c dThe block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:

| Name        | Default value | Allowed values                                                | Description                                                        |
|-------------|---------------|---------------------------------------------------------------|--------------------------------------------------------------------|
| facing      | `up`          | `down`<br/>`east`<br/>`north`<br/>`south`<br/>`up`<br/>`west` | The direction the amethyst is facing, determined by its anchoring. |
| waterlogged | `false`       | `true`<br/>`false`                                            | Whether or not the amethyst is located inside ofwater.             |

Bedrock Edition:

| Name                 | Metadata Bits | Default value | Allowed values                                                | Values forMetadata Bits | Description                                                        |
|----------------------|---------------|---------------|---------------------------------------------------------------|-------------------------|--------------------------------------------------------------------|
| minecraft:block_face | Not Supported | `up`          | `down`<br/>`east`<br/>`north`<br/>`south`<br/>`up`<br/>`west` | `Unsupported`           | The direction the amethyst is facing, determined by its anchoring. |



