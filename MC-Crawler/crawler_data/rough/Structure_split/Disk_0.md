# Disk
A disk is a feature consisting of a naturally generated roughly circular deposit of a soil-like block under or next to bodies of water.

## Contents
- 1 Description
- 2 List
- 3 Data values
	- 3.1 ID
	- 3.2 Config
- 4 History
- 5 Gallery
	- 5.1 Screenshots
- 6 References

## Description
Disks are generated at the Euclidean distance n (i.e. x2+y2=n2) from a given central block, creating a circular-looking pattern of the given block with a radius of n. They are commonly seen throughout rivers, shallow oceans, swamps and mangrove swamps.

## List
| Block                                                        | Replaces blocks  | Minimum size (n) | Maximum size (n) | Biomes                                                                             |
|--------------------------------------------------------------|------------------|------------------|------------------|------------------------------------------------------------------------------------|
| Sand,<br/>Sandstone(When above air)                          | Dirt,Grass Block | 2                | 6                | All Overworld biomes exceptswamp,mangrove swamp, andswamp hills‌[BE  only](Unused) |
| Gravel                                                       | Dirt,Grass Block | 2                | 5                | All Overworld biomes exceptswamp,mangrove swamp, andswamp hills‌[BE  only](Unused) |
| Clay                                                         | Dirt,Clay        | 2                | 3                | All Overworld biomes                                                               |
| Grass Block,<br/>Dirt(when undersolid-material blockorWater) | Dirt,Mud         | 2                | 6                | mangrove swamp                                                                     |

## Data values
### ID
Java Edition:

| Feature type        | Identifier |
|---------------------|------------|
| [No displayed name] | `disk`     |

| Configured feature  | Identifier    |
|---------------------|---------------|
| [No displayed name] | `disk_clay`   |
| [No displayed name] | `disk_grass`  |
| [No displayed name] | `disk_gravel` |
| [No displayed name] | `disk_sand`   |

Bedrock Edition:

| Feature             | Identifier           |
|---------------------|----------------------|
| [No displayed name] | `clay_feature`       |
| [No displayed name] | `gravel_feature`     |
| [No displayed name] | `sand_feature`       |
| [No displayed name] | `grass_disc_feature` |

### Config
Main article: Configured feature
Java Edition:

- config
	- state_providerThe block to use.
		- fallback：The block to use when all the rules' predicates are not passed.
			- 
			- Block state provider
		- rules(Required, but can be empty) Rules of the block to use.
			- One rule.
				- if_trueThe predicate of this rule.
					- 
					- Block predicate
				- thenThe block to use when the predicate is passed.
					- 
					- Block state provider
	- radiusThe radius of this disk. Value between 0 and 8 (inclusive).
		- 
		- Int provider
	- half_heightHalf of the height of this disk. Value between 0 and 4 (inclusive).
	- targetThis predicate must be passed to generate this feature.
		- 
		- Block predicate


An example

{
  "type": "minecraft:disk",
  "config": {
    "half_height": 1,
    "radius": {
      "type": "minecraft:uniform",
      "value": {
        "max_inclusive": 3,
        "min_inclusive": 2
      }
    },
    "state_provider": {
      "fallback": {
        "type": "minecraft:simple_state_provider",
        "state": {
          "Name": "minecraft:clay"
        }
      },
      "rules": []
    },
    "target": {
      "type": "minecraft:matching_blocks",
      "blocks": [
        "minecraft:dirt",
        "minecraft:clay"
      ]
    }
  }
}




