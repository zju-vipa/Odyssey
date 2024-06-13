## Dragon Fireball

Dragon Fireball




Dragon Fireball (JE)






Dragon Fireball (BE)







Hitbox size


Height: 1 blockWidth: 1 block 




{
    "title": "Dragon Fireball",
    "rows": [
        {
            "field": "Height: 1 block<br>Width: 1 block",
            "label": "(link to Hitbox article, displayed as Hitbox size)"
        }
    ],
    "invimages": [],
    "images": []
}
Dragon fireballs are special fireballs that the ender dragon fires while strafing. They cannot be deflected unlike ghast fireballs, and they do no impact damage. Instead, they deposit purple effect clouds across the ground that damages players the same way a lingering potion of Harming II does. This means that the ender dragon's fireballs deal magic damage, which ignores any damage reduction that comes from the player's unenchanted armor.  However its damage does get reduced by armor enchanted with the Protection enchantment. The purple effect cloud's hitbox slowly grows larger in diameter until it disappears.

As with its close-ranged breath attack, the purple clouds can be bottled to obtain the dragon's breath.

Unlike lingering potions of Harming, the effect cloud does not shrink when affecting mobs.


## Data values
### ID
Java Edition:

| Name            | Identifier      | Entity tags        | Translation key                  |
|-----------------|-----------------|--------------------|----------------------------------|
| Ender Dragon    | ender_dragon    | None               | entity.minecraft.ender_dragon    |
| Dragon Fireball | dragon_fireball | impact_projectiles | entity.minecraft.dragon_fireball |

Bedrock Edition:

| Name            | Identifier      | Numeric ID | Translation key             |
|-----------------|-----------------|------------|-----------------------------|
| Ender Dragon    | ender_dragon    | 53         | entity.ender_dragon.name    |
| Dragon Fireball | dragon_fireball | 79         | entity.dragon_fireball.name |

### Entity data
Ender dragons have entity data associated with them that contain various properties.

Bedrock Edition:

See Bedrock Edition level format/Entity format.
Java Edition:

Main article: Entity format

 Entity data
Tags common to all entities
Tags common to all mobs
 DragonPhase: A number indicating the dragon's current state. 0 means circling. 1 means strafing (preparing to shoot a fireball). 2 means flying to the portal to land (part of transition to landed state). 3 means landing on the portal (part of transition to landed state). 4 means taking off from the portal (part of transition out of landed state). 5 means landed, performing breath attack. 6 means landed, looking for a player for breath attack. 7 means landed, roar before beginning breath attack. 8 means charging player. 9 means flying to portal to die. 10 means hovering (flapping wings without moving) with no AI (default when using the /summon command).

Dragon fireballs have entity data associated with them that contain various properties.


 Entity data
Tags common to all entities
Tags common to all fireballs
Tags common to all projectiles

### Command details
A dragon fireball spawned by a command (left) and the damage and the explosion it caused (right).
In Java Edition, the /summon ender_dragon command, by default, summons a harmless ender dragon that hovers in place. Setting the DragonPhase tag (by issuing either the /summon ender_dragon ~ ~ ~ {DragonPhase:0} or the /data merge entity <selector> {DragonPhase:0} commands) starts the ender dragon's ordinary behavior, although the health bar does not appear because it is managed by the ender dragon fight status rather than by the dragon entity itself. If spawned away from the center of the map (x=0, z=0), it flies to the center then resumes normal behavior (see #Behavior).


