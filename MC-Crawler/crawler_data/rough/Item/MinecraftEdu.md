# MinecraftEdu
MinecraftEdu is a fork of Java Edition developed by TeacherGaming, published by E-Line Media and licensed by Mojang Studios.[2] It was meant as an educational version of Minecraft.

In the beginning, MinecraftEdu was developed by TeacherGaming, consisting of three developers and three teachers, located in the United States and Finland. Later, TeacherGaming expanded into a team of eight.

MinecraftEdu focuses on allowing the player to explore, interact with, and modify a dynamically-generated map made of one-cubic-meter-sized blocks. In doing so the student with the help of the teacher is supposed to learn a variety of subjects. The teacher can change settings to define where students can place and destroy blocks and the world used on the server.

On January 19, 2016, Mojang announced that they would be acquiring MinecraftEdu from TeacherGaming. At the same time, a new educational version of the game was announced: Minecraft: Education Edition (later renamed to Minecraft Education) has since launched to schools around the world.[3]

## Contents
- 1 Purchase and availability
	- 1.1 Hardware requirements
	- 1.2 Discontinuation
- 2 Development
	- 2.1 History of MinecraftEdu
- 3 Gameplay
	- 3.1 Features
		- 3.1.1 Blocks / Items
		- 3.1.2 Options/ Menus
			- 3.1.2.1 Teacher options
		- 3.1.3 Tutorial mode
		- 3.1.4 Mods
		- 3.1.5 Skins
- 4 Trailers
- 5 Gallery
- 6 External links
- 7 References

## Purchase and availability
MinecraftEdu could be purchased for US$18 per student (24 or less) or US$14 (25 or more) for the User license and US$41 for the server license. The server license could be bought as a one-time purchase. Once purchased, the game could be played by downloading the launcher. MinecraftEdu Hosting Beta was also available for US$20/month and did not require the user to pay the server software license again.

### Hardware requirements
According to http://minecraftedu.com/faq#question_2-13 and https://help.mojang.com/customer/portal/articles/325948-minecraft-system-requirements:

Minimum Requirements:

- A Windows, macOS, or Linux computer (desktop or laptop)
- 2 GB of RAM or greater
- Intel Pentium D, AMD Athlon or greater processor
- 200MB free hard disk space or more
- Java 6 Release 45 or later (including Java 7 and 8)

Recommended Requirements:

- CPU: Intel Core i3 or AMD Athlon II (K10) 2.8 GHz
- RAM: 4 GB
- GPU: GeForce 2xx Series or AMD Radeon HD 5xxx Series (Excluding Integrated Chipsets) with OpenGL 3.3
- HDD: 1 GB
- Latest release of Java 8 from java.com

Software Requirements:

- MinecraftRelease 1.6 or newer. Older versions must be updated to current versions
- Please note that some users experience issues playingMinecraftwhile using a mismatched version of Java for their operating system (32-bit or 64-bit), while using certain versions of Java 7, or while multiple versions of Java are installed.

### Discontinuation
As of April 5, 2016, MinecraftEdu is no longer for sale. However, customers that have already purchased MinecraftEdu licenses may continue to use MinecraftEdu. Since then, MinecraftEdu no longer receives new updates from TeacherGaming, and Mojang no longer supports MinecraftEdu. Worlds built in MinecraftEdu cannot be ported over to Minecraft Education.[4]

## Development
MinecraftEdu development has continued on a daily basis since it first launched in 2011. New features and fixes are being actively published. All current and future updates are included in the cost. Changes to the software can be viewed on the Changelog page.

The developers behind MinecraftEdu are Aleksi Postari and Toni Paavola You can follow them on Twitter for more information. Also stop by the development blog to read about how things are going.

### History of MinecraftEdu
| Time           | TeacherGaming LLC.                                                    | MinecraftEdu                                                                                |
|----------------|-----------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| Spring 2010    | SCGroup OY was founded                                                |                                                                                             |
| February 2011  | First contact with Mojang AB                                          |                                                                                             |
| June 2011      | Contact with Joel Levin                                               | The development of MinecraftEdu began                                                       |
| August 2011    | MinecraftEdu's sales calls for Finnish schools began                  |                                                                                             |
| September 2011 | Toni Paavola started training                                         |                                                                                             |
| October 2011   | The first MinecraftEdu licenses were sold                             |                                                                                             |
| November 2011  | TeacherGaming LLC was formed.Contact Carnegie from Mellon University. | The first test version of MinecraftEdu was sentto be tested for about ten people            |
| December 2011  | MinecraftEdu sale started.                                            | Theminecraftedu.comwebsite was launched.0.97 and later 0.975 of MinecraftEdu were released. |
| January 2012   |                                                                       |                                                                                             |
| February 2012  | Santeri & Joel met face to face. We rented office space.              |                                                                                             |
| March 2012     |                                                                       | MinecraftEdu version 0.98 was published.                                                    |
| May 2012       |                                                                       | MinecraftEdu version 0.982 was published.                                                   |
| June 2012      | Taavi Saarelainen, Miika Pakarinen,Aki Tanninen startedas trainees    |                                                                                             |
| Autumn 2012    | Toni Paavola started as a part-time employee.                         |                                                                                             |
| November 2012  |                                                                       | MinecraftEdu version 0.984 was published.                                                   |

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

#### Tutorial mode
- MinecraftEdu comes with a tutorial world that teachers may select from the server menu, that goes through the basics of controls, placing/destroyingblocks, teacher options, and more.

#### Mods
** Forge **
- MinecraftEdu comes prepackaged withMinecraftForgefor easy mod installation.

** ComputerCraftEdu **
- ComputerCraftEducome prepackaged with MinecraftEdu and is an educational version ofComputerCraftmade by TeacherGaming andDan200(Author of ComputerCraft), meant to teach students how to code inside ofMinecraft.

#### Skins
- Instead of having customizableskins, the player picks their skin from one of the many default skins that come with MinecraftEdu (in addition to Steve and Alex[verify]) when first joining a server or creating a world. In a multiplayer session, the skins they can pick from are dependent on whether the player is a student or a teacher.

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|---|---|---|---|---|---|---|---|---|----|----|----|----|----|
|   |   |   |   |   |   |   |   |   |    |    |    |    |    |

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|---|---|---|---|---|---|---|---|---|----|----|----|----|----|
|   |   |   |   |   |   |   |   |   |    |    |    |    |    |

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |

## Trailers








