### Exploding
If the player attempts to set their spawn at a charged respawn anchor in the Overworld, the End, or custom dimensions in which they are disabled, the block explodes (and is destroyed) similar to when a bed is used in the Nether or the End. The explosion has a power of 5 and sets fire to surrounding blocks.

### Redstone component
When charged, a redstone comparator gives a signal depending on the number of charges: 3 for one charge, 7 for two charges, 11 for three charges, 15 for four charges. An empty anchor gives a signal of 0.

The respawn anchor can also be charged with a dispenser.

The respawn anchor cannot be pushed by a piston. 

### Mobs
Hoglins run away from respawn anchors.

### Note blocks
Respawn anchors can be placed under note blocks to produce the "bass drum" sound.

## Data values
### ID
Java Edition:

| Name           | Identifier     | Form         | Block tags                     | Translation key                |
|----------------|----------------|--------------|--------------------------------|--------------------------------|
| Respawn Anchor | respawn_anchor | Block & Item | dragon_immunehoglin_repellents | block.minecraft.respawn_anchor |

Bedrock Edition:

| Name           | Identifier     | Numeric ID | Form                       | Item ID[i 1]   | Translation key          |
|----------------|----------------|------------|----------------------------|----------------|--------------------------|
| Respawn Anchor | respawn_anchor | 527        | Block & Giveable Item[i 2] | Identical[i 3] | tile.respawn_anchor.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block states

Java Edition:

| Name    | Default value | Allowed values | Description                                   |
|---------|---------------|----------------|-----------------------------------------------|
| charges | 0             | 01234          | How many charges the Respawn Anchor has left. |

Bedrock Edition:

| Name                  | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                   |
|-----------------------|---------------|---------------|----------------|-------------------------|-----------------------------------------------|
| respawn_anchor_charge | 0x10x20x4     | 0             | 01234          | 01234                   | How many charges the Respawn Anchor has left. |




