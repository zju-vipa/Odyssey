# Ghast
Ghasts are large, floating, ghost-like hostile mobs found in the Nether. Ghasts wander aimlessly and shoot explosive fireballs at players, which can be hit back to kill them instantly upon direct impact.

## Contents
- 1 Spawning
- 2 Drops
	- 2.1 On death
- 3 Behavior
	- 3.1 Fireball
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
	- 11.1 Screenshots
	- 11.2 In other media
- 12 References
- 13 External links

## Spawning
To spawn naturally, a ghast requires a solid block below it and a free space 5×5 blocks wide and 4 blocks high. They spawn only in the basalt deltas, nether wastes, and soul sand valley biomes (all three of which exist only in the Nether dimension), and in any light level. In Java Edition, ghasts cannot spawn in soul sand valleys if another ghast is within 16 blocks of spherical distance to the intended spawning location. In Bedrock Edition, two ghasts can spawn within any 4 chunk span.

Ghasts do not spawn in nether fortresses, but they can wander nearby.

## Drops
### On death
| Item |            | Roll Chance | Quantity (Roll Chance) |           |            |             |
|------|------------|-------------|------------------------|-----------|------------|-------------|
|      |            |             | Default                | Looting I | Looting II | Looting III |
|      | Ghast Tear | 100%        | 0–1                    | 0–2       | 0–3        | 0–4         |
|      | Gunpowder  | 100%        | 0–2                    | 0–3       | 0–4        | 0–5         |

- 5 when killed by the player.

## Behavior
Ghasts float around with their eyes and mouth closed and periodically make crying sounds heard from up to 80 blocks away. They have a hitbox of 4×4×4 blocks. The ghast's nine tentacles are not within their hitbox.

When within range, a ghast faces the player and shoots a fireball every 3 seconds, opening its eyes and mouth and making a screeching sound. A ghast requires a line of sight to the player before firing, which can be blocked by any solid block including transparent blocks. In Java Edition, they target players within 64 blocks horizontally and 4 blocks vertically[1], and continue attacking as long as they are within a 64 block sphere and have line of sight. In Bedrock Edition, a ghast normally targets a player within a sphere of 28 blocks, increasing to 64 blocks if the player damages it. in Bedrock Edition, a ghast holds its charge like a pillager when its target gets lost of its sight and shoots again instantly when in range.[2]

Ghasts do not attempt to approach the player once aggravated, but instead fire at the player from their position within firing range. If a ghast is within close range to its target, it may take damage from the explosion of its own fireball, regardless of the player hitting the fireball back.

Ghasts can provoke other mobs into targeting them, but in Java Edition they do not target other mobs, only the player.

Ghasts are immune to fire and lava damage. They are slowed by lava, occasionally sinking into it or passing through lava falls, making them immobilized and more vulnerable to ranged attacks for some time.

Despite their ghostly appearance, ghasts are not considered undead mobs.[3] This means they can drown,[4] are damaged by Instant Damage[5] and healed by Instant Health, are affected by Regeneration and Poison,[6] and are not affected by Smite.[7] Despite this, Withers never deliberately target them[8], and they are the only non-undead mob ignored by the Wither (excluding Agents‌[BE & edu  only], and mobs with the invulnerable NBT tag). They are also completely ignored by wolves, "Johnny" vindicators, goats, snow golems, trusting foxes and zoglins.

Despite being flying mobs, ghasts can destroy turtle eggs when on top of them.[9]


Fireball




Hitbox size


Height:JE: 1 BlockBE: 0.31 blocksWidth:JE: 1 BlockBE: 0.31 blocks 




{
    "title": "Fireball",
    "rows": [
        {
            "field": "'''Height:'''<br>'''(link to Java Edition article, displayed as JE):''' 1 Block<br>'''(link to Bedrock Edition article, displayed as BE):''' 0.31 blocks<br>'''Width:'''<br>'''(link to Java Edition article, displayed as JE):''' 1 Block<br>'''(link to Bedrock Edition article, displayed as BE):''' 0.31 blocks",
            "label": "(link to Hitbox article, displayed as Hitbox size)"
        }
    ],
    "invimages": [],
    "images": [
        "Fire Charge.png"
    ]
}
### Fireball
Main article: Fireball
Ghasts shoot fireballs at players, dealing damage to entities and creating an explosion that sets fire to nearby blocks upon impact. Blocks with blast resistance as low as 3.5 survive a fireball's explosion.

Hitting a fireball with another projectile or a melee attack deflects it, killing any ghast hit directly by it.


## Data values
### ID
Java Edition:

| Name  | Identifier | Entity tags        | Translation key        |
|-------|------------|--------------------|------------------------|
| Ghast | ghast      | fall_damage_immune | entity.minecraft.ghast |

Bedrock Edition:

| Name  | Identifier | Numeric ID | Translation key   |
|-------|------------|------------|-------------------|
| Ghast | ghast      | 41         | entity.ghast.name |

### Entity data
Java Edition:

Main article: Entity format
Ghasts have entity data associated with them that contains various properties.


 Entity data
Tags common to all entities
Tags common to all mobs
 ExplosionPower: The radius of the explosion created by the fireballs the ghast fires. Default value is 1.


Bedrock Edition:

See Bedrock Edition level format/Entity format.

