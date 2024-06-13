# Fossil
A fossil is a rarely-occurring skeletal feature composed of bone blocks, coal ore, or diamond ore.

## Contents
- 1 Generation
- 2 Structure
- 3 Data values
	- 3.1 ID
	- 3.2 Config
- 4 History
- 5 Issues
- 6 Trivia
- 7 Gallery
	- 7.1 Renders
		- 7.1.1 Skulls
		- 7.1.2 Spines
	- 7.2 Screenshots
- 8 See also
- 9 References

## Generation
Fossils randomly generate only in desert, swamp and mangrove swamp‌[Java Edition  only] biomes, and generate at y levels 45 to -50. Each chunk has two attempts within y-coordinates 0 to 320 or -63 to -8 underground to generate a fossil, each with a chance of 1⁄64. They have an equal chance to generate as any of the four variants of skull or four variants of spine.

Fossils first generate the pure-bone layer with a structure integrity of 0.9, meaning 10% of the bone blocks are removed and do not override original terrain blocks, leaving 90% bone blocks. Next, the ore layer generates with a structure integrity of 0.1, replacing 10% of the existing fossil with coal ore for fossils that generate above Y level 0, or deepslate diamond ore for fossils that generate below Y level -8. The locations of these ore blocks do not always correspond with the voids generated in the initial bone fossil, so the resulting combination of both generations usually result in an incomplete fossil structure composed of bone blocks and ores.

Because fossils are features instead of structures, they generate even when the "Generate Structures" option is turned off.[2]

## Structure
Main article: /Structure
Naturally-generated fossils are composed of a mix of bone blocks and coal or diamond ores, as detailed above. They are made with NBT structure files and have files for each type of fossil located in the folder minecraft.jar/data/minecraft/structures/fossil.

There are 4 type of skulls and 4 type of spines.

| Structure file                             | Description                   | Consists of                                                 | Images |
|--------------------------------------------|-------------------------------|-------------------------------------------------------------|--------|
| `fossil/skull_1`<br/>`fossil/skull_1_coal` | The largest skull.            | 86 in total Bone Block, Coal Ore, or Deepslate Diamond Ore  |        |
| `fossil/skull_2`<br/>`fossil/skull_2_coal` | The second largest skull.     | 75 in total Bone Block, Coal Ore, or Deepslate Diamond Ore  |        |
| `fossil/skull_3`<br/>`fossil/skull_3_coal` | The second smallest skull.    | 58 in total Bone Block, Coal Ore, or Deepslate Diamond Ore  |        |
| `fossil/skull_4`<br/>`fossil/skull_4_coal` | The smallest skull, one-eyed. | 32 in total Bone Block, Coal Ore, or Deepslate Diamond Ore  |        |
| `fossil/spine_1`<br/>`fossil/spine_1_coal` | The narrowest spine.          | 37 in total Bone Block, Coal Ore, or Deepslate Diamond Ore  |        |
| `fossil/spine_2`<br/>`fossil/spine_2_coal` | The second narrowest spine.   | 61 in total Bone Block, Coal Ore, or Deepslate Diamond Ore  |        |
| `fossil/spine_3`<br/>`fossil/spine_3_coal` | The second widest spine.      | 97 in total Bone Block, Coal Ore, or Deepslate Diamond Ore  |        |
| `fossil/spine_4`<br/>`fossil/spine_4_coal` | The widest spine.             | 121 in total Bone Block, Coal Ore, or Deepslate Diamond Ore |        |

## Data values
### ID
Java Edition:

| Feature type        | Identifier |
|---------------------|------------|
| [No displayed name] | `fossil`   |

| Configured feature  | Identifier        |
|---------------------|-------------------|
| [No displayed name] | `fossil_coal`     |
| [No displayed name] | `fossil_diamonds` |

Bedrock Edition:

| Feature             | Identifier                         |
|---------------------|------------------------------------|
| [No displayed name] | `fossil_feature`                   |
| [No displayed name] | `deepslate_diamond_fossil_feature` |

### Config
Main article: Configured feature
Java Edition:

- config
	- fossil_structures: (Cannot be empty) A list of fossil structure templates to choose from.
		- :structure template(referenced byID)
	- overlay_structures: (Cannot be empty) A list of overlay structure templates to choose from. Has to have the same length asfossil_structures.
		- :structure template(referenced byID)
	- fossil_processors:processor list(referenced byID orinlined) — The processor for fossil structure templates.
	- overlay_processors:processor list(referenced byID orinlined) — The processor for overlay structure templates.
	- max_empty_corners_allowed: Integer between 0 and 7 — How many corners of the structure are allowed to be empty for it to generate. Prevents structures floating in the air.


An example

{
  "type": "minecraft:fossil",
  "config": {
    "fossil_processors": "minecraft:fossil_rot",
    "fossil_structures": [
      "minecraft:fossil/spine_1",
      "minecraft:fossil/spine_2",
      "minecraft:fossil/spine_3",
      "minecraft:fossil/spine_4",
      "minecraft:fossil/skull_1",
      "minecraft:fossil/skull_2",
      "minecraft:fossil/skull_3",
      "minecraft:fossil/skull_4"
    ],
    "max_empty_corners_allowed": 4,
    "overlay_processors": "minecraft:fossil_coal",
    "overlay_structures": [
      "minecraft:fossil/spine_1_coal",
      "minecraft:fossil/spine_2_coal",
      "minecraft:fossil/spine_3_coal",
      "minecraft:fossil/spine_4_coal",
      "minecraft:fossil/skull_1_coal",
      "minecraft:fossil/skull_2_coal",
      "minecraft:fossil/skull_3_coal",
      "minecraft:fossil/skull_4_coal"
    ]
  }
}



