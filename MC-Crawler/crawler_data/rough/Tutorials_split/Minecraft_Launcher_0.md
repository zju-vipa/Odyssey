# Minecraft Launcher
The Minecraft Launcher is the game downloader and launcher for Minecraft: Java Edition and one of the game downloaders and launchers for Minecraft for Windows (Bedrock Edition), Minecraft Dungeons, and Minecraft Legends. It is available for Windows, macOS and Linux, but Minecraft for Windows and Minecraft Legends can be played only on Windows 10 & 11, and Minecraft Dungeons only on Windows 7 or later.

## Contents
- 1 Features
- 2 Minecraft: Java Edition
	- 2.1 Installations
	- 2.2 Backward compatibility
	- 2.3 Realms
	- 2.4 Skins
- 3 Minecraft for Windows
- 4 Minecraft Dungeons
	- 4.1 Play
	- 4.2 DLC
	- 4.3 FAQ
	- 4.4 Installation
	- 4.5 Patch Notes
- 5 Minecraft Legends
	- 5.1 Play
	- 5.2 FAQ
	- 5.3 Installation
	- 5.4 Patch Notes
- 6 Settings
- 7 Command line usage
- 8 Uninstalling the old Minecraft Unified Launcher
- 9 History
- 10 Trivia
- 11 Gallery
	- 11.1 Minecraft: Java Edition
	- 11.2 Backgrounds
	- 11.3 Version history
	- 11.4 2013–16
	- 11.5 2016–19
- 12 References
- 13 See also

## Features
The initial login screen
On the initial login screen, users must log in with a pre-existing Microsoft account, otherwise they can create a new one by clicking the link. Subsequent logins can be done in the "Settings" tab.

On the left side, a "News" tab, a tab for each game, and the Minecraft Launcher "Settings" tab can be seen.

The top left corner of the Minecraft Launcher contains the user's Xbox gamertag for the currently active account (which might differ from their Minecraft: Java Edition username)[2]. By clicking on it, users can manage or log out of their active account, and see a "Help" page with various links to helpful resources.

## Minecraft: Java Edition
The main "Play" section allows the user to download (if needed) and launch Minecraft: Java Edition with the "Play" button, and also includes an installation selection on the left (which sorts installations by last played), the user's Java Edition username on the right, and a list of the latest news for the game from minecraft.net below. 

- One can launch multiple instances of the game by pressing the "Play" button while the game is running.
- If the device is not connected to the internet, the game can be run in offline mode, but only if the game has been initially downloaded.
- If the user isn't logged into an account that has purchased the game, the "Play" button appears as a "Play demo" button that downloads and launches thedemo versionof the game.

There is also a "Patch notes" section where the patch notes of the game's update can be seen, including the snapshots (if enabled).

### Installations


Creating a new installation.
In the "Installations" section, custom installations can be created and edited. There are buttons to sort and search installations, as well as checkboxes to enable installations with "Releases", "Snapshot", and "Modded" versions of the game. Installations are stored in launcher_profiles.json (or launcher_profiles_microsoft_store.json when using the new Minecraft Launcher for Windows) in the game's directory (.minecraft).

By default, there are installations for the "Latest release" and for "Latest snapshot" (if enabled), both of which the game versions cannot be changed. A new installation can be created by clicking the "New installation" button and an existing installation can be edited by clicking on it. There is a "Play" button that launches the selected installation and a folder icon that takes to the installation's game directory. The ellipses button contains the options to edit, duplicate, or delete an installation.

On the create/edit installation page, the following can be changed:

- Icon, by selecting one of the default ones or adding a custom one. Custom icons must be a.pngand 128×128 pixels in size.
- Name, by default called "<unnamed installation>".
- Version, which includes access to older releases and snapshots (if enabled).
- Game directory, the location of where the game files are saved, the default being.minecraft. The location can be typed in or selected using the "Browse" button.
- Resolution, which changes the game's windows size. It has a list of resolutions, or a custom one can be typed in.
- Java executable, by default uses the bundled java runtime.
- JVM arguments, such as heap size.

Before, it was possible for the users to manually set a logging configuration (see Debugging on wiki.vg for more info), however this doesn't seem to work anymore.[3]

A specific game version's server jar can also be downloaded by selecting the version in the list and pressing the "Server" button next to it.

### Backward compatibility
Selecting older versions in the create new installation screen.
The Minecraft Launcher has the ability to play most older releases of the game (and older snapshots, if enabled) by default, but also some older versions prior to Release 1.0. In order to see these versions in the installations section, the player must enable "Show historical versions of Java Edition" in the Minecraft Launcher settings tab. Because these versions are outdated and unsupported, they may contain bugs and errors that are not present in newer versions. It is recommended to run old versions of the game in a separate directory and backup worlds to avoid save corruption or other problems.[4]

Once historical versions are enabled, the following can be accessed:

- Mostbetaversions.
- Mostalphaversions.
- Oneinfdevversion.
- Fourclassicversions.
- Fivepre-classicversions.[5]

Some issues with these older versions include:

- Some sounds are wrong;bows,doors, andexplosionsuse their sounds fromRC1, even in versions released prior to it. In versions beforeAlpha v1.1.2_01, sounds do not work at all.
- Skinsare missing in versions prior to1.7, as earlier versions used a different skin server, which has since been shut down.Capesmay still work, however.[needs testing]
- InAlpha v1.0.15and fromAlpha v1.2.0toAlpha v1.2.6, theMinecraft Launcherdoes not set the player's name properly, resulting in everyone using default names: "Player" followed by a random 3-digit number. This makes multiplayer difficult to play, as a player's location and inventory is reset every time they relaunch their client.

- InAlpha v1.2.5and Alpha v1.2.6 specifically, players are always named "Player524". Playing multiplayer in these versions is impossible, as joining a server kicks off other players with the same name.

- As a side effect of the above, and as a result of old authentication servers being shut down, online mode no longer works in versions beforeBeta 1.8.

