### Increasing efficiency
Increasing accuracy

Very high accuracy can be achieved by rebounding the TNT or shooting straight forward, because this reduces the alignment complexity by one axis. On the other hand direction changes in mid-air usually decrease accuracy.

Pixel precision:


Pushing TNT into Blocks with different width/ letting it fall onto blocks with different height aligns the TNT against those Blocks. This technique results in a precision of 1 pixel which is equivalent 1⁄16th of a block (or half a pixel/1⁄32th of a block for chains and lily pads). If TNT are pushed into the same hit box from the same direction they will usually have the same position in that axis.

Subpixel precision:

TNT with alignment differing in the subpixel precision.
Since TNT is only 0.98 blocks wide it makes a difference, from which direction it is pushed into a block. This can be used to achieve 0.02 block differences in alignment. If the TNT is not pushed against a block it is placed into the middle of the pixel which allows for 0.01 block differences in alignment.

Using errors in Java's floating point calculations alignments (for example pushing TNT from different directions) with approximately e-9 differences in alignment are possible.

TNT can be pushed into boats, which can be aligned anywhere to a precision of about e-11 using minecarts. This method is more complicated and less compact, than the other methods (since boats can be damaged multiple times in one tick, which forces them to be at least 8 blocks away from the propellants in reusable cannons). But it allows almost unmatched precision anywhere.

Motion alignment:

Using the motion of TNT any alignment can be achieved. Precise alignments can be hard to figure out properly though since most motion types are either too slow for TNT or to inconsistent and need to be canceled. Some motion types with notable consistency include water streams, bubble columns and TNT falling through powdered snow. They are especially useful since changing the delay for which TNT is exposed to them results in consistent position changes.

Propulsion and velocity

Some cannons use other methods than TNT (ie. slime blocks, water...) to accelerate TNT but this section is about propulsion from TNT explosions.

In general the following rules apply:

Propulsion is increased by adding propellants and reducing the distance between the propellant's explosion centre and the TNT's position (for many other entities the eyes are used instead of the position). Disregarding some exploits that involve the world's origin the maximum acceleration per propellant is one block per tick.

Propulsion is decreased, if the projectiles rebound, when different propellants cancel each other's motion, when exposure sample rays are obstructed, or when propellants slide on the ground.

Using every projectile

It is worth looking out for which projectiles can be removed and where other projectiles can be added. More projectiles often lead to a worse cannon. Scatter cannons and statics are known to be quite inefficient.

### Lag reduction
Lag reduction can be important in some cannons. For that it is advisable to shoot as straight as possible or use modifications, that improve entity motion performance. Apart from that all the rules that apply for other redstone contraptions also apply here.

Lazy acceleration

Lazy chunks only tick blocks and not entities. If the projectiles lay inside lazy chunks, they can accumulate acceleration given by propellants that explode outside lazy chunks. This allows for cannons to be charged way longer than four seconds, so that only a few hundred TNT are loaded at any time (except for the few ticks, where the cannon is shooting). Thus lag is reduced and cannons are also more compact. Chunk loading will break lazy cannons, if no safety mechanisms are implemented.

## Armor and Shielding
### Armor
It is generally best to use the highest blast resistance allowed. It is preferable to use blocks that have no hit box but some blast resistance (such as fence gates) over air.

Anti Mortar armor (without causing armor gaps).
Anti Mortar

By alternating slabs and walls vertically mortars with a prime phase intervals of one game tick can be stopped without it taking any armor away (compared to other blocks with the same blast resistance). Slabs and other blocks that are less than a block high can also help against shots that aren't fully compressed. Blocks that slow entities such as cobweb can be used to further increase the time it takes the Mortar to settle down, costing it even more delay.

Invisible

Some blocks can be invisible such as some block entities and walls (for invisible walls use the debug stick to remove all sides and set the Up-State to false).

Those blocks will still serve as armor (though TNT can pass through some of them) but they might be unexpected and can even hurt cannons.

Unmovable armor

It is generally slightly preferable to use unmovable armor so that flying machines cannot push it around.

Alternatives
Honey, powdered snow and cobweb can slow the TNT down. This can be useful at times but those blocks often get destroyed before they can be effective.

TNT resistant


Cannon resistant

Some blocks cannot be destroyed or bypassed by cannons (when they don't use exploits). Those include all blocks that cannot be replaced or moved and have a blast resistance above 9. Those blocks are usually not permitted or nerfed in fights because it is boring to shoot at something without progress.

Water

Even though water can't be destroyed by TNT it can be replaced with sand and sand can be destroyed with TNT so sometimes it is still allowed as armor. Water also is often allowed for sole use at launch points.

Cobblestone generators

Cobblestone generators might be considered a form of active shielding. Apart from that not much is to say about them except that they are a better version of water shielding.

Netherite

Netherite and its derivatives are indestructible for cannons. Though if it is moved, it is replaced with Block 36 (which is destructible by TNT) for a brief amount of time. 

