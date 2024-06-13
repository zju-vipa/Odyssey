## Gameplay
The objective of the game remains the same as regular Minecraft, where players can build virtual realities in a sandbox-like environment. However, MinecraftEdu also has the goal of an educational use to teach a variety of subjects. 

### Features
MinecraftEdu differs from the regular version in a variety of ways, such as a tutorial mode, teacher options and exclusive Blocks/items.

#### 
MinecraftEdu Blocks
These IDs are in the namespaced ID format, with their mcedu namespace omitted.

| Block                | Note                                                                                                                 | Namespaced ID        |
|----------------------|----------------------------------------------------------------------------------------------------------------------|----------------------|
| Information block    | When right clicked, it opens a menu with text that a teacher can write.                                              | `blockDialogMessage` |
| Spawn Block          | Defines the spawn of the world when placed by teacher. The last spawn block placed determines the spawn.             | `blockSpawnMP`       |
| Border block         | Used to define the area students can play in. Students cannot go over, under, or through it.                         | `blockBorder`        |
| Build allow block    | Allows students to build above the block even if the world is set to disallow building.                              | `blockBuildAllow`    |
| Build disallow block | Disallows students to build above the block even if the world is set to allow building.                              | `blockBuildDisallow` |
| Big sign             | A three block wide sign. When a sign is placed, it gives the player a choice if they would like a small or big sign. |                      |
| Information sign     | Decorative. Used to draw students' attention to important things.                                                    | `blockInfoSign`      |
| Foundation block     | Measures distance to other foundation blocks.                                                                        | `blockFoundation`    |
| Teleport Block       | Used to teleport large distances to the location you set in the world.                                               | `blockTeleport`      |
| Home Block           | Used to teleport players to their home.                                                                              | `blockHome`          |

| Block                | Namespaced ID            |
|----------------------|--------------------------|
| Number 0             | `edunumber_0`            |
| Number 1             | `edunumber_1`            |
| Number 2             | `edunumber_2`            |
| Number 3             | `edunumber_3`            |
| Number 4             | `edunumber_4`            |
| Number 5             | `edunumber_5`            |
| Number 6             | `edunumber_6`            |
| Number 7             | `edunumber_7`            |
| Number 8             | `edunumber_8`            |
| Number 9             | `edunumber_9`            |
| Add Symbol           | `edunumber_add`          |
| Subtract Symbol      | `edunumber_subtract`     |
| Divide Symbol        | `edunumber_divide`       |
| Multiply Symbol      | `edunumber_multiply`     |
| Equals Symbol        | `edunumber_equals`       |
| Over Symbol          | `edunumber_over`         |
| Less than Symbol     | `edunumber_lessthan`     |
| Decimal Dot Symbol   | `edunumber_decimaldot`   |
| Decimal Comma Symbol | `edunumber_decimalcomma` |
| Pi Symbol            | `edunumber_pi`           |

| Item            | Note                                                               | Namespaced ID        |
|-----------------|--------------------------------------------------------------------|----------------------|
| Block Inspector | Displays the name of the block the player is looking at on screen. | `itemBlockInspector` |

#### 
##### Teacher options
(Can open by pressing M. On older versions, it can be opened by pressing P.)

| Image | Option                   | Description                                                                                                                                                                                         |
|-------|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|       | Spectate Mode            | When enabled, the player is invisible to others.                                                                                                                                                    |
|       | Creative Mode (Self)     | When enabled, double-tap space to fly, unlimited blocks in inventory, destroy blocks instantly.                                                                                                     |
|       | Movement speed           | Adjust how fast the player walks or flies.                                                                                                                                                          |
|       | Gamemode                 | MinecraftEdu, Survival and Creative                                                                                                                                                                 |
|       | Difficulty               | Peaceful, Easy, Normal, Hard                                                                                                                                                                        |
|       | Allow Fire & TNT         | When enabled, fire can burn objects and spread, TNT can detonate and explode.                                                                                                                       |
|       | Allow Weather Effects    | When enabled, rain and snow storms may occur randomly.                                                                                                                                              |
|       | Generate Structures      | When enabled, structures and buildings are created when world is being generated.                                                                                                                   |
|       | Allow Other Dimensions   | When enabled, players can travel to other dimensions like nether and the end.                                                                                                                       |
|       | Allow Animals            | When enabled, peaceful animals spawn.                                                                                                                                                               |
|       | Allow Villagers          | When enabled, villagers spawn.                                                                                                                                                                      |
|       | Allow Monsters           | When enabled, monsters are generated and may attack players.                                                                                                                                        |
|       | Enable PvP               | When enabled, players can engage in combat with and injure one another.                                                                                                                             |
|       | Allow Student Respawning | When enabled, students can teleport themselves back to the spawn location using a button on the student menu.                                                                                       |
|       | Allow Student Surfacing  | When enabled, students can teleport themselves to back to the surface directly above their heads using a button on student menu.                                                                    |
|       | Students Can Build       | When enabled, students can place or destroy blocks anywhere except on top of Build Disallow Blocks.                                                                                                 |
|       | Freeze Students          | When enabled, students cannot move, destroy blocks or place blocks.                                                                                                                                 |
|       | Mute Students            | When enabled, students cannot use the in-game chat.                                                                                                                                                 |
|       | Keep Inventory           | When enabled, users don't lose their inventory content on death.                                                                                                                                    |
|       | Students Can Always Fly  | When enabled, students can fly in any gamemode.                                                                                                                                                     |
|       |                          |                                                                                                                                                                                                     |
|       |                          |                                                                                                                                                                                                     |
|       |                          |                                                                                                                                                                                                     |
|       |                          |                                                                                                                                                                                                     |
|       | Build Mode               | When enabled, the player can fly with precise movement control and can move through solid blocks                                                                                                    |
|       | Long Distance Building   | When enabled, the player place/dig blocks up to 60 blocks away.                                                                                                                                     |
|       | Fill/Clear tool          | When enabled, the player can place two blocks in opposite corners to completely fill the defined area with that block and hold nothing in their hands and right-click the corners to clear an area. |
|       | Place Amount             | Set how many blocks are placed in a column when the player places blocks.                                                                                                                           |
|       | Dig Amount               | Set how many blocks are destroyed in a column when the player dig blocks.                                                                                                                           |
|       | Undo Last Fill           | Reverts the most recent fills.                                                                                                                                                                      |
|       | Undo Last Place          | Reverts the most recent blocks placed.                                                                                                                                                              |
|       | Undo Last Dig            | Reverts the most recent blocks destroyed.                                                                                                                                                           |

