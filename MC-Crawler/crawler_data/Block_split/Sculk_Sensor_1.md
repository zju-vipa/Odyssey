### Redstone emission
Sculk sensors emit a redstone signal when they are activated. The strength of the redstone signal is inversely proportional to the distance the vibration signal traveled – the closer the vibration is to the sculk sensor, the stronger the redstone signal is, so it reaches the maximum redstone signal strength when the vibration is directly on top of the sensor.

#### Vibration frequencies

  

This section needs expansion. 
You can help by expanding it.Instructions: Bedrock Edition values


Each vibration in the game falls under a certain frequency value. This value can be measured with a comparator. With the right contraption, the player could detect if a certain action has occurred or is occurring nearby.

| Output | Vibration type       | Game event                     | Description                                                                                    |
|--------|----------------------|--------------------------------|------------------------------------------------------------------------------------------------|
| 1      | Step                 | minecraft:step                 | Player or entity steps                                                                         |
|        | Swim                 | minecraft:swim                 | Player or entity swims, boat paddles                                                           |
|        | Flap                 | minecraft:flap                 | Entity flaps (bat)                                                                             |
|        | Resonate 1           | minecraft:resonate_1           |                                                                                                |
| 2      | Projectile Land      | minecraft:projectile_land      | Projectile lands (snowball)                                                                    |
|        | Hit Ground           | minecraft:hit_ground           | Player or entity hits ground post-jump or fall                                                 |
|        | Splash               | minecraft:splash               | Player or entity splashes. Entity enters water or bubble column                                |
|        | Resonate 2           | minecraft:resonate_2           |                                                                                                |
| 3      | Item Interact Finish | minecraft:item_interact_finish | Item interaction (shield, spyglass, bone meal)                                                 |
|        | Projectile Shoot     | minecraft:projectile_shoot     | Projectile shoots (arrow, firework, etc.)                                                      |
|        | Instrument Play      | minecraft:instrument_play      | Goat horn plays                                                                                |
|        | Resonate 3           | minecraft:resonate_3           |                                                                                                |
| 4      | Entity Action        | minecraft:entity_action        | Entity roars (ravager), entity shakes (wolf after swimming), villager holds item, sniffer digs |
|        | Elytra Glide         | minecraft:elytra_glide         | Player glides                                                                                  |
|        | Resonate 4           | minecraft:resonate_4           |                                                                                                |
| 5      | Entity Dismount      | minecraft:entity_dismount      | Player dismounts                                                                               |
|        | Equip                | minecraft:equip                | Armor equipped in armor slot or stand                                                          |
|        | Resonate 5           | minecraft:resonate_5           |                                                                                                |
| 6      | Entity Mount         | minecraft:entity_mount         | Player mounts (horse)                                                                          |
|        | Entity Interact      | minecraft:entity_interact      | Player interaction with entity (breeding)                                                      |
|        | Shear                | minecraft:shear                | Sheep being sheared                                                                            |
|        | Resonate 6           | minecraft:resonate_6           |                                                                                                |
| 7      | Entity Damage        | minecraft:entity_damage        | Damage or death to entities (except armor stand)                                               |
|        | Resonate 7           | minecraft:resonate_7           |                                                                                                |
| 8      | Drink                | minecraft:drink                | Entity drinks                                                                                  |
|        | Eat                  | minecraft:eat                  | Entity eats                                                                                    |
|        | Resonate 8           | minecraft:resonate_8           |                                                                                                |
| 9      | Container Close      | minecraft:container_close      | Container (chest, shulker box, hopper) closes                                                  |
|        | Block Close          | minecraft:block_close          | Door, trapdoor, or fence gate closes                                                           |
|        | Block Deactivate     | minecraft:block_deactivate     | Block deactivation (piston, button, lever, pressure plate)                                     |
|        | Block Detach         | minecraft:block_detach         | Tripwire detachment                                                                            |
|        | Resonate 9           | minecraft:resonate_9           |                                                                                                |
| 10     | Container Open       | minecraft:container_open       | Container opens                                                                                |
|        | Block Open           | minecraft:block_open           | Door opens                                                                                     |
|        | Block Activate       | minecraft:block_activate       | Block activation                                                                               |
|        | Block Attach         | minecraft:block_attach         | Attachment of tripwire hook                                                                    |
|        | Prime Fuse           | minecraft:prime_fuse           | TNT or creeper activates                                                                       |
|        | Note Block Play      | minecraft:note_block_play      | Note block sounds                                                                              |
|        | Resonate 10          | minecraft:resonate_10          |                                                                                                |
| 11     | Block Change         | minecraft:block_change         | Block change (chiseled bookshelf, lectern)                                                     |
|        | Resonate 11          | minecraft:resonate_11          |                                                                                                |
| 12     | Block Destroy        | minecraft:block_destroy        | Block destruction                                                                              |
|        | Fluid Pickup         | minecraft:fluid_pickup         | Gathered fluid (water, honey bottle, powdered snow)                                            |
|        | Resonate 12          | minecraft:resonate_12          |                                                                                                |
| 13     | Block Place          | minecraft:block_place          | Block placement                                                                                |
|        | Fluid Place          | minecraft:fluid_place          | Fluid placement                                                                                |
|        | Resonate 13          | minecraft:resonate_13          |                                                                                                |
| 14     | Entity Place         | minecraft:entity_place         | Entity placement via spawn-egg, mob spawner, or evoker magic                                   |
|        | Lightning Strike     | minecraft:lightning_strike     | Lightning strikes                                                                              |
|        | Teleport             | minecraft:teleport             | Endermen, chorus fruit, shulker, or ender pearl teleportation                                  |
|        | Resonate 14          | minecraft:resonate_14          |                                                                                                |
| 15     | Entity Die           | minecraft:entity_die           | Armor stand dies, firework finishes                                                            |
|        | Explode              | minecraft:explode              | TNT, end crystal, bed/respawn anchor, or creeperexplodes                                       |
|        | Resonate 15          | minecraft:resonate_15          |                                                                                                |

#### Vibration resonance
When a sculk sensor detects a vibration, any adjacent block of amethyst will reemit a vibration on the same frequency that the sculk sensor detected.

