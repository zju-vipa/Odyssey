#### Behavior




























































In Bedrock Edition, the signal can go down from glass blocks.




























































However, the signal can never go down from slabs.
Redstone wire can transmit power, which can be used to operate mechanism components (doors, pistons, redstone lamps, etc.).
Redstone wire can be "powered" by a number of methods:

- from an adjacentpower componentor a strongly-powered block
- from the output of a redstone repeater or redstone comparator
- from adjacent redstone wire. The powering dust can be a level higher or lower, but with restrictions:
	- Redstone dust can be powered by redstone dust that is one level lower, or on anopaqueblock one level higher. A transparent block cannot‌[Java Edition  only]pass power downward.
	- The block "between" the two dust blocks must be air or transparent. A solid block there "cuts" the connection between the higher and lower dust.

The "power level" of redstone dust can vary from 0 to 15. Most power components power-up adjacent redstone dust to power level 15, but a few (daylight sensors, trapped chests, and weighted pressure plates) may create a lower power level. Redstone repeaters output power level 15 (when turned on), but redstone comparators may output a lower power level.






15

14

13

12

11

10

9

8

7

6

5

4

3

2

1

0


Redstone wire can transmit power up to 15 blocks.
Power level drops by 1 for every block of redstone wire it crosses. Thus, redstone wire can transmit power for no more than 15 blocks. To go further, the power level must be re-strengthened – typically with a redstone repeater.

Powered redstone wire on top of, or pointing at, an opaque block provides weak power to the block. A weakly-powered block cannot power other adjacent redstone wire, but can still power redstone repeaters and comparators, and activate adjacent mechanism components. Transparent blocks cannot be powered.

When redstone wire is unpowered, it appears dark red. When powered, it becomes bright red at power level 15, fading to darker shades with decreasing power. Powered redstone wire also produces "dust" particles of the same color.

While redstone wire always provides power to the directions it points into, it can still point into directions in which it cannot give power. If redstone wire comes in the form of a cross, the player can right-click to toggle it between a cross and dot. A redstone dot does not power anything adjacent to it, but powers the block under it.

## Data values
### ID
Java Edition:

| Redstone Dust | Identifier    | Form  | Translation key               |
|---------------|---------------|-------|-------------------------------|
| Block         | redstone_wire | Block | block.minecraft.redstone_wire |
| Item          | redstone      | Item  | item.minecraft.redstone       |

Bedrock Edition:

| Redstone Dust | Identifier    | Numeric ID | Form                         | Item ID[i 1]   | Translation key         |
|---------------|---------------|------------|------------------------------|----------------|-------------------------|
| Block         | redstone_wire | 55         | Block & Ungiveable Item[i 2] | Identical[i 3] | tile.redstone_wire.name |
| Item          | redstone      | 373        | Item                         | —              | item.redstone.name      |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Unavailable with /give command

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block states

Java Edition:

| Name  | Default value | Allowed values         | Description                                                           |
|-------|---------------|------------------------|-----------------------------------------------------------------------|
| east  | none          | nonesideup             | The way redstone dust connects to the east, side can also mean down.  |
| north | none          | nonesideup             | The way redstone dust connects to the north, side can also mean down. |
| power | 0             | 0123456789101112131415 | The redstone dust's current power level.                              |
| south | none          | nonesideup             | The way redstone dust connects to the south, side can also mean down. |
| west  | none          | nonesideup             | The way redstone dust connects to the west, side can also mean down.  |

Bedrock Edition:

| Name            | Metadata Bits | Default value | Allowed values         | Values forMetadata Bits | Description                              |
|-----------------|---------------|---------------|------------------------|-------------------------|------------------------------------------|
| redstone_signal | 0x10x20x40x8  | 0             | 0123456789101112131415 | 0123456789101112131415  | The redstone dust's current power level. |




List of block state combinations
Main article: Redstone Dust/Asset history[edit]


