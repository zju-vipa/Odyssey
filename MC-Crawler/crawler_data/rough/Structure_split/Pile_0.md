# Pile
A pile is a feature that generates only inside villages.

## Contents
- 1 Generation
- 2 Data values
	- 2.1 ID
	- 2.2 Config
- 3 History

## Generation
There are five variants of pile: hay, ice, melon, pumpkin, and snow. Hay piles generate with hay bales, ice piles generate with packed ice and sometimes blue ice, melon piles generate with melons, pumpkin piles generates with pumpkins and sometimes jack o'lanterns, and snow piles generate with snow. Piles can generate only in villages.

The pile variants spawn naturally in the indicated villages:

| Village type    | Hay Bale | Packed Ice | Melon | Pumpkin | Snow |
|-----------------|----------|------------|-------|---------|------|
| Plains Village  | Yes      |            |       |         |      |
| Desert Village  | Yes      |            |       |         |      |
| Savanna Village | Yes      |            | Yes   |         |      |
| Snowy Village   |          | Yes        |       |         | Yes  |
| Taiga village   |          |            |       | Yes     |      |

## Data values
### ID
Java Edition:

| Feature type        | Identifier   |
|---------------------|--------------|
| [No displayed name] | `block_pile` |

Java Edition:

| Configured feature  | Identifier     |
|---------------------|----------------|
| [No displayed name] | `pile_hay`     |
| [No displayed name] | `pile_ice`     |
| [No displayed name] | `pile_melon`   |
| [No displayed name] | `pile_pumpkin` |
| [No displayed name] | `pile_snow`    |

Bedrock Edition:

| Feature             | Identifier             |
|---------------------|------------------------|
| [No displayed name] | `hay_pile_feature`     |
| [No displayed name] | `ice_pile_feature`     |
| [No displayed name] | `melon_pile_feature`   |
| [No displayed name] | `pumpkin_pile_feature` |
| [No displayed name] | `snow_pile_feature`    |

### Config
Main article: Configured feature
Java Edition:

- config
	- state_providerThe block to use.
		- 
		- Block state provider


An example

{
  "type": "minecraft:block_pile",
  "config": {
    "state_provider": {
      "type": "minecraft:rotated_block_provider",
      "state": {
        "Name": "minecraft:hay_block",
        "Properties": {
          "axis": "y"
        }
      }
    }
  }
}




