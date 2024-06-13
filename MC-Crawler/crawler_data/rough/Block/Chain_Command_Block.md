# Command Block
A command block is a block that can execute commands. Because it cannot be obtained or used in Survival mode without cheats, it is primarily used on multiplayer servers, in Creative worlds, and custom maps.

An impulse command block is the default block type; it executes only once when activated.

A chain command block executes every time when triggered.

A repeating command block executes every game tick as long as it is activated.

## Contents
- 1 Obtaining
- 2 Usage
	- 2.1 Modification
	- 2.2 Activation
	- 2.3 Execution
		- 2.3.1 Trigger and chaining
	- 2.4 Output
		- 2.4.1 Success count
		- 2.4.2 Message
	- 2.5 Notes
		- 2.5.1 Easter eggs
	- 2.6 Piston interactivity
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
	- 4.3 Block data
- 5 History
- 6 Issues
- 7 Gallery
	- 7.1 Screenshots
- 8 References
- 9 External links

## Obtaining
In Java Edition, command blocks are available in the Creative inventory under the "Operator Utilities" tab, if the "Operator Items Tab" setting in the "Controls" Options tab is set to "ON". Across both Java and Bedrock editions, they can either be obtained by using the pick block control, or by using various commands, such as /give @s minecraft:command_block, or /setblock ~ ~ ~ command_block.

Just like other blocks that can store NBT data, using pick block + CTRL copies the command and options inside the command block. This allows it to be placed elsewhere without having to re-enter the data inside.

Command blocks are not flammable, and have the same blast resistance as bedrock. Command blocks, structure blocks, and jigsaw blocks cannot be mined in Survival.

Command blocks can be placed by a non-operator player.

## Usage
See also: Commands and Tutorials/Command blocks and functions

A command block can execute commands when activated by redstone power. It always has permissions of level 2‌[Java Edition  only]/level 1‌[Bedrock Edition  only], so it can be used to allow a specific use of a command by players who can't use that command in general (for example, allowing anyone to obtain a specific item with /give without allowing everyone to /give themselves whatever they want).

A command block has an orientation that determines the chain command block to activate, and the blocks to be checked to see if a command block in "Conditional" mode executes.

To execute the command, in Java Edition in multiplayer enable-command-block in the server.properties file must be set to true (default is false); in Bedrock Edition "Command Blocks Enabled" in options must be enabled.

### Modification
Java Edition command block GUI
To enter command or modify the command block, use the Use Item control on the command block to open the command block GUI (graphical user interface). The GUI opens only if the player is in Creative mode, and has the proper permissions. That means, in singleplayer, "Allow Cheats"‌[JE  only] or "Activate Cheats"‌[BE  only] in options must be enabled. In multiplayer, GUI can be opened only by operators in Creative mode, and in Java Edition op-permission-level in the server.properties file must be set to 2 or above (default is 4).

In Java Edition to enter command or modify the command block, enable-command-block in the server.properties file must be set to true (default is false).

Bedrock edition command block GUI
In Java Edition, opening the GUI in singleplayer pauses the game.

** Console Command‌[JE  only]/Command Input‌[BE  only] **
Commands can be entered in the top text pane. The text limit for commands in a command block is 32,500 characters, but the text pane can show only a small portion of this amount at a time.
Commands in a command block donotneed to be prefixed with the forward-slash (/) as they do in the chat window, but doing so still works.
PressTab ↹to complete words or cycle through options.
InBedrock Edition, below the console command text pane are some reminder tips about how to usetarget selectors.
** Previous Output **
The bottom text pane displays the output message (success or failure) of the last executed command (it is blank‌[JE  only]or " - "‌[BE  only]initially). Its text is not editable.
A button to the right of the Previous Output text pane‌[JE  only]or the left of the "Previous Output"‌[BE  only]specifies whether the last output should be stored and displayed. It isO‌[JE  only]/enabled‌[BE  only]when the output text should be stored andX‌[JE  only]/disabled‌[BE  only]when the output text should not be stored. For worlds with many command blocks, especially command blocks running on fast clocks, not storing the output text can reduce memory and storage requirements.
If gamerulesendCommandFeedbackis true (the default), default toO‌[JE  only]/enabled‌[BE  only]. Otherwise defaults toX‌[JE  only]/disabled‌[BE  only].
** Block Type **
Left: "Impulse" block type.Middle: "Chain" block type.Right: "Repeating" block type.Top: "Unconditional" mode.Bottom: "Conditional" mode.
Click the "Impulse/Chain/Repeat" button‌[JE  only]/"Block Type:" dropdown menu‌[BE  only]to change the command block's type. The default state is "Impulse", but non-default command blocks can be obtained and placed. The command block also changes color when changing its command block type:
- "Impulse" command blocks are orange. They execute once every time they areactivated.
- "Chain" command blocks are cyan. They execute once every time they aretriggeredif they have been activated.
- "Repeat" command blocks are blue. They execute their commands once every one gametick(or more‌[BE  only]) as long as they are activated.

