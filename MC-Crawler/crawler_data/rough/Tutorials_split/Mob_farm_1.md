## Designs
When planning a mob farm, one should consider the size of the spawnable area. The maximum spawnable area depends on where one plans to be in relation to the farm. If you plan to be directly beneath the center of the farm, waiting for the items, then the radius in which mobs can spawn can be used to calculate the maximum size of the spawnable area: 

floor( sqrt(Spawn Radius^2 - (Spawn Floor Height - Collection Floor Height)^2 )) = Spawnable Area

In Java Edition the spawn radius is 128 blocks. In Bedrock Edition the spawn radius is roughly 96 blocks for simulation distances > 4. For simulation distance 4 in Bedrock Edition the spawn radius is 44 blocks.

In practice, however, it is rarely worthwhile to fill the maximum spawnable area with a single farm that delivers mobs to central location. For example, if you plan to spend your time in a less defined position, it might be easier to repeat a simple design several times, ensuring that at least some areas are in the spawn range while limiting complexity. Moreover, transporting mobs long distances for killing makes a farm less efficient because of caps that limit spawning based on the number of mobs already in the loaded areas around the player. The impact of caps is especially important in Bedrock Edition, which has caps that limit population densities as well as a global cap that counts mobs around every player loaded in the world.

If you are making a room that relies on darkness to spawn mobs, cave sounds and bats are good signs that your spawner is dark enough to let hostile mobs spawn.

### Spawning tower
One of the most popular overworld designs for a general mob farm is based on a tower of spawning pads that are periodically flushed with water to push the mobs off so that they die from fall damage.  The water comes from a central pillar of dispensers and observers that cascade a clock signal between platforms.  This type of farm is known for its high production rates, simplicity, reliability, and ease of build.




Starting in 1.19.3, mobs no longer spawn on scaffolding.  In this case, just build the spawning platforms with top slabs instead of scaffolding. The central signal tower of observers, dispensers, scaffolding blocks remains the same.

#### Using observer blocks
The designs shown in the YouTube videos above are somewhat resource intensive, but this design requires only the following materials: 

- 1dispenser(per layer)
- 1water bucket(per layer)
- 1observer(per layer)
- 112opaqueblocks of choice (per layer)
- 1clock(e.g. an Ethonian hopper clock: 2hoppers, 2sticky pistons, 2comparators)
- A capture layer (just several dozenhoppersleading into a chest)

In addition to being inexpensive, it is also easier to build. 

The design uses three different layers that are repeated with a redstone clock added to the top layer.
The layers are as follows:

1. Top layer: Anobserverblock, facingupobserving the dispenser it; the rest of this layer is air.
2. Middle layer: This layer is completely air (once the dispenser is triggered, it becomes filled withwatertaking the block above the dispenser at its center).
3. Bottom layer: Thedispenser(facingup, surrounded by opaque blocks (e.g. cobblestone) to hold thewater. Fill the dispensers are filled with a bucket of water.

For layer one, the blocks must hold all of the water, so go out seven blocks in each direction, then fill in diagonally.
Optionally, you can surround these blocks with signs to prevent spiders from climbing up. However, this would be a large amount of work for little benefit.

This mechanism can cascade downward through quasi-connectivity. When the top dispenser is triggered the observer see the state change and signals down to the air gap above the dispenser below, activating it through quasi-connectivity.

This cascades down through all of the layers (make as many as you like, but anywhere between 3 and 10 should be plenty).
To start this cascade, the topmost dispenser needs to be activated. It is recommended to do so using an Ethonian hopper clock with about ten items in it. You can trigger the topmost observer using the redstone output from one of the emplacement the redstone block could be in the clock.
It is also recommended to make the layer on which you place the clock bigger than the other the hide the layers under from the sun, and to place torchs on it to prevent mob spawn.

### Sinkhole
The easiest possible design consists of a large, empty area of simple shape, with one or more holes in the ground for the mobs to drop through. The edge of each hole has to be lined with opened trapdoors or gates to trick the Mob AI into believing the hole to be solid ground. Trapdoors can also be controlled with redstone, so one could shut off the farm by closing the holes remotely.

The whole room is closed by a roof to create a minimal light level. A roof height of 3 allows Endermen to spawn, while a roof height of 1 would restrict the farm to spiders.

Sinkhole farms have limited effectiveness, as the chance for a mob to wander into a hole is small, and zero when the player is so far away that the mobs freeze.‌[Java Edition  only] But they can be built quickly and cheaply, and works in the Nether (unlike other designs requiring water because you can't place water in the Nether).

### Canal-style
Example layout of a 38x38 Canal-style farm
To improve the chances of a mob falling into the holes, one can add channels filled with flowing water, leading to the central hole. The channels are lined with open trapdoors to trick the mobs into falling in, and the water transports them into the grinders. Such a design requires a bit of planning to ensure that there is no stationary water in which the mobs might get stuck, reducing effectiveness.

Because the system uses water to transport mobs, it cannot capture Endermen, which teleport away when touching water. Therefore, the roof of the cavern should be 2 blocks above the ground to prevent griefing of your farm by Endermen taking blocks.

