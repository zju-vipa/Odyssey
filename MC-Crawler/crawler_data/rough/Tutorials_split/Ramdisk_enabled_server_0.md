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

