# Bundle
A bundle is an item that can store up to a stack's worth of mixed item types within itself in a single inventory slot. Items that stack to 16 occupy more space within the bundle, and items that do not stack occupy the entire bundle without allowing space for any other items.

## Contents
- 1 Obtaining
	- 1.1 Crafting
- 2 Usage
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Item data
- 5 History
- 6 Issues
- 7 Gallery
	- 7.1 Screenshots
- 8 References

## Obtaining
### Crafting
| Ingredients             | Crafting recipe | Description                  |
|-------------------------|-----------------|------------------------------|
| String+<br/>Rabbit Hide |                 | [only experimental "bundle"] |

## Usage


6416464
Item stack sizes (top row) and the number of bundle slots they take up (middle row). Sticks stack to 64, so they take up one bundle slot; ender pearls stack to 16, so they take up four; and swords do not stack, so they take up the whole bundle. So, for instance, a bundle may have 32 sticks and 8 ender pearls inside (bottom), which take up a total of (32×1)+(8×4)=64 bundle slots.


Hovering the mouse over a bundle filled with mob loot, nearly full, with 61 items.
Bundles are used to store different item types in the same inventory slot. This does not, however, increase the total capacity of the slot: each bundle has 64 "bundle slots" and each item placed in the bundle takes up these slots similar to how they take up space in a normal inventory slot: items that stack to 64 take up 1 bundle slot, items that stack to 16 (for example, eggs) take up 4, and items that do not stack (such as tools/weapons/armor) take up the whole bundle, all 64 slots.

Although bundles themselves cannot be stacked, a bundle can be placed inside another (nested): the inner bundle itself uses 4 slots plus the number of slots already occupied by the items in that bundle.[1]

To place items inside a bundle, either (1) pick up the bundle in the inventory and right-click on the item(s) to be placed inside or (2) pick up the item(s) and right-click on the bundle. When placing bundles inside another bundle, the interface uses the first method: picking up bundle A and right clicking on bundle B attempts to store bundle B inside A.

Bundles can be used inside the inventory to take out the last item put in. In this way, items are accessible LIFO (last in, first out). When used outside the inventory, it dumps all the items out into the world.

Hovering over the bundle shows its contained items in its inventory slots. The number of bundle slots used is displayed as <fullness>/64 in the tooltip. If the bundle is full, then the empty slots are greyed out with an .

Shulker boxes cannot be placed inside of bundles.

## Data values
### ID
Java Edition:

| Name   | Identifier | Form | Translation key         |
|--------|------------|------|-------------------------|
| Bundle | `bundle`   | Item | `item.minecraft.bundle` |

### Item data
- tag: The root object.

- 
	- Items: List of items in the bundle.
		- : An item in the bundle.
			- 
			- Tags common to all items

