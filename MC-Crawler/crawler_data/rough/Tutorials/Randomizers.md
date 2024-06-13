# Tutorials/Randomizers
Randomizers are redstone circuits that generate random signals. They can be used in a multitude of things, from running a light show, to making a casino. Note that randomizers, like the majority of redstone circuits, will only work in active chunks. If this is wanted for a adventure map or something where the player may get far away, it may be desirable to build the randomizer in spawn chunks‌[Java Edition  only] or a ticking area.‌[Bedrock Edition  only]

## Contents
- 1 Physical randomizers
	- 1.1 Dropper randomizer
	- 1.2 Shulker box randomizer
	- 1.3 Mob randomizer
	- 1.4 Jukebox randomizer
	- 1.5 Randomizers with analog signal output
		- 1.5.1 Analog 2-RNG
		- 1.5.2 Analog 3-RNG
		- 1.5.3 Analog 16-RNG
	- 1.6 Randomizers with digital signal output
- 2 Command randomizers
	- 2.1 Tick-based
	- 2.2 Random target selector based
	- 2.3 /random command based
	- 2.4 Bedrock Edition
- 3 References

## Physical randomizers
### Dropper randomizer

















A dropper randomizer
This randomizer utilizes the fact that droppers dispense items in random order. It will output a random signal strength of 1 or 3 whenever a signal is provided. To create it, place a dropper, hopper, and comparator as shown. Then put items of varying stack size into the dropper, e.g. a sword and a piece of dirt. When you power the dropper, it will put an item into the hopper, turning on the comparator. Since the items take up different amounts of space, the power level will vary. It may seem as if adding items that stack to sixteen will allow an output of two, but unfortunately unless the hopper is weighted with items beforehand, items that stack to 16 only result a level of one.

### Shulker box randomizer
Shulker boxes have the ability to be placed by dispensers, broken by pistons, and retain their items. When a shulker box is randomly placed by the dispenser, a comparator can produce 15 unique redstone signals.

### Mob randomizer



























































Mob randomizer with tripwires







































Mob randomizer with pressure plates (redstone revealed)
A mob randomizer is the general term for randomizers which use mobs to trigger redstone with their random wandering. This type of randomizer is best when several outputs are wanted and it doesn't matter when the signal occurs or for how long. Mob randomizers are usually created with either pressure plates or tripwires. Using tripwire is probably the easiest method, but it requires more iron.

The type of mob used in the randomizer can create some important variations. Some common choices include:

- Chickens, because they are small and can easily bereproduced.
- Snow golems, because they are silent.
- Pigsand other two-wide mobs, because they are less likely to not be triggering anything.
- Batsbecause they toggle it on and off frequently.

### Jukebox randomizer










In






Jukebox randomizer
This randomizer uses jukeboxes and hoppers to generate a redstone signal with a random strength from 1 to 12. This is unique because most other randomizers do not generate analog signals with so many possibilities. The two downsides to this randomizer are that it can only generate signals as fast as it takes for each music disc to finish playing and that it can be somewhat expensive.

### Randomizers with analog signal output
#### Analog 2-RNG



→







→













Analog 2-RNG
The dropper contains one stackable item and one non-stackable item.


1×3×2 (6 block volume), 1-wide, flat, silent
circuit delay: 3 ticks (rising) and 1 tick (falling)
Outputs either power level 1 or 3 while on, power level 0 while off.

When the input turns on, the dropper will randomly choose to push either the stackable item or the non-stackable item into the hopper, causing the comparator to output either power level 1 or 3. Because the powered dropper is a solid/opaque block, it will also deactivate the hopper, preventing it from pushing the item back to the dropper until the input turns off.

The output power level can be used as is (for example, to subtract 1 or 3 from a comparator in subtraction mode), but more often the output is connected to a line of two redstone dust so that the output is 0 or not 0 (to randomly power a repeater, activate a mechanism component, etc.).
Variations: If the dropper is powered indirectly (for example, by quasiconnecitvity or an adjacent powered block), the hopper won't be deactivated and will immediately push the item back into the dropper. This turns the circuit into a monostable rising edge detector with a 3.5-tick output pulse (still with a random power level of 1 or 3).

