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

