#### Renaming
Any item or stack of items can be renamed at a cost of one level plus any prior-work penalty. If the player is only renaming, the maximum total cost is 39 levels. The maximum length for renaming is 30 characters‌[BE  only] or 50 characters‌[JE  only]. Some items have special effects when renamed:

- Aname tagmust be renamed before it can be used.
- Renaming abucket of fish or axolotlrenames the mob inside as well, meaning a fish or axolotl can be named without a name tag.‌[Java Edition  only]
- A renamed item (can be any item, doesn't need to be a weapon) that kills another player or tamed mob causes the name to appear in the death message.‌[Java Edition  only]
- A renamedspawn eggproduces a mob with the same name.
- Chests,trapped chests,shulker boxes,furnaces,hoppers,droppers,dispensers,minecarts with chests,minecarts with hoppers,enchantment tables,barrels,smokers,blast furnacesandbrewing standsdisplay the name in their GUI when placed.
- Renamedcommand blocksuse their name in chat messages instead of[@].

Any name changes to items are applied to the data tag {Item:{tag:{display:{Name:"{\"text\":\"<name>\"}"}}}}. Similarly, this data tag can be accessed by the nbt argument using target selectors.

If the item name field is left blank, or is only whitespace or non-breaking spaces (or a combination of both), the default name for that item is used instead. Also, if the item name is unchanged from its current name (which can occur when renaming an item for the first time and using any of the aforementioned blank parameters), a red "X" appears on top of the arrow in the GUI.

Named items do not stack with unnamed or differently-named items of the same type.

### Enchanted books
Enchanted books can be used to enchant tools, armor and weapons. Enchanted books themselves can be combined to create higher-tiered books. This makes an anvil an alternative to the enchantment table.

### Falling anvils

Falling Anvil




Java Edition






Bedrock Edition







Hitbox size


Height: 0.98 BlocksWidth: 0.98 Blocks 




{
    "title": "Falling Anvil",
    "rows": [
        {
            "field": "Height: 0.98 Blocks<br>Width: 0.98 Blocks",
            "label": "(link to Hitbox article, displayed as Hitbox size)"
        }
    ],
    "invimages": [],
    "images": []
}
Main article: Falling Block
When there is no supporting block below an anvil, the anvil falls in the same way sand, gravel, concrete powder, and dragon eggs fall. A placed anvil cannot be pushed or pulled by pistons,‌[Java Edition  only] but a falling anvil can be pushed (though cannot be pulled), as it is an entity. This is different in Bedrock Edition where anvils can be pushed and pulled by pistons. Anvils make a metallic clang sound when they land.

A falling anvil damages any player or mob that it falls on. The damage amount depends on fall distance: 2 per block fallen after the first (e.g., an anvil that falls 4 blocks deals 6 damage). The damage is capped at 40 × 20, no matter how far the anvil falls. Wearing a helmet reduces the damage by 1⁄4, but this costs twice as much durability on the helmet as on other armor pieces. When a player dies by an anvil falling on them, the death message "<player> was squashed by a falling anvil" appears. However, if a player is merely touched by a falling anvil entity, no damage is dealt unless the falling anvil becomes an anvil block in the same block where the player is located.

If an anvil falls onto a block with a solid top surface, but the same block it is in cannot be replaced (torch, slab, etc.), it breaks and drops as an item.

An anvil can fall into the void if there is a straight path to it.

### Maps
Main article: Map
An anvil can be used instead of a crafting table to zoom a map out, to clone a map, or to place a player position marker on a map.‌[Bedrock Edition  only]



| Name                            | Ingredients                  | Anvil usage                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Description                                                                                                                                                                                                 |
|---------------------------------|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Map or Locator Map (zoomed out) | Mapor Locator Map +Paper     | .mw-parser-output .template-Anvil-background{box-sizing:content-box;width:324px;height:128px}.mw-parser-output .template-Anvil-prompt{display:block;color:#3F3F3F;font-family:Minecraft;font-size:16px;text-align:left;margin-left:106px;margin-top:-3px;overflow:hidden;text-overflow:ellipsis}.mw-parser-output .template-Anvil-inputbox{position:absolute;top:32px;right:6px;width:220px;height:32px}.mw-parser-output .template-Anvil-inputtext{display:block;margin:5px 6px;color:#FCFCFC;text-shadow:0.125em 0.125em 0 #3E3E3E;font-family:Minecraft;font-size:16px;overflow:hidden;text-overflow:ellipsis;max-width:208px}.mw-parser-output .template-Anvil-slot{display:block;position:absolute;top:84px;left:44px}.mw-parser-output .template-Anvil-hammer{position:absolute;top:6px;left:26px;background-size:cover;width:60px;height:60px}.mw-parser-output .template-Anvil-plus{position:absolute;top:90px;left:98px;background-size:cover;width:26px;height:26px}.mw-parser-output .template-Anvil-arrow{display:block;position:absolute;top:88px;left:196px;width:44px;height:30px}.mw-parser-output .template-Anvil-cost{display:block;position:absolute;top:126px;right:8px;background:#898989;padding:0 4px 0 4px;font-family:Minecraft;font-size:16px;overflow:hidden;text-overflow:ellipsis;max-width:308px}.mw-parser-output .template-Anvil-cost-expensive{color:#FC5F5F;text-shadow:0.125em 0.125em #3E1818,0.125em 0 #3E1818,0 0.125em #3E1818}.mw-parser-output .template-Anvil-cost-normal{color:#7EFC20;text-shadow:0.125em 0.125em #203E08,0.125em 0 #203E08,0 0.125em #203E08}Repair & Name MapLocator Map8 | Bedrock Editiononly.Supplying 8 sheets of paper results in a zoomed-out version of the input map.                                                                                                           |
| Map or Locator Map (cloned)     | Mapor Locator Map +Empty Map | Repair & Name MapLocator MapMapLocator Map2222                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Bedrock Editiononly.Only one copy can be made at a time.The non-empty input map must be a locator map for the output to be a locator map. An empty locator map is the same as an empty map for this recipe. |
| Locator Map                     | Map+Compass                  | Repair & NameMap                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Bedrock Editiononly.Maps crafted with only paper do not show the location marker; to add it, a compass must be added to the map.                                                                            |

### Becoming damaged
With each use, an anvil has a 12% chance to become damaged – degrading one stage at a time, first becoming chipped, then damaged, then eventually destroyed. An anvil typically survives for 25 uses on average or approximately one use per 1.24 iron ingots used in crafting the anvil.

An anvil can be damaged and destroyed from falling. If it falls from a height greater than one block, the chance of degrading by one stage is 5% × the number of blocks fallen.

The damage state does not affect the anvil's function, but only anvils of the same damage state can stack in inventory.

When an anvil is destroyed, the player automatically leaves the anvil GUI and it disappears.

