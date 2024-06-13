# Replace single block
Replace single block is a technical feature that replaces a single block using a list of targets and states. It is not used by the game currently.

## Contents
- 1 Data values
	- 1.1 ID
	- 1.2 Config
- 2 History

## Data values
### ID
| Feature type        | Identifier             |
|---------------------|------------------------|
| [No displayed name] | `replace_single_block` |

### Config
Main article: Configured feature
- config
	- targets(Required, but can be empty) A list of targets.
		- A target.
			- targetRule test. The blocks to replace.
				- 
				- A rule test
			- stateThe block to use.
				- 
				- Block state


An example

{
  "type": "minecraft:replace_single_block",
  "config": {
    "targets": [
      {
        "state": {
          "Name": "minecraft:diamond_ore"
        },
        "target": {
          "predicate_type": "minecraft:tag_match",
          "tag": "minecraft:stone_ore_replaceables"
        }
      },
      {
        "state": {
          "Name": "minecraft:deepslate_diamond_ore"
        },
        "target": {
          "predicate_type": "minecraft:tag_match",
          "tag": "minecraft:deepslate_ore_replaceables"
        }
      }
    ]
  }
}




