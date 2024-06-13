# Commands
Commands, also known as console commands and slash commands, are advanced features activated by typing certain strings of text.

## Contents
- 1 Usage
- 2 Command guide
	- 2.1 Syntax
	- 2.2 Restrictions
		- 2.2.1 Cheats
	- 2.3 Result
- 3 List and summary of commands
	- 3.1 Available in Java Edition
	- 3.2 Debugging commands
	- 3.3 Available in Bedrock Edition and Education
	- 3.4 Hidden commands
	- 3.5 Removed commands
		- 3.5.1 Removed from Java Edition
		- 3.5.2 Removed from Bedrock Edition or Education
		- 3.5.3 Other removed commands
			- 3.5.3.1 Developer commands
			- 3.5.3.2 Agent commands
	- 3.6 Joke commands
- 4 History
	- 4.1 Command additions and changes
	- 4.2 April Fools commands
- 5 Issues
- 6 See also
- 7 External links

## Usage
In the client, commands are entered via the chat window, which is displayed by pressing the T / ‌[BE  only] / ‌[BE  only] or / key. Using the / key also enters the forward-slash that commands require as a prefix, so it is a useful shortcut. The Up and Down keys can be used to view previously entered text, including all previously executed commands.

When the cursor is at a location corresponding to some types of argument (such as an entity ID), a list of applicable values appears above the text box. If the argument is already containing some characters, the list displays only those values containing the typed text. Pressing Tab while entering commands cycles through possible commands or arguments, and can be used to auto-enter them.

Commands may also be entered in a multiplayer server's console, but are not preceded by a / when entered this way. A server owner running commands in this way is often referred to as "ghosting".

Commands in command blocks can be preceded by a slash, but it is not required. 

Commands can be executed in the following ways;

- Entered by a player in the chat screen.
- Executed by acommand blockor aminecart with command block.
- Infunctions, in adata pack‌[JE  only]orbehavior pack‌[BE  only].
- In scripts, in abehavior pack‌[BE  only].
- In animation controllers, in abehavior pack‌[BE  only].
- In a block event response, in abehavior pack‌[BE  only].
- In an entity event response, in abehavior pack‌[BE  only].
- In a dedicatedserver, entered in the console.
- Clicking aJson textthat has "run_command" action.‌[JE  only]
- Requested by a WebSocket server connected to a client.‌[BE  only]
- By anNPCdialogue.‌[BE  only]

## Command guide
### Syntax
In Java Edition: 



Entry
Meaning


plain text
Enter this literally, exactly as shown.


<argumentName>
An argument, which should be replaced with an appropriate value.



Decorator
Meaning


[entry]
This entry is optional.


(entry|entry)(entry|entry|entry)etc.
Required. Pick one of these entries.


[entry|entry][entry|entry|entry]etc.
Optional. Pick one of these entries.


ellipsis ...
In the game, another full command is required.In this wiki, some required parts are left out.

For example:[<size>]is an optional argument.[size]is an optional plain text.
For example:advancement (grant|revoke) <targets> only <advancement> [<criterion>], whereadvancementandonlyare plain texts that shouble be entered literally;(grant|revoke)means we should pick one plain text fromgrantandrevoke;<targets>and<advancement>are required arguments, which should be replaced with appropriate values;[<criterion>]is an optional argument.
In Bedrock Edition: 



Entry
Meaning


plain text
Enter this literally, exactly as shown.


name: type
An argument, which should be replaced with an appropriate value.


command: command
Another full command is required.


plain text|plain text(plain text|plain text|plain text)etc
Enter one of these texts literally.



Decorator
Meaning


<entry>
This entry is required.


[entry]
This entry is optional.


ellipsis ...
In this wiki, some required parts are left out.

The angle bracket decorator (<entry>) cannot be applied on aplain text. A required plain text does not need any decorator.
For example, bothsetand<set>represent a required plain text, but the latter one is not used usually.<size: int>is a required argument.
In both Java Edition and Bedrock Edition, square bracket decorator ([entry]) mean that an entry is optional. Entries decorated with square brackets can only be at the end of a command. Multiple entries decorated with square brackets are allowed at the end of a command, for example, a [b] [c] at the end of a command indicates that only a, a b, and a b c are valid.

### Restrictions
Most commands require the executor have a high enough permission level. That means most commands are available in the singleplayer world only if cheats are enabled, and available in multiplayer server only if the player is an operator. See permission level for details.

Some commands have restrictions on who can use the command or in what context.

- None: The command has no restriction.
- Cheats only‌[BE  only]: Applicable only toBedrock Edition. When executedby the server, or a script, the command is available no matter whether cheats are enabled. (Commands from the console, ascheduled function, aticking function, or a WebSocket server connected with the dedicated server are executed by the server.) When executedin other ways, the command is available only if cheats are enabled. When cheats are disabled, these commands can't be used unless executed by a server or a script, even if the executor has a highpermission level.
	- InJava Edition, if s executor has a high enough permission level, it can use corresponding commands regardless of whether cheats are allowed.
- Dedicated server only: The command is available only on a dedicated server.
- Singleplayer only: The command is not available on a dedicated server.

#### Cheats
Cheats can be enabled when creating a new world by Allow Cheats‌[until JE 1.20.5] / Allow Commands‌[upcoming: JE 1.20.5] / Cheats‌[Bedrock Edition  only] options.

In Java Edition, the "Allow Commands" option when creating a new world is only affect the player in a singleplayer world or the owner of a LAN world. The "Allow Commands" option when opening a LAN world affects all players in the LAN world.

In Java Edition, in singleplayer worlds where cheats were not enabled at creation, they can be enabled on a temporary basis by opening the current game session to LAN play ( Esc → "Open to LAN", then "Allow Cheats" button and "Start LAN World"). The player does not actually need to be on a LAN or have others join. This is not permanent but allows the use of commands until the player quits the world, and changes the player makes via commands (items spawned, etc.) are saved with the world. The player can do this each time the player starts playing the world again. Note that this disables game pausing for the duration, so while open to LAN, the player should get somewhere safe or reload their world before using the Game Menu. The player can disable the LAN world by reloading the world. To permanently enable cheats, the level.dat file has to be edited. 

In Bedrock Edition, cheats can be toggled at any time in the "Game" tab of the settings menu. Enabling cheats in a world permanently prevents players from unlocking achievements in that world, even if cheats are later turned off. In BDS, /changesetting command can be used to toggle cheats.