** Condition **
Click the "Conditional/Unconditional"‌[JE  only]button/"Condition:" dropdown menu‌[BE  only]to change the command block's conditional behavior:
- "Conditional": A command block in conditional mode executes its command only when the command block behind it has executed successfully ("Success count"is greater than 0).
- "Unconditional" (default): A command block in unconditional mode executes its command even if there's a command block behind it that didn't execute its command successfully.

"Behind it" in the sense of opposite to the direction the command block is facing, regardless of chain direction or even if chaining is occurring.
** Redstone **
Click the "Always Active/Needs Redstone" button‌[JE  only]/"Redstone:" dropdown menu‌[BE  only]to change the command block's activation requirements:
- "Needs Redstone" (the default for impulse and repeat command blocks): A command block in the "Needs Redstone" setting can beactivatedonly with redstone.
- "Always Active" (the default for chain command blocks): The command block is activated when set to "Always Active". Then it is always active even without redstone activation.

** Execute on First Tick‌[BE  only] **
Specifies whether a repeat command block executes its command as soon as it isactivated. If it's disabled, executes the first time after the delay from the time when it is activated.
** Delay in Ticks‌[BE  only] **
For impulse or chain command block, specifies how many game ticks it delays before executing a command after it is activated or triggered.
For repeat command block, specifies how many game ticks it delays to execute again.
Note that for impulse or repeat command block, 0 and 1 work the same; the game takes 0 as 1. However, For chain command block, 0 and 1 are different.
** Hover Note‌[BE  only] **
Specifies the name of the command block, which can be seen when you point to the block. It is also used formessage commands. If the command block had been named in an anvil before placement, that name is used as well. If it is empty, defaults to!.
** Done **
InJava Edition, click the "Done" button orEnterto save the command and leave the command block GUI.
InBedrock Edition, close the GUI to save the command and changes.
** Cancel **
Click the "Cancel" button orEsc‌[JE  only]to leave the command block GUI without saving any changes.
### Activation
Command blocks are redstone mechanisms and can be activated by:

- An adjacent activepower component: for example, alever, ablock of redstone, adaylight sensor, abuttonetc.
- An adjacentpowered block(for example, an opaque block with an active redstone torch under it)
- A poweredredstone comparatororredstone repeaterfacing the mechanism component
- Poweredredstone dustconfigured to point at the command block (or on top of it) or directionless; a command block isnotactivated by adjacent powered redstone dust that is configured to point away from it.

A command block can also be activated by setting it to "Always Active" mode.

When activated, a command block executes its command, depending on the command block's type:

- An impulse command block executes its command once.
- A chain command block does not execute its command until it is triggered.
- A repeat command block executes its command once every one game tick (or more‌[BE  only]) until no longer activated.

### Execution
An impulse command block, when it is activated, checks whether the command block behind it has executed successfully (if in conditional mode). After the delay of 1 game tick (or more‌[BE  only]), if the condition is met before the delay (if in "Conditional" mode), it executes its command once and triggers the chain command block it is pointing to.

A repeat command block, when it is activated, after 1 game tick (always 1 no matter how many "Delay in Ticks" is), checks whether the command block behind it has executed successfully (if in conditional mode). If the condition is met, and if "Execute on First Tick" is enabled in Bedrock Edition, it executes its command once and triggers the chain command block it is pointing to. If it is still activated, it then checks, executes, and triggers the chain command block again after 1 game tick (or more‌[BE  only]).

