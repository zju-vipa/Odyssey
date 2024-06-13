# Lava lake
A lava lake is a small, widespread, naturally-generated feature in the Overworld that contains a volume of lava.

## Contents
- 1 Description
- 2 Generation
- 3 Data values
	- 3.1 ID
	- 3.2 Config
- 4 History
- 5 Issues
- 6 Gallery
	- 6.1 Screenshots
- 7 References

## Description
Lava lakes are shallow and often small bodies of liquid. Lava lakes found at the surface are surrounded by stone, which can be replaced by other features such as ore features of blocks such as dirt, gravel, and coal ore.

Lava lakes generate with a small air pocket above them, which may result in floating sand, floating snow cover, or even floating trees above[1]. Lava lakes that spawn on ground level may cause nearby trees to catch on fire and burn away.

## Generation
Lava lakes are rare on the surface but often found underground above Y=0, and replace blocks around them with stone. They can generate in any biomes in Overworld except the deep dark.

In Java Edition, the air pockets above lakes are generated with cave air instead of normal air. This is true even for lakes that are exposed to the open sky.

## Data values
### ID
Java Edition:

| Feature type        | Identifier |
|---------------------|------------|
| [No displayed name] | `lake`     |

| Configured feature  | Identifier  |
|---------------------|-------------|
| [No displayed name] | `lake_lava` |

Bedrock Edition:

| Feature             | Identifier |
|---------------------|------------|
| [No displayed name] | `[No ID]`  |

### Config
Main article: Configured feature
Java Edition:

- config
	- fluidThe block to use for the fluid of the lake.
		- 
		- Block state provider
	- barrierThe block to use for the barrier of the lake.
		- 
		- Block state provider


An example

{
  "type": "minecraft:lake",
  "config": {
    "barrier": {
      "type": "minecraft:simple_state_provider",
      "state": {
        "Name": "minecraft:stone"
      }
    },
    "fluid": {
      "type": "minecraft:simple_state_provider",
      "state": {
        "Name": "minecraft:lava",
        "Properties": {
          "level": "0"
        }
      }
    }
  }
}




