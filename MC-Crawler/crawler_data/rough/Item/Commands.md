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

### Result
After trying to run a command, it produces a certain result. There are various possible results, including "Unparseable", "Failed", "Successful", "Void"‌[JE  only], "Terminated"‌[JE  only], and "Error"‌[JE  only].

** Unparseable **
If the entered command is incomplete or any argument cannot be parsed by the server, the command is unparseable.
If an argument cannot be parsed by the server, in this wiki we often describe it as being specified incorrectly.
When typing an argument into the chat, it's noticeable if an argument is specified incorrectly inJava Edition.In Java Edition, if specified incorrectly, the argument is marked red and a syntax error message is displayed.
In Bedrock Edition, when typing in chat bar, if an argument can be parsed by the client, the next argument in syntax hint turns to white from gray. If all arguments (including optional arguments) are entered and parseable by the client, the whole syntax hint turns to gray from white. However, being able to be parsed by the client doesn't guarantee that this argument is parseable by the server.
InJava Edition, it behaves in the same way as typing in the chat when typing in acommand block.
InBedrock Edition, when entering into a command block, if the command is unparseable, a syntax error message is outputted into its output box when closing the command block screen.
When trying to execute an unparsable command, an error message is displayed.In Java Edition, it is "Unknown or incomplete command" or "Incorrect argument for command".
In Bedrock Edition, it is "Unknown command" or "Syntax error: unexpected ... at ...".
If any command in afunctionfile is unparseable, the function is unable to be loaded by the game.
InBedrock Edition, if a command in a script is unparseable, an error is thrown when trying run the command.
** Error‌[JE  only] **
If an error occurs with a command, it means that there's a noticeable bug on the command.
Technically, it means an exception other thanbrigadier.exceptions.CommandSyntaxExceptionis thrown during execution.
** Void‌[JE  only] **
Exclusive to/functioncommand. When it is void, the command has noresultorsuccessvalue that can be stored by/execute store.
** Terminating‌[JE  only] **
Exclusive to/executecommand. When running a/executecommand, if the number of execution branches becomes 0, the command terminates, ending before the last sub-command is executed.
For example:/execute as @s run ...in a command block.
** Failed and Successful **
If a command is not unparseable, erroring, void, nor terminating, it may be failed or successful.
If the Success Count is not less than 0, the command is failed. Otherwise, the command is successful.The Success Count can be read by a redstone comparator from a command block or a script‌[Bedrock Edition  only].
InJava Edition, if the command cannot be executed by command blocks, it has no Success Count. It is failed when/execute store success ... run ...stores 0, and successful when/execute store success ... run ...stores 1.
InBedrock Edition, if the command cannot be executed by command blocks or scripts, it still has a Success Count, but cannot be obtained.
Note that when we say whether a command is failed or successful, it must not be unparseable, erroring, void, or terminating. Though when unparseable, erroring, void or terminating, the Success Count is 0, it is not considered as being failed nor successful.
Note that not all "successful" commands actually do something, and not all "failed" commands fail to do something useful.
## List and summary of commands
The tables below summarizes all commands.