With only two items in the dropper, both output power levels will be chosen with equal probability. The probability of the output levels can be changed by adding additional stackable and non-stackable items to the dropper (which must all be different from each other so they won't stack). For example, with two different stackable items and three different non-stackable items, the RNG will output power level 1 40% of the time and power level 3 60% of the time.

Earliest Known Publication: March 14, 2013[1]


#### Analog 3-RNG














→







→













Analog 3-RNG
The dropper contains one 64-stackable item, one 16-stackable item, and one non-stackable item.



The hopper contains five 16-stackable items in the far right slot.

5
1×3×3 (9 block volume), 1-wide, silent
circuit delay: 3 ticks (rising) and 1 tick (falling)
Outputs power levels 1, 2, or 4 while on, power level 1 while off (but see variations below).
When building this circuit, wait until the hopper is deactivated by the powered dust before putting five 16-stackable items in its far right slot. Then put a 64-stackable item, a 16-stackable item, and a non-stackable item in the dropper.
Before the input turns on, the hopper's five 16-stackable items are enough to produce a power level 1 output from its comparator (even a single 64-stackable item would be enough for that). These five items should never be returned to the dropper, so the comparator's output will never drop below power level 1.
When the input turns on, the dropper will push an item into the hopper, which will be placed in the hopper's left slot. It takes 23 64-stackable items (or five 16-stackable items and three 64-stackable items, or six 16-stackable items) to produce power level 2, so if the 64-stackable item is pushed that won't be enough to increase the output power level, but if the 16-stackable item is pushed the output power level will increase to 2. And if the non-stackable item is pushed, the output power level will increase to 4.
The hopper is held deactivated by the powered dust when the circuit is off, and by the powered dropper when the circuit is on. But, when the input turns off, there is a brief 1-tick moment when the dropper has just turned off, but the torch attached to it hasn't turned on again. This allows the hopper to activate for 1 tick, pushing an item back into the dropper. A hopper always pushes items from its left slots first, so the hopper will push back the item the dropper pushed into it, rather than any of the 16-stackable items in its far right slot, allowing the circuit to reset itself.
Variations:The player can remove one of the items from the dropper to create a 2-RNG with different power level outputs than the regular 2-RNG: removing the 64-stackable item outputs power levels 2 or 4, removing the 16-stackable item outputs power levels 1 or 4, and removing the non-stackable item outputs power levels 1 or 2.
You can add additional redstone dust leading from the hopper to a block next to it, and then down to the side of the comparator. This 2-wide variation will keep the comparator's output off while the input is off.
With only three items in the dropper, all three output power levels will be chosen with equal probability. The probability of the output levels can be changed by adding additional 64-stackable, 16-stackable, and non-stackable items to the dropper (which must all be different from each other so they won't stack). For example, with one 64-stackable item, one 16-stackable item, and two different non-stackable items, the RNG will output power level 1 25% of the time, power level 2 25% of the time, and power level 4 50% of the time.
Additional items can be added to the hopper to increase all of the output power levels.
Earliest Known Publication:16 April 2013[2]

#### Analog 16-RNG
5×8×4 (160 block volume)
circuit delay: 8.5 ticks
Outputs power levels 0 to 15 while on, power level 1 while off.
Uses four 2-RNGs to subtract 1, 2, 4, and/or 8 from 15.
Reducing the number of 2-RNGs reduces the possible outputs: three 2-RNGs produces an 8-RNG, and two 2-RNGs produces a 4-RNG (the exact power levels depend on the power level provided to the subtraction comparators).
Earliest Known Publication:June 10, 2013[3]
Schematic: Analog 16-RNG View at: Mechanics/Redstone/Miscellaneous circuits/analog 16-rng [edit]
### Randomizers with digital signal output
Digital randomizers work by randomly generating a binary number and selecting a corresponding output using a binary decoder. To achieve a flat probability the bits are randomly generated, typically using an analog randomizer with a 50% chance of activation and a red-coder.

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

