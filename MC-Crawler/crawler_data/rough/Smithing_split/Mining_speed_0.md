# Breaking
Breaking, digging, punching, or mining is a common activity in Minecraft, performed (by default) by holding the left mouse button or right trigger while the cursor is pointing at a block, or by long-pressing on the block on touch screens. Breaking is the primary way to remove unwanted blocks and acquiring blocks for future placement or crafting.

## Contents
- 1 Basics of breaking
- 2 Speed
	- 2.1 Instant breaking
	- 2.2 Calculation
	- 2.3 Best tools
- 3 Blocks by hardness
- 4 Video
- 5 History
- 6 Trivia
- 7 Notes
- 8 References

## Basics of breaking


By holding down the destroy button while the player is within range of the target block and while selecting the block, the player's hand begins swinging, making a repetitive "thump" sound as the player hits the block, and cracks appear on it while being broken.

In Java Edition, this range is 5.2 blocks in Creative mode, and 4.5 blocks otherwise. In Bedrock Edition, the range is 5 blocks when using a keyboard/mouse or controller input, and when using touch input, the range is 12 blocks in Creative mode and 6 blocks otherwise.

Blocks are marked with a wireframe cube outline (or turn slightly brighter on touch screens), making the current target easily visible (this can be toggled on and off in Pocket Edition). After the cracks completely cover the block, it breaks and depending on the type of block and the tool used to do so, it may drop an item.

Although many blocks can be harvested with bare hands, certain ones require the use of a tool. In particular, to obtain resources from stone or metal-type blocks, the player must use a pickaxe. For harder blocks like iron ore or obsidian, a pickaxe made from a higher-tier material is required. 

The player can use shovels, axes and hoes to speed up the breaking of dirt-type blocks, wood, and plant-type blocks, respectively. However, tools are not required to get the resource drop (with the exception of snow and snow blocks, which require a shovel to get a drop). A downside to this is that tools also have durability, so they eventually wear out.

If the tool has the blue Unbreakable tag under its enchantment and name, it never breaks. In Java Edition, one can be acquired using the command /give: /give @s diamond_pickaxe{Unbreakable:1b}

The progress for breaking a block is reset if the target block changes while breaking. Progress is also reset whenever the breaking control is released. The player can move freely while breaking blocks. The player can even dig while jumping, swimming, or riding, although this reduces the breaking speed.

In Survival mode, however, some blocks are unbreakable, like bedrock, and in Adventure mode all blocks are unbreakable unless the player has a item/tool with the can_destroy NBT tag. In Spectator mode a player can't break blocks in any way, and in Creative mode all blocks are breakable unless the player is holding a sword, trident, or debug stick.

## Speed
The player's digging speed is controlled by three factors: the block being broken, the item the player is currently wielding, and the mining penalties affecting the player. Every block has a hardness value, which determines the base amount of breaking time if the player hits it with their bare hands.

The base time in seconds is the block's hardness multiplied by:

- 1.5 if the player can harvest the block with the current tool;
- 5 if the player cannot.

Assuming that the player can harvest the block, the next check is whether the player's tool increases the breaking speed for the block. See Best tools for a full list.

If the tool helps, then it increases digging speed by a constant multiplier, given in the following table:

| Material   | Nothing | Wood | Stone | Iron | Diamond | Netherite | Gold | Shears                                                       | Sword              | Efficiency                                       | Haste                                     |
|------------|---------|------|-------|------|---------|-----------|------|--------------------------------------------------------------|--------------------|--------------------------------------------------|-------------------------------------------|
| Tool Speed | 1       | 2    | 4     | 6    | 8       | 9         | 12   | 2 (1 onvinesandglow lichen, 5 onwool, 15 oncobwebsandleaves) | 1.5 (15 oncobwebs) | additional (1+level2) when using the proper tool | additional (20×level)% per level of Haste |

If a proper tool is used, the tool speed is further increased by the Efficiency enchantment. If the level of Efficiency is not 0, then the level squared plus 1 is added to the tool speed. For example, Efficiency I adds 2 to the value, while Efficiency V adds 26. The speed is also increased by (20×level)% per level of Haste, while Mining Fatigue decreases it by 70% for level I, 91% for level II, 97.3% for level III, and 99.19% for all other levels.

If the player's head is underwater and they are not wearing a helmet with the Aqua Affinity enchantment, breaking a block takes 5 times as long. If the player's feet are not touching the ground, an additional 5x penalty is added; this causes players floating in water to break blocks 25x slower than if they had been standing on land.

The total time to break a block is always a multiple of 1⁄20 of a second, or 1 game tick; any remainder is rounded up to the next tick.

### Instant breaking
Main article: Instant mining
When breaking a block, a tool and its enchantments do its speed value as "damage" to a block every game tick, and when that value exceeds the block's hardness times 30, the block breaks. If the tool and enchantments immediately exceed the hardness times 30, the block breaks with no delay; otherwise a 6 tick (3⁄10 second) delay occurs before the next block begins to break.

For example, a player with Haste II holding an Efficiency V diamond pickaxe (or netherite pickaxe) can break stone instantly, as the damage is (8+26)×(1+0.4)=47.6, which is greater than the base hardness of stone (1.5) times 30 (which is 45). Players in creative mode always break blocks instantly regardless of tools or status effects, except for when wielding a sword, debug stick, trident or a mace ‌[upcoming: JE 1.21 & BE 1.21.0], in which case the player is unable to break anything.

