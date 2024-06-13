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

##### Compound criteria
Compound criteria's names are divided into parts, delimited with periods (.). For example,minecraft.killed_by:minecraft.zombieis a valid compound criteria, under which player scores would increment whenever they're killed by zombie.
All objectives based on compound criteria is writable and can be modified with commands.
Allstatisticscan be used as a compound criteria whose name is itsidentifier. Player statistics are stored separately from the scoreboard, and as they update, scores in these objectives are updated in parallel.
In addition, there are some other compound criteria:
| Accepted ID Names                                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| "black", "dark_blue", "dark_green", "dark_aqua", "dark_red", "dark_purple", "gold", "gray", "dark_gray", "blue", "green", "aqua", "red", "light_purple", "yellow", "white" |

| Accepted ID Names                                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| "black", "dark_blue", "dark_green", "dark_aqua", "dark_red", "dark_purple", "gold", "gray", "dark_gray", "blue", "green", "aqua", "red", "light_purple", "yellow", "white" |

#### Bedrock Edition
Currently, "dummy" is the only criteria supported. As such, score can be changed only by commands.

## Display slots
An objective with two points to the player is displayed in the "list" slot, while an objective with the display name "Quest Points" with 0 points to the player is displayed in the "sidebar" slot.
Via the /scoreboard objectives setdisplay command (see command reference), players' scores in specific objectives can be displayed in certain 'slots' in-game. Each 'display slot' can show one objective at a time, and multiple 'display slots' may be used for the same or different objectives.

| Slot                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|--------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| list                                       | Displays a yellow number or some hearts (`/scoreboard objectives modify <objective> rendertype (hearts|integer)`) without a heading on the tab menu, where online players are shown.‌[Java Edition  only]Displays a white number without a heading on the Pause Menu, where online players are shown.‌[Bedrock Edition  only]Visible even in singleplayer.                                                                                               |
| sidebar                                    | Shows on the right hand side of the screen. Shows up to 15 entities with the highest score of that objective with a heading labeled with the objective's <DisplayName>. Note that players are shown even if offline, and untracked players are not shown. In addition, fake players with names starting with a # do not show up in the sidebar under any circumstances.                                                                                  |
| sidebar.team.<color> ‌[Java Edition  only] | There are 16 team-specific sidebar display slots. These operate the same as the standard sidebar slot, but display only to players who are on teams that use the specified color (for example, "sidebar.team.green" displays to players on "green" teams). Valid colors are: "black", "dark_blue", "dark_green", "dark_aqua", "dark_red", "dark_purple", "gold", "gray", "dark_gray", "blue", "green", "aqua", "red", "light_purple", "yellow", "white". |
| below_name                                 | Shows the <Score> followed by the objective's <DisplayName> below the player's nametag above their head. This is hidden beyond ~10 blocks and when the player issneaking. Not visible in singleplayer.                                                                                                                                                                                                                                                   |

## Tags
Main article: Commands/tag
Tags are a simple list of single-word strings stored directly in the  Tags data tag of an entity. As with objectives, tags are case-sensitive.

Target selectors can be used to check whether an entity has a tag with the "tag" argument.

## Teams
"team" redirects here.  For the command, see Commands/team.

  

This feature is exclusive to  Java Edition. 


Team is a list of entities that can be used by mapmakers or server operators to group entities or players together as an ally.

Entity can have only one team; team cannot share with other different team member. If a player is teamed with a hostile entity, that entity does not attack the player. This unique behavior is also apparent with a neutral entity who would normally attack hostile entities, like the Iron Golem.

Team has a name property, used internally for reference in commands, target arguments, and the file format. It is a single, case-sensitive text. Team also has other several properties to customize its appearance and behavior:

