# Direct item forms of blocks
The game prevents certain blocks from being obtained through normal gameplay methods, such as crafting, the creative inventory, the pick block key, and the Silk Touch enchantment. It also prevents such blocks from being given through less conventional methods, such as inventory editing, mods, and commands. Until 1.7.2 and 1.8, there had been a wide variety of blocks that could be edited into the inventory; over time, however, the game was updated so that these blocks became entirely unavailable, even though one utilized inventory editing. From Java Edition 1.13 onwards, blocks and items are completely different concepts, and numerical IDs no longer exist at all.

Currently, the game only accepts resource locations (such as minecraft:dirt) in most commands, and uses these resource locations when assigning blocks to the inventory and save files. The old method of obtaining a block via numerical IDs is no longer an option because the numerical id method getItemById(Integer.parseInt(id))  is no longer used in command /give.  In addition, the game automatically removes blocks with illegitimate resource locations from the inventory, so using inventory editors is also no longer an option . Furthermore, certain blocks with both block and item forms, such as minecraft:cake, cannot be obtained in their block form in the inventory; however, since the game has a corresponding item named minecraft:cake, the item form is given instead. The only option is modifying game's class where registered items and ItemBlocks (direct item forms of blocks) in order to register and obtain them. 

Despite never being intended to be obtainable, some of these could even be acquired in survival using unusual means.

## Contents
- 1 Java Edition
	- 1.1 List
		- 1.1.1 Removals
- 2 Bedrock Edition

## Java Edition
The game prevents certain blocks from being obtained through normal gameplay methods, such as crafting, the creative inventory, the pick block key, and the Silk Touch enchantment. It also prevents such blocks from being given through less conventional methods, such as inventory editing, mods, and commands. Until 1.7.2 and 1.8, there had been a wide variety of blocks that could be edited into the inventory; over time, however, the game was updated so that these blocks became entirely unavailable, even though one utilized inventory editing. From Java Edition 1.13 onwards, blocks and items are completely different concepts, and numerical IDs no longer exist at all.

Currently, the game only accepts resource locations (such as minecraft:dirt) in most commands, and uses these resource locations when assigning blocks to the inventory and save files. The old method of obtaining a block via numerical IDs is no longer an option because the numerical id method getItemById(Integer.parseInt(id))  is no longer used in command /give.  In addition, the game automatically removes blocks with illegitimate resource locations from the inventory, so using inventory editors is also no longer an option . Furthermore, certain blocks with both block and item forms, such as minecraft:cake, cannot be obtained in their block form in the inventory; however, since the game has a corresponding item named minecraft:cake, the item form is given instead. The only option is modifying game's class where registered items and ItemBlocks (direct item forms of blocks) in order to register and obtain them. 

Despite never being intended to be obtainable, some of these could even be acquired in survival using unusual means.

### List
The following data is based on the last version each item existed in.

