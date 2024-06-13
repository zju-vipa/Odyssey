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