### Available in Java Edition
| Command            | Description                                                                                                                     | OP level required                      | Multiplayer only |   |   |   |   |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|------------------|---|---|---|---|
| `/advancement`     | Gives, removes, or checks playeradvancements.                                                                                   | 2                                      | —                | — | — |   | — |
| `/attribute`       | Queries, adds, removes or sets an entity attribute.                                                                             | 2                                      | —                | — |   |   | — |
| `/ban`             | Adds player to banlist.                                                                                                         | 3                                      | Yes              | — | — |   | — |
| `/ban-ip`          | Adds IP address to banlist.                                                                                                     | 3                                      | Yes              | — | — |   | — |
| `/banlist`         | Displays banlist.                                                                                                               | 3                                      | Yes              | — | — |   | — |
| `/bossbar`         | Creates and modifies bossbars.                                                                                                  | 2                                      | —                | — | — |   |   |
| `/clear`           | Clears items from player inventory.                                                                                             | 2                                      | —                | — | — |   | — |
| `/clone`           | Copies blocks from one place to another.                                                                                        | 2                                      | —                |   | — | — | — |
| `/damage`          | Applies damage to the specified entities.                                                                                       | 2                                      | —                | — |   |   | — |
| `/data`            | Gets, merges, modifies and removes block entity and entity NBT data.                                                            | 2                                      | —                |   |   |   | — |
| `/datapack`        | Controls loaded data packs.                                                                                                     | 2                                      | —                | — | — | — |   |
| `/debug`           | Starts or stops a debugging session.                                                                                            | 3                                      | —                | — | — | — | — |
| `/defaultgamemode` | Sets the defaultgame mode.                                                                                                      | 2                                      | —                | — | — | — |   |
| `/deop`            | Revokes operator status from a player.                                                                                          | 3                                      | Yes              | — | — |   | — |
| `/difficulty`      | Sets the difficulty level.                                                                                                      | 2                                      | —                | — | — | — |   |
| `/effect`          | Adds or removesstatus effects.                                                                                                  | 2                                      | —                | — |   |   | — |
| `/enchant`         | Adds an enchantment to a player's selected item.                                                                                | 2                                      | —                | — | — |   | — |
| `/execute`         | Executes another command.                                                                                                       | 2                                      | —                |   |   |   |   |
| `/experience`      | An alias of`/xp`. Adds or removes playerexperience.                                                                             | 2                                      | —                | — | — |   | — |
| `/fill`            | Fills a region with a specific block.                                                                                           | 2                                      | —                |   | — | — | — |
| `/fillbiome`       | Fills a region with a specific biome.                                                                                           | 2                                      | —                | — | — | — |   |
| `/forceload`       | Forceschunksto constantly be loaded or not.                                                                                     | 2                                      | —                | — | — | — |   |
| `/function`        | Runs afunction.                                                                                                                 | 2                                      | —                | — | — | — |   |
| `/gamemode`        | Sets a player'sgame mode.                                                                                                       | 2                                      | —                | — | — |   | — |
| `/gamerule`        | Sets or queries agame rulevalue.                                                                                                | 2                                      | —                | — | — | — |   |
| `/give`            | Gives an item to a player.                                                                                                      | 2                                      | —                | — | — |   | — |
| `/help`            | Provides help for commands.                                                                                                     | 0                                      | —                | — | — | — | — |
| `/item`            | Manipulates items in inventories.                                                                                               | 2                                      | —                |   |   |   | — |
| `/jfr`             | Starts or stops a JFR profiling.                                                                                                | 4                                      | —                | — | — | — | — |
| `/kick`            | Kicks a player off a server.                                                                                                    | 3                                      | —                | — | — |   | — |
| `/kill`            | Kills entities (players, mobs, items, etc.).                                                                                    | 2                                      | —                | — |   |   | — |
| `/list`            | Lists players on the server.                                                                                                    | 0                                      | —                | — | — |   | — |
| `/locate`          | Locates closest structure, biome, or point of interest.                                                                         | 2                                      | —                |   |   | — |   |
| `/loot`            | Drops items from an inventory slot onto the ground.                                                                             | 2                                      | —                |   |   |   | — |
| `/me`              | Displays a message about the sender.                                                                                            | 0                                      | —                | — | — |   | — |
| `/msg`             | An alias of`/tell`and`/w`. Displays a private message to other players.                                                         | 0                                      | —                | — | — |   | — |
| `/op`              | Grants operator status to a player.                                                                                             | 3                                      | Yes              | — | — |   | — |
| `/pardon`          | Removes entries from the banlist.                                                                                               | 3                                      | Yes              | — | — |   | — |
| `/pardon-ip`       | Removes entries from the banlist.                                                                                               | 3                                      | Yes              | — | — |   | — |
| `/particle`        | Creates particles.                                                                                                              | 2                                      | —                | — | — |   | — |
| `/perf`            | Captures info and metrics about the game for 10 seconds.                                                                        | 4                                      | Yes              | — | — | — |   |
| `/place`           | Used to place a configured feature, jigsaw, template, or structure at a given location.                                         | 2                                      | —                |   | — | — |   |
| `/playsound`       | Plays a sound.                                                                                                                  | 2                                      | —                | — | — |   | — |
| `/publish`         | Opens single-player world to local network.                                                                                     | 4                                      | SP only          | — | — | — |   |
| `/random`          | Draw a random value or control the random number sequence.                                                                      | 0 (without`sequence`)<br/>2            | —                | — | — | — | — |
| `/recipe`          | Gives or takes player recipes.                                                                                                  | 2                                      | —                | — | — |   | — |
| `/reload`          | Reloads loot tables, advancements, and functions from disk.                                                                     | 2                                      | —                | — | — | — |   |
| `/return`          | Control execution flow inside functions and change their return value.                                                          | 2                                      | —                | — | — | — | — |
| `/ride`            | Used to make entities ride other entities, stop entities from riding, make rides evict their riders, or summon rides or riders. | 2                                      | —                | — |   |   | — |
| `/save-all`        | Saves the server to disk.                                                                                                       | 4                                      | Yes              | — | — | — |   |
| `/save-off`        | Disables automatic server saves.                                                                                                | 4                                      | Yes              | — | — | — |   |
| `/save-on`         | Enables automatic server saves.                                                                                                 | 4                                      | Yes              | — | — | — |   |
| `/say`             | Displays a message to multiple players.                                                                                         | 2                                      | —                | — | — |   | — |
| `/schedule`        | Delays the execution of a function.                                                                                             | 2                                      | —                | — | — | — | — |
| `/scoreboard`      | Manages scoreboard objectives and players.                                                                                      | 2                                      | —                | — |   |   | — |
| `/seed`            | Displays theworld seed.                                                                                                         | 0 in singleplayer<br/>2 in multiplayer | —                | — | — | — |   |
| `/setblock`        | Changes a block to another block.                                                                                               | 2                                      | —                |   | — | — | — |
| `/setidletimeout`  | Sets the time before idle players are kicked.                                                                                   | 3                                      | Yes              | — | — |   | — |
| `/setworldspawn`   | Sets theworld spawn.                                                                                                            | 2                                      | —                | — | — | — |   |
| `/spawnpoint`      | Sets the spawn point for a player.                                                                                              | 2                                      | —                | — | — |   | — |
| `/spectate`        | Make one player in spectator mode spectate an entity.                                                                           | 2                                      | —                | — | — |   | — |
| `/spreadplayers`   | Teleports entities to random locations.                                                                                         | 2                                      | —                | — |   |   | — |
| `/stop`            | Stops a server.                                                                                                                 | 4                                      | Yes              | — | — | — |   |
| `/stopsound`       | Stops a sound.                                                                                                                  | 2                                      | —                | — | — |   | — |
| `/summon`          | Summons an entity.                                                                                                              | 2                                      | —                | — |   | — | — |
| `/tag`             | Controls entity tags.                                                                                                           | 2                                      | —                | — |   |   | — |
| `/team`            | Controls teams.                                                                                                                 | 2                                      | —                | — |   |   | — |
| `/teammsg`         | An alias of`/tm`. Specifies the message to send to team.                                                                        | 0                                      | —                | — | — |   | — |
| `/teleport`        | An alias of`/tp`. Teleports entities.                                                                                           | 2                                      | —                | — |   |   | — |
| `/tell`            | An alias of`/msg`and`/w`. Displays a private message to other players.                                                          | 0                                      | —                | — | — |   | — |
| `/tellraw`         | Displays a JSON message to players.                                                                                             | 2                                      | —                | — | — |   | — |
| `/tick`            | Controls the tick rate of the game.                                                                                             | 3                                      | —                | — | — | — |   |
| `/time`            | Changes or queries the world's game time.                                                                                       | 2                                      | —                | — | — | — |   |
| `/title`           | Manages screen titles.                                                                                                          | 2                                      | —                | — | — |   | — |
| `/tm`              | An alias of`/teammsg`. Specifies the message to send to team.                                                                   | 0                                      | —                | — | — |   | — |
| `/tp`              | An alias of`/teleport`. Teleports entities.                                                                                     | 2                                      | —                | — |   |   | — |
| `/transfer`        | Triggers a transfer of a player to another server.                                                                              | 3                                      | Yes              | — | — |   | — |
| `/trigger`         | Sets a trigger to be activated.                                                                                                 | 0                                      | —                | — | — |   | — |
| `/w`               | An alias of`/tell`and`/msg`. Displays a private message to other players.                                                       | 0                                      | —                | — | — |   | — |
| `/weather`         | Sets the weather.                                                                                                               | 2                                      | —                | — | — | — |   |
| `/whitelist`       | Manages server whitelist.                                                                                                       | 3                                      | Yes              | — | — |   | — |
| `/worldborder`     | Manages theworld border.                                                                                                        | 2                                      | —                | — | — | — |   |
| `/xp`              | An alias of`/experience`. Adds or removes playerexperience.                                                                     | 2                                      | —                | — | — |   | — |

