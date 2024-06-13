# Trapped Chest
A trapped chest is a variant of the chest that functions similarly, but has a red-tinted latch, and produces redstone power while open.

Like normal chests, two trapped chests can merge into a large trapped chest if placed next to each other.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
- 2 Usage
	- 2.1 Container
	- 2.2 Redstone component
	- 2.3 Piglins
	- 2.4 Fuel
	- 2.5 Note blocks
- 3 Christmas chest
- 4 Sounds
	- 4.1 Generic
	- 4.2 Unique
- 5 Data values
	- 5.1 ID
	- 5.2 Block states
	- 5.3 Block data
- 6 Video
- 7 History
- 8 Issues
- 9 Trivia
- 10 References

## Obtaining
### Breaking
Trapped chests can be broken with any tool, but axes are the fastest. Items contained in the chest are dropped when the chest is broken. If one half of a large trapped chest is destroyed, the corresponding items from the destroyed trapped chest are dropped and the remaining trapped chest continues to function as a small trapped chest.

| Block     | Trapped Chest         |
|-----------|-----------------------|
| Hardness  | 2.5                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 3.75                  |
| Wooden    | 1.9                   |
| Stone     | 0.95                  |
| Iron      | 0.65                  |
| Diamond   | 0.5                   |
| Netherite | 0.45                  |
| Golden    | 0.35                  |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
Trapped chests naturally generate in "fake end portal rooms" in woodland mansions.

### Crafting
| Ingredients              | Crafting recipe |
|--------------------------|-----------------|
| Tripwire Hook+<br/>Chest |                 |

## Usage
Trapped chests can be used as containers and as redstone components.

To place a trapped chest, place the face of a block adjacent to the space the trapped chest should occupy.

Placing two adjacent trapped chests side-by-side typically joins them to create a large trapped chest. To avoid them joining and instead place two single trapped chests side by side, the player may sneak while placing the second trapped chest‌[Java Edition  only] ,or place the second trapped chest facing a different direction from the first one. Alternately, normal chests do not combine with trapped chests.

Trapped chests can be moved by pistons.‌[Bedrock Edition  only] Water and lava flow around without affecting them. Lava can create fire in air blocks next to trapped chests as if they were flammable, but the chests do not burn (and cannot be burned by other methods either).

Trapped chests can also activate buried TNT, destroying themselves, their contents and any mobs or players near them. They need to be opened twice for the TNT to be activated.

### Container
The GUI of a trapped chest.
The GUI of a large trapped chest.
A single trapped chest has 27 slots of inventory space, and a large trapped chest has 54 slots of inventory space. In a large trapped chest, the top three rows in the interface correspond to the western or northern chest block and the bottom three to the southern or eastern chest block.

To open the trapped chest GUI, use the Use Item control. To move items between the trapped chest inventory and the player inventory or hotbar while the trapped chest GUI is open, drag or shift-click the items. To exit the trapped chest GUI, use the Esc control.

By default, the GUI of a trapped chest is labeled "Chest" and the GUI of a large trapped chest is labeled "Large Chest." A trapped chest's GUI label can be changed by naming the trapped chest in an anvil before placing it, or by using the /data command‌[Java Edition  only] (for example, to label a trapped chest at (0,64,0) "Loot!", use /data merge block 0 64 0 {CustomName:'"Loot!"'}). If half of a large trapped chest is renamed, that name is used to label the GUI of the entire large trapped chest, but if the named half is destroyed, the other half reverts to the default label. If both halves of a large trapped chest have different names, the GUI label takes the name of the northernmost or westernmost half of the large trapped chest depending on its orientation (the half with the lowest coordinate in the appropriate axis).

A trapped chest can be "locked" by setting the trapped chest's Lock tag. If a trapped chest's Lock tag is not blank, the trapped chest cannot be opened except by players holding an item with the same name as the Lock tag's text. A trapped chest's Lock tag can be set or unset with the data command. For example, to lock a trapped chest at (0,64,0) so that only players holding an item named "Alice's Key" can open the trapped chest, use data merge block 0 64 0 {Lock:"Alice's Key"}.

