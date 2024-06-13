### Bedrock Edition
Upon noticing a player or mob, the wither flies to a random location and hovers in place. It shoots 3 black wither skulls and one blue wither skull before flying to another location. The time between each shot decreases as the wither loses health. On Normal difficulty or higher, if the wither has targeted an entity but cannot find a location to pathfind to, it shoots random blue skulls in a random direction along with the skulls directed toward the target.

At half health, it causes a large explosion that spawns 3 wither skeletons (except on Easy difficulty), as well as gaining wither armor. Instead of flying to a random location, it dashes toward its target, destroying blocks and damaging mobs in its path. It continues firing skulls as normal but dashes every second burst.

The wither's dash ability breaks all blocks in a 6x8x6 volume around it, rounded to the south-east if required. Despite the wither being able to destroy obsidian with blue skulls, the wither cannot dash through it.

It has different spawn and death animations, both of which involve the wither exploding. Wither roses always drop as an item when the wither kills a mob. Wither roses are dropped even when the game rule doMobLoot is set to false.[4] The wither rose inflicts the Wither effect for a couple of seconds when stepped on.

The sky light level drops to 11 and dark clouds appear from the moment the wither spawns until it is dead, preventing bogged, drowned, phantoms, skeletons, strays, zombies and zombie villagers from burning in sunlight.

On Easy difficulty, the wither does not inflict the wither effect or summon wither skeletons.

A wither retains its anti-projectile armor after healing it over 1/2 of its total HP, though it disappears after the game is restarted.[5]

## Wither Skull
Not to be confused with Wither Skeleton Skull.

| Hitbox size | Height: 0.3125 blocksWidth: 0.3125 blocks |
|-------------|-------------------------------------------|

{
    "title": "Wither Skull",
    "rows": [
        {
            "field": "Height: 0.3125 blocks<br>Width: 0.3125 blocks",
            "label": "(link to Hitbox article, displayed as Hitbox size)"
        }
    ],
    "invimages": [],
    "images": []
}
When attacking, the wither rapidly fires explosive projectiles called wither skulls, which look like its own heads, at its target. There are two types of wither skulls: a fast-moving black one, and a slower blue one.

- Black wither skulls explode with a blast power of 1, the same as aghast's fireball, and cannot break blocks with ablast resistanceabove 4.
- Blue wither skulls have the same explosion strength, but move slower and are more destructive to terrain. They break all breakable blocks (exceptreinforced deepslate), such asobsidian,ancient debrisandblocks of netherite. Blue skulls are able to destroywaterandlavasource blocks, but cannot break unbreakable blocks likebedrockandend portal frames. InMinecraft Education, blue wither skulls deal increased damage, but with the same explosion radius.

If either type of wither skull hits a player or mob, it does 8 damage on Normal difficulty. It also inflicts Wither II for 10 seconds on Normal difficulty and 40 seconds on Hard, which turns the player's hearts black () and drains health, similarly to Poison. However, unlike Poison, it can kill the player.

Like other status effects, the Wither effect can be cured by drinking milk.

In Bedrock Edition and Legacy Console Edition, the blue skull can be deflected by hitting it with an empty hand, weapon, tool, or throwable projectiles such as tridents, arrows, snowballs, and throwable potions.

## Data values
### ID
Java Edition:

| Name         | Identifier     | Entity tags                                                                                                                                                                          | Translation key                 |
|--------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------|
| Wither       | `wither`       | `can_breathe_under_water`<br/>`fall_damage_immune`<br/>`freeze_immune_entity_types`<br/>`ignores_poison_and_regen`<br/>`inverted_healing_and_harm`<br/>`undead`<br/>`wither_friends` | `entity.minecraft.wither`       |
| Wither Skull | `wither_skull` | `impact_projectiles`                                                                                                                                                                 | `entity.minecraft.wither_skull` |

Bedrock Edition:

| Name         | Identifier               | Numeric ID | Translation key                      |
|--------------|--------------------------|------------|--------------------------------------|
| Wither       | `wither`                 | `52`       | `entity.wither.name`                 |
| Wither Skull | `wither_skull`           | `89`       | `entity.wither_skull.name`           |
| Wither Skull | `wither_skull_dangerous` | `91`       | `entity.wither_skull_dangerous.name` |

### Entity data
Java Edition:

Main article: Entity format
Withers have entity data associated with them that contain various properties.

- Entity data
	- 
	- Tags common to all entities
	- 
	- Tags common to all mobs
	- Invul: The number of ticks of invulnerability left after being initially created. 0 once invulnerability has expired.

Wither skulls have entity data associated with them that contain various properties.

- Entity data
	- 
	- Tags common to all entities
	- 
	- Tags common to all fireballs
	- 
	- Tags common to all projectiles
	- dangerous[note 1]: 1 or 0 (true/false) - if true, the wither skull renders as blue, moves more slowly, and ignores the hardness values of most blocks upon exploding.

1. ↑Although blue wither skulls have existed since 12w37a, this field was not present until 23w41a.[6]


Bedrock Edition:

SeeBedrock Edition level format/Entity format.