### Debugging commands
Debugging commands are only enabled in internal development builds of Java Edition, and are not normally accessible in release versions.

| Command                 | Description                                                          | OP level required | Multiplayer only |   |   |  |   |
|-------------------------|----------------------------------------------------------------------|-------------------|------------------|---|---|--|---|
| `/warden_spawn_tracker` | Sets how many warnings asculk shriekergives before spawning awarden. | 2                 | —                | — | — |  | — |

### Available in Bedrock Edition and Education
| Command              | Description                                                                                                                     | BE  | edu | OP level required              | Server only |   |   |   |   |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------|-----|-----|--------------------------------|-------------|---|---|---|---|
| `/?`                 | An alias of`/help`. Provides help for commands.                                                                                 | Yes | Yes | 0                              | —           | — | — | — | — |
| `/ability`           | Grants or revokes a player ability.                                                                                             | Yes | Yes | 1                              | —           | — | — |   | — |
| `/allowlist`         | An alias of`/whitelist`. Manages server allowlist.                                                                              | Yes | —   | 4                              | Yes         | — | — |   | — |
| `/alwaysday`         | An alias of`/daylock`. Locks and unlocks the day-night cycle.                                                                   | Yes | Yes | 1                              | —           | — | — | — |   |
| `/camera`            | Switch to custom camera perspectives and fade the screen.                                                                       | Yes | —   | 1                              | —           | — | — |   | — |
| `/camerashake`       | Used to enable a camera shaking effect.                                                                                         | Yes | Yes | 1                              | —           | — | — |   | — |
| `/changesetting`     | Changes a setting on the dedicated server while it's running.                                                                   | Yes | —   | 4                              | Yes         | — | — | — | — |
| `/clear`             | Clears items from player inventory.                                                                                             | Yes | Yes | 1                              | —           | — | — |   | — |
| `/clearspawnpoint`   | Removes the spawn point for a player.                                                                                           | Yes | Yes | 1                              | —           | — | — |   | — |
| `/clone`             | Copies blocks from one place to another.                                                                                        | Yes | Yes | 1                              | —           |   | — | — | — |
| `/connect`           | An alias of`/wsserver`. Attempts to connect to the websocket server.                                                            | Yes | Yes | 0‌[edu  only]<br/>2‌[BE  only] | —           | — | — | — | — |
| `/damage`            | Applies damage to the specified entities.                                                                                       | Yes | —   | 1                              | —           | — |   |   | — |
| `/daylock`           | An alias of`/alwaysday`. Locks and unlocks the day-night cycle.                                                                 | Yes | Yes | 1                              | —           | — | — | — |   |
| `/dedicatedwsserver` | Attempts to connect to a websocket server.                                                                                      | Yes | —   | 0                              | Yes         | — | — | — | — |
| `/deop`              | Revokes operator status from a player.                                                                                          | Yes | Yes | 2                              | —           | — | — |   | — |
| `/dialogue`          | Opens NPC dialogue for a player.                                                                                                | Yes | Yes | 1                              | —           | — | — |   | — |
| `/difficulty`        | Sets the difficulty level.                                                                                                      | Yes | Yes | 1                              | —           | — | — | — |   |
| `/effect`            | Adds or removesstatus effects.                                                                                                  | Yes | Yes | 1                              | —           | — |   |   | — |
| `/enchant`           | Adds an enchantment to a player's selected item.                                                                                | Yes | Yes | 1                              | —           | — | — |   | — |
| `/event`             | Used to trigger an event on an entity.                                                                                          | Yes | —   | 1                              | —           | — |   |   | — |
| `/execute`           | Executes another command.                                                                                                       | Yes | Yes | 1                              | —           |   |   |   |   |
| `/fill`              | Fills a region with a specific block.                                                                                           | Yes | Yes | 1                              | —           |   | — | — | — |
| `/fog`               | Used for managing active fog settings for players.                                                                              | Yes | —   | 1                              | —           | — | — |   | — |
| `/function`          | Runs afunction.                                                                                                                 | Yes | Yes | 1                              | —           | — | — | — |   |
| `/gamemode`          | Sets a player'sgame mode.                                                                                                       | Yes | Yes | 1                              | —           | — | — |   | — |
| `/gamerule`          | Sets or queries agame rulevalue.                                                                                                | Yes | Yes | 1                              | —           | — | — | — |   |
| `/gametest`          | To test the GameTest features.                                                                                                  | Yes | —   | 1                              | —           | — | — | — | — |
| `/give`              | Gives an item to a player.                                                                                                      | Yes | Yes | 1                              | —           | — | — |   | — |
| `/help`              | An alias of`/?`. Provides help for commands.                                                                                    | Yes | Yes | 0                              | —           | — | — | — | — |
| `/hud`               | Changes the visibility of aHUD element.                                                                                         | Yes | —   | 1                              | —           | — | — |   | — |
| `/immutableworld`    | Allows setting immutable state of a world.                                                                                      | Yes | Yes | 1                              | —           | — | — | — |   |
| `/kick`              | Kicks a player off a server.                                                                                                    | Yes | Yes | 1                              | —           | — | — |   | — |
| `/kill`              | Kills entities (players, mobs, items, etc.).                                                                                    | Yes | Yes | 1                              | —           | — |   |   | — |
| `/list`              | Lists players on the server.                                                                                                    | Yes | Yes | 0                              | —           | — | — |   | — |
| `/locate`            | Locates closest structure or biome.                                                                                             | Yes | Yes | 1                              | —           |   |   | — |   |
| `/loot`              | Drops items from an inventory slot onto the ground.                                                                             | Yes | —   | 2                              | —           |   |   |   | — |
| `/me`                | Displays a message about the sender.                                                                                            | Yes | Yes | 0                              | —           | — | — |   | — |
| `/mobevent`          | Enables/disables a specified mob event.                                                                                         | Yes | Yes | 1                              | —           | — | — |   | — |
| `/msg`               | An alias of`/tell`and`/w`. Displays a private message to other players.                                                         | Yes | Yes | 0                              | —           | — | — |   | — |
| `/music`             | Allows the player to control playing music tracks.                                                                              | Yes | —   | 1                              | —           | — | — |   | — |
| `/op`                | Grants operator status to a player.                                                                                             | Yes | Yes | 2                              | —           | — | — |   | — |
| `/ops`               | An alias of`/permission`. Reloads and applies permissions.                                                                      | Yes | Yes | 4                              | Yes         | — | — |   | — |
| `/particle`          | Creates particles.                                                                                                              | Yes | Yes | 1                              | —           | — | — |   | — |
| `/permission`        | An alias of`/ops`. Reloads and applies permissions.                                                                             | Yes | Yes | 4                              | Yes         | — | — |   | — |
| `/playanimation`     | Used to run a one-off animation.                                                                                                | Yes | —   | 1                              | —           | — |   |   | — |
| `/playsound`         | Plays a sound.                                                                                                                  | Yes | Yes | 1                              | —           | — | — |   | — |
| `/recipe`            | Gives or takes player recipes.                                                                                                  | Yes | —   | —                              | —           | — | — |   | — |
| `/reload`            | Reloads loot tables, advancements, and functions from disk.                                                                     | Yes | Yes | 2                              | —           | — | — | — |   |
| `/remove`            | Removing agent.                                                                                                                 | —   | ?   | 2                              | —           | — |   | — | — |
| `/replaceitem`       | Replaces items in inventories.                                                                                                  | Yes | Yes | 1                              | —           |   |   |   | — |
| `/ride`              | Used to make entities ride other entities, stop entities from riding, make rides evict their riders, or summon rides or riders. | Yes | —   | 1                              | —           | — |   |   | — |
| `/save`              | Prepares a backup, queries its status, or resumes.                                                                              | Yes | —   | 4                              | Yes         | — | — | — |   |
| `/say`               | Displays a message to multiple players.                                                                                         | Yes | Yes | 1                              | —           | — | — |   | — |
| `/schedule`          | Delays the execution of a function.                                                                                             | Yes | —   | 1                              | —           | — | — | — | — |
| `/scoreboard`        | Manages scoreboard objectives and players.                                                                                      | Yes | Yes | 1                              | —           | — |   |   | — |
| `/script`            | Debugging options for GameTest Framework.                                                                                       | Yes | —   | ?                              | —           | — | — | — | — |
| `/scriptevent`       | Triggers a script event with an ID and message.                                                                                 | Yes | —   | ?                              | —           | — | — | — | — |
| `/setblock`          | Changes a block to another block.                                                                                               | Yes | Yes | 1                              | —           |   | — | — | — |
| `/setmaxplayers`     | Sets the maximum number of players allowed to join.                                                                             | Yes | Yes | 3                              | —           | — | — |   | — |
| `/setworldspawn`     | Sets theworld spawn.                                                                                                            | Yes | Yes | 1                              | —           | — | — | — |   |
| `/spawnpoint`        | Sets the spawn point for a player.                                                                                              | Yes | Yes | 1                              | —           | — | — |   | — |
| `/spreadplayers`     | Teleports entities to random locations.                                                                                         | Yes | Yes | 1                              | —           | — |   |   | — |
| `/stop`              | Stops a server.                                                                                                                 | Yes | —   | 4                              | Yes         | — | — | — |   |
| `/stopsound`         | Stops a sound.                                                                                                                  | Yes | Yes | 1                              | —           | — | — |   | — |
| `/structure`         | Used to save and load structures without having to use structure blocks items in inventories.                                   | Yes | —   | 1                              | —           |   |   | — |   |
| `/summon`            | Summons an entity.                                                                                                              | Yes | Yes | 1                              | —           | — |   | — | — |
| `/tag`               | Controls entity tags.                                                                                                           | Yes | Yes | 1                              | —           | — |   |   | — |
| `/teleport`          | An alias of`/tp`. Teleports entities.                                                                                           | Yes | Yes | 1                              | —           | — |   |   | — |
| `/tell`              | An alias of`/msg`and`/w`. Displays a private message to other players.                                                          | Yes | Yes | 0                              | —           | — | — |   | — |
| `/tellraw`           | Displays a JSON message to players.                                                                                             | Yes | Yes | 1                              | —           | — | — |   | — |
| `/testfor`           | Counts entities matching specified conditions.                                                                                  | Yes | Yes | 1                              | —           | — |   |   | — |
| `/testforblock`      | Tests whether a block is in a location.                                                                                         | Yes | Yes | 1                              | —           |   | — | — | — |
| `/testforblocks`     | Tests whether the blocks in two regions match.                                                                                  | Yes | Yes | 1                              | —           |   | — | — | — |
| `/tickingarea`       | Add, remove, or list ticking areas.                                                                                             | Yes | Yes | 1                              | —           | — | — | — |   |
| `/time`              | Changes or queries the world's game time.                                                                                       | Yes | Yes | 1                              | —           | — | — | — |   |
| `/title`             | Manages screen titles.                                                                                                          | Yes | Yes | 1                              | —           | — | — |   | — |
| `/titleraw`          | Controls screen titles with JSON messages.                                                                                      | Yes | Yes | 1                              | —           | — | — |   | — |
| `/toggledownfall`    | Toggles the weather.                                                                                                            | Yes | Yes | 1                              | —           | — | — | — |   |
| `/tp`                | An alias of`/teleport`. Teleports entities.                                                                                     | Yes | Yes | 1                              | —           | — |   |   | — |
| `/transfer`          | Triggers a transfer of a player to another server.                                                                              | Yes | Yes | 4                              | Yes         | — | — |   | — |
| `/volumearea`        | Add, remove, or list volume areas.                                                                                              | Yes | —   | 1                              | —           | — | — | — |   |
| `/w`                 | An alias of`/tell`and`/msg`. Displays a private message to other players.                                                       | Yes | Yes | 0                              | —           | — | — |   | — |
| `/wb`                | An alias of`/worldbuilder`. Ability to edit restricted blocks.                                                                  | Yes | Yes | 1                              | —           | — | — | — |   |
| `/weather`           | Sets the weather.                                                                                                               | Yes | Yes | 1                              | —           | — | — | — |   |
| `/whitelist`         | An alias of`/allowlist`. Manages server allowlist.                                                                              | Yes | —   | 4                              | Yes         | — | — |   | — |
| `/worldbuilder`      | An alias of`/wb`. Ability to edit restricted blocks.                                                                            | Yes | Yes | 1                              | —           | — | — | — |   |
| `/wsserver`          | An alias of`/connect`. Attempts to connect to the websocket server.                                                             | Yes | Yes | 0‌[edu  only]<br/>2‌[BE  only] | —           | — | — | — | — |
| `/xp`                | Adds or removes playerexperience.                                                                                               | Yes | Yes | 1                              | —           | — | — |   | — |