| Numeric ID |     | Item | Block                         | Name                      | Resource location    | Added                 | Removed        |
|------------|-----|------|-------------------------------|---------------------------|----------------------|-----------------------|----------------|
| Hex        | Dec |      |                               |                           |                      |                       |                |
| 0          | 0   |      | Air                           | tile.air.name             | air                  | 13w38b                | 13w38c         |
| 8          | 8   |      | Flowing Water                 | Water                     | flowing_water        | 0.24_SURVIVAL_TEST    | 14w25a         |
| 9          | 9   |      | Still Water                   | Water                     | water                | 0.24_SURVIVAL_TEST    | 14w25a         |
| A          | 10  |      | Flowing Lava                  | Lava                      | flowing_lava         | 0.24_SURVIVAL_TEST    | 14w25a         |
| B          | 11  |      | Still Lava                    | Lava                      | lava                 | 0.24_SURVIVAL_TEST    | 14w25a         |
| 1A         | 26  |      | Red Bed                       | Bed                       | bed                  | Beta 1.3              | 13w37a         |
| 22         | 34  |      | Piston Head                   | tile.null.name            | piston_head          | Beta 1.7              | 13w37a         |
| 24         | 36  |      | Moving Piston                 | tile.null.name            | piston_extension     | Beta 1.7              | 13w37a         |
| 2B         | 43  |      | Double Smooth Stone Slab      | [more information needed] | double_stone_slab    | 0.26 SURVIVAL TEST    | 14w25a         |
| 33         | 51  |      | Fire                          | Fire                      | fire                 | in-20100109           | 14w25a         |
| 37         | 55  |      | Redstone Wire                 | Redstone Dust             | redstone_wire        | Alpha v1.0.1          | 13w37a         |
| 3B         | 59  |      | Wheat                         | Crops                     | wheat                | in-20100206           | 13w37a         |
| 3E         | 62  |      | Lit Furnace                   | Furnace                   | lit_furnace          | in-20100219           | 15w49a         |
| 3F         | 63  |      | Oak Sign                      | Sign                      | standing_sign        | inf-20100607          | 13w37a         |
| 40         | 64  |      | Oak Door                      | Wooden Door               | wooden_door          | inf-20100607          | 13w37a         |
| 44         | 68  |      | Oak Wall Sign                 | Sign                      | wall_sign            | Alpha v1.0.1          | 13w37a         |
| 47         | 71  |      | Iron Door                     | Iron Door                 | iron_door            | Alpha v1.0.1          | 13w37a         |
| 4A         | 74  |      | Lit Redstone Ore              | Redstone Ore              | lit_redstone_ore     | Alpha v1.0.1          | 13w37a         |
| 4B         | 75  |      | Unlit Redstone Torch          | Redstone Torch            | unlit_redstone_torch | Alpha v1.0.1          | 13w37a         |
| 53         | 83  |      | Sugar Cane                    | Sugar cane                | reeds                | Alpha v1.0.11         | 13w37a         |
| 5A         | 90  |      | Nether Portal                 | Portal                    | portal               | Alpha v1.2.0          | 14w25a         |
| 5C         | 92  |      | Cake                          | Cake                      | cake                 | Beta 1.2              | 13w37a         |
| 5D         | 93  |      | Unpowered Redstone Repeater   | tile.diode.name           | unpowered_repeater   | Beta 1.3              | 13w37a         |
| 5E         | 94  |      | Powered Redstone Repeater     | tile.diode.name           | powered_repeater     | Beta 1.3              | 13w37a         |
| 68         | 104 |      | Pumpkin Stem                  | tile.pumpkinStem.name     | pumpkin_stem         | Beta 1.8 Pre-release  | 13w37a         |
| 69         | 105 |      | Melon Stem                    | tile.pumpkinStem.name     | melon_stem           | Beta 1.8 Pre-release  | 13w37a         |
| 73         | 115 |      | Nether Wart                   | Nether Wart               | nether_wart          | Beta 1.9 Prerelease   | 13w37a         |
| 75         | 117 |      | Brewing Stand                 | tile.brewingStand.name    | brewing_stand        | Beta 1.9 Prerelease 3 | 13w37a         |
| 76         | 118 |      | Cauldron                      | Cauldron                  | cauldron             | Beta 1.9 Prerelease 3 | 13w37a         |
| 77         | 119 |      | End Portal                    | tile.null.name            | end_portal           | Beta 1.9 Prerelease 3 | 14w25a         |
| 7C         | 124 |      | Lit Redstone Lamp             | Redstone Lamp             | lit_redstone_lamp    | 12w07a                | 13w37a         |
| 7D         | 125 |      | Double Oak Slab               | [more information needed] | double_wooden_slab   | 12w17a                | 14w25a         |
| 7F         | 127 |      | Cocoa                         | Cocoa                     | cocoa                | 12w19a                | 14w25a         |
| 84         | 132 |      | Tripwire                      | Tripwire                  | tripwire             | 12w22a                | 13w37a         |
| 8C         | 140 |      | Flower Pot                    | tile.flowerPot.name       | flower_pot           | 12w34a                | 13w37a         |
| 8D         | 141 |      | Carrots                       | Carrots                   | carrots              | 12w34a                | 13w37a[verify] |
| 8E         | 142 |      | Potatoes                      | Potatoes                  | potatoes             | 12w34a                | 13w37a[verify] |
| 90         | 144 |      | Skull                         | tile.skull.name           | skull                | 12w36a                | 13w37a         |
| 95         | 149 |      | Unpowered Redstone Comparator | tile.comparator.name      | unpowered_comparator | 13w01a                | 13w37a         |
| 96         | 150 |      | Powered Redstone Comparator   | tile.comparator.name      | powered_comparator   | 13w01a                | 13w37a         |

