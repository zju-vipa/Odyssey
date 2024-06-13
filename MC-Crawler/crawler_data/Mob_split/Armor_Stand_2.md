### Invisible and marker armor stands

  

This feature is exclusive to  Java Edition. 


An invisible armor stand (left) and a marker armor stand with no base plate (right) in Spectator mode.
In Java Edition, armor stands can be made invisible or used as markers by setting the NBT tags {Invisible: 1b} or {Marker: 1b} respectively. Both invisible[14] and marker armor stands are invulnerable to all attacks, including explosions and players in Creative mode; they can be removed only using the /kill command. Mobs ignore invisible and marker armor stands.[15]

Invisible armor stands still render any equipped items, they have a hitbox and can be interacted with by players in any game mode. Similar to mobs affected by the Invisibility effect, invisible armor stands can only be seen by players in Spectator mode, players in the same team as the invisible armor stand, or if the stand has the Glowing effect.

Marker armor stands are unaffected by physics (gravity, knockback, flowing water, pistons, etc). They have a hitbox size of 0, meaning that players and dispensers cannot interact with them. Due to the lack of a hitbox, it is possible to place blocks in the space visually occupied by a marker armor stand, or target blocks and entities behind it.

## Data values
### ID
Java Edition:

| Armor Stand | Identifier  | Form | Translation key            |
|-------------|-------------|------|----------------------------|
| Item        | armor_stand | Item | item.minecraft.armor_stand |

| Armor Stand | Identifier  | Entity tags             | Translation key              |
|-------------|-------------|-------------------------|------------------------------|
| Entity      | armor_stand | can_breathe_under_water | entity.minecraft.armor_stand |

Bedrock Edition:

| Armor Stand | Identifier  | Numeric ID | Form | Translation key       |
|-------------|-------------|------------|------|-----------------------|
| Item        | armor_stand | 552        | Item | item.armor_stand.name |

| Armor Stand | Identifier  | Numeric ID | Translation key         |
|-------------|-------------|------------|-------------------------|
| Entity      | armor_stand | 61         | entity.armor_stand.name |

### Item data
Java Edition:

Main article: Item format

 tag: The item's tag tag.
 EntityTag: Stores entity data that is applied to the entity when created.
See Entity Format.

Bedrock Edition:

In Bedrock Edition, armor stands have no additional item tag.
See Bedrock Edition level format/Item format.
### Entity data
Armor stands have entity data associated with them that contain various properties of the entity.

Java Edition:

Main article: Entity format

 Entity data
Tags common to all entities
Tags common to mobs except LeftHanded, DeathLootTable, DeathLootTableSeed, NoAI, Leash, CanPickUpLoot and PersistenceRequired.
Tags common to all mobs
 DisabledSlots: Bit field allowing disable place/replace/remove of armor elements. For example, the value 16191 or4144896 disables placing, removing and replacing of all equipment. These can be found using the bitwise OR operator.
 Invisible: 1 or 0 (true/false) - if true, ArmorStand is invisible, although items on it still display.
 Marker: 1 or 0 (true/false) - if true, ArmorStand's size is set to 0, has a tiny hitbox, and disables interactions with it. May not exist.
 NoBasePlate: 1 or 0 (true/false) - if true, ArmorStand does not display the base beneath it.
 Pose: Rotation values for the ArmorStand's pose.
 Body: Body-specific rotations.
: x-rotation.
: y-rotation.
: z-rotation.
 Head: Head-specific rotations.
: x-rotation.
: y-rotation.
: z-rotation.
 LeftArm: Left Arm-specific rotations.
: x-rotation.
: y-rotation.
: z-rotation.
 LeftLeg: Left Leg-specific rotations.
: x-rotation.
: y-rotation.
: z-rotation.
 RightArm: Right Arm-specific rotations.
: x-rotation.
: y-rotation.
: z-rotation.
 RightLeg: Right Leg-specific rotations.
: x-rotation.
: y-rotation.
: z-rotation.
 ShowArms: 1 or 0 (true/false) - if true, ArmorStand displays full wooden arms. If false, also place and replace interactions with the hand item slot are disabled.
 Small: 1 or 0 (true/false) - if true, ArmorStand is much smaller, similar to the size of a baby zombie.

| Binary | Integer number | Result                                       |
|--------|----------------|----------------------------------------------|
| 2^0    | 1              | Disable adding or changing mainhand item     |
| 2^1    | 2              | Disable adding or changing boots item        |
| 2^2    | 4              | Disable adding or changing leggings item     |
| 2^3    | 8              | Disable adding or changing chestplate item   |
| 2^4    | 16             | Disable adding or changing helmet item       |
| 2^5    | 32             | Disable adding or changing offhand item      |
| 2^8    | 256            | Disable removing or changing mainhand item   |
| 2^9    | 512            | Disable removing or changing boots item      |
| 2^10   | 1024           | Disable removing or changing leggings item   |
| 2^11   | 2048           | Disable removing or changing chestplate item |
| 2^12   | 4096           | Disable removing or changing helmet item     |
| 2^13   | 8192           | Disable removing or changing offhand item    |
| 2^16   | 65536          | Disable adding mainhand item                 |
| 2^17   | 131072         | Disable adding boots item                    |
| 2^18   | 262144         | Disable adding leggings item                 |
| 2^19   | 524288         | Disable adding chestplate item               |
| 2^20   | 1048576        | Disable adding helmet item                   |
| 2^21   | 2097152        | Disable adding offhand item                  |

Bedrock Edition:

See Bedrock Edition level format/Entity format.

