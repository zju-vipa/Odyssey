### Setting up a VPN



Note 
VPN's can cause issues connecting to Mojang's servers, Minecraft servers, or to the internet.



  


The contents of this section are not supported by Mojang Studios or the Minecraft Wiki.


An alternate way to set up a server between you and your friends is to set up a VPN (virtual private network). This method may be deemed unrecommended, and an inconvenience for many users due to the fact that all users who wish to connect to the server must download external software in order to join or create server. An alternative to this method is to port forward. A free software utility that can be used to set up a VPN is Hamachi by LogMeIn. OpenVPN is another (free, open source) alternative that supports most OSes, but is a bit more difficult to configure. Free Radmin VPN is another software with no need to register on the website and no limits per the number of users. The free version of Hamachi allows up to 5 connections (i.e. players).

#### Setting up Hamachi
1. Install Hamachi on each computer that wishes to participate in the server, including the host.Windows / MacLinux(32-bit and 64-bit.deband.rpmpackages are available, you can install it on Gentoo by emerging "net-misc/logmein-hamachi")
2. The host server signs up for admin via theLogmein website.
3. On the host machine, a new Hamachi network is created.
4. The host installs and configures theMinecraftserver software:The server IP field in server.properties is left blank (as default).
5. The host passes the newly created Hamachi network credentials to each of the players.
6. The players connect to the host's Hamachi network.
7. Now that all the machines are connected within the same Hamachi network, the host gives their machine's Hamachi IPv4 address to the players.
8. Each player connects using this IP as per the usualMinecraftmultiplayer screen.
9. Note that Hamachi has been squatting on an IANA-allocated IP block (25.0.0.0/8). As such, Hamachi fundamentally conflicts with the internet itself.

#### Setting up Radmin VPN
It is very similar to Hamachi installation.

1. Download free and installRadmin VPN
2. Create a network: after Radmin VPN installation on the local computer press "Create network" button. Set a Network name and a Password —> Press "Create" button.
3. Now the new network will appear in the main window —> invite friends, send them the info to connect -> you are welcome to runMinecraft.
4. Connection: after program launch press “Join network" —> in the dialog box press enter Network name and Password received from the network administrator —> "Join" —> the new network and its nodes will be shown in the main window. —> Connect to the host inMinecraft.

- If the connection on Radmin VPN has been established, but you don`t see other players in the game, then it is required to adjust firewall for work of the game or just turn the firewall off.

### Configuring the Minecraft server
1. Configure the server by editing theserver.propertiesfile, the format for which isexplained here. Be certain to edit the file with a text editor that does not add formatting (e.g., for italics), such asWindows Notepad. Additional configuration may not be necessary as many servers run fine from the default values.
2. To become or add an operator (op), type/op <targets>into the server console or gui. This adds the specified user's username andUUIDto theops.jsonfile. Operator status will not be changed if you change your username due to the use of UUID.
	- Administrators and operators may executecommands. In other words, operator (op) privileges allow you to control certain aspects of the game (e.g., teleporting players).
	- ops.json contents:[
  {
    "uuid": "",
    "name": "",
    "level": 4,
    "bypassesPlayerLimit": false
  }
]
3. If yourserver.propertiesis configured to enable whitelist, you can add a user to thewhitelist.jsonby typing/whitelist add <player>into the server console or gui. Due to the transition to the UUID system, it is not recommended to directly editwhitelist.json.

## Connecting to the Minecraft server

  

This section needs to be updated. 
Please update this section to reflect recent updates or newly available information.Reason:
Internal IP is less reliable than looking for the server by hostname, which is available through either router DNS or mDNS (Bonjour, available in all versions of macOS and Windows 10). Static IP works, but it requires making sure the router never gives the address to anyone else. (In an ideal world you'd just use the existing LAN server discovery system, but Mojang has decided it's irrelevant for dedicated.)
Port forwarding can potentially be replaced with UPnP. More flexible, but a bit brittle.


- If you are playing on the same machine on which the server is running, select the "Multiplayer" option in the game client, click direct connect, and then type inlocalhostinstead of an IP address.
	- Both hosting and playing on the same machine is not a recommended practice unless you have a powerful computer (e.g. more than 6 gigabytes of ram (4 for the server, 2 for the client, and some for the rest of the system).
- Users within your local network (i.e., that are accessing the same router) can connect using your internal IP address; port forwarding is not required for such local connections. The internal IP address of a specific network adapter can be found by typing "ipconfig" into the command prompt and looking for the IPv4 address, or by usingthis website. If the port is set to a number other than 25565 inserver.properties, that port must be included. This address (both IP and port) will look something like192.168.0.168:25565.
- Users connecting from the Internet (i.e., outside of your local network) must connect using your external IP address. You must port forward for someone outside your network to connect to the server.

