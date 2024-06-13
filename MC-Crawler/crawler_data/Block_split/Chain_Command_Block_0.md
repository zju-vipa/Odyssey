# Command Block
A command block is a block that can execute commands. Because it cannot be obtained or used in Survival mode without cheats, it is primarily used on multiplayer servers, in Creative worlds, and custom maps.

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

Console Command‌[JE  only]/Command Input‌[BE  only]
Commands can be entered in the top text pane. The text limit for commands in a command block is 32,500 characters, but the text pane can show only a small portion of this amount at a time.
Commands in a command block do not need to be prefixed with the forward-slash (/) as they do in the chat window, but doing so still works.
Press Tab ↹ to complete words or cycle through options.
In Bedrock Edition, below the console command text pane are some reminder tips about how to use target selectors.
Previous Output
The bottom text pane displays the output message (success or failure) of the last executed command (it is blank‌[JE  only] or " - "‌[BE  only] initially). Its text is not editable.
A button to the right of the Previous Output text pane‌[JE  only] or the left of the "Previous Output"‌[BE  only] specifies whether the last output should be stored and displayed. It is O‌[JE  only]/enabled‌[BE  only] when the output text should be stored and X‌[JE  only]/disabled‌[BE  only] when the output text should not be stored. For worlds with many command blocks, especially command blocks running on fast clocks, not storing the output text can reduce memory and storage requirements.
If gamerule sendCommandFeedback is true (the default), default to O‌[JE  only]/enabled‌[BE  only]. Otherwise defaults to X‌[JE  only]/disabled‌[BE  only].
Block Type
Left: "Impulse" block type.Middle: "Chain" block type.Right: "Repeating" block type.Top: "Unconditional" mode.Bottom: "Conditional" mode.
Click the "Impulse/Chain/Repeat" button‌[JE  only]/"Block Type:" dropdown menu‌[BE  only] to change the command block's type. The default state is "Impulse", but non-default command blocks can be obtained and placed. The command block also changes color when changing its command block type:
"Impulse" command blocks are orange. They execute once every time they are activated.
"Chain" command blocks are cyan. They execute once every time they are triggered if they have been activated.
"Repeat" command blocks are blue. They execute their commands once every one game tick (or more‌[BE  only]) as long as they are activated.
Condition
Click the "Conditional/Unconditional"‌[JE  only] button/"Condition:" dropdown menu‌[BE  only] to change the command block's conditional behavior:
"Conditional": A command block in conditional mode executes its command only when the command block behind it has executed successfully ("Success count" is greater than 0).
"Unconditional" (default): A command block in unconditional mode executes its command even if there's a command block behind it that didn't execute its command successfully.
"Behind it" in the sense of opposite to the direction the command block is facing, regardless of chain direction or even if chaining is occurring.
Redstone
Click the "Always Active/Needs Redstone" button‌[JE  only]/"Redstone:" dropdown menu‌[BE  only] to change the command block's activation requirements:
"Needs Redstone" (the default for impulse and repeat command blocks): A command block in the "Needs Redstone" setting can be activated only with redstone.
"Always Active" (the default for chain command blocks): The command block is activated when set to "Always Active". Then it is always active even without redstone activation.
Execute on First Tick‌[BE  only]
Specifies whether a repeat command block executes its command as soon as it is activated. If it's disabled, executes the first time after the delay from the time when it is activated.
Delay in Ticks‌[BE  only]
For impulse or chain command block, specifies how many game ticks it delays before executing a command after it is activated or triggered.
For repeat command block, specifies how many game ticks it delays to execute again.
Note that for impulse or repeat command block, 0 and 1 work the same; the game takes 0 as 1. However, For chain command block, 0 and 1 are different.
Hover Note‌[BE  only]
Specifies the name of the command block, which can be seen when you point to the block. It is also used for message commands. If the command block had been named in an anvil before placement, that name is used as well. If it is empty, defaults to !.
Done
In Java Edition, click the "Done" button or Enter to save the command and leave the command block GUI.
In Bedrock Edition, close the GUI to save the command and changes.
Cancel
Click the "Cancel" button or Esc‌[JE  only]to leave the command block GUI without saving any changes.
