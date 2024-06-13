# Smelting
Smelting is a method of obtaining refined goods from raw materials by heating in a furnace, blast furnace, smoker or campfire. For example, raw iron can be smelted to produce iron ingots using coal as fuel. Like crafting, smelting uses recipes to determine what item is produced, but its recipes are simpler. Smelting also yields experience.

## Contents
- 1 Usage and mechanics
- 2 Recipes
	- 2.1 Foods
	- 2.2 Ores
	- 2.3 Gear
	- 2.4 Furnace-only
- 3 Fuel
	- 3.1 Items that can be used as fuel in all types of furnaces
- 4 Hopper automation
- 5 Achievements
- 6 Advancements
- 7 History
- 8 Trivia
- 9 See also
- 10 References

## Usage and mechanics



The smelting interface.



  

This section needs cleanup to comply with the style guide. [discuss]
Please help improve this page. The talk page may contain suggestions.Reason: This section is a mess.


The furnace, blast furnace, and smoker share a similar interface: at the upper left is a slot for smeltable item input, below that is a slot for fuel input, and on the right is a slot where output items accumulate and can be removed by the player. Flames above the fuel slot act as a gauge showing the gradual consumption of the current fuel item, and an arrow in the middle gradually fills to show the progress of smelting the current input item.

To smelt, an input item and fuel must be placed into the input and fuel slots, respectively. The furnace then begins to smelt and continues even after the player closes the interface. (The player can still tell when a furnace is working by its block texture showing flames and fire particle effects appearing.)

The furnace burns one fuel item at a time. Different fuels will fuel the furnace for different amounts of time, and the item in the top will take different amounts of time depending on whether you use a smoker, blast furnace or furnace. The fuel gauge indicates how much of that fuel's burn time remains. As each fuel item is fully consumed, another one is taken from the fuel slot and the gauge starts over.

Smeltable input items are also processed one at a time but are not removed from the input slot while smelting is in progress. The arrow indicates how much of the smelting process has been completed. When the arrow is full, the input item is removed from the input stack and an output item is added to the output stack. Smelting of the next input item then begins immediately.

Smelting stops under any of four conditions:

- When the furnace runs out of smeltable items: That is, the input slot becomes empty.
- The furnace runs out of fuel: The fuel input slot is empty,andthe current fuel item is fully consumed (that is, the fuel gauge becomes empty).
- The output slot becomes full: Either the slot has a full stack of the output, or the output contains the wrong output item for the current input item (for example, if the output contains iron ingots, but the input contains raw gold). In this case, smelting (but not fuel consumption) is paused until the output slot becomes available (usually because items were removed by either a player or a hopper). If a fuel item burns out in this condition, a new one is not used until the output slot is again available.
- The furnace is broken: The contents of all the slots, any accumulated experience, and the furnace itself are dropped. The currently-burning fuel item is lost since it is removed from the fuel slot before burning begins. The furnace block itself may not be dropped if it was destroyed by anexplosion.

If smelting stops while a fuel item is still burning (a normal occurrence), the furnace continues to run visually but no more input items are processed. If the fuel has been exhausted (and the fuel gauge is empty) when an item has been partly smelted, the smelting progress is undone at double speed and the item remains in the input stack.

Smelting is suspended if players move far enough away from the furnace (including going to another dimension) that simulation stops in the chunk the furnace is in. It resumes when a player returns.

If the player sleeps in a bed while a furnace is smelting items, the furnace's progress remains the same as if the bed had not been used and no additional time had passed. This is because when a player sleeps in a bed, no time actually passes; the game simply sets the time of day to morning.

The furnace keeps track of experience for each item as smelting is completed for it, accumulating it in a hidden counter. It remembers the total earned experience even if a hopper is used to remove the items from the output slot. This earned experience is awarded to the next player who uses the interface to remove items manually, after which the counter is reset (if the player takes some of the output but leaves some in the slot, the experience corresponding to those items is retained by the furnace and not awarded to the player).

