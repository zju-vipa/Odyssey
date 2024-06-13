# Entity
Entities encompass all dynamic, moving objects throughout the Minecraft world.

## Contents
- 1 General behavior
	- 1.1 Further notes
		- 1.1.1 Boats, boat with chests and minecarts
		- 1.1.2 Gravity-affected blocks
		- 1.1.3 Interactions with "use" control
		- 1.1.4 Riding
- 2 Types of entities
- 3 Motion of entities
- 4 Data values
- 5 Video
- 6 History
- 7 Issues
- 8 See also
- 9 References

## General behavior
Properties all entities have are:

- A position, rotation, and velocity
- A volume consisting of one or more non-rotating, three-dimensionalboxeswith a fixed height and width
- Whether they are onfire, displayed as flames on or around the entity
- Whether they have anystatus effect, such as frompotions
- Aview point, even if it has no eyes

Most entities can be pushed around by water currents, and some can have their trajectory altered by explosions if already traveling at speed. Some entities can be renamed by using a name tag on them. Entity tiles, items, shot or thrown projectiles, area effect clouds, and experience orbs do not have health. Entities that do have a health status include mobs, players, armor stands, boats, boat with chests and minecarts.

Entities cannot pass through solid blocks, excluding vexes and ender dragons. Most types of entities prevent blocks from being placed in the space they occupy, except for dropped items and experience orbs, which are automatically pushed out of the block to open air. If a solid block enters an entity's space, such as falling sand or a swinging door, then it is free to move out of the solid block but not back in. For example, if a door is closed on the player, player can jump up and stand on top of the bottom-half door block, if there is air above the door.

Entities are lit according to the light level of the block their position is in. For example, if a minecart runs over a non-straight track directly into a solid block, it turns black because solid blocks always have a light level of 0; arrows are also sometimes seen to turn black, especially if fired shallowly into the ceiling.

### Further notes
Item frames, glow item frames, paintings, and lead knots, unlike most entities, align to the block grid, and are completely immobile.

Arrows, TNT and falling blocks are assumed to have infinite health, because they are neither destroyed by explosions (although they can be moved by explosions, and they can also be fired out of TNT cannons), nor by being on fire for long periods. However, they can still be "killed" with the use of the /kill command.

#### 
See also: Transportation (contains information about speed)
Boats, boats with chests and minecarts appear to recover health over time. For example, they can be broken by hitting them quickly, but cannot be destroyed by hits with unarmed hand with a pause after each hit. The amount of wobbling displayed by boats and minecarts when struck appears to indicate their current health. All minecart, boat and boat with chest variants have 6.

#### Gravity-affected blocks
Main article: Falling Block
Falling sand that collapsed into a dungeon.
Gravity-affected blocks include sand, gravel, anvils, red sand, dragon eggs, concrete powder, scaffolding, and pointed dripstone, along with snow layers in Bedrock Edition.

A gravity-affected block normally exists as a block, but when its support is removed, it becomes a falling block entity and falls down until hitting the top surface of another block. If there is valid space, it places itself as a block at the nearest on-grid position, or drops as an item if that position is occupied by a block without a solid top surface, such as a torch or a bottom slab.

While a falling block ordinarily falls straight down, its trajectory can be affected by explosions, bubble columns, pistons, reeling it in, and moving slime blocks, and can slide down the side of honey blocks. It is also possible to modify the velocity and direction of a falling block by using commands such as /data‌[Java Edition  only] or third-party programs. A falling block despawns and drops as an item if it does not land after existing for 600 ticks (30 seconds), or 100 ticks (5 seconds) if falling into the void[verify].

If a cave generates underneath sand, gravel, or red sand, the blocks remain stationary until it receives a block update. If a single block is updated and falls down, neighboring blocks are updated in a chain reaction that can cause the collapse of an entire region of gravity-affected blocks.

#### 
Entities with use interactions (such as boats, boat with chests, minecarts, cats, villagers, tamed parrots, and tamed wolves) do not stop the use action of a tool the player is holding. For example, using a water bucket on a tamed wolf causes the wolf to sit, but also empties the bucket near or onto the wolf.

#### Riding
A spider jockey.
Entities may be riding on, or attached to, other entities. When this is the case, only the lower/"outer" entity's volume collides with other things, and only that entity can control movement.‌[Java Edition  only] However, there are exceptions: players riding minecarts, boats, boats with chests, or saddled horses, baby zombies riding chickens, and skeletons riding horses or boats.

The only current legitimate combinations of riding entities are:

