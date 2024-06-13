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

#### Removals
See also: Java Edition data values § IDs

All of the following block items were removed at one point, as clarified in the following paragraphs.

In snapshot 13w37a for 1.7.2, the /give command was modified so that it would display the name of the item in chat. In fact, this change could not remove ItemBlocks, another change was necessary. Due to this,  Sets.newHashSet(Block[], {blocks here}) was added which removes the item forms of blocks in the list of its list. Due to this, 26 blocks were made unavailable.

In snapshot 14w25a for 1.8, changes were made to the way the icons of items were rendered, and the way block data was internally represented. Similar to 13w37a, this change could not remove ItemBlocks, another change was necessary. Due to this, registerItemBlock(block) method was added, which adds the item form of respective block. Due to this, 12 blocks were made unavailable. 

| Block                        | Resource location    | Dec | Hex | Obtainable until... |
|------------------------------|----------------------|-----|-----|---------------------|
| Bed                          | bed                  | 26  | 1A  | 1.7.2 (13w37a)      |
| Piston Head                  | piston_head          | 34  | 22  | 1.7.2 (13w37a)      |
| Piston Extension             | piston_extension     | 36  | 24  | 1.7.2 (13w37a)      |
| Redstone Wire                | redstone_wire        | 55  | 37  | 1.7.2 (13w37a)      |
| Wheat                        | wheat                | 59  | 3B  | 1.7.2 (13w37a)      |
| Standing Sign                | standing_sign        | 63  | 3F  | 1.7.2 (13w37a)      |
| Wooden Door                  | wooden_door          | 64  | 40  | 1.7.2 (13w37a)      |
| Wall Sign                    | wall_sign            | 68  | 44  | 1.7.2 (13w37a)      |
| Iron Door                    | iron_door            | 71  | 47  | 1.7.2 (13w37a)      |
| LitRedstone Ore              | lit_redstone_ore     | 74  | 4A  | 1.7.2 (13w37a)      |
| UnlitRedstone Torch          | unlit_redstone_torch | 75  | 4B  | 1.7.2 (13w37a)      |
| Sugar Cane                   | reeds                | 83  | 53  | 1.7.2 (13w37a)      |
| Cake                         | cake                 | 92  | 5C  | 1.7.2 (13w37a)      |
| UnpoweredRedstone Repeater   | unpowered_repeater   | 93  | 5D  | 1.7.2 (13w37a)      |
| PoweredRedstone Repeater     | powered_repeater     | 94  | 5E  | 1.7.2 (13w37a)      |
| Pumpkin Stem                 | pumpkin_stem         | 104 | 68  | 1.7.2 (13w37a)      |
| Melon Stem                   | melon_stem           | 105 | 69  | 1.7.2 (13w37a)      |
| Nether Wart                  | nether_wart          | 115 | 73  | 1.7.2 (13w37a)      |
| Brewing Stand                | brewing_stand        | 117 | 75  | 1.7.2 (13w37a)      |
| Cauldron                     | cauldron             | 118 | 76  | 1.7.2 (13w37a)      |
| LitRedstone Lamp             | lit_redstone_lamp    | 124 | 7C  | 1.7.2 (13w37a)      |
| Tripwire                     | tripwire             | 132 | 84  | 1.7.2 (13w37a)      |
| Flower Pot                   | flower_pot           | 140 | 8C  | 1.7.2 (13w37a)      |
| Skull                        | skull                | 144 | 90  | 1.7.2 (13w37a)      |
| UnpoweredRedstone Comparator | unpowered_comparator | 149 | 95  | 1.7.2 (13w37a)      |
| PoweredRedstone Comparator   | powered_comparator   | 150 | 96  | 1.7.2 (13w37a)      |
| Air                          | air                  | 0   | 0   | 1.7.2 (13w38c)      |
| FlowingWater                 | flowing_water        | 8   | 08  | 1.8 (14w25a)        |
| StillWater                   | water                | 9   | 09  | 1.8 (14w25a)        |
| FlowingLava                  | flowing_lava         | 10  | 0A  | 1.8 (14w25a)        |
| StillLava                    | lava                 | 11  | 0B  | 1.8 (14w25a)        |
| Double Stone Slab            | double_stone_slab    | 43  | 2B  | 1.8 (14w25a)        |
| Fire                         | fire                 | 51  | 34  | 1.8 (14w25a)        |
| Nether Portal                | portal               | 90  | 5A  | 1.8 (14w25a)        |
| End Portal                   | end_portal           | 119 | 77  | 1.8 (14w25a)        |
| Double Wooden Slab           | double_wooden_slab   | 125 | 7D  | 1.8 (14w25a)        |
| Cocoa                        | cocoa                | 127 | 7F  | 1.8 (14w25a)        |
| Carrots                      | carrots              | 141 | 8D  | 1.8 (14w25a)        |
| Potatoes                     | potatoes             | 142 | 8E  | 1.8 (14w25a)        |
| Lit Furnace                  | lit_furnace          | 62  | 3E  | 1.9 (15w49a)        |

