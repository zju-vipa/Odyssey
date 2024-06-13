### Improving PvP without Plugins
Players can use /gamerule keepInventory true so players cannot steal each other's items. Also, using /spawnpoint <x> <y> <z> and /teleport <x> <y> <z> to help move players around while in PvP competitions.

### Starter Kits
Players can easily give people a starter kit with a button without plugins: /give @p[distance=2]. 
To prevent people pressing the button a second time and again getting their kit, players can make two command blocks activated in order: /give @p[distance=2,m=2] minecraft:stone_pickaxe
/gamemode @p[distance=2] survival

### Colorful Messages
It is possible to create a colored, clickable message players can send to anybody. The command is /tellraw. Not to be confused with /tell. The basic format is /tellraw @a {text:"", color:<color>}
An example would be /tellraw @a {text:"Hello, Steve", color:blue, italic:true, obfuscated:true}. Simply place a comma and space with each addition. If you want other players to be able to click it, use clickEvent. Here's the example: /tellraw @p {text:"Run Coward! I hunger!", clickEvent:{action:run_command, value:"/give @p minecraft:cooked_porkchop 64"}}. This means when the player clicks the text, it will give them a stack of cooked pork. If you just want to tell them something without running a command, replace clickEvent with hoverEvent and run_command with show_text. Then just type the value text as a regular sentence, no slashes. If you want an easier job of it, here we have some tools:

Tellraw Generator 1
Tellraw Generator 2
Skylinerw's JSON Text Component
### Alarm System
When a player walks over a pressure plate, it can trigger a command block with /say <message> or /title <player> title <message>. @p can be used within the message to display the player closest to the command block upon triggering.

### Remove Players
Using coordinate and maximum parameters, players can teleport everyone within a specific area to another specific area.

### Reward Room
If a certain player has been very nice, regular, or helpful to the server but not quite meeting the requirements to be promoted to an admin, players could have a room full of buttons connected to command blocks with helpful effects, like giving the helpful player a stack of diamonds or a bedrock block, then have it connected to another command block, sending them to the spawn point. (It is very important this room is reinforced with bedrock, hidden, and you can only get in by teleporting to its co-ordinates to avoid abuse).

### Weather Machine
Command: /weather <weather>

Assuming only admins can get to it, a weather machine can be quite useful, players can turn rain on and off at will. One of the more helpful uses of this technique would be to use a combination of villagers (they run inside when it rains) and some form of redstone machinery to create and automatic rain disabler, this would allow you to shut off the rain almost immediately without needing to use the command, or to have an admin present. It can also be used to create, and/or end, a scenario where it is more advantageous to have rain as opposed to sunlight, and vice versa; such as during a forest fire, or when a thunderstorm is spawning monsters.

### Obstacle Course Prizes
with /teleport @p <x> <y> <z> and /give @p <item>, players could make an obstacle course or maze that when finished will give a player a prize, and will teleport them back to spawn or some other area.

### Time Machine
By making two similar places on one map, players can have a button activate a command block to teleport them from one to another, while also changing the time of day. This can be used to look like time travel.

### Proximity Mine
By using a condition such as /execute if entity @p[distance=..5,name=!<placing player>] run <command> hooked to a short clock and one or more TNT blocks via a comparator, the command block can act as an undetectable proximity mine against all players except the placing player.

### Secure Doors
By using a condition such as /execute if entity @p[distance=..5,name=<owner>] run <command>, the command block can detect a door's owner within a certain radius and open a door for them, and only for them.

### Custom Commands
By using a trigger objective, players can create commands that players can use on a server.

** Warp command example **
First, add the objective: /scoreboard objectives add warp trigger. Place a command block connected to a Redstone clock with the command /scoreboard players enable @a warp. Then place another command block connected to the clock with the command /teleport @a[scores={warp=1..}] <x> <y> <z> [<y-rot> <x-rot>]. Place a comparator facing away from that command block, activating a command block with the command /scoreboard players set @a[scores={warp=1..}] warp 0. When a player uses /trigger warp set 1, they will be teleported to (x,y,z) coordinates in the command block.




## Application in custom maps
This section details the applications of the command block in custom maps.

If one wishes to create a singleplayer adventure map, use /publish to allow all other commands to be used.

One map that takes advantage of a lot of the features of the command block is the Hypixel's Gladiator Arena in which the fighting system is almost only based on this.




### Silent Command Block
Sometimes it's important in a map to keep the command blocks silent, may it be to keep the magic of the suddenly appearing items in the inventory, or because the channel telling that the player was teleported, it can break the mood of a map. To keep them silent (except when you ask them to speak), just use the following:
/gamerule commandBlockOutput false

### 
Using pressure plates or tripwire, make areas (like a castle for instance) a different difficulty (in this instance peaceful). the doors could have tripwire hook to a command block that changes ones difficulty to peaceful, creating a sort of "Safe Haven". one could also do it the other way around, creating a more dangerous zone, such as arenas having the difficulty of hard, rather than normal or easy. Note that in multiplayer this will change the difficulty everywhere in the world, and thus may not be desirable.

