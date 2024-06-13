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