When executing a command, it also updates its success count: If in "Conditional" mode, if the command block behind it didn't execute successfully, it sets its success count to 0. Otherwise, it sets it to the success count of the command.

Also:

- When an impulse or repeat command block in "Needs Redstone" mode with a command is placed or is cloned by a command to a powered location, the new command block executes its command only if it hasn't been activated with redstone. InJava Edition, it also needs a block update to execute its command.
- When an impulse or repeat command block in "Always Active" mode with a command is placed or is cloned by a command to a powered location, the new command block executes its command only if it hasn't been activated with redstone.
- When an impulse or chain command block is set to "Repeat", if it has been activated, checks whether the command block behind it has executed successfully (if in conditional mode). After 1 game tick (always 1 no matter how many "Delay in Ticks" is), if the condition is met, it executes its command once and triggers the chain command block it is pointing to. Then it checks, executes, and triggers the chain command block again after 1 game tick (or more‌[BE  only]).

#### Trigger and chaining
If any command block having executed its command (whether successfully or unsuccessfully) faces a chain command block, it triggers the chain command block to also attempt execution.

When a chain command block is triggered,

- If it has been activated,
	- It checks whether it is in "Conditional" mode and the command block behind it hasn't executed successfully (Behind in the sense of the direction it is facing, not in the sense of which command block chained to it),
		- If true, it triggers another chain command block it is facing, without executing the command.
		- If false, it checks whether it has been already executed in this game tick. If false, it executes the command and triggers another chain command block it is facing. If true, it does nothing. That means that chained execution cannot be passed to a command block that has already executed in that game tick (loops execute only once).
- If it has not been activated, it triggers the chain command block it is facing to attempt execution.

Chained command blocks execute simultaneously in the same game tick in the order they are chained.

In Bedrock Edition, it can also delay before executing commands if "Delay in Ticks" is not 0:

When it is triggered,
- If it has been activated, the chain command block checks whether the command block behind it has executed successfully (if in conditional mode), then it delays.
	- After a delay, if the condition is met before the delay (if in "Conditional" mode), it executes its command once and triggers the chain command block it is pointing to no matter whether the condition met.
- If it has not been activated, it triggers (without delay) the chain command block it is facing to attempt execution.

In Java Edition, it can execute multiple times in the same game tick if "UpdateLastExecution" is set to false. In this case, it does not check whether it has already executed in this game tick.

If the chain command block has been activated when triggered, it also updates its success count: If in "Conditional" mode, if the command block behind it didn't execute successfully, it sets its success count to 0. Otherwise, it sets it to the success count of the command.

### Output
When activated, a command block can produce multiple types of output:

#### Success count
A command block can power a redstone comparator facing away from it (possibly separated by a block) with signal strength specific to the success count. Success count is an integer between 0 to 2,147,483,647 (inclusive).
The signal strength always reflects the last command executed, even after the command block is deactivated.
InJava Edition, success count is usually 0 or 1, except for/functionand/execute.
InBedrock Edition, success count is an integer related to the command (e.g., the number of players affected by the command, the number of blocks that were altered, the value returned by the command, etc.)
InJava Edition, leaving the command block GUI by clicking "Done" or pressingEnterresets the success count to 0, regardless of whether changes were made in the GUI. InBedrock Edition, leaving the GUI with changes resets the success count to 0.
#### Message
The output message describes the success or failure of the executed command, and may be written to multiple destinations:
Previous Output:The output message is always written to the "Previous Output" text pane of the command block GUI.
Chat:The output message is written to the chat text in singleplayer mode, or broadcast to all otheropsin multiplayer mode, unless it has been suppressed with/gamerule commandBlockOutput false. Some commands may write additional text to the chat as their normal function, which won't be suppressed (for example, the/saycommand writes a message to the chat of all players), separate from the output message. Chat messages that would usually be prefaced by a player's name (such as from the/me,/sayand/tellcommands) use@‌[Java Edition  only]/!‌[Bedrock Edition  only]as the player name. If the command block had been named in ananvilbefore placement, that name is used instead. InBedrock Edition, it can also modified in the GUI.
Logs:The output message is written to multiplayer server logs unless it has been suppressed with/gamerule logAdminCommands false.
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

