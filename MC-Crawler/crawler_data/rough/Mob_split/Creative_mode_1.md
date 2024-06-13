### Achievements

  

This feature is exclusive to  Bedrock Edition. 


In Bedrock Edition, opening a new Creative world or opening an existing world in Creative permanently disables achievements or trophies for that particular game, but has no other effects on gameplay. In other words, achievements/trophies work only in games that have never been in Creative.

## Creative inventory

  

This section 's factual accuracy may be compromised due to out-of-date information. 
Please update this section to reflect recent updates or newly available information.Reason: Java and Bedrock in 1.20 inventory changes.



  

This section is a work in progress. 
Please help expand and improve it. The talk page may contain suggestions.


The Creative mode inventory showing the Search tab for the Java Edition.
The Creative mode inventory showing the All tab in Bedrock Edition (Classic option).
The Creative mode inventory showing the All tab in Bedrock Edition (Pocket option).
In Creative, the normal inventory screen is replaced by the item selection screen, which contains almost all blocks and items (with some exceptions) in a tabbed interface. Some items and blocks are available only in Creative mode, such as spawn eggs. Likewise, some blocks can be used only in Creative, such as command blocks and structure blocks.

Main article: Creative inventory
### Java Edition
In Java Edition, there are 13 tabs that are ordered from top-left to bottom right as: 

- Building Blocks
- Colored Blocks
- Natural Blocks
- Functional Blocks
- Redstone Blocks
- Saved Hotbars
- Search Items
- Tools & Utilities
- Combat
- Food & Drinks
- Ingredients
- Spawn Eggs
- Operator Utilities(Needs to be enabled in settings)
- Survival Inventory

### Bedrock Edition
In Bedrock Edition, there are 5 tabs:

- Construction
- Equipment
- Items
- Nature
- All

When using the "Classic" UI profile, the buttons in the top right corner can toggle the inventory screen to show:

- only the Creative inventory
- both the Creative and the Survival inventory
- only the Survival inventory

When using the "Pocket" UI profile, it is not possible to display both the Creative and the Survival inventory at the same time; the Creative inventory, however, can be shrunk to also display the 2×2 crafting grid or the equipment slots using the tabs on the right side of the screen.

### General info
Some items behave differently in Creative mode. Items do not disappear or lose durability when used. For example, putting an item in an item frame, on an armor stand, or in a decorated pot does not cause it to disappear from the player's hand. Instead, the item is duplicated. It is the same for putting on armor by right-clicking it from the player's hotbar. Also, empty buckets simply make liquids disappear.

In Java Edition, there is a "destroy item" button, where items can be dragged to and deleted. ⇧ Shift + clicking on the button clears the entire inventory, including the hotbar, off-hand slot, and armor slots.

Item entities can be picked up by the player, but if the hotbar is already full, the items go into the Survival inventory.

### Pick block
The player can obtain items using pick block. Unlike Survival, the block selected appears in the player's hotbar even if the block is not already in the hotbar or in the Survival inventory. If it is in the inventory, then the block moves out of its former slot and replaces the block/item in the active hotbar slot, with the size of the stack preserved. If the hotbar is full then the selected block replaces the block/item in the active slot.

Most blocks give the player a copy of themselves when using pick block. Using it on an item frame gives the player the item held inside, or the item frame itself if no item is held. Using it on a mob gives the player a spawn egg of that mob. Using it on a mob head gives the mob type that it is; using it on custom heads gives only the mob type that was used in the command, but without the custom skin.

If the player holds Control and presses pick block, in addition to obtaining the item, it also preserves the block's NBT tags, allowing the player to place an identical copy of the block; this allows the player to duplicate items inside of chests, dispensers, and so on, and also duplicates the text on signs.

### Unavailable blocks and items
There are several blocks and a couple of items that do not appear in the Creative inventory. They can be obtained with the /give command and can be manually placed using /setblock command, using the IDs provided in the table below. Additionally, using pick block on these blocks also gives them, except where noted. Technical blocks, such as portals and off-state redstone torches, do not have corresponding inventory items at all in Java Edition and cannot be obtained without external help in Bedrock Edition, and thus cannot be legitimately obtained.

| Name                                 | Can be obtained with Pick Block? | Inventory availability |                 | Identifier                                                              |
|--------------------------------------|----------------------------------|------------------------|-----------------|-------------------------------------------------------------------------|
|                                      |                                  | Java Edition           | Bedrock Edition |                                                                         |
| Allow                                | Yes                              | N/A                    | No              | `allow`                                                                 |
| Barrier                              | Yes                              | Yes[note 1]            | No              | `barrier`                                                               |
| Border                               | Yes                              | N/A                    | No              | `border_block`                                                          |
| Command block                        | Yes                              | Yes[note 1]            | No              | `command_block`<br/>`repeating_command_block`<br/>`chain_command_block` |
| Debug stick                          | Not a block                      | Yes[note 1]            | N/A             | `debug_stick`                                                           |
| Deny                                 | Yes                              | N/A                    | No              | `deny`                                                                  |
| Ender dragon spawn egg               | Not a block                      | No                     | No              | `ender_dragon_spawn_egg`                                                |
| Minecart with command block          | Yes (entity)                     | Yes[note 1]            | No              | `command_block_minecart`                                                |
| Firework star[note 2]                | Not a block                      | Yes                    | No              | `firework_star`                                                         |
| Firework rocket[note 2]              | No (entity)                      | No                     | No              | `firework_rocket`                                                       |
| Petrified Oak Slab                   | Yes                              | No                     | No              | `petrified_oak_slab`                                                    |
| Structure block                      | Yes                              | Yes[note 1]            | No              | `structure_block`                                                       |
| Structure void                       | Yes                              | Yes[note 1]            | No              | `structure_void`                                                        |
| Knowledge book                       | Not a block                      | No                     | N/A             | `knowledge_book`                                                        |
| Jigsaw block                         | Yes                              | Yes[note 1]            | No              | `jigsaw`                                                                |
| Light block                          | Yes‌[JE  only]                   | Yes[note 1]            | No              | `light`‌[JE  only]<br/>`light_block`‌[BE  only]                         |
| Suspicious stew[note 2]              | Not a block                      | No                     | No              | `suspicious_stew`                                                       |
| Bundle                               | Not a block                      | Yes[note 3]            | N/A             | `bundle`                                                                |
| Uncraftable potion[note 2]           | Not a block                      | No                     | N/A             | `potion`                                                                |
| Uncraftable lingering potion[note 2] | Not a block                      | No                     | N/A             | `lingering_potion`                                                      |
| Uncraftable splash potion[note 2]    | Not a block                      | No                     | N/A             | `splash_potion`                                                         |
| Uncraftable tipped arrow[note 2]     | Not a block                      | No                     | N/A             | `tipped_arrow`                                                          |
| Wither spawn egg                     | Not a block                      | No                     | No              | `wither_spawn_egg`                                                      |

1. ↑ a b c d e f g hOnly if cheats are enabled and the "Operator Items Tab" option is turned on.
2. ↑ a b c d e f gOnly applies to the "empty" versions of the item without tags. Otherwise, it is available in Survival.
3. ↑Only through the "bundle" experimental data pack.

