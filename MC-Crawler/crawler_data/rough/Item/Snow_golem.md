# Snow Golem
A snow golem is a buildable passive mob that throws snowballs at monsters, which provokes them into attacking it. Depending on the biome temperature it also either produces a trail of snow, or takes heat damage and dies.

## Contents
- 1 Creation
- 2 Drops
	- 2.1 On death
	- 2.2 Sheared
- 3 Behavior
	- 3.1 Provocation by other mobs
- 4 Sounds
- 5 Data values
	- 5.1 ID
	- 5.2 Entity data
- 6 Achievements
- 7 Advancements
- 8 History
- 9 Issues
- 10 Trivia
- 11 Gallery
	- 11.1 Textures
	- 11.2 Screenshots
	- 11.3 Videos
	- 11.4 In other media
- 12 References

## Creation
See also: Tutorials/Snow golems














Snow golem build configuration.Jack o'lanterns can also be used.


Snow golems search for the nearest monster and attack it.
Snow golems are created by placing 2 snow blocks in an I shape (as shown in the image), and then placing a pumpkin‌[Bedrock Edition  only], a carved pumpkin, or a jack o'lantern on top. The pumpkin may be placed by the player, a dispenser, or an enderman.[1] The building pattern also works when arranged sideways or upside-down, as long as the pumpkin is the last block placed. The player can place the snow blocks in any pattern and then place an uncarved pumpkin.‌[Java Edition  only]

The snow golem spawns at the location of the snow block as its feet when created horizontally.


## Drops
### On death
| Item |          | Roll Chance | Quantity (Roll Chance) |           |            |             |
|------|----------|-------------|------------------------|-----------|------------|-------------|
|      |          |             | Default                | Looting I | Looting II | Looting III |
|      | Snowball | 100%        | 0–15                   | 0–15      | 0–15       | 0–15        |

### Sheared
A snow golem drops 1 carved pumpkin when sheared.

## Behavior
See also: Tutorials/Snow farming

A snow golem wanders aimlessly and tries to avoid water, obstacles and environmental hazards, but is immune to damage from powder snow.

A snow golem after shearing the carved pumpkin from its head.
A snow golem wears its carved pumpkin like a helmet. Its actual head is hidden beneath the pumpkin. Shearing a snow golem removes the pumpkin, revealing its face and making it drop the pumpkin. The pumpkin is stored using the Pumpkin tag instead of ArmorItems; a snow golem does not display its HandItems or its ArmorItems. After shearing the pumpkin, the player can give a snow golem a new pumpkin only by using a command, such as /data‌[Java Edition  only].

As a snow golem moves, it leaves a trail of snow on the ground if the blocks can support it[2] in any biome regardless of the temperature, unless it is in a mushroom field biome, in which it does not spread snow.‌[Bedrock Edition  only] If the mobGriefing game rule is false, a snow trail does not appear. A snow golem does'nt take any fall damage

Snow golems are damaged in contact with rain or water and in biomes with a temperature greater than 1.0. Examples include savannas, badlands, deserts or biomes in the Nether. The Fire Resistance effect allows them to survive in these biomes.‌[Java Edition  only][3]

A group of snow golems throwing snowballs at a spider.
Snow golems move toward all monsters (except ghasts) and throw snowballs at them up to 10 blocks away, provoking them, regardless of whether they attack the player.[4] When captured, they throw snowballs up to 16 blocks away. They throw one snowball per second. Thrown snowballs do not deal damage except to blazes and wolves,[5] but the snowballs knock back any mobs that they hit.

Additionally, snow golems also attack creepers and never intentionally attack the player, in Bedrock Edition, if a snowball hits the player, it deals knockback and makes tamed wolves & trusting foxes attack them. 

The snow golem's snowballs can set other mobs on fire in addition to knockback, if the shot flies through a lava block or a block that is on fire.‌[Bedrock Edition  only]

A snow golem is not provoked by another golem (snow or iron) attacking it, although an iron golem that is hit accidentally by a snow golem's snowball attacks the snow golem.

### Provocation by other mobs


