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


| Type | Weight                        | Min activation range (distance) | Max activation range (distance) | Entities spawned (amount) | Size     | Summon cap | Summon cap radius |
|------|-------------------------------|---------------------------------|---------------------------------|---------------------------|----------|------------|-------------------|
|      | Fangs attack (line)           | 3                               | 3.0                             | N/A                       | 16 Fangs | 20         | N/A               |
|      | Fangs attack (inside circle)  | 3                               | 0.0                             | 3.0                       | 5 Fangs  | 1.5        | N/A               |
|      | Fangs attack (outside circle) | 3                               | 0.0                             | 3.0                       | 8 Fangs  | 2.5        | N/A               |
|      | Summoning vexes               | 1                               | N/A                             | 3 Vexes                   | 1.0      | 8          | 16.0              |
|      |                               |                                 | Color conversion spell          | 3                         | 0.0      | 16.0       | N/A               |

| Type                          | Base delay                   | Delay per summon | Cooldown time | Cast duration | Entity lifespan |
|-------------------------------|------------------------------|------------------|---------------|---------------|-----------------|
| Fangs attack (line)           | 1.0                          | 0.05             | 5.0           | 2.0           | 1.1             |
| Fangs attack (inside circle)  | 1.0                          | 0.0              | 5.0           | 2.0           | 1.1             |
| Fangs attack (outside circle) | 0.15                         | 0.0              | 5.0           | 2.0           | 1.1             |
| Summoning vexes               | 2.0                          | N/A              | 17.0          | 5.0           | N/A             |
|                               | Sheep color conversion spell | N/A              | 5.0           | 3.0           | N/A             |

## Evoker fangs
This article is about the evoker fangs in Minecraft.  For evoker fangs in Minecraft Dungeons, see MCD:Evoker § Evoker fang.

Evoker Fangs




Hitbox size


Height: 0.8 blocksWidth: 0.5 blocks 




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

| Name         | Identifier   | Entity tags                   | Translation key               |
|--------------|--------------|-------------------------------|-------------------------------|
| Evoker       | evoker       | illagerillager_friendsraiders | entity.minecraft.evoker       |
| Evoker Fangs | evoker_fangs | None                          | entity.minecraft.evoker_fangs |

Bedrock Edition:

| Name         | Identifier        | Numeric ID | Translation key               |
|--------------|-------------------|------------|-------------------------------|
| Evoker       | evocation_illager | 104        | entity.evocation_illager.name |
| Evoker Fangs | evocation_fang    | 103        | entity.evocation_fang.name    |

### Entity data
Java Edition:

Main article: Entity format
Evokers have entity data associated with them that contains various properties.


 Entity data
Tags common to all entities
Tags common to all mobs
Tags common to all mobs spawnable in raids
 SpellTicks: Number of ticks until a spell can be cast. Set to a positive value when a spell is cast, and decreases by 1 per tick.

Evoker fangs have entity data associated with them that contains various properties.


 Entity data
Tags common to all entities
 Owner: The UUID of the entity that that fired the fangs, stored as four ints. If the entity is an Illager, the fangs do not damage other Illagers.
 Warmup: Time in ticks until the fangs appear. The fangs appear and begin to close as soon as this value becomes zero or less; negative values simply result in no delay. The value continues ticking down while the closing animation is playing, reaching -20 on naturally spawned fangs.

Bedrock Edition:

See Bedrock Edition level format/Entity format.