The campfire has 4 slots on the block and does not contain an interface. Up to four food items can be placed on a campfire, which cooks the items simultaneously. Unlike other blocks that can cook food, campfires do not require any kind of fuel to cook. Assuming that one uses all four slots to cook at once, campfires are more efficient than furnaces (taking 10 seconds less per four items and no fuel) for cooking, but must be watched so as to pick up the food and refill it once it is done. It is slower than a smoker by about ten seconds, but its lack of fuel consumption could be seen as a worthwhile trade-off. Once finished cooking, items pop off the campfire. If the campfire is extinguished while cooking food, the remaining cooking time quickly counts back up. Food items can be placed on an unlit campfire. Any items cooking on a campfire always drop when the campfire block is broken.

Other items can be placed on campfires using external editors, mods or add-ons.

## Recipes
All smelting recipes can be used in the furnace, but only subsets are available in the blast furnace and smoker. When available, they burn twice as fast (5 seconds or 100 game ticks), but use the same amount of fuel.

For fractional experience values, first multiply this value by the number of smelted items removed from the furnace, then award the player the whole-number part, and if there is a fractional part remaining, this represents the chance of an additional experience point.

- For example, when smelting 1coal oreand removing the coal, the value is 0.1, so every ten coal you remove grants you one experience point on average.
- When smelting 5sea picklesand removing all 5lime dye, the value is 0.2×5 = 1, so this grants only 1 point.
- The fractional experience stays within the furnace when the final total is not an integer, so the leftover experience is attributed to the next round of smelting.

### Foods
All food recipes can be used in a furnace or smoker. Food can alternatively be cooked on a campfire, which doesn't require any fuel and takes 30 seconds or 600 game ticks to cook an item, which is faster (when cooking at the maximum capacity of 4 items at a time) than a furnace, but this doesn't award any experience and is slower than a smoker.

| Product              | Ingredient        | Exp  | Description                                                                        |
|----------------------|-------------------|------|------------------------------------------------------------------------------------|
| <br/>Baked Potato    | <br/>Potato       | 0.35 | Fills5 (), while raw fills1 ().                                                    |
| <br/>Dried Kelp      | <br/>Kelp         | 0.1  | Fills1 (), while uncooked kelp is inedible. Used to craftdried kelp blocks.        |
| <br/>Steak           | <br/>Raw Beef     | 0.35 | Fills8 (), while raw fills3 ().                                                    |
| <br/>Cooked Porkchop | <br/>Raw Porkchop | 0.35 | Fills8 (), while raw fills3 ().                                                    |
| <br/>Cooked Mutton   | <br/>Raw Mutton   | 0.35 | Fills6 (), while raw fills2 ().                                                    |
| <br/>Cooked Chicken  | <br/>Raw Chicken  | 0.35 | Fills6 (), while raw fills2 ()and has a 30% chance to give theHungerstatus effect. |
| <br/>Cooked Rabbit   | <br/>Raw Rabbit   | 0.35 | Fills5 (), while raw fills3 ().                                                    |
| <br/>Cooked Cod      | <br/>Raw Cod      | 0.35 | Fills5 (), while raw fills2 ().                                                    |
| <br/>Cooked Salmon   | <br/>Raw Salmon   | 0.35 | Fills6 (), while raw fills2 ().                                                    |

### Ores
All ore recipes can be used in a furnace or blast furnace.

| Product              | Ingredient           | Exp | Description                                                                                                                                                                                                                                                                                          |
|----------------------|----------------------|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <br/>Iron Ingot      | <br/>Raw Iron        | 0.7 | Used to craft various items, includingblast furnaces,anvils,iron blocks,iron nuggets,rails,buckets,cauldrons,chains,compasses,crossbows,flint and steels,heavy weighted pressure plates,hoppers,iron trapdoors,minecarts,pistons,shears,shields,iron armor,iron tools,stonecuttersandtripwire hooks. |
| <br/>Copper Ingot    | <br/>Raw Copper      | 0.7 | Used to craft various items, includingspyglasses,lightning rods,brushes, andblocks of copper.                                                                                                                                                                                                        |
| <br/>Gold Ingot      | <br/>Raw Gold        | 1   | Used to craft various items, includingnetherite ingots,gold blocks,golden apples,gold nuggets,clocks,golden armor,golden tools,powered railsandlight weighted pressure plates. Also used as a currency forbartering.                                                                                 |
| <br/>Gold Ingot      | <br/>Nether Gold Ore | 1   | Used to craft various items, and as a currency forbarteringwithpiglins.<br/>Nether gold ore can be obtained only by mining with aSilk Touchpickaxe.                                                                                                                                                  |
| <br/>Netherite Scrap | <br/>Ancient Debris  | 2   | Used to craftnetherite ingots, which can be used to upgrade diamond gear and craftnetherite blocksas well aslodestones.                                                                                                                                                                              |

