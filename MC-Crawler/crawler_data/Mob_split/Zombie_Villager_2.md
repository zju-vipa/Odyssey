### Specific to Java Edition
- If a zombie villager spawned as a nitwit or was a nitwit before it was transformed into a zombie villager, it remains a nitwit if cured.
- Naturally spawned zombie villagers become unemployed, and may gain a different profession than the one they had while zombified.
- Curing a villager spreadsminor_positivegossip through the villagergossipsystem.

### Specific to Bedrock Edition
- A former nitwit zombie villager becomes an unemployed villager and can learn a profession after the cure.
- Villagers in a range of 16 blocks in a cube surrounding the cured villager also offer a small discount proportional to the number of cured villagers (up to 10).
- Saving and reloading the world causes the curing process to finish as soon as the chunk containing the villager is ticked. This does not happen if the player moves out of range, then returns: In that case, the countdown timer pauses until the player returns.

## Data values
### ID
Java Edition:

| Name            | Identifier      | Entity tags                                                                                         | Translation key                  |
|-----------------|-----------------|-----------------------------------------------------------------------------------------------------|----------------------------------|
| Zombie Villager | zombie_villager | can_breathe_under_waterignores_poison_and_regeninverted_healing_and_harmundeadwither_friendszombies | entity.minecraft.zombie_villager |

Bedrock Edition:

| Name                  | Identifier         | Numeric ID | Translation key                |
|-----------------------|--------------------|------------|--------------------------------|
| Zombie Villager (old) | zombie_villager    | 44         | entity.zombie_villager.name    |
| Zombie Villager (new) | zombie_villager_v2 | 116        | entity.zombie_villager_v2.name |

### Entity data
Zombie villagers have entity data associated with them that contains various properties.

Bedrock Edition:

See Bedrock Edition level format/Entity format.
Java Edition:

Main article: Entity format

 Entity data
Tags common to all entities
Tags common to all mobs
Tags common to all villagers
Tags common to all zombies
 ConversionTime: -1 when not being converted back to a villager, positive for the number of ticks until conversion back into a villager. The regeneration effect parallels this.
 ConversionPlayer: The UUID of the player who started curing the zombie, stored as four ints.


Zombie villager type
Main article: Zombie Villager/DV[edit]


Zombie villager profession
Main article: Zombie Villager/DV2[edit]


