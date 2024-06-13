# Tutorials/Horses
This tutorial describes how to measure horse attributes and breed them.

## Contents
- 1 Measuring
	- 1.1 Health
	- 1.2 Jump Strength
	- 1.3 Speed
- 2 Breeding difficulty
	- 2.1 Optimal Breeding Scheme

## Measuring
### Health
The health can be determined by looking at the heads-up display (HUD.) The saddle icons replacing your hunger bar while riding a horse is the horse’s health bar. One heart equals two health points. When you ride a horse that has an odd number of health points, the last health point isn’t shown on the HUD.  Sometimes, horses have an odd number of health points; one method you can check if the horse has an even or odd number of health points/hitpoints is by hitting the horse and mounting the horse to check the hitpoints. If the HUD shows one less health point lost in health than the attack damage to the player, after the player attacks it, either with or without tools, the horse has 1 more health point than shown in the HUD and thus has an odd number of health points. If the HUD shows the exact amount lost in health than the total attack damage to the player after the player attacks it, the horse has an even number of health and it has exactly the number of health points/hitpoints as shown in the HUD. The horse might regenerate one health point right after you attack it, so you might want to try again. Heal the horse to full health and attack it again to check again if you’re correct in checking if the horse has an odd or even number of hitpoints. For example, if a horse appears to have 22 hitpoints and you attack it, if the horse has lost one fewer health point than the damage you inflicted to the horse, and if the horse didn’t regenerate, then it means that the horse actually has 23 hitpoints.

### Jump Strength
The internal value for jump strength for horses ranges from 0.4 to 1.0, which turns out to be approximately 1.11 to 5.3 blocks. A device to measure this can be quite simple: build walls of increasing heights parallel to each other, 3 blocks apart. To test horse jump strength, simply jump over the shortest wall to arrive at the next wall, and continue jumping until you can no longer jump. The last wall you were able to jump over indicates your horses maximum jump strength. Slabs and snow layers can be used to create non-full block increments.

| Internal units | 0.4            | 0.5    | 0.6    | 0.7    | 0.8    | 0.9    | 1.0     | player |
|----------------|----------------|--------|--------|--------|--------|--------|---------|--------|
| blocks         | 1.1093[note 1] | 1.6248 | 2.2216 | 2.8933 | 3.6339 | 4.4379 | 5.29997 | 1.2522 |

1. ↑Horses with very low jump strengths can inconsistently clip onto platforms up to 1 7⁄32 blocks tall (jumping from snow layers to lily pads or chains), despite not reaching that height.

### Speed
Speed proves to be the most difficult attribute to measure. The internal value for horses ranges from .1125 to .3375. A device to measure this can be constructed with the delay on repeaters, using repeater locking. Create a very long chain of repeaters. 

Use a piston to hold back the horse. Connect redstone such that the piston releases the horse at the same time as a pulse starts down the repeater chain. At the end of a certain amount of blocks (~45 or so), add pressure plates, which are usually more consistent than tripwire. When these pressure plates are activated, use a long string of redstone to lock every repeater in the chain. This will "freeze" the chain and the pulse that started at the beginning will be frozen in place. You can mark the repeater where the pulse is frozen with a block. 

Keep in mind that you may need repeaters to lengthen the signal enough to lock the entire repeater chain, which will introduce a delay. You can account for this delay by adjusting the delay of the repeaters used for locking. As long as all the repeaters lock at the exact same time, the device will work. 

Also keep in mind that for the results to be consistent, you must be going perfectly straight every time. You can do this by opening F3 mode and looking at the "facing" label, which shows a numerical value for your camera angle. You can temporarily decrease your mouse sensitivity through the controls to align yourself perfectly. 

This device cannot measure the horse's exact speed in blocks/second, but can accurately measure its speed relative to other horses. Aside from server lag, it is incredibly consistent and can be used for accurate comparisons.

To convert a horse's internal speed to blocks/seconds, multiply the internal value by 42.16. This differs from the usual conversion of 43.17 blocks/sec, because horses do not move at their full internal speed.

| Internal units | 0.1125 (min) | 0.16875 | 0.2250 (avg) | 0.28125 | 0.3375 (max) |
|----------------|--------------|---------|--------------|---------|--------------|
| blocks/s       | 4.74         | 7.11    | 9.49         | 12.86   | 14.23        |

