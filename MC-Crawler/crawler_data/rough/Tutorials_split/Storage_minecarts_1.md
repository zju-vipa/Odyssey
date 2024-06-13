### 
Starting with 1.19, minecarts with hopper or chest no longer separate into the minecart and the hopper or chest items when broken, but still spill out their content like a hopper or chest would. This allows for instant minecart unloading with the option of subsequent reuse of the container minecart without player intervention. By carefully choosing the position where the minecart breaks, it is possible to separate the minecart item from the minecart's content and quickly redeploy it using a dispenser.

| First showcase of instant unloading on Java Edition by Inspector Talon (view on YouTube) |
|------------------------------------------------------------------------------------------|
|                                                                                          |

The general setup for an instant minecart unloader requires a method for aligning the minecart, a damage source that breaks the minecart, and two separate ways to collect the minecart item and the spilled content. On Java Edition the most common alignment method is running the minecart into a stair block and letting it snap down onto a straight rail, through that stair. The damage source is typically a lava cauldron and the minecart item is collected by a hopper directly under the cauldron, while the content is flushed into a collection mechanism using a water stream. Since there is no water in the nether, instant unloaders use sticky pistons to move the snapping rail and the block it rests on out of the way to the items can drop into a collection mechanism, but this approach is not 1-wide tileable. On Bedrock Edition the minecart mechanics are slightly different, so the alignment usually use a curved rail, while the damage source varies between different options like lava, soul fire or a cactus. Collection of the minecart item uses either a water stream or hopper, while the content is again flushed into a collection mechanism using a water stream. Due to the required layout, instant unloaders are not easily tileable on Bedrock Edition.

















































A compact, 1-wide tileable instant unloader for Java Edition. Scaffolding rests on waterlogged mangrove roots, the cauldron contains lava.
This example of an instant unloader for Java Edition is 1-wide tileable and uses water mechanics to send the dispensed minecart up the slanted powered rail instead of down. Even though the water in the rail is blocked by the scaffolding, there is water in the mangrove roots block below, which causes the water in the rail to push towards the roots. Incoming minecarts need enough momentum to collide with the vertical part in the center of the stair block. The minecart will then snap down onto the straight rail (using inactive powered rails is recommended here), which makes it clip into the lava cauldron and break in a way that the minecart item spawns overlapping the hopper's collection area. Any content of the minecart spawns outside the cauldron over the snapping rail and can be transported by either waterlogging the rail or periodically pulling out the rail and its supporting block using sticky pistons. Note that pulling the rail makes this no longer tileable, as the rail would change its direction and cause the minecart to snap away from the cauldron, where it won't break.

Note that this unloader uses quasi-connectivity to operate the dispenser. When the minecart passes over the detector rail, the observer sends a signal downwards that activates the dispenser twice, once when the minecart touches the rail, and again half a second later when the rail deactivates, which dispenses the minecart again. To prevent the minecart from being dispensed, a permanent redstone signal should be applied to the mangrove roots block. The dispenser should not be powered directly, as this would lock the hopper and potentially destroy the minecart item or send it into the item collection area. To dispense the minecart again after stopping the unloader, a separate redstone pulse must be applied, which can be achieved e.g. using a falling edge detector in the redstone circuit that also applies the signal to stop the unloader.



