# Ravager
A ravager is a large hostile mob that only spawns alongside illagers in raids. It attacks players, adult villagers, wandering traders and iron golems by biting, roaring, and running at them. A ravager can also get stunned when blocked by a shield.

## Contents
- 1 Spawning
	- 1.1 Raids
		- 1.1.1 Java Edition
		- 1.1.2 Bedrock Edition
- 2 Drops
	- 2.1 On death
- 3 Behavior
- 4 Sounds
- 5 Data values
	- 5.1 ID
	- 5.2 Entity data
- 6 Achievements
- 7 Advancements
- 8 History
- 9 Issues
- 10 Gallery
	- 10.1 Renders
	- 10.2 Screenshots
	- 10.3 Development images
	- 10.4 In other media
- 11 Trivia
- 12 References
- 13 External links

## Spawning
### Raids
Ravagers spawn starting at wave 3 as part of a raid.

#### Java Edition
Unridden ravagers spawn at wave 3, a ravager ridden by a pillager spawns at wave 5, and two ravagers - one ridden by a vindicator and one by an evoker - spawn at wave 7. If raid has an extra wave, another ravager or two can spawn at it as well.

#### Bedrock Edition
Up to 5 ravagers spawn as part of a raid. Unridden ravagers spawn at waves 3 and 5, a ravager ridden by a pillager spawns at waves 5 and 7, and a ravager ridden by an evoker spawns at wave 7.

Ravagers can be summoned with riders by using spawn event commands:  /summon ravager ~ ~ ~ minecraft:spawn_with_pillager_rider.

## Drops
### On death
| Item |        | Roll Chance | Quantity (Roll Chance) |           |            |             |
|------|--------|-------------|------------------------|-----------|------------|-------------|
|      |        |             | Default                | Looting I | Looting II | Looting III |
|      | Saddle | 100%        | 1                      | 1         | 1          | 1           |

A ravager drops 20 experience points when killed by a player or a tamed wolf.

## Behavior
Ravagers are hostile toward players, iron golems, adult villagers and wandering traders within a 32-block radius. They attack by ramming enemies with their head, dealing a knockback of 5 blocks. Ravagers also attack by opening and closing their mouths, similar to biting their target.

When a ravager sees a villager and an iron golem at the same time, it always prioritizes the villager, unless it is already fighting the iron golem.

A ravager can also destroy some types of block by charging into them. In Java Edition, ravagers can break all leaves and only some crops. In Bedrock Edition, the ravager can break most leaves, but not cherry leaves, most crops, including most plants and mushrooms, and turtle eggs.

| Block                                             | Bedrock Edition | Java Edition |
|---------------------------------------------------|-----------------|--------------|
| Bamboo                                            | Yes             | No           |
| Bamboo Sapling                                    | Yes             | No           |
| Beetroot                                          | Yes             | Yes          |
| Brown Mushroom                                    | Yes             | No           |
| Carrots                                           | Yes             | Yes          |
| Carved Pumpkin                                    | Yes             | No           |
| Chorus Flower                                     | Yes             | No           |
| Chorus Plant                                      | Yes             | No           |
| Dead Bush                                         | Yes             | No           |
| FernUnused variant                                | Yes             | N/A          |
| FernUnused variant                                | Yes             | N/A          |
| Sunflower                                         | Yes             | No           |
| Lilac                                             | Yes             | No           |
| Peony                                             | Yes             | No           |
| Rose Bush                                         | Yes             | No           |
| Large Fern                                        | Yes             | No           |
| Tall Grass                                        | Yes             | No           |
| Leaves                                            | Yes             | Yes          |
| Cherry Leaves                                     | No              | Yes          |
| Flowers, except forwither roseandtorchflower      | Yes             | No           |
| Wither Rose                                       | No[1]           | No           |
| Torchflower                                       | No              | No           |
| Grass                                             | Yes             | No           |
| Jack o'Lantern                                    | Yes             | No           |
| Melon                                             | Yes             | No           |
| Melon Stem                                        | Yes             | No           |
| Attached Melon Stem                               | Yes             | No           |
| Potatoes                                          | Yes             | No           |
| Pumpkin                                           | Yes             | No           |
| Attached Pumpkin Stem                             | Yes             | No           |
| Pumpkin Stem                                      | Yes             | No           |
| Red Mushroom                                      | Yes             | No           |
| Sugar Cane                                        | Yes             | No           |
| SaplingsexceptCherry SaplingandMangrove Propagule | Yes             | No           |
| Snow                                              | Yes             | No           |
| Sweet Berry Bush                                  | Yes             | No           |
| Turtle Egg                                        | Yes             | No           |
| Vines                                             | Yes             | No           |
| Lily Pad                                          | Yes             | No           |
| Wheat                                             | Yes             | Yes          |
| Crimson Fungus                                    | Yes             | No           |
| Warped Fungus                                     | Yes             | No           |
| Hanging Roots                                     | Yes             | No           |
| Cave Vines                                        | Yes             | No           |
| Cave Vines Plant                                  | Yes             | No           |
| Azalea                                            | Yes             | No           |
| Small Dripleaf                                    | Yes             | No           |
| Big Dripleaf                                      | Yes             | No           |
| Big Dripleaf Stem                                 | Yes             | No           |
| Spore Blossom                                     | Yes             | No           |
| Torchflower Crop                                  | No              | Yes          |
| Pitcher Crop                                      | No              | Yes          |


Although ravagers have a large version of the saddle as part of their texture, they do not actually wear one, and they cannot be ridden by the player. Ravagers can only spawn in raids, sometimes with a pillager, evoker, or vindicator‌[Java Edition  only] riding them; however, another mob can be allowed to ride a ravager using the /ride command.

In Bedrock Edition ravagers have delayed hits (hit_delay_pct: 0.5). When set to 0.0, ravager hits wouldn't be delayed to match Java Edition.

When its bite attack is blocked by a shield, no damage is dealt and knockback is halved. A ravager also has a 50% chance to become stunned and unable to move or attack for 2 seconds. After this period, it opens its mouth and roars, dealing 6 damage and a knockback of 5 blocks to nearby entities. The roar knocks back nearby illagers without damaging them and has no effect on other ravagers (note that vexes and witches are not treated as illagers and take both damage and knockback). Illagers knocked back by a ravager's roar can still take fall damage.

Ravagers do not attack pillagers who shoot at them by accident, and do not attack evokers when evoker fangs accidentally hit them. When a vindicator riding a ravager has been named "Johnny" it may attack the ravager while it is riding it, but the ravager does not attack the vindicator for any reason. When a ravager gets shot by a mob that battles with a projectile while it is attacking the player, the ravager first attempts to kill who shot it, then goes back to attacking the player once the deed is done. Any mob that doesn't battle with projectiles requires a ravagers to roar in order to aggro on it. 

In Java Edition, a ravager who gets attacked by a mob (excluding illagers or goats) or player alerts other ravagers to target the attacker unless the ravager was killed in one hit. 

Ravagers take 75% less of knockback, but they still float in water. A ravager being ridden dismounts its rider if it moves into water two blocks deep. Riders cannot mount ravagers again after being dismounted.

In Java Edition, any ravager can join a patrol if sufficiently near a patrol captain.

