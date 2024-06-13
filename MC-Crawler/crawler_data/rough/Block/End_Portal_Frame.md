# End Portal Frame
An end portal frame is a block that resembles end stone with a decorative bluish-green top, with sides decorated in hollow rounded rectangles with the same color as the top.

## Contents
- 1 Obtaining
	- 1.1 Natural generation
- 2 Usage
	- 2.1 Redstone
	- 2.2 Light source
	- 2.3 Note blocks
	- 2.4 Piston interactivity
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Gallery
	- 7.1 Screenshots
- 8 References
- 9 External links

## Obtaining
End portal frames, like bedrock, are indestructible in Survival or Adventure mode. It can be obtained only by accessing the Creative inventory or commands.

### Natural generation







































End portal generation design


12 end portal frames generate naturally to form the end portal in each stronghold end portal room, over a pool of lava with a staircase containing a silverfish monster spawner. The frames generate in a 5×5 square formation, with 3 frames on each side, without the corners. Each end portal frame generates facing inward, with a 10% chance of containing an eye of ender.

Each stronghold contains an end portal in Java Edition, while in Bedrock Edition only some strongholds have a portal.[1][more information needed] In Java Edition, each world contains exactly 128 strongholds, so a total of 1,536 end portal frames are generated. In Bedrock Edition, there is an unlimited amount of strongholds in each world, so the amount of end portal frames that may generate is unlimited. In Legacy Console Edition, there was only one end portal per world, so 12 end portal frames were generated.


There is an extremely low chance (10-12 or 10-10% or one in a trillion) for all twelve end portal frames to be filled in strongholds.

The chart below shows the probability of having each number of eyes of ender filled in (some values may be rounded). 

| Frames filled | Probability |                       | Probability ≥ |                       |
|---------------|-------------|-----------------------|---------------|-----------------------|
| 0             | 28.24 %     | 1 : 3.54              | 100 %         | 1 : 1                 |
| 1             | 37.66 %     | 1 : 2.66              | 71.76 %       | 1 : 1.39              |
| 2             | 23.01 %     | 1 : 4.35              | 34.10 %       | 1 : 2.93              |
| 3             | 8.52 %      | 1 : 11.7              | 11.09 %       | 1 : 9.02              |
| 4             | 2.13 %      | 1 : 46.9              | 2.56 %        | 1 : 39                |
| 5             | 0.38 %      | 1 : 264               | 0.43 %        | 1 : 231               |
| 6             | 4.91⨯10-4   | 1 : 2,036             | 5.41⨯10-4     | 1 : 1,848             |
| 7             | 4.68⨯10-5   | 1 : 21,383            | 5.02⨯10-5     | 1 : 19,928            |
| 8             | 3.25⨯10-6   | 1 : 307,911           | 3.41⨯10-6     | 1 : 292,952           |
| 9             | 1.60⨯10-7   | 1 : 6,235,191         | 1.66⨯10-7     | 1 : 6,030,090         |
| 10            | 5.35⨯10-9   | 1 : 187,055,743       | 5.45⨯10-9     | 1 : 183,318,064       |
| 11            | 1.08⨯10-10  | 1 : 9,259,259,259     | 1.09⨯10-10    | 1 : 9,174,327,988     |
| 12            | 10-12       | 1 : 1,000,000,000,000 | 10-12         | 1 : 1,000,000,000,000 |

## Usage
Using eyes of ender on end portal frames inserts them to the top of the frame if it is not inserted previously.

An end portal frame has a front face that faces the player when placed. Although the facing is almost invisible (one can distinguish only 2 rotations of end portal frames), all end portal frames must be placed correctly and face inward in order to be able to activate the end portal, and if all of the frames have eyes of ender inserted, the portal activates, replacing the inner 3×3 space with end portal blocks.

If an end portal is built in the End, entities are teleported back to the world spawn point in the Overworld, similar to the exit portal.

### Redstone
End portal frames output a redstone comparator signal of 15 when an eye is present. If there is no eye in the frame, it outputs a signal of 0.

### Light source
End portals frames emit a light level of 1.

### Note blocks
End portals frames can be placed under note blocks to produce "bass drum" sound.

### Piston interactivity
End portal frames cannot be pushed by pistons. They also cannot be pushed nor pulled by sticky pistons.

## Data values
### ID
Java Edition:

| Name             | Identifier         | Form         | Block tags                          | Translation key                    |
|------------------|--------------------|--------------|-------------------------------------|------------------------------------|
| End Portal Frame | `end_portal_frame` | Block & Item | `dragon_immune`<br/>`wither_immune` | `block.minecraft.end_portal_frame` |

Bedrock Edition:

| Name             | Identifier         | Numeric ID | Form                       | Item ID[i 1]   | Translation key              |
|------------------|--------------------|------------|----------------------------|----------------|------------------------------|
| End Portal Frame | `end_portal_frame` | `120`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.end_portal_frame.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:

| Name   | Default value | Allowed values                            | Description                                                                                                                                                                                                                                                        |
|--------|---------------|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| eye    | `false`       | `false`<br/>`true`                        | If true, the portal frame block contains aneye of ender.                                                                                                                                                                                                           |
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction of the end portal frame block.<br/>The opposite from the direction the player faces while placing the block.<br/>In order to activate a portal, all 12 blocks must be facing inward;<br/>for example, the northern three blocks must all face south. |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values                            | Values forMetadata Bits | Description                                                                                                                                                                                                                                                        |
|------------------------------|---------------|---------------|-------------------------------------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| end_portal_eye_bit           | `0x4`         | `false`       | `false`<br/>`true`                        | `0`<br/>`1`             | If the portal frame block contains aneye of ender.                                                                                                                                                                                                                 |
| minecraft:cardinal_direction | Not Supported | `south`       | `east`<br/>`north`<br/>`south`<br/>`west` | `Unsupported`           | The direction of the end portal frame block.<br/>The opposite from the direction the player faces while placing the block.<br/>In order to activate a portal, all 12 blocks must be facing inward;<br/>for example, the northern three blocks must all face south. |



