# Minecraft Comprehensive Skill Library

## Introduction

This comprehensive skill library is implemented based on the Mineflayer framework, aiming to provide an automated tool to collect all collectible and craftable items in the game of Minecraft.

```javascript
obtainItem(bot, count, type)
// 'count' is the number of items, 'type' is the type of item.
// For example, to obtain a diamond: obtainItem(bot, 1, "diamond");
```
## Get Started
We provide a new interface for testing this skill library in the Odyssey directory.

```python
test_mc_skill(skill_name, para_list)
# For example, to obtain a diamond:
test_mc_skill("obtainItem.js", [1, "diamond"])
```

## Interface

To simulate the process of solving prerequisite steps in the actual game to eventually obtain specific items, this skill library has introduced a recursive calling method. All interfaces can recursively call each other or themselves and pass parameters through a lookup table.

- `mineItem(bot, count = 1, type, explore_direction = new Vec3(1, 0, 1), explore_time = 300)`: Mine using specific tools.
- `craftItem(bot, count = 1, type, need_crafting_table = true)`: Craft items using a crafting table.
- `smeltItem(bot, count = 1, type, fuel = "coal")`: Smelt or cook items in a furnace.
- `collectItem(bot, count = 1, type, function = "kill")`: Collect items by killing animals or other special methods.

## Parameter Table

The following recursive parameter tables determine the parameters for the next recursive function call based on the current input parameters:

- `pre_tool.json`: Corresponds to the "mine" function, records the tools needed to mine various items.
- `pre_item.json`: Corresponds to the "craft" function, records the materials needed to craft various items, needed count and output count, and whether a crafting table is required.
- `pre_smelt.json`: Corresponds to the "smelt" function, records the smelting/cooking recipes for the furnace.
- `pre_collect.json`: Corresponds to the "collect" function, records the blocks or animals that may drop certain special items, and the specific methods for collecting these items.
- `func.json`: Indicates which function the obtain function should call to collect different types of items.
- `map_name.json`: Handles special cases. Matches in-game block names with their actual drops (e.g., diamond ore with diamonds) and categorizes items with the same function (e.g., various types of wood) into one class.

## Notes

The skill library achieves 789 major items in all three world dimensions of Minecraft (Overworld, The Nether, The End), and has good scalability. However, this skill library does not specifically implement functions for building Nether and end portals. If you need to test the above skills in the Nether or the End, make sure the bot has collected enough materials and tools in the overworld and manually transport them to the Nether or the End. Additionally, this skill library is designed specifically for procedural tasks corresponding to items that can be naturally collected or crafted, and does not currently include other categories of skills such as planting, husbandry, combat, and construction. We will continue to update this skill library to create a more comprehensive, open-world and user-friendly tool.

## Contact

Welcome your use and feedback. If you find any bugs or have other issues or suggestions during testing, please feel free to contact liyaoru@zju.edu.cn