The following additional ores can be smelted, but it's more efficient to mine them with an appropriate pickaxe. In most cases mining them saves fuel and yields more product and experience, especially if the pickaxe has a Fortune enchantment. Smelting them, though, allows obtaining them from an automatic device. The ore blocks themselves can be obtained only via the Silk Touch enchantment.

| Product            | Ingredient             | Exp | Description                                                                                                                          |
|--------------------|------------------------|-----|--------------------------------------------------------------------------------------------------------------------------------------|
| <br/>Redstone Dust | <br/>Redstone Ore      | 0.3 | Used tocraftvarious items andredstone blocks,brewing, or placed as redstone wire.<br/>When normally mined drops 4–5 redstone and1–5. |
| <br/>Coal          | <br/>Coal Ore          | 0.1 | Used as a fuel, and to crafttorches,campfiresandblocks of coal.<br/>When normally mined drops 1 coal and0–2.                         |
| <br/>Emerald       | <br/>Emerald Ore       | 1   | Used fortrading, and to craftblocks of emerald.<br/>When normally mined drops 1 emerald and3–7.                                      |
| <br/>Lapis Lazuli  | <br/>Lapis Lazuli Ore  | 0.2 | Used forenchantingand for craftingblue dyesandblocks of lapis lazuli.<br/>When normally mined drops 4–8 lapis lazuli and2–5.         |
| <br/>Diamond       | <br/>Diamond Ore       | 1   | Used to craft various items,enchanting tables,jukeboxesandblocks of diamond.<br/>When normally mined drops 1 diamond and3–7.         |
| <br/>Nether Quartz | <br/>Nether Quartz Ore | 0.2 | Used to craft various items andquartz blocks.<br/>When normally mined drops 1 nether quartz and2–5.                                  |
| <br/>Iron Ingot    | <br/>Iron Ore          | 0.7 | Used to craft various items.                                                                                                         |
| <br/>Copper Ingot  | <br/>Copper Ore        | 0.7 | Used to craft various items.                                                                                                         |
| <br/>Gold Ingot    | <br/>Gold Ore          | 1   | Used to craft various items, and as a currency forbarteringwithpiglins.                                                              |

### Gear
These recipes can be used in a furnace or blast furnace to recycle unneeded gear (tools, weapons, armor and horse armor).

| Product          | Ingredient                                                        | Exp | Description                                                         |
|------------------|-------------------------------------------------------------------|-----|---------------------------------------------------------------------|
| <br/>Iron Nugget | <br/><br/>Tools,armorandhorse armormade fromiron, chainmail armor | 0.1 | Can be crafted intolanterns,chains, oriron ingots.                  |
| <br/>Gold Nugget | <br/>Tools, armor and horse armor made fromgold                   | 0.1 | Can be crafted intogolden carrots,glistering melons, orgold ingots. |

### Furnace-only
These recipes are exclusive to the furnace.

