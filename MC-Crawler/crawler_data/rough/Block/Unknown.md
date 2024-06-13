# Unknown
Unknown is a placeholder block exclusive to Bedrock Edition that generates in place where blocks have an invalid ID or invalid components in their behavior files.
If the block has a unique model, it takes the shape of that model.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
- 2 Behavior
- 3 Data values
	- 3.1 ID
- 4 History

## Obtaining
### Breaking
The unknown block drops itself when broken, and breaks instantly with any tool.

| Block    | Unknown             |
|----------|---------------------|
| Hardness | 0                   |
|          | Breakingtime (secs) |
| Default  | 0.05                |

### Natural generation
Loading a block with an incorrect ID in any world results in it being replaced by an unknown block, although it retains its ID. The ID is not retained upon being broken.

## Behavior
The unknown block breaks instantly, and is able to be placed. Like ice, it has low friction.

## Data values
### ID
| Name    | Identifier | Numeric ID | Form                         | Item ID[i 1]   | Translation key     |
|---------|------------|------------|------------------------------|----------------|---------------------|
| Unknown | `unknown`  | `560`      | Block & Ungiveable Item[i 2] | Identical[i 3] | `tile.unknown.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Unavailable with /give command
3. ↑The block's direct item form has the same id as the block.

