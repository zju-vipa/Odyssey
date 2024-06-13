## Miscellaneous
### Combination locks
Main article: Tutorials/Combination locks
Combination locks are a type of redstone circuit. They generally have a number of components which must be set in the right combination in order to activate something such as a door. Combination locks can be very useful in creating adventure maps. Note that if you are playing in survival multiplayer, other players will still be able to break into the mechanism and cause it to activate without knowing the password.

### Sorting device
|  |  |  |  |  |  |  |
|--|--|--|--|--|--|--|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |

This is a device which sorts the inputs, putting 1s at the bottom and 0s at the top, in effect counting how many 1s and how many 0s there are.
It is designed so that it is easily expandable, as shown in the diagram. The 5×5 center square is tileable. The inputs are at the bottom and right and the outputs are at the top and left

Truth table for a three-bit sorting device:

| A | B | C | 1 | 2 | 3 |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 1 | 0 | 0 |
| 0 | 1 | 0 | 1 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 | 0 |
| 1 | 1 | 0 | 1 | 1 | 0 |
| 0 | 1 | 1 | 1 | 1 | 0 |
| 1 | 0 | 1 | 1 | 1 | 0 |
| 1 | 1 | 1 | 1 | 1 | 1 |


### Timer
Timers can detect the time difference between the first input and the second.




2





















1










A timer. The extra repeater at the bottom is to compensate for the delay of the upper repeaters.










































Example of a timer in action. This one determines the time difference between the input and output of a 2-tick repeater.

The amount of time can be determined by how far the signal travels. For example, if 5 of the locked repeaters are powered, it means the time difference was 0.4-0.5 seconds, ignoring lag. If the time difference is exactly 0.4 seconds, 4 repeaters will be powered.

The repeaters that will lock can be set to different delays. For example, if they are set to 4 ticks and the first 3 are active, it means the time difference was 0.8-1.2 seconds. You can even have a mix, which can be handy if you know what the range is likely to be. However, you will need to be careful when reading these timers.

If you are measuring higher scales, the second signal might not reach all of the repeaters. You will need repeaters to replenish the signal.

























A section of the timer that replenishes the signal. Since the upper repeater has a delay, another repeater is required in the lower section.

If the signals are short times (like if you are using observers), you may not have time to read the data. 











2



1
















An input modifier. When the inputs are applied, the timer will treat them as active until the button is pressed.

You can also measure how long a signal lasts.











































A timer that measures the duration of a stone button.

Please note the following when making a duration timer:

- Because of the delay that the redstone torch adds, the delay of the initial repeater, the one that stays unlocked, must be increased to 2 ticks.
- The data from the timer will be preserved.
- Because the repeaters will still be powered when the timer is used again, the circuit must be obstructed between uses in order to unlock the repeaters. To do this mine theredstone torch, wait for all of the repeaters to deactivate, and put the redstone torch back.

### Serial interface lock with D flip-flops


D flip-flop is an electronic component that allows you to change its output according to the clock. It's and RS NOR latch that sets its value to the D input when the ">" (clock) input is changing its state from low to high (in some cases from high to low). 

Basically, it's equivalent to the expression: "Set the output Q to the input D when the input C goes from 0 to 1".

For example, you can use D flip-flops to shift the value from left to right.



In this lock, the > signal propagates from the rightmost flip-flop to the leftmost, so the signal shifts to the right. This circuit allows you to input a 4-bit number with two levers. You can use any number of bits, but this configuration is already pretty secure even if someone figures out what a lock it is.

So, if you want to input the combination 1-0-1-0, follow these steps:

1. D = 1
2. > = 1
3. > = 0
4. D = 0
5. > = 1
6. > = 0
7. D = 1
8. > = 1
9. > = 0
10. D = 0
11. > = 1
12. > = 0

In theory, you can program the lock from this serial interface as well. Just attach 4 RS NOR latches and a hidden place for the programming levers.

This design is not very practical as a lock, but might be a nice feature on something like a puzzle challenge map.


