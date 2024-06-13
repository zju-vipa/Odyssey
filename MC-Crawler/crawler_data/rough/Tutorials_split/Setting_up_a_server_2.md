### Minecraft options
Options for the server JAR go after the -jar minecraft_server.jar part. Run with --help to see all available arguments that can be passed to the server. Below is a list of available commandline options for the server.

** --bonusChest **
If abonus chestshould be generated, when the world is first generated.
** --demo **
If the server is in demo mode. (Shows the players a demo pop-up, and players cannot break or place blocks or eat if the demo time has expired)
Equivalent to playingMinecraftwithout a account, you have about 5 in-game days before your trial ends.
** --eraseCache **
Erases the lighting caches, etc. Same option as when optimizing single player worlds.
** --forceUpgrade **
Forces upgrade on all the chunks, such that the data version of all chunks matches the current server version (same as with sp worlds).
This option significantly increases the time needed to start the server.
** --help **
Shows this help.
** --initSettings **
Loads the settings from 'server.properties' and 'eula.txt', then quits.
** --jfrprofile **
Initializes the Java Flight Recorder on the server. Only available on 1.18+.
** --nogui **
Doesn't open the GUI when launching the server.
You will still be able to interact with your server, but you must use the cmd or Terminal if enabled.
- noguidoes the same thing as this option for backward compatibility with very old versions of the server, but--noguiis preferable as it matches the format of other options

** --safeMode **
Loads level with vanilla datapack only.
** --serverId <String> **
Gives an ID to the server. (??)
Used only in crash reports. If not given, then the "Server Id" detail is not added to crash reports.
** --singleplayer <String> **
Runs the server in singleplayer mode. <String> is the name of the Singleplayer player.
The Singleplayer player data is loaded fromPlayerin thelevel.datfile.
Monsters spawn ignoring the 'spawn-monsters' property unless thedifficultyis Peaceful. Animals spawn ignoring the 'spawn-animals' property.
The defaultpermission levelis 0 (ignoring the 'op-permission-level' property) unless otherwise specified for a player in ops file.
The permission level required for the/publishcommand is 4. Although the server is already published.
The permission level required for the/seedcommand is 0, not 2.
Blacklists are disabled. These commands are not available:/ban-ip,/banlist,/ban,/pardon,/pardon-ip.
The local IP is '127.0.0.1' ignoring the 'server-ip' property. Use of authentication is disabled ignoring the 'online-mode' property. Prevention of proxy connections is disabled ignoring the 'prevent-proxy-connections' property.
The default game mode (the 'gamemode' property) is still used for new players, but does not change the world's default game mode (GameTypein thelevel.datfile).
** --universe <String> **
The folder in which to look for world folders. (default:., the current directory)
The following options are available from server.properties too. It might be a better idea to edit that file instead for easier management:

** --world <String> **
The name of the world folder in which the level.dat resides. (default:world)
This is the same aslevel-name.
** --port <Integer> **
Which port to listen on, overrides the server.properties value. (default: -1, read from server.properties)
SeeServer.properties, option "server-port", for restrictions on this value.
### Example command line
- Running a world found in the folder "cold" on port 1337, with 1G of RAM allowed:java -Xmx1G -jar minecraft_server.jar --port 1337 --nogui --world cold.

## Windows instructions
### Installing Java
The Minecraft server requires the Java Runtime Environment (also called JRE or simply Java). For your security, you should only use the most recent version of Java. To verify that you have the latest version, do one of the following: 

- Open Windows Control Panel, find Java (it may be inside the Programs category), and click on Update Now.
- Visithttp://java.com/en/download/installed.jsp. This will perform an automatic version check from your browser. However, theGoogle ChromeandFirefoxbrowsers do not run Java content and therefore cannot check Java through the browser.
- Open a command window and enter the commandjava -version. If a version number is reported, then check theJava websiteto see what the most recent version number is.

If you don't have Java or your version is outdated, then download the newest version at https://adoptopenjdk.net/ (OpenJDK) or http://www.java.com/download/ (Oracle "OTN" JDK)

## macOS instructions
Keep in mind that the server won't run correctly on macOS 10.4 and earlier and may crash your machine.

### Installing Java
Open the terminal.

- Check if you have java by runningjava -version. Make sure it's newer than 1.6 (best if newer than 1.8), for most versions, or java 17+ on 1.17 and later versions.

- If you don't have java, you can install it via HomeBrew:
	- Run/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"to install HomeBrew first.
	- Runbrew install openjdkto install java (OpenJDK).
- Runjava -versionagain. You should get something this time.

### Setting up the Minecraft server
See the Common instructions.

### Using Time Capsule



Contents in this section are disputed. 
This section should definitely not be in this part (it fits better under #IP address notes), but then it probably also does not belong under this article. We are not adding instructions for TP-link, D-link, Linksys and all other brands, so why single out AirPort specifically?


Some homes use AirPort Time Capsule as a wireless router instead of other brands. This section will teach you how to set one up without messing up your file server. 

NOTE: Make sure you have your admin username and password.

- Open System Preferences > Network.
- Click the Advanced button and go under TCP/IP.
- Where it says Configure IPv4, change that option to Using DHCP with manual address.
- Change the IP address to 10.0.1.x, where x is a number between the last number of the two numbers under DHCP range (i.e. 10.0.1.2 to 10.0.1.254 would be anywhere between 2 and 254).
- Now go to the Sharing section and make sure that Internet Sharing is on.
- Now, open up AirPort Utility and edit your Time Capsule settings.
- Go under Network and make sure the option Router Mode is set to DHCP and NAT. Now, click the + button under the Port Settings.
- Type in the following:
	- Description: Minecraft Server (or whatever you want to call it)
	- Private IP Address: The address you chose for the 4th step.
- Change everything with the word port in it to 25565.
- Now, hit Save and update the Time Capsule.

That's it! You're now ready to configure your server.

