# Tutorials/Command blocks and functions
Command blocks and functions can be used, among many other things, to change the difficulty, change the state of the weather, or give a player predesignated items. They are particularly useful for the /weather and /time set commands, as they are only available in cheat mode otherwise. The /time set command is especially useful, as it allows players to change the current time to a preset time at the press of a button.

Command blocks and functions can also be used to make text appear in the person's chat menu. The code to do this is /tell @p <message>, or /tell <username> <message>. If the @p parameter is present only the nearest person will see the message. If a username was specified, the username will be sent the message. The player can also type: /tell <your username> @p, e.g. /tell <username> and whenever someone walks over it, it will say: "[(hover note{Deafau;ts to @})] whispers to the player: <username>".

Changing the difficulty is accomplished by /difficulty <name of the difficulty> (e.g. /difficulty peaceful).

Another way to use command blocks and functions is to use /teleport @p <coordinates> to teleport between different bases in a world.

## Contents
- 1 General applications
- 2 Basic usage of commands
	- 2.1 Cookie announcer
	- 2.2 Time warper
	- 2.3 Wireless redstone
	- 2.4 Wireless buttons
	- 2.5 Starter kits
	- 2.6 Teleporting
	- 2.7 Security System for Mobs or Players
	- 2.8 Moving Sidewalk
	- 2.9 Replacement for pressure plates
	- 2.10 Commanding Passwords
	- 2.11 The Destroyer
	- 2.12 Landscaper
	- 2.13 Booby traps
	- 2.14 Teleporters
	- 2.15 Command-Piston-Repeater Fun
		- 2.15.1 Fast Pusher
		- 2.15.2 Slow Pusher
	- 2.16 Working Minecart with Dispenser
- 3 Singleplayer non-Creative maps
- 4 Multiplayer applications
	- 4.1 Command-based flying
		- 4.1.1 /tp command
		- 4.1.2 /clone command
		- 4.1.3 /summon command
	- 4.2 /data (merge/modify) [entity] command
	- 4.3 Teleportation/Transport
	- 4.4 Stop-Motion Animation
	- 4.5 Lottery
	- 4.6 Jails
	- 4.7 Creative Only
	- 4.8 Fun anti-creative mode trap
	- 4.9 Announcements
	- 4.10 Security Scan
	- 4.11 Race Referee
	- 4.12 Creative Area/World Guard
	- 4.13 Improving PvP without Plugins
	- 4.14 Starter Kits
	- 4.15 Colorful Messages
	- 4.16 Alarm System
	- 4.17 Remove Players
	- 4.18 Reward Room
	- 4.19 Weather Machine
	- 4.20 Obstacle Course Prizes
	- 4.21 Time Machine
	- 4.22 Proximity Mine
	- 4.23 Secure Doors
	- 4.24 Custom Commands
- 5 Application in custom maps
	- 5.1 Silent Command Block
	- 5.2 Safe Haven/Arena Fight Zone
	- 5.3 Detecting Cheaters
	- 5.4 It's bigger on the inside
	- 5.5 Save game
	- 5.6 Lava parkours
	- 5.7 Still want a bed?
	- 5.8 Time and weather following the scenario
	- 5.9 Detecting Players who switched to Peaceful
	- 5.10 Talking Adventure Map
	- 5.11 Making a Store
- 6 Spawners
	- 6.1 Part 1: The Basics
	- 6.2 Part 2: Custom monsters
	- 6.3 Part 3: SpawnPotentials
	- 6.4 Part 4: Rideable Monsters
- 7 More commands in fewer command blocks and recursion
- 8 Using a map item as a scroll
- 9 Further reading
- 10 Video
- 11 See also

## General applications
Command blocks and functions can be used, among many other things, to change the difficulty, change the state of the weather, or give a player predesignated items. They are particularly useful for the /weather and /time set commands, as they are only available in cheat mode otherwise. The /time set command is especially useful, as it allows players to change the current time to a preset time at the press of a button.

Command blocks and functions can also be used to make text appear in the person's chat menu. The code to do this is /tell @p <message>, or /tell <username> <message>. If the @p parameter is present only the nearest person will see the message. If a username was specified, the username will be sent the message. The player can also type: /tell <your username> @p, e.g. /tell <username> and whenever someone walks over it, it will say: "[(hover note{Deafau;ts to @})] whispers to the player: <username>".

Changing the difficulty is accomplished by /difficulty <name of the difficulty> (e.g. /difficulty peaceful).

Another way to use command blocks and functions is to use /teleport @p <coordinates> to teleport between different bases in a world.

## Basic usage of commands
There are many things players can do with command blocks. Here are examples of some of them:

### Cookie announcer
When run in order, such as in a chain of command blocks or functions, these commands will give a random player 5 cookies.

/tag @r add cookie

/give @a[tag=cookie] minecraft:cookie 5

/say @a[tag=cookie] has been given 5 cookies!

/tag @a[tag=cookie] remove cookie

### Time warper
By putting this command inside a repeating command block, the player can make time speed up. Adjust the number to change how fast it goes.

/time add 5

### Wireless redstone
Redstone can wirelessly be 'transmitted' by placing a redstone block at a certain location. The downside to this method is that the chunks being transmitted to must be loaded. This method is often used with Adventure maps to trigger more command blocks.

/setblock <x> <y> <z> redstone_block

/setblock <x> <y> <z> stone

To not require loading chunks, the scoreboard is needed. The second command will only complete successfully if the first has been run. Either a comparator or chained conditional command blocks can detect the success. The second command block should be set to repeat.

/scoreboard objectives add signal dummy

/scoreboard objectives remove signal

### Wireless buttons
See also: Button § Data values and Lever § Data values

