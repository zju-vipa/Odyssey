### Config
Main article: Configured feature
Java Edition:

- config
	- ignore_vines(optional, defaults to false) Allows the tree to generate even if there are vines blocking it.
	- force_dirt(optional, defaults to false) If true, places the dirt provider even when the block below the tree is a valid dirt-like block.
	- dirt_providerThe block to place below the trunk. Places only ifforce_dirtis true, or if there is not a valid dirt-like block below the trunk.
		- 
		- Block state provider
	- trunk_providerThe block to use for the trunk. Note that when the trunk placer isfancy_trunk_placer, the block must haveaxisproperty, such as logs.
		- 
		- Block state provider
	- foliage_providerThe block to use for the foliage.
		- 
		- Block state provider
	- minimum_sizeDefines the width of the tree at different heights relative to the lowest trunk block, for the minimum size of the feature.
		- min_clipped_height(optional) Value between 0 and 80 (inclusive). If the possible height at this location is lower than trunk height, but greater or equal to this value, the tree generates anyway. If not specified, the tree won't generate as long as the possible height is lower than trunk height. If the possible height at this location is lower than this value, the tree cannot generate.
		- typeOne oftwo_layers_feature_sizeorthree_layers_feature_sizeIf type is two_layers_feature_size, additional fields are as follows
		- limit(optional, defaults to 1) Value between 0 and 81 (inclusive). At heights lower than this value,lower_sizeis used, otherwiseupper_size.
		- lower_size(optional, defaults to 0) Value between 0 and 16 (inclusive). Minimum width of the tree at heights underlimit.
		- upper_size(optional, defaults to 1) Value between 0 and 16 (inclusive). Minimum width of the tree at heights greater than or equalslimit.If type is three_layers_feature_size, additional fields are as follows
		- limit(optional, defaults to 1) Value between 0 and 80 (inclusive). At heights lower than this value,lower_sizeis used, otherwiseupper_sizeormiddle_size.
		- upper_limit(optional, defaults to 1) Value between 0 and 80 (inclusive). At heights between this andlimit,middle_sizeis used. If the height is greater or equals, it usesupper_size.
		- lower_size(optional. defaults to 0) Value between 0 and 16 (inclusive). Minimum width of the tree at the lowest layer.
		- middle_size(optional, defaults to 1) Value between 0 and 16 (inclusive). Minimum width of the tree at the middle layer.
		- upper_size(optional, defaults to 1) Value between 0 and 16 (inclusive). Minimum width of the tree at the upper layer.
	- root_placer(optional) Controls how tree's roots are generated.
		- typeType of tree root placer, currently onlymangrove_root_placer.
		- root_providerThe block used as the root of the tree.
			- 
			- Block state provider
		- trunk_offset_yOffset perpendicular to the trunk.
			- 
			- Int provider
		- above_root_placement(optional) The blocks above the root.
			- above_root_providerThe block above the root.
				- 
				- Block state provider
			- above_root_placement_chanceThe probability of generating the block. Value between 0.0 and 1.0 (inclusive).
		- mangrove_root_placementMangrove root placement parameter.
			- max_root_widthThe maximum width of the root. Value between 1 and 12 (inclusive).
			- max_root_lengthThe maximum length of the root. Value between 1 and 64 (inclusive).
			- random_skew_chanceThe probability of random skew. Value between 0.0 and 1.0 (inclusive).
			- can_grow_throughA block ID or a block tag, or a list of block IDs. Blocks that roots can grow through.
			- muddy_roots_inA block ID or a block tag, or a list of block IDs. Roots in it will turn into muddy root blocks.
			- muddy_roots_providerBlocks used as muddy roots.
				- 
				- Block state provider
	- trunk_placer
		- base_heightValue between 0 and 32 (inclusive).
		- height_rand_aValue between 0 and 24 (inclusive).
		- height_rand_bValue between 0 and 24 (inclusive).
		- typeOne ofstraight_trunk_placer,forking_trunk_placer,giant_trunk_placer,mega_jungle_trunk_placer,dark_oak_trunk_placer,fancy_trunk_placer,bending_trunk_placer,upwards_branching_trunk_placer, orcherry_trunk_placer.If type is bending_trunk_placer, additional fields are as follows
		- bend_lengthValue between 1 and 64 (inclusive).
			- 
			- Int provider
		- min_height_for_leaves(optional, defaults to 1) Must be a positive integer.If type is upwards_branching_trunk_placer, additional fields are as follows
		- extra_branch_stepsThe number of steps to generate extra branches. Must be a positive integer.
			- 
			- Int provider
		- extra_branch_lengthGenerates extra branch length. Must be a non-negative integer.
			- 
			- Int provider
		- place_branch_per_log_probabilityThe probability of each log producing a branch. Value between 0.0 and 1.0 (inclusive).
		- can_grow_throughA block ID or a block tag, or a list of block IDs. Represents blocks that tree trunks can grow through.If type is cherry_trunk_placer, additional fields are as follows
		- branch_countValue between 1 and 3 (inclusive).
			- 
			- Int provider
		- branch_horizontal_lengthValue between 2 and 16 (inclusive).
			- 
			- Int provider
		- branch_start_offset_from_topA uniform int provider, which provides a number between two bounds with uniform distribution. Must between -16 and 0 (inclusive). And since it needs at least 2 blocks variation for the branch starts to fit both branches,max_inclusivemust be at leastmin_inclusive + 1.
			- min_inclusiveThe minimum possible value.
			- max_inclusiveThe maximum possible value.
		- branch_end_offset_from_topValue between -16 and 16 (inclusive).
			- 
			- Int provider
	- foliage_placer
		- radiusThe radius of the foliage.
			- 
			- Int provider
		- offsetThe vertical offest from the top of trunk to the top of the foliage.[needs testing]
			- 
			- Int provider
		- typeOne ofblob_foliage_placer,spruce_foliage_placer,pine_foliage_placer,acacia_foliage_placer,bush_foliage_placer,fancy_foliage_placer,jungle_foliage_placer,mega_pine_foliage_placer,dark_oak_foliage_placer,random_spread_foliage_placer, orcherry_foliage_placer.If type is blob_foliage_placer, bush_foliage_placer, fancy_foliage_placer, or jungle_foliage_placer, the additional fields are as follows
		- heightThe foliage's height. Value between 0 and 16 (inclusive).If type is spruce_foliage_placer, the additional fields are as follows
		- trunk_heightValue between 0 and 24 (inclusive).
			- 
			- Int provider
		- heightValue between 0 and 24 (inclusive).
			- 
			- Int provider
		- crown_heightValue between 0 and 24 (inclusive).
			- 
			- Int provider
		- foliage_heightValue between 1 and 512 (inclusive).
			- 
			- Int provider
		- leaf_placement_attemptsValue between 0 and 256 (inclusive).If type is cherry_foliage_placer, the additional fields are as follows
		- heightValue between 4 and 16 (inclusive).
			- 
			- Int provider
		- wide_bottom_layer_hole_chanceValue between 0.0 and 1.0 (inclusive).
		- corner_hole_chanceValue between 0.0 and 1.0 (inclusive).
		- hanging_leaves_chanceValue between 0.0 and 1.0 (inclusive).
		- hanging_leaves_extension_chanceValue between 0.0 and 1.0 (inclusive).
	- decorators(Required, but can be empty) Decorations to add to the tree apart from the trunk and leaves.
		- A decorator.
			- typeThe type of decoration to add. One oftrunk_vine,leave_vine,cocoa,beehive,alter_ground, orattached_to_leaves.If type is leave_vine, cocoa or beehive, additional fields are as follows
			- probabilityValue between 0.0 and 1.0 (inclusive).If type is alter_ground, additional fields are as follows
			- providerThe block to replace the ground with.
				- 
				- Block state provider
			- probabilityValue between 0.0 and 1.0 (inclusive).
			- exclusion_radius_xzThe minimum value of the horizontal distance between two decorations. Value between 0 and 16 (inclusive).
			- exclusion_radius_yThe minimum value of the vertical distance between two decorations. Value between 0 and 16 (inclusive).
			- required_empty_blocksThe number of empty blocks required by the decoration. Value between 0 and 16 (inclusive).
			- block_providerThe block of the decoration.
				- 
				- Block state provider
			- directions(Cannot be empty) Directions to generate.
				- A direction. Must beup,down,north,south,west, oreast.


