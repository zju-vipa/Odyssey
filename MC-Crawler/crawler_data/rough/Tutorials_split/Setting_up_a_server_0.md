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

