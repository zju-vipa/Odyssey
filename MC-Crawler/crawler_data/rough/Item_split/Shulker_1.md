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

