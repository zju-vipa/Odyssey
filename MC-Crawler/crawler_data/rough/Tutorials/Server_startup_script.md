# Tutorials/Server startup script
This is an example of possible Minecraft server startup and maintenance script for GNU/Linux distros.

## Contents
- 1 Systemd Script
	- 1.1 Installation
	- 1.2 Setup Instance
	- 1.3 Start/Stop Instances
	- 1.4 Autostart
		- 1.4.1 Enable
		- 1.4.2 Disable
- 2 Init.d Script
	- 2.1 Pre-Requisites
	- 2.2 Download
	- 2.3 Requirements
	- 2.4 Installation
	- 2.5 Uninstall
	- 2.6 Usage
	- 2.7 References
	- 2.8 Extra information
- 3 Alternative Startup Scripts

## Systemd Script
For all modern Servers supporting Systemd. Systemd is the jack of all trades. For Ubuntu, it comes with 15.04 (15.04 is an old version which have had end-of-support, we suggest using later LTS versions instead, but the following contents is fully working in this version).

### Installation
1. Connect to your (v)root server or if you want to run the server on your machine, open a terminal.
2. Become root using su or sudo. To check if you are root, runwhoamito display your username.
3. Next install the necessary packagesapt install openjdk-8-jre-headless curl screen nano bash grep
4. Create the /opt folder if it doesn't already exist:mkdir /opt
5. Create the minecraft group for the minecraft user we'll add in the next step:groupadd minecraft
6. Now you need to create the user for the service:useradd --system --shell /usr/sbin/nologin --home /opt/minecraft -g minecraft minecraft
7. Create the Systemd Unit filenano /etc/systemd/system/minecraft@.serviceand the following:

[Unit]
Description=Minecraft Server %i
After=network.target

[Service]
WorkingDirectory=/opt/minecraft/%i

# Solves the issue where the minecraft server will endlessly restart itself
# See https://askubuntu.com/questions/953920/systemctl-service-timed-out-during-start for more info
Type=simple

PrivateUsers=true
# Users Database is not available from within the unit, only root and minecraft is available, everybody else is nobody

User=minecraft
Group=minecraft

ProtectSystem=full
# Read only mapping of /usr /boot and /etc

ProtectHome=true
# /home, /root and /run/user seem to be empty from within the unit. It is recommended to enable this setting for all long-running services (in particular network-facing ones).

ProtectKernelTunables=true
# /proc/sys, /sys, /proc/sysrq-trigger, /proc/latency_stats, /proc/acpi, /proc/timer_stats, /proc/fs and /proc/irq will be read-only within the unit. It is recommended to turn this on for most services.
# Implies MountFlags=slave

ProtectKernelModules=true
# Block module system calls, also /usr/lib/modules. It is recommended to turn this on for most services that do not need special file systems or extra kernel modules to work
# Implies NoNewPrivileges=yes

ProtectControlGroups=true
# It is hence recommended to turn this on for most services.
# Implies MountAPIVFS=yes

# Set default memory values
Environment="MCMINMEM=512M" "MCMAXMEM=1024M" "SHUTDOWN_DELAY=5" "POST_SHUTDOWN_DELAY=10"
# Change memory values in environment file
EnvironmentFile=-/opt/minecraft/%i/server.conf

# Uncomment this to fix screen on RHEL 8
#ExecStartPre=+/bin/sh -c 'chmod 777 /run/screen'

ExecStart=/bin/sh -c \
    'find -L . \
      -maxdepth 1 \
      -type f \
      -iregex ".*/\\(FTBServer\\|craftbukkit\\|spigot\\|paper\\|forge\\|minecraft_server\\).*jar" \
      -print0 \
      -quit \
    | xargs -0 -I{} \
      /usr/bin/screen -DmS mc-%i \
        /usr/bin/java \
          -server \
          -Xms${MCMINMEM} \
          -Xmx${MCMAXMEM} \
          -XX:+UseG1GC \
          -XX:ParallelGCThreads=2 \
          -XX:MinHeapFreeRatio=5 \
          -XX:MaxHeapFreeRatio=10 \
          -jar {} \
          --nogui'

# Alternative to the above ExecStart. Found to work better as this creates the screen session prior to invoking java to run the server.
# Solves the problem many encountered when starting the service where it would fail with the error 'no screen session found'.
ExecStartPre=/bin/sh -c \
    'find -L . \
      -maxdepth 1 \
      -type f \
      -iregex ".*/\\(FTBServer\\|craftbukkit\\|spigot\\|paper\\|forge\\|minecraft_server\\).*jar" \
      -print0 \
      -quit \
    | xargs -0 -I{} \
      /usr/bin/screen -DmS mc-%i'
