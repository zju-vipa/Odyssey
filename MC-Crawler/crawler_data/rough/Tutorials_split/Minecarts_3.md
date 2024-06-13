### Usage of detector rails
Main article: Detector Rail
A detector rail can power 4 adjacent blocks and 2 blocks below it when a minecart, occupied or empty, is on it. This makes it possible to activate powered rails inline without redstone torches or wiring. 

A detector can be used to activate adjacent powered rails. However, if the detector is used to activate more than two or three (depending on approach speed) powered rails, the rails deactivate before the minecart reaches them, bringing the cart to an immediate stop.

One-way powered rail lines can be created by placing a detector rail before a powered rail. This way, occupied carts are boosted only if they are traveling the proper direction. Carts going the "wrong" way come to a stop because the powered rail is inactive.

Although inefficient, A two-way rail line can be created by placing detector rails on either side of the powered rail.

Alternately, placing powered and detector rails on a 1×1 slope does not propel a cart more than 3 blocks upward if there is not enough initial momentum.  The cart loses too much speed on the incline, meaning it can't make it from the detector rail to the powered rail before the powered rail returns to the "off" state.  If the cart is in a train of two or more carts, the last cart in the train becomes stuck instead.

A detector rail could also be used to activate an event based on a cart's location. For example, a fail-safe can be created to release a stopped cart in order to prevent a collision with an arriving cart.  The arriving cart passes over a detector rail, activating a powered rail that boosts the resting cart away.

### Additional properties
Powered rails do not curve like other rails.
Curved power rails exist in only the case where the final direction is toward the east (with the powered rail appearing in the north-south orientation), or in a T-junction where one path faces east along a north/south track.[4][5] It is possible to make a one-way curved railway using power rails, but not a bi-directional one.

When placing rails, regular rails prefer to curve toward the powered rail. In cases such as these, the south-west rule applies.

A cart reverses direction when it collides with an object (wall, single block, player, other carts) while traveling on a powered rail. It does not reverse direction if it collides with a translucent block, such as stone slabs or glass. If a track including powered rails is bordered by blocks acting as "buffers", the cart continues back and forth along the track indefinitely. Having carts interact with each other on a short track designed this way can be used to chain multiple carts together as a "train". Once aligned, they all move together at relatively the same speed.  

How far the charge passes down adjacent rails is independent of the length of redstone wire. Even if the rails are connected to a redstone torch by 15 blocks of redstone dust, the 8 adjacent rails still receive power despite the fact that they should be out of range for the torch.

## Parts of a simple system
### Powered rail mechanisms
#### Stop points
It is possible to make points in your track where a cart is stopped and then jumpstarted again by player input. This can be useful for creating checkpoints to certain sites of interest in your world. This can be done by using two powered track pieces on a one-block incline, by having the first powered track piece going down, with the second powered track piece at the bottom and a button placed alongside the second powered track piece, so that the button is directly above the track.

An example of a stop point
When the cart comes to this point, it stops on the incline, allowing the cart to use gravity to start the boost when the button is pushed. Players can then either stay in the cart and carry on to the next stop, or leave the cart at the station for themselves/other players to use later.

A "two-way" stop can be made by combining two of the normal stops with a detector rail in between. This pauses a minecart traveling in either direction and allow them to be restarted by pressing a button. 

Two-way minecart stop
#### Starting boost
To create a simple initial boost device using 2 powered rails, dig a hole 1 block deep and 2 blocks long. Place the powered rails inside the trench, connect one end to the track that you wish the minecart to exit. Finally, place the minecart on the powered rail. Once power is applied to the rail, the minecart is boosted out.

When one end of a powered rail has a solid block placed next to it a stationary cart on it gets accelerated away from the block. There are two common ways to exploit this behavior:

- Unpowered rail at the start of a rail line with a non-transparent block next to it. Place a cart on it and apply a redstone signal to the block to launch the cart.
- Powered rail at the start of a rail line with a block flush to the ground next to it, and an upward-facing piston under the block. When a cart is placed on the track, a redstone signal to the piston raises the block and to provide the initial push to start the cart moving.

