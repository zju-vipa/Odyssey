# Debug Stick
The debug stick is an item used to edit the block states of blocks. It is visually identical to a regular stick, but with a glint (as if enchanted).

## Contents
- 1 Obtaining
- 2 Usage
- 3 Data values
	- 3.1 ID
	- 3.2 Item data
- 4 History
- 5 Issues
- 6 Trivia
- 7 Gallery
	- 7.1 In other media
- 8 See also
- 9 References

## Obtaining
The debug stick is obtainable via commands such as /give or /item, or the Creative inventory if the player has the appropriate permissions. It can be obtained only in worlds with cheats on.

## Usage
The debug stick can be used to change block states. Hitting the block allows players to select the block state key they wish to change, for an example, switching between the conditional and the facing block state keys for a command block. Using the block allows them to cycle through the valid values for the block state key, again as an example, the player can make the command block face, down, east, north, south, up, or west if they chose the facing block state key. Sneaking while hitting or using cycles through the block state keys or values in reverse order.

It is notable that using debug stick directly on an interactive block without sneaking uses the block itself instead of the stick.[1]

The debug stick cannot be used while in Survival or Adventure mode. It works only in Creative mode with cheats enabled. In modes other than Creative, it acts like a regular item — although when using it on a block, the player swings the stick as if interacting with it (but nothing happens).

## Data values
### ID
| Name        | Identifier  | Form | Translation key            |
|-------------|-------------|------|----------------------------|
| Debug Stick | debug_stick | Item | item.minecraft.debug_stick |

### Item data

 tag: The item's tag tag.
 DebugProperty: A compound where each key is a block ID, and the value is the block state key to edit for that block ID. Block tags are not supported.
 Block ID: The block state key of the block to edit, for example "minecraft:oak_fence": "east".

## See also
- Block states


