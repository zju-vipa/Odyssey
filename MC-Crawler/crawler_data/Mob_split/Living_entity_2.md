## Motion of entities
"Gravity" redirects here.  For the Minecraft Dungeons enchantment, see MCD:Gravity.
Gravity works differently in Minecraft than the real world, as not everything is subject to the same acceleration. Additionally, there is a drag force proportional to velocity, again dependent on the entity.

This is a GitHub repository with some in-depth explanation about the topic.

| Kind                                                                         | Acceleration | Drag (vertical) | Drag (horizontal) | Terminal velocitym/tick | Terminal velocitym/s | Applies drag: |
|------------------------------------------------------------------------------|--------------|-----------------|-------------------|-------------------------|----------------------|---------------|
| Players and other living entities[note 2][note 3]                            | 0.08         | ~0.02           | ~0.09             | 3.92                    | 78.4                 | After         |
| Players/mobs withSlow Falling[note 2]                                        | 0.01         | ~0.02           | ~0.09             | 0.49                    | 9.8                  | After         |
| Items,falling blocks, andTNT[note 4]                                         | 0.04         | 0.02            | 0.02              | 1.96                    | 39.2                 | After         |
| Minecarts[note 5][note 4]                                                    | 0.04         | 0.05            | 0.05              | 0.76                    | 16.0                 | After         |
| Boatsandboat with chests[note 6][note 4]                                     | ~0.04        | 0.00            | ~0.10             | ∞                       | ∞                    | -             |
| Throwneggs,snowballs, andender pearls                                        | ~0.03        | ~0.01           | ~0.01             | 3.00                    | 60.0                 | Before        |
| Thrownpotions                                                                | ~0.05        | ~0.01           | ~0.01             | 5.00                    | 100.0                | Before        |
| Thrownbottles o' enchanting                                                  | ~0.07        | ~0.01           | ~0.01             | 7.00                    | 140.0                | Before        |
| Experience orbs[note 4]                                                      | 0.03         | 0.02            | ~0.02             | 1.47                    | 29.4                 | After         |
| Thrownfishing bobbers[note 4]                                                | 0.03         | 0.08            | 0.08              | 0.345                   | 6.9                  | After         |
| Llama spit                                                                   | ~0.06        | ~0.01           | ~0.01             | 6.00                    | 120.0                | Before        |
| Firedarrows, and throwntridents                                              | ~0.05        | ~0.01           | ~0.01             | 5.00                    | 100.0                | Before        |
| Fireballs,small fireballs,wither skulls, anddragon fireballs[note 2][note 7] | 0.10         | ~0.05[note 8]   | ~0.05             | 1.90                    | 38.0                 | After         |
| Wind charges‌[upcoming: JE 1.21 & BE 1.21.0][note 7]                         | 0.10         | 0.00            | 0.00              | ∞                       | ∞                    | -             |

Applying an initial upward velocity initialVelocity on an entity, the entity's vertical velocity after falling for a number of ticks ticksPassed can be given by the formulas:

Drag applied before acceleration:
finalVelocity=(initialVelocity×(1−drag)ticksPassed)−(acceleration×1−(1−drag)ticksPasseddrag)
Drag applied after acceleration[note 2]:
finalVelocity=(initialVelocity×(1−drag)ticksPassed)−(acceleration×1−(1−drag)ticksPasseddrag×(1−drag))

↑ a b In Bedrock Edition, these entities are under the mob category.

↑ a b c d Note that when living entities and explosive projectiles are simulated, the drag is applied after the acceleration, rather than before; this is why their terminal velocities aren't whole numbers while the others are.

↑ Players, mobs and armor stands whose OnGround property is set to 1 have an horizontal drag force of ~0.454.

↑ a b c d e In each tick, items, falling blocks, primed TNTs, minecarts, boats, experience orbs and fishing bobbers apply acceleration together with velocity to update the position. This means that the new position is calculated by subtracting the acceleration from the current velocity.

↑ Minecarts have a maximum horizontal velocity of 0.4. Any greater value is reset to that number.

↑ Boats' horizontal position gets updated using next tick's velocity instead of the current one.

↑ a b Explosive projectiles and wind charges are not affected by gravity but instead get acceleration from getting damaged.

↑ Dangerous wither skulls have drag force of ~0.27.


## Data values
Java Edition:

Main article: Entity format

: Root tag.
Tags common to all entities

Bedrock Edition:

See Bedrock Edition level format/Entity format.

## See also
- Block entity– unlike the entities mentioned above, these are simply blocks that store additional data.


