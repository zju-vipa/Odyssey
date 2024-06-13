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

