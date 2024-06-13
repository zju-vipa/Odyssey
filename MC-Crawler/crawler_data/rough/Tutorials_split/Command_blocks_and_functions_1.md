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

