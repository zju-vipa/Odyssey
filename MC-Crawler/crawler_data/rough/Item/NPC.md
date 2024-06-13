# NPC
Non player characters (abbreviated as NPCs) are interactive passive mobs that have model similar to villagers. They are exclusive to Minecraft Education and Bedrock Edition.[1]

## Contents
- 1 Spawning
- 2 Behavior
- 3 Interface
	- 3.1 Customization
- 4 Sounds
- 5 Data values
	- 5.1 ID
	- 5.2 Entity data
- 6 History
- 7 Issues
- 8 Gallery
	- 8.1 Renders
	- 8.2 Screenshots
	- 8.3 In other media
- 9 References
- 10 External links

## Spawning
Unlike other entities, NPCs do not spawn naturally; they can be spawned using the NPC spawn egg (it can be obtained with the following command: /give @s spawn_egg 1 51), or by using the command /summon npc. When spawned, an NPC displays a name hovering over its head. The default name is "NPC" with a color code of §e, resulting in the name being yellow.

To spawn an NPC with its spawn egg, the player must have the Worldbuilder authorization, automatically granted to players in Creative mode, or by using the /worldbuilder command.

## Behavior
NPCs have no basic AI. They can neither move nor be pushed by most entities, but they can be pushed by the breeze's wind charge‌[upcoming], and by explosions, water, lava, by sticky pistons from below or sides with a slime block attached and they can slide on ice when pushed. They cannot take damage nor be affected by potions. Nevertheless, the NPCs can still turn their body and stare at the nearest player if close enough. 
NPCs can also never ride minecarts or boats, and the vehicles go through NPCs. The player cannot use a lead on them.

NPCs are invulnerable to attacks. An NPC is attacked by zoglins, withers, wardens, goats, and vindicators named Johnny, but the NPC remains undamaged, pufferfish also inflate when an NPC is nearby. Foxes don't sleep near NPCs as well. Projectiles pass through them. However, an NPC dies when going below Y=-64, and despawns if it falls into the void.

## Interface
NPC interface without world builder permission.
NPC interface with world builder permission.
Right-clicking an NPC displays the interface. It can be edited only as long as the player has the world builder permission. The interface allows the player to edit the dialog, name, appearance and advanced settings. When the player doesn't have the world builder permission, it shows only the dialog and buttons.

### Customization
** Name **
The name of an NPC can be entered in the top text pane titled "Name". The text limit for the name is 32, and the color can be changed by using thecolor codesas by default the color is yellow (§e). Please note that there is a difference between the display name (the one you can change in the interface and is shown to everyone) and the actual name. The actual name is the one you want to use when using "@e[name=NPC]", and is often by default, just NPC. If you want it to have a different name, use /summon or rename the spawn egg to the preferred name.
** Dialog **
The dialog box located right below the "Name" and often used as a tool for guiding. The text limit for the dialog is 256, although in some cases it appears as 337.
** Appearance **
NPCs appearance are selectable, to change the skin simply just by left clicking on the preferred skin.
There are currently 60 skins available for the NPCs and defaults to the yellow-robed NPC.
** Advanced Settings **
The advanced NPC settings consists of URL and commands. They are used to create interactive buttons. The current maximum advanced settings that can be added is 6.URL‌[Minecraft Education  only]
The URL feature allows the player to add a hyperlink button. The URL can be entered at the first input box below the title up to 1024 letters.
To change the button name or label can be proceeded by filling the input box titled "Button Name", the current text limit for the label is 16 letters.
When added, the button appears only if the player has the world builder permission disabled. The button label defaults to "Learn More" and the color defaults to blue, it can be changed by using the color codes.
Command

The command feature allows the player to add one or more executable commands in the NPC. The command can be entered at the first input box below the title, unlike the command block wherein multiple commands can be executed in one window. The current maximum characters for the command is 1024. The command(s) get executed when the dialogue with the NPC is closed.
The command can be presented either as a button or a direct command. As a button, the button name or label can be changed by filling the input box titled "Button Name", the text limit for the label is 16 letters. It can be executed only if the player has the world builder permission disabled.
When not added as a button, the command is executed after the dialogue with the NPC, visible by right clicking the NPC, has closed. In contrariwise, the button is displayed and has a label color defaults to light gray, and can be changed by using the color codes. (the default name of the NPC is NPC)
@initiator‌[Bedrock Edition  only] is a specialized Target selector that targets the player that has interacted with the NPC, distinguishing them from other players that may interact later. This is useful for running commands on a per-player basis.
## Data values
### ID
| Name | Identifier | Numeric ID | Translation key   |
|------|------------|------------|-------------------|
| NPC  | `npc`      | `51`       | `entity.npc.name` |

### Entity data
NPCs have entity data associated with them that contain various properties.

SeeBedrock Edition level format/Entity format.
