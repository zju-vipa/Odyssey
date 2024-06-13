# Tutorials/Ramdisk enabled server
This tutorial is intended to give you a basic understanding of what a ramdisk is, what use it is for Minecraft and how to make a Minecraft server use a ramdisk.

## Contents
- 1 Ramdisk introduction
- 2 Advantages
- 3 Disadvantages
- 4 Why it makes sense for Minecraft servers
- 5 Basic Minecraft and ramdisk setup
	- 5.1 GNU/Linux (easy way)
	- 5.2 GNU/Linux (alternative)
	- 5.3 GNU/Linux (quick & dirty)
	- 5.4 Windows
	- 5.5 macOS

## Ramdisk introduction
Conventionally, files and directories are stored on hard disk drives which, by today's standards, offer a lot of space at mediocre data transfer rates (between 80MB/s and 200MB/s). Ramdisks are virtual file systems (unlike HDDs which are hardware) that live completely inside the computer's RAM. They offer significantly higher data transfer rates (between 3,000MB/s and 15,000MB/s) at the cost of volatility (data is lost after restarting the computer) and space (limited by the amount of RAM installed on the system, including swap space). Many utilities however make it possible to backup Ramdisk data at set intervals, and before the system is shut down, then load the last data when the system starts up.

## Advantages
- Very high transfer speed (data to application)
- Very low seek time (searching between and in files)

## Disadvantages
- Ramdisks are cleared when a system restarts (Not true for Dataram RAMDisk)
- Unfeasible if the world size exceeds the available RAM

## Why it makes sense for Minecraft servers
In a Minecraft server, one of the strongest bottlenecks are disk I/O related operations (e.g. chunk management). By moving the data into the RAM, access times are near instant and data transfer rates become significantly faster, making chunk loading and saving much faster operations. Since a Minecraft world currently consists of very many chunk files, seek time is equally, if not more, important for overall speed.

## Basic Minecraft and ramdisk setup
Make sure to back up your files before starting!

### 
A simple way to load a minecraft server into a ramdisk was posted on the Aimless Bits blog [1] on March 12, 2011. It involves modifying the server startup script available on the wiki and making some minor changes to fstab. This guide fleshes out the process and makes some minor changes to Aimless Bits' script.

This quick guide assumes you have a user for loading minecraft, a minecraft directory and a server running. It also helps to be familiar with the /etc/init.d/minecraft startup script.

- Firstly, start by creating a directory for the ramdisk in your home directory, i.e. "/home/username/minecraft_ramdisk".
- To mount it as a ramdisk, simply edit your /etc/fstab/ file:

sudo nano /etc/fstab

Then add this line, making sure that the path is correct (username, dir name etc.)

tmpfs  /home/username/minecraft_ramdisk tmpfs  defaults,size=512m      0       0

The size of the ramdisk MUST be larger than the minecraft directory world. Make sure that you give yourself some overhead.

- Restart your computer. The ramdisk then loads every time you restart. If you wish to load immediately, type

mount -t tmpfs none /home/username/minecraft_ramdisk -o size=512m

It's now a matter of simply running a modified script that loads the files on the drive onto the server, copies them back on a timely basis to prevent data loss, and does backups. Again, this is a modified version of the script found at Aimless Bits.

If you have /etc/init.d/minecraft, delete it or overwrite it with this script. If you don't, make a new text file, call it minecraft, and copy this script into it.

#!/bin/bash
# /etc/init.d/minecraft
# version 0.9 (Sasquatch) 2016-04-29 (YYYY-MM-DD)

### BEGIN INIT INFO
# Provides:   minecraft
# Required-Start: $local_fs $remote_fs
# Required-Stop:  $local_fs $remote_fs
# Should-Start:   $network
# Should-Stop:    $network
# Default-Start:  2 3 4 5
# Default-Stop:   0 1 6
# Short-Description:    Minecraft RAMDISK Server
# Description:    Starts the minecraft server via ramdisk
### END INIT INFO