| Product                                 | Ingredient                                                          | Exp                | Description                                                                                                                                                                                                           |
|-----------------------------------------|---------------------------------------------------------------------|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <br/>Stone                              | <br/>Cobblestone                                                    | 0.1                | Used as a building material. Also used for craftingstone pressure plates,stone buttons,stone bricks,grindstones,stonecutters,redstone repeatersandcomparators. Can be smelted intosmooth stone.                       |
| <br/>Smooth Stone                       | <br/>Stone                                                          | 0.1                | Used as a building material. Also used for craftingsmooth stone slabs,armor stands, andblast furnaces.                                                                                                                |
| <br/>Cracked Stone Bricks               | <br/>Stone Bricks                                                   | 0.1                | Decoration block.                                                                                                                                                                                                     |
| <br/>Deepslate                          | <br/>Cobbled Deepslate                                              | 0.1                | Decoration block.                                                                                                                                                                                                     |
| <br/>Cracked Deepslate Bricks           | <br/>Deepslate Bricks                                               | 0.1                | Decoration block.                                                                                                                                                                                                     |
| <br/>Cracked Deepslate Tiles            | <br/>Deepslate Tiles                                                | 0.1                | Decoration block.                                                                                                                                                                                                     |
| <br/>Smooth Sandstone                   | <br/>Sandstone                                                      | 0.1                | Used as a building material. Also used for craftingsmooth sandstone slabsandstairs.                                                                                                                                   |
| <br/>Smooth Red Sandstone               | <br/>Red Sandstone                                                  | 0.1                | Used as a building material. Also used for craftingsmooth red sandstone slabsandstairs.                                                                                                                               |
| <br/>Cracked Nether Bricks              | Nether Bricks                                                       | 0.1                | Decoration block.                                                                                                                                                                                                     |
| <br/>Smooth Basalt                      | Basalt                                                              | 0.1                | Decoration block.                                                                                                                                                                                                     |
| <br/>Cracked Polished Blackstone Bricks | <br/>Polished Blackstone Bricks                                     | 0.1                | Decoration block.                                                                                                                                                                                                     |
| <br/>Smooth Quartz                      | <br/>Block of Quartz                                                | 0.1                | Used as a building material. Also used for craftingsmooth quartz slabsandstairs.                                                                                                                                      |
| <br/>Terracotta                         | <br/>Clay                                                           | 0.35               | Decoration block. Also used for craftingstained terracotta. Can be smelted intoglazed terracotta.                                                                                                                     |
| <br/>Glazed Terracotta                  | <br/>Stained Terracotta                                             | 0.1                | Decoration block. Can be pushed bypistonsbut does not stick.                                                                                                                                                          |
| <br/>Glass                              | Sand                                                                | 0.1                | Used to make transparent structures. Also used to craftglass panes,glass bottles, stained glass,end crystals,daylight detectors, andbeacons.                                                                          |
| <br/>Sponge                             | <br/>Wet Sponge                                                     | 0.15               | Used to soak up water. Drying aspongeallows it to be reused. If an emptybucketis in the fuel slot when smelting finishes, it becomes awater bucket. Wet sponges can also be instantly dried when placed inthe Nether. |
| <br/>Charcoal                           | <br/>Log<br/><br/>Wood<br/><br/>Stripped Log<br/><br/>Stripped Wood | 0.15               | Used to crafttorches, soul torches,campfiresandfire charges, and as fuel for smelting or for aminecart with furnace‌[JE  only]. Input must be an Overworld log or wood, not sticks, planks, or stems.                 |
| <br/>Popped Chorus Fruit                | <br/>Chorus Fruit                                                   | 0.1                | Used to makepurpur blocksandend rods. Cannot be eaten.                                                                                                                                                                |
| <br/>Lime Dye                           | <br/>Sea Pickle                                                     | 0.1                | Used as adye.                                                                                                                                                                                                         |
| <br/>Green Dye                          | <br/>Cactus                                                         | JE:1[1]<br/>BE:0.2 | Used as adye.                                                                                                                                                                                                         |
| <br/>Brick                              | <br/>Clay Ball                                                      | 0.3                | Used to makebricksandflower pots.                                                                                                                                                                                     |
| <br/>Nether Brick                       | <br/>Netherrack                                                     | 0.1                | Used to makenether bricks,nether brick fencesandred nether bricks.                                                                                                                                                    |

## Fuel
See also: Tutorials/Smelting

There are multiple fuels that can be used to smelt items. The type of fuel that should be used depends on the number of items in question.

For larger jobs, a single lava bucket or a block of coal can smelt more items than can fit in the furnace, a lava bucket being able to smelt 100 blocks and a block of coal being able to smelt 80 —both input and output are limited to a maximum of a stack of 64 items (with some items not being able to be stacked or being possible to stack only 16 of them).

### Items that can be used as fuel in all types of furnaces

  