### Hidden commands

  

This feature is exclusive to  Bedrock Edition and  Minecraft Education. 


These commands are unavailable in general cases. Most of them can be accessed with a Websocket Server, NPC, or the Scripting API.

| Command               | Description                                                                         | BE  | edu | OP level required              | Server only |   |   |   |   |
|-----------------------|-------------------------------------------------------------------------------------|-----|-----|--------------------------------|-------------|---|---|---|---|
| `/agent`              | Controls the agent.                                                                 | Yes | Yes | 0‌[edu  only]<br/>1‌[BE  only] | —           | — |   | — | — |
| `/codebuilder`        | Sets Code Builder state for a player.                                               | —   | Yes | 1                              | —           | — | — | — | — |
| `/classroommode`      | Ability to edit restricted blocks.                                                  | —   | Yes | 0                              | —           | — | — | — | — |
| `/closechat`          | Closes the chat window of the local player if it is open.                           | —   | Yes | 0                              | —           | — | — | — | — |
| `/closewebsocket`     | Closes websocket connection if there is one.                                        | Yes | Yes | 0                              | —           | — | — | — | — |
| `/code`               | Launches Code Builder.                                                              | —   | Yes | 0                              | —           | — | — | — | — |
| `/enableencryption`   | Enable encryption for the current websocket connection.                             | Yes | Yes | 0                              | —           | — | — | — | — |
| `/getchunkdata`       | Gets pixels for a specific chunk.                                                   | Yes | Yes | 3                              | —           | — | — | — | — |
| `/getchunks`          | Gets list of chunks that are loaded.                                                | Yes | Yes | 3                              | —           | — | — | — | — |
| `/geteduclientinfo`   | Shows the information about the client.                                             | —   | Yes | 0                              | —           | — | — | — | — |
| `/geteduserverinfo`   | Shows the information about the server.                                             | Yes | —   | 0                              | Yes         | — | — | — | — |
| `/getlocalplayername` | Shows the name of the local player.                                                 | Yes | Yes | 0                              | —           | — | — | — | — |
| `/getspawnpoint`      | Gets the spawn position of the specified player(s).                                 | Yes | Yes | 3                              | —           | — | — | — | — |
| `/gettopsolidblock`   | Gets the position of the top non-air block below the specified position.            | Yes | Yes | 0‌[edu  only]<br/>1‌[BE  only] | —           | — | — | — | — |
| `/globalpause`        | Sets or gets the paused state of the game for all players.                          | Yes | Yes | 3                              | —           | — | — | — | — |
| `/lesson`             | Handle Educational Lesson reporting.                                                | —   | Yes | 0                              | —           | — | — | — | — |
| `/listd`              | Lists the information about players on the server.                                  | Yes | Yes | 3                              | —           | — | — |   | — |
| `/querytarget`        | Gets transform, name, and id information about the given target entity or entities. | Yes | Yes | 0‌[edu  only]<br/>2‌[BE  only] | —           | — |   |   | — |
| `/spawnitem`          | Spawns an item entity at position.                                                  | —   | Yes | 0                              | —           | — |   | — | — |
| `/takepicture`        | Takes a photo of a player or from a player's point of view.                         | Yes | Yes | 1                              | —           | — | — | — |   |

