# Bedrock Edition 1.21.0
1.21.0 is an upcoming major update to Bedrock Edition scheduled to release sometime in mid-2024.[1] Originally announced at Minecraft Live 2023 on October 15, 2023, the update is said to focus on "combat, adventures, and tinkering". It includes several copper block variants, and trial chambers. It also includes the new crafter, new tuff block variants, and more enemies that spawn in the trial chambers. 

## Contents
- 1 Additions
	- 1.1 Gameplay
- 2 Changes
	- 2.1 Blocks
	- 2.2 General
	- 2.3 Technical
- 3 Experimental Additions
	- 3.1 Blocks
	- 3.2 Items
	- 3.3 Mobs
	- 3.4 Non-mob entities
	- 3.5 World generation
	- 3.6 Gameplay
	- 3.7 General
- 4 Experimental Changes
- 5 References

## Additions
### Gameplay
Game rule
- Added a new game rule to control decay of drops fromTNTexplosions, namedtntExplosionDropDecay.
	- The rule can be set totrueto re-enable the previous behavior where not all blocks would drop when exploded by TNT.

## Changes
### Blocks
Coral Block and Dead Coral Block
- The differentblock statesfor thecoral_blockID have now been split up into their own IDs.

| Old ID      | New ID                  |
|-------------|-------------------------|
| coral_block | tube_coral_block        |
|             | brain_coral_block       |
|             | bubble_coral_block      |
|             | fire_coral_block        |
|             | horn_coral_block        |
|             | dead_tube_coral_block   |
|             | dead_brain_coral_block  |
|             | dead_bubble_coral_block |
|             | dead_fire_coral_block   |
|             | dead_horn_coral_block   |

Grass and Fern
- The differentblock statesfor thetallgrassID have now been split up into their own IDs.

| Old ID    | New ID      |
|-----------|-------------|
| tallgrass | short_grass |
|           | fern        |

### General
Updated Edit World
- Screen/Export World or Export as Template if clear player data is set it will be applied in a copy and then exported. (Previewonly)

EDU Toggle
- Chemistry items now appear in thecreative inventorywhen the Education edition toggle is on.

Accessibility features
- Added text-to-speech support for member search results in the Realms Stories Member tab. (PreviewOnly)
- TheRealms StoriesOpt In screen now enumerates its active buttons with text-to-speech on. (PreviewOnly)

UI
- Added missing indentation to list items in some models, which should make those lists easier to read.
- On touch devices, when moving items between different slots, the icon no longer appears as duplicated between the moving item and the destination slot.
- On touch devices, when moving enchanted items between different slots, the moving icon is now rendered correctly.
- On touch devices, stack-splitting UI no longer appears for unstackable items.
- On touch devices, items from Creative Inventory are now unselectable.
- On touch devices, it is now possible to swap two identical items.
- Removed faulty hotbar scale setting for Pocket UI.
- Added slide-off persistence to new d-pad touch control scheme.
	- Changes positioning and scale of default new touch d-pad control scheme.
	- Also allows for moving the dpad closer to the hotbar when customizing touch controls.

### Technical
Bedrock Editor
- Released the version0.6.0.

API
- ScreenDisplay
	- MovedgetHiddenHudElements(): HudElements[]frombetato11.0.
	- MovedisForcedHidden(hudElement: HudElements): booleanfrombetato11.0.
	- MovedresetHudElements(): voidfrombetato11.0.
	- MovedsetHudVisibility(visible: HudVisibility, hudElements?: HudElements[]): voidfrombetato11.0.
	- MovedhideAllExcept(hudElements?: HudElements[]): voidfrombetato11.0.
- HudElement
	- MovedHudElementenumfrombetato11.0.
	- MovedHudElementsCountfrombetato11.0.
- HudVisibility
	- MovedHudVisibilityenumfrombetato11.0.
	- MovedHudVisibilityCountfrombetato11.0.
- MovedWeatherChangeBeforeEventfrombetato11.0.
- BlockPermutation
	- Removed functionclone.
- Creator Settings UI**Watchdog settings.
	- Increase script hang threshold.
	- Disable/Enable slow script warnings and adjust threshold.
	- Disable/Enable script spike warnings and adjust threshold.
	- RemoveddisableWatchdogmethod.
	- AddeddisableWatchdogTimingWarningsto disable spike and slow warnings per behavior pack.
- ReleasedItemEnchantableComponentfrombetato11.0.
- Released Enchantment APIs frombetato11.0.
	- interfaceEnchantment.
	- enumEnchantmentSlot.
	- classEnchantmentType.
	- classEnchantmentTypes.
- Added new interfaceEntityFilterwith many of the existing options fromEntityRaycastOptions.
- EntityRaycastOptionsnow inherits fromEntityFilter.
- EntityQueryOptionsnow inherits fromEntityFilter.
- Removed propertyblockFilter(and several others, now moved toEntityFilter) fromBlockRaycastOptions.
- BlockRaycastOptionsnow inherits fromBlockFilter.
- ReleasedBlockFilterto4.0.
- Releasedvolumefrombetatov1.11.0.;General
- Removedserver-authoritative-block-breakingfrom the defaultserver.properties.
- Removedserver-authoritative-soundfrom server.properties.;Graphical
- Changed the default Anti Aliasing setting to "2" instead of "4" for better performance with minimal visual degradation.

Blocks
- Updated block geometry to allow uv rotations.
	- This allows to rotate the specified uv rect in 90 degree increments before applying it to a block face.
	- Supported fromminecraft:geometryformat version 1.21.0 and up.
- Added pivot for scale in the Block Transformation Component.
- Added pivot for rotation in the Block Transformation Component.

Trial Spawners
- Added optionalequipment_loot_tableto the spawn data present inspawn_potentialsof Trial Spawner configs.
	- If present, rolled items from the specified loot table will be equipped to the mob that spawns.

Molang
- Added Molangstate_time -> numberfor animation controllers, which returns the time in seconds spent in the current controller state (inclusive of blend time). Requires "Upcoming Creator Features" experimental toggle.

UI
- On touch devices players can once again distribute a selected item stack over multiple slots by dragging it over them.

## Experimental Additions
These additions and changes are accessible by enabling the "Update 1.21" and "Beta APIs" experimental toggles.

### Blocks
 Crafter
- A newblockthat enables thecraftingofitemsand blocks viaredstone.


- The crafter ejects one crafted item at a time when powered by a new redstone pulse. Upon receiving this new pulse, the crafter ejects the result from the front face.
- All the result items will be ejected together when the output result has multiple type of items.
- Crafters can be oriented in any direction when placed.
- They have a unique user interface:
	- They have a 3×3 interactable crafting grid.
	- Their crafting grid slots are toggleable, meaning that the player can change the behavior of a slot by clicking or pressing on a slot with an empty hand.
	- A "toggled" slot cannot hold any items and therefore cannot have items placed into it by other blocks such ashoppersanddroppers.
	- Unlike thecrafting table, the slots display a preview of the crafted item which will be crafted and ejected on the next redstone pulse but cannot be manually taken out by the player.
	- The user interface is shared between all players interacting with them, meaning that multiple players can interact with them at the same time, similar tochestsand hoppers.
- They interact with other blocks in the following ways:
	- When read by aredstone comparator, the redstone signal strength is 0 to 9, where each non-empty or toggled slot adds 1 strength.
	- Hoppers can be used to both insert and pull items out of them.
	- Droppers can be used to insert items into them.
	- Moving items in from another block with ahopperor adropperprioritizes filling items into slots following these rules:
		- Crafters prioritize the first empty slot from left-to-right and top-to-bottom.
		- If there are no empty slots then crafters prioritize the smallest stack of the same item and pick the first if there are multiple.
		- If there is a toggled slot, it is skipped. The item will then be moved into thecontainer.
		- If the item cannot be moved, it is ejected into theworld.

 Heavy core
- A mysterious, dense block which can be combined with abreeze rodto craft amace.
- The heavy core block has a 8.3% chance of being rewarded when using aominous trial keyon aominous vaultin thetrial chambers.

 Ominous trial spawner
