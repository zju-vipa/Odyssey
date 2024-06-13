# Tutorials/Custom structures
This tutorial explains how to create a data pack that adds a custom structure to the world. It assumes you already know how to create a data pack.

pack.mcmeta
## Contents
- 1 Structure Set
- 2 Structure
- 3 Template pool
- 4 Structure NBT

## Structure Set
A structure set is where the placement starts. It defines where in the world the structure should be placed, and how rare it is.

data/example/worldgen/structure_set/tall_towers.json
{
  "structures": [
    {
      "structure": "example:tall_tower",
      "weight": 1
    }
  ],
  "placement": {
    "type": "minecraft:random_spread",
    "spacing": 5,
    "separation": 2,
    "salt": 1646207470
  }
}

Structure sets are made up of two parts:

- structurestakes a weighted list of different structures(see below), allowing structure variants (for example the vanilla Nether has a structure set with both the bastion and fortress).
- placementspecifies in which chunks to spawn the structure. The simplest option israndom_spreadwhere you can give the average distance in chunks (spacing) and the minimum distance in chunks (separation). Thesaltis then used together with the world seed to randomly place structures in a chunk grid.


Full JSON format

: Root object.
 structures: (Required, but can be empty) The structures that may be placed. One configured structure feature shouldn't be included by two structure sets.
: A structure to be placed.
 structure: structure (referenced by  ID or  inlined) — The structure to be placed.
 weight: Determines the chance of it being chosen over others. Must be a positive integer.
 placement: How the structures should be placed.
 salt: A number that assists in randomization; see salt (cryptography). Must be a non-negative integer.
 frequency: (Optional, default to 1.0) Probability to try to generate if other conditions below are met. Values between 0.0 to 1.0 (inclusive). Setting it to a number does not mean one structure is generated this often, only that the game attempts to generate one; biomes or terrain could lead to the structure not being generated.
 frequency_reduction_method: (Optional, defaults to default) Provides a random number generator algorithm for frequency. One of default (the random number depends on the seed, position and  salt), legacy_type_1 (the random number depends only on the seed and position, and randomness only occurs when the locations differ greatly), legacy_type_2 (same as default, but with fixed salt: 10387320) and legacy_type_3 (the random number depends only on seed and position).
 exclusion_zone: Specifies that it cannot be placed near certain structures.
 chunk_count: Value between 1 and 16 (inclusive).
 other_set: A structure set ID.
 locate_offset: (optional, defaults to [0,0,0]) The chunk coordinate offset given when using /locate structure.
: X. Value between -16 and 16 (inclusive).
: Y. Value between -16 and 16 (inclusive).
: Z. Value between -16 and 16 (inclusive).
 type: One of minecraft:concentric_rings or minecraft:random_spread.
Additional fields depending on value of  type, see Placement types.



## Structure
The structure is the ID you will be able to reference in the /locate command. It contains the configuration on what to place in the world, in which biomes, as well as structure properties like mob spawns.

data/example/worldgen/structure/tall_tower.json
{
  "type": "minecraft:jigsaw",
  "biomes": "#minecraft:has_structure/mineshaft",
  "step": "surface_structures",
  "spawn_overrides": {},
  "terrain_adaptation": "beard_thin",
  "start_pool": "example:tall_tower",
  "size": 1,
  "start_height": {
    "absolute": 0
  },
  "project_start_to_heightmap": "WORLD_SURFACE_WG",
  "max_distance_from_center": 80,
  "use_expansion_hack": false
}

When creating custom structures, you should always set  type to jigsaw. The  biomes field is a biome tag controlling which biomes are allowed to spawn this structure in. The  start_pool references a template pool (see below) which will define the actual structure layout. If you want to use jigsaws, make sure to increase the  size value. It is the jigsaw depth limit and it has a maximum of 20.

Full JSON format of jigsaw structures:


jigsaw



 Structure configuration
 type: jigsaw
