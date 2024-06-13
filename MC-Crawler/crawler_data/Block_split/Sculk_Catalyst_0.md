# Sculk Catalyst
A sculk catalyst is a block that converts blocks around it to blocks in the sculk family (except for more sculk catalysts) when a mob or player that drops experience dies nearby. 

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Mob loot
	- 1.4 Chest loot
- 2 Usage
	- 2.1 Blooming
		- 2.1.1 Blooming range
		- 2.1.2 Sculk charges
	- 2.2 Sculk growth
		- 2.2.1 Discharging
		- 2.2.2 Blooming without spreading
	- 2.3 Light source
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
	- 4.3 Block data
- 5 Advancements
- 6 History
- 7 Issues
- 8 Trivia
- 9 Gallery
	- 9.1 Textures
	- 9.2 Screenshots
- 10 References

## Obtaining
### Breaking
A sculk catalyst can be mined with any tool, but hoes are the quickest. It drops 5 experience if mined without Silk Touch.

| Block     | Sculk Catalyst        |
|-----------|-----------------------|
| Hardness  | 3                     |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 4.5                   |
| Wooden    | 2.25                  |
| Stone     | 1.15                  |
| Iron      | 0.75                  |
| Diamond   | 0.6                   |
| Netherite | 0.5                   |
| Golden    | 0.4                   |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


### Natural generation
Sculk catalysts are generated within the deep dark biome.


### Mob loot
A warden drops a single sculk catalyst upon death, unaffected by Looting.

| Source | Roll Chance | Quantity (Roll Chance) |           |            |             |
|--------|-------------|------------------------|-----------|------------|-------------|
|        |             | Default                | Looting I | Looting II | Looting III |
| Warden | 100%        | 1                      | 1         | 1          | 1           |

### Chest loot
| Item           | Structure    | Container | Quantity | Chance                         |
|----------------|--------------|-----------|----------|--------------------------------|
|                |              |           |          | Java EditionandBedrock Edition |
| Sculk Catalyst | Ancient City | Chest     | 1–2      | 16.1%                          |

## Usage
Sculk catalyst blooming.
Sculk catalysts convert experience into sculk veins, sculk sensors, and sculk shriekers, and use experience to convert many natural blocks into sculk.
Sculk catalyst detection range.
It turns the blocks around the dead Mob into sculk or sculk veins.
### Blooming
When a living entity (a mob or player) dies near a sculk catalyst, it blooms. This sculk bloom converts the entity's experience into sculk charges, which can grow new sculk blocks, sensors and shriekers. Sculk blocks are always produced, with up to 1 sculk block per experience point. A sculk charge also has a 9% chance to grow a sculk sensor, and a 1% chance to grow to generate a sculk shrieker.

A bloom occurs for the death of any living entity, and can even consume multiple entities at once. Sculk blooms work on every living entity (including ender dragons [1][2], withers, and wardens). A sculk bloom cannot occur if the entity is not directly above a solid block or if the entity is below the sculk catalyst. This means pointed dripstone cannot be used to make a simple sculk farm, since sculk growth cannot happen when mobs die on pointed dripstone stalagmites.

During a sculk bloom, the catalyst gives off soul particles, and creates a patch of sculk blocks with sculk veins around them. Sculk blooms can replace blocks in the sculk_replaceable tag, including the surface materials of most of the biomes in all the Overworld, Nether, and End.

Sculk blooms occur only in response to deaths. Other sources of experience are simply ignored.

#### Blooming range
A sculk bloom occur for the death of any living entity within a Euclidean distance of 8 blocks in Java Edition or 10 blocks in Bedrock Edition from a sculk catalyst.

If the entity dies near multiple sculk catalysts, only the nearest sculk catalyst blooms.

#### Sculk charges
When a living entity (a player or mob), is consumed by a sculk bloom, it won't drop experience, because the sculk bloom event converts the entity's experience into sculk charges. 1 sculk charge is generated per experience point the mob would have dropped if it was killed by a player or a tamed wolf. These charges are used to convert the block beneath the entity into a sculk block. If the block is already a sculk block, or if there are extra sculk charges, the sculk block absorbs the sculk charges. Up to 1000 charges can be present in one block. Considering how unlikely it is for a sculk block to receive the maximum number charges, sculk blocks can store essentially unlimited charges.

The sculk charge in a block is lost when the block is destroyed or broken.

### Sculk growth

Sculk growth is an event where a sculk bloom starts on a non-sculk block. The sculk growth first tries to convert the charged block into a sculk block. The following blocks can be converted:

Stone
Granite
Andesite
Diorite
Tuff
Calcite
Deepslate
Dripstone Block
Terracotta
Netherrack
Nylium
Basalt
Smooth Basalt
Blackstone
End Stone
Gravel
Sand
Red sand
Sandstone
Red Sandstone
Dirt
Grass Block
Mycelium
Podzol
Coarse Dirt
Rooted Dirt
Clay
Moss Block
Mud
Muddy Mangrove Roots
Soul Sand
Soul Soil
in Java Edition, these blocks are marked under the sculk_replaceable tag.

Sculk growth can grow all of the sculk family blocks, except for more sculk catalysts:

If the charged block can't be converted, sculk veins grow on the block instead. If sculk veins can't grow, the sculk charge is removed and nothing happens.

Each sculk block costs 1 experience to grow, but some sculk charges are used to grow sensors or shriekers, or are lost to decay.

When a sculk block is grown, it also tries to grow sculk veins on every face of every blocks adjacent to it. This can produce upto 20 sculk veins. Each sculk vein costs 1 sculk charge when it grows on a block that cannot be converted into sculk.

Sculk growth can't happen on a block that is completely covered by blocks, unless some of those blocks are sculk veins.

Sculk veins are never placed on the sides of a sculk block and they are removed when the block they are attached to is converted to a sculk block.

