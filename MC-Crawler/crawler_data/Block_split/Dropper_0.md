# Dropper
A dropper is a low-capacity storage block that can eject its contents into the world or into other containers when given a redstone signal.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Crafting
- 2 Usage
	- 2.1 Container
	- 2.2 Redstone component
		- 2.2.1 Container interactions
	- 2.3 Note blocks
	- 2.4 Crafting ingredient
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
	- 4.3 Block data
- 5 Video
- 6 History
- 7 Issues
- 8 Trivia
- 9 Gallery
	- 9.1 Renders
		- 9.1.1 Java Edition
		- 9.1.2 Bedrock Edition
- 10 See also
- 11 References
- 12 External links

## Obtaining
### Breaking
A dropper can be mined with a pickaxe, in which case it drops itself and its contents. If mined without a pickaxe, the dropper drops only its contents.

| Block     | Dropper               |
|-----------|-----------------------|
| Hardness  | 3.5                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 17.5                  |
| Wooden    | 2.65                  |
| Stone     | 1.35                  |
| Iron      | 0.9                   |
| Diamond   | 0.7                   |
| Netherite | 0.6                   |
| Golden    | 0.45                  |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


### Crafting
| Ingredients               | Crafting recipe |
|---------------------------|-----------------|
| Cobblestone+Redstone Dust |                 |

## Usage
A dropper can be used as a container or as a redstone component to move items.

A dropper can be placed so that its output faces in any direction, including up or down. When placed, the dropper's output faces toward the player. With default textures, the droppers output side looks like a face when positioned for horizontal output. Otherwise, the output side has a square hole.

In Java Edition, droppers cannot be moved by pistons.

### Container
GUI of the dropper.
A dropper has 9 slots of inventory space.

To open the dropper GUI, use the Use Item control. To move items between the dropper inventory and the player inventory or hotbar while the dropper GUI is open, drag or shift-click the items. To exit the dropper GUI, use the Esc control.

By default, the GUI of a dropper is labeled "Dropper". A dropper's GUI label can be changed by naming the dropper in an anvil before placing it. In Java Edition, droppers can also be renamed by using the /data command (for example, to label a dropper at (0,64,0) "Alice's Dropper", use /data merge block 0 64 0 {CustomName:'"Alice's Dropper"'}).

In Java Edition, a dropper can be "locked" (or subsequently unlocked) by setting the dropper's Lock tag with the /data command. If a dropper's Lock tag is not blank, the dropper cannot be accessed except by players holding an item with the same name as the Lock tag's text. For example, to lock a dropper at (0,64,0) so that only players holding an item named "Alice's Key" can access the dropper, use /data merge block 0 64 0 {Lock:"Alice's Key"}.

### Redstone component
See also: Redstone circuit

A dropper can be used to eject items, or push items into another container.

Activation
A dropper can be activated by:
an adjacent active power component (exceptions: a redstone torch does not turn ON a dropper it is attached to)
an adjacent powered opaque block (strongly-powered or weakly-powered)
a powered redstone repeater or redstone comparator facing the dropper
powered redstone dust configured to point at the dropper, or on top of it; a dropper is not activated by adjacent powered redstone dust that is configured to point in another direction.
In addition to the methods above, droppers in Java Edition can also be activated by quasi-connectivity. A dropper activates if one of the methods above would activate a mechanism component in the block above the dropper, even if there is no mechanism component there (even if the block above the dropper is air or a transparent block), but only when the dropper receives a block update (including a redstone update within two blocks of the dropper).
A dropper has a 2 redstone tick (4 game ticks, or 0.2 seconds barring lag) delay between activation and a response. During this time, additional inputs are ignored.
Behavior
See also: Tutorials/Item elevator § Dropper

When activated, a dropper waits 2 redstone ticks (4 game ticks, or 0.2 seconds barring lag) and then ejects one item from its inventory. The dropper does not continue to eject items while activated — ejection occurs only on the initial activation (the rising edge of an input signal). To eject multiple items, repeatedly activate the dropper with a clock circuit.
If multiple slots are occupied by items, a random occupied slot is chosen for ejection. The slot is chosen when an item is ejected, not when the dropper is initially activated, thus it is possible to move items into or out of a dropper between its activation and item dispensing.
If the dropper is facing a container, the ejected item is transferred into the container. If the container it is facing is full, or the item cannot be inserted into the container, the dropper does not activate.
Otherwise, the item is ejected in the direction the dropper is facing, as if a player had used the drop control. Even items that would be treated differently by a dispenser (such as arrows) are simply ejected by a dropper.
A dropper makes a clicking noise (the random.click sound event) when activated empty or when ejecting items into air. It is silent when it successfully transfers an item into any kind of chest or barrel, or another dropper.
A dropper is an opaque block, so powering it directly can cause adjacent mechanism components (including other droppers) to activate as well.

A line of droppers, each pushing items into the next dropper, is known as a dropper pipe. A dropper pipe must be clocked to move items, but can be clocked to move items faster than a hopper pipe's transfer rate. When a dropper pipe pushes items upward, it is known as a droppervator (short for "dropper elevator").

