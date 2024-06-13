# Shulker
A shulker is a box-shaped hostile mob found in end cities. It hides in its shell to protect itself and blend in with its surroundings, and attacks by shooting homing bullets that inflict Levitation. It is the only source of shulker shells, which are used to craft shulker boxes.

## Contents
- 1 Spawning
	- 1.1 Natural generation
	- 1.2 Post-generation
- 2 Drops
	- 2.1 On death
- 3 Behavior
	- 3.1 Shulker bullet
	- 3.2 Coloring
- 4 Transportation
- 5 Sounds
	- 5.1 Shulker
	- 5.2 Shulker bullet
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
		- 12.1.1 Open
		- 12.1.2 Closed
	- 12.2 Screenshots
	- 12.3 In other media
- 13 References
- 14 External links

## Spawning
### Natural generation
Shulkers spawn during the generation of end cities, which are located on the outer islands of the End. They usually spawn on the walls of the city and on end ships. They do not despawn naturally, even in Peaceful difficulty.

### Post-generation
There is a chance for a new shulker of the same color to spawn when a shulker is hit with a shulker bullet (including one of its own).

The following conditions need to be met:

- When the shulker gets hit and then has less than half its health remaining, there is a 25% chance for it to attempt teleportation without spawning a new shulker instead of checking the conditions below.
- The hit shulker must have its lid open.
- The hit shulker needs to find somewhere to teleport. For this, it takes a random block in a 17×17×17 cuboid centered on the shulker and then checks if the block has a valid face to teleport to. If not it proceeds to try this up to 4 more times. If no valid face is found, the attempt fails.
- Each other shulker within 8 blocks of the hit shulker decreases the odds of success by 20%. When five or more other shulkers are nearby, no shulkers spawn, but the hit shulker still teleports.

If the attempt succeeds a new shulker spawns where the old shulker was before it teleported.

## Drops
### On death
| Item |                   | Roll Chance | Quantity (Roll Chance) |            |            |             |
|------|-------------------|-------------|------------------------|------------|------------|-------------|
|      |                   |             | Default                | Looting I  | Looting II | Looting III |
|      | Shulker Shell(JE) | 50%–68.75%  | 1 (50%)                | 1 (56.25%) | 1 (62.5%)  | 1 (68.75%)  |
|      | Shulker Shell(BE) | 100%        | 0–1                    | 0–2        | 0–3        | 0–4         |

Shulkers also drop 5 when killed by a player or a tamed wolf.

## Behavior





The shell of the mob looks similar to a purpur block, blending in to its natural surroundings. Inside the shell of the mob is a small yellow head with two eyes. Spawning shulkers with other colors can be done using the /summon command, as detailed below.

Shulkers generally remain stationary, attached to an adjacent block with a full face.[1] However, if the block the shulker occupies becomes something other than air or the shulker finds itself not adjacent to any full face, or the shell cannot fully open (due to solid blocks or entities such as boats or other shulkers), it attempts to teleport (5 attempts per tick) to an air block within a 17×17×17 cube centered on the shulker where the shulker can attach to a full face and open. If it finds no valid position to teleport onto it does not move.

Shulkers evaluate the collision box of scaffolding based on their current position,[2] which can result in the shulker teleporting to a position only to find it invalid and teleport again.

Shulkers occasionally open their shell for 1–3 seconds. When a target comes within about 16 blocks, it opens fully and shoots guided projectiles that follow the shulker's target, called shulker bullets, moving only along the X, Y, or Z axes and leaving trails of white particles. The projectiles can be destroyed by attacking them or blocked with a shield. If the projectile hits an entity, it does 4 damage and inflicts the Levitation status effect for 10 seconds, this status effect has no effect underwater[3]‌[Java Edition  only], or while riding a mob. The shulker continues firing every 1–5.5 seconds while the target remains in range. If the shulker's target dies with projectiles still in flight, they fall to the ground.

Shulkers can attack each other, in which case they shoot fully guided bullets at each other, but are unaffected by Levitation when hit. The normal teleportation habits apply during these battles, and is likely to result in the duplication of more shulkers.

When its shell is closed, a shulker has 20 ( × 10) armor points and deflects arrows. When the shell opens, it loses this natural armor and takes damage as normal. When at less than half health, a shulker has a 25% chance of teleporting (as described above) after taking damage. When a shulker is attacked, other shulkers in the area target the attacker as well.

Shulkers don't take burning damage from lava or fire. They drown in water, but try to teleport away when water or lava flows into the block they occupy.

In Peaceful difficulty, shulkers exist within the world, but do not attack,[4] like piglins and hoglins in Bedrock Edition.

