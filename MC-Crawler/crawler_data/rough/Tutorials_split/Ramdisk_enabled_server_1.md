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