- Amoborplayerin aminecart,boatorboat with chests.
- A boat or boat with chest in a minecart‌[Java Edition  only][1].
- A player on a saddledpig,horse,donkey,mule,skeleton horse,llama,strider, orcamel.
- Any type ofskeletonon aspiderorcave spider‌[Bedrock Edition  only]; also known as aspider jockey.
- Any type of babyzombieorzombified piglin‌[Java Edition  only]on achickenor other mobs‌[Bedrock Edition  only]; also known as achicken jockey.
- Skeleton traps;skeletonsridingskeleton horses.
- Pillager,vindicator, orevokerriding aravager.
- Babypiglin, riding a babyhoglin.
- Baby piglin, riding a baby piglin on a baby hoglin.
- Baby piglin, riding a baby piglin, riding a baby piglin on a baby hoglin.
- Astrider, riding another strider.
- Zombified piglinriding a strider.

Note that a parrot on player shoulder isn't considered as riding.

It is possible to have even more levels, such as a baby piglin on another baby piglin who is riding a hoglin in a minecart in a boat.

Entities can also be stacked on top of each other with the use of the /summon and /data commands in Java Edition. For example, using /summon spider ~ ~ ~ {Passengers:[{id:skeleton}]} summons a spider jockey, or using /ride in Bedrock Edition.

If an entity is riding another entity, the top entity cannot teleport because as soon as the teleport is made, the entity is teleported back to riding the other entity.‌[Java Edition  only]

Starting from the Nether Update, entities that are riders or passengers of other entities cannot despawn.[verify]‌[Java Edition  only]

## Types of entities
The table below lists types of entities that currently exist in Minecraft. 

Entities listed as "solid" obstruct the passage of other entities. 


