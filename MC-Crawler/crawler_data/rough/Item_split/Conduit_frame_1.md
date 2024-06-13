### Light source
Conduits emit a light level of 15, the brightest light level in the game, whether activated or not, and even on land.

## Data values
### ID
Java Edition:

| Name    | Identifier | Form         | Block tags         | Translation key           |
|---------|------------|--------------|--------------------|---------------------------|
| Conduit | `conduit`  | Block & Item | `mineable/pickaxe` | `block.minecraft.conduit` |

| Name         | Identifier |
|--------------|------------|
| Block entity | `conduit`  |

Bedrock Edition:

| Name    | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key     |
|---------|------------|------------|----------------------------|----------------|---------------------|
| Conduit | `conduit`  | `412`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.conduit.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

| Name         | Savegame ID |
|--------------|-------------|
| Block entity | `Conduit`   |

### Block states
See also: Block states

Java Edition:

| Name        | Default value | Allowed values     | Description                                                     |
|-------------|---------------|--------------------|-----------------------------------------------------------------|
| waterlogged | `true`        | `false`<br/>`true` | Whether or not there's water in the same place as this conduit. |

### Block entity
A conduit has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format

- Block entity data
	- 
	- Tags common to all block entities
	- Target: TheUUIDof the hostile mob the conduit is currently attacking, stored as four ints. May not be present.

Bedrock Edition:

SeeBedrock Edition level format/Block entity format.
## Notes
1. ↑Conduits can be activated only by full blocks by design; see MC-128661
2. ↑Completed conduits only damage one mob at a time; see MC-198923