| Property               | Description                                                                                                                                                                                                                                                                                          | Value                                                                                                                                                                      |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| displayName            | Specify team's display name that appears on the player name in chat, nametag, player list menu, and on the scoreboard sidebar.                                                                                                                                                                       | Raw JSON text format                                                                                                                                                       |
| color                  | Specify team's color that appears on the player name in chat, nametag, player list menu, and on the scoreboard sidebar. It also changes the color of the entities outline caused by theGlowingeffect.                                                                                                | "black", "dark_blue", "dark_green", "dark_aqua", "dark_red", "dark_purple", "gold", "gray", "dark_gray", "blue", "green", "aqua", "red", "light_purple", "yellow", "white" |
| collisionRule          | Control the way member collides with other teams, or entities.                                                                                                                                                                                                                                       | "always" (default), "never", "pushOtherTeams", "pushOwnTeam"                                                                                                               |
| deathMessageVisibility | Hide or show memberdeath message.                                                                                                                                                                                                                                                                    | "always" (default), "never", "hideForOtherTeams", "hideForOwnTeam"                                                                                                         |
| nametagVisibility      | Hide or show member's nametag from other teams, or everyone. Member's nametag appears above the player head.                                                                                                                                                                                         | "always" (default), "never", "hideForOtherTeams", "hideForOwnTeam"                                                                                                         |
| friendlyFire           | Allow whether or not member can attack other member on the same team. The attack damage can be from melee attack, bow and arrow,splash potionof harming, and more. Note that team members may still inflict negative status effects on each other with potions, like with a splash potion of poison. | "true" (default) or "false"                                                                                                                                                |
| seeFriendlyInvisibles  | Allow whether or not member can see other own team member withInvisibilityeffect.                                                                                                                                                                                                                    | "true" (default) or "false"                                                                                                                                                |
| prefix                 | Specify team's prefix that appears before the member's name in the chat, nametag, and the player list menu.                                                                                                                                                                                          | A quoted string.                                                                                                                                                           |
| suffix                 | Specify team's suffix that appears after the member's name in the chat, nametag, and the player list menu.                                                                                                                                                                                           | A quoted string.                                                                                                                                                           |

Commands can be used to check whether team members exist by using target selection with the "team" argument. (The '!' character may be placed before a name to check for entities not on a team.) For example, inputting /execute if entity @a[team=red] into a command block provides comparator output if any player exists on the red team. Conversely, /execute if entity @a[team=!red] provides output when there are any players not on the red team. /execute if entity @a[team=!] allows output when at least one player is on any team, and /execute if entity @a[team=] allows output when at least one player is on no team.

## Command reference
Main article: Commands/scoreboard
### Objectives commands
| Commands                                                                                                                                                                                                                                                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                      |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| scoreboard objectives list                                                                                                                                                                                                                                                                 | List all existing objectives with their display names and criteria.                                                                                                                                                                                                                                                                                                                              |
| scoreboard objectives add<objective> <criteria> [<displayName>]‌[Java Edition  only]<br/>scoreboard objectives add<objective: string> dummy [displayName: string]‌[Bedrock Edition  only]                                                                                                  | Create a new objective with the given internal objective name, specified criterion, and the optional display name. InBedrock Edition, "dummy" is the only criterion currently supported.`<displayName>`defaults to`<objective>`when unspecified. Seeabove sectionfor more on these arguments.                                                                                                    |
| scoreboard objectives remove<objective>‌[Java Edition  only]<br/>scoreboard objectives remove<objective: string>‌[Bedrock Edition  only]                                                                                                                                                   | Delete all references to the named objective in the scoreboard system. Data is deleted from the objectives list and score holders' scores, and if it was on a display list it is no longer displayed.                                                                                                                                                                                            |
| scoreboard objectives setdisplay<slot > [<objective ]‌[Java Edition  only]<br/>scoreboard objectives setdisplay<list|sidebar> [objective: string] [ascending|descending]‌[Bedrock Edition  only]<br/>scoreboard objectives setdisplaybelowname [objective: string]‌[Bedrock Edition  only] | Display score info for the objective in the given slot. Valid slots are listed and described inDisplay Slots. InBedrock Edition, if slot is`list`or`sidebar`, there is an additional optional argument`ascending|descending`to specify the sort order. Note that the objective parameter is optional; if no objective is provided, this display slot is cleared (returned to its default state). |
| scoreboard objectives modify<objective>displayname<displayName> ‌[Java Edition  only]                                                                                                                                                                                                      | Change the display name of the scoreboard in display slots.                                                                                                                                                                                                                                                                                                                                      |
| scoreboard objectives modify<objective>rendertype(hearts|integer) ‌[Java Edition  only]                                                                                                                                                                                                    | Change the display format of the player list.                                                                                                                                                                                                                                                                                                                                                    |

