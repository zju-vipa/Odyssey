### Output
When activated, a command block can produce multiple types of output:

#### Success count
A command block can power a redstone comparator facing away from it (possibly separated by a block) with signal strength specific to the success count. Success count is an integer between 0 to 2,147,483,647 (inclusive).
The signal strength always reflects the last command executed, even after the command block is deactivated.
In Java Edition, success count is usually 0 or 1, except for /function and /execute.
In Bedrock Edition, success count is an integer related to the command (e.g., the number of players affected by the command, the number of blocks that were altered, the value returned by the command, etc.)
In Java Edition, leaving the command block GUI by clicking "Done" or pressing Enter resets the success count to 0, regardless of whether changes were made in the GUI. In Bedrock Edition, leaving the GUI with changes resets the success count to 0.
#### Message
The output message describes the success or failure of the executed command, and may be written to multiple destinations:
Previous Output: The output message is always written to the "Previous Output" text pane of the command block GUI.
Chat: The output message is written to the chat text in singleplayer mode, or broadcast to all other ops in multiplayer mode, unless it has been suppressed with /gamerule commandBlockOutput false. Some commands may write additional text to the chat as their normal function, which won't be suppressed (for example, the /say command writes a message to the chat of all players), separate from the output message. Chat messages that would usually be prefaced by a player's name (such as from the /me, /say and /tell commands) use @ ‌[Java Edition  only] / ! ‌[Bedrock Edition  only] as the player name. If the command block had been named in an anvil before placement, that name is used instead. In Bedrock Edition, it can also modified in the GUI.
Logs: The output message is written to multiplayer server logs unless it has been suppressed with /gamerule logAdminCommands false.
###  Notes
Command blocks execute commands with OP level 2. The following commands cannot be used in a command block: /ban, /banlist, /ban-ip, /debug, /deop, /kick‌[JE  only], /op, /pardon, /pardon-ip, /publish, /reload‌[BE  only], /save-all, /save-off, /save-on, /stop, and /whitelist (i.e., /debug, /publish, and all of the multiplayer-only commands except /list).

#### Easter eggs
Main article: Easter eggs § Command blocks
Running "Searge" (case insensitive) as the command in the command block without a preceding "/" will set the previous output to "#itzlipofutzli". Its success count is 1.

### Piston interactivity
Command blocks cannot be pushed by pistons. They also cannot be pushed or pulled by sticky pistons.

## Data values
### ID
Java Edition:

| Name                    | Identifier              | Form         | Block tags                 | Translation key                         |
|-------------------------|-------------------------|--------------|----------------------------|-----------------------------------------|
| Command Block           | command_block           | Block & Item | dragon_immunewither_immune | block.minecraft.command_block           |
| Chain Command Block     | chain_command_block     | Block & Item | dragon_immunewither_immune | block.minecraft.chain_command_block     |
| Repeating Command Block | repeating_command_block | Block & Item | dragon_immunewither_immune | block.minecraft.repeating_command_block |

| Name         | Identifier    |
|--------------|---------------|
| Block entity | command_block |

Bedrock Edition:

| Name                    | Identifier              | Numeric ID | Form                       | Item ID[i 1]   | Translation key                   |
|-------------------------|-------------------------|------------|----------------------------|----------------|-----------------------------------|
| Command Block           | command_block           | 137        | Block & Giveable Item[i 2] | Identical[i 3] | tile.command_block.name           |
| Chain Command Block     | chain_command_block     | 189        | Block & Giveable Item[i 2] | Identical[i 3] | tile.chain_command_block.name     |
| Repeating Command Block | repeating_command_block | 188        | Block & Giveable Item[i 2] | Identical[i 3] | tile.repeating_command_block.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ a b c Available with /give command.

↑ a b c The block's direct item form has the same id as the block.


| Name         | Savegame ID  |
|--------------|--------------|
| Block entity | CommandBlock |

### Block states
See also: Block states

Java Edition:

| Name        | Default value | Allowed values           | Description                                       |
|-------------|---------------|--------------------------|---------------------------------------------------|
| conditional | false         | falsetrue                | True if the command block is in conditional mode. |
| facing      | north         | downeastnorthsouthupwest | The direction the command block is pointing.      |

Bedrock Edition:

| Name             | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                                                                                                           |
|------------------|---------------|---------------|----------------|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| conditional_bit  | 0x8           | false         | falsetrue      | 01                      | True if the command block is in conditional mode.                                                                                     |
| facing_direction | 0x10x20x4     | 0             | 012345         | 012345                  | The direction the command block is pointing.0: facing down 1: facing up 2: facing north 3: facing south 4: facing west 5: facing east |



### Block data
A command block has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format


 Block entity data
Tags common to all block entities
 auto: 1 or 0 (true/false) - Allows to activate the command without the requirement of a redstone signal.
 Command: The command to issue to the server.
 conditionMet: 1 or 0 (true/false) - Indicates whether a conditional command block had its condition met when last activated. True if not a conditional command block.
 CustomName: Optional. The name JSON text component of this command block, replacing the usual '@' when using commands such as /say and /tell.
 LastExecution: stores the tick a chain command block was last executed in.
 LastOutput: The last line of output generated by the command block. Still stored even if the game rule commandBlockOutput is false. Appears in the GUI of the block when right-clicked, and includes a timestamp of when the output was produced.
 powered: 1 or 0 (true/false) - States whether or not the command block is powered by redstone or not.
 SuccessCount: Represents the strength of the analog signal output by redstone comparators attached to this command block.
 TrackOutput: 1 or 0 (true/false) - Determines whether the LastOutput is stored. Can be toggled in the GUI by clicking a button near the "Previous Output" textbox. Caption on the button indicates current state: "O" if true, "X" if false.
 UpdateLastExecution: 1 or 0 (true/false) - Defaults to true. If set to false, loops can be created where the same command block can run multiple times in one tick.

Bedrock Edition:

See Bedrock Edition level format/Block entity format.

