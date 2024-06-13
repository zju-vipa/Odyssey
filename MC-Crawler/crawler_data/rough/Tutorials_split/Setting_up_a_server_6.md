### IP address notes
- Unless you set a static IP for the computer that is hosting the game, the internal IP address can change. This affects port forwarding rules, and can make them invalid. Each modem or router has a different way of setting a static IP address. You should refer to the manual for your device(s) or online documentation for further instruction.
- If you are having players connect to your external IP, your external IP can change if you do not have a static IP from your internet service provider. Use a tool such asWanIPto periodically check on the external IP address. You may also search "my ip address" on Google and it will show your IP address. Alternatively, you can look into a DDNS service that will allow you to have a name, rather than an IP address, that will remain the same. The name will point to your external IP address, regardless of whether or not it changes (the DNS is updated when changes occur, hence "dynamic").
- For troubleshooting purposes you can try runningMinecrafton the server machine and connect locally. You can connect through eitherlocalhost, your home network IP (192.168.x.x) or your public (Internet) IP.
- If for some reason you have trouble with connecting publicly over your IPv4, try connecting over IPv6. This should only be done for testing whether your server is online, external players should still use IPv4.

### 
- You must open a TCP/UDP port (default is 25565) on the firewall.
	- If the server in question is not reachable via a globally routable IP address, you will need to add appropriate address and/or port number translation rules to the gateway — usually your router has the global IP address.
- For help with address translation, opening the firewall and routing (these three make up what people call port mapping/forwarding),portforward.comis a good source. Select your router from that list, skip the ad that comes after selecting the device, and you will see instructions for setting up port forwarding. Alternatively, you can read the documentation supplied with your router, modem, or other ISP related hardware.
- Verify the port is open, and note your external IP by using a port checker tool, such asYou Get Signal. The default port you should test is 25565, unless you specified something else.Have the Minecraft server running when you test the port.
- You can obtain your external IP address fromYouGetSignal.

#### Local network dedicated servers



This only applies to Classic (v0.30) servers. 


A common problem for server administrators is the inability to connect to your own server via another machine on your local network. A typical scenario for this is that you have a Classic server running on a dedicated machine, and you have your own machine which you play on. They're both connected to the same router/switch, and have internal IP's with the octets '192.168.x.x'. Normally, connecting via the URL generated for your server will result in an error message claiming that the server is offline.

To correct this, you must add a function to the end of your URL, bookmarks, or whatever else you connect by. The function is: ?override=true
Example: http://www.minecraft.net/classic/play/4c3bebb1a01816acbe31c5ece1570da5?override=true

Previously, (before the 1.8 beta and website update) this was &override=true. This caused much confusion since the change was not announced by Mojang, and wasn't announced on the website applet pages either. Before the update, connecting to your own URL via the website resulted in red text under the applet window saying "If you can't connect, try this link instead." The link returned the same thing, with the &override=true affixed to the end.

Note: This situation does not effect Beta servers, and you should be able to connect via an internal or external IP.

#### The SRV record
Java Edition since 1.3 also supports using custom ports without requiring the player to type it. This is achieved by using a SRV record (for "service") in the DNS. The SRV record tells Minecraft the actual host and port to use; some DynDNS services and most static DNS services allow you to set it up.[2]

To manually verify the SRV record, use (assuming the player-facing domain is "YOUR.DOMAIN.com"):

> nslookup -q=srv _minecraft._tcp.YOUR.DOMAIN.com
Server:  UnKnown
Address:  [REDACTED]

Non-authoritative answer:
_minecraft._tcp.YOUR.DOMAIN.com  SRV service location:
          priority       = 5
          weight         = 5
          port           = 65312
          svr hostname   = ACTUAL.DOMAIN.com

## 
Q: I have a problem which is not answered in here! What should I do to?

A: Go to the Minecraft Forums and post your problem there. To help you, they need the following information:

- Operating system
- Version of Java
- One machine or multiple computers
- Exact description of the problem
- Steps you have taken to solve the problem
- Any errors you encountered
- Screenshots of the problem (if possible)
- Anything else that might help us to solve your problem—there almost never is too much information (passwords would be too much information!)

And please, if we were able to help you, post where the problem was exactly and what the fix was for that. Other people will appreciate that (and we will be able to get a grip on the common problems)!


Q: On a Windows computer, when I double click the batch file it opens a command prompt window, but quickly disappears and the server does not start.

