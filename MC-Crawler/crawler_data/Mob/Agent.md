# Agent
The Agent is a interactive passive mob that is exclusive to Minecraft Education and Bedrock Edition.

## Contents
- 1 Usage
	- 1.1 Agent commands
- 2 Sounds
- 3 Data values
	- 3.1 ID
- 4 History
- 5 Issues
- 6 Trivia
- 7 Gallery
	- 7.1 Screenshots
	- 7.2 In other media
- 8 External links

## Usage
In Minecraft Education, the agent is used in conjunction with Code Connection for Minecraft / Code Builder, and is programmable by a visual programming language.

In Education and Bedrock Editions, the agent can be used in conjunction with WebSocket servers. 

The agent carries its own 27-item inventory, which can be manipulated by commands that the player programs it to use, or edited directly by a GUI that the player can access in-game, in any dimension.

The visual interface allows the player to drag and drop commands, structural constructs and other components into a sequence, and associate the sequence with a custom-named slash command, which can be executed in the traditional way, from the console.

The agent in a dripstone cave
The agent can push pressure plates. The agent also is invulnerable to attacks and is targeted by wardens, but the agent remains undamaged. Projectiles pass through them. Agents can also never ride minecarts or boats, and vehicles go through them. The player cannot use a lead on them.

The agent can interact with buttons, levers or other right-click mechanisms like doors and gates.  

### Agent commands
Main article: Commands/agent
- attack <direction>
- destroy <direction>
- drop <int:slotNum> <int:quantity> <direction>
- drop all <direction>
- move <direction>
- turn <turnDirection>
- inspect <direction>
- inspect data <direction>
- detect <direction>
- detectredstone <direction>
- transfer <int:srcSlotNum> <int:quantity> <int:dstSlotNum>
- create agent
- remove agent
- teleport to player
- teleport to location facing direction
- collect <string:item>
- till <direction>
- place <int:slotNum> <direction>
- place on move<int:slotNum> <true/false>
- get item count <int:slotNum>
- get item space <int:slotNum>
- get item detail <int:slotNum>

<direction> refers to forward|back|left|right|up|down

<turnDirection> refers to left|right

## Data values
### ID
| Name  | Identifier | Numeric ID | Translation key   |
|-------|------------|------------|-------------------|
| Agent | agent      | 56         | entity.agent.name |

