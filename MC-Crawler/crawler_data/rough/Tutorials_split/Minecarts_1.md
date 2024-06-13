## Powered rails
### Behavior
Powered rails may be activated by redstone to turn them "on" which makes them able to add momentum to carts already moving over them. When unpowered they are "off" and strongly reduce the momentum of a cart passing over them.

Note that a minecart placed on an active powered rail cannot move as it has no motion for the powered rail to add to. Once the cart is pushed, its rider uses a forward or backward move, or a block placed at one of its ends, the cart's direction of motion is set and the powered rail can affect it.

If a cart is placed on an inactive powered rail that is sloped the braking effect is strong enough to keep it stationary against "gravity". if the powered rail is then turned on gravity is enough to start the cart rolling downhill, which then causes the rail to affect the cart's momentum. 

A rail that is "off" slows carts passing over it as if by friction. A single inactive rail is enough to completely halt a cart in most cases. Carts that are loaded and/or at full speed cannot be stopped by just one block, but two "off" rails can stop it. On a long downslope, a stretch of three inactive rails are required to be sure of halting a speeding, loaded cart.

### Powering
Power can be transmitted to the rail from any of the six adjacent positions (above, below, or any side) in the same way redstone is powered.

Powered rails propagate power to each other if they are adjacent and part of the same track, for up to 9 blocks from the power source (1 being powered directly which is propagated to 8 adjacent rails). They also receive power from any adjacent detector rails (when a cart passes over it), even if they are not part of the same track (which follows from the rules above).
Because the detector rail powers attached rails, it could be used to activate power rails only when necessary:

- For one-way travel, place a detector rail before the powered rail
- For two-way travel, place a detector rail on both sides of the powered rail

In practice, it is far more efficient to have powered rails constantly active using other means:

- Place aredstone torcheither next to the powered rail or two blocks underneath it or use poweredredstonewiring to achieve the same effect
- Place an activatedleveron the bottom side of the block the powered rail is on (cheapest, requires only a stick and a cobblestone to make)
- Place the powered rail on ablock of redstone

#### Momentum
The speed of a cart which is boosted using Powered Rails is calculated to be at the maximum of 8 m/s, however, the cart maintains an internal "momentum" value that keeps the cart at the maximum speed of 8 m/s until the excess momentum is depleted.

A single powered rail on the flat ground against a stop block gives an occupied cart enough momentum to travel 80 rail tiles on a flat surface, or 8 tiles for an unoccupied cart. Tests show that putting several powered rails in a row has observable diminishing returns with each additional powered rail on how much farther a cart travels.[1] This implies that the momentum gained is smaller if the cart's speed is faster and vice versa.

Tests show that climbing slopes impact momentum severely, thus the cart speed plummets fast. However, if there is enough surplus momentum, carts easily travel up slopes. Conversely, carts traveling down slopes gain momentum. Downward sloped powered rails add both the momentum from the rails and the momentum from going downhill to your cart.

### Climbing slopes
6 blocks up without additional boosting in Beta 1.5, 10 in Beta 1.6
Launching from rest via four powered rails, an occupied cart has enough momentum to climb a 1/1 slope 10 blocks high without further boosting and then travel horizontally at a very slow speed for at least a dozen blocks before coming to a stop. Such a cart does not have enough momentum to climb an 11 block high slope. An empty cart in a similar setup can climb only 5 blocks and then travel a few blocks horizontally.

When minecarts travel upslope without having sufficient stored momentum, a powered rail is needed 1 every 4 blocks to sustain movement all the way to the top of the slope, Alternatively, 2 every 8 blocks are somewhat easier to supply power to (note that this doesn't seem to be working as of patch 1.14.4, and may require additional testing) However, note this is a worst-case scenario where there is no momentum to start with.

If working with empty carts (for instance, a storage cart transport system), 1 powered every 2 blocks is necessary to sustain the movement. To minimize powering requirements, 2 powered followed by 2 unpowered can also be used (analogous to loaded player-carrying carts). 

When traveling up a slope at full speed (8 m/s) one powered rail is sufficient to maintain full speed for two blocks high, meaning that alternating between powered and unpowered rails maintains full speed up a slope.  Consecutive powered rails on a slope adds more momentum, so eight powered rails can be followed by 8 normal rails to maintain full speed while traveling up the slope.  Less momentum is gained by each consecutive rail as the strip gets longer.