Fields common to all structures
 start_pool: template pool (referenced by  ID or  inlined) — The template pool the structure starts from.
 size: Value between 0 and 20 (inclusive) — The depth of jigsaw structures to generate.
 start_height: If project_start_to_heightmap is unset, the structure will start at the value provided. Otherwise, the value acts as an offset from the heightmap.
Height provider
 project_start_to_heightmap: (optional) The heightmap the start height should project to. Can be WORLD_SURFACE_WG, WORLD_SURFACE, OCEAN_FLOOR_WG, OCEAN_FLOOR, MOTION_BLOCKING, or MOTION_BLOCKING_NO_LEAVES.
 start_jigsaw_name: (optional) The name of the jigsaw block the structure start attaches to.
 max_distance_from_center: The maximum 3D Chebyshev distance from the jigsaw pieces to the structure start. Value between 1 and 128 (inclusive) when  terrain_adaptation is "none", otherwise from 1 to 116 (inclusive).
 use_expansion_hack: Only used in villages.
 pool_aliases: (optional) used to rewire jigsaw pool connections by redirecting pool references on individual structure instances.
: pool alias



## Template pool
The template pool defines how to build up your structure. The example in this tutorial does not use jigsaw, so this is quite straight forward: we want to place a single structure NBT file.

data/example/worldgen/template_pool/tall_tower.json
{
  "fallback": "minecraft:empty",
  "elements": [
    {
      "weight": 1,
      "element": {
        "element_type": "minecraft:single_pool_element",
        "location": "example:stone_tall_tower",
        "projection": "rigid",
        "processors": "minecraft:empty"
      }
    }
  ]
}

A single structure is selected from the  elements list. You can add structure variants by adding multiple elements here. The  location field references a structure NBT file


Full JSON format

 The root tag
 fallback: template pool (referenced by  ID) — Used as fallback if structures in this pool can't generate.
 elements: A list of elements to randomly select from.
: An element.
 weight: How likely this element is to be chosen when using this pool. Value between 1 and 150 (inclusive).
 element: The properties of this element.
 projection: Can be rigid to place a fixed structure (like a house), or terrain_matching to match the terrain height (like a village road).
 element_type: Can be minecraft:empty_pool_element to generate nothing, minecraft:feature_pool_element to generate a placed feature, minecraft:list_pool_element to generate multiple elements one after another (lower elements replace their front ones), and minecraft:legacy_single_pool_element or minecraft:single_pool_element to generate a structure template. The difference between legacy_single_pool_element and single_pool_element, is that the legacy_single_pool_element does not replace existing blocks with air, and the single_pool_element replaces blocks with air and relies on the structure_void block to avoid not replacing blocks.
If  element_type is feature_pool_element, additional fields are as follows:
 feature: placed feature (referenced by  ID or  inlined) — The feature to place.
If  element_type is list_pool_element, additional fields are as follows:
 elements: A list of elements to choose from.
: An element, with the same format above.
If  element_type is legacy_single_pool_element or single_pool_element, additional fields are as follows:
 location: structure template (referenced by  ID) — The template to place
 processors: processor list (referenced by  ID or  inlined) — The processors that should modify the template.



## Structure NBT
The final piece to get a custom structure in your world is to have a structure NBT file.

data/example/structures/stone_tall_tower.nbt

You can create your own structure in-game, or download this one

| World generation | Dimensions Dimension types World presets Biomes Carvers Configured features Placed features   Noise settings   Noise router Density functions Noises Surface rules    Structures   Structure sets Template pools Processor lists Structure templates |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Noise settings   | Noise router<br/>Density functions<br/>Noises<br/>Surface rules<br/>                                                                                                                                                                                 |
| Structures       | Structure sets<br/>Template pools<br/>Processor lists<br/>Structure templates<br/>                                                                                                                                                                   |

| Noise settings | Noise router Density functions Noises Surface rules |
|----------------|-----------------------------------------------------|

| Structures | Structure sets Template pools Processor lists Structure templates |
|------------|-------------------------------------------------------------------|

| World generation | Adding a new dimension Custom structures |
|------------------|------------------------------------------|