Shulkers are treated differently than true blocks. For example, mobs are unable to pathfind around[5] or jump over them,[6] and falling on them from a height does not produce particles.[7] Their spawn egg also does not destroy blocks such as grass.[8]

In Bedrock Edition, they apply Levitation II instead of I.

Gravity-affected blocks break when falling onto a shulker.

### Shulker bullet
| Hitbox size | Height: 0.3125 blocksWidth: 0.3125 blocks |
|-------------|-------------------------------------------|

{
    "title": "Shulker bullet",
    "rows": [
        {
            "field": "Height: 0.3125 blocks<br>Width: 0.3125 blocks",
            "label": "(link to Hitbox article, displayed as Hitbox size)"
        }
    ],
    "invimages": [],
    "images": [
        "Shulker Bullet.png"
    ]
}
A shulker bullet is a guided projectile that is shot from shulkers. They follow the targeted entity along the X, Y, or Z axis and leave trails of white particles. A shulker bullet that hits a mob or player deals damage and affects them with Levitation for ten seconds.

The shulker's projectiles also have entity data that control its movement.

The bullet can be destroyed by hitting it with any item, shooting it with an arrow, or blocking it with a shield. It is also destroyed upon contact with a block or lava.

### Coloring
In Bedrock Edition, shulkers can be dyed in a similar fashion to sheep. Using a dye on a shulker gives it the color of the dye. They can be dyed only in Creative mode.

In Java Edition, the color of a shulker is changed through commands using the color byte tag.

## Transportation
A shulker is transported in the Overworld by boat. Pistons raise the boat uphill.
Shulkers can be moved by boats or minecarts; pushing a boat/cart into a shulker causes it to board. A boat's sides block some of a shulkers projectiles.

A shulker pushed through the exit portal gets transported to the world spawn point in the Overworld. Since shulkers teleport when not adjacent to a solid block, they must be pushed down the central pillar of the exit portal (or a manually placed block directly above the portal) with a piston. Alternatively, if a shulker is in a boat that has been ridden into the exit portal, it is possible to break the boat with an arrow shot at the boat. This causes the shulker to go through the exit portal. When riding the shulker into the exit portal by a boat, the boat becomes "submerged" in the portal fluid and exiting the boat causes the player to go through the exit portal.

## Data values
### ID
Java Edition:

| Name           | Identifier       | Entity tags          | Translation key                   |
|----------------|------------------|----------------------|-----------------------------------|
| Shulker        | `shulker`        | `fall_damage_immune` | `entity.minecraft.shulker`        |
| Shulker Bullet | `shulker_bullet` | None                 | `entity.minecraft.shulker_bullet` |

Bedrock Edition:

| Name           | Identifier       | Numeric ID | Translation key              |
|----------------|------------------|------------|------------------------------|
| Shulker        | `shulker`        | `54`       | `entity.shulker.name`        |
| Shulker Bullet | `shulker_bullet` | `76`       | `entity.shulker_bullet.name` |

### Entity data
Java Edition:

Main article: Entity format
Shulkers have entity data associated with them that contains various properties.

- Entity data
	- 
	- Tags common to all entities
	- 
	- Tags common to all mobs
	- Bullets fires by a shulker areprobablyfir
	- APX: Approximate X coordinate.
	- APY: Approximate Y coordinate.
	- APZ: Approximate Z coordinate.
	- AttachFace: Which face of its block the shulker is attached to. The shulker also opens in the direction going from the center of the block to that face when the shulker opens up.0bmeans the the top face.1bmeans the the bottom face.2bmeans the the north face.3bmeans the the south face.4bmeans the the west face.5bmeans the the east face.
	- Color: The color of the shulker. Default is 0. Shulkers spawned by eggs or as part of End cities have value 16.
		- SeeShulker/DVfor color table.
	- Peek: "Height" of the head of the shulker.
		- This "height" is measured in pixels from the bottom of the shulker, where 1 pixel = 1/16th of a block.[more information needed]
		- This "height" goes in the direction that the shulker is facing according toAttachFace.[more information needed]


Shulker color
Main article: Shulker/DV[edit]

Shulker bullets have entity data associated with them that contains various properties.

- Entity data
	- 
	- Tags common to all entities
	- 
	- Tags common to all projectiles
	- Steps: How many "steps" it takes to attack to the target. The higher it is, the further out of the way the bullet travels to get to the target. If set to 0, it makes no attempt to attack the target and instead uses TXD/TYD/TZD in a straight line.
	- Target: TheUUIDof the target of this shulker bullet, stored as four ints.
	- TXD: The offset in the X direction to travel in accordance with its target.
	- TYD: The offset in the Y direction to travel in accordance with its target.
	- TZD: The offset in the Z direction to travel in accordance with its target.


Bedrock Edition:

SeeBedrock Edition level format/Entity format.
