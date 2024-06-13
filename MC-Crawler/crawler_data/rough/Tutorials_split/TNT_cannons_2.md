#### Converting signals
Sometimes signals can have unwanted side effects. This section is explaining, which signal type fits which purpose.

Double- & long activation

Double- and long activation often interfere with future events such as placing new TNT. They might also mess up T flip-flops and counting circuits.

To prevent this try to reduce all kinds of long activations (>four game ticks).
Common sources are: (observers detecting...) Buttons, pressure plates, repeaters, redstone lamps, pistons, string, TNT placement and ignition.
If there is no way around long or double activations, they can be reduced back to short pulses using rising edge monostable circuits.

Piston spitting

Piston spitting is sticky pistons pushing blocks but not pulling them back.

If this is unwanted it can be fixed by using signal lengths of more than two game ticks.

Update order

As a rule of thumb: The earlier a signal was created, the earlier it's update priority is. A 4 redstone tick repeater is processed before a comparator that activates that same tick, because it's signal was created 8 game ticks before that of the comparator (comparators create their signals in the same game tick as they get powered due to comparator priming). And the same can be said about the TNT that will be ignited by those components. The difference in update order is called event delay or ED.

Zero ticks

When a redstone pulse is terminated in the same tick, it is called a zero tick. It is equivalent to a one game tick pulse for some blocks and entities but is not processed by others at all. Some blocks such as sticky pistons and trapdoors get activated and deactivated with the pulse. This results in loads of useful properties. Some are:
Trapdoors that are activated with a zero tick pulse might let TNT pass but not players. Propellants might move only for a zero tick, after accelerated to destroy nearby blocks or phase through unloaded chunks.

#### Synchronization
The synchronization of cannons is explained above.

Since this is a brought topic, only some rules how to make the synchronization less complicated can be named:
It is best to let signals stay combined whenever possible. For example if you have an injector- and a projectile delay, let the projectile delay branch of off the injector delay. Now they can be adjusted simultaneously without changing the relative delay between projectile and injector. Or if two parts of the cannon undergo similar changes, it might be possible to perform those changes using the same component.
Parts acting in parallel can hide dangers. A common problem is, that one part is BUDed by the other. Those problems are usually easy to fix but hard to find, so it is important to know, what to look for.

### Moving TNT
Moving blocks

Moving TNT blocks comes with some unique problems. Many of them are caused by it being impossible to power the TNT / direct redstone signals through. But other, way more problematic problems come from the TNT often needing to move, while the player is using the cannon.

To prevent slow down of the loading in block streams, the pusher might use 0 ticks. Those allow continuous loading but come with some problems. If the TNT is pushed using a clock it will be unordered. 0 tick placement detectors on the other hand can get big and might not reset fast enough, especially during lag spikes.
Another way to reduce this slow down is by moving the player. Trapped between two flowerpots the player can quickly move left and right, placing TNT into two different pushers. This requires a lot of loading skill and is not applicable in most conventional cannon layouts though.
A similar effect is achieved by moving the TNT furthest away from the player first, so that it can already be loaded again - looking through the transparent parts of the piston head - while the TNT closer to the player are still pushed.

To prevent TNT blocks from being pushed into the TNT of previous shots (no matter if the latter is in block or entity, form this might cause problems) either those TNT have to be primed faster or they need to be moved somewhere else. Moving it somewhere else can increase cannon volume dramatically though if it is solved via multiple chambers so instead a better and more complicated solution is to store all the TNT and ignite them in one chamber.

Compression

Top: Trapdoors, that let TNT but not players passMiddle: CompressorBottom: Compressor and separator
Compression is the process of moving TNT to their launching position.

Gravity and pistons and / or flowing water are usually used to achieve the compression. To prevent the inaccuracies that come with the prime motion of TNT, it has to be pushed into a wall, so that the motion gets cancelled.

Separation

As the name suggests, separation refers to the process of separating TNT and keeping it separated.

TNT can be separated by it's position in the update order using pressure plates. If the TNT is moved onto the pressure plate it activates a trapdoor, that prevents other TNT from being moved there. To separate multiple TNT at once, the process might be repeated setups involving iron- or golden pressure plates can be used.

Usually the TNT are initially separated though. To keep the TNT less complicated and more compact methods can be used. Those include flaps (trapdoors or piston setups, that open for a moment to let a bunch of TNT pass, while the next batch lands on them) - which are most commonly used to separate multiple shots from each other - and setups, that push the TNT into multiple horizontally differing positions - often used to separate propellants and projectiles or in very fast Machine guns.

