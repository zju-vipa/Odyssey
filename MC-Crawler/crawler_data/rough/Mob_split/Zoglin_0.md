# Zoglin
A zoglin is an undead hostile mob created when a hoglin enters the Overworld or End. It never retreats or flees, and attacks players and almost all non-zoglin mobs indiscriminately, using the same tusk attack as its non-zombified counterpart.

## Contents
- 1 Spawning
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
- 11 References

## Spawning
Zoglins spawn when a hoglin has been in the Overworld or the End for 300 game ticks (15 seconds). For their first 10 seconds after zombification, they get the  Nausea effect. This nausea effect is cosmetic and does not affect its behavior.
Like most hostile mobs, zoglins despawn when the difficulty is changed to Peaceful.

## Drops
### On death
Both adult and baby zoglins share the following item drop table:

| Item |              | Roll Chance | Quantity (Roll Chance) |           |            |             |
|------|--------------|-------------|------------------------|-----------|------------|-------------|
|      |              |             | Default                | Looting I | Looting II | Looting III |
|      | Rotten Flesh | 100%        | 1–3                    | 1–4       | 1–5        | 1–6         |

- 5 if adult and baby killed by aplayeror tamedwolfinJava Edition.
- 1–3 if adult killed by a player or tamed wolf inBedrock Edition.

## Behavior
Zoglins are hostile toward armor stands[1], cameras‌[BE & edu  only], players in Adventure or Survival mode, and all mobs except agents, creepers, ghasts, and other zoglins. This includes hoglins and zombified piglins. Normal hoglins do not attack zoglins unless provoked by zoglins.

When an adult zoglin attacks, it flings its target into the air. Blocking with shields does not mitigate this. When a baby zoglin attacks, they do not fling their target. Baby zoglins, unlike baby hoglins, never grow up. Any mob that can retaliate attacks a zoglin in return after being attacked, including baby zoglins.

In Java Edition adult zoglins attack once every two seconds and babies attack every second, In Bedrock Edition both adults and babies attack once every second, making them more destructive compared to Java Edition, even on peaceful difficulty.

When a zoglin attacks a piglin, the piglin either retreats or fights back. Piglin brutes attack zoglins if they are attacked first and never retreat. They also attack the zoglin if the zoglin attacks a piglin or another piglin brute.

If a zoglin is fed crimson fungus before it is zombified, it does not despawn naturally and it doesn't count toward the mob cap.

Zoglins are incapable of breeding and do not flee from blocks that repel hoglins. Zoglins can be leashed. Unlike baby hoglins, baby zoglins attack baby zombified piglins. Piglins flee from zoglins if they are not engaged in combat.

Being an undead mob, they are: 

- damaged by the status effectInstant Healthand healed by the status effectInstant Damage.
- unaffected by the status effectsRegenerationandPoison.
- ignored by thewither.
- affected by theSmiteenchantment.
- unable to swim inwater, but do not drown.
- a threat toarmadillos, causing them to hide in their shell.‌[upcoming: JE 1.20.5 & BE 1.21.0]

Like zombified piglins, they are immune to fire and lava.

## Data values
### ID
Java Edition:

| Name   | Identifier | Entity tags                                                                                                                              | Translation key           |
|--------|------------|------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| Zoglin | `zoglin`   | `can_breathe_under_water`<br/>`ignores_poison_and_regen`<br/>`inverted_healing_and_harm`<br/>`undead`<br/>`wither_friends`<br/>`zombies` | `entity.minecraft.zoglin` |

Bedrock Edition:

| Name   | Identifier | Numeric ID | Translation key      |
|--------|------------|------------|----------------------|
| Zoglin | `zoglin`   | `126`      | `entity.zoglin.name` |

### Entity data
Zoglins have entity data associated with them that contains various properties.

Java Edition:

Main article: Entity format
- Entity data
	- 
	- Tags common to all entities
	- 
	- Tags common to all mobs
	- IsBaby: 1 or 0 (true/false) - true if the zoglin is a baby. May not exist.

Bedrock Edition:

SeeBedrock Edition level format/Entity format.