| Type                                                             | Solid                                          | Health                                   | Resource location                                                                                | Living entity |
|------------------------------------------------------------------|------------------------------------------------|------------------------------------------|--------------------------------------------------------------------------------------------------|---------------|
| Player[note 1]                                                   | Yes                                            | 20× 10(Varies withattributes)            | `player`                                                                                         | Yes           |
| Mob                                                              | Yes                                            | Varies                                   | seeJava Edition data values § Entities                                                           | Yes           |
| Armor Stand[note 1]                                              | No                                             | 20× 10                                   | `armor_stand`                                                                                    | Yes           |
| Arrow                                                            | Yes (to boats, boat with chests and minecarts) | ∞                                        | `arrow`,`spectral_arrow`‌[JE  only]                                                              | No            |
| Balloon‌[edu & BE  only]                                         | Yes                                            | ∞                                        | `balloon`                                                                                        | No            |
| Block display‌[JE  only]                                         | No                                             | ∞                                        | `block_display`                                                                                  | No            |
| Boat                                                             | Yes                                            | 6<br/>Recovers health quickly over time. | `boat`                                                                                           | No            |
| Boat with Chest                                                  | Yes                                            | 6<br/>Recovers health quickly over time. | `chest_boat`                                                                                     | No            |
| Egg                                                              | Yes                                            | ∞                                        | `egg`                                                                                            | No            |
| End Crystal                                                      | No                                             | 5                                        | `end_crystal`‌[JE  only],`ender_crystal`‌[BE  only]                                              | No            |
| Ender Pearl                                                      | Yes                                            | ∞                                        | `ender_pearl`                                                                                    | No            |
| Evoker Fangs                                                     | No                                             | ?[more information needed]               | `evoker_fangs`‌[JE  only],`evocation_fang`‌[BE  only]                                            | No            |
| Eye of Ender                                                     | No                                             | ∞                                        | `eye_of_ender`‌[JE  only],`eye_of_ender_signal`‌[BE  only]                                       | No            |
| Experience Orb                                                   | No                                             | 5                                        | `experience_orb`‌[JE  only],`xp_orb`‌[BE  only]                                                  | No            |
| Falling Block                                                    | No                                             | ∞                                        | `falling_block`                                                                                  | No            |
| Fishing Bobber                                                   | Yes (to boats, boat with chests and minecarts) | ∞                                        | `fishing_bobber`‌[JE  only],`fishing_hook`‌[BE  only]                                            | No            |
| Fireball<br/>Small Fireball<br/>Wither skull<br/>Dragon Fireball | Yes                                            | ∞                                        | `fireball`,`small_fireball`,`wither_skull`,`wither_skull_dangerous`‌[BE  only],`dragon_fireball` | No            |
| Firework Rocket                                                  | No                                             | ∞                                        | `fireworks_rocket`                                                                               | No            |
| Ice Bomb‌[edu & BE  only]                                        | Yes                                            | ∞                                        | `ice_bomb`                                                                                       | No            |
| Interaction‌[JE  only]                                           | No                                             | ∞                                        | `interaction`                                                                                    | No            |
| Item                                                             | Yes (to boats, boat with chests and minecarts) | 5                                        | `item`                                                                                           | No            |
| Item display‌[JE  only]                                          | No                                             | ∞                                        | `item_display`                                                                                   | No            |
| Item frame‌[JE  only]                                            | No                                             | ∞                                        | `item_frame`,`glow_item_frame`                                                                   | No            |
| Lightning Bolt                                                   | No                                             | ∞                                        | `lightning_bolt`                                                                                 | No            |
| Leash Knot                                                       | No                                             | ∞                                        | `leash_knot`                                                                                     | No            |
| Llama Spit                                                       | Yes                                            | ∞                                        | `llama_spit`                                                                                     | No            |
| Marker‌[JE  only]                                                | No                                             | ∞                                        | `marker`                                                                                         | No            |
| <br/>Minecart                                                    | Yes (to other entities)                        | 6<br/>Recovers health quickly over time. | `minecart`                                                                                       | No            |
| <br/>Minecart with chest                                         | Yes (to other entities)                        | 6<br/>Recovers health quickly over time. | `chest_minecart`                                                                                 | No            |
| <br/>Minecart with command block                                 | Yes (to other entities)                        | 6<br/>Recovers health quickly over time. | `command_block_minecart`                                                                         | No            |
| <br/>Minecart with furnace‌[JE  only]                            | Yes (to other entities)                        | 6<br/>Recovers health quickly over time. | `furnace_minecart`                                                                               | No            |
| <br/>Minecart with hopper                                        | Yes (to other entities)                        | 6<br/>Recovers health quickly over time. | `hopper_minecart`                                                                                | No            |
| <br/>Minecart with monster spawner‌[JE  only]                    | Yes (to other entities)                        | 6<br/>Recovers health quickly over time. | `spawner_minecart`                                                                               | No            |
| <br/>Minecart with TNT                                           | Yes (to other entities)                        | 6<br/>Recovers health quickly over time. | `tnt_minecart`                                                                                   | No            |
| Painting                                                         | No                                             | ∞                                        | `painting`                                                                                       | No            |
| PrimedTNT                                                        | No                                             | ∞                                        | `tnt`                                                                                            | No            |
| Text display‌[JE  only]                                          | No                                             | ∞                                        | `text_display`                                                                                   | No            |
| Shulker Bullet                                                   | Yes                                            | ∞                                        | `shulker_bullet`                                                                                 | No            |
| Snowball                                                         | Yes                                            | ∞                                        | `snowball`                                                                                       | No            |
| Trident                                                          | Yes                                            | ∞                                        | `trident`‌[JE  only],`thrown_trident`‌[BE  only]                                                 | No            |
| Wind Charge‌[upcoming: JE 1.21 & BE 1.21.0]                      | Yes                                            | ∞                                        | `wind_charge`‌[JE  only],`breeze_wind_charge`‌[JE  only],`wind_charge_projectile`‌[BE  only]     | No            |

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
- finalVelocity=(initialVelocity×(1−drag)ticksPassed)−(acceleration×1−(1−drag)ticksPasseddrag)

Drag applied after acceleration[note 2]:
- finalVelocity=(initialVelocity×(1−drag)ticksPassed)−(acceleration×1−(1−drag)ticksPasseddrag×(1−drag))

1. ↑ a bIn Bedrock Edition, these entities are under the mob category.
2. ↑ a b c dNote that when living entities and explosive projectiles are simulated, the drag is applied after the acceleration, rather than before; this is why their terminal velocities aren't whole numbers while the others are.
3. ↑Players, mobs and armor stands whose OnGround property is set to 1 have an horizontal drag force of ~0.454.
4. ↑ a b c d eIn each tick, items, falling blocks, primed TNTs, minecarts, boats, experience orbs and fishing bobbers apply acceleration together with velocity to update the position. This means that the new position is calculated by subtracting the acceleration from the current velocity.
5. ↑Minecarts have a maximum horizontal velocity of 0.4. Any greater value is reset to that number.
6. ↑Boats' horizontal position gets updated using next tick's velocity instead of the current one.
7. ↑ a bExplosive projectiles and wind charges are not affected by gravity but instead get acceleration from getting damaged.
8. ↑Dangerous wither skulls have drag force of ~0.27.

## Data values
Java Edition:

Main article: Entity format
- : Root tag.
	- 
	- Tags common to all entities

Bedrock Edition:

See Bedrock Edition level format/Entity format.

