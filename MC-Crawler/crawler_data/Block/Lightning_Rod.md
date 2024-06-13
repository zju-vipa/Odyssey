# Lightning Rod
A lightning rod is a block used to divert lightning strikes.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Crafting
- 2 Usage
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 Advancements
- 6 History
- 7 Issues
- 8 Trivia
- 9 Gallery
	- 9.1 Renders
		- 9.1.1 Java Edition
		- 9.1.2 Bedrock Edition
		- 9.1.3 Powered
	- 9.2 Screenshots
	- 9.3 Development images
- 10 References

## Obtaining
### Breaking
A lightning rod must be mined with a stone pickaxe or better, or else it drops nothing.

| Block     | Lightning Rod         |
|-----------|-----------------------|
| Hardness  | 3                     |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 15                    |
| Wooden    | 7.5                   |
| Stone     | 1.15                  |
| Iron      | 0.75                  |
| Diamond   | 0.6                   |
| Netherite | 0.5                   |
| Golden    | 1.25                  |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


### Crafting
| Ingredients  | Crafting recipe |
|--------------|-----------------|
| Copper Ingot |                 |

## Usage
Lightning rods can be oriented in different directions. Lightning rods that are the highest block in the column redirect lightning strikes within a spherical volume having a radius of 128 blocks in Java Edition and 64 blocks in Bedrock Edition. The block emits particles during thunderstorms as an indicator. If multiple lightning rods are in range, the closest to the original location of the strike is chosen.

Lightning can also strike a lightning rod hit by a trident enchanted with Channeling during a thunderstorm, even if there are solid blocks above it blocking rainfall, as long as all the blocks are fully transparent (sky light level 15 at rod position). Lightning rods do not divert the lightning created by a Channeling trident thrown at an entity, or the lightning summoned by commands.

Unlike in real life, a lightning rod doesn't require a direct connection to ground in order to work.

Lightning strikes on lightning rods cannot summon skeleton trap horses.

A lightning rod and the block it's attached to emit a redstone signal for 8 game ticks when struck by lightning.

Lightning diverted by a lightning rod can still start fires nearby (quickly extinguished on non-flammable blocks or by rain) and inflicts lightning damage on mobs within a 6×12×6 box centered 4 blocks above the bottom center of the lightning rod block (that is, extending 2 below and 9 above). Adjacent blocks can ignite even if the lightning rod is mounted on a non-flammable block.

## Data values
### ID
Java Edition:

| Name          | Identifier    | Form         | Translation key               |
|---------------|---------------|--------------|-------------------------------|
| Lightning Rod | lightning_rod | Block & Item | block.minecraft.lightning_rod |

Bedrock Edition:

| Name          | Identifier    | Numeric ID | Form                       | Item ID[i 1]   | Translation key         |
|---------------|---------------|------------|----------------------------|----------------|-------------------------|
| Lightning Rod | lightning_rod | 567        | Block & Giveable Item[i 2] | Identical[i 3] | tile.lightning_rod.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.




### Block states
See also: Block states

Java Edition:

| Name        | Default value | Allowed values           | Description                                                                  |
|-------------|---------------|--------------------------|------------------------------------------------------------------------------|
| facing      | up            | updownnorthsoutheastwest | The direction that the lightning rod is facing, determined by its anchoring. |
| powered     | false         | falsetrue                | Whether or not the lightning rod is powered.                                 |
| waterlogged | false         | falsetrue                | Whether or not there's water in the same place as this lightning rod.        |

Bedrock Edition:

| Name             | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                                                           |
|------------------|---------------|---------------|----------------|-------------------------|---------------------------------------------------------------------------------------|
| facing_direction | Not Supported | 0             | 012345         | Unsupported             | The direction the lightning rod faces.0: Down 1: Up 2: North 3: South 4: West 5: East |



