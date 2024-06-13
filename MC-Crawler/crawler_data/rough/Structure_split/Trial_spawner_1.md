#### Spawning values
| Type                                                | Spawn interval             | Total mobs (base) | Total mobs added per player | Simultaneous mobs (base) | Simultaneous mobs added per player |
|-----------------------------------------------------|----------------------------|-------------------|-----------------------------|--------------------------|------------------------------------|
| Default values                                      | 40 game ticks (2 seconds)  | 6                 | 2                           | 2                        | 1                                  |
| Breeze                                              | 20 game ticks (1 second)   | 2                 | 1                           | 1                        | 0.5                                |
| Baby zombie                                         | 20 game ticks (1 second)   | Default           | Default                     | Default                  | 0.5                                |
| All others in trial chambers                        | 20 game ticks (1 second)   | Default           | Default                     | 3                        | 0.5                                |
| All others (slow versions)[more information needed] | 160 game ticks (8 seconds) | Default           | Default                     | 4                        | 2                                  |

Mobs spawn in positions that have a line of sight to the spawner, in a 4-block spherical radius. This is different from the monster spawner, which has a larger, rectangular spawning box. Otherwise, the standard mob spawning rules apply (mobs cannot collide with blocks, guardians and elder guardians spawn only in water, etc.)

### Completion
All mobs spawned by the trial spawner must be defeated before the trial spawner can drop loot. A mob is considered defeated when is either killed or transformed into another entity (excepting the transformation of creepers into charged creepers; the charged creeper must be defeated before completion of the trial spawner).

If a mob spawns more mobs upon death, only the initial mob must be defeated in order to complete the spawner (i.e. slimes and magma cubes).

#### Cooldown
Upon completion, the trial spawner enters a cooldown state for 30 minutes (36000 game ticks) before it can be activated again.

### Custom trial spawners
Using a spawn egg on a trial spawner sets the trial spawner's type to that egg's entity.

Trial spawners placed by players have the same loot data as those found in trial chambers.

### Loot
When all mobs have been killed, the spawner waits 40 ticks (2 seconds). Then, every 30 ticks (1.5 seconds), it ejects random items from the loot table. It does this for every detected player. It has a 50% chance of picking the trial key, in which case it drops for all players. The other 50% of the time it drops one of the other items for each player.
In Java Edition, each trial spawner contains 1 item stack,  with the following distribution: 

| Item                   | Stack Size  [A] | Weight   [B]    | Chance   [C] | Avg.per spawner   [D] | Avg. # spawnersto defeat   [E] |
|------------------------|-----------------|-----------------|--------------|-----------------------|--------------------------------|
| Trial Key              | 1               | $\frac{13}{26}$ | 50.0%        | 0.500                 | 2.0                            |
| Glow Berries           | 2–10            | $\frac{3}{26}$  | 11.5%        | 0.692                 | 8.7                            |
| Emerald                | 1–6             | $\frac{3}{26}$  | 11.5%        | 0.404                 | 8.7                            |
| Baked Potato           | 1–3             | $\frac{3}{26}$  | 11.5%        | 0.231                 | 8.7                            |
| Golden Carrot          | 1–3             | $\frac{1}{26}$  | 3.8%         | 0.077                 | 26.0                           |
| Ender Pearl            | 1               | $\frac{1}{26}$  | 3.8%         | 0.038                 | 26.0                           |
| Potion of Regeneration | 1               | $\frac{1}{26}$  | 3.8%         | 0.038                 | 26.0                           |
| Potion of Strength     | 1               | $\frac{1}{26}$  | 3.8%         | 0.038                 | 26.0                           |



↑ The size of stacks (or for unstackable items, number) of this item on any given roll.

↑ The weight of this item relative to other items in the pool.

↑ The odds of finding any of this item in a single chest.

↑ The number of items expected per chest, averaged over a large number of chests.

↑ The average number of chests the player should expect to search to find any of this item.



### Ominous trial
Main article: Ominous Trial Spawner
A player with Bad Omen that is within the activation range of a trial spawner is given the Trial Omen effect, starting an ominous trial. During an ominous trial, trial spawners near a player with Trial Omen are converted into ominous trial spawners. When a trial spawner becomes ominous, all of its existing mobs are despawned. If the spawner was on cooldown and was not ominous before going on cooldown, the cooldown is skipped when becoming ominous.

## Data values
### ID
Java Edition:

| Name          | Identifier      | Form         | Translation key                 |
|---------------|-----------------|--------------|---------------------------------|
| Trial Spawner | `trial_spawner` | Block & Item | `block.minecraft.trial_spawner` |

| Name         | Identifier      |
|--------------|-----------------|
| Block entity | `trial_spawner` |

Bedrock Edition:

| Name          | Identifier      | Numeric ID | Form                       | Item ID[i 1]   | Translation key           |
|---------------|-----------------|------------|----------------------------|----------------|---------------------------|
| Trial Spawner | `trial_spawner` | `-315`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.trial_spawner.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

| Name         | Savegame ID    |
|--------------|----------------|
| Block entity | `TrialSpawner` |

