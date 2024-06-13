# Bedrock
Bedrock is an indestructible block found in all three dimensions. It cannot be obtained as an item in Survival.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Post-generation
- 2 Usage
	- 2.1 Trapping the wither
	- 2.2 End crystal
	- 2.3 Note blocks
	- 2.4 Piston interactivity
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
	- 5.1 Data history
- 6 Issues
- 7 Trivia
- 8 Gallery
	- 8.1 Screenshots
- 9 External links
- 10 References
- 11 External links

## Obtaining
Bedrock can be obtained from the Creative inventory, or using commands.

### Breaking
| Block    | Bedrock             |
|----------|---------------------|
| Hardness | ∞                   |
|          | Breakingtime (secs) |
| Default  | ∞                   |

See also: Tutorials/Breaking bedrock

Bedrock cannot normally be broken in Survival mode with any tool. It can only be broken by hand in snapshot 22w13oneBlockAtATime and has a hardness value of 600.

However, it can be broken using glitches involving a piston, but it does not drop as an item.

### Natural generation
Bedrock comprises the five bottom-most layers of the Overworld in a rough pattern, although the top four layers are predominantly flat bedrock with only rare gaps, rendering the lowest, completely flat fifth layer (at Y=-64) mostly inaccessible.

In the Nether, bedrock comprises both the top and bottom four layers in a rough pattern. In both Java and Bedrock Editions, the patterns of bedrock are consistent in the Nether. At the top of the Nether, bedrock prevents the player from ascending above Y=127 without exploiting glitches, although in Java Edition the build limit extends to Y=255 in the Nether, meaning it is possible to build there. This space, known as the "Nether ceiling", consists entirely of flat bedrock and the occasional mushrooms. No mobs spawn here, as nothing can spawn on bedrock, although mobs can spawn on valid blocks placed by a player.

In the End, a single block of bedrock generates on top of each obsidian pillar, each topped with an end crystal. The bedrock remains after the destruction of the crystal (because it is indestructible), and is lit on fire indefinitely. Bedrock additionally comprises part of the exit portal at the center of the central island. Unlike in other dimensions, there is no bedrock floor at the bottom of the End, meaning it is possible to fall into the void without exploiting glitches.

An unlimited number of end gateways generate randomly across the outer End islands, each consisting of 12 blocks of bedrock.


### Post-generation
If the bedrock that makes up the exit portal is removed by any means, it regenerates when the ender dragon is defeated or re-summoned. 

An end gateway is generated on the central End island upon the death of each ender dragon, which is mostly made of bedrock. A total of 20 of these gateways generate in a circle centered on the exit portal in set positions. A corresponding end gateway is generated in the inner edge of the outer islands after an end gateway on the central island is activated for the first time.

## Usage
Bedrock generates at the bottom of the Overworld and the Nether in order to prevent players from falling into the void. 

The bedrock ceiling in the Nether was intended to prevent players from accessing the Nether ceiling, which was meant to be an empty out-of-bounds area where players cannot build. This remains true in Bedrock Edition. However, in Java Edition 1.2.1, the world height was doubled from 127 to 255, a change which was applied in all three dimensions, allowing players to build on the Nether ceiling. Due to the number of players taking advantage of this change, it was decided by Mojang that this was to be treated as an intended feature.[1]

Bedrock generates as part of important structures in the End, including crucial elements of the ender dragon fight, as well as the gateways and the exit portals, in order to prevent them from being broken and keep them accessible and usable.

Mobs do not spawn on bedrock. Endermen are unable to place the block they are holding onto bedrock.

Beacons treat bedrock as a transparent block, meaning their beams can pass through it, allowing beacons to be used in the Nether.

In the End, any fire on bedrock never extinguishes naturally, similar to netherrack.

### Trapping the wither
Main article: Tutorials/Wither cage
Since bedrock is indestructible in Survival, it can be used against withers. Certain configurations of bedrock (Such as that found under the exit portal) can be used to securely trap withers by spawning them below the bedrock. The wither can then either be easily killed, utilized to break blocks automatically, or used to farm wither roses.

### End crystal
Bedrock is one of the only two blocks on which end crystals can be placed, the other being obsidian.

Placing an end crystal on bedrock in the End sets it on fire.

### Note blocks
Note blocks can be placed above bedrock to produce "bass drum" sounds.

### Piston interactivity
Bedrock is unable to be pushed or pulled by either of the piston variants (regular or sticky).

## Data values
### ID
Java Edition:

| Name    | Identifier | Form         | Block tags                                                                                                      | Translation key         |
|---------|------------|--------------|-----------------------------------------------------------------------------------------------------------------|-------------------------|
| Bedrock | bedrock    | Block & Item | dragon_immuneinfiniburn_endwither_immunelava_pool_stone_replaceablesfeatures_cannot_replacegeode_invalid_blocks | block.minecraft.bedrock |

Bedrock Edition:

| Name    | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key   |
|---------|------------|------------|----------------------------|----------------|-------------------|
| Bedrock | bedrock    | 7          | Block & Giveable Item[i 2] | Identical[i 3] | tile.bedrock.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block states

In Bedrock Edition, bedrock uses the following block states:

Bedrock Edition:

| Name           | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                      |
|----------------|---------------|---------------|----------------|-------------------------|--------------------------------------------------|
| infiniburn_bit | 0x1           | false         | falsetrue      | 01                      | Specifies if this bedrock can burn indefinitely. |



