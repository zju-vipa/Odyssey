# Tutorials/Zero-ticking
This tutorial seeks to teach the player how to make a redstone signal turn on and off in the same tick, go over how this could be used, particularly with its uses on pistons.

## Contents
- 1 Introduction
	- 1.1 Zero-tick pulse generation
	- 1.2 Zero-tick chaining
	- 1.3 Zero-tick repeaters
	- 1.4 Creating a zero-tick clock
- 2 Uses of zero-ticking
	- 2.1 Embedding entities
	- 2.2 Fast block farms
	- 2.3 Zero-tick plant farms

## Introduction
When a redstone signal is sent through a pulse limiter, it shortens the pulse. When the pulse is shortened enough, strange behaviors arise. If a sticky piston is powered by a 2-tick pulse, it will start extending but after two ticks, the piston will drop its block and start retracting. If a sticky piston is powered by a 1-tick pulse, the same behavior will happen, but instead of happening after 2 ticks it will only happen after one tick.

When a piston receives a pulse that turns on, and then off in the same tick, this is known as a 0-tick pulse. This will cause sticky pistons to instantly drop their block and start retracting.‌[Java Edition  only]. Regular pistons will start retracting instantly when powered by a 0-tick pulse, but the block will not instantly teleport unlike sticky pistons. Because a 0-tick pulse turns on and off in the same tick, many 0-tick pulses will not render, but the pulse still exists. Due to how 0-tick pulses work, some 0-tick pulses are unable to bud-power pistons in some circumstances.

### Zero-tick pulse generation
See also: Pulse circuit § Pulse limiter

All 0-tick pulses are created by powering a redstone line, and then using pistons to remove the power source later in the tick. 























Producing a 0-tick pulse using tile tick priorities

One method of doing so is using tile tick priorities. Since comparators are processed in a tick later than repeaters, one can generate a 0-tick pulse by powering a redstone line using this behavior. In this example, redstone repeater is used to power the output line, and a comparator is used to power a piston which will remove the block in front of repeater to depower the line. Since the comparator always powers after repeaters, the redstone line will always turn off after it turns on, creating a reliable 0-tick pulse. The advantage to this 0-tick generator is that it's 0-tick pulse is earlier in a tick relative to 0-tick pulses generated through other methods.

A 0-tick generator that uses budded pistons






Another common method of generating 0-tick pulses is to use budded pistons. As budded pistons only retract when updated, this can be used to control which order pistons move and therefore controlling the order in which a redstone line is powered then unpowered. One example is to have a redstone line that directly powers a sticky piston and bud-powers two other sticky pistons. The piston directly powered by the redstone line will have a block on its face, and the last piston in the chain will have a redstone block on its face. A second redstone line will be at the bottom which is the output; it will be powered by the piston with a redstone block and is cut off by the solid block. When the redstone line on top is powered, nothing will happen. But when the input is depowered, then a 0-tick pulse is created. The redstone line will depower, but only cause the piston that is directly powered to start retracting. This will uncut the output line, turning it on. When this piston retracts it will then update the piston in the middle, causing that one to retract which will then cause the last piston to start retracting, which will remove power from the line.


### Zero-tick chaining
Within a tick, 0-tick pulses happen , but 0-tick pulses can happen after other 0-tick pulses while still being in the same tick. This is known as 0-tick chaining where two or more 0-tick pulses are activated in a row.

0-tick chaining that relies on the fact that tileticks process before block events
One method of 0-tick chaining is to utilize the fact that tileticks such as repeaters and comparators will process in a tick before block events such as piston extensions and retractions. In the shown example, when the input is powered, the quartz block will be 0-ticked by both pistons causing it to instantly move two blocks, ending up above the diamond block. The 0-tick generator to the right makes use of tileticks and will activate before the 0-tick generator on the left, which uses block events. This method of chaining is very compact, but it comes at a downside that this method can only be used once per chain.


0-tick chaining that uses a long update chain before the second 0-tick generator
Another method of chaining is to utilize the fact that update chains can be used to manipulate the order in which things are processed in a tick. In the shown example, there are two 0-tick generators. The one on the left has an update chain before powering it, while the one on the right is directly powered. When the input is depowered, the 0-tick generator on the right will activate first as it is directly powered causing its output piston to instantly drop its block. While this is happening, the update chain is retracting. Then, the 0-tick generator on the left will will activate causing its output piston to instantly drop its block.