- A more powerful active phase of the trial spawner with unique challenges and rewards.
	- Provides a more challenging experience that advanced players can opt into for better rewards.
- If a trial spawner detects a player that has the Trial Omen effect, the spawner will become ominous if:
	- It is not in cooldown.
	- Or, it is in cooldown but was not ominous during its last activation.
		- Making it ominous this way will bypass the cooldown.
- While active, it will:
	- Glow blue instead of orange.
	- Emit soul flames instead of normal flames.
	- Very commonly spawns mobs with equipment if they can wear it.
		- The equipment these mobs wear have armor trims applied from the trial chambers.
		- Known issue: these mobs can currently drop their equipment on death, but they will not in the future.
	- Periodically spawn potions and projectiles on top of unsuspecting players and mobs.
		- Based on their location, spawners in an area will select a random set of projectiles to spawn.
		- These projectiles will always include a single type of lingering potion from a set of possible effects.
- Becoming ominous will despawn any existing mobs it spawned and reset its challenge.
	- It will stay ominous until it has been defeated and its cooldown has finished.
- When defeated, it will eject a different set of loot to normal trial spawners.

In Java Edition 1.21, each trial chambers trial spawner ominous contains 1 item stack,  with the following distribution: 




 Item 
  Stack Size  [A]
  Weight   [B]
  Chance   [C]
  Avg.per spawner   [D]
  Avg. # spawnersto defeat   [E]

Ominous Trial Key
133⁄11030.0%0.3003.3

Baked Potato
2–421⁄11019.1%0.5735.2

Steak
1–221⁄11019.1%0.2865.2

Golden Carrot
1–214⁄11012.7%0.1917.9

Rotten Flesh
1–47⁄1106.4%0.15915.7

Potion of Regeneration
17⁄1106.4%0.06415.7

Potion of Strength
17⁄1106.4%0.06415.7
{ "chestNames": [ "trial-chambers-trial-spawner-ominous" ], "gameVersion": "JavaUpcoming", "loot": { "trial-chambers-trial-spawner-ominous": { "poolsJava": [], "poolsBedrockUpcoming": [], "itemDataJava": [], "superheader": "[[Trial Chambers]]", "poolsJavaUpcoming": [ { "items": { "rotten-flesh": [ 1, 4, 7 ], "golden-carrot": [ 1, 2, 14 ], "ominous-trial-key": [ 1, 1, 33 ], "potion-of-regeneration": [ 1, 1, 7 ], "cooked-beef": [ 1, 2, 21 ], "potion-of-strength": [ 1, 1, 7 ], "baked-potato": [ 2, 4, 21 ] }, "rolls": [ 1, 1 ], "totalweight": 110 } ], "structure": "Trial Chambers", "container": "Trial ominous spawner", "itemDataJavaUpcoming": { "baked-potato": { "itemname": "baked-potato", "sizes": [ "2–4" ], "sortsize": [ 3 ], "sortweight": [ 21 ], "weights": [ "<sup>21</sup>&frasl;<sub>110</sub>" ], "avgamount": 0.5727272727272728, "chanceany": 0.19090909090909092 }, "golden-carrot": { "itemname": "golden-carrot", "sizes": [ "1–2" ], "sortsize": [ 1.5 ], "sortweight": [ 14 ], "weights": [ "<sup>14</sup>&frasl;<sub>110</sub>" ], "avgamount": 0.19090909090909092, "chanceany": 0.12727272727272732 }, "rotten-flesh": { "itemname": "rotten-flesh", "sizes": [ "1–4" ], "sortsize": [ 2.5 ], "sortweight": [ 7 ], "weights": [ "<sup>7</sup>&frasl;<sub>110</sub>" ], "avgamount": 0.1590909090909091, "chanceany": 0.0636363636363636 }, "potion-of-regeneration": { "sortsize": [ 1 ], "weights": [ "<sup>7</sup>&frasl;<sub>110</sub>" ], "chanceany": 0.0636363636363636, "sizes": [ 1 ], "sortweight": [ 7 ], "armor": 0, "material": 0, "avgamount": 0.06363636363636363, "itemname": "potion-of-regeneration" }, "cooked-beef": { "itemname": "cooked-beef", "sizes": [ "1–2" ], "sortsize": [ 1.5 ], "sortweight": [ 21 ], "weights": [ "<sup>21</sup>&frasl;<sub>110</sub>" ], "avgamount": 0.2863636363636364, "chanceany": 0.19090909090909092 }, "potion-of-strength": { "sortsize": [ 1 ], "weights": [ "<sup>7</sup>&frasl;<sub>110</sub>" ], "chanceany": 0.0636363636363636, "sizes": [ 1 ], "sortweight": [ 7 ], "armor": 0, "material": 0, "avgamount": 0.06363636363636363, "itemname": "potion-of-strength" }, "ominous-trial-key": { "itemname": "ominous-trial-key", "sizes": [ 1 ], "sortsize": [ 1 ], "sortweight": [ 33 ], "weights": [ "<sup>33</sup>&frasl;<sub>110</sub>" ], "avgamount": 0.3, "chanceany": 0.30000000000000004 } }, "allRollsJavaUpcoming": [ 1 ], "itemDataBedrock": [], "poolsBedrock": [], "allRollsBedrockUpcoming": [], "allRollsBedrock": [], "itemDataBedrockUpcoming": [], "chest_type": "ominous trial spawner", "header": "Ominous Spawner", "allRollsJava": [], "link": "[[trial chambers]] ominous spawner", "structID": "trial-chambers" } } }


↑ The size of stacks (or for unstackable items, number) of this item on any given roll.

↑ The weight of this item relative to other items in the pool.

↑ The odds of finding any of this item in a single chest.

↑ The number of items expected per chest, averaged over a large number of chests.

↑ The average number of chests the player should expect to search to find any of this item.



- Ominous trial keys have a 30% chance of ejecting from a defeated ominous trial spawner, replacing the usual 50% chance to eject trial keys.

 Ominous vault
- A variant of vaults that have a different texture and emit soul flames instead of normal flames.
- These can be found throughout thetrial chambersin harder to find places and require an ominous trial key to unlock.
- These vaults hold a more valuable set of rewards than the standard vaults unlocked by trial keys.
- Ominous vaults can provide some particularly valuable items.

In Java Edition 1.21, each trial chambers ominous vault contains  items drawn from 3 pools,  with the following distribution: 




 Item 
  Stack Size  [A]
  Weight   [B]
  Chance   [C]
  Avg.per container   [D]
  Avg. # containersto loot   [E]

1×
1–3×
1×
1×
1–3×
1×

Emerald
4–104–10—5⁄1325⁄15—54.9%4.9321.8

Wind Charge
8–128–12—4⁄1324⁄15—46.2%5.6362.2

Arrow of Slowness IV
4–124–12—3⁄1323⁄15—36.4%3.3822.7

Diamond
2–32–3—2⁄1322⁄15—25.5%0.7053.9

Nothing[F]
——1——3⁄1225.0%0.2504.0

Flow Armor Trim Smithing Template
——1——3⁄1225.0%0.2504.0

Enchanted Golden Apple
——1——3⁄1225.0%0.2504.0

Block of Emerald
1——24⁄132——18.2%0.1825.5

Flow Banner Pattern
——1——2⁄1216.7%0.1676.0

Ominous Bottle III - V[G]
11—1⁄1321⁄15—13.4%0.1417.5

Enchanted Crossbow[H]
1——16⁄132——12.1%0.1218.2

Block of Iron
1——16⁄132——12.1%0.1218.2

Golden Apple
1——16⁄132——12.1%0.1218.2

Enchanted Diamond Axe[I]
1——12⁄132——9.1%0.09111.0

Enchanted Diamond Chestplate[I]
1——12⁄132——9.1%0.09111.0

Heavy Core
——1——1⁄128.3%0.08312.0

Enchanted Book[J]
1——8⁄132——6.1%0.06116.5

Enchanted Book[K]
1——8⁄132——6.1%0.06116.5

Enchanted Book[L]
1——4⁄132——3.0%0.03033.0

