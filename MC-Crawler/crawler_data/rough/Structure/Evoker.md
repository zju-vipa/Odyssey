# Evoker
An evoker is a spell-casting illager that can be found in woodland mansions and raids, and is the only source of the totem of undying. It uses two spells to attack: one that summons armor-piercing fangs and one that summons vexes.

## Contents
- 1 Spawning
	- 1.1 Woodland mansions
	- 1.2 Raids
		- 1.2.1 Java Edition
		- 1.2.2 Bedrock Edition
- 2 Drops
	- 2.1 On death
- 3 Behavior
	- 3.1 Fang attack
	- 3.2 Summoning vexes
	- 3.3 Combo attack
	- 3.4 Sheep color conversion spell
	- 3.5 Attack pattern data
		- 3.5.1 Java Edition
		- 3.5.2 Bedrock Edition
- 4 Evoker fangs
- 5 Sounds
- 6 Data values
	- 6.1 ID
	- 6.2 Entity data
- 7 Achievements
- 8 Advancements
- 9 History
- 10 Issues
- 11 Trivia
- 12 Gallery
	- 12.1 Renders
	- 12.2 Textures
	- 12.3 Screenshots
	- 12.4 In other media
- 13 References
- 14 External links

## Spawning
### Woodland mansions
Evokers spawn during the generation of particular woodland mansion rooms. They do not respawn after their initial spawn.

Evokers spawned with mansions do not naturally despawn (unless the world difficulty is switched to Peaceful).

### Raids
Evokers can spawn during raids by themselves or riding ravagers. Evokers cannot spawn in raids on Easy difficulty, because such raids have only three waves, while evokers appear in the fifth wave and above.

#### Java Edition
Evokers spawn during raids starting at wave five. Up to five evokers spawn on Hard difficulty. During these events, they can be a raid captain. On Hard difficulty, evokers can also spawn riding a ravager at wave seven. They may also rarely spawn as a raid captain.

#### Bedrock Edition
Up to five evokers spawn during raids, with one evoker spawning during waves five and six, and three evokers spawning during wave seven. One of them rides a ravager during wave seven.

## Drops
### On death
| Item |                  | Roll Chance | Quantity (Roll Chance) |           |            |             |
|------|------------------|-------------|------------------------|-----------|------------|-------------|
|      |                  |             | Default                | Looting I | Looting II | Looting III |
|      | Totem of Undying | 100%        | 1                      | 1         | 1          | 1           |
|      | Emerald          | 100%[d 1]   | 0–1                    | 0–2       | 0–3        | 0–4         |
|      | Ominous Banner   | 100%[d 2]   | 1                      | 1         | 1          | 1           |

1. ↑Dropped only when kill credit is given to the player
2. ↑When holding an ominous banner.

- 10experiencewhen killed by a player or tamedwolf.

## Behavior
An evoker moves at the player's sprinting speed, crosses its arms and does not show its hands. In Bedrock Edition, an evoker riding an entity does not visually sit down.

An evoker attacking with its fangs.
Evokers attack players, adult villagers, iron golems, snow golems‌[BE  only] and wandering traders within 12 blocks by rising and waving both of their arms while looking at their target and summoning magical fangs or vexes, creating different colored particles for the different attacks.

If the player is within a ten block radius and the evoker is not in the middle of summoning an attack, the evoker flees from the player to avoid being attacked.

An evoker summoning fangs in two circles around it.
If an evoker is attacked, all evokers in a twelve block radius become alerted and start attacking the player, even if they are behind walls. In Java Edition, the alerted evokers can attack the player from an infinite distance away, even if the player switches to Creative or Spectator mode[1]; this can be fixed by relogging the world, or by setting the game rule universalAnger to True. This is only true for the alerted evokers, not the intitially attacked evoker.

In Java Edition, an evoker is passive to other illagers even if it is harmed. Any evoker can search for and join a patrol if sufficiently near a patrol captain.

In Java Edition, evokers and illusioners are faster without any effects during raids.

In Java Edition, evokers are given three seconds of the Glowing effect if a bell is rung within 32 blocks of them. This applies to both evokers spawned in raids and evokers spawned in woodland mansions.

### Fang attack
The evoker signals this attack by producing purple particles () and a low-pitched sound. 

A number of fangs rise out of the ground around the player, then snap shut and vanish. 

Players or mobs caught in the attack are dealt 6 damage, regardless of difficulty. This harm is not mitigated by armor but is mitigated by enchantments such as Protection. Any evoker-summoned fangs do not deal damage to any illagers, although fangs summoned or spawned by the player do. When a neutral or hostile mob is caught in the attack, the mob attacks the evoker.

Fangs appear no lower than the feet of the lowest combatant and no higher than one block above the feet of the highest combatant. Fangs attempt to appear on the highest opaque block between those two extremes, but fail to spawn if they are obstructed by a solid block. In practice, this means that fangs cannot spawn inside deep pits or on top of high walls, but may, for example, go up a staircase if the target is at the top and the evoker at the bottom, or vice versa. Likewise, an evoker floating in a boat on water cannot summon fangs against a player swimming or floating in a boat because there are no opaque blocks from which the fangs can appear.

The evoker typically summons sixteen fangs in a straight line toward the target. However, if the target is within three blocks of the evoker, the evoker summons the fangs in two circles around itself: the smaller circle has five fangs and the larger has eight. The fangs do not seek the player, thus the player is able to dodge them. Summoning fangs resets the evoker's spell cooldown to two seconds and resets the cooldown for summoning fangs to five seconds.

### Summoning vexes
The evoker signals this attack by producing white particles () for two seconds and a higher-pitched sound. Three vexes appear nearby. The evoker can summon vexes as long as there are fewer than eight vexes within sixteen blocks centered on the evoker. 

