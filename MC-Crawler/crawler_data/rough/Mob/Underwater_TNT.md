# Underwater TNT
Underwater TNT is a block that can be used by the player to initiate a controlled explosion underwater.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Crafting
- 2 Usage
	- 2.1 Behavior
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block state
- 5 Trivia
- 6 History
- 7 Issues

## Obtaining
### Breaking
Underwater TNT can be broken instantly with any tool, or without a tool. However, primed underwater TNT cannot be broken, as it is an entity.

### Crafting
| Ingredients     | Crafting recipe |
|-----------------|-----------------|
| Sodium+<br/>TNT |                 |

## Usage
Main article: TNT § Usage
Underwater TNT blocks can be activated the same way as a normal TNT block.

### Behavior
Once activated, it explodes like a normal TNT block. However, unlike the traditional TNT block, it can damage blocks underwater. It can still explode in the air, although it does not work in lava. Underwater TNT has the same delayed detonation rate as normal TNT.

## Data values
### ID
| Name           | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key            |
|----------------|------------|------------|----------------------------|----------------|----------------------------|
| Underwater TNT | `tnt`      | `46`       | Block & Giveable Item[i 2] | Identical[i 3] | `tile.underwater_tnt.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

| Name                  | Identifier | Numeric ID | Translation key   |
|-----------------------|------------|------------|-------------------|
| Primed Underwater TNT | `tnt`      | `65`       | `entity.tnt.name` |

### Block state
| Name                 | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                                                   |
|----------------------|---------------|---------------|----------------|-------------------------|-------------------------------------------------------------------------------|
| allow_underwater_bit | `0x2`         | `false`       | `false`        | `0`                     | This is normal TNT.                                                           |
|                      |               |               | `true`         | `1`                     | This is Underwater TNT.                                                       |
| explode_bit          | `0x1`         | `false`       | `false`        | `0`                     | Hittingthe TNT block breaks it, dropping it as an item that can be picked up. |
|                      |               |               | `true`         | `1`                     | Hittingthe TNT block causes it to ignite and then explode.                    |