Block of Diamond
1——1⁄132——0.8%0.008132.0
{ "chestNames": [ "trial-chambers-reward-ominous" ], "gameVersion": "JavaUpcoming", "loot": { "trial-chambers-reward-ominous": { "poolsJava": [], "poolsBedrockUpcoming": [], "itemDataJava": [], "display_name": "trial chambers ominous vault", "superheader": "[[Trial Chambers]]", "poolsJavaUpcoming": [ { "items": { "tipped-arrow-strong-slowness": [ 4, 12, 3 ], "diamond": [ 2, 3, 2 ], "level-enchanted-diamond-axe": [ 1, 1, 12 ], "enchanted-book-rnd-wind-charge": [ 1, 1, 4 ], "enchanted-book-rnd-breach-density": [ 1, 1, 8 ], "golden-apple": [ 1, 1, 16 ], "enchanted-book-rnd-trial-chambers": [ 1, 1, 8 ], "level-enchanted-diamond-chestplate-3": [ 1, 1, 12 ], "ominous-bottle-2": [ 1, 1, 1 ], "block-of-emerald": [ 1, 1, 24 ], "block-of-diamond": [ 1, 1, 1 ], "wind-charge": [ 8, 12, 4 ], "emerald": [ 4, 10, 5 ], "block-of-iron": [ 1, 1, 16 ], "level-enchanted-crossbow": [ 1, 1, 16 ] }, "rolls": [ 1, 1 ], "totalweight": 132 }, { "items": { "tipped-arrow-strong-slowness": [ 4, 12, 3 ], "diamond": [ 2, 3, 2 ], "wind-charge": [ 8, 12, 4 ], "emerald": [ 4, 10, 5 ], "ominous-bottle-2": [ 1, 1, 1 ] }, "rolls": [ 1, 3 ], "totalweight": 15 }, { "items": { "heavy-core": [ 1, 1, 1 ], "flow-armor-trim-smithing-template": [ 1, 1, 3 ], "enchanted-golden-apple": [ 1, 1, 3 ], "empty": [ 1, 1, 3 ], "flow-banner-pattern": [ 1, 1, 2 ] }, "rolls": [ 1, 1 ], "totalweight": 12 } ], "structure": "Trial Chambers", "container": "Ominous Vault", "itemDataJavaUpcoming": { "block-of-diamond": { "itemname": "block-of-diamond", "sizes": [ 1, "—", "—" ], "sortsize": [ 1, 0, 0 ], "sortweight": [ 1, 0, 0 ], "weights": [ "<sup>1</sup>&frasl;<sub>132</sub>", "—", "—" ], "avgamount": 0.007575757575757576, "chanceany": 0.007575757575757569 }, "heavy-core": { "itemname": "heavy-core", "sizes": [ "—", "—", 1 ], "sortsize": [ 0, 0, 1 ], "sortweight": [ 0, 0, 1 ], "weights": [ "—", "—", "<sup>1</sup>&frasl;<sub>12</sub>" ], "avgamount": 0.08333333333333333, "chanceany": 0.08333333333333337 }, "enchanted-book-rnd-wind-charge": { "itemname": "enchanted-book-rnd-wind-charge", "sizes": [ 1, "—", "—" ], "sortsize": [ 1, 0, 0 ], "sortweight": [ 4, 0, 0 ], "weights": [ "<sup>4</sup>&frasl;<sub>132</sub>", "—", "—" ], "avgamount": 0.030303030303030304, "chanceany": 0.030303030303030276 }, "ominous-bottle-2": { "itemname": "ominous-bottle-2", "sizes": [ 1, 1, "—" ], "sortsize": [ 1, 1, 0 ], "sortweight": [ 1, 1, 0 ], "weights": [ "<sup>1</sup>&frasl;<sub>132</sub>", "<sup>1</sup>&frasl;<sub>15</sub>", "—" ], "avgamount": 0.1409090909090909, "chanceany": 0.134115974560419 }, "block-of-emerald": { "itemname": "block-of-emerald", "sizes": [ 1, "—", "—" ], "sortsize": [ 1, 0, 0 ], "sortweight": [ 24, 0, 0 ], "weights": [ "<sup>24</sup>&frasl;<sub>132</sub>", "—", "—" ], "avgamount": 0.18181818181818182, "chanceany": 0.18181818181818177 }, "wind-charge": { "itemname": "wind-charge", "sizes": [ "8–12", "8–12", "—" ], "sortsize": [ 10, 10, 0 ], "sortweight": [ 4, 4, 0 ], "weights": [ "<sup>4</sup>&frasl;<sub>132</sub>", "<sup>4</sup>&frasl;<sub>15</sub>", "—" ], "avgamount": 5.636363636363636, "chanceany": 0.4616625514403292 }, "empty": { "sortsize": [ 0, 0, 1 ], "weights": [ "—", "—", "<sup>3</sup>&frasl;<sub>12</sub>" ], "chanceany": 0.25, "sizes": [ "—", "—", 1 ], "sortweight": [ 0, 0, 3 ], "armor": 0, "material": 0, "avgamount": 0.25, "itemname": "empty" }, "level-enchanted-crossbow": { "sortsize": [ 1, 0, 0 ], "weights": [ "<sup>16</sup>&frasl;<sub>132</sub>", "—", "—" ], "chanceany": 0.12121212121212122, "sizes": [ 1, "—", "—" ], "sortweight": [ 16, 0, 0 ], "armor": 0, "material": 0, "avgamount": 0.12121212121212122, "itemname": "level-enchanted-crossbow" }, "block-of-iron": { "sortsize": [ 1, 0, 0 ], "weights": [ "<sup>16</sup>&frasl;<sub>132</sub>", "—", "—" ], "chanceany": 0.12121212121212122, "sizes": [ 1, "—", "—" ], "sortweight": [ 16, 0, 0 ], "armor": 0, "material": 2, "avgamount": 0.12121212121212122, "itemname": "block-of-iron" }, "diamond": { "itemname": "diamond", "sizes": [ "2–3", "2–3", "—" ], "sortsize": [ 2.5, 2.5, 0 ], "sortweight": [ 2, 2, 0 ], "weights": [ "<sup>2</sup>&frasl;<sub>132</sub>", "<sup>2</sup>&frasl;<sub>15</sub>", "—" ], "avgamount": 0.7045454545454545, "chanceany": 0.2552113729891508 }, "level-enchanted-diamond-axe": { "sortsize": [ 1, 0, 0 ], "weights": [ "<sup>12</sup>&frasl;<sub>132</sub>", "—", "—" ], "chanceany": 0.09090909090909094, "sizes": [ 1, "—", "—" ], "sortweight": [ 12, 0, 0 ], "armor": 0, "material": 4, "avgamount": 0.09090909090909091, "itemname": "level-enchanted-diamond-axe" }, "golden-apple": { "sortsize": [ 1, 0, 0 ], "weights": [ "<sup>16</sup>&frasl;<sub>132</sub>", "—", "—" ], "chanceany": 0.12121212121212122, "sizes": [ 1, "—", "—" ], "sortweight": [ 16, 0, 0 ], "armor": 0, "material": 3, "avgamount": 0.12121212121212122, "itemname": "golden-apple" }, "level-enchanted-diamond-chestplate-3": { "sortsize": [ 1, 0, 0 ], "weights": [ "<sup>12</sup>&frasl;<sub>132</sub>", "—", "—" ], "chanceany": 0.09090909090909094, "sizes": [ 1, "—", "—" ], "sortweight": [ 12, 0, 0 ], "armor": 2, "material": 4, "avgamount": 0.09090909090909091, "itemname": "level-enchanted-diamond-chestplate-3" }, "flow-banner-pattern": { "itemname": "flow-banner-pattern", "sizes": [ "—", "—", 1 ], "sortsize": [ 0, 0, 1 ], "sortweight": [ 0, 0, 2 ], "weights": [ "—", "—", "<sup>2</sup>&frasl;<sub>12</sub>" ], "avgamount": 0.16666666666666666, "chanceany": 0.16666666666666663 }, "enchanted-golden-apple": { "sortsize": [ 0, 0, 1 ], "weights": [ "—", "—", "<sup>3</sup>&frasl;<sub>12</sub>" ], "chanceany": 0.25, "sizes": [ "—", "—", 1 ], "sortweight": [ 0, 0, 3 ], "armor": 0, "material": 3, "avgamount": 0.25, "itemname": "enchanted-golden-apple" }, "flow-armor-trim-smithing-template": { "sortsize": [ 0, 0, 1 ], "weights": [ "—", "—", "<sup>3</sup>&frasl;<sub>12</sub>" ], "chanceany": 0.25, "sizes": [ "—", "—", 1 ], "sortweight": [ 0, 0, 3 ], "armor": 0, "material": 0, "avgamount": 0.25, "itemname": "flow-armor-trim-smithing-template" }, "enchanted-book-rnd-trial-chambers": { "sortsize": [ 1, 0, 0 ], "weights": [ "<sup>8</sup>&frasl;<sub>132</sub>", "—", "—" ], "chanceany": 0.06060606060606055, "sizes": [ 1, "—", "—" ], "sortweight": [ 8, 0, 0 ], "armor": 0, "material": 0, "avgamount": 0.06060606060606061, "itemname": "enchanted-book-rnd-trial-chambers" }, "emerald": { "itemname": "emerald", "sizes": [ "4–10", "4–10", "—" ], "sortsize": [ 7, 7, 0 ], "sortweight": [ 5, 5, 0 ], "weights": [ "<sup>5</sup>&frasl;<sub>132</sub>", "<sup>5</sup>&frasl;<sub>15</sub>", "—" ], "avgamount": 4.931818181818182, "chanceany": 0.5486344930789375 }, "tipped-arrow-strong-slowness": { "itemname": "tipped-arrow-strong-slowness", "sizes": [ "4–12", "4–12", "—" ], "sortsize": [ 8, 8, 0 ], "sortweight": [ 3, 3, 0 ], "weights": [ "<sup>3</sup>&frasl;<sub>132</sub>", "<sup>3</sup>&frasl;<sub>15</sub>", "—" ], "avgamount": 3.381818181818182, "chanceany": 0.3641212121212122 }, "enchanted-book-rnd-breach-density": { "sortsize": [ 1, 0, 0 ], "weights": [ "<sup>8</sup>&frasl;<sub>132</sub>", "—", "—" ], "chanceany": 0.06060606060606055, "sizes": [ 1, "—", "—" ], "sortweight": [ 8, 0, 0 ], "armor": 0, "material": 0, "avgamount": 0.06060606060606061, "itemname": "enchanted-book-rnd-breach-density" } }, "allRollsJavaUpcoming": [ 1, "1–3", 1 ], "itemDataBedrock": [], "poolsBedrock": [], "allRollsBedrockUpcoming": [], "allRollsBedrock": [], "itemDataBedrockUpcoming": [], "chest_type": "reward-container", "header": "Ominous Vault", "allRollsJava": [], "link": "[[trial chambers]] ominous vault", "structID": "trial-chambers" } } }


