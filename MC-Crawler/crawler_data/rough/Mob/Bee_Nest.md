# Bee Nest
A bee nest is a naturally occuring block that houses bees. They fill with honey as bees pollinate flowers and return to their homes and, when full, can either be sheared for honeycombs or honey bottles extracted using glass bottles.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Post-generation
- 2 Usage
	- 2.1 Bee housing
	- 2.2 Harvesting
	- 2.3 Redstone component
	- 2.4 Note blocks
	- 2.5 Fuel
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
	- 4.3 Block data
- 5 Achievements
- 6 Advancements
- 7 History
- 8 Issues
- 9 See also
- 10 Gallery
	- 10.1 Renders
		- 10.1.1 Bee nest
		- 10.1.2 On tree
	- 10.2 Screenshots
	- 10.3 In other media
- 11 References

## Obtaining
### Breaking
See also: Tutorials/Honey farming § Avoiding Bee Anger

Bee nests can be broken by any tool or by the player's fist, though they break faster with an axe. 

If a bee nest is broken with a tool not enchanted with Silk Touch, it drops nothing and any bees inside emerge angry at the player, stinging them and causing poison. Nearby bees will also become angry and attack. If a Silk Touch tool is used, the bee nest drops itself and any bees inside remain inside, and any bees nearby do not become angry. 

If broken in Creative mode with bees inside, the bee nest drops itself and bees inside remain inside.

| Block     | Bee Nest              |
|-----------|-----------------------|
| Hardness  | 0.3                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 0.45                  |
| Wooden    | 0.25                  |
| Stone     | 0.15                  |
| Iron      | 0.1                   |
| Diamond   | 0.1                   |
| Netherite | 0.05                  |
| Golden    | 0.05                  |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
A naturally generated bee nest in a village in a Superflat world.
Naturally generated bee nests generate with 3 bees in them. The bee nests always face south.

Bee nests generate in the following biomes with different chances:

| Biome                                               | Chance[note 1] |                 |  |
|-----------------------------------------------------|----------------|-----------------|--|
|                                                     | Java Edition   | Bedrock Edition |  |
| Meadow                                              |                | 100%            |  |
| Cherry grove                                        | 5%             | Unknown         |  |
| Plains<br/>Sunflower plains                         |                | 5%              |  |
| Mangrove swamp                                      | 5%             | 4%              |  |
| Flower forest                                       | 2%             | 3%              |  |
| Forest<br/>Birch forest<br/>Old growth birch forest | 0.2%           | 0.035%          |  |

1. ↑The chance for each naturally-generated oak, birch, mangrove tree, or cherry tree to have a bee nest.


### Post-generation
Oak, birch, or cherry trees grown from saplings that are within 2 blocks (including diagonally) of a flower on the same Y-level have a 5% chance to grow with a bee nest containing 1–3 bees. This holds true in any biome in any dimension, and for any flower including wither roses and flowering azaleas.

## Usage
### Bee housing
Dripping honey.
Bee nests and beehives can house up to 3 bees at a time. They can enter through any unobstructed side, top, or bottom, but can exit only from the front, and only if it's unobstructed by a solid block (including a non-full solid block in Bedrock Edition).

Bees fly into a nest or hive at night, during rain, and after loading up with pollen from a flower. They first look for one at the same coordinates as the last one they entered, but if there's no nest or hive there, or it already contains 3 bees when they arrive, they search the nearby area for another one.

Igniting a nest or hive allows any bees inside to escape, possibly catching fire as they flee.

### Harvesting
See also: Tutorials/Honey farming

Bees are protected from a campfire by placing a carpet over it.‌[Java Edition  only]
Once full, bee nests and beehives provide two harvestable products: honey and honeycomb.

Each time a bee enters a nest or hive covered in pollen, it starts converting it to honey and honeycomb. After it's done, it waits for daylight with no rain (if necessary), then exits to go collect more pollen. If the bee hive or nest is in the Nether or in the End the bee exits as soon as it converts the pollen. When the bee exits, the hive increments its honey level by 1 and has a 1% chance to increment it by 2. Once it has the maximum honey level of 5, it changes its appearance to show honey oozing out and, if the block below it isn't a full solid block, starts dripping honey particles. (The dripping honey is decorative; it cannot be collected in a cauldron.) These changes signal that the hive or nest is ready for harvesting.