# SERVER SETTINGS
JARFILE="spigot.jar"
USERNAME="minecraft"
MCSTORE="/home/$USERNAME/server_store"
MCPATH="/home/$USERNAME/ramdisk"
BACKUPPATH="/home/$USERNAME/backups/"
WORLD='world'

# Machine Settings
CPU_COUNT=8
MAX_RAM=8048
START_RAM=2048

# JAVA INVOCATION
INVOCATION="java -Xmx${MAX_RAM}M -Xms${START_RAM}M -server -jar $JARFILE -o false"

# COLOR CODES
NOR="\e[0m"
BOL="\e[1m"
GRE="\e[32m"
RED="\e[31m"
YEL="\e[33m"

# ERRORS
LAST_BACK="${RED}${BOL}Last $WORLD.bak still exists!${NOR} The server may have crashed. ${YEL}Please check logs.${NOR}\n"

check_java() {
  if java -version 2>&1 >/dev/null | grep -q "java version" ; then
    return 1
  else 
	return 0
  fi
}

check_ramdisk() {
  if ! df -h | grep -q $MCPATH ; then
	return 1
  else
	return 0
  fi
}

as_user() {
  if [ "`whoami`" == "$USERNAME" ] ; then
    bash -c "$1"
  else
    su - $USERNAME -c "$1"
  fi
}

mc_status() {
  ps aux |grep -F -v grep|grep -F -v SCREEN|grep -F --quiet $JARFILE
  return $?
}

mc_start() {
  if check_java ; then
    if mc_status ; then
      echo -e "${YEL}Tried to start but $JARFILE was already running!${NOR}"
    else
	  #if ! df -h | grep -q $MCPATH ; then
      #  echo -e "${YEL}Starting RAMDISK...${NOR}\n"
      #  start_ramdisk
      #fi	  
      echo -e "${YEL}Starting ${JARFILE}...${NOR}"
      if [ -d $MCSTORE/$WORLD.bak ]; then
        echo -e $LAST_BACK
        exit 1
      fi
      cd $MCPATH
      if [ ! -f "$MCPATH/$JARFILE" ]; then 
        echo -e "${YEL}RAMDISK is empty...  prepping.${NOR}"
        as_user "cp -R $MCSTORE/* $MCPATH/"
      fi
      as_user "cd $MCPATH && screen -dmS minecraft $INVOCATION"
      sleep 7
      if mc_status; then
        echo -e "${GRE}${JARFILE} is now running.${NOR}"
      else
        echo -e "${RED}${BOL}Could not start $JARFILE.${NOR}"
      fi
    fi
  else
    exit 1
  fi
}

mc_saveoff() {
  if mc_status; then
    echo -e "${YEL}${JARFILE} is running... suspending saves.${NOR}"
    TO_SCREEN="screen -p 0 -S minecraft -X eval 'stuff "
    as_user "$TO_SCREEN \"say SERVER BACKUP STARTING. Server going readonly...\"\015'"
    as_user "$TO_SCREEN \"save-off\"\015'"
    as_user "$TO_SCREEN \"save-all\"\015'"
    sync
    sleep 10
  else
    echo -e "${RED}${BOL}${JARFILE} was not running.${NOR} ${YEL}Not suspending saves.${NOR}"
  fi
}

mc_saveon() {
  if mc_status; then
    echo -e "${YEL}$JARFILE is running... re-enabling saves${NOR}"
    TO_SCREEN="screen -p 0 -S minecraft -X eval 'stuff "
    as_user "$TO_SCREEN \"save-on\"\015'"
    as_user "$TO_SCREEN \"say SERVER BACKUP ENDED. Server going read-write...\"\015'"
  else
    echo -e "${RED}${BOL}${JARFILE} was not running.${NOR} ${YEL}Not resuming saves.${NOR}"
  fi
}

