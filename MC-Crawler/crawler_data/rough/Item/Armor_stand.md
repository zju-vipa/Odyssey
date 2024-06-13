# Armor Stand
An armor stand is an inanimate mob-like entity that can wear armor. In Bedrock Edition, armor stands can also hold items and be posed without the need of commands.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
- 2 Usage
	- 2.1 Equipping armor
	- 2.2 Equipping items
	- 2.3 Dispensers
	- 2.4 Posing
	- 2.5 Naming
	- 2.6 Further customization
- 3 Behavior
	- 3.1 Armor
	- 3.2 Status effects
	- 3.3 Mob interactions
	- 3.4 Invisible and marker armor stands
- 4 Sounds
- 5 Data values
	- 5.1 ID
	- 5.2 Item data
	- 5.3 Entity data
- 6 Advancements
- 7 History
- 8 Issues
- 9 Trivia
- 10 Video
- 11 Gallery
	- 11.1 Renders
		- 11.1.1 Java Edition
		- 11.1.2 Bedrock Edition
		- 11.1.3 Poses
	- 11.2 Screenshots
- 12 References
- 13 External links

## Obtaining
### Breaking
An armor stand can be broken by quickly attacking it twice, dropping itself and any armor or item placed onto it. Players in Adventure mode cannot break armor stands.[1]

In Bedrock Edition, if an armor stand is killed by a harming potion while holding a totem of undying, then the armor stand revives instead of dropping the totem, as with any mob holding a totem of undying.

### Natural generation
Two armor stands are found in each taiga village outdoor armory, one equipped with an iron helmet, the other with an iron chestplate.

### Crafting
| Ingredients                  | Crafting recipe |
|------------------------------|-----------------|
| Stick+<br/>Smooth Stone Slab |                 |

## Usage
Players can use armor stands to hold armor, mob heads, carved pumpkins, and elytra, or other items and blocks if it has arms. The stand does not have a GUI, so players interact with it directly. Armor stands can be placed in 8 different orientations. Armor stands cannot be placed if there is not enough room (i.e. it is occupied by other entities or solid blocks).

Armor stands are entities, allowing them to be pushed by pistons, moved by flowing water, pulled with fishing rods, pushed by attacks that inflict knockback, and bounced by slime blocks.

### Equipping armor
Using armor on a stand places the armor in the appropriate slot; if the slot is already equipped with armor, the old armor is swapped with the armor held by the player. Pressing the use control on armor with a bare hand removes the armor and places it in the highlighted hotbar slot.

### Equipping items
In Bedrock Edition, armor stands have arms by default; in Java Edition, arms can be made visible only by setting the NBT tag {ShowArms: 1b} via commands or external editors. Pressing the use control on an armor stand with arms while holding a non-equippable item places it in its main hand. In Java Edition, shields are always placed in the off-hand instead. If the armor stand already holds an item, it is swapped with the item held by the player.

Items from an armor stand's main hand can be retrieved by pressing the use control in any empty spot in Java Edition, or from the chestplate zone, if empty, in Bedrock Edition. In Java Edition, items in the off-hand slot can be retrieved only if the main hand slot is empty; in Bedrock Edition items in the off-hand slot cannot be retrieved unless the armor stand is broken.

In Java Edition, commands can be used to equip items in an armor stand's hands even if its arms are not visible. 

### Dispensers
In Java Edition, dispensers can place armor stands. Dispensers ignore the normal placement rules of armor stands - this means they can place armor stands inside solid blocks, or if the needed space is occupied by other entities.

Armor, mob heads, carved pumpkins, or elytra can be automatically placed on armor stands with a dispenser. Unlike players, dispensers cannot swap armor or items already equipped on the armor stand. Additionally, dispensers can equip shields in an armor stand's off-hand, if it has arms; in Bedrock Edition, this is the only way to equip shields in the off-hand slot without using commands.

### Posing

  

This feature is exclusive to  Bedrock Edition. 


In Bedrock Edition, the pose of the armor stand can be changed by interacting with the armor stand (or pressing the Pose button on mobile devices) while sneaking, or by using a redstone signal. There are 13 possible poses.

| No. | Namespace ID                           | Redstone power | Image |
|-----|----------------------------------------|----------------|-------|
| 0   | `animation.armor_stand.default_pose`   | 0              |       |
| 1   | `animation.armor_stand.no_pose`        | 1              |       |
| 2   | `animation.armor_stand.solemn_pose`    | 2              |       |
| 3   | `animation.armor_stand.athena_pose`    | 3              |       |
| 4   | `animation.armor_stand.brandish_pose`  | 4              |       |
| 5   | `animation.armor_stand.honor_pose`     | 5              |       |
| 6   | `animation.armor_stand.entertain_pose` | 6              |       |
| 7   | `animation.armor_stand.salute_pose`    | 7              |       |
| 8   | `animation.armor_stand.hero_pose`      | 8, 13 or more  |       |
| 9   | `animation.armor_stand.riposte_pose`   | 9              |       |
| 10  | `animation.armor_stand.zombie_pose`    | 10             |       |
| 11  | `animation.armor_stand.cancan_a_pose`  | 11             |       |
| 12  | `animation.armor_stand.cancan_b_pose`  | 12             |       |

