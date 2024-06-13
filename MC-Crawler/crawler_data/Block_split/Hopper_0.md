# Hopper
A hopper is a low-capacity storage block that can be used to collect item entities directly above it, as well as to transfer items into and out of other containers. A hopper can be locked with redstone power to stop it from moving items into or out of itself.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Crafting
- 2 Usage
	- 2.1 Container
	- 2.2 Crafting ingredient
	- 2.3 Redstone component
		- 2.3.1 Redstone signals
		- 2.3.2 Collecting items
		- 2.3.3 Pushing and pulling items
		- 2.3.4 Container interactions
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
	- 4.3 Block data
- 5 Achievements
- 6 Video
- 7 History
- 8 Issues
- 9 Trivia
- 10 Gallery
	- 10.1 Renders
		- 10.1.1 Java Edition
		- 10.1.2 Bedrock Edition
	- 10.2 Screenshots
- 11 References

## Obtaining
### Breaking
To obtain a hopper, mine it with a pickaxe. Using any other item to mine a hopper drops only its contents.

| Block     | Hopper                |
|-----------|-----------------------|
| Hardness  | 3                     |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 15                    |
| Wooden    | 2.25                  |
| Stone     | 1.15                  |
| Iron      | 0.75                  |
| Diamond   | 0.6                   |
| Netherite | 0.5                   |
| Golden    | 0.4                   |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


### Crafting
A hopper can be crafted from 5 iron ingots and a chest.

| Ingredients      | Crafting recipe |
|------------------|-----------------|
| Iron Ingot+Chest |                 |

## Usage
See also: Tutorials/Hopper

Hoppers can face down or sideways.
A hopper can be used as a container, as a crafting ingredient, and as a redstone component.

A hopper has an "output" tube at its bottom that can face down or sideways and provides a visual indication of which block the hopper is set up to drop its items into, if that block has an inventory. To place a hopper, use the Place Block control while aiming at the surface to which its output should face (Hoppers do not orient themselves automatically). To place a hopper directly on the face of an already interactable block, the player can sneak while placing the hopper. Attempting to place a hopper aimed on the bottom face of a block instead faces downward. With some blocks, such as the furnace and brewing stand, the hopper has multiple uses. A hopper does not change direction after placement, and it is not attached to the container it faces; the container can be removed or replaced, and the hopper remains unchanged.

Hoppers cannot be moved by pistons.‌[Java Edition  only] Despite not being a solid block, attached blocks such as rails, levers, tripwire and redstone dust can be placed on top of hoppers, but not on their sides.

### Container
Hopper GUI showing the hopper's five slots of inventory at the top and the player's inventory below.
A hopper can be used as a container and has 5 slots of inventory space.

To open the hopper GUI, use it. To move items between the hopper inventory and the player inventory or hotbar while the hopper GUI is open, drag or shift-click the items. To exit the hopper GUI, use the Esc key, B button or circle button, depending on the device.

By default, the GUI of a hopper is labeled "Item Hopper". A hopper's GUI label can be changed by naming the hopper in an anvil before placing it, or, in Java Edition, by using the data command (for example, to label a hopper at (0,64,0) "Steve's Hopper", use /data merge block 0 64 0 {CustomName:'"Steve's Hopper"'}).

In Java Edition, a hopper's GUI can be "locked" (or subsequently unlocked) by setting the hopper's Lock tag with the data command. If a hopper's Lock tag is not blank, the hopper cannot be accessed except by players holding an item with the same name as the Lock tag's text. For example, to lock a hopper at (0,64,0) so that only players holding an item named "Steve's Key" can access the hopper, use /data merge block 0 64 0 {Lock:"Steve's Key"}.

### Crafting ingredient
| Name                 | Ingredients     | Crafting recipe |
|----------------------|-----------------|-----------------|
| Minecart with Hopper | Hopper+Minecart |                 |

### Redstone component
See also: Redstone circuit and Redstone components § Hopper

Flowchart of hopper logic
While a hopper is not powered by redstone signals, it operates with three functions:

- Collectitem entities(free-floating items in the world) into its inventory from the space above it
- Pulla single item into its inventory from a container above it
- Pusha single item from its own inventory into a container it faces

A hopper first attempts to push any items inside it. Afterward, it checks if the block above it is a type of container. If so, it attempts to pull from it. Otherwise, the hopper attempts to collect item entities. Notably, hoppers can push to and pull from other hoppers, forming hopper pipes or hopper chains, which allow transporting items across several blocks and are further discussed below.

#### Redstone signals
When a hopper receives a redstone signal (and is considered to be "activated"), all three functions stop. To avoid confusion over the terms "activated" and "deactivated", powered hoppers are often described as being locked and unpowered hoppers described as being unlocked. Hoppers can be powered by soft powered blocks, meaning a redstone dust trail pointing into a block touching the hopper locks it just as effectively as a block of redstone or any other power component touching the hopper. When the hopper is unlocked during a redstone tick, it does not push or pull/collect during the same tick, but has a delay of 1 redstone tick instead.

While a locked hopper does not push or pull/collect items, it may still receive items from dispensers, droppers and other hoppers, and may have its items pulled out by another hopper beneath it. Hence, the item flow in a horizontal hopper pipe may be stopped by locking just one of the hoppers, but stopping a vertical hopper pipe requires locking two adjacent hoppers at the same time, such that both the pushing of the top one and the pulling of the bottom one are stopped.

A hopper does not output any redstone signals by itself, but its fullness can be read using a redstone comparator, which needs to be placed next to it and facing away from it. An empty hopper outputs a signal strength of 0 and a completely full hopper outputs a signal strength of 15. Notably, a single stackable item (16 or 64) outputs a signal strength of 1 and a single non-stackable item outputs a signal strength of 3.

In Java Edition, if the hopper being read is part of a horizontal hopper pipe, the comparator can individually read each item passing through the chain, because items are pushed through the hoppers one by one at a speed that is manageable by the comparator. If there is an uninterrupted stream of items, the comparator does not switch off in between items. On the other hand, in a vertical hopper pipe, some of the hoppers may never produce a reading above 0, even with a continuous stream of items, because pushes and pulls both occur in the same game tick: The hoppers' items get pulled out a single game tick after they're pushed in and this isn't measurable by a comparator, because comparators need measurements lasting at least 1.5 redstone ticks to produce a reading.