ExecStart=/bin/sh -c \
    '/usr/bin/java \
          -server \
          -Xms${MCMINMEM} \
          -Xmx${MCMAXMEM} \
          -XX:+UseG1GC \
          -XX:ParallelGCThreads=2 \
          -XX:MinHeapFreeRatio=5 \
          -XX:MaxHeapFreeRatio=10 \
          -jar {} \ # insert server jar name. i.e. 'server.jar'
          --nogui' 

# Simplified of alternative
ExecStartPre=/bin/sh -c '/usr/bin/screen -dmS mc-%i'
ExecStart=/bin/sh -c '/usr/bin/java -server -Xmx${MCMAXMEM} -Xms${MCMINMEM} -jar server.jar --nogui'

ExecReload=/usr/bin/screen -p 0 -S mc-%i -X eval 'stuff "reload"\\015'

ExecStop=/usr/bin/screen -p 0 -S mc-%i -X eval 'stuff "say SERVER SHUTTING DOWN. Saving map..."\\015'
ExecStop=/bin/sh -c '/bin/sleep ${SHUTDOWN_DELAY}'
ExecStop=/usr/bin/screen -p 0 -S mc-%i -X eval 'stuff "save-all"\\015'
ExecStop=/usr/bin/screen -p 0 -S mc-%i -X eval 'stuff "stop"\\015'
ExecStop=/bin/sh -c '/bin/sleep ${POST_SHUTDOWN_DELAY}'

Restart=on-failure
RestartSec=60s

[Install]
WantedBy=multi-user.target

#########
# HowTo
#########
#
# Create a directory in /opt/minecraft/XX where XX is a name like 'survival'
# Add minecraft_server.jar into dir with other conf files for minecraft server
#
# Enable/Start systemd service
#    systemctl enable minecraft@survival
#    systemctl start minecraft@survival
#
# To run multiple servers simply create a new dir structure and enable/start it
#    systemctl enable minecraft@creative
# systemctl start minecraft@creative
#
# To change specific server memory assignment, create file /opt/minecraft/XX/server.conf (where XX is your server name) and add below lines:
# MCMINMEM=512M
# MCMAXMEM=2048M



### Setup Instance
Now you can Upload your FTB Modpacks into a subfolder of /opt/minecraft/. For example, you would place the modpack "FTB Beyond" in "/opt/minecraft/FTBBeyond" (without spaces in the name).
If you want to run vanilla instances, just create a folder within /opt/minecraft and upload the minecraft_server.jar and create the eula.txt file (using: echo "eula=true" > /opt/minecraft/vanilla/eula.txt).

After you uploaded the minecraft server files, make sure, that "minecraft" is the owner and owning group. To do so just run "ls -la /opt/minecraft". If it is not, run "chown minecraft:minecraft /opt/minecraft/FTBBeyond".
You may also require to complete the installation. For current FTB packages you would run:

cd /opt/minecraft/FTBBeyond
echo "eula=true" > /opt/minecraft/FTBBeyond/eula.txt
su -c "/opt/minecraft/FTBBeyond/FTBInstall.sh" -s "/bin/bash" minecraft

### 
You start your server using "systemctl start minecraft@FTBBeyond" and stop it using "systemctl stop minecraft@FTBBeyond". The part behind the "@" is your instance name e. g. the Folder Name.
This script also takes care to automatically stop your minecraft server if you reboot the server.

### Autostart
#### Enable
systemctl enable minecraft@FTBBeyond
#### Disable
systemctl disable minecraft@FTBBeyond
## Init.d Script
For legacy Servers which don't have OS-integrated Systemd

### Pre-Requisites
Screen package must be installed.
On CentOs and Red Hat-based distributions: 

yum install screen
On Debian based systems such as Ubuntu:

apt-get install screen python
### Download
To download the script with wget, run the following (WATCH OUT SCRIPT NEEDS WORK: change the WORLD, MCPATH and BACKUPPATH variables.
Important: If you use the wget method and the first character of every line is an empty space, the script won't work and update-rc.d outputs errors. If so, you have to remove the leading empty spaces from each line. Be careful not to delete anything else than empty space though!)

wget -O minecraft "http://minecraft.wiki/Tutorials/Server_startup_script/Script?action=raw"
 #!/bin/bash
 # /etc/init.d/minecraft
 # version 0.4.2 2016-02-09 (YYYY-MM-DD)
 #
 ### BEGIN INIT INFO
 # Provides:   minecraft
 # Required-Start: $local_fs $remote_fs screen-cleanup
 # Required-Stop:  $local_fs $remote_fs
 # Should-Start:   $network
 # Should-Stop:    $network
 # Default-Start:  2 3 4 5
 # Default-Stop:   0 1 6
 # Short-Description:    Minecraft server
 # Description:    Starts the minecraft server
 ### END INIT INFO
 
 #Settings
 SERVICE='minecraft_server.jar'
 SCREENNAME='minecraft_server'
 OPTIONS='--nogui'
 USERNAME='minecraft'
 WORLD='world'
 MCPATH='/home/minecraft'
 BACKUPPATH='/minecraft/minecraft.backup'
 MAXHEAP=2048
 MINHEAP=1024
 HISTORY=1024
 CPU_COUNT=1
 INVOCATION="java -Xmx${MAXHEAP}M -Xms${MINHEAP}M -XX:+UseConcMarkSweepGC \
 -XX:+CMSIncrementalPacing -XX:ParallelGCThreads=$CPU_COUNT -XX:+AggressiveOpts \
 -jar $SERVICE $OPTIONS" 
 
 ME=`whoami`
 as_user() {
   if [ "$ME" = "$USERNAME" ] ; then
     bash -c "$1"
   else
     su - "$USERNAME" -c "$1"
   fi
 }
 
 mc_start() {
   if  pgrep -u $USERNAME -f $SERVICE > /dev/null ; then
     echo "$SERVICE is already running!"
   else
     echo "Starting $SERVICE..."
     cd $MCPATH
     as_user "cd $MCPATH && screen -h $HISTORY -dmS ${SCREENNAME} $INVOCATION"
     sleep 7
     if pgrep -u $USERNAME -f $SERVICE > /dev/null ; then
       echo "$SERVICE is now running."
     else
       echo "Error! Could not start $SERVICE!"
     fi
   fi
 }
 
 mc_saveoff() {
   if pgrep -u $USERNAME -f $SERVICE > /dev/null ; then
     echo "$SERVICE is running... suspending saves"
    as_user "screen -p 0 -S ${SCREENNAME} -X eval 'stuff \"say SERVER BACKUP STARTING. Server going readonly...\"\015'"
     as_user "screen -p 0 -S ${SCREENNAME} -X eval 'stuff \"save-off\"\015'"
     as_user "screen -p 0 -S ${SCREENNAME} -X eval 'stuff \"save-all\"\015'"
     sync
     sleep 10
   else
     echo "$SERVICE is not running. Not suspending saves."
   fi
 }
 
 mc_saveon() {
   if pgrep -u $USERNAME -f $SERVICE > /dev/null ; then
     echo "$SERVICE is running... re-enabling saves"
     as_user "screen -p 0 -S ${SCREENNAME} -X eval 'stuff \"save-on\"\015'"
     as_user "screen -p 0 -S ${SCREENNAME} -X eval 'stuff \"say SERVER BACKUP ENDED. Server going read-write...\"\015'"
   else
     echo "$SERVICE is not running. Not resuming saves."
   fi
 }
 
 mc_stop() {
   if pgrep -u $USERNAME -f $SERVICE > /dev/null ; then
     echo "Stopping $SERVICE"
     as_user "screen -p 0 -S ${SCREENNAME} -X eval 'stuff \"say SERVER SHUTTING DOWN IN 10 SECONDS. Saving map...\"\015'"
     as_user "screen -p 0 -S ${SCREENNAME} -X eval 'stuff \"save-all\"\015'"
     sleep 10
     as_user "screen -p 0 -S ${SCREENNAME} -X eval 'stuff \"stop\"\015'"
     sleep 7
   else
     echo "$SERVICE was not running."
   fi
   if pgrep -u $USERNAME -f $SERVICE > /dev/null ; then
     echo "Error! $SERVICE could not be stopped."
   else
     echo "$SERVICE is stopped."
   fi
 }
 
 mc_update() {
   if pgrep -u $USERNAME -f $SERVICE > /dev/null ; then
     echo "$SERVICE is running! Will not start update."
   else
     as_user "cd $MCPATH && wget -q -O $MCPATH/versions --no-check-certificate https://piston-meta.mojang.com/mc/game/version_manifest.json"
     if [ "$1" == "snapshot" ] ; then
       JSONVERSION=`cd $MCPATH && cat versions | python -c "exec(\"import json,sys\nobj=json.load(sys.stdin)\nversion=obj['latest']['snapshot']\nfor v in obj['versions']:\n   if v['id']==version:\n    print(v['url'])\")"`
     else
       JSONVERSION=`cd $MCPATH && cat versions | python -c "exec(\"import json,sys\nobj=json.load(sys.stdin)\nversion=obj['latest']['release']\nfor v in obj['versions']:\n   if v['id']==version:\n    print(v['url'])\")"`
     fi
     as_user "cd $MCPATH && wget -q -O $MCPATH/versions --no-check-certificate $JSONVERSION"
     MC_SERVER_URL=`cd $MCPATH && cat versions | python -c 'import json,sys;obj=json.load(sys.stdin);print(obj["downloads"]["server"]["url"])'`
     as_user "rm $MCPATH/versions"
     as_user "cd $MCPATH && wget -q -O $MCPATH/minecraft_server.jar.update --no-check-certificate $MC_SERVER_URL"
     if [ -f $MCPATH/minecraft_server.jar.update ] ; then
       if `diff $MCPATH/$SERVICE $MCPATH/minecraft_server.jar.update >/dev/null` ; then
         echo "You are already running the latest version of $SERVICE."
       else
         as_user "mv $MCPATH/minecraft_server.jar.update $MCPATH/$SERVICE"
         echo "Minecraft successfully updated."
       fi
     else
       echo "Minecraft update could not be downloaded."
     fi
   fi
 }
 
 mc_backup() {
    mc_saveoff
    
    NOW=`date "+%Y-%m-%d_%Hh%M"`
    BACKUP_FILE="$BACKUPPATH/${WORLD}_${NOW}.tar"
    echo "Backing up minecraft world..."
    #as_user "cd $MCPATH && cp -r $WORLD $BACKUPPATH/${WORLD}_`date "+%Y.%m.%d_%H.%M"`"
    as_user "tar -C \"$MCPATH\" -cf \"$BACKUP_FILE\" $WORLD"
 
    echo "Backing up $SERVICE"
    as_user "tar -C \"$MCPATH\" -rf \"$BACKUP_FILE\" $SERVICE"
    #as_user "cp \"$MCPATH/$SERVICE\" \"$BACKUPPATH/minecraft_server_${NOW}.jar\""
 
    mc_saveon
 
    echo "Compressing backup..."
    as_user "gzip -f \"$BACKUP_FILE\""
    echo "Done."
 }
 
 mc_command() {
   command="$1";
   if pgrep -u $USERNAME -f $SERVICE > /dev/null ; then
     pre_log_len=`wc -l "$MCPATH/logs/latest.log" | awk '{print $1}'`
     echo "$SERVICE is running... executing command"
     as_user "screen -p 0 -S ${SCREENNAME} -X eval 'stuff \"$command\"\015'"
     sleep .1 # assumes that the command will run and print to the log file in less than .1 seconds
     # print output
     tail -n $((`wc -l "$MCPATH/logs/latest.log" | awk '{print $1}'`-$pre_log_len)) "$MCPATH/logs/latest.log"
   fi
 }

 mc_listen() {
   if pgrep -u $USERNAME -f $SERVICE > /dev/null ; then
     as_user "tail -f $MCPATH/logs/latest.log"
   else
     echo "$SERVICE is not running. Cannot listen to server."
   fi
}

 
 #Start-Stop here
 case "$1" in
   start)
     mc_start
     ;;
   stop)
     mc_stop
     ;;
   restart)
     mc_stop
     mc_start
     ;;
   update)
     mc_stop
     mc_backup
     mc_update $2
     mc_start
     ;;
   backup)
     mc_backup
     ;;
   status)
     if pgrep -u $USERNAME -f $SERVICE > /dev/null ; then
       echo "$SERVICE is running."
     else
       echo "$SERVICE is not running."
     fi
     ;;
   command)
     if [ $# -gt 1 ] ; then
       shift
       mc_command "$*"
     else
       echo "Must specify server command (try 'help'?)"
     fi
     ;;
   listen)
     mc_listen
     ;;
 
   *)
   echo "Usage: $0 {start|stop|update|backup|status|restart|command \"server command\"}"
   exit 1
   ;;
 esac
 
 exit 0