To harvest honey, the player uses a glass bottle on the nest or hive; the bottle then becomes a honey bottle. To harvest honeycomb, the player uses shears on the nest or hive, causing it to drop three honeycomb items. After harvesting, the hive or nest is reset to empty (honey level 0, with the default appearance).

Alternatively, honey or honeycomb can be harvested by powering a redstone dispenser containing either a glass bottle or shears. The dispenser must be placed beside and facing the hive or nest.

This is the maximum distance a beehive can be from a campfire while applying the calming effect (5 blocks).
Harvesting from a beehive or bee nest causes any bees inside it to become aggravated toward the player, unless there is a fire directly beneath it or a lit campfire within five blocks below, and the smoke is not obstructed. Smoke can pass through no more than one solid block, and only if that block is directly above the campfire. Placing a carpet above the campfire leaves room for the bees to hover beneath the nest and still avoid taking fire damage. In Java Edition, the smoke coming through the carpet also calms the bees. In Bedrock Edition, a carpet is treated as an obstruction that removes the calming effect of the campfire's smoke. Without a block covering the fire, the bees can still avoid fire damage if the campfire is placed 4–5 blocks below the nest.

### Redstone component
Beehives and bee nests have comparator output with a strength equal to the honey level in the block. Once the beehive or bee nest is filled with honey it emits a signal strength of five.

### Note blocks
Beehives and bee nests can be placed under note blocks to produce "bass" sound.

### Fuel
In Bedrock Edition, beehives and bee nests can be used as fuel in a furnace, smelting 1.5 items per block.



## Data values
### ID
Java Edition:

| Name     | Identifier | Form         | Block tags | Translation key            |
|----------|------------|--------------|------------|----------------------------|
| Bee Nest | `bee_nest` | Block & Item | `beehives` | `block.minecraft.bee_nest` |

| Name         | Identifier |
|--------------|------------|
| Block entity | `beehive`  |

Bedrock Edition:

| Name     | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key      |
|----------|------------|------------|----------------------------|----------------|----------------------|
| Bee Nest | `bee_nest` | `473`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.bee_nest.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

| Name         | Savegame ID |
|--------------|-------------|
| Block entity | `Beehive`   |

### Block states
Java Edition:

| Name        | Default value | Allowed values                              | Description                                                                                                                                                     |
|-------------|---------------|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing      | `north`       | `east`<br/>`north`<br/>`south`<br/>`west`   | The opposite from the direction the player faces while placing the block.                                                                                       |
| honey_level | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | Every pollinated bee that leaves the hive after working increases the honey level by one. When at level 5, honey can be bottled or honeycombs can be harvested. |

Bedrock Edition:

| Name        | Metadata Bits | Default value | Allowed values                              | Values forMetadata Bits | Description                                                                                                                                                     |
|-------------|---------------|---------------|---------------------------------------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| direction   | Not Supported | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`                 | `Unsupported`           | The direction the block faces.0: south<br/>1: west<br/>2: north<br/>3: east<br/>                                                                                |
| honey_level | Not Supported | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | `Unsupported`           | Every pollinated bee that leaves the hive after working increases the honey level by one. When at level 5, honey can be bottled or honeycombs can be harvested. |



### Block data
A beehive has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format

- Block entity data
	- 
	- Tags common to all block entities
	- Bees: Entities currently in the hive.
		- An entity in the hive.
			- EntityData: The NBT data of the entity in the hive.
				- Seeentity format.
			- MinOccupationTicks: The minimum amount of time in ticks for this entity to stay in the hive.
			- TicksInHive: The amount of ticks the entity has stayed in the hive.
	- FlowerPos: Stores the location of a flower, so other bees can go to it.
		- X: X coordinate of the flower.
		- Y: Y coordinate of the flower.
		- Z: Z coordinate of the flower.

Bedrock Edition:

SeeBedrock Edition level format/Block entity format.
