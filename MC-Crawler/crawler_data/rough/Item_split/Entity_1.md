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