### Removed commands
#### Removed from Java Edition
| Command          | Description                                                             | Version removed                 | Reason for deletion                                           | OP level required | Multiplayer only |   |   |   |   |
|------------------|-------------------------------------------------------------------------|---------------------------------|---------------------------------------------------------------|-------------------|------------------|---|---|---|---|
| `/?`             | An alias of`/help`. Provides help for commands.                         | Java Edition 1.13<br/>(17w45a)  | ?                                                             | 0                 | —                | — | — | — | — |
| /achievement     | Gives or takes an achievement from a player                             | Java Edition 1.12<br/>(17w13a)  | Achievementswere superseded byadvancements                    | 2                 | —                | — | — |   | — |
| /banip           | Bans a player by IP number                                              | Java Edition Indev 0.31         | Superseded by`/ban-ip`                                        | 3                 | Yes              | — | — |   | — |
| /blockdata       | Modifies the data tag of a block                                        | Java Edition 1.13<br/>(17w47a)  | Superseded by`/data`                                          | 2                 | —                |   | — | — | — |
| /broadcast       | Broadcasts a message across the entire server                           | Java Edition Classic 0.0.16a_01 | Superseded by`/say`                                           | 1                 | —                | — | — | — | — |
| /chunk           | Force chunks to load constantly or not                                  | Java Edition 1.13.1<br/>(pre1)  | Superseded by`/forceload`                                     | 2                 | —                | — | — | — |   |
| /entitydata      | Modifies the data tag of an entity                                      | Java Edition 1.13<br/>(17w45b)  | Superseded by`/data`                                          | 2                 | —                | — |   | — | — |
| /home            | Teleports player to the worldspawn                                      | Java Edition Alpha v1.2.5       | Superseded by`/kill`                                          | 0                 | —                | — | — | — | — |
| `/locatebiome`   | Locates biomes                                                          | Java Edition 1.19(22w19a)       | Superseded by`/locate`                                        | 2                 | —                | — | — | — | — |
| `/placefeature`  | Used to place a configured feature at a given location                  | Java Edition 1.19(22w18a)       | Superseded by`/place`                                         | 2                 | —                |   | — | — |   |
| /replaceitem     | Replaces items in inventories                                           | Java Edition 1.17<br/>(20w46a)  | Superseded by`/item`                                          | 2                 | —                |   |   |   | — |
| /setspawn        | Sets the current location as the default spawn location for new players | Java Edition Indev 0.31         | Superseded by`/setworldspawn`                                 | 2                 | —                | — | — | — | — |
| /solid           | Toggles between placing stone or bedrock                                | Java Edition Indev 0.31         | Bedrockwas added to the Creative inventory as a separate item | 2                 | —                | — | — | — | — |
| /stats           | Update objectives from command results                                  | Java Edition 1.13<br/>(17w45a)  | Merged with`/execute`                                         | 2                 | —                |   |   |   | — |
| `/testfor`       | Counts entities matching specified conditions.                          | Java Edition 1.13<br/>(17w45a)  | Merged with`/execute`                                         | 2                 | —                | — |   |   | — |
| `/testforblock`  | Tests whether a block is in a location.                                 | Java Edition 1.13<br/>(17w45a)  | Merged with`/execute`                                         | 2                 | —                |   | — | — | — |
| `/testforblocks` | Tests whether the blocks in two regions match.                          | Java Edition 1.13<br/>(17w45a)  | Merged with`/execute`                                         | 2                 | —                |   | — | — | — |
| /toggledownfall  | Toggles the weather                                                     | Java Edition 1.13<br/>(17w45a)  | Redundancy with`/weather`                                     | 2                 | —                | — | — | — |   |
| /unban           | Pardons a banned player                                                 | Java Edition Alpha v1.0.16      | Superseded by`/pardon`                                        | 3                 | Yes              | — | — |   | — |