This spell resets the evoker's spell cooldown to five seconds and resets the cooldown for summoning vexes to seventeen seconds.

An evoker summoning vexes.
### Combo attack
In Java Edition, evokers may summon two circle fangs while summoning vexes, without any cooldown. It usually happens when a player melee attacks an evoker while it is summoning vexes.

### Sheep color conversion spell
An evoker using its sheep color conversion spell.
While the evoker is not engaged in combat and /gamerule mobGriefing is set to true, it changes the wool color of any blue sheep within sixteen blocks from blue to red. 

After the spell, the sheep is red.
The evoker signals this spell by producing orange particles () and making a "wololo" sound. 

This spell resets the evoker's spell cooldown to three seconds and resets the cooldown for the sheep color conversion spell to seven seconds. Evokers look at the sheep they are using the spell on while they are doing the spell until they finish the spell. 

In Bedrock Edition, evokers can still change a sheep's color when /gamerule mobGriefing is set to false. 

### Attack pattern data
#### Java Edition

  

This section of the article is empty. 
You can help by adding to it.


#### Bedrock Edition


| Type                          | Weight | Min activation range (distance) | Max activation range (distance) | Entities spawned (amount) | Size | Summon cap | Summon cap radius |
|-------------------------------|--------|---------------------------------|---------------------------------|---------------------------|------|------------|-------------------|
| Fangs attack (line)           | 3      | 3.0                             | N/A                             | 16 Fangs                  | 20   |            | N/A               |
| Fangs attack (inside circle)  | 3      | 0.0                             | 3.0                             | 5 Fangs                   | 1.5  |            | N/A               |
| Fangs attack (outside circle) | 3      | 0.0                             | 3.0                             | 8 Fangs                   | 2.5  |            | N/A               |
| Summoning vexes               | 1      |                                 | N/A                             | 3 Vexes                   | 1.0  | 8          | 16.0              |
| Color conversion spell        | 3      | 0.0                             | 16.0                            |                           |      |            | N/A               |

| Type                          | Base delay | Delay per summon | Cooldown time | Cast duration | Entity lifespan |
|-------------------------------|------------|------------------|---------------|---------------|-----------------|
| Fangs attack (line)           | 1.0        | 0.05             | 5.0           | 2.0           | 1.1             |
| Fangs attack (inside circle)  | 1.0        | 0.0              | 5.0           | 2.0           | 1.1             |
| Fangs attack (outside circle) | 0.15       | 0.0              | 5.0           | 2.0           | 1.1             |
| Summoning vexes               | 2.0        | N/A              | 17.0          | 5.0           | N/A             |
| Sheep color conversion spell  |            | N/A              | 5.0           | 3.0           | N/A             |

## Evoker fangs
This article is about the evoker fangs in Minecraft.  For evoker fangs in Minecraft Dungeons, see MCD:Evoker § Evoker fang.
| Hitbox size | Height: 0.8 blocksWidth: 0.5 blocks |
|-------------|-------------------------------------|

{
    "title": "Evoker Fangs",
    "rows": [
        {
            "field": "Height: 0.8 blocks<br>Width: 0.5 blocks",
            "label": "(link to Hitbox article, displayed as Hitbox size)"
        }
    ],
    "invimages": [],
    "images": [
        "Evoker Fangs.png"
    ]
}
Evoker fangs are the entities that evokers use to attack the player with their fang attack. Evoker fangs are not affected by the Peaceful difficulty.

The individual fangs in an evoker's fang attacks each have a delay. Before the delay is over, the fangs cannot be seen, although unlike truly invisible entities, fangs in warmup still have a visible debug hitbox. After the delay, the fangs expand into existence, snap shut, make critical hit particles and shrink out of sight again, dealing 6 magic damage to all mobs standing on the spot. Killing an evoker fang does not contribute to the "Monster Hunter" advancement or achievement.

## Data values
### ID
Java Edition:

| Name         | Identifier     | Entity tags                                   | Translation key                 |
|--------------|----------------|-----------------------------------------------|---------------------------------|
| Evoker       | `evoker`       | `illager`<br/>`illager_friends`<br/>`raiders` | `entity.minecraft.evoker`       |
| Evoker Fangs | `evoker_fangs` | None                                          | `entity.minecraft.evoker_fangs` |

Bedrock Edition:

| Name         | Identifier          | Numeric ID | Translation key                 |
|--------------|---------------------|------------|---------------------------------|
| Evoker       | `evocation_illager` | `104`      | `entity.evocation_illager.name` |
| Evoker Fangs | `evocation_fang`    | `103`      | `entity.evocation_fang.name`    |

### Entity data
Java Edition:

Main article: Entity format
Evokers have entity data associated with them that contains various properties.

- Entity data
	- 
	- Tags common to all entities
	- 
	- Tags common to all mobs
	- 
	- Tags common to all mobs spawnable in raids
	- SpellTicks: Number of ticks until a spell can be cast. Set to a positive value when a spell is cast, and decreases by 1 per tick.

Evoker fangs have entity data associated with them that contains various properties.

- Entity data
	- 
	- Tags common to all entities
	- Owner: TheUUIDof the entity that that fired the fangs, stored as four ints. If the entity is anIllager, the fangs do not damage other Illagers.
	- Warmup: Time in ticks until the fangs appear. The fangs appear and begin to close as soon as this value becomes zero or less; negative values simply result in no delay. The value continues ticking down while the closing animation is playing, reaching -20 on naturally spawned fangs.

Bedrock Edition:

SeeBedrock Edition level format/Entity format.