### Naming
Upside-down armor stands in Bedrock Edition
Using a renamed name tag on an armor stand gives it a custom name. In Java Edition, the name is not displayed by default,[2] while in Bedrock Edition it is displayed similarly to renamed mobs. In Java Edition, armor stands can also be given custom names by renaming them at an anvil. In Java Edition, a renamed armor stand keeps its custom name when broken. In Bedrock Edition, armor stands named "Dinnerbone" or "Grumm" turn upside-down.

### Further customization
Armor stands that have been customized with commands in Java Edition (from left to right: arms, no base plate, small, invisible, custom pose)
Commands, such as /item in Java Edition or /replaceitem in Bedrock Edition, can be used to give armor stands items that normally cannot be equipped in armor or hand slots. In maps heavily using command blocks, armor stands can be used to keep scoreboard objectives that are 'global' to the map, run commands, etc. 

In Java Edition, armor stands can be customized further to have arms, pose, disobey gravity, dual wield and other things by summoning them using /summon with customized NBT tags. For example, it is possible to create an armor stand with arms using the /summon command. It is also possible to change an armor stand without arms into a stand with arms by using the /data command. The commands are as follows:

- /data merge entity @e[type=armor_stand,sort=nearest,limit=1] {ShowArms:1}, which changes the nearest armor stand into an armor stand with arms.
- /summon minecraft:armor_stand ~ ~ ~ {ShowArms:1}, which summons a new armor stand with arms shown.
- /summon minecraft:armor_stand ~ ~ ~ {Rotation:[0.0f]}, which summons a new armor stand that faces a desired direction (dependent on changing "0.0f" to other numbers like "90.0f" or "180.0f", otherwise it faces the same way as a default armor stand).

Other examples of customization include removing the stone plate below the armor stand, or giving the armor stand a small size (roughly the same size and proportions as a baby zombie).

## Behavior
An armor stand affected by a night vision potion in Bedrock Edition
An armor stand being damaged by the Wither effect potion in Bedrock Edition
Because armor stands are entities, they obey gravity, allowing them to fall and rest on non-full blocks such as enchanting tables, snow layers and slabs. Armor stands can't be leashed and can't ride on boats, but in Bedrock Edition, they can sit on minecarts.

Armor stands wobble slightly when being hit by the player. They are not damaged by cacti and sweet berry bushes, but can be broken by arrows and tridents. An armor stand destroyed by an explosion or a firework rocket does not drop as an item. Armor stands in water and lava at the same time are not consumed by the lava.

Being living entities, armor stands can also have attributes added to them, and can be affected by effects.

Sculk catalysts blooms without spreading when an armor stand is destroyed.[3]

In Java Edition, summoning an armor stand with no health causes the death animation.[4]

Advancements count armor stands as mobs and they can be used for advancements such as adventure and arbalistic.

### Armor
Any armor on the stand drops when the stand is broken. Armor stands can display enchanted, trimmed, and all forms of dyed armor. The effects of most enchanted armor have no effect when on an armor stand, with three exceptions: 

- Frost Walkercreatesfrosted iceblocks onwateras usual if an armor stand is pushed with apiston, although results are inconsistent.[5][6][7]
- Depth Striderslows the movement of the armor stand when being pushed with water.
- InJava Edition, aplayermay take damage from hitting an armor stand that holds armor enchanted withThorns.[8]

### Status effects
In Bedrock Edition, armor stands can be affected by status effects.[9] They can be 'killed' by Harming and Decay splash/lingering potions, lava, fire, and campfires, and they play the player death sound and fall to their side and disappear, yielding no armor stand item. If an armor stand is equipped with an item or armor, that item or armor is considered as "naturally-spawned equipment" with an 8.5% chance of dropping when the armor stand "dies" from the Instant Damage or the Wither status effect. If the dropped item is any form of weapon, tool or armor, it drops in a badly damaged state because the game considers it as "naturally-spawned equipment".

In Java Edition, armor stands can be given status effects only via commands, as they ignore any effect source in regular gameplay (splash potions, area effect clouds, shulker bullets, etc).[10] Armor stands with status effects do not emit particles, and are immune to most effects except for Glowing, Levitation, and Slow Falling.

