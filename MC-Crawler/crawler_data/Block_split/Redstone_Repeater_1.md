### Signal delay
When initially placed, a redstone repeater has a delay of one redstone tick (equivalent to two game ticks, or 0.1 seconds barring lag).

A repeater's delay can be modified by using the Use Item control. Each use increases the repeater's delay by one redstone tick, to a maximum of four redstone ticks, then back to one redstone tick. Longer delays can be made with multiple repeaters – for example, a repeater set to 'four' and another to 'one' provides a half-second delay (0.4s + 0.1s = 0.5s).

A repeater set to a delay of two to four redstone ticks increases the length of any shorter on-pulse to match the length of the repeater's delay, and suppress any shorter off-pulse. For example, a repeater set to a 4-tick delay changes a 1-tick, 2-tick, or 3-tick on-pulse into a 4-tick on-pulse, and does not allow through any off-pulse shorter than 4 ticks.

Although a repeater cannot be set to have a delay of zero, instant repeater circuits are possible (circuits that repeat a signal with no delay).

In Bedrock Edition, the first repeater have a delay of zero but the repeater is still showing 1-tick.[more information needed]

###  Signal direction
See also: Mechanics/Redstone/Transmission circuit § Diode

A redstone repeater acts as a diode – it allows redstone signals through in one direction (unlike redstone dust or opaque blocks that can transmit redstone signals in any direction).

A diode can be used to protect a redstone circuit from redstone signals feeding back into the circuit from its output, or can be used to isolate one part of a circuit from another.

###  Signal locking
See also: Mechanics/Redstone/Memory circuit

The left repeater has been locked in an unpowered output state by the right repeater.
A redstone repeater can be "locked" by another powered redstone repeater facing its side. When locked, the repeater does not change its output (whether powered or unpowered), no matter what the input does. When the side repeater turns back off, the repeater returns to its normal behavior.

A repeater can also be locked by a powered redstone comparator facing its side. This offers additional possibilities for locking signals because a comparator's output can be affected from 3 sides as well as by containers.

If a repeater is locked again too quickly after unlocking (e.g. the lock is controlled by a fast clock circuit), or the lock and the input are changed only on the same tick (e.g. because they're fed by the same clock and both repeaters have the same delay), the repeater does not switch states.

## Data values
### ID
Java Edition:

| Name              | Identifier | Form         | Translation key          |
|-------------------|------------|--------------|--------------------------|
| Redstone Repeater | repeater   | Block & Item | block.minecraft.repeater |

Bedrock Edition:

| Redstone Repeater | Identifier         | Numeric ID | Form                         | Item ID[i 1]   | Translation key    |
|-------------------|--------------------|------------|------------------------------|----------------|--------------------|
| Unpowered block   | unpowered_repeater | 93         | Block & Ungiveable Item[i 2] | Identical[i 3] | —                  |
| Powered block     | powered_repeater   | 94         | Block & Ungiveable Item[i 2] | Identical[i 3] | —                  |
| Item              | repeater           | 419        | Item                         | —              | item.repeater.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ a b Unavailable with /give command

↑ a b The block's direct item form has the same id as the block.


### Block states
See also: Block states

Java Edition:

| Name    | Default value | Allowed values     | Description                                                                                                                                 |
|---------|---------------|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| delay   | 1             | 1234               | The redstone repeater's delay in redstone ticks.                                                                                            |
| facing  | north         | eastnorthsouthwest | The direction from theoutputside to theinputside of a repeater.The opposite from the direction the player faces while placing the repeater. |
| locked  | false         | falsetrue          | True if the repeater is currently locked.                                                                                                   |
| powered | false         | falsetrue          | If the redstone repeater is lit.                                                                                                            |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values     | Values forMetadata Bits | Description                                                                                                                                 |
|------------------------------|---------------|---------------|--------------------|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| minecraft:cardinal_direction | Not Supported | south         | eastnorthsouthwest | Unsupported             | The direction from theoutputside to theinputside of a repeater.The opposite from the direction the player faces while placing the repeater. |
| repeater_delay               | 0x40x8        | 0             | 0123               | 0123                    | The redstone repeater's delay in redstone ticks minus 1.                                                                                    |




