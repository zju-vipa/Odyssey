# Glowing
Glowing is a status effect that shows entity positions through blocks.

## Contents
- 1 Effect
- 2 Causes
- 3 Immune mobs
- 4 Advancements
- 5 Data values
	- 5.1 ID
- 6 History
- 7 Issues
- 8 Gallery
- 9 References

## Effect
The glowing effect added to entities by command
 The Glowing effect causes entities to glow with an outline that can be seen through blocks and entities. This outline is white by default, but can be set to display other colors if the entity is part of a team. The outline displays around any holes in a mob's texture or model, though only when that part of the model can be seen all the way through. If multiple entities with glowing are near each other, the outlines merge to prevent overlapping/Z-Fighting.

This does not affect mob models as seen in the inventory, of either the player or ridden mobs.[1]

## Causes
| Cause          | Potency | Length | Notes                                                                                  |
|----------------|---------|--------|----------------------------------------------------------------------------------------|
| Spectral Arrow | I       | 0:10   | When shot by it.                                                                       |
| Bell           | I       | 0:03   | Hitting a bell applies the effect to anyillagersorwitcheswithin 32 blocks of the bell. |

## Immune mobs
Withers, ender dragons, dropped items and display entities are unaffected by Glowing.

## Data values
### ID
| Name    | Identifier | Numeric ID | Translation key            |
|---------|------------|------------|----------------------------|
| Glowing | `glowing`  | `24`       | `effect.minecraft.glowing` |