↑ The size of stacks (or for unstackable items, number) of this item on any given roll.

↑ The weight of this item relative to other items in the pool.

↑ The odds of finding any of this item in a single chest.

↑ The number of items expected per chest, averaged over a large number of chests.

↑ The average number of chests the player should expect to search to find any of this item.

↑ 'Nothing' does not refer to the chance of an empty chest.  Instead, it refers to the chance that the random loot generator does not add any loot on a single roll.

↑ Ominous bottle level between III and V

↑ Enchantment probabilities are the same as a level-5 to level-20 enchantment would be on an enchantment table that was able to apply treasure enchantments (except Soul Speed, and Swift Sneak), and where the chance of multiple enchantments is not reduced.

↑ a b Enchantment probabilities are the same as a level-5 to level-15 enchantment would be on an enchantment table that was able to apply treasure enchantments (except Soul Speed, and Swift Sneak), and where the chance of multiple enchantments is not reduced.

↑ Enchanted with a random level of Breach, or Density.

↑ Enchanted with a random level of Sharpness, Bane of Arthropods, Efficiency, Fortune, Silk Touch, or Feather Falling.

↑ Enchanted with a random level of Wind Charge.



 Trial spawner
- Generates intrial chambers.
- The trial spawner is a new form ofspawnerthat ejects rewards upon completion and can have variable levels of challenge inmultiplayer.
- The challenge level will increase for each new player a trial spawner notices nearby.
	- Challenge level will not decrease until it is reset during a trial spawner's cooldown.
- Unlikemonster spawners, a trial spawner will spawn a limited number of mobs proportional to its current challenge level.
	- It can only spawn a mob at positions that are within line of sight.
	- It can spawn a mob regardless of any light level requirement the mob.
	- Spawned mobs are persistent.
- Once all mobs are defeated, the trial spawner will eject a set of rewards proportional to the current challenge level.
	- After the rewards have been ejected, the trial spawner goes into cooldown for 30 minutes during which it will no longer spawn mobs.

In Java Edition, each trial spawner contains 1 item stack,  with the following distribution: 




 Item 
  Stack Size  [A]
  Weight   [B]
  Chance   [C]
  Avg.per spawner   [D]
  Avg. # spawnersto defeat   [E]

Trial Key
113⁄2650.0%0.5002.0

Glow Berries
2–103⁄2611.5%0.6928.7

Emerald
1–63⁄2611.5%0.4048.7

Baked Potato
1–33⁄2611.5%0.2318.7

Golden Carrot
1–31⁄263.8%0.07726.0

Ender Pearl
11⁄263.8%0.03826.0

Potion of Regeneration
11⁄263.8%0.03826.0

