# Action bar
The action bar is the space just above the player's hotbar where text can be displayed. Some gameplay elements like beds use this to give contextual hints to the player. Text can also be displayed using the /title command.

## Contents
- 1 Gameplay uses
- 2 Commands
- 3 History
- 4 See also

## Gameplay uses
| Displayed text                                                               | Cause                                                                                                             |
|------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Now Playing: %s                                                              | When amusic discstarts playing nearby.                                                                            |
| Press %1$s to Dismount                                                       | When the player starts riding a vehicle.                                                                          |
| This bed is occupied                                                         | When another mob is already sleeping in thebed.                                                                   |
| You can sleep only at night or during thunderstorms                          | When a player tries to sleep during the day and without a thunderstorm.                                           |
| You may not rest now; the bed is too far away                                | When a player tries to sleep in a bed that is too far away.                                                       |
| This bed is obstructed                                                       | When a player tries to sleep in a bed that has suffocating blocks directly above.                                 |
| You may not rest now; there are monsters nearby                              | When a player tries to sleep in a bed while there are hostile mobs within a 17×11×17 box centered around the bed. |
| %s/%s players sleeping                                                       | When a player starts sleeping but not enough players are sleeping to skip the night. Announced to all players.    |
| Sleeping through this night                                                  | When enough players are sleeping to skip the night. Announced to all players.                                     |
| No amount of rest can pass this night                                        | When a player starts sleeping but the`playersSleepingPercentage`game ruleis set above 100.                        |
| %s is locked!                                                                | When a player attempts to open achestthat is locked.                                                              |
| Unable to open. Loot not generated yet.                                      | When a player inSpectatortries to open a chest with loot that hasn't been opened yet.                             |
| Item hotbar saved (restore with %1$s+%2$s)                                   | After saving a creative hotbar.                                                                                   |
| Social Interactions are only available in Multiplayer worlds                 | Attempting to open thesocial interactionsscreen in aSingleplayerworld.                                            |
| Chat disabled in client options.                                             | Attempting to open thechatwhen it is disabled in theoptions.                                                      |
| Chat disabled by launcher option. Cannot send message.                       | Attempting to open the chat when it is disabled from thelauncher.                                                 |
| Chat not allowed by account settings. Press '%s' again for more information. | Attempting to open the chat when it is disabled from the account.                                                 |
| Chat not allowed by account settings. Cannot send or view messages.          | After pressing the chat keybind to get more information.                                                          |

## Commands
Main article: Commands/title
A custom text message can be displayed on the action bar using the /title command:

- JE:title <targets> actionbar <title>
- BE:title <player: target> actionbar <titleText: message>