### Players commands
| Commands                                                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| scoreboard players list[<target>]‌[Java Edition  only]<br/>scoreboard players list[playername: target]‌[Bedrock Edition  only]                                                                                                                                                      | Lists all score holders that are tracked in some way by the scoreboard system. The optional`<target>`or`playername: target`parameter is used to list the scores of particular score holders.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| scoreboard players get<target> <objective> ‌[Java Edition  only]                                                                                                                                                                                                                    | Return the scoreboard value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| scoreboard players set<targets> <objective> <score>‌[Java Edition  only]<br/>scoreboard players set<player: targets> <objective: string> <count: int>‌[Bedrock Edition  only]                                                                                                       | Set the targets' scores of the given objective, overwriting any previous score.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| scoreboard players add<targets> <objective> <score>‌[Java Edition  only]<br/>scoreboard players add<player: targets> <objective: string> <count: int>‌[Bedrock Edition  only]                                                                                                       | Increments the targets' scores in that objective by the given amount.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| scoreboard players remove<targets> <objective> <score>‌[Java Edition  only]<br/>scoreboard players remove<player: targets> <objective: string> <count: int>‌[Bedrock Edition  only]                                                                                                 | Decrements the targets' scores in that objective by the given amount.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| scoreboard players random<player: target> <objective: string> <min: int> <max: int> ‌[Bedrock Edition  only]                                                                                                                                                                        | Sets the targets' scores in that objective to a random number between min and max, both inclusive.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| scoreboard players reset<targets> [<objective>]‌[Java Edition  only]<br/>scoreboard players reset<player: target> [objective: string]‌[Bedrock Edition  only]                                                                                                                       | Deletes score or all scores for the target. If`<objective>`is specified, then only that objective is cleared. Otherwise, this applies to all objectives. Note that this does not merely set the score(s) to 0: it removes the targets from the scoreboard altogether (or for the given objective).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| scoreboard players test<player: target> <objective: string> <min: wildcard int> [<max: wildcard int>] ‌[Bedrock Edition  only]                                                                                                                                                      | Tests if targets' scores are within`min: wildcard int`and`max: wildcard int`(Defaults to 2,147,483,647).`min: wildcard int`can be replaced with asterisk (*) to represent -2,147,483,648, and`max: wildcard int`can be replaced with asterisk (*) to represent 2,147,483,647.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| scoreboard players enable<targets> <objective> ‌[Java Edition  only]                                                                                                                                                                                                                | Enables the target player(s) to use the`/trigger`command on the specified objective. This command accepts non-player entities, but only players can actually use the`/trigger`command. Until this has been done, players that attempt to`/trigger`that objective fail. Using the`/trigger`command disables it again. Note that if the target(s) did not previously have a score for the specified objective, this command sets their score to 0.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| scoreboard players operation<targets> <targetObjective> <operation> <source> <sourceObjective>‌[Java Edition  only]<br/>scoreboard players operation<player: target> <targetObjective: string> <operation: operator> <selector: target> <objective: string>‌[Bedrock Edition  only] | Applies an arithmetic operation altering the targets' score(s) in the target objective, using sources' scores in the source objective as input.<operation> may be:"+=" Addition: Add source's score to that of target<br/>"-=" Subtraction: Subtract source's score from that of target<br/>"*=" Multiplication: Set target's score to the product of target's and source's scores<br/>"/=" (Integer) Division: Divide target's score by source's score, and use the result (rounded down) to set the target score.<br/>"%=" Modulus: Divide target's score by source's score, and use the remainder to set the target score<br/>"=" Assign: Set target's score to that of source<br/>"<" Min: Set target's score to source's score only if source has the lesser score.<br/>">" Max: Set target's score to source's score only if source has the greater score.<br/>"><" Swaps target's and source's scores<br/>In all cases except "><", source's score remains unchanged. If target or source isn't tracked by the specified objective, it is set to 0. If more than one score holder is specified as sources, performs the operation once with each source's score. If more than one target score holder is specified, performs the operation for each target one by one. |