A: Right-click your .bat program and hit edit; add a new line and type pause save and run the file. If it says invalid path, it is probably due to an incorrect path to java.exe/javaw.exe or your Minecraft server jar file. You may just need to change /jre7/ to /jre6/ . Or search your system for java.exe/javaw.exe and adjust the path accordingly. (It's probably under c:\program files or c:\program files (x86).) Also, you must have the offline version of Java installed—not just the Java plug-in for your browser.


Q: Whenever I try to get the server up, it says "Failed to bind to port!".

A: The most common reason this happens is because you put an IP address in the server-ip field in your server.properties file. If the IP you specify isn't the same as any of your network interfaces, (your wireless or wired IPv4 from ipconfig/ifconfig/ip a) Minecraft will throw the port binding failure message. By leaving it blank, you let it bind to all interfaces. You will then be able to connect using localhost and people on your wired/wireless network (in the same subnet) can connect using the computers/server's (private) IP address. 

Alternatively, the error can mean that you have tried to use a port that is already in use or that you do not have permission to use (ports < 1024 are privileged and require root/Administrator access to bind to). You can try a different port by changing it in your server.properties file in this line: server-port=25565.

Note: You should avoid using the following ports for your server as some ISPs may block these ports for security reasons and you shouldn't be running the Minecraft server as root (in the case of a Linux type OS and ports < 1024):

- 21 (Used by most FTP Servers)
- 22 (Used by Secure Shell daemon)
- 25 (Used by Mail Servers for SMTP)
- 53 (Used by DNS Servers)
- 80 (Used by most Web Servers)
- 110 (Used by most Mail Servers for POP3)
- 115 (Used by Simple File Transfer Protocol)
- 143 (Used by Mail Servers for IMAP)
- 443 (SSL port for Web Servers)
- 3306 (Used by most MySQL Servers)

Generally avoid any port below number 1024, since those ports are generally referred as well-known ports and are registered with the IANA for important services.


Q: I tried to run the server with Solaris/OpenSolaris and got the following error:

java.io.InterruptedIOException: Operation interrupted 
at java.net.SocketInputStream.socketRead0(Native Method) 
at java.net.SocketInputStream.read(SocketInputStream.java:129) 
at java.net.SocketInputStream.read(SocketInputStream.java:182) 
at java.io.FilterInputStream.read(FilterInputStream.java:66) 
at gq.a(SourceFile:131) 
at ji.g(SourceFile:197) 
at ji.c(SourceFile:17) 
at oq.run(SourceFile:84) 
2011-05-31 16:57:26 [INFO] /:44673 lost connection

A: For whatever reason, out of all of the operating systems, only Solaris throws that exception when a thread interrupts a connection. A workaround is to change the default behavior on the command line:

java -Xmx1G -Xms32M -XX:-UseVMInterruptibleIO -XX:+UseConcMarkSweepGC \
 -XX:+CMSIncrementalPacing -XX:ParallelGCThreads=$CPU_COUNT -XX:+AggressiveOpts\
 -jar minecraft.jar --nogui

This instructs Java to use an interruptible IO stack instead of the default IO that is sensitive to interrupted threads.


Q: When I try to connect to my server this is what it says:

               Connection lost 
 
The server responded with an invalid server key

A: This error is usually caused when the server sends an unrecognized function to the client, which may be caused by using unrecognized server software, unbalanced client / server versions or modifications to the client.


Q: I cannot break/place any blocks!?

A: This is most usually caused by interacting with blocks in a protected area. If you are trying to interact near spawn, most likely it has been protected, by the Minecraft server software; either build away from it or get operator status.


Q: My server runs fine, but I cannot connect to it!

A: This could be caused by a series of issues. Please post a thread using the template provided above.


Q: How do you give a .jar server more ram?

A: Change the numbers in the server launch command "-Xmx1G -Xms1G". The -Xms part specifies how much memory the server starts with, and the -Xmx part is the maximum amount of memory the server can use.
-Xmx1G -Xms2G = 1GB
-Xmx2G -Xms1G = 2GB
And so on.


Q: Why is the server CPU constantly at full load?

A: Some users are experiences full CPU load on the server. This may be caused by the GUI (graphic user interface) window. Run the server with the --nogui option to disable this window.


Q: Help! How do you find out your server's IP address?

A: Read #Connecting to the Minecraft server


Q: I port forwarded and allowed java.exe in my firewall and it's still not working!

A: Your modem might be acting as a router as well. If you switch ISP's or upgrade your connection to the Internet, you may get issued a modem/router combination (which might explain why it worked in the past).
You can verify this by looking for the WAN IP of your router. If it's a private IP, you'll need to log into the modem/router your ISP issued to you, and configure port forwarding to the WAN IP of your router.


Q: I turned off my firewall on my router/modem how does it still not work???!!! However, port forwarding sites report they can "see" me?? What's going on???!!

A: Turning off your firewall on your router/modem means you essentially disabled port forwarding. Port forwarding is actually a subset of firewall rules. If no rule exists on that port (for example 25565), the firewall will ignore/drop the connection attempt (hence, you get a connection timed out). If there is a rule, it should pass on the connection to whatever computer is configured to receive the initial connection attempt.

When you disable the router/modem firewall and test your public (non RFC 1918) IP address on a port forwarding-checking website, the website will hit your router/modem, and your router/modem will respond, yes you can see me. This is another reason why disabling your firewall is bad; you incorrectly believe that people outside your network can connect to your Minecraft Server on your computer, when really, they're trying to connect to the router/modem itself. 

To solve this, the next step is to confirm if your port forwarding (rules) are correct. By Google-ing "minecraft server checker" you'll be able to check if you configured your network correctly such that users outside your network running the Minecraft client can indeed connect to your computer through your router/modem.

Note: You may need to be careful about the Minecraft Query: it may use layer 4, the transport layer, UDP, to query your server. Many Internet and YouTube guides will only tell you to port forward TCP (this guide outlines that you do both).


Q: What is connection timed out and connection refused?

A: Simply put, connection timed out is when a firewall ignores a connection attempt (ignores the intial connection packet with the SYN flag in the 3-way handshake). Connection refused is when there's no process listening on the port; therefore, the operating system lets the client (in the standard client-server model) know their connection attempt did not work.

The default configuration on all Windows computers (the home version) and (just about) all (SOHO) routers is to drop or time out the connections. This is called "stealth mode" and you can read more about it on superuser. Here's a brief summary: "The idea is that refusing a connection instead of timing it out will tell an attacker that there actually is a computer on that IP-Address. With the connection attempt timing out, the hope is that the attacker will ignore the computer."

You can read more about connection refused on serverfault.

So if your error message is a connection timed out, it's usually a firewall problem; you either need to allow Java in the Windows firewall or port forward. If the error message is a connection refused, perhaps your Minecraft server has not started properly or you turned off the firewall on your router instead of port forwarding.

As always, you can always ask the Minecraft Forum if you are uneasy or unsure about something, particularly if opening the command prompt/terminal and running commands makes you nervous. 

Connection filtered and connection closed is another way of saying timed out and refused, respectively.