This article is a work in progress. 
Please help expand and improve it. The talk page may contain suggestions.


| Fuel                                      | Burning time(seconds)[note 1]  | Number of operations per fuel | Number of operations per stack (64) of fuel[note 2] | Seconds per log[note 3]       | Seconds per bamboo[note 4]   | Amount needed to smelt a stack (64) of items | Notes                                                                     |
|-------------------------------------------|--------------------------------|-------------------------------|-----------------------------------------------------|-------------------------------|------------------------------|----------------------------------------------|---------------------------------------------------------------------------|
| Lava Bucket                               | 1000<br/>16:40<br/>20000 ticks | 100                           | 100                                                 | None used                     | None used                    | 0.64                                         | If a lava bucket is used as fuel, anempty bucketremains in the fuel slot. |
| Block of Coal                             | 800<br/>13:20<br/>16000 ticks  | 80                            | 5120                                                | None used                     | None used                    | 0.8                                          |                                                                           |
| Dried Kelp Block                          | 200<br/>3:20<br/>4000  ticks   | 20                            | 1280                                                | None used                     | None used                    | 3.2                                          |                                                                           |
| Blaze Rod                                 | 120<br/>2:00<br/>2400 ticks    | 12                            | 768                                                 | None used                     | None used                    | $5\frac{1}{3}$                               |                                                                           |
| Coal                                      | 80<br/>1:20<br/>1600 ticks     | 8                             | 512                                                 | None used                     | None used                    | 8                                            |                                                                           |
| Charcoal                                  | 80<br/>1:20<br/>1600 ticks     | 8                             | 512                                                 | 70<br/>[note 5]               | None used                    | 8                                            |                                                                           |
| AnyBoat                                   | 60<br/>1200 ticks              | 6                             | 6                                                   | 48                            | $2\frac{2}{3}$               | $10\frac{2}{3}$                              |                                                                           |
| AnyBoat with Chest                        | 60<br/>1200 ticks              | 6                             | 6                                                   | $18\frac{6}{13}$<br/>(~18.46) | $1\frac{1}{39}$<br/>(~1.03)  | $10\frac{2}{3}$                              |                                                                           |
| Bamboo Mosaic                             | 15<br/>300 ticks               | 1.5                           | 96                                                  | None used                     | $3\frac{1}{3}$               | $42\frac{2}{3}$                              |                                                                           |
| Bamboo Mosaic Slab                        | 7.5<br/>150 ticks              | 0.75                          | 48                                                  | 60                            | $3\frac{1}{3}$               | $85\frac{1}{3}$                              | ‌[Java Edition  only]                                                     |
|                                           | 15<br/>300 ticks<br/>[note 6]  | 1.5                           | 96                                                  | 120<br/>[note 6]              | $6\frac{2}{3}$<br/>[note 6]  | $42\frac{2}{3}$                              | ‌[Bedrock Edition  only]                                                  |
| Bamboo Mosaic Stairs                      | 15<br/>300 ticks               | 1.5                           | 96                                                  | None used                     | $3\frac{1}{3}$               | $42\frac{2}{3}$                              |                                                                           |
| Bee Nest                                  | 15<br/>300 ticks               | 1.5                           | 96                                                  | None used                     | None used                    | $42\frac{2}{3}$                              | ‌[Bedrock Edition  only]                                                  |
| Beehive                                   | 15<br/>300 ticks               | 1.5                           | 96                                                  | 10                            | $\frac{5}{9}$<br/>(0.5)      | $42\frac{2}{3}$                              | ‌[Bedrock Edition  only]                                                  |
| Chiseled Bookshelf                        | 15<br/>300 ticks               | 1.5                           | 96                                                  | $2\frac{13}{16}$<br/>(2.8125) | $\frac{4}{9}$<br/>(0.4)      | $42\frac{2}{3}$                              |                                                                           |
| Block of BambooorBlock of Stripped Bamboo | 15<br/>300 ticks               | 1.5                           | 96                                                  | None used                     | $1\frac{2}{3}$               | $42\frac{2}{3}$                              | ‌[Java Edition  only]                                                     |
| OverworldLogorStripped Log                | 15<br/>300 ticks               | 1.5                           | 96                                                  | 15                            | None used                    | $42\frac{2}{3}$                              |                                                                           |
| OverworldWoodorStripped Wood              | 15<br/>300 ticks               | 1.5                           | 96                                                  | 11.25                         | None used                    | $42\frac{2}{3}$                              |                                                                           |
| OverworldPlanks                           | 15<br/>300 ticks               | 1.5                           | 96                                                  | 60                            | $3\frac{1}{3}$               | $42\frac{2}{3}$                              |                                                                           |
| OverworldWooden Slab                      | 7.5<br/>150 ticks              | 0.75                          | 48                                                  | 60                            | $3\frac{1}{3}$               | $85\frac{1}{3}$                              | ‌[Java Edition  only]                                                     |
|                                           | 15<br/>300 ticks<br/>[note 6]  | 1.5                           | 96                                                  | 120<br/>[note 6]              | $6\frac{2}{3}$<br/>[note 6]  | $42\frac{2}{3}$                              | ‌[Bedrock Edition  only]                                                  |
| OverworldWooden Stairs                    | 15<br/>300 ticks               | 1.5                           | 96                                                  | 40                            | $2\frac{2}{9}$<br/>(2.2)     | $42\frac{2}{3}$                              |                                                                           |
| OverworldWooden Pressure Plate            | 15<br/>300 ticks               | 1.5                           | 96                                                  | 30                            | $1\frac{2}{3}$               | $42\frac{2}{3}$                              |                                                                           |
| OverworldWooden Button                    | 5<br/>100 ticks                | 0.5                           | 32                                                  | 20                            | $1\frac{1}{9}$<br/>(1.1)     | 128                                          | ‌[Java Edition  only]                                                     |
|                                           | 15<br/>300 ticks               | 1.5                           | 96                                                  | 60                            | $3\frac{1}{3}$               | $42\frac{2}{3}$                              | ‌[Bedrock Edition  only]                                                  |
| OverworldWooden Trapdoor                  | 15<br/>300 ticks               | 1.5                           | 96                                                  | 20                            | $1\frac{1}{9}$<br/>(1.1)     | $42\frac{2}{3}$                              |                                                                           |
| OverworldFence Gate                       | 15<br/>300 ticks               | 1.5                           | 96                                                  | 15                            | $\frac{15}{17}$<br/>(~0.88)  | $42\frac{2}{3}$                              |                                                                           |
| OverworldWooden Fence                     | 15<br/>300 ticks               | 1.5                           | 96                                                  | 36                            | $\frac{15}{22}$<br/>(0.681)  | $42\frac{2}{3}$                              |                                                                           |
| Mangrove Roots                            | 15<br/>300 ticks               | 1.5                           | 96                                                  | None used                     | None used                    | $42\frac{2}{3}$                              | ‌[Java Edition  only]                                                     |
| Ladder                                    | 15<br/>300 ticks               | 1.5                           | 96                                                  | $51\frac{3}{7}$<br/>(~51.43)  | $3\frac{3}{14}$<br/>(~3.21)  | $42\frac{2}{3}$                              | ‌[Java Edition  only]                                                     |
| Crafting Table                            | 15<br/>300 ticks               | 1.5                           | 96                                                  | 15                            | $\frac{5}{6}$<br/>(0.83)     | $42\frac{2}{3}$                              |                                                                           |
| Cartography Table                         | 15<br/>300 ticks               | 1.5                           | 96                                                  | 15                            | $\frac{5}{6}$<br/>(0.83)     | $42\frac{2}{3}$                              |                                                                           |
| Fletching Table                           | 15<br/>300 ticks               | 1.5                           | 96                                                  | 15                            | $\frac{5}{6}$<br/>(0.83)     | $42\frac{2}{3}$                              |                                                                           |
| Smithing Table                            | 15<br/>300 ticks               | 1.5                           | 96                                                  | 15                            | $\frac{5}{6}$<br/>(0.83)     | $42\frac{2}{3}$                              |                                                                           |
| Loom                                      | 15<br/>300 ticks               | 1.5                           | 96                                                  | 30                            | $1\frac{2}{3}$               | $42\frac{2}{3}$                              |                                                                           |
| Bookshelf                                 | 15<br/>300 ticks               | 1.5                           | 96                                                  | 10                            | $\frac{5}{9}$<br/>(0.5)      | $42\frac{2}{3}$                              |                                                                           |
| Lectern                                   | 15<br/>300 ticks               | 1.5                           | 96                                                  | 7.5                           | $\frac{5}{12}$<br/>(0.416)   | $42\frac{2}{3}$                              |                                                                           |
| Composter                                 | 15<br/>300 ticks               | 1.5                           | 96                                                  | $17\frac{1}{7}$<br/>(~17.14)  | $\frac{20}{21}$<br/>(~0.95)  | $42\frac{2}{3}$                              |                                                                           |
| Chest                                     | 15<br/>300 ticks               | 1.5                           | 96                                                  | 7.5                           | $\frac{5}{12}$<br/>(0.416)   | $42\frac{2}{3}$                              |                                                                           |
| Trapped Chest                             | 15<br/>300 ticks               | 1.5                           | 96                                                  | $6\frac{6}{7}$<br/>(~6.86)    | $\frac{60}{157}$<br/>(~0.38) | $42\frac{2}{3}$                              |                                                                           |
| Barrel                                    | 15<br/>300 ticks               | 1.5                           | 96                                                  | $8\frac{4}{7}$<br/>(~8.57)    | $\frac{10}{21}$<br/>(~0.48)  | $42\frac{2}{3}$                              |                                                                           |
| Daylight Detector                         | 15<br/>300 ticks               | 1.5                           | 96                                                  | 40                            | $2\frac{2}{9}$<br/>(2.2)     | $42\frac{2}{3}$                              |                                                                           |
| Jukebox                                   | 15<br/>300 ticks               | 1.5                           | 96                                                  | 7.5                           | $\frac{5}{12}$<br/>(0.416)   | $42\frac{2}{3}$                              |                                                                           |
| Note Block                                | 15<br/>300 ticks               | 1.5                           | 96                                                  | 7.5                           | $\frac{5}{12}$<br/>(0.416)   | $42\frac{2}{3}$                              |                                                                           |
| AnyBanner                                 | 15<br/>300 ticks               | 1.5                           | 24                                                  | 120                           | 7.5                          | $42\frac{2}{3}$                              |                                                                           |
| Crossbow                                  | 15<br/>300 ticks               | 1.5                           | 1.5                                                 | $26\frac{2}{3}$               | $1\frac{23}{37}$<br/>(1.621) | $42\frac{2}{3}$                              | ‌[Java Edition  only]                                                     |
|                                           | 10<br/>200 ticks               | 1                             | 1                                                   | $17\frac{7}{9}$<br/>(17.7)    | $1\frac{3}{37}$<br/>(1.081)  | 64                                           | ‌[Bedrock Edition  only]                                                  |
| Bow                                       | 15<br/>300 ticks               | 1.5                           | 1.5                                                 | 40                            | 2.5                          | $42\frac{2}{3}$                              | ‌[Java Edition  only]                                                     |
|                                           | 10<br/>200 ticks               | 1                             | 1                                                   | $26\frac{2}{3}$               | $1\frac{2}{3}$               | 64                                           | ‌[Bedrock Edition  only]                                                  |
| Fishing Rod                               | 15<br/>300 ticks               | 1.5                           | 1.5                                                 | 40                            | 2.5                          | $42\frac{2}{3}$                              |                                                                           |
| OverworldWooden Door                      | 10<br/>200 ticks               | 1                             | 64                                                  | 20                            | $1\frac{1}{9}$<br/>(1.1)     | 64                                           |                                                                           |
| OverworldSign                             | 10<br/>200 ticks               | 1                             | 16                                                  | $18\frac{6}{13}$<br/>(~18.46) | $\frac{10}{29}$<br/>(~0.34)  | 64                                           |                                                                           |
| OverworldHanging Sign                     | 10<br/>200 ticks               | 1                             | 16                                                  | 10                            | $1\frac{1}{9}$<br/>(1.1)     | 64                                           |                                                                           |
| Wooden Pickaxe                            | 10<br/>200 ticks               | 1                             | 1                                                   | 10                            | $\frac{4}{7}$<br/>(~0.57)    | 64                                           |                                                                           |
| Wooden Shovel                             | 10<br/>200 ticks               | 1                             | 1                                                   | 20                            | $1\frac{3}{17}$<br/>(~1.18)  | 64                                           |                                                                           |
| Wooden Hoe                                | 10<br/>200 ticks               | 1                             | 1                                                   | $13\frac{1}{3}$               | $\frac{10}{13}$<br/>(~0.77)  | 64                                           |                                                                           |
| Wooden Axe                                | 10<br/>200 ticks               | 1                             | 1                                                   | 10                            | $\frac{4}{7}$<br/>(~0.57)    | 64                                           |                                                                           |
| Wooden Sword                              | 10<br/>200 ticks               | 1                             | 1                                                   | 16                            | $\frac{10}{11}$<br/>(0.90)   | 64                                           |                                                                           |
| Bowl                                      | 5<br/>100 ticks                | 0.5                           | 32                                                  | $26\frac{2}{3}$               | $1\frac{13}{27}$<br/>(1.481) | 128                                          | ‌[Java Edition  only]                                                     |
|                                           | 10<br/>200 ticks               | 1                             | 64                                                  | $53\frac{1}{3}$               | $2\frac{26}{27}$<br/>(2.962) | 64                                           | ‌[Bedrock Edition  only]                                                  |
| AnySapling                                | 5<br/>100 ticks                | 0.5                           | 32                                                  | None used                     | None used                    | 128                                          |                                                                           |
| Stick                                     | 5<br/>100 ticks                | 0.5                           | 32                                                  | 40                            | 2.5                          | 128                                          |                                                                           |
| Dead Bush                                 | 5<br/>100 ticks                | 0.5                           | 32                                                  | None used                     | None used                    | 128                                          |                                                                           |
| Azalea                                    | 5<br/>100 ticks                | 0.5                           | 32                                                  | None used                     | None used                    | 128                                          |                                                                           |
| AnyWool                                   | 5<br/>100 ticks                | 0.5                           | 32                                                  | None used                     | None used                    | 128                                          | ‌[Java Edition  only]                                                     |
| Any WoolCarpet                            | 3.35<br/>67 ticks              | 0.335                         | 21.44                                               | None used                     | None used                    | $191\frac{3}{67}$<br/>(~191.04)              | ‌[Java Edition  only]                                                     |
| Bamboo                                    | 2.5<br/>50 ticks               | 0.25                          | 16                                                  | None used                     | 2.5                          | 256                                          |                                                                           |
| Scaffolding                               | 2.5<br/>50 ticks               | 0.25                          | 16                                                  | None used                     | 2.5                          | 256                                          |                                                                           |

