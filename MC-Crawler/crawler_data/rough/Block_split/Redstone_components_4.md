###  Activator rail
Main article: Activator Rail
An activator rail is used to activate a minecart.

** Placement **
An activator rail can be attached to thetopof anyopaqueblock, or to thetopof an upside-downslabor upside-downstairs. If the attachment block is removed, the activator rail drops as an item.
When placed, an activator rail configures itself to line up with adjacent rails, activator rails, powered rails, and detector rails, as well as such adjacent rails one block above. If there are two such adjacent rails not on opposite sides, or three or more such adjacent rails, an activator rail lines up in the east-west direction. If there are no such adjacent rails, an activator rail lines up in the north-south direction. An activator rail slopes upward to match with a rail above it (when there is more than one such rail, the order of preference is: west, east, south, and north). Other configurations can be created by placing and removing various rails.
** Activation **
In addition to the methods above, an activator rail can also be activated by an activator rail adjacent to it that is activated. Activator rail can transmit activation up to 9 rails (the first originally-activated activator rail, and up to eight additional activator rails). Activation transmitted in this way can power only activator rails.
** Effect **
An activator rail affects certain minecarts passing over it. The effects vary with the type of minecart activated:
- Aminecart with command blockexecutes its command every 2 redstone ticks (5 times per second).
- Aminecart with hopperis deactivated by an activated activator rail (it stops sucking up items in its path, or transferring items to containers as it passes them), and re-activated by an unactivated activator rail.
- Aminecart with TNTis ignited by an active activator rail.
- Regular minecarts with an entity riding it (mob or player) eject that entity if the activator rail is active.
- Other minecarts are not affected by an activator rail.

###  Bell
Main article: Bell
Bells can be rung using a redstone signal.

###  Dispenser
Main article: Dispenser
A dispenser is used to automatically affect the environment by throwing items.

** Activation **
SeeQuasi-Connectivityabove.
** Effect **
When activated, a dispenser ejects one item. If multiple slots are occupied by items, a random item is ejected.
The effects of being activated vary with ejected item:

Dispenser Behavior


Item

Effect


ArmorElytraHeads
Shield


Equips on a player within a one-block distance (any armor, made from any material)


ArrowBottle o' EnchantingEggFire ChargeSnowballSplash Potion

Fired in the direction the dispenser is facing, as if a player had used the item themselves


Boat

Placed as entity (i.e., a right-clickable vehicle) onto the block in front of the dispenser, if it is water or air above water; otherwise dropped (see below)


Firework Rocket

Placed as entity (i.e., a flying firework) onto the block in front of the dispenser


Bone Meal

Increments the growth stage of beetroot crops, carrots, cocoa pods, crops, melon stems, potatoes, pumpkin stems, and saplings in front of the dispenser; grows grass, dandelions, and roses, if a grass block is in front of the dispenser; grows a huge mushroom if facing a mushroom; otherwise remains unused


Bucket

Collects lava or water in front of the dispenser (replacing the empty bucket in the dispenser with a lava bucket or water bucket); otherwise dropped (see below)


Flint and Steel

Ignites the block the dispenser is facing; reduces the remaining durability of the used flint and steel


Lava BucketWater Bucket

Places lava or water in the block in front of the dispenser (replacing the lava or water bucket in the dispenser with an empty bucket), if the block in front of the dispenser is one that the player could use a lava or water bucket on (e.g., air, flowers, grass, etc.); otherwise dropped (see below)


MinecartMinecart with ChestMinecart with Command BlockMinecart with FurnaceMinecart with HopperMinecart with TNT

Placed as entity (i.e., a right-clickable vehicle) in the block in front of the dispenser, if the dispenser is in front of a type of rail; otherwise dropped (see below)


TNT

Ignites TNT on the block in front of the dispenser


Shears

Shears sheep within a one-block radius


Glowstone

If a respawn anchor is one block away, it fills the respawn anchor by 1 as if a player had right clicked with glowstone. If the respawn anchor is full, the dispenser does nothing


Others

Dropped—ejected toward the block in front of the dispenser, as if the player had used the Drop control (default Q)

** Considerations **
A dispenser is an opaque block, so powering it directly can activate adjacent mechanism components (including other dispensers) as well.
###  Door
Main article: Door
A door is used to control or prevent the movement of mobs, items, boats, and other entities. A door may be of two types: a wooden door can be opened and closed by redstone power or by a player right-clicking on it, while an iron door can be operated only by redstone power.

** Placement **
A door can be attached to thetopof mostopaqueblocks, or to thetopof an upside-downslabor upside-downstairs. If the attachment block is removed, the door drops as an item.
A door is placed on the edge of the block facing the player. By default the door's hinge is positioned on the left side, but another door or block can force the hinge to the right side.
** Effect **
While activated, a door re-positions to the other side of its hinge, allowing movement through its former position and denying movement through its current position. When activated, any entities on the door fall off.
A door doesn't actually move (the way a piston arm or a pushed block moves), it simply disappears from one side and re-appears on another; therefore, it does not push entities as it opens.
