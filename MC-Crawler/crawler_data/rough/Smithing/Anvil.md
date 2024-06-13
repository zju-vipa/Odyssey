# Anvil
An anvil is a gravity-affected utility block used to rename items, combine enchantments and repair items without losing the enchantments. An anvil has limited durability, and as it is used or dropped too far, gradually becomes a slightly damaged anvil‌[BE  only] or chipped anvil‌[JE  only], then a very damaged anvil‌[BE  only] or damaged anvil‌[JE  only], then breaks and vanishes.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
- 2 Usage
	- 2.1 Repairing and renaming items
		- 2.1.1 Repairing
		- 2.1.2 Renaming
	- 2.2 Enchanted books
	- 2.3 Falling anvils
	- 2.4 Maps
	- 2.5 Becoming damaged
- 3 Creative mode
- 4 Sounds
	- 4.1 Generic
	- 4.2 Unique
- 5 Data values
	- 5.1 ID
	- 5.2 Block states
	- 5.3 Falling block entity
- 6 Achievements
- 7 History
- 8 Issues
- 9 Trivia
- 10 Gallery
	- 10.1 Renders
	- 10.2 Screenshots
	- 10.3 Development images
- 11 References
- 12 External links

## Obtaining
### Breaking
Anvils can be mined using any pickaxe. If mined without a pickaxe, they drop nothing.

| Block     | Anvil                 |
|-----------|-----------------------|
| Hardness  | 5                     |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 25                    |
| Wooden    | 3.75                  |
| Stone     | 1.9                   |
| Iron      | 1.25                  |
| Diamond   | 0.95                  |
| Netherite | 0.85                  |
| Golden    | 0.65                  |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
A damaged anvil generates in the "Forge room" of the woodland mansion.
An anvil can also generate in trail ruins.

### Crafting
A total of 31 iron ingots (including 27 for three blocks of iron) are required to craft an anvil.

| Ingredients                   | Crafting recipe |
|-------------------------------|-----------------|
| Block of Iron+<br/>Iron Ingot |                 |

## Usage
### Repairing and renaming items
The GUI of the anvil.
Main article: Anvil mechanics
Anvils have two modes to repair items that have a durability rating:

- As with thegrindstone, a player may repair items by combining two similar items. With the anvil, however, the target retains its enchantments and may gain new ones from the sacrificed items.
- Alternatively, a player can use materials originally required in the crafting of the item (iron ingotsfor iron items with durability,diamondsfor diamond items with durability) to repair a single item. One material can repair 25% of the target's maximum durability. This is a good deal in the case of achestplate, for example; a full repair (four materials) would total only half of the item's original cost (eight materials). In the case of tools and weapons, however, this may be a significantly less economical option; combining two diamond shovels would cost two diamonds in total, while up to four diamonds could be required to directly repair one. Still, it may be worth making the more expensive upgrade if the enchantments are considered difficult to obtain.

If the items are unable to be combined, a red "X" appears over the arrow pointing to the slot of the resulting item. Also, if the target item is at full durability and the sacrifice does not have any enchantments, the anvil also refuses to combine the items, unless if renaming the item to a valid name.

In addition, the player can rename any item – not just items with durability – by using an anvil.

#### Repairing
See also: Repair

Example showing a repair of two diamond pickaxes.
Repairing with materials works for the most part, but not with all items: in general, repairing works for items with their material in the default name. For example, an anvil can repair an iron pickaxe with materials (iron in this case) while an anvil cannot repair bows or shears except with other bows or shears. Special cases: chain armor can be repaired with iron ingots, turtle shells can be repaired with scutes, and elytra can be repaired with phantom membranes. The repair does not need to be complete; one material repairs 1⁄4 of the item's maximum durability. Repair of an unenchanted item can cost more material than simply crafting a new item or combining damaged items. The exception is armor, which consumes less material at the cost of experience levels.

Repairing with a matching item works for any item with durability including bows, shears and so on. The items must be a matching tool and of a matching material. For example, a golden pickaxe cannot combine with a golden sword or iron pickaxe.

In both cases, the resulting durability is limited to the item's maximum, and there is no discount for "over-repair".

As a subset of repairing one item with another, the anvil can transfer enchantments from the sacrifice to the target. This can have a synergistic effect when both items share identical enchantments, or simply add to each other when they do not. Two Sharpness II swords can be combined to make a Sharpness III sword, for example, or a pickaxe with Efficiency can be combined with one that has Unbreaking. This can produce enchantments and combinations that are not possible with an enchanting table. But even so, some enchantments cannot be combined if they are similar, or contradicting, in terms of what they do. If the target is damaged, the player has to pay for the repair as well as the transfer.

Transferring high-level enchantments is more expensive, and renaming an item has an additional surcharge. The anvil has a limit of 39 levels; beyond that, repairs are refused. This limit is not present in Creative mode.

Every time armor or tools are repaired, the minimum experience cost doubles (e.g., 1 level, 2 levels, 4 levels, 8 levels, etc.).

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
| Hitbox size | Height: 0.98 BlocksWidth: 0.98 Blocks |
|-------------|---------------------------------------|

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



| Name                            | Ingredients                       | Anvil usage                                    | Description                                                                                                                                                                                                 |
|---------------------------------|-----------------------------------|------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Map or Locator Map (zoomed out) | Mapor Locator Map +<br/>Paper     | Repair & Name MapLocator Map8                  | Bedrock Editiononly.Supplying 8 sheets of paper results in a zoomed-out version of the input map.                                                                                                           |
| Map or Locator Map (cloned)     | Mapor Locator Map +<br/>Empty Map | Repair & Name MapLocator MapMapLocator Map2222 | Bedrock Editiononly.Only one copy can be made at a time.The non-empty input map must be a locator map for the output to be a locator map. An empty locator map is the same as an empty map for this recipe. |
| Locator Map                     | Map+<br/>Compass                  | Repair & NameMap                               | Bedrock Editiononly.Maps crafted with only paper do not show the location marker; to add it, a compass must be added to the map.                                                                            |