1. ↑All times given are for fuel burned in a furnace. When burned in a blast furnace or smoker, fuel is burned twice as fast but produces the same number of items.
2. ↑Items in red are not stackable, items in yellow only stack up to 16.
3. ↑Calculated as the burning time in seconds divided by the number of logs used to make one fuel when all wood ingredients are made from logs. Items in red are not made entirely of wood.
4. ↑Calculated as the burning time in seconds divided by the amount of bamboo used to make one fuel when all wood ingredient are made from bamboo. Items in red are not made entirely of bamboo.
5. ↑80 seconds of fuel per log, but 10 seconds are needed to smelt the charcoal, so the net time is 70 seconds.
6. ↑ a b c d e fWooden slabs have the same burn time as planks due to a bug; see MCPE-94368.

## Hopper automation
See also: Tutorials/Hopper § Automatic smelting



















Automated furnace
The smelting process can be automated with hoppers on the top and bottom of the furnace. For larger smelting jobs, a third hopper on the side of the furnace can feed in fuel and, in case of lava being used as fuel, any empty buckets come out of the bottom hopper. This automatically feeds and empties the furnace so that different materials can be smelted in the same batch with no loss.

Whenever a hopper or minecart with hopper removes items from a furnace, any experience earned from cooking or smelting the removed items is saved in the furnace and awarded to the next player who manually removes an item from the furnace's output slot. This saved experience is in addition to that earned for the manually removed item(s).

