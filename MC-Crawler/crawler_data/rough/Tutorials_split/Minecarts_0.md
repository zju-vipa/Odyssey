# Tutorials/Minecarts
This tutorial covers basic minecart stations and systems and is designed for those without significant redstone knowledge and only minor experience with minecarts and rails. This tutorial doesn't touch on furnace or storage minecarts. Images below do not always show a space-saving design, but rather one that makes all components immediately visible.

## Contents
- 1 Absolute basics
	- 1.1 Minecarts
	- 1.2 Rails
- 2 Best practices for laying tracks
- 3 Powered rails
	- 3.1 Behavior
	- 3.2 Powering
		- 3.2.1 Momentum
	- 3.3 Climbing slopes
	- 3.4 Optimal use
	- 3.5 Usage of detector rails
	- 3.6 Additional properties
- 4 Parts of a simple system
	- 4.1 Powered rail mechanisms
		- 4.1.1 Stop points
		- 4.1.2 Starting boost
		- 4.1.3 "Whirligig" cyclical minecart accelerator
	- 4.2 Launcher
	- 4.3 Rider detection
		- 4.3.1 Empty carts
	- 4.4 Boosters
	- 4.5 Junction
	- 4.6 Multiple destination selector
	- 4.7 Piston bolt
- 5 Troubleshooting
- 6 See also
- 7 References

## Absolute basics
### Minecarts
The following are the most important properties of minecarts.

- Minecarts move at 8 m/s at top speed on a straight track. On a diagonal track they move at 11.314 m/s = sqrt(2) * 8.
- Minecarts move differently depending on their load.
	- A minecart with a player inside travels 309m from full speed, staying at full speed for 176m.
	- A fully loadedhopperorchest minecarttravels 40m from full speed.
	- An empty hopper or chest minecart travels 165m from full speed.
	- A chest minecart carrying 320 items (5 stacks) travels 101m from full speed.
- Activatedpowered rails, down slopes, and being pushed by players or mobs add momentum to a cart, increasing its speed.
	- A minecart with a player inside goes from stationary to full speed after about 13m of powered rail.
- A player riding in a cart may add momentum by "pushing" it using theforwardcontrol.
- A stretch of an unactivated powered rail of at least two blocks length brings a loaded cart at full speed to a complete halt.
- A long stretch of rail or an up-slope reduces a cart's momentum and thus its speed, eventually stopping it unless the forward key is held throughout by a player riding the cart.
- Minecarts "bounce" off of obstructions on the track. Running into a player, mob, or a stopped cart causes it to reverse direction, even on a powered track.

### Rails
Please see the individual pages for each type of rail for information on their properties and basic usage:

- Railsalways have to sit on another solid block and are the only rail type that can curve.
- Detector railsgive off a redstone signal when a cart passes over them, otherwise they act as a regular rail.
- Powered railsadd momentum to a cart passing over them when powered, when unpowered they have a braking action and slow or even stop a cart.
- Activator railstrigger an action on a cart passing above them when powered: TNT minecarts are set off, a hopper cart gets deactivated, and players/mobs riding in one are pushed out of it.

The rest of this page discusses the use of these components in building tracks and rail transport systems.

## Best practices for laying tracks
The performance of a rail line is affected by the way the track is placed. Turning next to a wall (see below) or having hills to climb adversely affect the speed of a cart, and so its distance traveled.


Some YouTube videos suggested that diagonal track might offer better performance than straight runs, this has not been proven to be the case. Another distance trial track was constructed with a length of 300 blocks. Carts with no rider travel the same distance as on the straight track, about 18 blocks before they stop, and a cart with a player riding can make it to the end of the track. The interaction with blocks next to the track seems to be a little stronger with carts on a diagonal track. With lampposts placed only every 10 blocks along the track an unmanned cart could cover only 12 blocks, and with a player riding just over 180 blocks, a significant reduction.

What the tests have confirmed is the increase in speed. On each curved track, a cart effectively moves 2 blocks, thus its maximum speed is 11.314 m/s, an improvement over the maximum of  8 m/s on a straight track.


A minecart with no rider, at full speed, can climb 10 blocks on unpowered, upward sloping rail. This suggests that powered track is needed at this height only to keep a cart climbing. However, the cart slows so much that it can reach only another 5 blocks high with 2 lengths of powered track starting at 9 blocks high. Further testing showed the minimum number of powered blocks to keep the cart climbing well is 3 powered rails every 6 blocks starting at 9 blocks high, at the cost of a strong reduction in speed. To maintain speed in a climb, a ratio of 5:4, powered versus regular rail segments, is a good compromise for decent speed at a reasonable cost, starting with 2 powered rails on the flat before the upward slope to be sure the cart starts the climb at maximum speed.

If construction cost is no object one can of course use powered rails all the way to the top to get the best possible performance.

Carts with a rider, or chest carts, have more momentum and so climb higher than one that is unloaded. With a rider, a cart can climb at least 24 blocks before needed powered rails to go higher.

Running a track next to a wall makes no difference to the speed of progress, but an adjacent one-block-high wall significantly slows down a cart if the cart is pointed at the wall while entering a turn or "diagonal" section.

