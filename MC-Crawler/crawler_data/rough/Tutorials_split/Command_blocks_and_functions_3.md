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

