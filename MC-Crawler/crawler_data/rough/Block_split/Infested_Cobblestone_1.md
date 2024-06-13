### Post-generation
Infested blocks are generated when a silverfish enters the respective normal block form.

## Usage
When mined, an infested block spawns a silverfish that immediately attacks the player. If the player attacks a silverfish directly with a sword, bow, or potion of Harming, or when a silverfish takes poison damage, nearby infested blocks break, spawning more aggressive silverfish. If the silverfish is killed in one hit, then nearby infested blocks do not break, and no silverfish spawn from them.

### Identifying
Note blocks placed on infested blocks produce flute sounds‌[Bedrock Edition  only] or harp sounds‌[Java Edition  only], while those placed on the non-infested stone, cobblestone, or stone bricks produce bass drum sounds.

In Bedrock Edition, a player can distinguish infested from normal blocks by observing that an infested block takes a bit faster to break when using a pickaxe than the stone it appears to be, but without a pickaxe, it still breaks faster.

A silverfish does not spawn if the block is destroyed by the ender dragon.

In Java Edition, using the debug screen, a player can identify whether or not a block is infested.

## Data values
### ID
Java Edition:

| Name                           | Identifier                       | Form         | Translation key                                  |
|--------------------------------|----------------------------------|--------------|--------------------------------------------------|
| Infested Stone                 | `infested_stone`                 | Block & Item | `block.minecraft.infested_stone`                 |
| Infested Cobblestone           | `infested_cobblestone`           | Block & Item | `block.minecraft.infested_cobblestone`           |
| Infested Stone Bricks          | `infested_stone_bricks`          | Block & Item | `block.minecraft.infested_stone_bricks`          |
| Infested Cracked Stone Bricks  | `infested_cracked_stone_bricks`  | Block & Item | `block.minecraft.infested_cracked_stone_bricks`  |
| Infested Mossy Stone Bricks    | `infested_mossy_stone_bricks`    | Block & Item | `block.minecraft.infested_mossy_stone_bricks`    |
| Infested Chiseled Stone Bricks | `infested_chiseled_stone_bricks` | Block & Item | `block.minecraft.infested_chiseled_stone_bricks` |
| Infested Deepslate             | `infested_deepslate`             | Block & Item | `block.minecraft.infested_deepslate`             |

Bedrock Edition:

| Name               | Identifier           | Numeric ID | Form                       | Item ID[i 1]   | Translation key                                                                                                                                                                                                              |
|--------------------|----------------------|------------|----------------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Infested Block     | `monster_egg`        | `97`       | Block & Giveable Item[i 2] | Identical[i 3] | `tile.monster_egg.stone.name`<br/>`tile.monster_egg.cobble.name`<br/>`tile.monster_egg.brick.name`<br/>`tile.monster_egg.mossybrick.name`<br/>`tile.monster_egg.crackedbrick.name`<br/>`tile.monster_egg.chiseledbrick.name` |
| Infested Deepslate | `infested_deepslate` | `709`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.infested_deepslate.name`                                                                                                                                                                                               |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑ a bAvailable with /give command.
3. ↑ a bThe block's direct item form has the same id as the block.

### Block states
See also: Block states

Bedrock Edition:
Infested Deepslate:

| Name        | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                            |
|-------------|---------------|---------------|----------------|-------------------------|----------------------------------------|
| pillar_axis | Not Supported | `y`           | `x`            | `Unsupported`           | The deepslate is oriented east–west.   |
|             |               |               | `y`            | `Unsupported`           | The deepslate is oriented vertically.  |
|             |               |               | `z`            | `Unsupported`           | The deepslate is oriented north–south. |

Others:

| Name                   | Metadata Bits             | Default value | Allowed values         | Values forMetadata Bits | Description                   |
|------------------------|---------------------------|---------------|------------------------|-------------------------|-------------------------------|
| monster_egg_stone_type | `0x1`<br/>`0x2`<br/>`0x4` | `stone`       | `stone`                | `0`                     | Infested Stone                |
|                        |                           |               | `cobblestone`          | `1`                     | Infested Cobblestone          |
|                        |                           |               | `stone_brick`          | `2`                     | Infested Stone Brick          |
|                        |                           |               | `mossy_stone_brick`    | `3`                     | Infested Mossy Stone Brick    |
|                        |                           |               | `cracked_stone_brick`  | `4`                     | Infested Cracked Stone Brick  |
|                        |                           |               | `chiseled_stone_brick` | `5`                     | Infested Chiseled Stone Brick |




