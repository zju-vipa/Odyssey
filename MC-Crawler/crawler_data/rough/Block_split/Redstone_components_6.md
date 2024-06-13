###  Rail
Main article: Rail
Rails and powered rails as mechanism components
A rail is used to switch the track of a minecart.

** Placement **
A rail can be attached to thetopof anyopaqueblock, or to thetopof an upside-downslabor upside-downstairs. If the attachment block is removed, the rail drops as an item.
When placed, rail configures itself to line up with adjacent rails, powered rails, and detector rails, as well as such adjacent rails one block up. If there are two such adjacent rails on non-opposite sides, the rail curves from one to the other. If there are three or four such adjacent rails, the rail curves between two of them (when choosing which directions to curve between, a rail prefers south over north, and east over west). If there are no such adjacent rails, the rail lines up in the north-south direction. If a rail it would line up with is one block up, a rail slants upward toward itwithoutcurving (with multiple options to slant upward to, a rail prefers, in order: west, east, south, and north). Other configurations can be created by placing and removing various rails.
** Effect **
When activated, a rail in a "T" junction flips to curve the other way (activating a rail in another configuration has no effect).
###  Redstone lamp
Main article: Redstone Lamp
A redstone lamp is used to provide light.

** Activation **
A redstone lamp activates normally, but takes 2 ticks to deactivate.
** Effect **
While activated, a redstone lamp has block light level 15 (so produces block light level 14 in all adjacent transparent spaces). An activated redstone lamp is transparent to sky light.
** Considerations **
A redstone lamp is an opaque block, so powering it directly can cause adjacent mechanism components (including other redstone lamps) to activate as well.
###  TNT
Main article: TNT
TNT is used to create an explosion.

** Activation **
In addition to the methods above, TNT can also be activated byfireand explosions, as well as flaming arrows.
** Effect **
When activated, TNT ignites and becomes primed TNT, an entity that can fall like sand or be pushed by pistons (but isn't moved by water). Primed TNT explodes 40 ticks (4 seconds) after being ignited by redstone power (10-30 ticks for TNT ignited by an explosion).
** Considerations **
A TNT is a transparent block, so powering it directly does not cause adjacent mechanism components (including TNTs) to activate.
###  Trapdoor
A trapdoor is used to control or prevent the movement of mobs, items, boats, and other entities. A trapdoor may be of two types: a wooden door can be opened and closed by redstone power or by a player right-clicking on it, while an iron door can be operated only by redstone power.

** Placement **
A trapdoor can be attached to the top, bottom, or thesideof blocks. If the attachment block is removed, the trapdoor does not drop.
** Effect **
While activated, a trapdoor re-positions itself in a vertical state, allowing vertical movement through it. When activated, any entities on the trapdoor fall down.
Similar to a door, a trapdoor doesn't actually move (the way a piston arm or a pushed block moves), it simply disappears from one state and re-appears in another, so it does not push entities as it opens.
###  Command block
Main article: Command Block
A command block is used to execute a server command. Command blocks can be obtained only by placing it or giving it to the player with commands.

** Types **
A command block have 3 types: impulse (execute a command once), chain (execute a command when triggered) and repeat (execute a command for 1 or more redstone ticks when powered)

** Placement **
After being placed, the player can set the command to be executed by right-clicking on the command block.
** Effect **
When activated, a command block executes its defined commandonce. To make a command block constantly execute its command, it must be run on aclock circuitor using a repeating command block.
Like other mechanism components, an already-activated command block does not respond to other redstone signals. To make a command block execute its defined command more than once it must be deactivated and re-activated repetitively.
** Considerations **
A command block is an opaque block, so powering it directly can activate adjacent mechanism components (including other command blocks) as well.

###  Structure block
Main article: Structure Block
A Structure Block is used to save and load structures. Structure blocks can be obtained only by placing it or giving it to the player with commands.

** Placement **
After being placed, the player can set the mode or the structure to save/load by right-clicking the structure block.
** Effect **
Redstone signals can be used to automate some of the structure block's functions.
Like other mechanism components, an already-activated structure block does not respond to other redstone signals. To make a command block execute its defined command more than once it must be deactivated and re-activated repetitively.
## Mobile components
###  Minecart
Main article: Minecart
A minecart is used to transport a mob or player over rails.

** Behavior **
The player can move a minecart by pushing against it while outside the minecart (whether the minecart is on rails or not), or by pressing the Forward control key (by default, W) while inside the minecart (only while the minecart is on rails). A minecart resting on powered rails configured to point at an adjacent opaque block is propelled away from the opaque block when the powered rails are activated. A minecart traveling over activated powered rails gets a speed boost. When a minecart passes over an activated activator rails, the entity inside it is ejected out.
