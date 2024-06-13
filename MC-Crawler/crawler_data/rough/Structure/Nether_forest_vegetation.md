# Nether forest vegetation
Nether forest vegetation is a feature that generates surface vegetation in the crimson forest and warped forest biomes.

## Contents
- 1 Data values
	- 1.1 ID
	- 1.2 Config
- 2 History

## Data values
### ID
Java Edition:

| Feature type        | Identifier                 |
|---------------------|----------------------------|
| [No displayed name] | `nether_forest_vegetation` |

| Configured feature  | Identifier                           |
|---------------------|--------------------------------------|
| [No displayed name] | `crimson_forest_vegetation`          |
| [No displayed name] | `crimson_forest_vegetation_bonemeal` |
| [No displayed name] | `warped_forest_vegetation`           |
| [No displayed name] | `warped_forest_vegetation_bonemeal`  |
| [No displayed name] | `nether_sprouts`                     |
| [No displayed name] | `nether_sprouts_bonemeal`            |

Bedrock Edition:

| Feature             | Identifier               |
|---------------------|--------------------------|
| [No displayed name] | `crimson_fungus_feature` |
| [No displayed name] | `warped_fungus_feature`  |
| [No displayed name] | `warped_roots_feature`   |
| [No displayed name] | `nether_sprouts_feature` |

which is used in:

| Feature             | Identifier                       |
|---------------------|----------------------------------|
| [No displayed name] | `crimson_fungus_scatter_feature` |
| [No displayed name] | `warped_fungus_scatter_feature`  |
| [No displayed name] | `warped_roots_scatter_feature`   |
| [No displayed name] | `nether_sprouts_scatter_feature` |

### Config
Main article: Configured feature
Java Edition:

- config
	- state_providerThe block to use.
		- 
		- Block state provider
	- spread_widthThe horizonal distance to spread to. The max width isspread_width * 2 -1. Must be a positive integer.
	- spread_heightThe vertical distance to spread. The max height isspread_height * 2 -1. Must be a positive integer.


An example

{
  "type": "minecraft:nether_forest_vegetation",
  "config": {
    "spread_height": 4,
    "spread_width": 8,
    "state_provider": {
      "type": "minecraft:simple_state_provider",
      "state": {
        "Name": "minecraft:nether_sprouts"
      }
    }
  }
}