### Mob interactions
Zoglins, goats in Java Edition, and vindicators named Johnny in Bedrock Edition[11] attack armor stands, but the armor stand remains undamaged; pufferfish also inflate when an armor stand is nearby.[12] In Java Edition, tamed wolves attempt to attack armor stands if the player hits one or if the armor stand is wearing armor with Thorns enchantment and damages the player.[13] Statistics classify the armor stand as mobs if the player dies while hitting the armor stand with the thorns enchantment.

### Invisible and marker armor stands

  

This feature is exclusive to  Java Edition. 


An invisible armor stand (left) and a marker armor stand with no base plate (right) in Spectator mode.
In Java Edition, armor stands can be made invisible or used as markers by setting the NBT tags {Invisible: 1b} or {Marker: 1b} respectively. Both invisible[14] and marker armor stands are invulnerable to all attacks, including explosions and players in Creative mode; they can be removed only using the /kill command. Mobs ignore invisible and marker armor stands.[15]

Invisible armor stands still render any equipped items, they have a hitbox and can be interacted with by players in any game mode. Similar to mobs affected by the Invisibility effect, invisible armor stands can only be seen by players in Spectator mode, players in the same team as the invisible armor stand, or if the stand has the Glowing effect.

Marker armor stands are unaffected by physics (gravity, knockback, flowing water, pistons, etc). They have a hitbox size of 0, meaning that players and dispensers cannot interact with them. Due to the lack of a hitbox, it is possible to place blocks in the space visually occupied by a marker armor stand, or target blocks and entities behind it.

## Data values
### ID
Java Edition:

| Armor Stand | Identifier    | Form | Translation key              |
|-------------|---------------|------|------------------------------|
| Item        | `armor_stand` | Item | `item.minecraft.armor_stand` |

| Armor Stand | Identifier    | Entity tags               | Translation key                |
|-------------|---------------|---------------------------|--------------------------------|
| Entity      | `armor_stand` | `can_breathe_under_water` | `entity.minecraft.armor_stand` |

Bedrock Edition:

| Armor Stand | Identifier    | Numeric ID | Form | Translation key         |
|-------------|---------------|------------|------|-------------------------|
| Item        | `armor_stand` | `552`      | Item | `item.armor_stand.name` |

| Armor Stand | Identifier    | Numeric ID | Translation key           |
|-------------|---------------|------------|---------------------------|
| Entity      | `armor_stand` | `61`       | `entity.armor_stand.name` |

### Item data
Java Edition:

Main article: Item format
- tag: The item'stagtag.

- 
	- EntityTag: Stores entity data that is applied to the entity when created.
		- SeeEntity Format.

Bedrock Edition:

InBedrock Edition, armor stands have no additional item tag.
SeeBedrock Edition level format/Item format.
### Entity data
Armor stands have entity data associated with them that contain various properties of the entity.

Java Edition:

Main article: Entity format
- Entity data
	- 
	- Tags common to all entities
	- Tags common to mobs except LeftHanded, DeathLootTable, DeathLootTableSeed, NoAI, Leash, CanPickUpLoot and PersistenceRequired.
	- 
	- Tags common to all mobs
	- DisabledSlots: Bit field allowing disable place/replace/remove of armor elements. For example, the value16191or4144959disables placing, removing and replacing of all equipment. These can be found using the bitwise OR operator.
	- Invisible: 1 or 0 (true/false) - if true, ArmorStand is invisible, although items on it still display.
	- Marker: 1 or 0 (true/false) - if true, ArmorStand's size is set to 0, has a tiny hitbox, and disables interactions with it. May not exist.
	- NoBasePlate: 1 or 0 (true/false) - if true, ArmorStand does not display the base beneath it.
	- Pose: Rotation values for the ArmorStand's pose.
		- Body: Body-specific rotations.
			- : x-rotation.
			- : y-rotation.
			- : z-rotation.
		- Head: Head-specific rotations.
			- : x-rotation.
			- : y-rotation.
			- : z-rotation.
		- LeftArm: Left Arm-specific rotations.
			- : x-rotation.
			- : y-rotation.
			- : z-rotation.
		- LeftLeg: Left Leg-specific rotations.
			- : x-rotation.
			- : y-rotation.
			- : z-rotation.
		- RightArm: Right Arm-specific rotations.
			- : x-rotation.
			- : y-rotation.
			- : z-rotation.
		- RightLeg: Right Leg-specific rotations.
			- : x-rotation.
			- : y-rotation.
			- : z-rotation.
	- ShowArms: 1 or 0 (true/false) - if true, ArmorStand displays full wooden arms. If false, also place and replace interactions with the hand item slot are disabled.
	- Small: 1 or 0 (true/false) - if true, ArmorStand is much smaller, similar to the size of a baby zombie.

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

SeeBedrock Edition level format/Entity format.