The previous is often used in conjunction with buttons. Sometimes however, there might not be enough room to hide a command block. In that case, the player can use a repeating command block to test if a button on (x, y, z) is pressed.

/execute if block <x1> <y1> <z1> #minecraft:buttons[powered=true] run clone <x1> <y1> <z1> <x2> <y2> <z2> <x3> <y3> <z3>

### Starter kits
Using command blocks users can give starter kits to new players.

/clear @p[tag=!started,distance=..5]

/tag @p add started

/give @p iron_sword

/give @p bread 5

/teleport @p <x> <y> <z>

The problem with this setup is that players can only get the starter kit once, even if they die. To fix this, use these commands. The first command should only be run once, probably by the player rather than a command block.

/scoreboard objectives add died deathCount

/tag remove @p[scores={died=0..}] started

/scoreboard players set @p died 0

### Teleporting
The player can teleport by using the /teleport teleport or tp <y> commands, where y is the vertical difference between the upper and lower elevator entrances.
The elevator can also be made to tp a player to any coordinate just by leaving out the ~ before the numbers. When ~ is left in the command, the normal (x,y,z) is set to (0,0,0) where the command was made, such as standing on a pressure plate or wherever the player is standing when the command block received power. If a pressure plate was at the coordinates of (-36,96,-12) that ran to a command block with a command of /teleport @p ~3 ~4 ~5 it would tp the player to the coordinates of (-33,100,-7). The same outcome can be achieved by having the command of /teleport @p -33 100 -7 one block must be subtracted from the x and z axis to get to the right coordinates. Using @p, @s, @a @e.

### Security System for Mobs or Players
Command blocks can also be used to make a security system. Just put a pressure plate which triggers a command block in front of an iron door, which will be the entrance to the house. Insert the command: kill @e[type=(mob)] and hook it up with chain command blocks to kill different mobs. this is to not kill you or other players. do this second command in a command block to teleport all things in the vicinity: tp @e[r=2] ~(any distance) ~(any distance) ~(any distance)

### Moving Sidewalk
A similar concept to the elevator but made to move a player along the x or z coordinates.
This can be created by:

- Use the/fillcommand.

/fill <x1> <y1> <z1> <x2> <y2> <z2> command_block{Command:"/execute as @p at @s run teleport @s ~-1 ~ ~"}

- Edit the coordinates inside the brackets to change the direction the player will move
- Place pressure plates on top of all the command blocks.
- Step on it

Users might want to turn command block output off since the chat will keep spamming command block output via using /gamerule commandblockoutput false

### Replacement for pressure plates
Pressure plates only blend in with only gold, iron, stone, and wood planks, but cannot be concealed in any other floor; command blocks can be used instead. Pressure plates can be replaced with a command block by using the if argument in the command /execute with a range and a clock circuit. The command /execute if @p[distance=..2] will test to see if any players are within a range of 2 (the command block itself plus 2 more blocks in every direction). Range 2 is the range a player want for a command block under a floor. Keep in mind that it will produce a globe shaped trigger area (rather than a cube), so a range of 2 makes an approximately 5×5×5 area and a range of 1 makes a 3×3×3 area (more like a + pattern with an extra block above and below the center). The player can get around this by using the dx, dy and dz arguments. 

