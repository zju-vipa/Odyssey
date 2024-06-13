# Tutorials/Setting up a server
This tutorial takes you through the steps of setting up your own Java Edition server using the default server software that Mojang Studios distributes free of charge. The software may be installed on most operating systems, including Windows, macOS, GNU/Linux and BSD.

For more tutorials, see the bottom of this page or the Tutorials page. For more information on Minecraft servers, see the Server page.

Notes:

## Contents
- 1 Warning
	- 1.1 Security recommendations
- 2 Java
	- 2.1 OpenJDK vs OracleJDK
	- 2.2 JRE vs JDK
	- 2.3 Java Version
	- 2.4 Headless Java
- 3 Common instructions
	- 3.1 Java options
	- 3.2 Minecraft options
	- 3.3 Example command line
- 4 Windows instructions
	- 4.1 Installing Java
- 5 macOS instructions
	- 5.1 Installing Java
	- 5.2 Setting up the Minecraft server
	- 5.3 Using Time Capsule
- 6 Linux instructions
	- 6.1 Installing Java
		- 6.1.1 Solus
		- 6.1.2 Debian, Ubuntu, Raspbian
		- 6.1.3 openSUSE
		- 6.1.4 Arch Linux
		- 6.1.5 Gentoo
		- 6.1.6 Other distros
- 7 FreeBSD instructions
	- 7.1 Installing Java
	- 7.2 Launching Minecraft Server
- 8 Hostman
- 9 Cloudron
- 10 Docker
	- 10.1 Getting docker (for Linux, Mac & Windows)
	- 10.2 Docker image
	- 10.3 Updating Docker image
	- 10.4 Docker-Minecraft on Synology diskstation
- 11 Configuring the environment
	- 11.1 Writing a script to launch the server
		- 11.1.1 On Windows
		- 11.1.2 On macOS, Linux, and FreeBSD
	- 11.2 Startup and maintenance script
	- 11.3 Port forwarding
	- 11.4 Setting up a VPN
		- 11.4.1 Setting up Hamachi
		- 11.4.2 Setting up Radmin VPN
	- 11.5 Configuring the Minecraft server
- 12 Connecting to the Minecraft server
	- 12.1 IP address notes
	- 12.2 Firewalling, NATs and external IP addresses
		- 12.2.1 Local network dedicated servers
		- 12.2.2 The SRV record
- 13 FAQ (frequently asked questions)
- 14 Video/Alternative Tutorials

## Warning



Note 
Running server software on your computer without a clear understanding of what you are doing may make your system vulnerable to attacks from outside.


Since you're about to run your own server, you should be aware of the possible dangers. Running by the instructions below should not put you at any risk, but this is a wiki which everybody is allowed to edit, and we don't know about your system configuration, so we can’t guarantee you'll be 100% out of danger. 

In order to run your server and stay out of trouble, we highly suggest that you should at least know about the following:

- Using the command-line and editing configuration files
- Networking in general (IP,DHCP,ports, etc.)
- Your system configuration
- Your network configuration
- Your router configuration (if you want other people to connect over the Internet)

### Security recommendations
Before exposing your server to the public, it is recommended to follow these practices:

- Only give out necessary permissions to run a Minecraft server. Such permissions likesudoor running as asuper userare too extensive, and can leave out tosecurity vulnerabilities.
- Close unused ports, and open ports when needed. This is recommended to prevent outside attacks and security exploits. Only open essential ports, such as Minecraft server's default port 25565, or your custom port. Remember to close the port when it is not needed anymore.
- If you're usingSecure Shell, make sure to enable some form of authentication, such as password or SSH key. Passwords must be strong. Strong passwords are at least twelve characters long, and combine uppercase and lowercase letters, numbers, and special characters.[1]SSH keys are akin to a secret password, and must be kept safe and private. Never share SSH keys over insecure networks.
- Enable whitelist for your server. Exposing your Minecraft server to the public opens the door for other players or foreigners that you don't recognize, and can lead togriefing. Whitelist is configurable throughwhitelist.jsonor the/whitelistcommand. Only add trusted players into your whitelist.
- Configure your networkfirewallproperly to prevent outside intrusion.
- Regularly update your server to the latest version, and avoid any releases known to have vulnerabilities.
- Regularly make server backups to safeguard your data against loss or corruption.
- Review your server plugins andmodsfor known vulnerabilities.
- Test plugins and mods on a separate server instance, and not your main one.
- For personal or private servers, expose the server's port only to the local host.

## Java
Java is a programming language designed to create programs for the Java Virtual Machine (JVM). The JVM supports many different platforms. By doing this, developers write code for the JVM and any platform supported by the JVM can run the program. Further reading.(Remote shell port)

This section is designed to answer some frequently asked questions about Java and guide you through some decisions regarding Java.

#### OpenJDK vs OracleJDK
OpenJDK and OracleJDK are very similar. OpenJDK is the official open source reference implementation of Java. OpenJDK is an open source codebase that almost all other JDKs are built on. Excluding packaging, cosmetic and license differences OpenJDK is the same as OracleJDK.

Alternatively, Microsoft also offers their own build of OpenJDK and is available for commercial purposes.

