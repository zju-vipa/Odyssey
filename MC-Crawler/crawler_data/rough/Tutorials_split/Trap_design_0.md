# Tutorials/Trap design
Traps deal damage to the target without the assistance of the player. Not all traps are hidden and visible traps can induce a sense of safety in the target before they trigger the main one. In the following, the target is either the player or a mob, and not all traps are equally effective against them.

## Contents
- 1 Video
- 2 Trap Parts
	- 2.1 Trigger
	- 2.2 Complications
	- 2.3 Method
- 3 Using the Terminology
- 4 Safety
- 5 Disarming Traps
- 6 Mob grinder

## Trap Parts
There are three or four parts that can be seen in most traps:

- Trigger. The trigger is what starts the trap. It tends to be triggered by the target.
- Complication. These make the trap more efficient, but are not strictly necessary.
- Method. The method is the way the target is dispatched. The method is how the damage is dealt.
- Bait. This is usually how you lure players in. This can be, for example, valuable objects, or it can be something highly visible, like black wool in the desert. This can be added to your trap or incorporate a small modification to a building being trapped.

### Trigger
A trigger is what activates the trap. Triggers tend to use redstone, but analog triggers are also possible (water breaking torches, for example). Triggers can be effective if hidden in plain sight. This can be a button beside a door, or a pressure plate infront of a door which triggers more than expected.

- Pressure platessend a trigger whenever a player or mob steps on it and the signal is turned off when the player moves. A pressure plate can be attached to an RS NOR latch to stabilize the signal. Hiding a pressure plate can be done by keeping a low light level in the area and placing the pressure plate in the path of any player going through that area.

- Buttonscreates a short pulse and can be attached to an RS NOR latch or T flip-flop to stabilize the signal. If a button is used as a trigger, the target must be tricked into believing the button does another task (such as open a door or toggle lights).

- If a block is mined with aredstone torchon it (the torch being out of sight), the destroyed torch can be used as a trigger. The trick is to have the target mine the block on their own free will, which can be done by using a valuable or rare block such as diamond or gold.

- Watercurrents can be updated by an adjacent block update. This can be seen when redstone redirects water but also works with doors activated byhandandfurnaces. The updated water flow would then knock out a redstone torch, creating the signal.

- ABUD switchcan be used to trigger a trap if a door, or chest is opened. They can also detect other block state changes

- Some players have experimented with the ability to pick up an item through a corner. The item is placed on a wooden pressure plate, the deactivation of which creates a signal. The item will disappear after 5 minutes, so the trap is unstable without a pre-trigger complications, but this can be avoided by redispensing it. This trigger also assumes the target has room in their inventory for the item being used. Arrows tend to be used because many players carry arrows and probably wouldn't notice an extra. This trigger is much more hidden than others, almost any corner can be a trigger. A tutorial video explaining this type of trigger is shown below.




### Complications
A complication is any part between the trap triggering and the method being employed. Many more complications exist than just those below. Complications tend to add a delay to the trap, which is usually not desirable.

- A redstone clock can be used to generate periodic pulses. This is almost always used with arrow dispensers or a trap that is triggered periodically such as a piston grinder.

- RS NOR latch / T flip-flop. These circuits take a short pulse and stabilize it. An RS NOR latch uses two inputs, one to set the signal, and another to reset it. The reset switch would be away from the target. A T flip-flop uses only one input which toggles the signal. This is less common in traps than an RS NOR latch because the target could have a chance to reset the trap before they are killed.

- False walls (pistons/gravity). False walls hide important parts. This is a complication in that it does not deal damage, but hides the method, thus giving the target a false sense of security. Pistons can easily place and replace false walls, but redstone wiring can be difficult to hide in an open area. Sand and gravel can be used as an airlock to reveal important parts by using water to knock down the supporting torch, but this requires manual reseting every time the trap is triggered.

- A hole can be considered a complication because it forces the target into a smaller area rather than deal the killing damage. For the sake of this tutorial, a hole is a non-fatal fall, and a pit is a fatal fall. Like a pit, the target is often pushed into it.

- Water has limited pushing power which can be effective if the target doesn't react, such as with mobs. These are very common in mob farms as canals, but are almost entirely ineffective when used to transport players.

