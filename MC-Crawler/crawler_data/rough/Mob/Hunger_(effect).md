# Hunger (effect)
Hunger is a status effect which causes the hunger bar to deplete faster than normal.

## Contents
- 1 Effect
- 2 Causes
- 3 Immune mobs
- 4 Advancements
- 5 Data values
	- 5.1 ID
- 6 History
- 7 Issues

## Effect
Hunger increases food exhaustion by 0.005 × level per game tick (removes 1 () saturation point every (40 ÷ level) seconds). It also turns the hunger bar a yellow-green color(). Negative levels decrease food exhaustion, although they do not increase saturation or the hunger bar.

The status effect does not decrease hunger level on Peaceful, although it does re-color the hunger bar.

An example of how eating rotten flesh can cause the hunger status effect.
Hunger inflicted by eating rotten flesh, raw chicken or by being attacked by a husk adds 3.0 to the player's exhaustion level over the course of 30 seconds, draining 3/4 of a saturation point. When a pufferfish is eaten, 4.5 exhaustion points are added over the course of 15 seconds, draining 1 () and 1⁄8 (0.125) saturation points.

## Causes
| Cause        | Potency | Length                           | Notes                                                                  |
|--------------|---------|----------------------------------|------------------------------------------------------------------------|
| Husk         | I       | (7 xregional difficulty) seconds | Attack                                                                 |
| Pufferfish   | III     | 0:15                             | Does not apply toWolveswhen fed pufferfish‌[Bedrock Edition  only].    |
| Rotten Flesh | I       | 0:30                             | 80% chance of receiving. Does not apply toWolveswhen fed rotten flesh. |
| Raw Chicken  | I       | 0:30                             | 30% chance of receiving. Does not apply toWolveswhen fed raw chicken.  |

## Immune mobs
Only withers and ender dragons are immune. Only players are affected, as all other mobs do not have hunger.

## Data values
### ID
Java Edition:

| Name   | Identifier | Numeric ID | Translation key           |
|--------|------------|------------|---------------------------|
| Hunger | `hunger`   | `17`       | `effect.minecraft.hunger` |

Bedrock Edition:

| Name   | Identifier | Numeric ID | Translation key |
|--------|------------|------------|-----------------|
| Hunger | `hunger`   | `17`       | `potion.hunger` |

