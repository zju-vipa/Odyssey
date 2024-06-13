# Scoreboard
The scoreboard system is a complex gameplay mechanic utilized through commands. Mainly intended for mapmakers and server operators, scoreboards are used to track, set, and list the scores of entities in a myriad of different ways.

## Contents
- 1 Objectives
	- 1.1 Criteria
		- 1.1.1 Java Edition
			- 1.1.1.1 Single criteria
			- 1.1.1.2 Compound criteria
		- 1.1.2 Bedrock Edition
- 2 Display slots
- 3 Tags
- 4 Teams
- 5 Command reference
	- 5.1 Objectives commands
	- 5.2 Players commands
	- 5.3 Tags commands
	- 5.4 Teams commands
- 6 NBT format
- 7 History
- 8 Issues
- 9 Gallery
	- 9.1 Screenshots
- 10 References

## Objectives
Entities can hold scores in the scoreboard specified by objective. Objective tracks a number of points for entities while meeting a single criteria. Objective scores are stored as 32-bit integer with the range of -2,147,483,648 and 2,147,483,647.

Objective has two main property: a name and a criteria. The objective's name is used internally for referencing in commands, target arguments, and the file format. And the criteria determines its behavior — primarily what to track.

InJava Edition, the objective's name allowed character set for it includes all lowercase and uppercase letters, numbers, underscore, period, minus and plus. InBedrock Edition, it can contain any character.
The entity's score in any objective can be changed from commands, and unless it's read-only and automatically set by the game (see Criteria). It can be increased by, decreased by, or set to a given amount with commands. Non-player entities support only dummy criteria in the scoreboard; their scores can be changed only by commands and not automatically by the game. Unlike players, when a non-player entity dies, its scores are deleted.

The score holder's name can either be the player's name or the entity's UUID. For players, the score holder's name doesn’t need to belong to an actual player.

Objective also has other properties to customize its appearance and behavior:

| Property          | Description                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| displayname       | Specify the objective's display name that appears in the player list, above the player head, and the sidebar. By default, the objective's name is the display name.                                                                                                                                                                                                                                                              |
| numberformat      | Specify the objective's number format for the score. The number format can be blank, fixed, and styled.Blank number format displays nothing on the scoreboard. Fixed number format displays the contents specified in the command.Styled number format displays the score number with the styling applied from the raw JSON text format, such as "color", "italic", "bold", and etc. This means "text" JSON property is ignored. |
| rendertype        | Specify the objective's render type for the score. Score can be rendered by integers or hearts.When the score is greater than 44, the hearts displayed turn into "<integer>hp" in the player list (not in the sidebar, instead, only integers are shown), and the <integer> is divided by 2.                                                                                                                                     |
| displayautoupdate | Set whether or not display auto updates when the score has changed. Value is boolean: true (default) or false.                                                                                                                                                                                                                                                                                                                   |

The number format property and the score holder's name can be changed per-entity using /scoreboard players display numberformat|name <target> ....

Server operators can select entities by their scores using target selector with the "scores" argument (syntax @e[scores={<name>=<min>..<max>}]. This argument uses "<name>" to specify the score name of the objective.

For example, inputting/execute if entity @a[scores={deaths=1..}]into acommand blocktriggers acomparatororconditional command blockif any player has died at least once, assuming the "deaths" score is an objective of the "deathCount" criteria.
### Criteria
#### Java Edition
##### Single criteria
These criteria's names consist of a single alphabetical string.


Criteria name

Description

Can be modified


dummy

Score that can be changed only by commands, and not automatically by the game. This can be used for storing integer states and variables, which then can be used with the scoreboard's operations to do arithmetic calculation.

Yes


trigger

Score that can be changed by commands, and not automatically by the game. The /trigger command can be used by players to set or increment and decrement their own score. The command fails if the objective has not been "enabled" for the player using it. If the player uses it, the objective is automatically disabled for them afterward. By default, all trigger objectives are disabled for any players. Ordinary players can use the /trigger command, even if cheats are disabled or if they are not server operators, in which case this is useful for safely taking non-operator player input.

Yes


deathCount

Score increments automatically for a player when they die.

Yes


playerKillCount

Score increments automatically for a player when they kill another player.

Yes


totalKillCount

Score increments automatically for a player when they kill another player or a mob.

Yes


health

Ranges from 0 to 20 on a normal player; represents the amount of half-hearts the player has. May appear as 0 for players before their health has changed for the first time. Extra hearts and absorption hearts also count to the health score, meaning that with Attributes/Modifiers or the Health Boost or Absorption status effects, health can far surpass 20.

No


xp

Matches the total amount of experience the player has collected since their last death (or in other words, their score).

No


level

Matches the current experience level of the player.

No


food

Ranges from 0 to 20; represents the amount of hunger points the player has. May appear as 0 for players before their foodLevel has changed for the first time.

No


air

Ranges from 0 to 300; represents the amount of air the player has left from swimming under water, matches the air nbt tag of the player.

No


armor

Ranges from 0 to 20; represents the amount of armor points the player has. May appear as 0 for players before their armor has changed for the first time.

No