mc_stop() {
  if mc_status; then
    echo -e "${YEL}${JARFILE} is running... stopping.${NOR}"
    TO_SCREEN="screen -p 0 -S minecraft -X eval 'stuff "
    as_user "$TO_SCREEN \"say SERVER SHUTTING DOWN IN 5 SECONDS. Saving map...\"\015'"
    as_user "$TO_SCREEN \"save-all\"\015'"
    sleep 5
    as_user "$TO_SCREEN \"stop\"\015'"
    sleep 5
  else
    echo -e "${RED}${JARFILE} was not running.${NOR}"
  fi

  if mc_status; then
    echo -e "${RED}{$BOL}${JARFILE} could not be shut down... still running.${NOR}"
  else
    echo -e "${GRE}$JARFILE is stopped.${NOR}"
  fi
}


mc_update() {
  if mc_status; then
    echo -e "${RED}${BOL}${JARFILE} is running!{$NOR} ${YEL}Will not start update.${NOR}"
  else
    MC_SERVER_URL=http://minecraft.net/`wget -q -O - http://www.minecraft.net/download.jsp | grep minecraft_server.jar\</a\> | cut -d \" -f 2`
    as_user "cd $MCPATH && wget -q -O $MCPATH/minecraft_server.jar.update $MC_SERVER_URL"
    if [ -f $MCPATH/minecraft_server.jar.update ]; then
      if `diff $MCPATH/$JARFILE $MCPATH/minecraft_server.jar.update >/dev/null`
     then 
       echo -e "${YEL}You are already running the latest version of ${BOL}${JARFILE}${NOR}${YEL}.${NOR}"
	   rm $MCPATH/minecraft_server.jar.update >/dev/null
     else
       as_user "mv $MCPATH/minecraft_server.jar.update $MCPATH/$JARFILE"
       echo -e "${GRE}${BOL}Minecraft successfully updated.${NOR}"
      fi
    else
      echo -e "${RED}${BOL}Minecraft update could not be downloaded.${NOR}"
    fi
  fi
}

mc_backup() {
   echo -e "${YEL}Backing up minecraft files...${NOR}"
   as_user "tar zcf $BACKUPPATH/MCBKUP_`date "+%Y.%m.%d-%H"`.tar.gz $MCSTORE"
   echo -e "${GRE}Backup complete!${NOR}"
}

mc_rdsave() {
  if mc_status; then
    echo -e "${YEL}Saving RAMDISK...${NOR}"
    if [ ! -f $MCPATH/$JARFILE ]; then
      echo -e "${RED}${BOL}Error: Minecraft not in RAMDISK${NOR}"
    else
      if [ -d $MCSTORE/$WORLD.bak ]; then
        echo -e $LAST_BACK
        exit 1
      fi
      if [ -d $MCSTORE/$WORLD ]; then
        as_user "mv $MCSTORE/$WORLD $MCSTORE/$WORLD.bak"
      fi

      TO_SCREEN="screen -p 0 -S minecraft -X eval 'stuff "
      as_user "$TO_SCREEN \"save-off\"\015'"
      as_user "$TO_SCREEN \"save-all\"\015'" 
      as_user "cp -R $MCPATH/* $MCSTORE/"
      as_user "$TO_SCREEN \"save-on\"\015'"

      if [ -d $MCSTORE/$WORLD.bak ]; then
        as_user "rm -r $MCSTORE/$WORLD.bak"
      fi
    fi
  else
    echo -e "${RED}Service is not running.${NOR}"
 fi

}

mc_rdhalt() {
   echo -e "${YEL}Saving RAMDISK...${NOR}"
   if [ ! -f $MCPATH/$JARFILE ]; then 
     echo -e "${RED}${BOL}Error: Minecraft not in RAMDISK${NOR}"
   else
     if [ -d $MCSTORE/$WORLD.bak ]; then
        echo -e $LAST_BACK
        exit 1
     fi
     if [ -d $MCSTORE/$WORLD ]; then
       as_user "mv $MCSTORE/$WORLD $MCSTORE/$WORLD.bak"
     fi

     echo -e "${GRE}Saved.${NOR} Screen session closed."
     as_user "cp -R $MCPATH/* $MCSTORE/"
	 as_user "rm -rf $MCPATH/*"

     if [ -d $MCSTORE/$WORLD.bak ]; then
       as_user "rm -r $MCSTORE/$WORLD.bak"
     fi
   fi
}

