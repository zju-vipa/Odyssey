# Infested Block
Infested blocks consist of stone, cobblestone, deepslate, or any stone bricks variants that take less time to break and spawn only silverfish when broken without Silk Touch. Silverfish hide in these blocks, and emerge when a nearby silverfish is attacked in order to attack the aggressor. Infested blocks cannot be obtained in item form.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Post-generation
- 2 Usage
	- 2.1 Identifying
- 3 Sounds
	- 3.1 Stone
	- 3.2 Deepslate
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Trivia
- 8 References
- 9 External links

## Obtaining
Infested blocks are not obtainable by Silk Touch, and are only available through the Creative inventory or commands. However, they can be retained from worlds played in versions where they were legitimately obtainable.

### Breaking
Breaking an infested block by hand. More silverfish appear when attacking the first one.
| Block     | Infested StoneInfested Stone Bricks | Infested Cobblestone | Infested Deepslate    |
|-----------|-------------------------------------|----------------------|-----------------------|
| Hardness  | 0.75                                | 1                    | 1.5                   |
| Tool      |                                     |                      |                       |
|           |                                     |                      | Breakingtime (sec)[A] |
| Default   | 1.15                                | 1.5                  | 2.25                  |
| Wooden    | 0.6                                 | 0.75                 | 1.15                  |
| Stone     | 0.3                                 | 0.4                  | 0.6                   |
| Iron      | 0.2                                 | 0.25                 | 0.4                   |
| Diamond   | 0.15                                | 0.2                  | 0.3                   |
| Netherite | 0.15                                | 0.2                  | 0.25                  |
| Golden    | 0.1                                 | 0.15                 | 0.2                   |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


When the block is broken, whether by a player or by an explosion, a silverfish spawns where it was broken unless the difficulty is Peaceful or the game rule doTileDrops is set to false (doMobSpawning is irrelevant).

Infested blocks take less time to break than their normal counterparts. When breaking them with a pickaxe, they take half as much time to break as their normal counterparts.

When mined with anything other than a Silk Touch-enchanted tool, an infested block drops nothing and spawns a silverfish that immediately attacks the player. If the player attacks a silverfish directly with a sword, bow, or potion of Harming, or when a silverfish takes Poison damage, nearby infested blocks break, spawning more aggressive silverfish. If the silverfish is killed in one hit, then nearby infested blocks do not break, and no silverfish spawn from them.[1]

When mined with a tool enchanted with Silk Touch, however, the equivalent non-infested block is dropped without spawning a silverfish on all game difficulties.[2] Any Silk Touch-enchanted tool (including swords) will cause an infested block to drop its non-infested equivalent (that is, a pickaxe is not required). A player wishing to collect stone bricks from a stronghold safely should use Silk Touch-enchanted pickaxes.

### Natural generation
Infested stone bricks are occasionally found in strongholds and igloo basements in place of normal stone bricks. Infested mossy and chiseled stone bricks also spawn in igloos, but they do not generate naturally in strongholds.[3]

Infested cobblestone is found in the rarely generated "End portal" room in woodland mansions.

Infested stone and deepslate can generate in the Overworld in the form of blobs. Infested blocks attempt to generate 14 times per chunk in ore features of size 0-13‌[JE  only]/0-10‌[BE  only], from altitudes -64 to 63 in Java Edition or 0 to 64 in Bedrock Edition, within one of the following biomes, or within a chunk that is at least partially occupied by one of these biomes:

- Windswept Gravelly Hills
- Windswept Hills
- Windswept Forest
- Meadow
- Cherry Grove
- Grove
- Snowy Slopes
- Jagged Peaks
- Frozen Peaks
- Stony Peaks

Infested stone can replace stone, andesite, diorite, granite, tuff, and deepslate. If it replaces tuff or deepslate, it becomes infested deepslate.


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

| Name                           | Identifier                     | Form         | Translation key                                |
|--------------------------------|--------------------------------|--------------|------------------------------------------------|
| Infested Stone                 | infested_stone                 | Block & Item | block.minecraft.infested_stone                 |
| Infested Cobblestone           | infested_cobblestone           | Block & Item | block.minecraft.infested_cobblestone           |
| Infested Stone Bricks          | infested_stone_bricks          | Block & Item | block.minecraft.infested_stone_bricks          |
| Infested Cracked Stone Bricks  | infested_cracked_stone_bricks  | Block & Item | block.minecraft.infested_cracked_stone_bricks  |
| Infested Mossy Stone Bricks    | infested_mossy_stone_bricks    | Block & Item | block.minecraft.infested_mossy_stone_bricks    |
| Infested Chiseled Stone Bricks | infested_chiseled_stone_bricks | Block & Item | block.minecraft.infested_chiseled_stone_bricks |
| Infested Deepslate             | infested_deepslate             | Block & Item | block.minecraft.infested_deepslate             |

Bedrock Edition:

| Name               | Identifier         | Numeric ID | Form                       | Item ID[i 1]   | Translation key                                                                                                                                                                         |
|--------------------|--------------------|------------|----------------------------|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Infested Block     | monster_egg        | 97         | Block & Giveable Item[i 2] | Identical[i 3] | tile.monster_egg.stone.nametile.monster_egg.cobble.nametile.monster_egg.brick.nametile.monster_egg.mossybrick.nametile.monster_egg.crackedbrick.nametile.monster_egg.chiseledbrick.name |
| Infested Deepslate | infested_deepslate | 709        | Block & Giveable Item[i 2] | Identical[i 3] | tile.infested_deepslate.name                                                                                                                                                            |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ a b Available with /give command.

↑ a b The block's direct item form has the same id as the block.


### Block states
See also: Block states

Bedrock Edition:
Infested Deepslate:

| Name        | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                            |
|-------------|---------------|---------------|----------------|-------------------------|----------------------------------------|
| pillar_axis | Not Supported | y             | x              | Unsupported             | The deepslate is oriented east–west.   |
|             |               |               | y              | Unsupported             | The deepslate is oriented vertically.  |
|             |               |               | z              | Unsupported             | The deepslate is oriented north–south. |

Others:

| Name                   | Metadata Bits | Default value | Allowed values       | Values forMetadata Bits | Description                   |
|------------------------|---------------|---------------|----------------------|-------------------------|-------------------------------|
| monster_egg_stone_type | 0x10x20x4     | stone         | stone                | 0                       | Infested Stone                |
|                        |               |               | cobblestone          | 1                       | Infested Cobblestone          |
|                        |               |               | stone_brick          | 2                       | Infested Stone Brick          |
|                        |               |               | mossy_stone_brick    | 3                       | Infested Mossy Stone Brick    |
|                        |               |               | cracked_stone_brick  | 4                       | Infested Cracked Stone Brick  |
|                        |               |               | chiseled_stone_brick | 5                       | Infested Chiseled Stone Brick |