Potion of Strength
11⁄263.8%0.03826.0
{ "chestNames": [ "trial-chambers-trial-spawner" ], "gameVersion": "Java", "loot": { "trial-chambers-trial-spawner": { "poolsJava": [ { "items": { "baked-potato": [ 1, 3, 3 ], "ender-pearl": [ 1, 1, 1 ], "golden-carrot": [ 1, 3, 1 ], "potion-of-regeneration": [ 1, 1, 1 ], "glow-berries": [ 2, 10, 3 ], "emerald": [ 1, 6, 3 ], "potion-of-strength": [ 1, 1, 1 ], "trial-key": [ 1, 1, 13 ] }, "rolls": [ 1, 1 ], "totalweight": 26 } ], "poolsBedrockUpcoming": [], "itemDataJava": { "ender-pearl": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>26</sub>" ], "chanceany": 0.038461538461538436, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.038461538461538464, "itemname": "ender-pearl" }, "glow-berries": { "itemname": "glow-berries", "sizes": [ "2–10" ], "sortsize": [ 6 ], "sortweight": [ 3 ], "weights": [ "<sup>3</sup>&frasl;<sub>26</sub>" ], "avgamount": 0.6923076923076923, "chanceany": 0.11538461538461542 }, "golden-carrot": { "itemname": "golden-carrot", "sizes": [ "1–3" ], "sortsize": [ 2 ], "sortweight": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>26</sub>" ], "avgamount": 0.07692307692307693, "chanceany": 0.038461538461538436 }, "emerald": { "itemname": "emerald", "sizes": [ "1–6" ], "sortsize": [ 3.5 ], "sortweight": [ 3 ], "weights": [ "<sup>3</sup>&frasl;<sub>26</sub>" ], "avgamount": 0.40384615384615385, "chanceany": 0.11538461538461542 }, "potion-of-regeneration": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>26</sub>" ], "chanceany": 0.038461538461538436, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.038461538461538464, "itemname": "potion-of-regeneration" }, "baked-potato": { "itemname": "baked-potato", "sizes": [ "1–3" ], "sortsize": [ 2 ], "sortweight": [ 3 ], "weights": [ "<sup>3</sup>&frasl;<sub>26</sub>" ], "avgamount": 0.23076923076923078, "chanceany": 0.11538461538461542 }, "potion-of-strength": { "sortsize": [ 1 ], "weights": [ "<sup>1</sup>&frasl;<sub>26</sub>" ], "chanceany": 0.038461538461538436, "sizes": [ 1 ], "sortweight": [ 1 ], "armor": 0, "material": 0, "avgamount": 0.038461538461538464, "itemname": "potion-of-strength" }, "trial-key": { "itemname": "trial-key", "sizes": [ 1 ], "sortsize": [ 1 ], "sortweight": [ 13 ], "weights": [ "<sup>13</sup>&frasl;<sub>26</sub>" ], "avgamount": 0.5, "chanceany": 0.5 } }, "display_name": "trial spawner", "superheader": "[[Trial Chambers]]", "poolsJavaUpcoming": [], "structure": "Trial Chambers", "container": "Trial spawner", "itemDataJavaUpcoming": [], "allRollsJavaUpcoming": [], "itemDataBedrock": [], "poolsBedrock": [], "allRollsBedrockUpcoming": [], "allRollsBedrock": [], "itemDataBedrockUpcoming": [], "chest_type": "trial spawner", "header": "Spawner", "allRollsJava": [ 1 ], "link": "[[trial chambers]] spawner", "structID": "trial-chambers" } } }


↑ The size of stacks (or for unstackable items, number) of this item on any given roll.

↑ The weight of this item relative to other items in the pool.

↑ The odds of finding any of this item in a single chest.

↑ The number of items expected per chest, averaged over a large number of chests.

↑ The average number of chests the player should expect to search to find any of this item.



- Trial spawners cannot be crafted nor obtained by players inSurvival- instead, they can be found naturally placed throughouttrial chambers.
- Trial spawners are extremely slow to mine and resistant to explosions, and will not drop even withSilk Touch.
- When placed inCreative, trial spawners have no mob type set by default.
	- The mob type can be set by interacting with it while holding aspawn egg.
- Players in Creative orSpectatormode are not detected or noticed by trial spawners.

 Vault
- Can be found in thetrial chambers.
- Can be unlocked with atrial key.
- Eachplayercan open the vault only once to get a reward.

In Java Edition and Bedrock Edition, each trial chambers reward container contains  items drawn from 3 pools,  with the following distribution: 




 Item 
  Stack Size  [A]
  Weight   [B]
  Chance   [C]
  Avg.per container   [D]
  Avg. # containersto loot   [E]

1×
1–3×
1×
1×
1–3×
1×

Nothing[F]
——1——36⁄4875.0%0.7501.3

Emerald
2–42–4—12⁄1104⁄22—39.6%1.4182.5

Arrow
2–82–8—4⁄1104⁄22—34.6%2.0002.9

Arrow of Poison
2–82–8—4⁄1104⁄22—34.6%2.0002.9

Iron Ingot
1–41–4—3⁄1103⁄22—26.9%0.7503.7

Honey Bottle
1–21–2—3⁄1103⁄22—26.9%0.4503.7

Ominous Bottle I - II[G]
11—2⁄1102⁄22—18.6%0.2005.4

Golden Apple
——1——6⁄4812.5%0.1258.0

Damaged Shield[H]
1——12⁄110——10.9%0.1099.2

Enchanted Bow[I]
1——12⁄110——10.9%0.1099.2

Wind Charge
4–124–12—1⁄1101⁄22—9.6%0.80010.4

Diamond
1–21–2—1⁄1101⁄22—9.6%0.15010.4

Golden Carrot
1–2——8⁄110——7.3%0.10913.7

Enchanted Book[J]
1——8⁄110——7.3%0.07313.7

Enchanted Book[K]
1——8⁄110——7.3%0.07313.7

Enchanted Crossbow[L]
1——8⁄110——7.3%0.07313.7

Enchanted Iron Axe[I]
1——8⁄110——7.3%0.07313.7

Enchanted Iron Chestplate[I]
1——8⁄110——7.3%0.07313.7

Bolt Armor Trim Smithing Template
——1——3⁄486.2%0.06216.0

Guster Banner Pattern
——1——2⁄484.2%0.04224.0

Enchanted Diamond Axe[I]
1——4⁄110——3.6%0.03627.5

Enchanted Diamond Chestplate[I]
1——4⁄110——3.6%0.03627.5

Trident
——1——1⁄482.1%0.02148.0
{ "chestNames": [ "trial-chambers-reward" ], "gameVersion": "Java", "loot": { "trial-chambers-reward": { "poolsJava": [ { "items": { "damaged-shield": [ 1, 1, 12 ], "arrow": [ 2, 8, 4 ], "tipped-arrow-poison": [ 2, 8, 4 ], "level-enchanted-iron-axe": [ 1, 1, 8 ], "wind-charge": [ 4, 12, 1 ], "iron-ingot": [ 1, 4, 3 ], "level-enchanted-crossbow": [ 1, 1, 8 ], "diamond": [ 1, 2, 1 ], "golden-carrot": [ 1, 2, 8 ], "level-enchanted-iron-chestplate-3": [ 1, 1, 8 ], "level-enchanted-bow-2": [ 1, 1, 12 ], "ominous-bottle": [ 1, 1, 2 ], "level-enchanted-diamond-chestplate-3": [ 1, 1, 4 ], "level-enchanted-diamond-axe": [ 1, 1, 4 ], "enchanted-book-rnd-trial-chambers": [ 1, 1, 8 ], "emerald": [ 2, 4, 12 ], "enchanted-book-rnd-mending-trident": [ 1, 1, 8 ], "honey-bottle": [ 1, 2, 3 ] }, "rolls": [ 1, 1 ], "totalweight": 110 }, { "items": { "diamond": [ 1, 2, 1 ], "arrow": [ 2, 8, 4 ], "tipped-arrow-poison": [ 2, 8, 4 ], "ominous-bottle": [ 1, 1, 2 ], "wind-charge": [ 4, 12, 1 ], "emerald": [ 2, 4, 4 ], "honey-bottle": [ 1, 2, 3 ], "iron-ingot": [ 1, 4, 3 ] }, "rolls": [ 1, 3 ], "totalweight": 22 }, { "items": { "trident": [ 1, 1, 1 ], "bolt-armor-trim-smithing-template": [ 1, 1, 3 ], "empty": [ 1, 1, 36 ], "golden-apple": [ 1, 1, 6 ], "guster-banner-pattern": [ 1, 1, 2 ] }, "rolls": [ 1, 1 ], "totalweight": 48 } ], "poolsBedrockUpcoming": [], "itemDataJava": { "damaged-shield": { "sortsize": [ 1, 0, 0 ], "weights": [ "<sup>12</sup>&frasl;<sub>110</sub>", "—", "—" ], "chanceany": 0.10909090909090913, "sizes": [ 1, "—", "—" ], "sortweight": [ 12, 0, 0 ], "armor": 0, "material": 0, "avgamount": 0.10909090909090909, "itemname": "damaged-shield" }, "arrow": { "sortsize": [ 5, 5, 0 ], "weights": [ "<sup>4</sup>&frasl;<sub>110</sub>", "<sup>4</sup>&frasl;<sub>22</sub>", "—" ], "chanceany": 0.3462331807936616, "sizes": [ "2–8", "2–8", "—" ], "sortweight": [ 4, 4, 0 ], "armor": 0, "material": 0, "avgamount": 2, "itemname": "arrow" }, "tipped-arrow-poison": { "sortsize": [ 5, 5, 0 ], "weights": [ "<sup>4</sup>&frasl;<sub>110</sub>", "<sup>4</sup>&frasl;<sub>22</sub>", "—" ], "chanceany": 0.3462331807936616, "sizes": [ "2–8", "2–8", "—" ], "sortweight": [ 4, 4, 0 ], "armor": 0, "material": 0, "avgamount": 2, "itemname": "tipped-arrow-poison" }, "level-enchanted-iron-axe": { "sortsize": [ 1, 0, 0 ], "weights": [ "<sup>8</sup>&frasl;<sub>110</sub>", "—", "—" ], "chanceany": 0.07272727272727275, "sizes": [ 1, "—", "—" ], "sortweight": [ 8, 0, 0 ], "armor": 0, "material": 2, "avgamount": 0.07272727272727272, "itemname": "level-enchanted-iron-axe" }, "wind-charge": { "itemname": "wind-charge", "sizes": [ "4–12", "4–12", "—" ], "sortsize": [ 8, 8, 0 ], "sortweight": [ 1, 1, 0 ], "weights": [ "<sup>1</sup>&frasl;<sub>110</sub>", "<sup>1</sup>&frasl;<sub>22</sub>", "—" ], "avgamount": 0.8, "chanceany": 0.09647479680349696 }, "iron-ingot": { "itemname": "iron-ingot", "sizes": [ "1–4", "1–4", "—" ], "sortsize": [ 2.5, 2.5, 0 ], "sortweight": [ 3, 3, 0 ], "weights": [ "<sup>3</sup>&frasl;<sub>110</sub>", "<sup>3</sup>&frasl;<sub>22</sub>", "—" ], "avgamount": 0.75, "chanceany": 0.2692669558090294 }, "level-enchanted-crossbow": { "sortsize": [ 1, 0, 0 ], "weights": [ "<sup>8</sup>&frasl;<sub>110</sub>", "—", "—" ], "chanceany": 0.07272727272727275, "sizes": [ 1, "—", "—" ], "sortweight": [ 8, 0, 0 ], "armor": 0, "material": 0, "avgamount": 0.07272727272727272, "itemname": "level-enchanted-crossbow" }, "ominous-bottle": { "sortsize": [ 1, 1, 0 ], "weights": [ "<sup>2</sup>&frasl;<sub>110</sub>", "<sup>2</sup>&frasl;<sub>22</sub>", "—" ], "chanceany": 0.18612116658698177, "sizes": [ 1, 1, "—" ], "sortweight": [ 2, 2, 0 ], "armor": 0, "material": 0, "avgamount": 0.2, "itemname": "ominous-bottle" }, "diamond": { "sortsize": [ 1.5, 1.5, 0 ], "weights": [ "<sup>1</sup>&frasl;<sub>110</sub>", "<sup>1</sup>&frasl;<sub>22</sub>", "—" ], "chanceany": 0.09647479680349696, "sizes": [ "1–2", "1–2", "—" ], "sortweight": [ 1, 1, 0 ], "armor": 0, "material": 4, "avgamount": 0.15, "itemname": "diamond" }, "golden-carrot": { "itemname": "golden-carrot", "sizes": [ "1–2", "—", "—" ], "sortsize": [ 1.5, 0, 0 ], "sortweight": [ 8, 0, 0 ], "weights": [ "<sup>8</sup>&frasl;<sub>110</sub>", "—", "—" ], "avgamount": 0.10909090909090909, "chanceany": 0.07272727272727275 }, "level-enchanted-iron-chestplate-3": { "sortsize": [ 1, 0, 0 ], "weights": [ "<sup>8</sup>&frasl;<sub>110</sub>", "—", "—" ], "chanceany": 0.07272727272727275, "sizes": [ 1, "—", "—" ], "sortweight": [ 8, 0, 0 ], "armor": 2, "material": 2, "avgamount": 0.07272727272727272, "itemname": "level-enchanted-iron-chestplate-3" }, "golden-apple": { "itemname": "golden-apple", "sizes": [ "—", "—", 1 ], "sortsize": [ 0, 0, 1 ], "sortweight": [ 0, 0, 6 ], "weights": [ "—", "—", "<sup>6</sup>&frasl;<sub>48</sub>" ], "avgamount": 0.125, "chanceany": 0.125 }, "level-enchanted-bow-2": { "sortsize": [ 1, 0, 0 ], "weights": [ "<sup>12</sup>&frasl;<sub>110</sub>", "—", "—" ], "chanceany": 0.10909090909090913, "sizes": [ 1, "—", "—" ], "sortweight": [ 12, 0, 0 ], "armor": 0, "material": 0, "avgamount": 0.10909090909090909, "itemname": "level-enchanted-bow-2" }, "bolt-armor-trim-smithing-template": { "itemname": "bolt-armor-trim-smithing-template", "sizes": [ "—", "—", 1 ], "sortsize": [ 0, 0, 1 ], "sortweight": [ 0, 0, 3 ], "weights": [ "—", "—", "<sup>3</sup>&frasl;<sub>48</sub>" ], "avgamount": 0.0625, "chanceany": 0.0625 }, "empty": { "itemname": "empty", "sizes": [ "—", "—", 1 ], "sortsize": [ 0, 0, 1 ], "sortweight": [ 0, 0, 36 ], "weights": [ "—", "—", "<sup>36</sup>&frasl;<sub>48</sub>" ], "avgamount": 0.75, "chanceany": 0.75 }, "level-enchanted-diamond-chestplate-3": { "sortsize": [ 1, 0, 0 ], "weights": [ "<sup>4</sup>&frasl;<sub>110</sub>", "—", "—" ], "chanceany": 0.036363636363636376, "sizes": [ 1, "—", "—" ], "sortweight": [ 4, 0, 0 ], "armor": 2, "material": 4, "avgamount": 0.03636363636363636, "itemname": "level-enchanted-diamond-chestplate-3" }, "trident": { "itemname": "trident", "sizes": [ "—", "—", 1 ], "sortsize": [ 0, 0, 1 ], "sortweight": [ 0, 0, 1 ], "weights": [ "—", "—", "<sup>1</sup>&frasl;<sub>48</sub>" ], "avgamount": 0.020833333333333332, "chanceany": 0.02083333333333337 }, "honey-bottle": { "itemname": "honey-bottle", "sizes": [ "1–2", "1–2", "—" ], "sortsize": [ 1.5, 1.5, 0 ], "sortweight": [ 3, 3, 0 ], "weights": [ "<sup>3</sup>&frasl;<sub>110</sub>", "<sup>3</sup>&frasl;<sub>22</sub>", "—" ], "avgamount": 0.45, "chanceany": 0.2692669558090294 }, "enchanted-book-rnd-mending-trident": { "sortsize": [ 1, 0, 0 ], "weights": [ "<sup>8</sup>&frasl;<sub>110</sub>", "—", "—" ], "chanceany": 0.07272727272727275, "sizes": [ 1, "—", "—" ], "sortweight": [ 8, 0, 0 ], "armor": 0, "material": 0, "avgamount": 0.07272727272727272, "itemname": "enchanted-book-rnd-mending-trident" }, "enchanted-book-rnd-trial-chambers": { "sortsize": [ 1, 0, 0 ], "weights": [ "<sup>8</sup>&frasl;<sub>110</sub>", "—", "—" ], "chanceany": 0.07272727272727275, "sizes": [ 1, "—", "—" ], "sortweight": [ 8, 0, 0 ], "armor": 0, "material": 0, "avgamount": 0.07272727272727272, "itemname": "enchanted-book-rnd-trial-chambers" }, "emerald": { "itemname": "emerald", "sizes": [ "2–4", "2–4", "—" ], "sortsize": [ 3, 3, 0 ], "sortweight": [ 12, 4, 0 ], "weights": [ "<sup>12</sup>&frasl;<sub>110</sub>", "<sup>4</sup>&frasl;<sub>22</sub>", "—" ], "avgamount": 1.418181818181818, "chanceany": 0.39557407280923435 }, "level-enchanted-diamond-axe": { "sortsize": [ 1, 0, 0 ], "weights": [ "<sup>4</sup>&frasl;<sub>110</sub>", "—", "—" ], "chanceany": 0.036363636363636376, "sizes": [ 1, "—", "—" ], "sortweight": [ 4, 0, 0 ], "armor": 0, "material": 4, "avgamount": 0.03636363636363636, "itemname": "level-enchanted-diamond-axe" }, "guster-banner-pattern": { "itemname": "guster-banner-pattern", "sizes": [ "—", "—", 1 ], "sortsize": [ 0, 0, 1 ], "sortweight": [ 0, 0, 2 ], "weights": [ "—", "—", "<sup>2</sup>&frasl;<sub>48</sub>" ], "avgamount": 0.041666666666666664, "chanceany": 0.04166666666666663 } }, "display_name": "trial chambers reward container", "superheader": "[[Trial Chambers]]", "poolsJavaUpcoming": [], "structure": "Trial Chambers", "container": "Reward container", "itemDataJavaUpcoming": [], "allRollsJavaUpcoming": [], "itemDataBedrock": { "damaged-shield": { "sortsize": [ 1, 0, 0 ], "weights": [ "<sup>12</sup>&frasl;<sub>110</sub>", "—", "—" ], "chanceany": 0.10909090909090913, "sizes": [ 1, "—", "—" ], "sortweight": [ 12, 0, 0 ], "armor": 0, "material": 0, "avgamount": 0.10909090909090909, "itemname": "damaged-shield" }, "arrow": { "sortsize": [ 5, 5, 0 ], "weights": [ "<sup>4</sup>&frasl;<sub>110</sub>", "<sup>4</sup>&frasl;<sub>22</sub>", "—" ], "chanceany": 0.3462331807936616, "sizes": [ "2–8", "2–8", "—" ], "sortweight": [ 4, 4, 0 ], "armor": 0, "material": 0, "avgamount": 2, "itemname": "arrow" }, "tipped-arrow-poison": { "sortsize": [ 5, 5, 0 ], "weights": [ "<sup>4</sup>&frasl;<sub>110</sub>", "<sup>4</sup>&frasl;<sub>22</sub>", "—" ], "chanceany": 0.3462331807936616, "sizes": [ "2–8", "2–8", "—" ], "sortweight": [ 4, 4, 0 ], "armor": 0, "material": 0, "avgamount": 2, "itemname": "tipped-arrow-poison" }, "level-enchanted-iron-axe": { "sortsize": [ 1, 0, 0 ], "weights": [ "<sup>8</sup>&frasl;<sub>110</sub>", "—", "—" ], "chanceany": 0.07272727272727275, "sizes": [ 1, "—", "—" ], "sortweight": [ 8, 0, 0 ], "armor": 0, "material": 2, "avgamount": 0.07272727272727272, "itemname": "level-enchanted-iron-axe" }, "wind-charge": { "itemname": "wind-charge", "sizes": [ "4–12", "4–12", "—" ], "sortsize": [ 8, 8, 0 ], "sortweight": [ 1, 1, 0 ], "weights": [ "<sup>1</sup>&frasl;<sub>110</sub>", "<sup>1</sup>&frasl;<sub>22</sub>", "—" ], "avgamount": 0.8, "chanceany": 0.09647479680349696 }, "iron-ingot": { "itemname": "iron-ingot", "sizes": [ "1–4", "1–4", "—" ], "sortsize": [ 2.5, 2.5, 0 ], "sortweight": [ 3, 3, 0 ], "weights": [ "<sup>3</sup>&frasl;<sub>110</sub>", "<sup>3</sup>&frasl;<sub>22</sub>", "—" ], "avgamount": 0.75, "chanceany": 0.2692669558090294 }, "level-enchanted-crossbow": { "sortsize": [ 1, 0, 0 ], "weights": [ "<sup>8</sup>&frasl;<sub>110</sub>", "—", "—" ], "chanceany": 0.07272727272727275, "sizes": [ 1, "—", "—" ], "sortweight": [ 8, 0, 0 ], "armor": 0, "material": 0, "avgamount": 0.07272727272727272, "itemname": "level-enchanted-crossbow" }, "ominous-bottle": { "sortsize": [ 1, 1, 0 ], "weights": [ "<sup>2</sup>&frasl;<sub>110</sub>", "<sup>2</sup>&frasl;<sub>22</sub>", "—" ], "chanceany": 0.18612116658698177, "sizes": [ 1, 1, "—" ], "sortweight": [ 2, 2, 0 ], "armor": 0, "material": 0, "avgamount": 0.2, "itemname": "ominous-bottle" }, "diamond": { "sortsize": [ 1.5, 1.5, 0 ], "weights": [ "<sup>1</sup>&frasl;<sub>110</sub>", "<sup>1</sup>&frasl;<sub>22</sub>", "—" ], "chanceany": 0.09647479680349696, "sizes": [ "1–2", "1–2", "—" ], "sortweight": [ 1, 1, 0 ], "armor": 0, "material": 4, "avgamount": 0.15, "itemname": "diamond" }, "golden-carrot": { "itemname": "golden-carrot", "sizes": [ "1–2", "—", "—" ], "sortsize": [ 1.5, 0, 0 ], "sortweight": [ 8, 0, 0 ], "weights": [ "<sup>8</sup>&frasl;<sub>110</sub>", "—", "—" ], "avgamount": 0.10909090909090909, "chanceany": 0.07272727272727275 }, "level-enchanted-iron-chestplate-3": { "sortsize": [ 1, 0, 0 ], "weights": [ "<sup>8</sup>&frasl;<sub>110</sub>", "—", "—" ], "chanceany": 0.07272727272727275, "sizes": [ 1, "—", "—" ], "sortweight": [ 8, 0, 0 ], "armor": 2, "material": 2, "avgamount": 0.07272727272727272, "itemname": "level-enchanted-iron-chestplate-3" }, "golden-apple": { "itemname": "golden-apple", "sizes": [ "—", "—", 1 ], "sortsize": [ 0, 0, 1 ], "sortweight": [ 0, 0, 6 ], "weights": [ "—", "—", "<sup>6</sup>&frasl;<sub>48</sub>" ], "avgamount": 0.125, "chanceany": 0.125 }, "level-enchanted-bow-2": { "sortsize": [ 1, 0, 0 ], "weights": [ "<sup>12</sup>&frasl;<sub>110</sub>", "—", "—" ], "chanceany": 0.10909090909090913, "sizes": [ 1, "—", "—" ], "sortweight": [ 12, 0, 0 ], "armor": 0, "material": 0, "avgamount": 0.10909090909090909, "itemname": "level-enchanted-bow-2" }, "bolt-armor-trim-smithing-template": { "itemname": "bolt-armor-trim-smithing-template", "sizes": [ "—", "—", 1 ], "sortsize": [ 0, 0, 1 ], "sortweight": [ 0, 0, 3 ], "weights": [ "—", "—", "<sup>3</sup>&frasl;<sub>48</sub>" ], "avgamount": 0.0625, "chanceany": 0.0625 }, "empty": { "itemname": "empty", "sizes": [ "—", "—", 1 ], "sortsize": [ 0, 0, 1 ], "sortweight": [ 0, 0, 36 ], "weights": [ "—", "—", "<sup>36</sup>&frasl;<sub>48</sub>" ], "avgamount": 0.75, "chanceany": 0.75 }, "level-enchanted-diamond-chestplate-3": { "sortsize": [ 1, 0, 0 ], "weights": [ "<sup>4</sup>&frasl;<sub>110</sub>", "—", "—" ], "chanceany": 0.036363636363636376, "sizes": [ 1, "—", "—" ], "sortweight": [ 4, 0, 0 ], "armor": 2, "material": 4, "avgamount": 0.03636363636363636, "itemname": "level-enchanted-diamond-chestplate-3" }, "trident": { "itemname": "trident", "sizes": [ "—", "—", 1 ], "sortsize": [ 0, 0, 1 ], "sortweight": [ 0, 0, 1 ], "weights": [ "—", "—", "<sup>1</sup>&frasl;<sub>48</sub>" ], "avgamount": 0.020833333333333332, "chanceany": 0.02083333333333337 }, "honey-bottle": { "itemname": "honey-bottle", "sizes": [ "1–2", "1–2", "—" ], "sortsize": [ 1.5, 1.5, 0 ], "sortweight": [ 3, 3, 0 ], "weights": [ "<sup>3</sup>&frasl;<sub>110</sub>", "<sup>3</sup>&frasl;<sub>22</sub>", "—" ], "avgamount": 0.45, "chanceany": 0.2692669558090294 }, "enchanted-book-rnd-mending-trident": { "sortsize": [ 1, 0, 0 ], "weights": [ "<sup>8</sup>&frasl;<sub>110</sub>", "—", "—" ], "chanceany": 0.07272727272727275, "sizes": [ 1, "—", "—" ], "sortweight": [ 8, 0, 0 ], "armor": 0, "material": 0, "avgamount": 0.07272727272727272, "itemname": "enchanted-book-rnd-mending-trident" }, "enchanted-book-rnd-trial-chambers": { "sortsize": [ 1, 0, 0 ], "weights": [ "<sup>8</sup>&frasl;<sub>110</sub>", "—", "—" ], "chanceany": 0.07272727272727275, "sizes": [ 1, "—", "—" ], "sortweight": [ 8, 0, 0 ], "armor": 0, "material": 0, "avgamount": 0.07272727272727272, "itemname": "enchanted-book-rnd-trial-chambers" }, "emerald": { "itemname": "emerald", "sizes": [ "2–4", "2–4", "—" ], "sortsize": [ 3, 3, 0 ], "sortweight": [ 12, 4, 0 ], "weights": [ "<sup>12</sup>&frasl;<sub>110</sub>", "<sup>4</sup>&frasl;<sub>22</sub>", "—" ], "avgamount": 1.418181818181818, "chanceany": 0.39557407280923435 }, "level-enchanted-diamond-axe": { "sortsize": [ 1, 0, 0 ], "weights": [ "<sup>4</sup>&frasl;<sub>110</sub>", "—", "—" ], "chanceany": 0.036363636363636376, "sizes": [ 1, "—", "—" ], "sortweight": [ 4, 0, 0 ], "armor": 0, "material": 4, "avgamount": 0.03636363636363636, "itemname": "level-enchanted-diamond-axe" }, "guster-banner-pattern": { "itemname": "guster-banner-pattern", "sizes": [ "—", "—", 1 ], "sortsize": [ 0, 0, 1 ], "sortweight": [ 0, 0, 2 ], "weights": [ "—", "—", "<sup>2</sup>&frasl;<sub>48</sub>" ], "avgamount": 0.041666666666666664, "chanceany": 0.04166666666666663 } }, "poolsBedrock": [ { "items": { "damaged-shield": [ 1, 1, 12 ], "arrow": [ 2, 8, 4 ], "tipped-arrow-poison": [ 2, 8, 4 ], "level-enchanted-iron-axe": [ 1, 1, 8 ], "wind-charge": [ 4, 12, 1 ], "iron-ingot": [ 1, 4, 3 ], "level-enchanted-crossbow": [ 1, 1, 8 ], "diamond": [ 1, 2, 1 ], "golden-carrot": [ 1, 2, 8 ], "level-enchanted-iron-chestplate-3": [ 1, 1, 8 ], "level-enchanted-bow-2": [ 1, 1, 12 ], "ominous-bottle": [ 1, 1, 2 ], "level-enchanted-diamond-chestplate-3": [ 1, 1, 4 ], "level-enchanted-diamond-axe": [ 1, 1, 4 ], "enchanted-book-rnd-trial-chambers": [ 1, 1, 8 ], "emerald": [ 2, 4, 12 ], "enchanted-book-rnd-mending-trident": [ 1, 1, 8 ], "honey-bottle": [ 1, 2, 3 ] }, "rolls": [ 1, 1 ], "totalweight": 110 }, { "items": { "diamond": [ 1, 2, 1 ], "arrow": [ 2, 8, 4 ], "tipped-arrow-poison": [ 2, 8, 4 ], "ominous-bottle": [ 1, 1, 2 ], "wind-charge": [ 4, 12, 1 ], "emerald": [ 2, 4, 4 ], "honey-bottle": [ 1, 2, 3 ], "iron-ingot": [ 1, 4, 3 ] }, "rolls": [ 1, 3 ], "totalweight": 22 }, { "items": { "trident": [ 1, 1, 1 ], "bolt-armor-trim-smithing-template": [ 1, 1, 3 ], "empty": [ 1, 1, 36 ], "golden-apple": [ 1, 1, 6 ], "guster-banner-pattern": [ 1, 1, 2 ] }, "rolls": [ 1, 1 ], "totalweight": 48 } ], "allRollsBedrockUpcoming": [], "allRollsBedrock": [ 1, "1–3", 1 ], "itemDataBedrockUpcoming": [], "chest_type": "reward-container", "header": "Reward", "allRollsJava": [ 1, "1–3", 1 ], "link": "[[trial chambers]] reward", "structID": "trial-chambers" } } }


↑ The size of stacks (or for unstackable items, number) of this item on any given roll.

↑ The weight of this item relative to other items in the pool.

↑ The odds of finding any of this item in a single chest.

↑ The number of items expected per chest, averaged over a large number of chests.

↑ The average number of chests the player should expect to search to find any of this item.

↑ 'Nothing' does not refer to the chance of an empty chest.  Instead, it refers to the chance that the random loot generator does not add any loot on a single roll.

↑ Ominous bottle level between I and II

↑ The item has between 50% and 100% of its total durability.

↑ a b c d e Enchantment probabilities are the same as a level-5 to level-15 enchantment would be on an enchantment table that was able to apply treasure enchantments (except Soul Speed, and Swift Sneak), and where the chance of multiple enchantments is not reduced.

↑ Enchanted with a random level of Mending, Riptide, Loyalty, Channeling, or Impaling.

↑ Enchanted with a random level of Sharpness, Bane of Arthropods, Efficiency, Fortune, Silk Touch, or Feather Falling.

↑ Enchantment probabilities are the same as a level-5 to level-20 enchantment would be on an enchantment table that was able to apply treasure enchantments (except Soul Speed, and Swift Sneak), and where the chance of multiple enchantments is not reduced.



 Chiseled copper
- Generates intrial chambers.
- Can be crafted from 2cut copper slabsor can be obtained by cutting blocks of copper using astonecutter.


- Has different levels of oxidation.
- Oxidation can be reversed with anaxe.
- Honeycombprevents oxidation from occurring.

 Copper grate
- Generates intrial chambers.
- Can be crafted from 4blocks of copperor can be obtained by cutting blocks of copper using astonecutter.

4444
- Has its own exclusive breaking sound.
- Has different levels of oxidation.
- Oxidation can be reversed with anaxe.
- Honeycombprevents oxidation from occurring.
- Can bewaterlogged.
- Lightshines through it.
- Mobscannot spawn on or be suffocated in it.

 Copper bulb
- Generates intrial chambers.
- Can be crafted from 3blocks of copper, ablaze rodand a piece ofredstone dust.

4444
- Emitslightbased on its oxidation level. The light gets dimmer with increased oxidation.
- Has different levels of oxidation.
- Oxidation can be reversed with anaxe.
- Honeycombprevents oxidation from occurring.
- Defaults to an off state but can be toggledwith a redstone pulse.
- The block state is readable, allowing the block to function as aT flip-flop.

 Copper door
3333
- Generates intrial chambers.
- Can be opened by aplayer.
- Can also be toggled opened and closed withredstone.
- Has different levels of oxidation.
- Oxidation can be reversed with anaxe.
- Honeycombprevents oxidation from occurring.

 Copper trapdoor
2222
*Generates in trial chambers.

- Can be opened by aplayer.
- Can also be toggled opened and closed withredstone.
- Has different levels of oxidation.
- Oxidation can be reversed with anaxe.
- Honeycombprevents oxidation from occurring.

 Tuff stairs
- Can be crafted fromtuffor can be obtained by cutting tuff using astonecutter.

 Tuff slab
- Can be crafted fromtuffor can be obtained by cutting tuff using astonecutter.
- Can be used to craftchiseled tuff.

 Tuff wall
- Can be crafted fromtuffblocks or can be obtained by cutting tuff using astonecutter.

 Chiseled tuff
- Can be crafted fromtuff slabsor can be obtained by cutting tuff using astonecutter.


- Generates intrial chambers.

 Polished tuff
- Generates intrial chambers.
- Can be crafted fromtuffor can be obtained by cutting tuff using astonecutter.
- Can be used to craft their respectivestairs,slabsandwalls.

 Tuff bricks
- Generates intrial chambers.
- Can be crafted frompolished tuffor can be obtained by cutting tuff using astonecutter.
- Can be used to craft achiseled variantand a respectivestairs,slabsandwalls.