#Start-Stop here
case "$1" in
  cjava)
    if check_java ; then
      echo -e "${BOL}Oracle Java 7${NOR} or higher is required to run Minecraft Server. (Oracle Java 8 Recommended)\n"
	else
	  echo -e "${GRE}Java is installed!${NOR}"
	fi
	;;
  cramdisk)
    if check_ramdisk ; then
	  echo -e "${BOL}${RED}RAMDISK is offline!${NOR}\n"
	else
	  echo -e "${GRE}RAMDISK is online.${NOR}"
	fi
	;;
  start)
    check_java
    mc_start
    ;;
  stop)
    mc_stop
    mc_rdhalt
    ;;
  restart)
    mc_stop
    mc_rdhalt
    mc_start
    ;;
  update)
    mc_stop
    mc_backup
    mc_update
    mc_start
    ;;
  backup)
    mc_rdsave
    mc_saveoff
    mc_backup
    mc_saveon
    ;;
  disksavehalt)
    mc_rdhalt
    ;;
  disksaverun)
    mc_rdsave
    ;;
  status)
    if mc_status; then
      echo -e "${GRE}${JARFILE} is running.${NOR}"
    else
      echo -e "${RED}${JARFILE} is not running.${NOR}"
    fi
    ;;
  cmd)
    TO_SCREEN="screen -p 0 -S minecraft -X eval 'stuff "
    as_user "$TO_SCREEN \"${2}\"\015'"
	sleep .5
	awk '/./{line=$0} END{print line}' ${MCPATH}/logs/latest.log
    ;;
  *)
  echo "Usage: /etc/init.d/minecraft {start|stop|restart|cmd|update|backup|status|cramdisk|cjava|disksaverun}"
  exit 1
  ;;
esac

- Move this script into your /etc/init.d/ directory, and make it executable:

mv /directory/wherefileis/filename /etc/init.d/minecraft
chmod a+x /etc/init.d/minecraft

Note:  This script misses the command option that the other minecraft init script has on this website, server startup script. Therefore, the script is rewritten with the command code in it, so ramdisk servers can also use the command thing to sync things without having to get another plugin to schedule things: http://pastebin.com/4ynwL2js


You're almost done! This script behaves exactly like the standard startup script, only that it takes care of loading and maintaining the ramdisk. You can also modify the script to use rsync instead of cp

"rsync -r -t $MCSTORE/ $MCPATH/"

In case you want to do other things, such as remote copying, but performance differences are probably negligible unless you have very big worlds.

- DO NOT SKIP THIS STEP. You need to add a crontab entry to save your world. See below for specific reasons, but you run the risk of losing data if you don't do this. This script has two disk save functions, disksavehalt and disksaverun. Disksavehalt assumes the screen session is closing or backing up, and thus does not disable level saving. Do NOT call this function in crontab. Use disksave run instead. To do this

sudo crontab -e

Then add the line:

*/5 * * * * /etc/init.d/minecraft disksaverun
20 */6 * * * /etc/init.d/minecraft backup

The number represents how often in minutes should you save the world. If you feel like you have a robust setup, power supply backups and the whole shebang, run this less frequently. Otherwise, stick to 5 minutes at the least! 

The other line runs minecraft backup every 6 hours, at :20. Don't skimp on backups! You've been warned!

Hope this helps all those would be admins out there. Good luck!

### 
On most GNU/Linux distributions there is already a ramdisk set up (usually mounted to /dev/shm (shared memory)) which defaults to using at most half of your total installed RAM. If there is not one already set up, resources on how to do it are widely available on the Internet.