An example

{
  "type": "minecraft:tree",
  "config": {
    "decorators": [],
    "dirt_provider": {
      "type": "minecraft:simple_state_provider",
      "state": {
        "Name": "minecraft:dirt"
      }
    },
    "foliage_placer": {
      "type": "minecraft:spruce_foliage_placer",
      "offset": {
        "type": "minecraft:uniform",
        "value": {
          "max_inclusive": 2,
          "min_inclusive": 0
        }
      },
      "radius": {
        "type": "minecraft:uniform",
        "value": {
          "max_inclusive": 3,
          "min_inclusive": 2
        }
      },
      "trunk_height": {
        "type": "minecraft:uniform",
        "value": {
          "max_inclusive": 2,
          "min_inclusive": 1
        }
      }
    },
    "foliage_provider": {
      "type": "minecraft:simple_state_provider",
      "state": {
        "Name": "minecraft:spruce_leaves",
        "Properties": {
          "distance": "7",
          "persistent": "false",
          "waterlogged": "false"
        }
      }
    },
    "force_dirt": false,
    "ignore_vines": true,
    "minimum_size": {
      "type": "minecraft:two_layers_feature_size",
      "limit": 2,
      "lower_size": 0,
      "upper_size": 2
    },
    "trunk_placer": {
      "type": "minecraft:straight_trunk_placer",
      "base_height": 5,
      "height_rand_a": 2,
      "height_rand_b": 1
    },
    "trunk_provider": {
      "type": "minecraft:simple_state_provider",
      "state": {
        "Name": "minecraft:spruce_log",
        "Properties": {
          "axis": "y"
        }
      }
    }
  }
}




