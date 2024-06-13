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