## Bedrock Edition
In Bedrock Edition, some of the items can only be obtained from inventory editing.

| Block                                  | Resource location                     | Dec                       | Hex                       |
|----------------------------------------|---------------------------------------|---------------------------|---------------------------|
| Air                                    | air                                   | 0                         | 0                         |
| Water                                  | flowing_water                         | 8                         | 8                         |
| StationaryWater                        | water                                 | 9                         | 9                         |
| Lava                                   | flowing_lava                          | 10                        | A                         |
| StationaryLava                         | lava                                  | 11                        | B                         |
| Bed                                    | bed                                   | 26                        | 1A                        |
| Piston Head                            | pistonarmcollision                    | 34                        | 22                        |
| Double Stone Slab                      | double_stone_slab                     | 43                        | 2B                        |
| Fire                                   | fire                                  | 51                        | 33                        |
| Redstone Wire                          | redstone_wire                         | 55                        | 37                        |
| Wheat Crops                            | wheat                                 | 59                        | 3B                        |
| Oak Standing Sign                      | standing_sign                         | 63                        | 3F                        |
| Oak Door                               | wooden_door                           | 64                        | 40                        |
| Oak Wall Sign                          | wall_sign                             | 68                        | 44                        |
| Iron Door                              | iron_door                             | 71                        | 47                        |
| LitRedstone Ore                        | lit_redstone_ore                      | 74                        | 4A                        |
| UnlitRedstone Torch                    | unlit_redstone_torch                  | 75                        | 4B                        |
| Sugar Cane                             | reeds                                 | 83                        | 53                        |
| Nether Portal                          | portal                                | 90                        | 5A                        |
| Cake                                   | cake                                  | 92                        | 5C                        |
| UnpoweredRedstone Repeater             | unpowered_repeater                    | 93                        | 5D                        |
| PoweredRedstone Repeater               | powered_repeater                      | 94                        | 5E                        |
| Invisible Bedrock                      | invisiblebedrock                      | 95                        | 5F                        |
| Pumpkin Stem                           | pumpkin_stem                          | 104                       | 68                        |
| Melon Stem                             | melon_stem                            | 105                       | 69                        |
| Nether Wart                            | nether_wart                           | 115                       | 73                        |
| Brewing Stand                          | brewing_stand                         | 117                       | 75                        |
| Cauldron                               | cauldron                              | 118                       | 76                        |
| End Portal                             | end_portal                            | 119                       | 77                        |
| LitRedstone Lamp                       | lit_redstone_lamp                     | 124                       | 7C                        |
| Cocoa                                  | cocoa                                 | 127                       | 7F                        |
| Tripwire                               | tripwire                              | 132                       | 84                        |
| Flower Pot                             | flower_pot                            | 140                       | 8C                        |
| Carrot                                 | carrots                               | 141                       | 8D                        |
| Potato                                 | potatoes                              | 142                       | 8E                        |
| Mob head                               | skull                                 | 144                       | 90                        |
| UnpoweredRedstone Comparator           | unpowered_comparator                  | 149                       | 95                        |
| PoweredRedstone Comparator             | powered_comparator                    | 150                       | 96                        |
| StandingBanner                         | standing_banner                       | 176                       | B0                        |
| WallBanner                             | wall_banner                           | 177                       | B1                        |
| Inverted Daylight Detector             | daylight_detector_inverted            | 178                       | B2                        |
| Double Red Sandstone Slab              | double_stone_slab2                    | 181                       | B5                        |
| Spruce Door                            | spruce_door                           | 193                       | C1                        |
| Birch Door                             | birch_door                            | 194                       | C2                        |
| Jungle Door                            | jungle_door                           | 195                       | C3                        |
| Acacia Door                            | acacia_door                           | 196                       | C4                        |
| Dark Oak Door                          | dark_oak_door                         | 197                       | C5                        |
| Item Frame                             | frame                                 | 199                       | C7                        |
| Frosted Ice                            | frosted_ice                           | 207                       | CF                        |
| End Gateway                            | end_gateway                           | 209                       | D1                        |
| Chalkboard                             | chalkboard                            | 230                       | E6                        |
| Beetroots                              | beetroot                              | 244                       | F4                        |
| Block moved by Piston                  | movingblock                           | 250                       | FA                        |
| Kelp                                   | kelp                                  | 393                       | 189                       |
| Bubble Column                          | bubble_column                         | 415                       | 19F                       |
| Double End Stone Brick Slab            | double_stone_slab3                    | 422                       | 1A6                       |
| Double Mossy Stone Brick Slab          | double_stone_slab4                    | 423                       | 1A7                       |
| Spruce Standing Sign                   | spruce_standing_sign                  | 436                       | 1B4                       |
| Spruce Wall Sign                       | spruce_wall_sign                      | 437                       | 1B5                       |
| Birch Standing Sign                    | birch_standing_sign                   | 441                       | 1B9                       |
| Birch Wall Sign                        | birch_wall_sign                       | 442                       | 1BA                       |
| Jungle Standing Sign                   | jungle_standing_sign                  | 443                       | 1BB                       |
| Jungle Wall Sign                       | jungle_wall_sign                      | 444                       | 1BC                       |
| Jungle Standing Sign                   | acacia_standing_sign                  | 445                       | 1BD                       |
| Jungle Wall Sign                       | acacia_wall_sign                      | 446                       | 1BE                       |
| Dark Oak Standing Sign                 | darkoak_standing_sign                 | 447                       | 1BF                       |
| Dark Oak Wall Sign                     | darkoak_wall_sign                     | 448                       | 1C0                       |
| Sweet Berry Bush                       | sweet_berry_bush                      | 462                       | 1CE                       |
| Campfire                               | campfire                              | 462                       | 1CE                       |
| Lava Cauldron                          | lava_cauldron                         | 469                       | 1D5                       |
| Sticky Piston Head                     | stickypistonarmcollision              | 472                       | 1D8                       |
| Soul Fire                              | soul_fire                             | 492                       | 1EC                       |
| Nether Sprouts                         | nether_sprouts                        | 493                       | 1ED                       |
| Crimson Door                           | crimson_door                          | 499                       | 1F3                       |
| Warped Door                            | warped_door                           | 500                       | 1F4                       |
| Crimson Standing Sign                  | crimson_standing_sign                 | 505                       | 1F9                       |
| Warped Standing Sign                   | warped_standing_sign                  | 506                       | 1FA                       |
| Crimson Wall Sign                      | crimson_wall_sign                     | 507                       | 1FB                       |
| Warped Wall Sign                       | warped_wall_sign                      | 508                       | 1FC                       |
| Crimson Double Slab                    | crimson_double_slab                   | 521                       | 209                       |
| Warped Double Slab                     | warped_double_slab                    | 522                       | 20A                       |
| Blackstone Double Slab                 | blackstone_double_slab                | 538                       | 21A                       |
| Polished Blackstone Bricks Double Slab | polished_blackstone_brick_double_slab | 540                       | 21C                       |
| Soul Campfire                          | soul_campfire                         | 545                       | 221                       |
| Polished Blackstone Double Slab        | polished_blackstone_double_slab       | 549                       | 225                       |
| Cobbled Deepslate Double Slab          | cobbled_deepslate_double_slab         | 651                       | 28B                       |
| Polished Deepslate Double Slab         | polished_deepslate_double_slab        | 652                       | 28C                       |
| Deepslate Tile Double Slab             | deepslate_tile_double_slab            | 653                       | 28D                       |
| Deepslate Brick Double Slab            | deepslate_brick_double_slab           | 654                       | 28E                       |
| Lit Deepslate Redstone Ore             | lit_deepslate_redstone_ore            | [more information needed] | [more information needed] |

