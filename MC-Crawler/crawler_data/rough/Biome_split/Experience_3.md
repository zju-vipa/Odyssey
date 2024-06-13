## Score
Example of the score in Hardcore mode.
The score is the number of experience the player has collected since their last death. This number is the total experience the player has collected, rather than the amount of experience they had upon death. When the player dies, the score is displayed on the death screen.

## Data values
### ID
Java Edition:

| Name           | Identifier       | Translation key                   |
|----------------|------------------|-----------------------------------|
| Experience Orb | `experience_orb` | `entity.minecraft.experience_orb` |

Bedrock Edition:

| Name           | Identifier | Numeric ID | Translation key      |
|----------------|------------|------------|----------------------|
| Experience Orb | `xp_orb`   | `69`       | `entity.xp_orb.name` |

### Entity data
Experience orbs have entity data associated with them that contain various properties.

Java Edition:

Main article: Entity format
- Entity data
	- 
	- Tags common to all entities
	- Age: The number of ticks the XP orb has been "untouched". After 6000 ticks (5 minutes) the orb is destroyed.
	- Count: The remaining number of times that the orb can be picked up. When the orb is picked up, the value decreases by 1. When multiple orbs are merged, their values are added up to result orb. When the value reaches 0, the orb is depleted.
	- Health: The health of XP orbs. XP orbs take damage from fire, lava, falling anvils, and explosions. The orb is destroyed when its health reaches 0.
	- Value: The amount of experience the orb gives when picked up.

Bedrock Edition:

SeeBedrock Edition level format/Entity format.

