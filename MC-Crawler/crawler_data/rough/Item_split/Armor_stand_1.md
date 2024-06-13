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