| Name                    | Identifier                | Form         | Block tags                          | Translation key                           |
|-------------------------|---------------------------|--------------|-------------------------------------|-------------------------------------------|
| Command Block           | `command_block`           | Block & Item | `dragon_immune`<br/>`wither_immune` | `block.minecraft.command_block`           |
| Chain Command Block     | `chain_command_block`     | Block & Item | `dragon_immune`<br/>`wither_immune` | `block.minecraft.chain_command_block`     |
| Repeating Command Block | `repeating_command_block` | Block & Item | `dragon_immune`<br/>`wither_immune` | `block.minecraft.repeating_command_block` |

| Name         | Identifier      |
|--------------|-----------------|
| Block entity | `command_block` |

Bedrock Edition:

| Name                    | Identifier                | Numeric ID | Form                       | Item ID[i 1]   | Translation key                     |
|-------------------------|---------------------------|------------|----------------------------|----------------|-------------------------------------|
| Command Block           | `command_block`           | `137`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.command_block.name`           |
| Chain Command Block     | `chain_command_block`     | `189`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.chain_command_block.name`     |
| Repeating Command Block | `repeating_command_block` | `188`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.repeating_command_block.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑ a b cAvailable with /give command.
3. ↑ a b cThe block's direct item form has the same id as the block.

| Name         | Savegame ID    |
|--------------|----------------|
| Block entity | `CommandBlock` |

### Block states
See also: Block states

Java Edition:

| Name        | Default value | Allowed values                                                | Description                                       |
|-------------|---------------|---------------------------------------------------------------|---------------------------------------------------|
| conditional | `false`       | `false`<br/>`true`                                            | True if the command block is in conditional mode. |
| facing      | `north`       | `down`<br/>`east`<br/>`north`<br/>`south`<br/>`up`<br/>`west` | The direction the command block is pointing.      |

Bedrock Edition:

| Name             | Metadata Bits             | Default value | Allowed values                              | Values forMetadata Bits                     | Description                                                                                                                                                    |
|------------------|---------------------------|---------------|---------------------------------------------|---------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| conditional_bit  | `0x8`                     | `false`       | `false`<br/>`true`                          | `0`<br/>`1`                                 | True if the command block is in conditional mode.                                                                                                              |
| facing_direction | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | The direction the command block is pointing.0: facing down<br/>1: facing up<br/>2: facing north<br/>3: facing south<br/>4: facing west<br/>5: facing east<br/> |



### Block data
A command block has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format

- Block entity data
	- 
	- Tags common to all block entities
	- auto: 1 or 0 (true/false) - Allows to activate the command without the requirement of a redstone signal.
	- Command: The command to issue to the server.
	- conditionMet: 1 or 0 (true/false) - Indicates whether a conditional command block had its condition met when last activated. True if not a conditional command block.
	- CustomName: Optional. The name JSON text component of this command block, replacing the usual '@' when using commands such as/sayand/tell.
	- LastExecution: stores the tick a chain command block was last executed in.
	- LastOutput: The last line of output generated by the command block. Still stored even if thegame rulecommandBlockOutputisfalse. Appears in the GUI of the block when right-clicked, and includes a timestamp of when the output was produced.
	- powered: 1 or 0 (true/false) - States whether or not the command block is powered by redstone or not.
	- SuccessCount: Represents the strength of the analog signal output by redstone comparators attached to this command block.
	- TrackOutput: 1 or 0 (true/false) - Determines whether the LastOutput is stored. Can be toggled in the GUI by clicking a button near the "Previous Output" textbox. Caption on the button indicates current state: "O" if true, "X" if false.
	- UpdateLastExecution: 1 or 0 (true/false) - Defaults to true. If set to false, loops can be created where the same command block can run multiple times in one tick.

Bedrock Edition:

SeeBedrock Edition level format/Block entity format.
