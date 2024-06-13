# Darkness
Darkness is a status effect that causes the player's vision to temporarily deteriorate. The effect is caused by the activation of a sculk shrieker, or by being within detection range of a warden.

## Contents
- 1 Effect
- 2 Causes
- 3 Data values
	- 3.1 ID
- 4 Immune mobs
- 5 Advancements
- 6 History
- 7 Issues
- 8 References
- 9 See also

## Effect
Darkness, when applied, dims the player's vision. A dark vignette appears around the player, which initially makes faraway objects hard to see. The vignette then steadily closes in around the player, diminishing the player's eyesight. The player can only see about 14 blocks away. When the effect wears off, the vignette retreats and the player's vision reverts to normal. Unlike Blindness, Darkness does not leave a circle of unaffected vision centered on the player; moreover, luminous objects such as fire can still be seen even when viewed from far away by a player with the effect applied.  

With the Darkness effect, the player's vision slowly cycles every few seconds between complete darkness, and relative visibility where they can see within a distance of roughly 14 blocks. The strength of this pulsing effect can be adjusted using the "Darkness Pulsing"‌[JE  only]/"Darkness effect strength"‌[BE  only] slider under the accessibility settings, which is normally at 100%; when set to 0%, the player's vicinity does not darken at all, but their vision is still restricted to about 14 blocks.

Unlike other status effects, Darkness does not cause particles to appear around the player when it is naturally activated, nor does its icon appear in the player's heads-up display in Java Edition.[1] This is similar to when an effect is given using the /effect command with the hideParticles argument set to true. However, the particles do appear when hideParticles is set to false, and the effect's icon can be seen when entering the player's inventory.

## Causes
| Cause                               | Potency | Length | Notes                                        |
|-------------------------------------|---------|--------|----------------------------------------------|
| Sculk Shrieker(naturally generated) | I       | 0:13   | When activated, to players within 40 blocks  |
| Warden                              | I       | 0:13   | Every 6 seconds, to players within 20 blocks |

## Data values
### ID
Java Edition:

| Name     | Identifier | Numeric ID | Translation key             |
|----------|------------|------------|-----------------------------|
| Darkness | `darkness` | `33`       | `effect.minecraft.darkness` |

Bedrock Edition:

| Name     | Identifier | Numeric ID | Translation key   |
|----------|------------|------------|-------------------|
| Darkness | `darkness` | `30`       | `effect.darkness` |

## Immune mobs
Boss mobs and wardens are immune to this effect. However, it does not affect mob behavior.


