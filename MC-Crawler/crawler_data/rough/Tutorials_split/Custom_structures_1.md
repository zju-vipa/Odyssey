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


