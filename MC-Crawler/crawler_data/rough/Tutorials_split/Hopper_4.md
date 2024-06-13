#### Alternate version



























































Special item filter

(back layer)





A









































B

C









Special item filter

(front layer)2-wide, item-safetransfer rate: 2.5 ips
This hopper-speed version does not require an additional step to slow down the input stream. It comes from a video by ilmango about potion sorting. Inputs and outputs work the same way as in the 1-wide design. The input stream is fed into a dropper facing the brewing stand or shulker box, while a comparator circuit triggers the dropper and the locking and unlocking of hoppers.


## Hopper clocks
Main article: Clock circuit § Hopper clocks

























Delayed hopper clock
flat, silentclock period: 40 ticks to 256 seconds 

Five stacks of items are in the leftmost hopper.

















Looped hopper clock
flat, silentclock output: 4 ticks on, 12 ticks offclock period: 16 ticks

1 item is in one of the hoppers.
Hoppers are commonly used to create clocks and delay circuits. Since items can travel back and forth between two hoppers, this is an easy way to make a clock. It is more iron intensive, however.

The looped hopper clock works by having an item traveling in a "loop" between the four hoppers. Whenever the comparator detects the item in a hopper, it turns on. This clock can be adjusted by adding or removing hoppers and items.

The delayed hopper clock works by taking turns completely emptying each hopper. When the hopper on the left completely empties, the redstone torch turns on and the other hopper begins emptying. Note that exactly 5 stacks of items must be used with this design. To decrease the clock speed, use fewer stackable items. "Delayed hopper clock origin"


## Item counter























































Item counter 

1-widetransfer rate: 1.25 ipssize: 1×5×4
This is a mechanism that outputs a short redstone signal for every item that goes through the dropper. The mechanism slows down the items moving through the dropper and the hopper above to make the outputs comfortable to use for counting mechanisms.

The output of this counter can be used in combination with a counting mechanism such as the scoreboard command in a command block.



