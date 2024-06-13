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