Do note that OracleJDK (Oracle's "OTN") builds require a paid subscription for commercial and production purposes. This likely includes running a Minecraft server even if it is non-profit. Oracle does provide its own OpenJDK builds, but they are not packed into an installer format for easy use.

#### JRE vs JDK
JRE stands for Java Runtime Environment. JRE is a package tool designed to run Java programs. JDK is a package of tools designed to develop Java programs. If you have the JDK then you have the JRE and the JVM too. 

There is another version of Java called Headless Java. It is frequently used in servers as it’s less resource intensive because it does not have the GUI nor the mouse/keyboard support.

#### Java Version
For servers running Minecraft 1.16 or older, JRE Version 8 or higher is required, 1.17 requires Version 16 or higher, and Minecraft 1.18 or newer requires Version 18 or higher. While servers can run on an older version of Java, newer releases may offer bug fixes, more stability, security, and performance. 

#### Headless Java
A headless Java installation is a trimmed down version of Java. It does not have a GUI or mouse/keyboard support. Headless Java is frequently used in Servers or other environments where a GUI is not needed.

| “ | There are several virtual packages used in Debian for Java. These cover runtime compatibility and come in two flavors; headless (omits graphical interfaces) and normal. | „ |
|---|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
|   | — Debian Wiki                                                                                                                                                            |   |

## Common instructions
The general gist of running a Minecraft server is that you will need to install java, run the server, accept the EULA, and run it again. Once you have installed java and opened up a command line, everything is basically the same.

- Check thesystem requirementsfor CPU, RAM, and disk space.
- Install Java. Use the OS-specific instructions below for this.
- Download your server jar file from thedownload page.
- Make a new folder for the jar file and move it there. This will be where all the configuration and the world files will be stored, so you don't want these to just sit in "Downloads".
- Open a command prompt or a terminal interface. (On windows: search for cmd. On macOS: open terminal in launchpad."
- Check again if Java is available. Typejava -version.
- Typecd(change directory), followed by the path to the folder where you placed your server jar file. You can drag the folder into the terminal window to get the path, if you have a GUI open.
- Run the server for the first time by typingjava -jar minecraft_server.jar --nogui(replacing the jar name (minecraft_server.jar in this case) by whatever you named the jar file to be).
- A file calledeula.txtwill be generated after you run the server for the first time. Open it in a text editor and changeeula=falsetoeula=true. It signifies that you have read and understood the end user license agreement that you'll follow when using the software. If you don't do this, the server will shut down immediately when you try to start it.
- Now the server has been set up, and you can simply run it withjava -jar minecraft_server.jar. If you don't want a GUI for typing commands, add a space and--noguito the command. (Some people say it makes the server much much faster.) You can also use a few other switches described below.

At this point you should have a basic server running. See Configuring the environment for more information about configuring your server. One of the things you definitely want to do is writing a script to launch the server so you don't have to remember the command line.

### Java options
Java options should be added between the  java and the -jar  on the command line, or in your startup script.

** Memory limits **
The most important thing for aMinecraftserver is memory to run with.-Xmxdefines how much memory it is allowed to use.-Xmx2G(2 gigabytes) is more than enough for a home server with 5 players on defaultsimulation distance(5×212= 2205 chunks simulated), but do scale it up by your actual settings. Setting the value too low causes frequent GC stops. Making it too high can make GC too long on Java 8 – a version you should not be using in the first place.
-Xms(the initial memory size) is the next biggest knob, butonlyaffects startup performance. If your server also runs things other thanMinecraft, set it to 1/4 of the maximum size (so for our case,-Xms512M) for a good balance: the JVM will be allowed to return some memory to the OS when it's not needed. (The return algorithm isveryconservative, so it has very minimal effect on long-term performance.) If your server is fully dedicated toMinecraft, feel free to go higher: making it equal to the maximum size disables heap scaling and gives maximum startup speed.
A "soft max heap size" (-XX:SoftMaxHeapSize=1G) is available for some versions of JRE. The JRE will try to only use that much memory, but will go over to a maximum of-Xmxif necessary. If you are running many things on your server, this may be useful.
** GC **
The default GC on Java 9+ used by modernMinecraftis G1GC (Java 8 also has it, but it is off by default). The flags used by the official launcher-XX:+UnlockExperimentalVMOptions -XX:+UseG1GC -XX:G1NewSizePercent=20 -XX:G1ReservePercent=20 -XX:MaxGCPauseMillis=50 -XX:G1HeapRegionSize=32Mworks reasonably well, though of coursebetter flags (brucethemoose)exist. (Aikar's famous flagsare good, but not optimal.)
On Java 14+, ZGC is available. This GC is almost lag-free with millisecond-level pauses. Delete all GC-related flags and simply use-XX:+UnlockExperimentalVMOptions -XX:+UseZGC. Tuning flags other than-Xmxarea lot less importantcompared to in GCs (the default is quite good), although-XX:-ZProactiveis worth a try if you want to trade memory for lag.
** VM **
OnSolaris, use-d64to tell the JVM to use your 64-bit processor properly. Since nobody uses Solaris, this is irrelevant.
Calculations may be made faster with GraalVM, benefiting operations such as chunk generation. A basic version is bundled in the common "HotSpot" Java 9–15, but it was later removed due to maintenance burden. Now you need to download it separately: useinstructions from brucethemoose.
To sum up, a reasonable flag combination can be as simple as -Xmx4G -Xms1G -XX:SoftMaxHeapSize=3G -XX:+UnlockExperimentalVMOptions -XX:+UseZGC. That is it. There are bits that you can squeeze from complicated flags, but you would get much more from modified server software. In fact, all serious discussions (e.g. Aikar and brucethemoose) of server performance assume some degree of modding.

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

## Linux instructions
Linux comes in many different varieties called distributions (distros). Some of these distros are designed or better suited for running a server. If you are setting up a dedicated server it is recommended to use one of these distros. 

Linux, in general, is more welcoming to open source programs. So where applicable it is recommended you use open source programs, such as OpenJDK.

### Installing Java
For most distributions, it is recommended to install OpenJDK 16 (for 1.17+) or OpenJDK 8 (for below 1.17) from the official repositories. For Oracle Java refer to Oracle's Download Page.

Note: While not affecting Minecraft server, JavaFX or other proprietary aspects of Java will need to be installed separately.

Specific instructions are included for each distro below, but not all have been updated to 1.17. If it only says to install OpenJDK 8, that means that it has not yet been updated to 1.17.

#### Solus
Run sudo eopkg install openjdk-8 to install OpenJDK.

For OracleJDK refer to Solus Help Center

Note: OpenJDK 11 is not in Solus' repositories.

#### 
Note: You might need to install the package "software-properties-common" by running sudo apt-get install software-properties-common and/or "python-software-properties" by running sudo apt-get install python-software-properties to use the apt-add-repository command.

Due to licensing issues, the repository frequently used to install Oracle Java has been discontinued. It is now recommended that you install OpenJDK 8 or above. 

OpenJDK can be installed with one command: 

- sudo apt update; sudo apt-get install openjdk-8-jdk-headlessbelowMinecraftServer 1.17
- sudo apt update; sudo apt install openjdk-16-jdk-headlessat or aboveMinecraftServer 1.17

Removing the 'headless' part of the command will install all components of Java.

Note: <1.17 tested in Ubuntu 18.04, 1.17 tested in Ubuntu Server 20.04.2 LTS

#### openSUSE
Note: Due to possible instability openSuse Tumbleweed is not recommended as a dedicated server.

Just run the command from the terminal: sudo zypper in java-1_8_0-openjdk 

Java should be installed.

Note: Tested in openSuse Leap 15.1

#### Arch Linux
Both java 8 and 16 are in arch linux's repostiory.

Just run pacman -S jre-openjdk-headless, For the OpenJDK 16 JRE, Remove "-headless" for the full JRE if you want to run with GUI.

Just run pacman -S jre8-openjdk-headless, For the OpenJDK 8 JRE, Remove "-headless" for the full JRE if you want to run with GUI.

If you encounter issues it is recommended that you refer to the ArchWiki

#### Gentoo
Run emerge --ask virtual/jdk

Gentoo Wiki

#### Other distros
Check your distro's documentation. It should have information on how to install OpenJDK.

Alternatively, you can visit Java's website directly to download the Java package for Linux. Most distros work with this (either 32 or 64-bit). Instructions for the installation of those different packages are given on the site.

If during installation, it asks for a password, enter your password. If you get asked "Is this OK [Y/N]" Enter Y and press enter if required. Java should now be installed.



## FreeBSD instructions

  

This section needs to be updated. 
Please update this section to reflect recent updates or newly available information.Reason: The official people have been using Java 8 for quite a while, so Java 7 is definitely outdated. A lot of the crashing is gone with OpenJDK8, so maybe the whole Linux-compat thing can be removed once tested.


This part was tested with FreeBSD 10.0 amd64 and 'jre-7u65-linux-i586.tar.gz'

### Installing Java
Due to performance and crash issue with OpenJDK and Minecraft server, we will install Oracle JRE made for linux.

Before installing this JRE, you have to install the linux binary compatibility on FreeBSD, you can follow this documentation.
Jave requires some information about the proc. You have to mount linprocfs, type:

kldload linprocfs
mount -t linprocfs linprocfs /compat/linux/proc

and add this line to /etc/fstab:

linprocfs   /compat/linux/proc   linprocfs   rw   0  0

The Oracle JRE has a dependency marked as forbidden and the installation will fail. Go to /usr/ports/textproc/linux-f10-expat2.0.1/ and in the Makefile remove the line which starts with FORBIDDEN=.

Next you have to manually get the linux tarball due to licence issue (like `jre-7u65-linux-i586.tar.gz') from java official web site and copy the file to /usr/ports/distfiles.
Then to install the JRE, go to /usr/ports/java/linux-sun-jre17/ and run make install distclean.

Note: The previous version of this part, tested on FreeBSD 9.2 amd64, was explained like this: You may have to set JRE_UPDATE_VERSION variable in your Makefile to the actual number (e.g. 45 like in this example) and run 'make install NO_CHECKSUM=1'.

Try running java -version. You may end up with a message that it cannot find libjli.so. One way to fix it is to add your java paths to the search explicitly.
Make a symlink:

ln -s /usr/local/linux-sun-jre1.7.0/lib/i386 /compat/linux/usr/lib/java

And in /compat/linux/etc/ld.so.conf.d/java.conf add:

/usr/lib/java
/usr/lib/java/jli

Run /compat/linux/sbin/ldconfig.
Now java -version should work.

### Launching Minecraft Server
Create a folder and copy the Minecraft server jar in it.
In the actual version you will get this exception syscall epoll_create not implemented if you run the server in the usual way, so we add this line to the command to fix that -Djava.nio.channels.spi.SelectorProvider=sun.nio.ch.PollSelectorProvider.
The command to launch is like:

java -Xmx1024M -Xms1024M -Djava.nio.channels.spi.SelectorProvider=sun.nio.ch.PollSelectorProvider -jar minecraft_server.1.7.10.jar --nogui

## Hostman
Hostman is an application hosting provider to host apps in the cloud. Minecraft is available as a one-click app package on Hostman. Installation takes about 2 minutes, there's an instruction on how to configure the server and start playing. You can have multiple Minecraft services on one server. Try a free demo here.

## Cloudron
Cloudron is a platform to self-host apps on your server. Minecraft is available as a one click app on Cloudron. It comes with a web interface to manage Minecraft from the browser. You can also have multiple installations of Minecraft on the same server. You can try a demo here (username: cloudron password: cloudron)

## Docker
Docker is a free container based platform which helps to isolate instances of a Minecraft Server from each-other and from the host system. Docker and the owner of the repository of the container are not affiliated with Mojang.

### 
Read https://docs.docker.com/install/

### Docker image
1. Download the image by runningdocker pull sirplexus/minecraft-server-standalone:latest
2. Set up the container with port 25565 open, 1G ram assigned and named "MyServer":docker container create --publish 25565:25565/tcp --name "MyServer" --env RAM=1G sirplexus/minecraft-server-standalone
3. Start the container:docker container start MyServer

### Updating Docker image

For updating minecraft-server-standalone run 
docker pull sirplexus/minecraft-server-standalone:latest

### Docker-Minecraft on Synology diskstation



Note 
This is for self-hosted worlds, NOT a standalone. You will need to download a server.jar from the official site.


Docker is an "Add-on Packages" on many new Synology Diskstations, and many of them are powerful enough to run at least one Docker Minecraft.

Before starting the docker, you need to make a folder containing the version of Minecraft you would like to play (It has to be named "server.jar") and an eula.txt (read about this under "Common instructions").

The way to setup a Minecraft server on a Synology Diskstation is to:

1. Install and open docker on your Diskstation
2. Search for "sirplexus" under Registry and find "sirplexus/minecraft-server". Right click and "Download this image".
3. After download you can find the image under image. Press "Laungh"
4. Press "Advanced settings" and go to the tab "Volume". Add the previus created folder and set "mound path" to "/srv/minecraft".
5. Go to the tab "Port Settings" and assign a "Local Port". This is the port you will connect to from theMinecraft Launcher.
6. Press "Apply" and "Next" and again "Apply" to finish the container.

You will now be able to play Minecraft on your Synology Diskstation. The IP address it the IP of the Diskstation and the Port number is assigned undet step 5.

## Configuring the environment
### Writing a script to launch the server
It's definitely boring to have to remember the command-line options for your server every time you launch it. Luckily, we can write it down in a file and just run that instead.

#### On Windows
The windows version of a script is called a batch file. Create a text file in the folder where you put the jar as "start.bat", and then right click it to edit using notepad. Paste the following in:

@ECHO OFF
java -Xms1024M -Xmx2048M -jar minecraft_server.jar --nogui
pause

Double click the file to start your server. You may get a "Class_Not_Found" and ServerGuiConcole error, just ignore these errors
and you should see your "Server Thread/INFO" dialog start the server.

The "pause" command is there to keep the window open so you can read what happened after the server stops.

#### 
All these systems use a common scripting language called the "POSIX shell script" on the command line. Create a text file in the folder where you put the jar as "start.sh" and write the following in:

#!/bin/sh
cd "$(dirname "$0")"
exec java -Xms1G -Xmx1G -jar server.jar --nogui

Now save the file. Run chmod a+x start.sh (or path to wherever you put the script) to make it executable. You can now run the file by double-clicking or by running ./start.sh in the folder (or using a whole path from outside there).

If you want to add a pausing part like the Windows example, remove the exec word, and add a line of read -n 1 -p "Waiting..." to the end. This is useful if you are running the script by double-clicking on the GUI.

### Startup and maintenance script
Alternatively, you can manage/automate the startup and shutdown of the Minecraft server using a script such as the ones listed below:

- Minecraft Server Control Script (MSCS)is a server-management script for UNIX and Linux poweredMinecraftservers. Features include:
	- Run multipleMinecraftworlds.
	- Start, stop, and restart single or multiple worlds.
	- Create, delete, disable, and enable worlds.
	- Includes support for additional server types: Forge, BungeeCord, SpigotMC, etc.
	- Automatically backup worlds, remove backups older than X days, and restart worlds.
	- Visit theMinecraft Server Control Script Github pagefor more information.
- Minecraft Server ManagerA comprehensive startup script forMinecraftand Bukkit servers (support Debian, such as Ubuntu).
	- MSM can also periodically createWorld Edit compatiblebackups.
	- Keeps players informed with configurable in-game messages, such as "Shutting down in 10 seconds!"
	- Expose in-game commands (such as "say", "op" and "whitelist") to the terminal.
	- Tab completion on all commands makes learning easy.
	- VisitMinecraft Server Manager's GitHub pagefor the full list of features.
- Server startup script
- FreeBSD startup script
- OpenBSD startup script
- Ubuntu startup script
- rfwadminstartup script with web interface (for Linux servers). Nice web interface for quickly saving and loading maps.
- Minecraft Systemd ServiceA fully systemd-integratedMinecraftservice:
	- Working on CentOS and Fedora
	- Protecting the server with various readonly and inaccessible jails
	- Safe restart and stop operations using rcon
	- Can be combined with aMinecraft Command Center Scriptfor ease of administration
- Arch Linux systemd wrapper

### Port forwarding
See also: Wikipedia:Port forwarding

Port forwarding is used when you have a router and you wish to let users connect to your server through it. If you wish to host your server for local reasons, it is not required that you do so. Keep in mind that port forwarding might cause security risks.

When port forwarding, it varies on how your router will ask you for the information. If you don't understand on how your router wants you to input the information, try visiting PortForward.com for a tutorial.

Once you have managed to locate your router's admin page, and find the Port Forwarding page; hit add new service (may not work) (if you use Belkin, this can be very difficult to perform) or custom service. When you get a page asking to setup the new rule, it should prompt you on what you want to call it. You may name it as you wish, but for simplicity, name it "minecraft". Then, you want to look for "type". If "TCP/UDP" or "Both" isn't an option you will have to create two rules for both protocols. For the ports (internal and external), enter 25565. If it asks for anything else other than output IP (or internal IP, server IP), leave it alone and continue.

To find your computer's IP address, use the following steps:

**  Windows **
PressWin+R; this should be up to the "Run" dialog box. Typecmdand hitEnter. This should open a command window with a black background. From there, typeipconfigand pressEnter. You should be given a list of text. Scroll up to "Wireless LAN" (if using wireless) or "Ethernet" (if using a wired connection), and look at "IPv4 address". To the right of this should be a string of numbers (of the form xxx.xxx.xxx.xxx). Copy this down by right-clicking the window and selecting "Mark", then highlight the area and hit Enter.Don't copy any parentheses or letters.
The IP location on OS X
** Mac **
Locate your way to your desktop. Pull up the apple menu under the logo and scroll down toSystem Preferences; then select "Network" your IP should be on the lower right as "IP address (xxx.xxx.xxx.xxx)". Once you have your IP, copy it down.
** Linux **
Either you use the network diagnose center (depending on distribution), or the terminal withifconfig. The output should return all your interfaces. Search forinet addr:xxx.xxx.xxx.xxx, copy the xxx.xxx.xxx.xxx numbers down.
Once you have this IP, enter it in the "Output IP / Server IP" or whatever way it asks for where the service points to.
Once you have completed it, find where it says to save/continue/apply. And you have successfully port forwarded. When you run yourMinecraftserver, you have to leave the Server IP field empty in the server properties.
For people to connect to your server, they must use your external IP, which you can find at websites such asIP Chicken. If you don't want to use such IPs, use DynDNS services such asNoIP DynDNS
Now it is time to configure and connect.

### Setting up a VPN



Note 
VPN's can cause issues connecting to Mojang's servers, Minecraft servers, or to the internet.



  


The contents of this section are not supported by Mojang Studios or the Minecraft Wiki.


An alternate way to set up a server between you and your friends is to set up a VPN (virtual private network). This method may be deemed unrecommended, and an inconvenience for many users due to the fact that all users who wish to connect to the server must download external software in order to join or create server. An alternative to this method is to port forward. A free software utility that can be used to set up a VPN is Hamachi by LogMeIn. OpenVPN is another (free, open source) alternative that supports most OSes, but is a bit more difficult to configure. Free Radmin VPN is another software with no need to register on the website and no limits per the number of users. The free version of Hamachi allows up to 5 connections (i.e. players).

#### Setting up Hamachi
1. Install Hamachi on each computer that wishes to participate in the server, including the host.Windows / MacLinux(32-bit and 64-bit.deband.rpmpackages are available, you can install it on Gentoo by emerging "net-misc/logmein-hamachi")
2. The host server signs up for admin via theLogmein website.
3. On the host machine, a new Hamachi network is created.
4. The host installs and configures theMinecraftserver software:The server IP field in server.properties is left blank (as default).
5. The host passes the newly created Hamachi network credentials to each of the players.
6. The players connect to the host's Hamachi network.
7. Now that all the machines are connected within the same Hamachi network, the host gives their machine's Hamachi IPv4 address to the players.
8. Each player connects using this IP as per the usualMinecraftmultiplayer screen.
9. Note that Hamachi has been squatting on an IANA-allocated IP block (25.0.0.0/8). As such, Hamachi fundamentally conflicts with the internet itself.

#### Setting up Radmin VPN
It is very similar to Hamachi installation.

1. Download free and installRadmin VPN
2. Create a network: after Radmin VPN installation on the local computer press "Create network" button. Set a Network name and a Password —> Press "Create" button.
3. Now the new network will appear in the main window —> invite friends, send them the info to connect -> you are welcome to runMinecraft.
4. Connection: after program launch press “Join network" —> in the dialog box press enter Network name and Password received from the network administrator —> "Join" —> the new network and its nodes will be shown in the main window. —> Connect to the host inMinecraft.

- If the connection on Radmin VPN has been established, but you don`t see other players in the game, then it is required to adjust firewall for work of the game or just turn the firewall off.

### Configuring the Minecraft server
1. Configure the server by editing theserver.propertiesfile, the format for which isexplained here. Be certain to edit the file with a text editor that does not add formatting (e.g., for italics), such asWindows Notepad. Additional configuration may not be necessary as many servers run fine from the default values.
2. To become or add an operator (op), type/op <targets>into the server console or gui. This adds the specified user's username andUUIDto theops.jsonfile. Operator status will not be changed if you change your username due to the use of UUID.
	- Administrators and operators may executecommands. In other words, operator (op) privileges allow you to control certain aspects of the game (e.g., teleporting players).
	- ops.json contents:[
  {
    "uuid": "",
    "name": "",
    "level": 4,
    "bypassesPlayerLimit": false
  }
]
3. If yourserver.propertiesis configured to enable whitelist, you can add a user to thewhitelist.jsonby typing/whitelist add <player>into the server console or gui. Due to the transition to the UUID system, it is not recommended to directly editwhitelist.json.

## Connecting to the Minecraft server

  

This section needs to be updated. 
Please update this section to reflect recent updates or newly available information.Reason:
Internal IP is less reliable than looking for the server by hostname, which is available through either router DNS or mDNS (Bonjour, available in all versions of macOS and Windows 10). Static IP works, but it requires making sure the router never gives the address to anyone else. (In an ideal world you'd just use the existing LAN server discovery system, but Mojang has decided it's irrelevant for dedicated.)
Port forwarding can potentially be replaced with UPnP. More flexible, but a bit brittle.


- If you are playing on the same machine on which the server is running, select the "Multiplayer" option in the game client, click direct connect, and then type inlocalhostinstead of an IP address.
	- Both hosting and playing on the same machine is not a recommended practice unless you have a powerful computer (e.g. more than 6 gigabytes of ram (4 for the server, 2 for the client, and some for the rest of the system).
- Users within your local network (i.e., that are accessing the same router) can connect using your internal IP address; port forwarding is not required for such local connections. The internal IP address of a specific network adapter can be found by typing "ipconfig" into the command prompt and looking for the IPv4 address, or by usingthis website. If the port is set to a number other than 25565 inserver.properties, that port must be included. This address (both IP and port) will look something like192.168.0.168:25565.
- Users connecting from the Internet (i.e., outside of your local network) must connect using your external IP address. You must port forward for someone outside your network to connect to the server.

### IP address notes
- Unless you set a static IP for the computer that is hosting the game, the internal IP address can change. This affects port forwarding rules, and can make them invalid. Each modem or router has a different way of setting a static IP address. You should refer to the manual for your device(s) or online documentation for further instruction.
- If you are having players connect to your external IP, your external IP can change if you do not have a static IP from your internet service provider. Use a tool such asWanIPto periodically check on the external IP address. You may also search "my ip address" on Google and it will show your IP address. Alternatively, you can look into a DDNS service that will allow you to have a name, rather than an IP address, that will remain the same. The name will point to your external IP address, regardless of whether or not it changes (the DNS is updated when changes occur, hence "dynamic").
- For troubleshooting purposes you can try runningMinecrafton the server machine and connect locally. You can connect through eitherlocalhost, your home network IP (192.168.x.x) or your public (Internet) IP.
- If for some reason you have trouble with connecting publicly over your IPv4, try connecting over IPv6. This should only be done for testing whether your server is online, external players should still use IPv4.

### 
- You must open a TCP/UDP port (default is 25565) on the firewall.
	- If the server in question is not reachable via a globally routable IP address, you will need to add appropriate address and/or port number translation rules to the gateway — usually your router has the global IP address.
- For help with address translation, opening the firewall and routing (these three make up what people call port mapping/forwarding),portforward.comis a good source. Select your router from that list, skip the ad that comes after selecting the device, and you will see instructions for setting up port forwarding. Alternatively, you can read the documentation supplied with your router, modem, or other ISP related hardware.
- Verify the port is open, and note your external IP by using a port checker tool, such asYou Get Signal. The default port you should test is 25565, unless you specified something else.Have the Minecraft server running when you test the port.
- You can obtain your external IP address fromYouGetSignal.

#### Local network dedicated servers



This only applies to Classic (v0.30) servers. 


A common problem for server administrators is the inability to connect to your own server via another machine on your local network. A typical scenario for this is that you have a Classic server running on a dedicated machine, and you have your own machine which you play on. They're both connected to the same router/switch, and have internal IP's with the octets '192.168.x.x'. Normally, connecting via the URL generated for your server will result in an error message claiming that the server is offline.

To correct this, you must add a function to the end of your URL, bookmarks, or whatever else you connect by. The function is: ?override=true
Example: http://www.minecraft.net/classic/play/4c3bebb1a01816acbe31c5ece1570da5?override=true

Previously, (before the 1.8 beta and website update) this was &override=true. This caused much confusion since the change was not announced by Mojang, and wasn't announced on the website applet pages either. Before the update, connecting to your own URL via the website resulted in red text under the applet window saying "If you can't connect, try this link instead." The link returned the same thing, with the &override=true affixed to the end.

Note: This situation does not effect Beta servers, and you should be able to connect via an internal or external IP.

#### The SRV record
Java Edition since 1.3 also supports using custom ports without requiring the player to type it. This is achieved by using a SRV record (for "service") in the DNS. The SRV record tells Minecraft the actual host and port to use; some DynDNS services and most static DNS services allow you to set it up.[2]

To manually verify the SRV record, use (assuming the player-facing domain is "YOUR.DOMAIN.com"):

> nslookup -q=srv _minecraft._tcp.YOUR.DOMAIN.com
Server:  UnKnown
Address:  [REDACTED]

Non-authoritative answer:
_minecraft._tcp.YOUR.DOMAIN.com  SRV service location:
          priority       = 5
          weight         = 5
          port           = 65312
          svr hostname   = ACTUAL.DOMAIN.com

## 
Q: I have a problem which is not answered in here! What should I do to?

A: Go to the Minecraft Forums and post your problem there. To help you, they need the following information:

- Operating system
- Version of Java
- One machine or multiple computers
- Exact description of the problem
- Steps you have taken to solve the problem
- Any errors you encountered
- Screenshots of the problem (if possible)
- Anything else that might help us to solve your problem—there almost never is too much information (passwords would be too much information!)

And please, if we were able to help you, post where the problem was exactly and what the fix was for that. Other people will appreciate that (and we will be able to get a grip on the common problems)!


Q: On a Windows computer, when I double click the batch file it opens a command prompt window, but quickly disappears and the server does not start.

A: Right-click your .bat program and hit edit; add a new line and type pause save and run the file. If it says invalid path, it is probably due to an incorrect path to java.exe/javaw.exe or your Minecraft server jar file. You may just need to change /jre7/ to /jre6/ . Or search your system for java.exe/javaw.exe and adjust the path accordingly. (It's probably under c:\program files or c:\program files (x86).) Also, you must have the offline version of Java installed—not just the Java plug-in for your browser.


Q: Whenever I try to get the server up, it says "Failed to bind to port!".

A: The most common reason this happens is because you put an IP address in the server-ip field in your server.properties file. If the IP you specify isn't the same as any of your network interfaces, (your wireless or wired IPv4 from ipconfig/ifconfig/ip a) Minecraft will throw the port binding failure message. By leaving it blank, you let it bind to all interfaces. You will then be able to connect using localhost and people on your wired/wireless network (in the same subnet) can connect using the computers/server's (private) IP address. 

Alternatively, the error can mean that you have tried to use a port that is already in use or that you do not have permission to use (ports < 1024 are privileged and require root/Administrator access to bind to). You can try a different port by changing it in your server.properties file in this line: server-port=25565.

Note: You should avoid using the following ports for your server as some ISPs may block these ports for security reasons and you shouldn't be running the Minecraft server as root (in the case of a Linux type OS and ports < 1024):

- 21 (Used by most FTP Servers)
- 22 (Used by Secure Shell daemon)
- 25 (Used by Mail Servers for SMTP)
- 53 (Used by DNS Servers)
- 80 (Used by most Web Servers)
- 110 (Used by most Mail Servers for POP3)
- 115 (Used by Simple File Transfer Protocol)
- 143 (Used by Mail Servers for IMAP)
- 443 (SSL port for Web Servers)
- 3306 (Used by most MySQL Servers)

Generally avoid any port below number 1024, since those ports are generally referred as well-known ports and are registered with the IANA for important services.


Q: I tried to run the server with Solaris/OpenSolaris and got the following error:

java.io.InterruptedIOException: Operation interrupted 
at java.net.SocketInputStream.socketRead0(Native Method) 
at java.net.SocketInputStream.read(SocketInputStream.java:129) 
at java.net.SocketInputStream.read(SocketInputStream.java:182) 
at java.io.FilterInputStream.read(FilterInputStream.java:66) 
at gq.a(SourceFile:131) 
at ji.g(SourceFile:197) 
at ji.c(SourceFile:17) 
at oq.run(SourceFile:84) 
2011-05-31 16:57:26 [INFO] /:44673 lost connection

A: For whatever reason, out of all of the operating systems, only Solaris throws that exception when a thread interrupts a connection. A workaround is to change the default behavior on the command line:

java -Xmx1G -Xms32M -XX:-UseVMInterruptibleIO -XX:+UseConcMarkSweepGC \
 -XX:+CMSIncrementalPacing -XX:ParallelGCThreads=$CPU_COUNT -XX:+AggressiveOpts\
 -jar minecraft.jar --nogui

This instructs Java to use an interruptible IO stack instead of the default IO that is sensitive to interrupted threads.


Q: When I try to connect to my server this is what it says:

               Connection lost 
 
The server responded with an invalid server key

A: This error is usually caused when the server sends an unrecognized function to the client, which may be caused by using unrecognized server software, unbalanced client / server versions or modifications to the client.


Q: I cannot break/place any blocks!?

A: This is most usually caused by interacting with blocks in a protected area. If you are trying to interact near spawn, most likely it has been protected, by the Minecraft server software; either build away from it or get operator status.


Q: My server runs fine, but I cannot connect to it!

A: This could be caused by a series of issues. Please post a thread using the template provided above.


Q: How do you give a .jar server more ram?

A: Change the numbers in the server launch command "-Xmx1G -Xms1G". The -Xms part specifies how much memory the server starts with, and the -Xmx part is the maximum amount of memory the server can use.
-Xmx1G -Xms2G = 1GB
-Xmx2G -Xms1G = 2GB
And so on.


Q: Why is the server CPU constantly at full load?

A: Some users are experiences full CPU load on the server. This may be caused by the GUI (graphic user interface) window. Run the server with the --nogui option to disable this window.


Q: Help! How do you find out your server's IP address?

A: Read #Connecting to the Minecraft server


Q: I port forwarded and allowed java.exe in my firewall and it's still not working!

A: Your modem might be acting as a router as well. If you switch ISP's or upgrade your connection to the Internet, you may get issued a modem/router combination (which might explain why it worked in the past).
You can verify this by looking for the WAN IP of your router. If it's a private IP, you'll need to log into the modem/router your ISP issued to you, and configure port forwarding to the WAN IP of your router.


Q: I turned off my firewall on my router/modem how does it still not work???!!! However, port forwarding sites report they can "see" me?? What's going on???!!

A: Turning off your firewall on your router/modem means you essentially disabled port forwarding. Port forwarding is actually a subset of firewall rules. If no rule exists on that port (for example 25565), the firewall will ignore/drop the connection attempt (hence, you get a connection timed out). If there is a rule, it should pass on the connection to whatever computer is configured to receive the initial connection attempt.

When you disable the router/modem firewall and test your public (non RFC 1918) IP address on a port forwarding-checking website, the website will hit your router/modem, and your router/modem will respond, yes you can see me. This is another reason why disabling your firewall is bad; you incorrectly believe that people outside your network can connect to your Minecraft Server on your computer, when really, they're trying to connect to the router/modem itself. 

To solve this, the next step is to confirm if your port forwarding (rules) are correct. By Google-ing "minecraft server checker" you'll be able to check if you configured your network correctly such that users outside your network running the Minecraft client can indeed connect to your computer through your router/modem.

Note: You may need to be careful about the Minecraft Query: it may use layer 4, the transport layer, UDP, to query your server. Many Internet and YouTube guides will only tell you to port forward TCP (this guide outlines that you do both).


Q: What is connection timed out and connection refused?

A: Simply put, connection timed out is when a firewall ignores a connection attempt (ignores the intial connection packet with the SYN flag in the 3-way handshake). Connection refused is when there's no process listening on the port; therefore, the operating system lets the client (in the standard client-server model) know their connection attempt did not work.

The default configuration on all Windows computers (the home version) and (just about) all (SOHO) routers is to drop or time out the connections. This is called "stealth mode" and you can read more about it on superuser. Here's a brief summary: "The idea is that refusing a connection instead of timing it out will tell an attacker that there actually is a computer on that IP-Address. With the connection attempt timing out, the hope is that the attacker will ignore the computer."

You can read more about connection refused on serverfault.

So if your error message is a connection timed out, it's usually a firewall problem; you either need to allow Java in the Windows firewall or port forward. If the error message is a connection refused, perhaps your Minecraft server has not started properly or you turned off the firewall on your router instead of port forwarding.

As always, you can always ask the Minecraft Forum if you are uneasy or unsure about something, particularly if opening the command prompt/terminal and running commands makes you nervous. 

Connection filtered and connection closed is another way of saying timed out and refused, respectively.

## 
Here are some other tutorials on how to set up a Minecraft server:

- Windows
	- How to make a Minecraft Server in under 10 Minutes! (Port Forward Guide Too!)
	- How to Make a Minecraft Server in 2020 (1.15.2) | 5:43Pt. 2 - Easy: Port Forward | 3:11
	- How to create a Minecraft Server in 2020 tutorial
- Mac OS X
	- How to SET UP MINECRAFT SERVER on Mac OS
	- Port Forward (easy method)
	- Alternative video tutorial on setting up a Minecraft server with Mac
- Linux
	- Linux tutorial for more advanced users
	- How to Install Minecraft Server on CentOS
	- How to make a Minecraft Server on Ubuntu for beginners
- Others
	- How to Set Up Port Forwarding
	- How to Port Forward any Minecraft Server (1.6.2)
	- Alternative port forwarding tutorial for Windows (with pictures)
- Full course
	- Course: How to Make a Server



1. ↑https://tailscale.com/learn/ssh-security-best-practices-protecting-your-remote-access-infrastructure
2. ↑https://www.noip.com/support/knowledgebase/how-to-add-a-srv-record-to-your-minecraft-server-remove-the-port-on-the-end-of-the-url/

| Introductory      |                                                                                                                                                                           |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Basics            | Menu screen<br/>Game terms<br/>                                                                                                                                           |
| Newcomer survival | The first day/beginner's guide<br/>The second day<br/>The third day<br/>Hunger management<br/>Things not to do<br/>Simple tips and tricks<br/>Your first ten minutes<br/> |
| Shelters          | Best biomes for homes<br/>Best building materials<br/>Building and construction<br/>Navigation<br/>Shelters<br/>Shelter types<br/>                                        |

| General                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| General                    | Achievement guide<br/>Advancement guide<br/>Best enchantments guide<br/>Breaking a fall<br/>Breaking bedrock<br/>Combat<br/>Complete main adventure<br/>Creating a village<br/>Downgrading<br/>Dual wielding<br/>End survival<br/>Exploring caverns<br/>Gathering resources on peaceful difficulty<br/>Getting food quickly<br/>Headless pistons<br/>Hitboxes<br/>Horses<br/>Indestructible end crystals<br/>Mapping<br/>Measuring distance<br/>Minecraft in education<br/>Mining Diamonds Fossils Ancient Debris<br/>Diamonds<br/>Fossils<br/>Ancient Debris<br/>Nether hub<br/>Nether portals<br/>Nether survival<br/>Organization<br/>Pillar jumping<br/>Playing with a controller<br/>PvP PvP bases<br/>PvP bases<br/>Spawn-proofing<br/>Summoning jockeys<br/>The Void<br/>Time-saving tips<br/>Thunderstorm survival<br/>Units of measure<br/>Village mechanics Trading<br/>Trading<br/>X-ray glitches<br/> |
| Enchanting<br/>andsmelting | Enchanting mechanics<br/>Anvil mechanics<br/>Automatic smelting<br/>Manual smelting<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

| Challenges                |                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| General                   | Acquiring a conduit<br/>Curing a zombie villager<br/>Defeating temples<br/>Defeating a village raid<br/>Defeating a Nether fortress<br/>Defeating a bastion remnant<br/>Defeating a monster room<br/>Defeating a pillager outpost<br/>Defeating a woodland mansion<br/>Defeating a monument<br/>Defeating an End city<br/>Defeating the Ender dragon<br/>Defeating the Wither<br/>Exploring an ancient city<br/>Obtaining every music disc<br/> |
| Non-standard<br/>survival | Adventure survival<br/>Half hearted hardcore<br/>Hardcore mode<br/>Surviving in a single area indefinitely<br/>Infinite desert survival<br/>Island survival<br/>Manhunt<br/>Mob switch<br/>Nomadic experience<br/>Skywars survival<br/>Superflat survival<br/>Flat survival<br/>Ultra hardcore survival<br/>                                                                                                                                    |
| Challenge maps            | Beating a challenge map<br/>Creating a challenge map<br/>                                                                                                                                                                                                                                                                                                                                                                                       |

| Constructions |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Constructions | Adding beauty to constructions<br/>Airlock<br/>Architectural terms<br/>Building a cruise ship<br/>Building a metropolis<br/>Building a rollercoaster<br/>Building safe homes<br/>Building water features<br/>Color palette<br/>Creating shapes<br/>Defense<br/>Desert shelter<br/>Elevators<br/>Endless circling pool<br/>Furniture<br/>Glazed terracotta patterns<br/>Making nice floors<br/>Pixel art<br/>Ranches<br/>Roof types Curved roofs Roof construction guidelines Roof decorations<br/>Curved roofs<br/>Roof construction guidelines<br/>Roof decorations<br/>Secret door<br/>Settlement guide<br/>Underwater home<br/>Walls and buttresses<br/>Water gate<br/>Water-powered boat transportation<br/> |
| Blockbreaking | Blast chamber<br/>Igniting TNT underwater<br/>Wither cage<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

| Farming        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Blocksanditems | Amethyst<br/>Armor<br/>Azalea<br/>Bamboo<br/>Basalt<br/>Bedrock<br/>Blaze rod<br/>Bone meal<br/>Cactus<br/>Chorus fruit<br/>Clay and mud<br/>Cobblestone<br/>Cocoa bean<br/>Copper<br/>Crops (Beetroot, Carrot, Potato, Wheat)<br/>Dirt<br/>Dragon's Breath<br/>Dripstone<br/>Egg<br/>Fern<br/>Fish<br/>Flower<br/>Froglight<br/>Glow berries<br/>Glow ink sac<br/>Glow lichen<br/>Goat horn<br/>Gold<br/>Hanging roots<br/>Honey<br/>Ice<br/>Iron<br/>Kelp<br/>Lava<br/>Meat<br/>Moss block<br/>Mushroom<br/>Music disc<br/>Nautilus shell<br/>Nether growth<br/>Nether vine<br/>Nether wart<br/>Obsidian<br/>Powder snow<br/>Pumpkin, Melon<br/>Rooted dirt<br/>Sculk growths<br/>Scute<br/>Seagrass<br/>Sea pickle<br/>Snow<br/>Soul soil<br/>Sugar cane<br/>Sweet berries<br/>Tree<br/>Trident<br/>Vine<br/>Villager trading hall<br/>Wither rose<br/>Wool<br/>Duplication<br/> |
| Mobs           | Mob farming<br/>Mob grinding<br/>Monster spawner traps<br/>Allay<br/>Animals<br/>Axolotl<br/>Blaze<br/>Cat<br/>Cave spider<br/>Creeper<br/>Drowned<br/>Ender dragon<br/>Enderman<br/>Frog<br/>Goat<br/>Guardian<br/>Hoglin<br/>Iron golem<br/>Magma cube<br/>Phantom<br/>Piglin bartering farm<br/>Raid<br/>Shulker<br/>Slime<br/>Squid<br/>Turtle<br/>Villager<br/>Wandering trader<br/>Warden<br/>Witch<br/>Wither<br/>Wither skeleton<br/>Zombie<br/>Zombie villager<br/>Zombified piglin<br/>                                                                                                                                                                                                                                                                                                                                                                                   |

| Mechanisms            |                                                                                                                                                                                                                                                                                                                                                                  |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Basicredstone         | Automatic respawn anchor recharger<br/>Basic logic gates<br/>Combination locks<br/>Command block<br/>Flying machines<br/>Hopper<br/>Item sorting<br/>Item transportation<br/>Mechanisms<br/>Observer stabilizer<br/>Randomizers<br/>Redstone music<br/>Redstone tips<br/>Rube Goldberg machine<br/>Shulker box storage<br/>Villager trading hall*Water tram<br/> |
| Detectors             | Block update detector<br/>Comparator update detector<br/>Daylight detector<br/>                                                                                                                                                                                                                                                                                  |
| Minecarts             | Train station<br/>Minecarts Storage Storage system<br/>Storage<br/>Storage system<br/>                                                                                                                                                                                                                                                                           |
| Traps                 | Snow golems<br/>TNT cannons<br/>Trapdoor uses<br/>Trap design<br/>Traps<br/>                                                                                                                                                                                                                                                                                     |
| Pistons               | Piston uses<br/>Piston circuits<br/>Quasi-connectivity<br/>Zero-ticking<br/>Instant repeaters<br/>                                                                                                                                                                                                                                                               |
| Advanced<br/>redstone | Advanced redstone circuits<br/>Arithmetic logic<br/>Calculator<br/>Command stats<br/>Hourly clock<br/>Morse code<br/>Printer<br/>Redstone computers<br/>Redstone telegraph<br/>                                                                                                                                                                                  |

| Servers      |                                                                                                                                                                                                                                                                      |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| General      | Playing on servers<br/>Multiplayer Survival<br/>Spawn jail<br/>Griefing prevention<br/>Joining a LAN world with alternate accounts<br/>                                                                                                                              |
| Server setup | Setting up a server<br/>Server startup script<br/>FreeBSD startup script<br/>OpenBSD startup script<br/>Ubuntu startup script<br/>Setting up a Hamachi server<br/>Setting up a Minecraft Forge server<br/>Setting up a Spigot server<br/>Ramdisk enabled server<br/> |

| Technical                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Technical                   | Improving frame rate<br/>Minecraft help FAQ (IRC channel)<br/>Running the data generator<br/>Update Java<br/>                                                                                                                                                                                                                                                                                                                                            |
| Maps                        | Custom maps<br/>Map downloads<br/>Command NBT tags<br/>Falling blocks<br/>Updating old terrain using MCEdit<br/>                                                                                                                                                                                                                                                                                                                                         |
| Resource packs              | Creating a resource pack<br/>Loading a resource pack<br/>Sound directory<br/>                                                                                                                                                                                                                                                                                                                                                                            |
| Data packs                  | Creating a data pack<br/>Installing a data pack<br/>Custom world generation<br/>                                                                                                                                                                                                                                                                                                                                                                         |
| Creating<br/>Minecraftmedia | Creating videos<br/>Livestreaming<br/>                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Game installation           | Installing snapshots<br/>Installing Minecraft Preview and beta versions<br/>How to get a crash report<br/>Installing Forge mods<br/>Custom Minecraft directory<br/>Playing and saving Minecraft on a thumb drive<br/>Playing and saving Minecraft on a thumb drive with the old launcher<br/>Recover corrupted saved world data<br/>Run Minecraft through Google Drive<br/>Save game data to Dropbox (world data only)<br/>Saved data Dropbox guide<br/> |

| Outdated |                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Outdated | Building micro shelters<br/>Custom texture packs<br/>Door-based iron golem farming<br/>End of light mob farms<br/>Far Lands<br/>How to get a crash report<br/>Installing mods<br/>Man-made lake<br/>Managing slimes in superflat mode<br/>Minecart booster<br/>Potion farming<br/>Repeater reboot system<br/>Survival with no enabled data packs<br/>Update LWJGL<br/>Update Minecraft<br/>Village chaining<br/>Water ladder<br/> |

