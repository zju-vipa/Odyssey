### Projectile spawning
When at least one player is within the activation range of an ominous trial spawner, every 8 seconds it spawns ominous item spawners above any such player or any mob that was spawned by this ominous trial spawner. The ominous item spawner displays a projectile for 3 to 6 seconds before shooting that projectile downwards. Each ominous trial spawner has a set of 2 projectiles it spawns, one of which is a lingering potion. The lingering potion effect is selected randomly from one of the following (all with equal chance):

- Wind Charged
- Oozing
- Weaving
- Infested
- Strength
- Speed
- Slow Falling

The second projectile is randomly selected from one of the following (again, all with equal chance):

- Arrow
- Arrow of Poison
- Arrow of SlownessIV
- Fire charge
- Wind charge
- Bottle o' enchanting

### Loot
Ominous trial spawners in trial chambers eject different (better) rewards compared to the non-ominous state.

Like the normal trial spawner, it ejects the loot once for each detected player. Instead of trial keys, an ominous trial spawner has a 30% chance to eject ominous trial keys, in which case it drops for all payers.  The other 70% of the time it drops one of the other items for each player.
In Java Edition 1.21, each trial chambers trial spawner ominous contains 1 item stack,  with the following distribution: 

| Item                   | Stack Size  [A] | Weight   [B]     | Chance   [C] | Avg.per spawner   [D] | Avg. # spawnersto defeat   [E] |
|------------------------|-----------------|------------------|--------------|-----------------------|--------------------------------|
| Ominous Trial Key      | 1               | $\frac{33}{110}$ | 30.0%        | 0.300                 | 3.3                            |
| Baked Potato           | 2–4             | $\frac{21}{110}$ | 19.1%        | 0.573                 | 5.2                            |
| Steak                  | 1–2             | $\frac{21}{110}$ | 19.1%        | 0.286                 | 5.2                            |
| Golden Carrot          | 1–2             | $\frac{14}{110}$ | 12.7%        | 0.191                 | 7.9                            |
| Rotten Flesh           | 1–4             | $\frac{7}{110}$  | 6.4%         | 0.159                 | 15.7                           |
| Potion of Regeneration | 1               | $\frac{7}{110}$  | 6.4%         | 0.064                 | 15.7                           |
| Potion of Strength     | 1               | $\frac{7}{110}$  | 6.4%         | 0.064                 | 15.7                           |



↑ The size of stacks (or for unstackable items, number) of this item on any given roll.

↑ The weight of this item relative to other items in the pool.

↑ The odds of finding any of this item in a single chest.

↑ The number of items expected per chest, averaged over a large number of chests.

↑ The average number of chests the player should expect to search to find any of this item.



Ominous trial spawners converted from manually placed trial spawners will continue to drop the loot of a normal trial spawner (see Trial Spawner#Loot)

## Data values
Main article: Trial Spawner § Data values
The ominous trial spawner is technically a block state of the trial spawner. Therefore, it has the same data value structure.