### Becoming damaged
With each use, an anvil has a 12% chance to become damaged – degrading one stage at a time, first becoming chipped, then damaged, then eventually destroyed. An anvil typically survives for 25 uses on average or approximately one use per 1.24 iron ingots used in crafting the anvil.

An anvil can be damaged and destroyed from falling. If it falls from a height greater than one block, the chance of degrading by one stage is 5% × the number of blocks fallen.

The damage state does not affect the anvil's function, but only anvils of the same damage state can stack in inventory.

When an anvil is destroyed, the player automatically leaves the anvil GUI and it disappears.

## Creative mode
In creative mode, the anvil functions a little differently than other game modes:

- Any repair/enchant/rename operation may be done, regardless of the player's experience level. Incompatible enchantments are allowed as well (enchanting blocks etc.)
	- The experience cost is not taken from the player.
- The repair cost of toolsdoesstill increase.
	- It continues doubling with each repair, past the usual limit of 39 levels.
	- When it reaches the capacity of signed 32-bit integers, no repair cost is shown and the "product" item cannot be taken out of the anvil. Tools in this state also cannot be renamed or enchanted.
- Anvils are not damaged on use.

## Data values
### ID
Java Edition:

| Name          | Identifier      | Form         | Block tags | Item tags | Translation key                 |
|---------------|-----------------|--------------|------------|-----------|---------------------------------|
| Anvil         | `anvil`         | Block & Item | `anvil`    | `anvil`   | `block.minecraft.anvil`         |
| Chipped Anvil | `chipped_anvil` | Block & Item | `anvil`    | `anvil`   | `block.minecraft.chipped_anvil` |
| Damaged Anvil | `damaged_anvil` | Block & Item | `anvil`    | `anvil`   | `block.minecraft.damaged_anvil` |

Bedrock Edition:

| Name  | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key                                                                                  |
|-------|------------|------------|----------------------------|----------------|--------------------------------------------------------------------------------------------------|
| Anvil | `anvil`    | `145`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.anvil.intact.name`<br/>`tile.anvil.slightlyDamaged.name`<br/>`tile.anvil.veryDamaged.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:

| Name   | Default value | Allowed values                            | Description                                                                                                                                                                                                                                                                   |
|--------|---------------|-------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | An anvil pointing north or south is aligned with its long dimension pointing north–south.<br/>An anvil pointing east or west is aligned with its long dimension pointing east–west.<br/>This value is 90° clockwise from the direction a player faces while placing an anvil. |

Bedrock Edition:

| Name                         | Metadata Bits   | Default value | Allowed values                            | Values forMetadata Bits | Description                                                                                                                                                                                                                                                                   |
|------------------------------|-----------------|---------------|-------------------------------------------|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| damage                       | `0x4`<br/>`0x8` | `undamaged`   | `broken`                                  | `3`                     | Broken Anvil (inaccessible and unused, uses anvil base texture)                                                                                                                                                                                                               |
|                              |                 |               | `slightly_damaged`                        | `1`                     | Slightly Damaged Anvil.                                                                                                                                                                                                                                                       |
|                              |                 |               | `undamaged`                               | `0`                     | Anvil.                                                                                                                                                                                                                                                                        |
|                              |                 |               | `very_damaged`                            | `2`                     | Very Damaged Anvil.                                                                                                                                                                                                                                                           |
| minecraft:cardinal_direction | Not Supported   | `south`       | `east`<br/>`north`<br/>`south`<br/>`west` | `Unsupported`           | An anvil pointing north or south is aligned with its long dimension pointing north–south.<br/>An anvil pointing east or west is aligned with its long dimension pointing east–west.<br/>This value is 90° clockwise from the direction a player faces while placing an anvil. |



### Falling block entity
Main article: Falling Block
- Dynamic block entity data
	- 
		- 
		- Tags common to all entities
	- BlockState: The falling block represented by this entity.
		- Name: Theresource locationof the block.
		- Properties: Optional. Theblock statesof the block.
			- Name: The block state name and its value.
	- CancelDrop: 1 or 0 (true/false) - true if the block should be destroyed instead of placed after landing on a solid block. When true, the block is not dropped as an item, even if theDropItemtag is set to true. However, if the entity is deleted due to itsTimevalue being too high, this tag is ignored and an item is dropped depending on theDropItemtag.CancelDropdefaults to 1 for fallingsuspicious sandandsuspicious gravel, and 0 for the other vanilla falling blocks and any summoned falling block.
	- DropItem: 1 or 0 (true/false) – true if the block should drop as an item when it breaks. Any block that does not have an item formwith the same ID as the blockdoes not drop even if this is set.
	- FallHurtAmount: Multiplied by theFallDistanceto calculate the amount of damage to inflict. By default this value is 2for anvils, and 6for pointed dripstone.
	- FallHurtMax: The maximum hit points of damage to inflict on entities that intersect this falling block. For vanilla falling blocks, always 40× 20.
	- HurtEntities: 1 or 0 (true/false) – true if the block should hurt entities it falls on. Defaults to 1 foranvilsandpointed dripstoneand to 0 for the other vanilla falling blocks and any summoned falling block.
	- TileEntityData: Optional. The tags of the block entity for this block.
	- Time: The number of ticks the entity has existed. WhenTimegoes above 600, or above 100 while the block is at Y=-64 or is outside building height, the entity is deleted.