It is possible to move anything into the ramdisk, but this tutorial focuss on just moving the map into it and leaving the server files on the conventional drive.

Given the following basic server directory "minecraft_server/", inside a user's home directory, containing the world "world" and all other required files

| ~/minecraft_server/  |
|----------------------|
| world/               |
| minecraft_server.jar |
| server.log           |
| server.properties    |
| ...                  |

We want to move "world/" into the shared memory. Because of the volatility of ramdisks, we also want to create a new folder into which an automated script periodically saves the current snapshot of the world, called (for example) "world_storage" by copying the current world to a new name

$ cd ~/minecraft_server/
$ cp -r world/ world_storage/

Now with the old world in a safe location, we can go ahead and move the world into the ram-disk

$ mkdir /dev/shm/minecraft
$ mv world/ /dev/shm/minecraft

By now, the world is loaded into the RAM, but the Minecraft server doesn't see it in its directory anymore, causing it to recreate it when started. To stop it from doing that, we have to create a symbolic link to the world in the ramdisk by running

$ ln -s /dev/shm/minecraft/world/ .

This creates a link to "/dev/shm/minecraft/world/" called "world/" in the server's directory, which the server uses like the actual world folder, but now inside the RAM.

Now we need to take care of the volatility of the ramdisk, by periodically saving the world from the RAM into "world_storage/". I'm going to use cron for scheduling and rsync for synching here.

