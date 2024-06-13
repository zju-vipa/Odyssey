# Tutorials/Update Java
As of Minecraft Java Edition 1.18, the Minecraft Launcher is bundled with the Microsoft Build of OpenJDK (Java version 17.0.8). If need be, it is possible to change the used Java version in the profile options menu.

## Contents
- 1 What is Java?
- 2 Why update?
- 3 Where to download
	- 3.1 Other VMs
	- 3.2 Notes
- 4 How to update
- 5 Notes
- 6 Known issues
- 7 References
- 8 External links

## 
Java is a programming language and computing platform. Unlike many other languages, Java does not run directly on the hardware, but in a virtual machine, called the JVM (Java Virtual Machine).[1] Minecraft (Java Edition) is written in Java, and uses it for game logic, rendering, and networking.

As of September 19, 2023, the latest stable Java versions are 1.8.0_382 (OpenJDK) (Long-Term Support or LTS), 11.0.20 (LTS), 17.0.8 (LTS) and 21 (LTS).

If you use a custom JVM, you should notice that the official launcher only allow the custom JVM with the same primary Java version as the minimum required Java version to launch the game.[2]

## 
The latest versions of Java contain important enhancements to help improve performance, stability and security of the Java applications that run on your machine. Installing the latest Java update ensures that Minecraft continues to run safely and efficiently.

- Different Minecraft versions have different requirements of minimum Java version.
	- From the first version ofMinecraft,Java Edition pre-Classic rd-132211toJava Edition 1.5.2,Minecraftrequires Java 5 (1.5.0) or newer.
	- FromJava Edition 1.6.1(13w16a) toJava Edition 1.11.2(1.12:17w06a),Minecraftrequires Java 6 (1.6.0) or newer.
	- FromJava Edition 1.12(17w13a) toJava Edition 1.16.5(1.17:21w18a),Minecraftrequires Java 8 (1.8.0) or newer.[3]
	- FromJava Edition 1.17(21w19a) toJava Edition 1.17.1(1.18:1.18 Pre-release 1),Minecraftrequires Java 16 or newer.[4]
	- FromJava Edition 1.18(1.18 Pre-release 2) toJava Edition 1.20.4(1.20.5:24w14potato),Minecraftrequires Java 17 or newer.[5]
	- SinceJava Edition 1.20.5(24w14a),Minecraftrequires Java 21 or newer.[6]
- Minecraftmay sometimes crash without being run by a relatively modern version of Java.
- Java updates fix lots of problems and bugs and typically cause increases in performance.
	- For example, the newer garbage collectors can help with lag spikes during high memory usage.[7]
- Running a server requires your computer to have Java installed instead of the pre-installed Java. SeeTutorials/Setting up a serverfor more information.

## Where to download
See also: Wikipedia:OpenJDK § OpenJDK builds

You can get Java either from Oracle or from someone who builds OpenJDK. For the purpose of Minecraft they are essentially the same, but Oracle's "OTN" version (Oracle JDK uses "Oracle No-Fee Terms and Conditions" as of Java 17 LTS) requires a PAID license for commercial and production purposes. If you make money from streaming Minecraft or running a Minecraft server (even non-profit), you MUST use OpenJDK unless you want to figure out how to pay.

- Microsoft Build of OpenJDK(the officially tested OpenJDK build for Minecraft)
- Adoptium OpenJDK (Continuation of AdoptOpenJDK)(stable builds only, check github.com/adoptium for development builds - Microsoft also sponsors Adoptium so you can assume this is also well tested)
- Zulu OpenJDK(stable and development builds)
- Oracle OpenJDK(stable and development builds) - zip packages only (no installer)
- Oracle JRE(NOTrecommended unless you want to pay) (stable "OTN" builds)

You will see that Java is divided into LTS (long-term support) like 11 and STS (short-term support) version numbers like 16. An LTS version will be given updates for longer, so people tend to use them as a stable standard of "modern, but not too new" Java.

### Other VMs
Some other Java compatible VMs include:

- IBM's Semeru, optimized for low memory and fast startup
- Oracle's GraalVM, also optimized for low memory and fast startup

### Notes
- The licensing change in January 2019 (8u211) is partially why Minecraft's 1.16.5 official launcher is stuck at 8u51, instead of a newer Java 8 update.
- Java 9 to Java 16 (except Java 11) are no longer supported by Oracle: they no longer receive public security updates,[8]and are to be regarded as insecure. Oracle has removed them from its download page but the builds are still availablein the Java Archive. Oracle does not recommend using builds from the Java Archive.[9]
	- Java 13, 15 is supported bysource code, provides support inAzul Zulu.

## How to update
When you install Java, go to your launcher, edit or create an installation, and in the Java Executable box, type C:\Program Files\Java\jvm-[version]\bin\javaw.exe (Windows)
or: /usr/lib/jvm/(java version)/bin/java (Linux) or: /usr/bin/java (macOS). The exact value depends on where your java is installed.

You must remove -XX:+CMSIncrementalMode from your JVM Arguments. This option is meaningless for Java 9 and newer, and will cause a launch failure if you keep it there.

## Notes
- Because the official launcher has Java integrated, you won't need to download and install the Java unless you are using third-party launchers instead.
- If your computer runs a 64-bit operating system, it's recommended to install the 64-bit Java for better performance.
- Administrator privileges are required when installing on some systems.

## Known issues
- In Java 11 or newer, a very rare crash may occur in world generation code (MC-149777). A fabric mod called Voyager exists to fix this issue.[7]If you are using Fabric API 0.26.2 or above, this mod is not needed as the fix is included. This bug was fixed in 1.17 snapshot21w20aand hence does not exist from 1.17+.[10]
- Do not upgrade if you are using Intel HD2xxx/3xxx graphics on Windows 10, asthe driver is bugged. Java 8 uses a slower rendering method that makes it work, and that is mainly why Mojang stuck to this old version.[7]

