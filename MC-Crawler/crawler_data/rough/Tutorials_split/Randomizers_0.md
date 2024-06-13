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


