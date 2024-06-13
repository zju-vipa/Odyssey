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