First, we need a script that can be called by cron (it doesn't have to be a script, you could call rsync directly from the cron command line, but this allows for easy customizing later on)

#!/bin/sh

VOLATILE="/home/$USER/minecraft_server/world/"
PERMANENT="/home/$USER/minecraft_server/world_storage/"

#TODO: Check if both directories actually exist, skipped here for clearness
rsync -r -t -v "$VOLATILE" "$PERMANENT"

And then we need to make this script execute every few minutes (I'll use 5 minutes here, you can test out what works best for you)

$ crontab -e

This opens an editor (more precisely, the editor in your "EDITOR" environment variable) for editing your user cron table. Add the following line:

*/5 * * * * bash /home/<your_username>/minecraft_server/save_world.sh &>/dev/null

Now if your server restarts, you must recreate the world folder (/dev/shm/minecraft) then (/dev/shm/minecraft/world) in the shared memory because the /dev/shm/ empties after restart,. You can do this by making another similar shell script.

So make a shell script file like before:

exec 1>/tmp/backup_world.log 2>&1 #sends the output to this file
#!/bin/sh
#remake the paths
mkdir /dev/shm/minecraft
mkdir /dev/shm/minecraft/world

VOLATILE="/home/$USER/minecraft_server/world/"
PERMANENT="/home/$USER/minecraft_server/world_storage/"

#TODO: Check if both directories actually exist, skipped here for clearness
#reversed the order
rsync -r -t -v "$PERMANENT" "$VOLATILE"

Every time you restart you need to run this script to remount the Ramdisk. Do not add this to the crontab. You can add this to the start up if you figure it out.



### 
This is a quick and dirty (but functionally identical) version of the GNU/Linux alternative listed above. Here, this technique is used with a Fedora-based server and it works great. 

Start from your working server directory and copy the existing world to a backup location:

cp -r world/ world_storage/

- You might want to keep an additional backup copy of the world as well, in case something goes wrong.

We need the directory name "world" to make this work, so remove world/ from the working directory:

rm world/ -rf

Now, we want to redirect the server to a world directory in shared memory. Do this by creating a soft link from shared memory to your working directory:

ln -s /dev/shm/world/ .

Shared memory is volatile, so we need something to back up the world directory to disk periodically. A single line in crontab does the trick:

*/5 * * * * rsync -r -t -v /dev/shm/world/ /path_to_minecraft/world_storage/

Now we need a way to "mount" the world in shared memory. Create a start.sh file and include the following 2 lines:

cp /path_to_minecraft/world_storage/ /dev/shm/world/ -r
rsync -r -t -v /dev/shm/world/ /path_to_minecraft/world_storage/

You can use the start.sh script to mount your world in shared memory each time you reboot your server. Then you can start the Minecraft server as normal (or add a 3rd line to start.sh for convenience). If you choose to start the server with start.sh and use the screen command, be sure to start the start.sh script with screen. Using screen inside the script causes the server to run in the background, leaving you unable to run console commands.

### Windows
Use a Ramdisk utility like Dataram RAMDisk (freeware version available) to create a RAM disk and place the server files on it. Dataram RAMDisk has the option to automatically save an image every time it shuts down and also every few minutes. The free version restricts its maximum disk space to 1G. If larger Ramdisks are required, the Winramtech and the Softperfect Ramdisks seem to offer the best performance with similar features as Dataram RAMDisk.

Before you begin:

- At least 4G of RAM on your machine is ideal
- Enabling "Save Disk Image on Shutdown" impacts your Windows shutdown times where you leave RAMDisk running on shutdown, and similarly startup times for "Load Disk Image on Startup". This is not a problem if you manually start and stop the server only when needed.
- Search the Internet for some ways to save your RAMDisk in case it does not work.
- FAT16 isgenerallyfaster than FAT32 on RAM disks, however FAT16 formatting is not available for partitions over 2048MB
- REMEMBER:Always have a backup!If your computer crashes, you lose any data on the RAM disk that has not been backed-up/copied to your hard drive!
- Make sure that you allocate more than enough memory for the RAM disk than that of the size of your 'Minecraft Server' folder. Remember that the Minecraft world data can increase by a lot!
- ...and on the other hand, don't leave too little RAM remaining for the running of Windows and the server itself.

Setting up your RAM disk (Simple usage)

1. Download and installDataram RAMDisk
2. Set your disk size (Setting the maximum is not recommended)
3. If the disk size you set was 2048MB or less, choose 'FAT16 Partition', otherwise choose 'FAT32 Partition' (Advanced users may wish to select 'unformatted' and format the disk themselves)
4. Go under the Load/Save tab and select all three RAMDisk saving methods ("AutoSave", "Save Disk Image on Shutdown" and "Load Disk Image on Startup")
5. Click 'Start RAMDisk'
6. Now go to 'My Computer' and you should see a new disk
7. Open it and copy all your Minecraft Server files in it.
8. Start your server per usual, now from the RAM disk you have just created. You are now up and running!

Your RAM disk now automatically saves upon shutdown, and is restored (with data intact) on startup. Boot and shutdown times get lengthened depending on the size you set.

Also, you may wish to adjust the AutoSave interval.

If you did not select "Save Disk Image on Shutdown", make sure continue reading especially!!

You need to follow these procedures every time you shutdown the computer to avoid data loss!

** Stopping the RAM disk manually (Before shutting down computer) **
1. Stop your Minecraft server if it is running
2. Open the Dataram RAMDisk configuration Utility (again)
3. Please enable "Load Disk Image on Startup" if not already under the Load/save tab
4. Click 'Save disk image now'
5. Click 'Stop RAMDisk'

When you wish to start the server next time, just start it like you did the first time. Do this only if you ticked 'Load Disk Image at Startup'.

** Alternative **
1. Stop your server
2. Copy all the files in the RAMDisk to a backup folder in a hard disk
3. Click 'Stop RAMDisk' on the Dataram RAMDisk configuration Utility

To start it again, start your RAMDisk like you did the first time and copy all the server files into the RAMDisk, then start your server.

### macOS
Type this to create your RAM disk on macOS:

diskutil erasevolume HFS+ "ramdisk" `hdiutil attach -nomount ram://1165430`

It's only one command line to write, quite fast and efficient.

If you've followed these instructions, your Ramdisk appears in /Volumes/ramdisk. After that, proceed as if you were on Linux, using Terminal and your favorite text editor.

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

