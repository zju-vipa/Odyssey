## Command randomizers
### Tick-based
This randomizer uses a repeating command block adding 1 point to a score per tick, then another repeating command block truncating the value to its maximum. When a random value is needed, repeating command blocks testing for certain values are used. This setup is not completely random as it is based on the time it is activated, but is random enough for most purposes.

In this example, the minimum value is 10 and the maximum is 20.
To start, a dummy scoreboard  objective must be created to store the values: /scoreboard objectives add randomizer dummy. Next, two repeating command blocks are needed, both set to "always active". The first one adds 1 point to the score every tick: /scoreboard players add ticks randomizer 1. The second one truncates the value to the aforementioned minimum and maximum: /execute if score ticks randomizer matches 21.. run scoreboard players set ticks randomizer 10 (where "21" is the maximum exclusive value and "10" is the minimum value). Finally, a set of command blocks testing each value are needed, all attached to the single input; for example, /execute if score ticks randomizer matches 12 run say hi will run /say hi (placing [@] hi in chat) if the random value between 10 and 20 is 12. The following schematic shows an example setup where the command blocks testing each value are attached to an input:

























































































Tick-based randomizer
### Random target selector based

  

This tutorial is exclusive to  Java Edition. 


The randomizer is based on the random target selector criteria (limit=1,sort=random). It is a derivative of the idea by NOPEname.[4]

At startup, run the following commands. You may wrap them in a function for convenience.

scoreboard objectives add RandomBit dummy
execute unless entity @e[type=armor_stand, tag=RandomizerResult] run summon minecraft:armor_stand 0 -1 1 {Marker: 1b, NoGravity: 1b, Invisible: 1b, Silent: 1b}
tag @e[type=armor_stand,x=0,y=-1,z=1] add RandomizerResult
scoreboard players set @e[tag=RandomizerResult] RandomBit 0
execute unless entity @e[type=armor_stand, tag=Randomizer] run summon minecraft:armor_stand 0 -1 0 {Marker: 1b, NoGravity: 1b, Invisible: 1b, Silent: 1b}
execute unless entity @e[type=armor_stand, tag=Randomizer] run summon minecraft:armor_stand 1 -1 0 {Marker: 1b, NoGravity: 1b, Invisible: 1b, Silent: 1b}
tag @e[type=armor_stand,x=0,y=-1,z=0] add Randomizer
tag @e[type=armor_stand,x=1,y=-1,z=0] add Randomizer

The execute unless part is not necessary, but it is helpful if you do wrap them in a function and want to invoke the function multiple times (e.g. for testing).

Every time you need to obtain a random bit (0 or 1), you can run the following commands, either manually, via a chain of command blocks, or a function.

tag @e[type=armor_stand,tag=Randomizer] remove PickedBit
tag @e[type=armor_stand,tag=Randomizer,sort=random,limit=1] add PickedBit
execute store result score @e[type=armor_stand, tag=RandomizerResult] RandomBit run data get entity @e[type=armor_stand, tag=PickedBit,limit=1] Pos[0]

Now you have a scoreboard objective with a randomized bit. This method can easily be extended to generate a random number in a large range.

### 

  

This tutorial is exclusive to  Java Edition. 


As of Java Edition 1.20.2, there is native support for generating randomized values with the /random command.

### Bedrock Edition

  

This tutorial is exclusive to  Bedrock Edition. 


There is native support of randomized scoreboard objectives in Bedrock in the form of /scoreboard.


