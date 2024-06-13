#### Inverted daylight detector
Using a daylight detector inverts it. However, the output of the inverted detector is not a simple inversion of the daylight detector's output; it uses a much simpler algorithm that depends only on the internal sky light level. Specifically, it outputs a signal strength of 15 minus the current internal sky light level, where values over 15 or below 0 are taken as 15 or 0 respectively. This means that an inverted daylight detector actually outputs a strength of 11 at midnight when it's clear weather, if it has line of sight with the sky. The effects of shade are applied before inverting, so shade increases the signal strength when it isn't already full, and prevents it from reaching zero. 

### Fuel
Daylight detectors can be used as a fuel in furnaces, smelting 1.5 items per block.

### Note blocks
Daylight detectors can be placed under note blocks to produce "bass" sounds.

## Data values
### ID
Java Edition:

| Name              | Identifier        | Form         | Translation key                   |
|-------------------|-------------------|--------------|-----------------------------------|
| Daylight Detector | daylight_detector | Block & Item | block.minecraft.daylight_detector |

| Name         | Identifier        |
|--------------|-------------------|
| Block entity | daylight_detector |

Bedrock Edition:

| Name                     | Identifier                 | Numeric ID | Form                         | Item ID[i 1]   | Translation key             |
|--------------------------|----------------------------|------------|------------------------------|----------------|-----------------------------|
| Daylight Sensor          | daylight_detector          | 151        | Block & Giveable Item[i 2]   | Identical[i 3] | tile.daylight_detector.name |
| Inverted Daylight Sensor | daylight_detector_inverted | 178        | Block & Ungiveable Item[i 4] | Identical[i 3] | —                           |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ a b The block's direct item form has the same id as the block.

↑ Unavailable with /give command


| Name         | Savegame ID      |
|--------------|------------------|
| Block entity | DaylightDetector |

### Block states
See also: Block states

Java Edition:

| Name     | Default value | Allowed values         | Description                                                       |
|----------|---------------|------------------------|-------------------------------------------------------------------|
| inverted | false         | falsetrue              | If true, the daylight detector is inverted.                       |
| power    | 0             | 0123456789101112131415 | The current redstone power level produced by the daylight sensor. |

Bedrock Edition:

| Name            | Metadata Bits | Default value | Allowed values         | Values forMetadata Bits | Description                                                       |
|-----------------|---------------|---------------|------------------------|-------------------------|-------------------------------------------------------------------|
| redstone_signal | 0x10x20x40x8  | 0             | 0123456789101112131415 | 0123456789101112131415  | The current redstone power level produced by the daylight sensor. |



### Block data
A daylight detector has a block entity associated with it which stores only its entity ID and position (the minimum data for a block entity). Although the daylight detector's block entity stores no additional data, the block entity ensures that the daylight detector is updated every game tick.

Java Edition:

See also: Block entity format


 Block entity data
Tags common to all block entities

Bedrock Edition:

See Bedrock Edition level format/Block entity format.

