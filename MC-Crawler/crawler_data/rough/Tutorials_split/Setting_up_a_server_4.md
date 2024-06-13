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

