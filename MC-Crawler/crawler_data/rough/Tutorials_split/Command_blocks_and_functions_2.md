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

