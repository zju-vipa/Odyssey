### Warped Forest ambience
| Name                              | Sound | Group          |
|-----------------------------------|-------|----------------|
| Warped Forest Ambience            |       | Loop           |
| Warped Forest Addition 1          |       | Loop Additions |
| Warped Forest Addition 2          |       |                |
| Warped Forest Addition 3          |       |                |
| Warped Forest Addition 4          |       |                |
| Warped Forest Addition 5          |       |                |
| Warped Forest Addition 6          |       |                |
| Warped Forest Enish 1             |       |                |
| Warped Forest Enish 2             |       |                |
| Warped Forest Enish 3             |       |                |
| Warped Forest Help 1              |       |                |
| Warped Forest Help 2              |       |                |
| Warped Forest Here 1              |       |                |
| Warped Forest Here 2              |       |                |
| Warped Forest Here 3              |       |                |
| Warped Forest Mood 1              |       | Mood           |
| Warped Forest Mood 2              |       |                |
| Warped Forest Mood 3              |       |                |
| Warped Forest Mood 4              |       |                |
| Warped Forest Mood 5              |       |                |
| Warped Forest Mood 6              |       |                |
| Warped Forest Mood 7              |       |                |
| Warped Forest Mood 8<br/>(Unused) |       |                |
| Warped Forest Mood 9<br/>(Unused) |       |                |
| Warped Forest Creak 1             |       |                |
| Warped Forest Creak 2             |       |                |
| Warped Forest Creak 3             |       |                |
| Warped Forest Creak 4             |       |                |
| Warped Forest Creak 5             |       |                |

## Mood algorithm
Mood ambience sounds occur based on a "mood" percent value between 0–100. The mood increases when the player is in a cave or in a dark place, and decreases otherwise. When the mood reaches 100%, one of the sounds plays randomly, resetting the mood to 0% and thus restarting the cycle. The darker it is, and the more non-transparent blocks there are, the quicker the mood increases. in Java Edition, the current mood value appears on the debug screen.

This is the simplified algorithm for computing this value in pseudocode:

updateMood(mood):
    tickDelay = 6000
    maxLightLevel = 15
    block = select a random block in a 17×17×17 block cube centered around the player
    skyLight = block.getSkyLightLevel()

    if (skyLight > 0):
        mood = mood - (skyLight / maxLightLevel) * 0.015
    else:
        blockLight = block.getBlockLightLevel()
        mood = mood - (blockLight - 1) / tickDelay
    
    if (mood ≥ 1.0):
        player.playSpookySound()
        mood = 0.0
    else if (mood < 0):
        mood = 0.0

This method is called once every tick. It selects a random block in a 17×17×17 area centered around the player's eye position, and alters the mood value accordingly:

- If the selected block has sky light, it decreases the mood by1⁄1000per sky light level.
- If it has a block light level above 1, it decreases the mood value by(block light level - 1)⁄6000.
- If the block light level is 0, it increases the mood value by1⁄6000.

This means that a player in complete darkness hears an ambient noise every 6000 ticks (5 minutes).

Because non-transparent blocks are considered to have a sky and block light level of 0, the mood value increases especially fast inside a cave.