### Requirements
- screen
- python (apt-get install python)

### Installation
Use your favorite editor to create file called minecraft in /etc/init.d/ and paste the script above in that file.

Edit the USERNAME and MCPATH -variables according to your setup.  If you use a wrapper script, change INVOCATION to start it instead of starting the server directly.

Make sure the newly created file has required permissions
You can set the permissions by running:

chmod a+x /etc/init.d/minecraft
Then run (on Debian-based distributions)

update-rc.d minecraft defaults
Starting with Debian 6.0, the insserv command is used instead, if dependency-based booting is enabled.
insserv will produce no output if everything went OK. Examine the error code in $? if you want to be sure.

insserv minecraft
On CentOs and RHEL(Redhat enterprise Linux)
You will need to add the process into the chkconfig list chkconfig manages startup scripts under systemd

chkconfig --add minecraft
To check if the process is done correctly use the ntsysv command keep scrolling until you see the minecraft process if you don't
repeat the chkconfig command. 
to add required symbolic links.
Note: your system will most likely warn you that the script does not meet all requirements. The script will however work.

You can also setup an entry in your crontab to backup the server.
A sample crontab to backup every half hour on the hour, and 30 minutes into the hour:

- Using the user account you want the work done under, run:

crontab -e
and add this

0,30 * * * * /etc/init.d/minecraft backup
If the process is unsuccessful, try:

VISUAL=/usr/bin/nano crontab -e
### Uninstall
(In debian based GNU/Linux distribution)

update-rc.d -f  minecraft remove
(In CentOs/RHEL)

chkconfig --del minecraft
### Usage
The script may be invoked via the following command on most systems, where "(command)" will be "stop", "start", "restart", or any of the other options it supports.

/etc/init.d/minecraft (command)
On most RedHat- or Debian-based distribution where the `service` command is available, it should be invoked as:

service minecraft (command)
To view the screen, use:

screen -r
To exit the screen, use:

CTRL+a+d
### References
- http://www.debian-administration.org/articles/28
- https://wiki.debian.org/LSBInitScripts/DependencyBasedBoot

### Extra information
If you still want to view the live log file, use this command in the server directory.

tail -f logs/latest.log
## Alternative Startup Scripts
The following scripts offer the same functions as the above script but contain more useful features:

- mcwrapper

- [Multi World] Minecraft Server Control Script
	- Run multiple Minecraft worlds.
	- Start, stop, and restart single or multiple worlds.
	- Create, delete, disable, and enable worlds.
	- SupportsCraftBukkitin addition to the standard Mojang server distribution.
	- Users automatically notified of important server events.
	- Uses theMinecraft Query protocolto keep track of current server conditions.
	- LSB and systemd compatible init script, allows for seamless integration with your server's startup and shutdown sequences.
	- Map worlds using theMinecraft Overviewermapping software.
	- Backup worlds, and remove backups older than X days.
	- Update the server software and installed addons.
	- Send commands to a world server from the command line.

- minecraftd
	- Start, stop, and restart the server using either systemd or the script directly
	- Send commands to a server from the command line
	- Backup server (world, plugins, configuration, etc.), and purge old ones (configurable)
	- Suspend server if no player is logged in and bring it up as soon as one tries to join to maximazie efficiency
	- Purely written in bash and condensed features in about 500 lines of code to keep the foorprint small
	- Flexible configuration: support for e.g. spigot/craftbukkit, adjustable threads and RAM usage, etc.
	- Full systemd support with init and backup script
	- Secure resource usage: run script as different user and drop permissions if not requiered
	- Very similar to the script described in this article: It as well uses screen and tar but offers more advanced features
	- ExcellentArch Linux support

- MC Sheller

- Minecraft Systemd ServiceA nice systemd service that features:
	- safe shutdown using rcon
	- protection of the system by making most of the system readonly
	- uses systemd journal to log
	- can be combined with a nicecommandcenter script
	- is fully integrated in the systemd-toolchain

- minecraft init
	- modification of this script with a lot more features like multiworld

- Minecraft Service

- Dagmar d'Surreal's Sysv init script

- Setsuna-Xero's OpenRC(Gentoo) compatible init script, with conf.d defaults

- Mineserv Perl Init Script
	- A very simple automatic start/stop script with backup and cleanup functions and the ability to pass commands to the server console.

- McSrv Script by 7thCore
	- Bash language only script
	- Only uses systemd
	- Start, stop, backup functions and much more
	- Multi instance support
	- TmpFs/Ramdisk support that can be configured for each instance
	- Vanilla server automatic updates
	- Can run vanilla, forge and spigot jar files
	- Pre-built packages for Arch and Debian based systems that also install all dependancies
	- Discord integration. Sends notifications on start, stop, crashd and update events
	- Email integration. Sends emails on start, stop, crash and update events. Crash events also include logs in the email
	- More documentation available on the project's GitHub Wiki

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

