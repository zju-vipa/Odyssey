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

