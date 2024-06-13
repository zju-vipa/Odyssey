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
| Ingredients             | Crafting recipe |
|-------------------------|-----------------|
| Stick+Smooth Stone Slab |                 |

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

| No. | Namespace ID                         | Redstone power | Image |
|-----|--------------------------------------|----------------|-------|
| 0   | animation.armor_stand.default_pose   | 0              |       |
| 1   | animation.armor_stand.no_pose        | 1              |       |
| 2   | animation.armor_stand.solemn_pose    | 2              |       |
| 3   | animation.armor_stand.athena_pose    | 3              |       |
| 4   | animation.armor_stand.brandish_pose  | 4              |       |
| 5   | animation.armor_stand.honor_pose     | 5              |       |
| 6   | animation.armor_stand.entertain_pose | 6              |       |
| 7   | animation.armor_stand.salute_pose    | 7              |       |
| 8   | animation.armor_stand.hero_pose      | 8, 13 or more  |       |
| 9   | animation.armor_stand.riposte_pose   | 9              |       |
| 10  | animation.armor_stand.zombie_pose    | 10             |       |
| 11  | animation.armor_stand.cancan_a_pose  | 11             |       |
| 12  | animation.armor_stand.cancan_b_pose  | 12             |       |