### Tags commands
Main article: Commands/tag
### Teams commands

  

This feature is exclusive to  Java Edition. 


Main article: Commands/team
## NBT format

  

This feature is exclusive to  Java Edition. 


The file scoreboard.dat in the 'data' folder of a Minecraft world stores the scoreboard data for that world as a GZip'd NBT file:

- The root tag.
	- data: The scoreboard data.
		- Objectives: A list of compound tags representing objectives.
			- An objective.
				- CriteriaName: The criterion of this objective.
				- DisplayName: The display name of this objective in JSON. If none was specified during the objective's creation, this is set to{"text":"Value of Name"}.
				- Name: The internal name of this objective.
				- RenderType: The way the score is displayed. Can be "integer" or "hearts", but defaults to "integer".
				- display_auto_update: 1 or 0 (true/false) - Whether the display names in the sidebar automatically updates whenever the score values are changed.
				- format: Optional, the default number format for this objective.
					- type: One ofblank,fixed, orresult(calledstyledin the command).
					- Additional fields based on the type.
		- PlayerScores: A list of compound tags representing scores tracked by the scoreboard system.
			- A tracked player/objective pair with a score.
				- Score: The score this player has in this objective.
				- Name: The name of the player who has this score in this objective.
				- Objective: The internal name of the objective that this player has this score in.
				- Locked: 1 or 0 (true/false) - false if this objective is "enabled". Meaningful only for objectives with the criteria "trigger", where this must be false before a player can use the /trigger command on it.
				- display: Optional, the text component used as display name in the sidebar.
				- format: Optional, the number format of the player score.
					- type: One ofblank,fixed, orresult(calledstyledin the command).
					- Additional fields based on the type.
		- Teams: A list of compound tags representing teams.
			- A Team.
				- AllowFriendlyFire: 1 or 0 (true/false) - true if players on this team can harm each other.
				- SeeFriendlyInvisibles: 1 or 0 (true/false) - true if players on this team can see invisible teammates.
				- NameTagVisibility: The value of the nametagVisibility option of this team.
				- DeathMessageVisibility: The value of the deathMessageVisibility option of this team. Valid options are: never, hideForOtherTeams, hideForOwnTeam, always
				- CollisionRule: The value of the collisionrule option of this team. Valid options are: always, pushOwnTeam, never, pushOtherTeams
				- DisplayName: The display name of this team in JSON. If none was specified during the team's creation, this is set to{"text":"Value of Name"}.
				- Name: The internal name of this team.
				- MemberNamePrefix: The prefix prepended to names of players on this team. In JSON format.
				- MemberNameSuffix: The suffix appended to names of players on this team. In JSON format
				- TeamColor: The text-based color ("black", "dark_blue", etc.) given to the team. Does not exist if no color is set.
				- Players: A list of names of players on this team.
					- The name of a player on this team.
		- DisplaySlots: A set of slots that display specific objectives. If a slot is empty, its tag is not present.
			- slot_n: The internal name of the objective displayed (see below).

| No. | Type                        | Name                      |
|-----|-----------------------------|---------------------------|
| 0   | Player list                 | list                      |
| 1   | On the sidebar              | sidebar                   |
| 2   | Below the player's username | belowName                 |
| 3   | Team color                  | sidebar.team.black        |
| 4   |                             | sidebar.team.dark_blue    |
| 5   |                             | sidebar.team.dark_green   |
| 6   |                             | sidebar.team.dark_aqua    |
| 7   |                             | sidebar.team.dark_red     |
| 8   |                             | sidebar.team.dark_purple  |
| 9   |                             | sidebar.team.gold         |
| 10  |                             | sidebar.team.gray         |
| 11  |                             | sidebar.team.dark_gray    |
| 12  |                             | sidebar.team.blue         |
| 13  |                             | sidebar.team.green        |
| 14  |                             | sidebar.team.aqua         |
| 15  |                             | sidebar.team.red          |
| 16  |                             | sidebar.team.light_purple |
| 17  |                             | sidebar.team.yellow       |
| 18  |                             | sidebar.team.white        |

