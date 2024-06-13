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