| Entity                                 | Snow golem actively attacks the mob? | Actively attacks the snow golem?                         | Notes                                                                                                    |
|----------------------------------------|--------------------------------------|----------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| Bee                                    | No                                   | No                                                       | Bees retaliate if accidentally attacked.                                                                 |
| Blaze                                  | Yes                                  | No                                                       | Blazes retaliate                                                                                         |
| Bogged‌[upcoming]                      | Yes                                  | No                                                       |                                                                                                          |
| Breeze‌[upcoming]                      | Yes                                  | No                                                       |                                                                                                          |
| Creeper                                | Yes                                  | No                                                       | Creepers retaliate                                                                                       |
| Dolphin                                | No                                   | No                                                       | Dolphins retaliate if accidentally attacked.                                                             |
| Ender Dragon                           | Yes                                  | No                                                       |                                                                                                          |
| Enderman                               | Yes                                  | No                                                       | Endermen teleport away when hit by a snowball.                                                           |
| Endermite                              | Yes                                  | No                                                       | Endermites retaliate                                                                                     |
| Evoker                                 | Yes                                  | Yes‌[BE  only]<br/>No‌[JE  only]                         |                                                                                                          |
| Drowned                                | Yes                                  | Partial‌[BE  only]<br/>No‌[JE  only]                     | Drowned do not attack any mob that is not touching water during daytime.                                 |
| Fox                                    | No                                   | No                                                       | InBedrock Edition, trusting foxes attack the snow golem if the golem unintentionally attacks the player. |
| Ghast                                  | No                                   | No                                                       | Ghasts can still unintentionally damage the snow golem.                                                  |
| Giant‌[JE  only]                       | Yes                                  | N/A                                                      | Giants do not have any AI.                                                                               |
| Goat                                   | No                                   | Randomly                                                 |                                                                                                          |
| Guardian<br/>Elder Guardian            | Yes                                  | No                                                       |                                                                                                          |
| Hoglin                                 | Yes‌[JE  only]<br/>No‌[BE  only]     | No                                                       | Hoglins retaliate                                                                                        |
| Husk<br/>Zombie<br/>Zombie Villager    | Yes                                  | Yes‌[BE  only]<br/>No‌[JE  only]                         |                                                                                                          |
| Illusioner‌[JE  only]                  | Yes                                  | No                                                       | Illusioners retaliate                                                                                    |
| Iron Golem                             | No                                   | No                                                       | Iron golems retaliate if accidentally attacked.                                                          |
| Killer Bunny‌[JE  only]                | No                                   | No                                                       | Killer bunnies retaliate if accidentally attacked.                                                       |
| Llama<br/>Trader Llama                 | No                                   | No                                                       | Llamas retaliate if accidentally attacked.                                                               |
| Magma Cube                             | Yes                                  | No                                                       |                                                                                                          |
| Phantom                                | Yes                                  | No                                                       |                                                                                                          |
| Piglin                                 | Yes                                  | No                                                       | Piglins retaliate                                                                                        |
| Piglin Brute                           | Yes                                  | No                                                       | Piglin brutes retaliate                                                                                  |
| Pillager                               | Yes                                  | No                                                       | Pillagers retaliate                                                                                      |
| Polar Bear                             | No                                   | No                                                       | Polar bears retaliate if accidentally attacked.                                                          |
| Pufferfish                             | No                                   | No                                                       | Pufferfish can still damage the golem with its defense.                                                  |
| Ravager                                | Yes                                  | No                                                       | Ravagers retaliate                                                                                       |
| Shulker                                | Yes                                  | No                                                       | Shulkers retaliate                                                                                       |
| Silverfish                             | Yes                                  | Yes‌[BE  only]<br/>No‌[JE  only]                         |                                                                                                          |
| Skeleton<br/>Stray<br/>Wither Skeleton | Yes                                  | No                                                       | Skeletons retaliate                                                                                      |
| Slime                                  | Yes                                  | Yes‌[BE  only]<br/>No‌[JE  only]                         | Slimes retaliate ‌[JE  only]                                                                             |
| Spider<br/>Cave Spider                 | Yes                                  | No                                                       | Spiders retaliate                                                                                        |
| Vex                                    | Yes                                  | Partial                                                  | A vex attacks a snow golem immediately when an evoker summons three vexes.                               |
| Vindicator                             | Yes                                  | Yes‌[BE  only]<br/>No/Yes (if named "Johnny")‌[JE  only] |                                                                                                          |
| Villager                               | No                                   | No                                                       | Villagers can accidentally damage the snow golem by setting off a firework.‌                             |
| Warden                                 | Yes                                  | Yes                                                      |                                                                                                          |
| Witch                                  | Yes                                  | Yes‌[BE  only]<br/>No‌[JE  only]                         |                                                                                                          |
| Wither                                 | Yes                                  | Yes                                                      |                                                                                                          |
| Wolf(wild)                             | No                                   | No                                                       | Wild wolves retaliate if accidentally attacked.                                                          |
| Wolf(tamed)                            | No                                   | No                                                       | Tamed wolves attack the snow golem if the owner attacks the golem.                                       |
| Zoglin                                 | Yes                                  | Yes                                                      |                                                                                                          |
| Zombified Piglin                       | Yes                                  | No                                                       | Zombified piglins retaliate.                                                                             |
| All other mobs                         | No                                   | No                                                       |                                                                                                          |

## Data values
### ID
Java Edition:

| Name       | Identifier   | Entity tags                                           | Translation key               |
|------------|--------------|-------------------------------------------------------|-------------------------------|
| Snow Golem | `snow_golem` | `fall_damage_immune`<br/>`freeze_immune_entity_types` | `entity.minecraft.snow_golem` |

Bedrock Edition:

| Name       | Identifier   | Numeric ID | Translation key          |
|------------|--------------|------------|--------------------------|
| Snow Golem | `snow_golem` | `21`       | `entity.snow_golem.name` |

### Entity data
Snow golems have entity data associated with them that contain various properties.

Java Edition:

Main article: Entity format
- Entity data
	- 
	- Tags common to all entities
	- 
	- Tags common to all mobs
	- Pumpkin: 1 or 0 (true/false) - whether or not the Snow Golem has a pumpkin on its head.

Bedrock Edition:

SeeBedrock Edition level format/Entity format.
