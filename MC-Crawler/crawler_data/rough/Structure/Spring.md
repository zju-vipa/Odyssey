# Spring
A spring is a feature of a single unit of liquid that generates within the world, flowing out into spaces level with or lower than the source.

## Contents
- 1 Types of springs
	- 1.1 Normal springs
	- 1.2 Ceiling springs
	- 1.3 Hidden lava
- 2 Data values
	- 2.1 ID
	- 2.2 Config
- 3 History
- 4 Gallery
	- 4.1 Screenshots
- 5 References

## Types of springs
There are three main categories of fluid springs.

### Normal springs
A water spring as viewed from inside a cave.
This most familiar type of spring can generate as either water or lava, and generate in the sides of stone surfaces. These are commonly encountered on the sides of cliffs, as well as inside caves. Lava springs are a common source of forest fires.

### Ceiling springs
These types of springs are exclusive to the Nether, and generate only as lava. As their name implies, they generate on ceilings, and the liquid flows directly downwards from them. These are quite common sightings in the Nether, and the resultant lava spreading can sometimes make traversing terrain difficult.

### Hidden lava
A closed nether spring near a quartz ore blob.
Unlike the other types of springs, these are hidden from generation. These are particularly dangerous and care must be taken (like taking a Potion of Fire Resistance) when mining in the Nether, as they can be dangerous when uncovered.

## Data values
### ID
Java Edition:

| Feature type        | Identifier       |
|---------------------|------------------|
| [No displayed name] | `spring_feature` |

| Configured feature  | Identifier              |
|---------------------|-------------------------|
| [No displayed name] | `spring_water`          |
| [No displayed name] | `spring_lava_overworld` |
| [No displayed name] | `spring_lava_frozen`    |
| [No displayed name] | `spring_lava_nether`    |
| [No displayed name] | `spring_nether_closed`  |
| [No displayed name] | `spring_nether_open`    |

Bedrock Edition:

| Feature                | Identifier                         |
|------------------------|------------------------------------|
| [No displayed name]    | `lava_spring_feature`              |
| [No displayed name]    | `water_spring_feature`             |
| [No displayed name]    | `minecraft:legacy:springs_feature` |
| [No displayed name][1] | `[No ID]`                          |

### Config
Main article: Configured feature
Java Edition:

- config
	- stateThe fluid to use.
		- 
		- Block state
	- rock_count(optional, defaults to 4) The required number of blocks adjacent to the spring that belong tovalid_blocks.
	- hole_count(optional, defaults to 1) The required number of air blocks adjacent to the spring.
	- requires_block_below(optional, defaults to true) Whether the spring feature requires a block invalid_blocksbelow the fluid.
	- valid_blocksCan be a block ID or a block tag, or a list of block IDs.


An example

{
  "type": "minecraft:spring_feature",
  "config": {
    "hole_count": 1,
    "requires_block_below": true,
    "rock_count": 4,
    "state": {
      "Name": "minecraft:water",
      "Properties": {
        "falling": "true"
      }
    },
    "valid_blocks": [
      "minecraft:stone",
      "minecraft:granite",
      "minecraft:diorite",
      "minecraft:andesite",
      "minecraft:deepslate",
      "minecraft:tuff",
      "minecraft:calcite",
      "minecraft:dirt",
      "minecraft:snow_block",
      "minecraft:powder_snow",
      "minecraft:packed_ice"
    ]
  }
}



