# Server
Minecraft servers allow players to play online or via a local area network with other people. Internally, the game runs a server for single-player games, this was done in order to make the single-player game experience consistent with the multiplayer experience and make it so that changes made to the game such as bug fixes apply to both single-player games and multiplayer games.  Official server software is only available on Java Edition in the release state. The Bedrock Edition server software is currently in Alpha.

## Contents
- 1 Types of servers
- 2 Hosting a server
- 3 Managing and maintaining a server
	- 3.1 Kick messages
- 4 History
- 5 See also
- 6 External links

## Types of servers
See also: Tutorials/Playing on servers

Multiple archetypes of Minecraft servers exist, distinguished by the unique gameplay features, rules, and societal structures that they implement. No two servers are the same, and frequently the line between archetypes is blurred or indistinguishable. Many special types of servers rely on the use of map editors or the Creative game mode to build custom maps and the CraftBukkit server software to provide additional features. Some of these servers are more PVP orientated, some involve aspects of Survival, Creative and Adventure mode, some have a built-in economy, and some of them contain built-in minigames.

Some server types are:

- Survival: These servers are servers that use only survival mode. They are similar to Anarchy Servers, except there are usually rules, and usually prohibit Griefing and Exploiting.
- Creative: These are servers that only use Creative mode. Usually, servers give the players Creative, but limit the items they can access and/or limit the plot size. This is usually done to prevent griefing to other players' plots and to prevent excessive lagspikes.
- Minigame: These are servers that host multiple minigames (such as spleef, capture the flag, missile-, bed- and sky wars and more).
- Anarchy: These servers have no rules at all. Many players engage in cheating, exploiting, and use of vulgar language.
- Faction: Similar in concept to Survival servers, but claims are used to mark land as "yours". Untrusted players cannot build on "your" land.
- Personal/Private: These are servers that players can make on their own. Usually, the link is private, shared only with the user's close friends.
- Hardcore: The same as survival mode, except players only have one life. This typically ends with a "last man standing" scenario, This type of server is mainly used in SkyWars and Survival Games.
- Roleplay:These servers have their players acting as their own persona, sometimes being dictated by the Roleplay that is happening.
- City build:Here usually plots can be claimed to build cities on them.
- Sky block:On sky block one starts with just a few blocks above the void and then farms their way up.
- War Gear, War Ship and Air Ship:Modes where one spends time building vanilla fighting machines on build servers and can try them out in the arena.
- Modded servers:Servers can be modded to provide a playing experience very different to to the vanilla game.

## Hosting a server
There are many tools provided for players to be able to manage and host a server. Note that servers have requirements in order to run efficiently and smoothly.

- The default multiplayer softwareis free of charge and is available by Mojang Studios for Windows, macOS, and Unix-like systems (Linux, BSD...). See theMinecraft multiplayer server tutorialand Mojang Studios'Minecraft multiplayer server downloadpage for help.
- Opening a world to LANprovides a server that is accessible only to other people on the local network unless port forwarding is set up on the router. See thesetting up a LAN world tutorialfor more information.
- Custom server softwaresuch as CraftBukkit, Spigot, and Sponge provide players a way to add plugins to a server. These are generally used for larger servers that run plugins to ensuregrieferprotection, non-vanilla commands (e.g./sethome), custom minigames, etc.
- Rented serversare servers hosted externally by another company. These hosted servers are (usually) not provided free of charge - the player must rent them on a regular basis.
- Realmsare Mojang Studios' official hosting service that allows a limited number of players onto a server. Note that the Java Realms are still separate from Realms for other versions ofMinecraft.
- Dedicated Serversare servers that provide a wider range of power sources. These servers are much more flexible and allow for almost complete control.

See Tutorials#Servers for tutorials on how to use these programs.

## Managing and maintaining a server
See also: Tutorials/Server maintenance

Servers are generally managed by administrators and operators. The administrator generally takes responsibility for the server. It may be that the server is running from their machine, or that they simply have jurisdiction over a server. Operators generally assist the administrators to moderate a server and to prevent unruly players and griefers. Both operators and administrators have access to various commands in order to ensure the smooth running of the server. On a default server, players are assigned as operator or administrator by using the /op <playername> command, or by editing the ops.json in the server directory, then restarting the server.

Local servers do not strictly require access to minecraft.net, and so can be played on an isolated local network with no internet connection. They use minecraft.net as a repository of player skins and also a database containing a list of accounts, preventing hackers and griefers from using false names while on such a server. This and other settings are modified by editing the server.properties text file.

The server saves the level in the "world" folder every 30 seconds if chunks have been modified, by default.

### Kick messages
Kick messages are messages that are displayed when an operator kicks the player, or the player has issues connecting to the server.

- End Of Stream(Client message) – The server has stopped sending data to the client
- Internal Server Error:java.net.Minecraft– The server is sending unknown information to the client, usually from aserver mod, this happens with a client with an outdated mod tries to join the server with the updated mod.
- Timed Out- The client has lost connection to the server, most likely due to disconnecting from the Internet or having Minecraft features blocked by a firewall.
- Internal exception: java.io.IOException: Received string length longer than the maximum allowed ([Number]>256)– A chat message that the client sent to the server exceeded the maximum character limit.
- Internal Server Error– The server generated an exception when handling the client's request.
- Disconnected- The player disconnected by using the Disconnect button in the Main Menu
- Illegal characters in chat– The client was denied sending certain characters, such as the § symbol
- Kicked for spamming(disconnect.spam)- The client is sending chat messages too quickly
- Read timed out– The server can't find the player's connection
- Bad login– The client is running in offline mode and can't connect to an authenticated server
- You logged in from another location- Another client has logged in to the server the player is playing on with the player's username.
- Outdated client(Please use {version}) – The server is running a more recent version ofMinecraftthan the client is
- Outdated server(I'm still on {version}) – The client is running a more recent version ofMinecraftthan the server is
- You are banned from this server(Maybe followed byReason: {reason}and/orYour ban will be removed on {date}) – Self-explanatory, the client is banned and remains banned until pardoned by an admin
- You have been IP banned.- The client's IP has been banned.
- Kicked by an operator.- The client has been disconnected using the/kickcommand. This message appears when no custom message is entered.[note 1]Another message is "Kicked/Banned By " Reason: (what has been typed in after /kick or /ban)
- Flying is not enabled on this server- The client tried to fly for longer than 5 seconds in Survival or Adventure mode, usually enabled by plugins.
- Attempting to attack an invalid entity- ??, Happens when a client tries to hit either themselves, or an entity that can't normally be attacked (e.g. Arrow, Egg, Ender Pearl, Trident). This is only possible through mods/plugins.
- Illegal stance- ??, Happens when a client is extremely high or low
- Illegal position- The client is beyond X/Z: ±30,000,000 (±32,000,000 in 1.6.4 and lower.)
- You have died. Game over, man, it's game over!- The client is dead but tried to join inHardcoremode.
- You have been idle for too long!- The client was idle for a longer time than allowed.
- Out of memory!- This happens when 100% of memory is consumed or if one traveled past X/Z: ±34,359,738,368 in Beta 1.7.3 or lower (seeFar Lands). (It shows up on the F3Debug screen)
- Server closed.- The server has been shut down either by closing out of the "Minecraft server" window/pressing ALT+F4, stopping the server through the dashboard/console (for rented servers), or using the/stopcommand.

1. ↑Please note that the /kick command can disconnect clients with custom message.