Alternately the player can specify the x, y and z coordinates in the command (e.g. /execute if @p[x=50,y=64,z=46,distance=..1] but be warned that the range cannot be shrinked to the 1-block point. As with the non-xyz version range means center block plus range number of blocks around it, which makes sense from a command block (where “just the center block” would mean you have to be standing in the command block) but doesn’t make sense here. At any rate a range 1 sphere (+ pattern with an extra block on top and bottom) can be buried underground with just the top sticking out, provided the player know no one will be walking through the bottom 2 layers of the globe. Trying this with the non-xyz version of the command would require the command block itself to be embedded in the surface of the floor where it can be seen.

Important note: When writing the code in brackets [], do not put spaces between commas , :
Do not add / during coding unless instructed to.

Bad: [x=0, y=0, z=0, distance=..1]

Bad: [x=0 ,y=0 ,z=0 ,distance=..1]

Bad: [x=0 , y=0 , z=0 , distance=..1]

Good: [x=0,y=0,z=0,distance=..1]

### Commanding Passwords
Players can now create passwords with command blocks, using the if block argument on /execute. Place a command block. This will be the one you put input in. Place another command block, and type in the following command:
/execute if block <x, y, z coordinates of first command block> command_block{Command:"<input>"}
Example:
/execute if block ~2 ~ ~ command_block{Command:"That's Numberwang!"}
Place a comparator connected to the second command block, and place a button on or next to it to power the block. Now type "That's Numberwang!" (without quotes). If the second command block properly finds the first, the comparator will activate whatever it's wired to. If you want the first command block to reset so the password isn't used by someone else, also place a command block with /setblock that activates after /execute.

If you don't want to let people edit your command block, you can test for a sign instead, but this means having to test for the password separately on each of the sign's 4 lines. To add a touch, you can fill the sign with air, but remember to give it back using /give @p sign.

### The Destroyer
This allows the player to destroy a cube of materials around them as they walk, using /execute. The command is /execute as @p at @s run fill ~1 ~2 ~1 ~-1 ~0 ~-1 air‌[Java Edition  only] or /execute @p ~ ~ ~ fill ~1 ~2 ~1 ~-1 ~0 ~-1 air‌[Bedrock Edition  only]. Use the repeating command block with the "Always Active" option selected, and the cube of air will be created wherever a player go. Basically, /fill takes out a specified amount of space, similar to /setblock, but it uses two coordinates and fills the space in between them with the material of the players choosing . In this case, that material would be air. Now, every time a player moves, it will fill a 3×3 cube of air around the player. A destroyer is great for enemy bases, or simply being a crazy griefer.  

- This also deletes water, so the player basically becomes a moving sponge. To not remove water, use/execute as @p at @s run fill ~1 ~2 ~1 ~-1 ~0 ~-1 air keep waterinstead.
- This works in any game mode.

### Landscaper
This is a reversed version of Destroyer. /execute as @p at @s run fill ~1 ~-1 ~1 ~-1 ~-1 ~-1 grass_block‌[Java Edition  only] or /execute @p ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~-1 ~-1 grass‌[Bedrock Edition  only]. This puts a 3×3 grass square under a player.

### Booby traps
An extremely lethal booby trap would be a command block set to teleport someone into the void.

The player can do /kill @e[distance=..2] in a command block below a block with a pressure plate to make a multi-use landmine that kills all nearby entities upon stepping on it (including players, item frames, and paintings)

Note that booby traps that use @p can be dangerous due to the fact that non-player entities could trigger them (if something like a pressure plate is used), resulting in the teleportation of the nearest player, no matter how far away they are and regardless of the fact that they haven't actually stepped on the plate. To get around this, players can either use the /execute if entity command as an invisible pressure plate, or they can do /teleport @p[distance=..<radius>] x y z rot<x> rot<y>. Hook a clock circuit up to a command block programmed with /execute if entity @p[x=1, y=2, z=3, distance=..<radius>], with the coordinates changed as appropriate. Note that as of Java Edition 1.8 a range of zero can now be specified.

### Teleporters
It is possible to make teleporters using the command block. (e.g. /teleport @p <x> <y> <z>) Taking it one step further, a teleporting station can be made, with multiple button-activated teleporters that each teleport to different locations. Scouting and testing teleportation destinations first is advisable, to make sure players don't end up stuck inside blocks or in other unintended places. If players appear in ground while testing coordinates, use /teleport @p ~ ~8 ~ to get out (may require multiple uses).

If a player use the teleport command with the command block, one can use relative coordinates in the destination coordinates by placing an ~ in front of a coordinate (e.g. code: /teleport @p ~ ~8 ~. This would teleport the player 8 blocks into the air).

Commands that use coordinates (e.g. /teleport or /spawnpoint) add 0.5 to whole numbers when no decimal follows. This is so you appear centered over the block you appear on instead of at the edge or corner of it. For example, the number -33 would execute as -32.5, and 187 as 187.5. To prevent this behavior, add .0 (25.3, 90.0) after them, as these values are executed left as-is. 
It is also possible to teleport minecarts or boats, with players in them. The command is /teleport @e[type=boat] <x> <y> <z>.

### Command-Piston-Repeater Fun
- Command block:/setblock <x> <y> <z> minecraft:sand
- 1st Piston Front: Showing to set/setblock <x> <y> <z> minecraft:sandto that position

#### Fast Pusher
Note: Repeaters are risen by 1 block from 1 to 3 for visualization
- 1 (1 Repeater): Set to 1
- 2 (1 Repeater): Set to 3
- 3 (2 Repeaters): Set to 4 and 2
- 4 (1 Repeater): Set to 2
- 5 (2 Repeaters): Set to 4 and 1
- 6 (2 Repeaters): Set to 4 and 4
- 7 (1 Repeater): Set to 2
- 8 and 9 (2 Repeaters): Set to 4 and 4

#### Slow Pusher

- 1 (Repeater): Set to 4
- 2 (Repeater): Set to 4
- 3 (Repeater): Set to 4
- 4 (Repeater): Set to 1
- 5 (Repeater): Set to 1
- 6 (Repeater): Set to 1
- 8 (Repeater): Set to 4
- 9 (Repeater): Set to 2
- 10 (Repeater): Set to 2

### Working Minecart with Dispenser
To create a working minecart with dispenser, run this command:
/summon minecraft:command_block_minecart ~ ~ ~ {CustomDisplayTile:1,DisplayTile:dispenser,DisplayOffset:10}

"CustomDisplayTile" tells the game to render the block in the cart differently. "displayTile" tells it to change it to a certain block ID (a Dispenser). See This Minecraft Forum article for a better explanation of this, and other useful things.

Add this command to the "dispenser" by right clicking it:
/summon arrow ~ ~ ~1.5 {Motion:[0.0,0.0,1.0]}

## Singleplayer non-Creative maps
By swapping gamemode it is possible to use command blocks and functions in single player outside of creative mode. Simply swap to creative mode with the /gamemode creative command, set the command block command to whatever the player want, then swap back to /gamemode survival. The command block only needs to be set in creative, but will still function once back in normal.

It can also be used to teleport to certain areas (for example a far-away stronghold, a deep mining operation, or a floating island). If it took the player a very long time to get there, and if they don’t mind sort-of cheating, then you can set up a teleport system. Make sure that the player are on Creative mode while setting it (use the command /gamemode creative. If they don't have cheats enabled, open the LAN and set the cheats on), but they can still activate it in Survival mode. Type this command in when having the command block GUI open /teleport @p <x> <y> <z>. Then, activate the command block with redstone (including buttons, levers, and pressure plates), and they will be sent to their destination. The player can set up multiple different teleports. This can also be used when doing a big project that spans over a very large area or if they are transferring chests to from an old house to a newer house.

## Multiplayer applications
This section details the applications of the command block in multiplayer.

### Command-based flying
Commands can also be used for flying entities or structures. Most commands based flying machines use command blocks so that when the player turns on an input, it activates certain command blocks. Unlike piston based technologies, however, these cannot be legitimately made in survival as command blocks require set up by an operator in creative mode.

#### 
Using the /tp command, entities can be teleported in a specific direction in small repeated increments, to exhibit a smooth flying. With clever command usage, movement can be controlled by various means such as holding a specific item

#### 
Using the /clone command, it is possible to more easily move structures by cloning them and teleporting entities in it with /tp. It can be accomplished by cloning a structure relative to an entity with /execute. The entity, in turn, can be controlled by some other means.

#### 
Using the /summon command, it is possible to lift an entity with explosions, somewhat similar to real life rockets. This can be done by spawning instantly detonating creepers or TNT below an entity. However, there is a multitude of disadvantages, including:

- It is noisy and potentially laggy compared to most other types of flying.
- This method is destructive to the terrain. Using creepers withoutmobgriefingenabled could solve this.
- Damage to the entity being flown. This can be partially solved withBlast Protection,status effectsor the InvulnerableNBT Tag..

### 
Using the /data command (1.13+), it is possible to change the velocities applied to an entity rideable by the player, such as minecart or boat. 
The equivalent command for versions below 1.13 is the /entitydata command.

### 
Through /teleport, one can create teleporters for public use on a server. It can be applied to a range of scenarios. For example, one could make a system of portals in a particularly large world in which all portals link to a central hub, which contains portals to all other portal locations creating a sort of "Fast Travel Hub" using <X> <Y> <Z>

### Stop-Motion Animation
By using the /clone command with lots of different copies of it, slightly altered bit by bit, and then just clone the areas into one spot in sequence. That way the player doesn't have to be teleported, but the landscape around them can be animated as the clone commands copy the various animation "frames" near the player sequentially.

### Lottery
Through /give @r, one can create a lottery. Keep in mind that now, /give will directly put items into one's inventory, instead of throwing them on the ground in front of the character. 

As mentioned above one can create a lottery but that lottery is usable by the public. A simple edit can change that... First create a new objective. (For example: /scoreboard objectives add lottery dummy) Then use this command on a command block /scoreboard players add <playerName> lottery 1 to enter players into the lottery then do /give @r[scores={lottery=1..}] to start the lottery and only the players chosen can be in the lottery.

### Jails
By rigging a fast clock to a command block executing /teleport , they can force a player to stay at a certain place. If they do this it would be advisable to either turn off commands in their chat settings or do /gamerule commandBlockOutput false. Using the "Range" and "Minimum Range" parameters, they can have it teleport players back only when they're a certain distance away.

Alternatively, giving the player certain status effects at high levels using the /effect command can mimic the effect of a jail. Use /effect give @p minecraft:slowness <insert duration of effect> 127 to keep the player from moving, and /effect give @p minecraft:mining_fatigue <insert duration of effect> 127 to keep the player from breaking things. If player really want to kick it up a notch, poison the player (use one of the previous two commands, but replace the first number with 19).

### Creative Only
By using the parameter [gamemode=creative], only players in Creative will be affected by the command block.

### Fun anti-creative mode trap
If player place a repeating command block with "Always Active" option, they can set /teleport @a[gamemode=creative] ~0 ~1 ~0 for hilarious (like really hilarious) results. This could be a way to get creative mode people to change to Survival and is also really fun to watch.

### Announcements
By using /me in a command block one can create announcements that could play even when the admin or owner wasn't there.

### Security Scan
By using /clear, players can scan people for items. If they want to remove certain items, use /clear <playername> <itemid>. For example, on a server that doesn't want griefing, players could have a clock connected to a command block set to /clear @a minecraft:flint_and_steel.

### Race Referee
Using /say @p, the command block can report the nearest player. If the command block is placed after a finish line, it will say the finishers in order. Players can also do /tellraw @p {"text":"THIS IS A MESSAGE"} and when activated the message "THIS IS A MESSAGE" will come up on the chat system. Players can also color the text using "color" at the end of the next command /tellraw @p {"text":"THIS IS A MESSAGE","color":"green"}.

### 
Creating a "Creative Only" zone is possible through command blocks, but it is complex and more of a case-by-case basis. The basic idea would be to create a "fence" of command block affected zones so that, once a player flies in creative through it, they would be changed to survival or adventure mode. 
A "World Guard" zone would be a lot simpler, just have a command block do /gamemode adventure @a[x y z r m] and when people leave, just have a button to change them to survival.

One could also utilize the distance argument defining an area-of-effect /gamemode adventure @a[gamemode=!creative,distance=0..(X)] combined with a deactivating command block /gamemode survival @a[gamemode=!creative,distance=(X+2)..(X+12)]. Set both blocks to repeat and be self-powered and there should be a fairly "seamless" transition zone between normal and protected. The distance variables for the range of effect (specifically the reversion block) can vary, but a buffer between the X and X+2 variables should be there to accommodate the second block being at a different position than the protection block. The gap between the two variables in the reversion block need not be exactly 10 blocks, but a buffer helps for lag concerns in guaranteeing that once left, a player will revert back to survival mode. 

Do note that if you have a nether portal within the protection zone, that the player will NOT be reverted to survival once they step through, so place a reversion cube of any type (Impulse or Repeating) in the Nether on the other side of that portal.

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

### Detecting Cheaters
Using parameter [gamemode=creative], the player can affect those who are in Creative, or Survival with parameter [gamemode=survival].

### 
This is a simple one, just have a system of teleporting command blocks at the entrance/exit of a place, and players can build the interior somewhere else, allowing them to cheat space restriction. (example of use: you want interior walls to be wool, but exterior walls to be wood (normally 2m thick walls).
You can make the outside of the house be 8×10 m, and the inside of the house be 8×10 m.) Or, have the inside of the house 20×20 instead.

### Save game
By using the /spawnpoint command, one can easily make a button-activated checkpoint.

### Lava parkours
As said before, there is a command that makes the player able to keep their inventory upon death: /gamerule keepInventory true. Simply connect this to a pressure plate before a parkour level over lava and you don't have to use any kind of chest minecart (especially useful when the player has it's full inventory, which is bigger than a single chest).

### 
It's true that the /spawnpoint command can be useful because you don't have to wait for the night to create a checkpoint, but sometimes you may want to have a BUD switch connected to the bed or something similar, so that you don't have to type the command in every time. To do this, you just need to have a discreet pressure plate connected to a block with the /time set 18000 command, and it will set the time to night so the player can sleep.

### Time and weather following the scenario
Many times, a player will be building something, and it will start raining or start to get dark, which both can be disturbing to the player. Fortunately, you can use commands to turn off the rain, as well as make the sun go back to sunrise. To toggle rain on and off, just use the /weather command. Use clear if you want to clear the weather, or rain or thunder, if you would like to toggle on rain or a thunderstorm. For example, if you want the weather to be rain but not thunder, type in the /weather rain command. 

Along with this, you can also use /time set with a number: 23250 is sunrise, 6000 is midday, 12750 is sunset and 18000 is midnight. So, if you want to set the time to sunrise, type in the chat: /time set 23250.

### Detecting Players who switched to Peaceful
** Note:  The difficulty for a specific world can be locked as of Java Edition 1.8. **
Create a hostile mob (so it disappears when switching to Peaceful) that never despawns if the player is far away. To do so, use a name tag on the mob (or third party software if you are playing in a version previous to 1.5.2) and place it on a pressure plate. Make sure it will keep it pressed infinitely, so make sure surround it with 2 high blocks or fences, so that it can't jump or walk away. Make a redstone circuit that causes a command block to activate when input from pressure plate ceases to exist. Place a message inside the block that informs the player on chat that the map has been broken and must be redownloaded. This way, switching to Peaceful will cause the mob to vanish and activate the message. You can even make a teleportation command block so that a cheater is banished from the map to a small room without a way out as soon as they switch to Peaceful.

### Talking Adventure Map
The /say command is extremely useful because it simply prints text into the chat. It may be one of the better uses of the Command Block as you don't need silly signs or long books to show the game rules. Just put a bunch of command blocks in lines with repeaters set to two or three ticks (to avoid spamming players) allowing you to easily remove a chest of books or a large number of signs. 

Another use of /say is talking NPCs and other mobs. Imagine you enter a butchery and you want the butcher to say something. Usually, you might use signs or books, using up room in the butchery and having seemingly random objects strewn around a map. With the /say command you can make the butcher talk. Maybe a pig behind the counter could even beg for mercy! Let's take another example: you are in a factory and an alarm suddenly rings and says in chat it will explode. Having it in the chat, especially if the text is long, keeps the stressful mood; the same thing works for bomb timers. The situation might feel tenser if the chat displays '10..' '9..' 8..' individually as well.

Last but not least, it makes it easier to create a Quest System. Let's say the player gets in a butchery. It activates through a pressure plate connected to a RS NOR Latch (to avoid activation twice) and a command block with the /say command in which the butcher asks for the player's help: they need to kill a pig. The player gets to the pig that is standing on a stone pressure plate, that turns off when the pig is dead. So, when the player gets back to the butchery, it activates another circuit containing yet another RS NOR Latch and two command blocks with two commands. First, the /say command in which the butcher thanks the player, and another one, the /give command, so the player gets the reward. Along with that, don't forget to use the @p command so the butcher says the player's name. For example, if the command block is set to do this: /say Thanks, @p. You helped me a lot killing that pig., the channel will say: "[@]: Thanks, <name of the player>. You helped me a lot killing that pig." This increases immersion into the map, as the NPCs seem tailored for the player. You could also change [@] to [Butcher] by renaming the /say command block using an anvil.

### Making a Store
By using /give @p[level=<level>..] <item> <amount> and /experience add @p[level=<level>..] -<level> levels you can make a shop system that trades a certain amount of exp for items. For instance, if you made a command block with /give @p[level=5..] grass_block 64 and another with /experience add @p[level=5..] -5 levels connected to the same redstone current, it will take 5 levels from the player, and in return, give them 64 grass blocks.

- Subtracting experiencecanwork as a currency, by using the command/experience add @p[level=3..] -3 levels. The minimum experience for the command to work can be listed inside the brackets.

Custom villagers selling whatever you want can be created with command blocks. Custom villagers are not available through Minecraft: Bedrock Edition. 
e.g.: /summon villager ~-2 ~0 ~0 {Profession:3,CustomName:BLACKSMITH,CustomNameVisible:0,Offers:{Recipes:[
{maxUses:13,buy:{id:388,Count:5},sell:{id:283,Count:1,tag:{ench:[{id:16,lvl:9},{id:20,lvl:6}],display:{Name:Molten Gold Sword}}}},{maxUses:13,buy:{id:388,Count:1},sell:{id:280,Count:1,tag:{ench:[{id:16,lvl:5}],display:{Name:Whuppin Stick}}}},{maxUses:13,buy:{id:388,Count:2},sell:{id:369,Count:1,tag:{ench:[{id:16,lvl:5},{id:20,lvl:10}],display:{Name:Radioactive Whuppin Stick}}}},]}}

The part labeled "Buy" is what the villager is accepting as payment, the part that says "sell" is what he's giving in return. You can change the maxUses to 1000 if you never want the offer to run out, or to 1 if you want to make it a one-of-a-kind item. Note that the first item there (the gold sword) has an out of range enchantment (sharpness 9). Yes this works, but always research what exactly the enchantment does before making an out of range one as some stuff does nothing or even does negative effects (respiration's "see underwater" side effect makes everything a blinding white at high levels, as if you dove into slush-filled arctic waters). As for that gold sword, keep in mind that gold swords wear out insanely fast (there's a reason people call them butter swords after all). A level 10 Unbreaking enchantment should bring a gold sword up to a decent durability level. Also notice that the other 2 "weapons" are actually a Stick and a Blaze Rod with weapon enchantments on them. Using any non-weapon as a weapon does the same damage as an empty hand (1 damage, aka half a heart) but the enchantments on these ones make them the equal of an unenchanted sword. The advantage is that sticks, blaze rods, or other items is that you can use it infinitely. The same trick can be used with mob heads and respiration 3 to make an infinite durability scuba mask.

## Spawners
Command blocks can create spawners using the /setblock command, e.g.: /setblock ~1 ~-1 ~0 spawner{SpawnData:{id:zombie,HandItems:[{id:iron_sword,Count:1}]}} Anything that counts as an entity can be spawned (except a player), which includes all mobs, as well as minecarts, fireballs, arrows, snowballs, ender pearls, custom thrown potions, fireworks, primed TNT, falling sand, red sand, or gravel, paintings and item frames, experience orbs, and even dropped items of any type. 

Pig, cow, or chicken spawners can be placed in the butcher's backyard in a village to create a constant meat supply. E.g.: /setblock ~1 ~-1 ~0 spawner{MaxNearbyEntities:10,RequiredPlayerRange:16,SpawnCount:6,SpawnRange:2,MinSpawnDelay:50,MaxSpawnDelay:200,SpawnData:{id:pig,Passengers:[{id:chicken}]}} Note that the spawner in the last code example will spawn a chicken riding a pig. There doesn't seem to be a limit to how many levels of riders you can use. For example, you could create a chicken riding a pig riding a cow riding a horse riding a silverfish riding a villager ("Say, that's a mighty odd hat you have on, Farmer Brown"). 

Please note that if you want to use the RequiredPlayerRange tag you have to use the MaxNearbyEntities tag as well. The same thing applies to MinSpawnDelay and MaxSpawnDelay. Lastly, note that the y value used in both of those spawner example codes was ~-1, which (assuming the player are not flying) will put the spawner in the surface level of the ground at your feet.

If you don't want to target a specific player, you can use @a, @p, or @r instead of <player>. Keep in mind that you can use @p (which means closest player) in player issued commands as an easy to type 2 character replacement for your own name as the closest player to you will always be you.

#### Part 1: The Basics
This code will create a zombie spawner 2 blocks from you in the x direction. Note that the name given for mob spawners in this code (minecraft:spawner) is the long version and you can leave out the minecraft: part.

/setblock ~2 ~0 ~0 minecraft:spawner{SpawnData:{id:zombie}}

This next code is also pretty basic but it includes the 6 basic parameters that can be set.

/setblock ~0 ~-1 ~-3 spawner{SpawnRange:4,RequiredPlayerRange:16,SpawnCount:4,MaxNearbyEntities:6,MinSpawnDelay:200,MaxSpawnDelay:800,SpawnData:{id:skeleton}}

Notes:

- All times are in game ticks (20ths of a second). 200-800 is 10–40 seconds.

- Keep in mind that they are in groups of 2 and won't work if their partner is missing. SpawnRange requires RequiredPlayerRange (and vice-versa), MinSpawnDelay requires MaxSpawnDelay, and assuming SpawnCount needs MaxNearbyEntities.

- There is also a parameter called "Delay" which contains the amount of time before next spawn (20 ticks for the first time, whatever random number it picks between MaxSpawnDelay and MinSpawnDelay every other time).

- The coordinates given are ~0 ~-1 ~-3 (so 3 blocks in the negative Z direction from the commandblock's current position and 1 block down). This presumably will imbed it in the surface of the floor. Keep in mind that a spawners "SpawnRange" setting only applies horizontally not vertically. Vertically it will only spawn at the same height or 1 lower or higher, so imbedding it in the surface of the floor cuts the available spawn area by 2/3rds (but can help hide it). Naturally occurring spawners have their height cut by 1/3rd due to appearing 1 block above the floor instead of 2.

- All the values used here are the defaults.

#### Part 2: Custom monsters
The next thing to do is to modify the spawn data. Spawn data is what tells the spawner you want a non-standard version of a monster, such as a zombie with a diamond sword and a chain helmet.

/setblock ~ ~1 ~ spawner{SpawnData:{id:zombie,HandItems:[{id:diamond_sword,Count:1}],ArmorItems:[{},{},{},{id:chainmail_helmet,Count:1}]}}

Using ~ without any number after it in the coordinates counts as zero. Because of the fact that none of those 6 parameters from the last example are used, they will all be defaults.
Note that there are now two types of item slots, Hand and Armor. Hand items are in the order Mainhand, Offhand, while armor items go in the order Boots, Legs, Chest, Helmet. You must even specify empty slots (the { }, parts), unless they're after the last non-empty slot. So, if you want your custom mob to have a helmet, you have to specify all 5 slots, but if it's just boots, you can leave off the other 3. Likewise, if you want them to have leg armor. you have to specify the boot slot, but not chest and helmet slots.
Remember that creatures that burn in sunlight are safe if they have a helmet on, although it damages the helmet instead.
As for the count tag, most codes can get away with leaving it out; however, it is important. An item without a count tag is a stack of zero, better known in the community as a "Ghost Item". A player trying to use a ghost item will have it disappear out of their hands with its first use (which is a failure). While monsters can use ghost items without problem (hence why codes get away with leaving it out sometimes), if they drop the items the player who picks it up won't be able to use it, so it is highly recommended to use the count tag.

The next example of customized monsters, consists of a skeleton with an enchanted bow (Flame) with a custom mob head (Spider, internet connection required or it's just Steve) with Protection 2 riding a Skeleton Horse.

/setblock ~2 ~1 ~2 spawner{SpawnData:{id:skeleton_horse,Tame:1,Passengers:[{id:skeleton,HandItems:[{id:bow,Count:1,tag:{Enchantments:[{id:flame,lvl:1}]}}],ArmorItems:[{},{},{},{id:player_head,Count:1,tag:{Enchantments:[{id:protection,lvl:2}],SkullOwner:MHF_Spider}}]}]}} replace 

As of 1.12, passengers can control their mounts to an extent, which means that former issues with Zombie passengers are no longer extant. A more in-depth look at the behavior of passengers and mounts can be found at Tutorials/Summoning Jockeys. 
The skeleton horse has Tame set to 1 (yes). Note that there is currently an ongoing bug where summoned mobs riding horses with saddles cannot move, regardless of whether the horse is tame. Technically you can have multiple levels of riders, although this gets silly quickly.

#### Part 3: SpawnPotentials
Using the SpawnPotentials tag, you can create a mob spawner with multiple mobs in it. It will randomly pick one each time when the timer is reset (a second after spawning the previous mobs). Since these codes contain multiple mobs, they tend to be quite long codes. Here's a version of the SpawnPotentials code, that is easier on the eye:br>

/setblock ~ ~1 ~1 spawner{SpawnRange:6,RequiredPlayerRange:12,SpawnCount:1,MaxNearbyEntities:6,MinSpawnDelay:100,MaxSpawnDelay:600,SpawnData:{id:"zombie",HandItems:[{id:"wooden_sword",Count:1},{}],ArmorItems:[{id:"leather_boots",Count:1},{id:"leather_leggings",Count:1,tag:{display:{color:5013401}}},{id:"leather_chestplate",Count:1,tag:{display:{color:6717235}}},{id:"player_head",Count:1,tag:{SkullOwner:Reimac}}]},SpawnPotentials:[{Entity:{id:"zombie",HandItems:[{id:"wooden_sword",Count:1,tag:{Damage:58}},{}],ArmorItems:[{id:"leather_boots",Count:1},{id:"leather_leggings",Count:1,tag:{display:{color:5013401}}},{id:"leather_chestplate",Count:1,tag:{display:{color:6717235}}},{id:"player_head",Count:1,tag:{SkullOwner:Reimac}}]},Weight:4},{Entity:{id:"skeleton",HandItems:[{id:"iron_sword",Count:1},{}],ArmorItems:[{id:"leather_boots",Count:1,tag:{display:{color:1644825}}},{id:"leather_leggings",Count:1,tag:{display:{color:1644825}}},{id:"leather_chestplate",Count:1,tag:{display:{color:1644825}}},{id:"player_head",Count:1,tag:{SkullOwner:2insanepeople}}]},Weight:2},{Entity:{id:"zombie",HandItems:[{id:"stone_sword",Count:1},{}],ArmorItems:[{id:"chainmail_boots",Count:1,tag:{Enchantments:[{id:"protection"}]}},{id:"chainmail_leggings",Count:1,tag:{Enchantments:[{id:"protection"}]},{id:"chainmail_chestplate",Count:1,tag:{Enchantments:[{id:"protection"}]},{id:"player_head",Count:1,tag:{SkullOwner:Flixnore}}]},Weight:4},{Entity:{id:"zombie",Fire:2400,HandItems:[{id:"golden_sword",Count:1,tag:{Enchantments:[{id:"punch",lvl:1}]}},{}],ArmorItems:[{id:"golden_boots",Count:1},{id:"golden_leggings",Count:1},{id:"golden_chestplate",Count:1},{id:"carved_pumpkin",Count:1,tag:{Enchantments:[{id:"protection",lvl:2},{id:"fire_protection",lvl:10}]}}]},Weight:4},{Entity:{id:"zombie",HandItems:[{id:"iron_sword",Count:1,tag:{Enchantments:[{id:"sharpness",lvl:2}]}},{}],ArmorItems:[{id:"iron_boots",Count:1},{id:"iron_leggings",Count:1},{id:"iron_chestplate",Count:1},{id:"player_head",Count:1,tag:{ench:[{id:0,lvl:2}],SkullOwner:2zqa}}]},Weight:4},{Entity:{id:"zombie",HandItems:[{id:"diamond_pickaxe",Count:1,tag:{Enchantments:[{id:"sharpness",lvl:4},{id:"knockback",lvl:4},{id:"bane_of_arthropods",lvl:4},{id:"looting",lvl:3},{id:"unbreaking",lvl:3}]}},{}],ArmorItems:[{id:"diamond_boots",Count:1,tag:{Enchantments:[{id:"fire_protection",lvl:4},{id:"feather_falling",lvl:4}]}},{id:"diamond_leggings",Count:1,tag:{Enchantments:[{id:"blast_protection",lvl:4}]}},{id:"diamond_chestplate",Count:1,tag:{Enchantments:[{id:"protection",lvl:4}]}},{id:"player_head",Count:1,tag:{SkullOwner:MHF_Herobrine,Enchantments:[{id:"protection",lvl:4},{id:"fire_protection",lvl:4},{id:"blast_protection",lvl:4},{id:"thorns",lvl:3},{id:"respiration",lvl:1}]}}],CustomNameVisible:1,CustomName:'"Herobrine"',PersistenceRequired:1},Weight:1}]}
It contains a lot of codes, because of the fact that it is actually 6 separate mobs. In order we have:

- Before the "SpawnPotentials" tag: The starter, which will never pop up again after the first time. If you want to see him again, you have to include him a second time under SpawnPotentials. Its appearance is just a random person in blue jeans (blue dyed leather leg armor), and a green dye shirt (green dyed leather tunic), with a wooden sword. He's a zombie under that mob head of it, of course.
- Same thing, only this time, the wooden sword is 2 hits away from breaking.
- The next one has a ninja-like appearance. This one is a skeleton under its mask, but he's been given an iron sword. All of its leather armor is dyed ninja-black. Skeletons with swords close the gap quicker than zombies, so watch out.
- Zombie with a stone sword and chain armor, with Protection II on its mob head.
- The next one has a gold sword, golden armor, a pumpkin on its head, and he's on fire! The pumpkin is enchanted with Protection II and Fire Resistance X in a desperate attempt to keep him on its feet and threatening the player for more than 5 seconds. It works, but if the player plays keep away then the zombie does tend to burn to death. Its sword has fire aspect too.
- Iron Sword and Armor. Sharpness II on its sword, Protection II on its mob head.
- The final mob, fakeHerobrine, here has highly enchanted diamond armor (boots with Fire Protection IV and Feather Falling IV, leggings with Blast Protection IV, a chestplate with Protection IV, a mob head with Protection IV, Fire Protection IV, Blast Protection IV, Respiration III) and a diamond pickaxe enchanted with Sharpness IV, Smite IV, Bane of Arthropods IV, Looting III and Unbreaking III. Its also got the previously unseen CustomNameVisible (set to 1 for yes), a CustomName, and PersistenceRequired (set to 1 for yes). That last one will prevent it from ever despawning, although it can be killed normally. If you can get through that diamond armor and level 4 resistances.

Other than the ninja, it's a straight tour of the 5 tiers of swords and armor. Note that the Weight tag, used right after the Entity tag in each SpawnPotential. That determines how rarely it's picked. Specific numbers don't mean anything, just the ratios between the numbers. For example, if you want all the potentials to have an equal chance just set all the weights to 1. Changing them all to 8 wouldn't do anything different (they're still all the same size as each other), however, changing all but one to 8 would make that one 1/8th as likely as the rest. In this code, 4 is the default. The ninja only has a weight of 2 (making him half as likely to be picked) and fake Herobrine has a weight of 1 (making him 1/4th as likely to be picked, and thank god!)

#### Part 4: Rideable Monsters
Mobs can be ridden by using Minecarts or Boats on their heads. The command is fairly simple:

/setblock ~ ~1 ~ minecraft:spawner{SpawnPotentials:[{Entity:{id:"<Entity>",Passengers:[{id:"minecraft:minecart"(or "minecraft:boat")}]}}]}

Tips: 

- Bosses can also be spawned with a spawner. Adding aminecartis also possible.
- Hostile mobs with shooting abilities can and will use them against survival players. Watch out.
- Although the minecart would stuck in their head,ghastscan also be ridden. However, you may need anelytraor atridentenchanted with riptide to do that.
- Endermencannot be walked around, but they can be forced to teleport by shooting a projectile at them (e.g.; snowball).
- Ocelotsare some of the fastest mobs to ride, seeing they're trying to get away from you. They can also be partially controlled, by pointing away from the place you want to go.
- Spidersare the only mobs that slow down when ridden.
- Slimesand their Nether cousins,magma cubes, can have their sizes changed.

## More commands in fewer command blocks and recursion
There are several ways to combine groups of commands into just one command.

Use the following sets of commands for recursion:
/scoreboard objectives add counter dummy
/scoreboard players set target_count counter <target count>
/execute if score count counter < target_count counter <chained command>
/execute unless score count counter < target_count counter run scorebard objectives remove counter
/scoreboard players add count counter 1

To run multiple commands, summon a command-block minecart riding another command-block minecart riding another, with the commands in reverse order, on an activator rail. There are also commands called one-command tool that use this tactic.

## Using a map item as a scroll
A YouTuber called SethBling used a map as a scroll to perform commands (summon creatures, teleport). The player will have an empty map in the inventory and when the player uses it, it becomes a filled map which immediately disappears and a redstone task is done.

Pros

- Fast redstone interaction.
- Compact system.
- At-will triggered system, just right-click to activate it.
- Single use: the map disappears during the inventory check, but you can give it back through/give.

Cons

- There can only be one purpose for the scroll, i.e. players cannot do a scroll of teleporting and a scroll of strength without using complicated data values.
- The player may see the map animation when activating the map before it gets deleted.
- The player cannot use the map item during your playthrough (showing a text message, a path, a drawing, …).

Building the mechanism

The player can change the display name of an item to give the player a better understanding of the object and use the tooltip display. Use the following command to give the player a custom named map:
/give <player> map{display:{Name:"<displayName>",Lore:["<tooltip>"]}}

- player: the player you want to reach (@p, @a[arguments],...).
- displayName: the name displayed when you scroll in the hotbar or when you hover the item with your mouse.
- tooltip: the text below the item name when you hover it.

Detecting the activation of the map



- The two hoppers form a redstone clock. You can use other clocks shownhere.
- The Command block 1 contains the/givecommand described in the section above. It can be dismissed if the player doesn't want the scroll to come back after being activated.
- The Command block 2 contains the inventory check command:

/clear <player> filled_map

- The Command block 3 is the output in case of success. You can do whatever you want: give an effect to the player, teleport him somewhere,... You can also wire this output to a door, a piston,...

Going further
The /clear command can check for other interactive items:

- Check for aglass bottleif the player just drank a potion.
- Check for afishing rodwhen the line is reeled in. The/clearsyntax involves another argument, the damage value, after the item name:

/clear <player> fishing_rod{Damage:2}
Note that spamming the reel, or hooking a mob, may damage it more than 2, so make another one of these every 2.

## Further reading
- Feare's Command Block Tutorials(Not Found)

- Dragnoz' YouTube tutorials to a lot of possibilities using data tags(Out of date)

