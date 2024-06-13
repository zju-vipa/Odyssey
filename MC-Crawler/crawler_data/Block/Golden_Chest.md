# Golden Chest
A golden chest is a joke variant of the chest, added in snapshot 23w13a_or_b, that is created by opening a normal/trapped chest while the minecraft:midas_touch vote rule is activated. Ender chests are not affected.

## Contents
- 1 Obtaining
	- 1.1 Breaking
- 2 Usage
	- 2.1 Container
	- 2.2 Redstone component
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 History

## Obtaining
Golden chests are not a separate block and thus can't be obtained with the command /give or through the creative inventory. To create a golden chest without minecraft:midas_touch activated, the player can use the /setblock command with a regular or trapped chest and the tag "gold": /setblock ~ ~ ~ minecraft:chest{gold:1b}, or /setblock ~ ~ ~ minecraft:trapped_chest{gold:1b}.

Opening a large chest with midas_touch changes the chest visually, but the texture is glitched. Large golden chest/trapped chest does not change the items inside into gold.

### Breaking
Golden chests cannot be obtained when mined, and drop normal chests, even when using a tool enchanted with Silk Touch.

| Block     | Golden Chest          |
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


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


## Usage
Golden chests work similar to normal chests, have a golden appearance and don't drop when broken. Golden trapped chests still function as trapped chests, but have no identifier like in regular ones. They however have a random chance on every item in the chest turning into a golden item, according to the minecraft:midas_touch vote rule:

- Iron nuggets become gold nuggets.
- Raw copper and raw iron become raw gold.
- Raw copper blocks and raw iron blocks become raw gold blocks.
- Normal ore blocks become gold ore.
- Deepslate ore blocks become deepslate gold ore.
- Nether quartz ore becomes nether gold ore.
- Swords, axes, pickaxes, shovels, hoes, armor and horse armor become golden.
- Apples become golden apples and golden apples become enchanted golden apples.
- Carrots become golden carrots.
- Melon slices become glistering melon slices.
- Rails become powered rails.
- Arrows become spectral arrows.
- Other items and blocks become gold ingots and gold blocks.

### Container
Main article: Chest § Container
A golden chest has 27 slots of inventory space.

Golden chests open when used. To move items between the golden chest inventory and the player inventory or hotbar while the golden chest GUI is open, drag or shift-click the items. Holding Shift and double-clicking while holding an item moves all items of the type clicked on in or out of the golden chest, to the extent that space is available for them. To exit the golden chest GUI, use the Esc control.

### Redstone component
Main article: Trapped Chest § Redstone component
Golden trapped chests can be used to detect when their inventory is accessed by players.

A golden trapped chest is inactive while not being accessed, but activates when accessed by a player. Mobs cannot access/activate a golden trapped chest, and a golden trapped chest is not activated by items moving into or out of it by droppers or hoppers.

While active, a golden trapped chest:

- powers any adjacentredstone dust, including beneath the golden trapped chest, to apower levelequal to the number of players accessing the golden trapped chest (maximum 15);
- powers any adjacentredstone repeatersfacing away from the golden trapped chest to power level 15;
- strongly powers any full solid opaque block (stone, dirt, block of gold, etc.) beneath the golden trapped chest to a power level equal to the number of players accessing the golden trapped chest (maximum 15);
- activates any adjacentmechanism components, including above or below, such aspistons,redstone lamps, etc. Due to hoppers being locked by redstone activation, hoppers below a golden trapped chest do not take items from it while it is open.

An active golden trapped chest does not power any adjacent redstone comparators facing away from it. Redstone comparators can measure the block state of the golden trapped chest, producing a power level from 0 to 15 proportional to how full the golden trapped chest is. Anything else powered by an active trapped chest (including a block beneath it) can power redstone comparators normally.

