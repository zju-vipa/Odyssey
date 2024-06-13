# Grindstone
A grindstone is a block that repairs items and tools as well as removing enchantments from them, except for curses. It also serves as a weaponsmith's job site block.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
- 2 Usage
	- 2.1 Repairing and disenchanting
	- 2.2 Changing profession
	- 2.3 Piston interactivity
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 Achievements
- 6 History
- 7 Issues
- 8 Trivia
- 9 Gallery
	- 9.1 Screenshots
- 10 References

## Obtaining
### Breaking
Grindstones can be obtained using any pickaxe. If mined without a pickaxe, it drops nothing.

| Block     | Grindstone            |
|-----------|-----------------------|
| Hardness  | 2                     |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 10                    |
| Wooden    | 1.5                   |
| Stone     | 0.75                  |
| Iron      | 0.5                   |
| Diamond   | 0.4                   |
| Netherite | 0.35                  |
| Golden    | 0.25                  |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


### Natural generation
A grindstone generated inside a weaponsmith shelter structure.
Grindstones naturally generate at village weaponsmiths and trail ruins.

### Crafting
| Ingredients                | Crafting recipe | Description                                                                                                                                                                                            |
|----------------------------|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Stick+Stone Slab+AnyPlanks |                 | InBedrock Edition, grindstone recipes built with crimson, warped, or mangrove planks can use a slab of almost any of the stone types including sandstone, quartz, and bricks.[more information needed] |

## Usage
A grindstone can be oriented in different directions. In Java Edition it doesn't need a supporting block. In Bedrock Edition it breaks if unsupported.

### Repairing and disenchanting
Interface for the grindstone
When used, an interface is displayed with two input slots and one output slot.

It resets the repair cost for items.

Placing one enchanted item in an input slot forms a new non-enchanted item of the same type and durability in the output slot. Removing the item from the output slot consumes the input item and drops some experience.

Placing two items (enchanted or not) of the same type in the input slots forms a new non-enchanted item of that type and with a durability equal to the sum of the durabilities of the two input items, plus 5% of the maximum durability of that item (rounded down), up to its maximum durability. Both input items are consumed in the process. If either input item was enchanted, then removing the output item drops some experience. If an armour trim is applied to the top slot of the grindstone when combining armour pieces, the trim will be preserved.

Amount of experience is related to the minimum modified enchantment level of enchantments. The final amount is a uniformly-distributed random amount between half the resulting sum of all enchantments (rounded up) and the sum itself.

As with all non-enchanted items, the new item has no prior work penalty. A grindstone cannot remove a curse. Grindstones also do not remove an item's custom name.

If the action is not applicable (e.g. only one non-enchanted item, or the two inputs are different items), the arrow displays a red cross like that of an anvil and no item appears in the output slot.

The following tables show the durability bonuses of various items:

| Armor      | Leather | Gold | Chainmail | Iron | Turtle shell | Diamond | Netherite |
|------------|---------|------|-----------|------|--------------|---------|-----------|
| Helmet     | 2       | 3    | 8         | 8    | 13           | 18      | 20        |
| Chestplate | 4       | 5    | 12        | 12   | N/A          | 26      | 29        |
| Leggings   | 3       | 5    | 11        | 11   | N/A          | 24      | 27        |
| Boots      | 3       | 4    | 9         | 9    | N/A          | 21      | 24        |


| Tools     |     |
|-----------|-----|
| Wood      | 3   |
| Gold      | 1   |
| Stone     | 6   |
| Iron      | 12  |
| Diamond   | 78  |
| Netherite | 101 |

| Miscellaneous tools and weapons |                           |
|---------------------------------|---------------------------|
| Bow                             | 19                        |
| Crossbow                        | 23                        |
| Trident                         | 12                        |
| Shield                          | 16                        |
| Elytra                          | 21                        |
| Carrot on a stick               | 1                         |
| Warped fungus on a stick        | 5                         |
| Fishing rod                     | 3‌[JE  only]19‌[BE  only] |
| Shears                          | 11                        |
| Flint and steel                 | 3                         |
| Brush                           | 3                         |


### Changing profession
If a village has a grindstone that has not been claimed by a villager, any villager who did not already pick a job site block has a chance to change their profession into weaponsmith.

### Piston interactivity
Grindstones cannot be pushed by pistons or pulled by sticky pistons.

## Data values
### ID
Java Edition:

| Name       | Identifier | Form         | Translation key            |
|------------|------------|--------------|----------------------------|
| Grindstone | grindstone | Block & Item | block.minecraft.grindstone |

Bedrock Edition:

| Name       | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key      |
|------------|------------|------------|----------------------------|----------------|----------------------|
| Grindstone | grindstone | 450        | Block & Giveable Item[i 2] | Identical[i 3] | tile.grindstone.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block states

Java Edition:

| Name   | Default value | Allowed values     | Description                                                                                                                            |
|--------|---------------|--------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| face   | wall          | ceilingfloorwall   | What the grindstone is attached to.                                                                                                    |
| facing | north         | eastnorthsouthwest | The direction the grindstone is facing.Opposite from the direction the player faces when placing a grindstone on the floor or ceiling. |

Bedrock Edition:

| Name       | Metadata Bits | Default value | Allowed values              | Values forMetadata Bits | Description                                                                                                                                                             |
|------------|---------------|---------------|-----------------------------|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| attachment | 0x40x8        | standing      | standinghangingsidemultiple | 0123                    | What the grindstone is attached to.                                                                                                                                     |
| direction  | 0x10x2        | 0             | 0123                        | 0123                    | The direction the grindstone is facing. Opposite from the direction a player faces when placing the block.0: South facing 1: West facing 2: North facing 3: East facing |