#### Removed from Bedrock Edition or Education
| Command              | Description                                                        | Version removed                            | Reason for deletion      | BE      | edu     | OP level required | Server only |   |   |   |   |
|----------------------|--------------------------------------------------------------------|--------------------------------------------|--------------------------|---------|---------|-------------------|-------------|---|---|---|---|
| /clearfixedinv       | Clears fixed inventory slots                                       | Pocket Edition v0.16.0 alpha<br/>(build 2) | ?                        | Removed | Removed | 2                 | ?           | — | — |   | — |
| /detect              | Execute a command when condition is met                            | Bedrock Edition 1.2.0                      | Superseded by`/execute`  | Removed | —       | 1                 | —           | — | — | — | — |
| /executeasself       | Execute a command                                                  | ?                                          | ?                        | Removed | Removed | 0                 | —           | — | — | — | — |
| `/mixer`             | Mixer interactivity control                                        | Bedrock Edition 1.16.210                   | Mixer was discontinued   | Removed | —       | 0                 | —           | — | — | — | — |
| `/position`          | Toggles player coordinates to be displayed on the HUD              | Education Edition 1.0.21                   | Superseded by`/gamerule` | —       | Removed | 0                 | —           | — | — | — | — |
| /resupply            | Update thevillagers' supply for economic trade                     | ?                                          | ?                        | Removed | —       | 2                 | —           | — |   | — | — |
| /setfixedinvslot     | Sets fixed inventory slot with a specific item                     | Pocket Edition v0.16.0 alpha<br/>(build 2) | ?                        | Removed | Removed | 2                 | —           | — | — |   | — |
| /setfixedinvslots    | Sets the amount of fixed inventory slots                           | Pocket Edition v0.16.0 alpha<br/>(build 2) | ?                        | Removed | Removed | 2                 | —           | — | — |   | — |
| `/transferserver`    | Transfer player to a server                                        | Bedrock Edition 1.2.3                      | ?                        | Removed | Removed | —                 | —           | — | — | — | — |
| `/videostream`       | Attempts to connect to the websocket server to send a video stream | ?                                          | ?                        | Removed | —       | 1                 | —           | — | - | — | — |
| `/videostreamaction` | Attempts to run a action on video stream                           | ?                                          | ?                        | Removed | —       | 1                 | —           | — | - | — | — |

#### Other removed commands
##### Developer commands
Main article: Developer commands

  

This feature is exclusive to  Bedrock Edition. 


Developer commands are only enabled in internal development builds of Bedrock Edition, and are not normally accessible in release versions.

##### Agent commands

  

This section describes an education-related feature. 
This feature is available only in Minecraft Education or when enabling the "Education" option in Bedrock Edition.


Superseded by /agent

- /move
- /turn
- /attack
- /destroy
- /drop
- /dropall
- /inspect
- /inspectdata
- /detect
- /detectredstone
- /transfer
- /createagent
- /tpagent
- /collect
- /till
- /place
- /getitemcount
- /getitemspace
- /getitemdetail

### Joke commands

  

This feature is exclusive to  Java Edition. 


These commands only exist in April Fools' Day joke versions of the game.

- /debugdim
- /transform
- /vote
- /warp

