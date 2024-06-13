### Cauldrons
Main article: Cauldron § Holding potions
In Bedrock Edition, arrows can be used on cauldrons that contain potions to create tipped arrows.

## Behavior




Technical information related to the arrow entity has been checked in Java Edition and might differ in Bedrock Edition.



Arrow




Hitbox size


Height: 0.5 blocksWidth: 0.5 blocksEye Height: 0.13 blocks 




{
    "title": "Arrow",
    "rows": [
        {
            "field": "Height: 0.5 blocks<br>Width: 0.5 blocks<br>Eye Height: 0.13 blocks",
            "label": "(link to Hitbox article, displayed as Hitbox size)"
        }
    ],
    "invimages": [],
    "images": [
        "Arrow.png"
    ]
}
### Spawning
An arrow entity spawns when an arrow item is shot out of a bow, crossbow, dispenser, or a bow- or crossbow-wielding mob. Arrow entities spawn with a starting velocity calculated using the following process:

- The direction of the velocity is set as the facing vector of the entity that shot it, or the vector pointing straight out of a dispenser.
- The magnitude of the velocity is set as 0 to 3 for bows depending on how far they're drawn, 3.15 for crossbows, and 1.1 for dispensers.
- A random vector is added to the previously determined velocity. This vector ranges from−0.0172275⋅inaccuracyto0.0172275⋅inaccuracyon every axis. Inaccuracy is 1 for bows and crossbows, and 6 for dispensers.

Because crossbows shoot slightly faster arrows than bows but have the same inaccuracy, crossbows can feel more accurate; Their randomness is smaller in proportion to their total velocity.

### Movement
An arrow entity follows this list of steps in order when calculating its movement each game tick:

- If it is intersecting a block's collision box, itsinGroundNBT value is set to true.
- If it is on fire and in rain, water, or powder snow (including cauldrons containing water or powder snow), its fire is extinguished.


If inGround is true: 

If it is no longer intersecting a block's collision box:
inGround is set to false.
Its velocity in each axis is multiplied by a random number from 0 to 0.2.
Otherwise, it ticks its despawn timer.

- IfinGroundis false:


It calculates collisions with blocks and entities: 

It sets its target position to its current position plus its velocity.
It performs a raycast from its current position to the target position, checking for blocks to hit. If the raycast hits a block, the target position gets set to the point that was hit.
It performs a raycast from its position to the target position, checking for entities to hit.

If a block was found and no entity was found, handle effects from block collision: 

The block is activated, if applicable. For example, targets and wooden buttons are activated here.
The arrow's velocity is set to the target position minus the arrow position.
The arrow is moved directly away from the target position by 0.05 blocks
inGround is set to true.
crit is set to false.
PierceLevel is set to 0.


If any entity was found, handle effects from entity collision: 

If the entity is an Enderman, it is skipped.
The arrow will attempt to damage the entity. See the Damage section for more information. If the damage fails:
If the entity has the deflects_projectiles tag, the arrow's velocity will be rotated a random angle about the Y axis and scaled by 0.5.
Otherwise, its velocity is multiplied by -0.1.


Its velocity vector is added to its position vector.
Its velocity vector is multiplied by 0.99 if it's in air or 0.6 if it's in water (this is the "drag").
0.05 is subtracted from its velocity vector's y component (this is the "gravity").
The arrow movement (when not stuck in a block) can be solved as a recurrence relation to obtain the following formulas:

Vt→=0.99t⋅(V0→+[050])−[050]

Pt→=P0→+100⋅(1−0.99t)⋅(V0→+[050])−[05t0]

Where Vt→ is the velocity at tick t and Pt→ is the position at tick t. These formulas can quickly calculate the position and velocity at a future tick t given an initial position and velocity. To make them work for arrows in water instead, change 0.99 with 0.6 and 100 with 2.5.

### Damage
The damage an arrow inflicts on an entity depends on the damage NBT tag, the crit NBT tag, and the arrow's speed.

The damage NBT tag is determined by the item that shot it: It is 2 for everything except bows enchanted with Power, in which case it's 2.5+power level2.

The crit NBT tag is given to all arrows shot out of crossbows or fully charged bows.

The damage inflicted on an entity is damage NBT tag ⋅ speed, rounded up to a whole number. If the arrow has the crit NBT tag, it does an random amount of additional damage between 0 and damage2+2.

| Source        | Damage Tag | Crit Tag        | Starting Speed | Average Damage |
|---------------|------------|-----------------|----------------|----------------|
| Bow (Power I) | 3          | Yes             | 3±0.0172275    | 12.25× 6.125   |
|               |            | Bow (Power II)  | 3.5            | 14.75× 7.375   |
|               |            | Bow (Power III) | 4              | 16× 8          |
|               |            | Bow (Power IV)  | 4.5            | 18.5× 9.25     |
|               |            | Bow (Power V)   | 5              | 19.75× 9.875   |
|               |            | Bow             | 2              | 8.5× 4.25      |
|               |            | Crossbow        | 3.15±0.0172275 | 9.75× 4.875    |
|               | Dispenser  | No              | 1.1±0.103365   | 3.5× 1.75      |

