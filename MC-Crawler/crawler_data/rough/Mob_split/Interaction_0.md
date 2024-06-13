# Interaction
Interaction entities are entities useful for map or data pack creators to see who the last player to click on a certain spot is. They can only be created with the /summon or /execute summon command.
Interaction entities are invisible and of a custom size. Their boundary box can be viewed via the F3 + B debug shortcut.

## Contents
- 1 Behavior
- 2 Usage
	- 2.1 Advancement triggers
	- 2.2 /execute on with Interactions
- 3 Data values
	- 3.1 ID
	- 3.2 Entity data
- 4 History

## Behavior
Interaction entities record the UUID of the last player that left-clicked and right-clicked them, and the time at which the interaction happened. If response is set to true, left-clicking an interaction entity plays a punching sound, and right-clicking it makes the player's arm swing.

## Usage
You can check information on who last left-clicked and right-clicked on the interaction entity with the /data get entity command. This information can be useful in datapack and map creation. You can also change their size to match the area you want to be checked.

### Advancement triggers
- Interacting with (right-clicking) an Interaction entity triggersplayer_interacted_with_entity.
- Attacking (left-clicking) an Interaction entity triggersplayer_hurt_entity.

### 
The Interaction entity targets the player who last interacted with it. That makes the following possible:

- /execute on attackerexecute as the last player who attacked (left-clicked) the entity.
- /execute on targetexecute as the last player who interacted with (right-clicked) the entity.

## Data values
### ID
| Entity      | Identifier    | Translation key                |
|-------------|---------------|--------------------------------|
| Interaction | `interaction` | `entity.minecraft.interaction` |

### Entity data
See also: Entity format

Interaction entities have entity data associated with them that contain various properties of the entity.

- root tag
	- 
	- Tags common to all entities
	- width: The width of the entity's bounding box. Defaults to 1.
	- height: The height of the entity's bounding box. Defaults to 1.
	- response: 1 or 0 (true/false). Specifies whether an interaction should trigger a response. Defaults to 0 (false).
	- attack: The last attack (left click) to hit the entity.
		- player: The UUID of the player that attacked the entity. The 128-bit UUID is stored as four 32-bit integers, ordered from most to least significant.
		- timestamp: When the attack took place.
	- interaction: The last interaction (right click) to hit the entity.
		- player: The UUID of the player that interacted with the entity. The 128-bit UUID is stored as four 32-bit integers, ordered from most to least significant.
		- timestamp: When the interaction took place.




