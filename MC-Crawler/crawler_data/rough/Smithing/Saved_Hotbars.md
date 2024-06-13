# Saved Hotbars
The Saved Hotbars menu is a feature in Java Edition that allows the Creative mode player to save selectable hotbar slots.

## Contents
- 1 Use
- 2 Controls
- 3 File format
- 4 History

## Use
Up to 9 hotbars can be saved.

The player can save their current row using (by default) C + a number 1 through 9 corresponding to which row in the inventory menu the hotbar row should be saved into. For instance, putting items in the hotbar and pressing C + 1 saves the player's current hotbar into row 1 of the Saved Hotbars inventory menu. This row can then be loaded into the hotbar using (by default) X + 1. Note: the inventory must be closed in order to save or load hotbars.

By default, the 9 slots are marked with an informational paper item with instructions on how to save slots as its custom name.
If an empty hotbar is saved, it clears the bookmarked hotbar and puts back the paper into the respective slot.

The Saved Hotbar menu is common between all worlds the player loads – it is not saved locally to any individual world.

## Controls
The Saved Hotbar controls can be found in the "Creative Mode" section of the "Key Binds" options menu. The two options are:

- Load Hotbar Activator (default key:X)
- Save Hotbar Activator (default key:C)

## File format
Hotbars are saved into the hotbar.nbt file, an uncompressed NBT file found in root of the .minecraft folder, that is created the first time a hotbar is saved.

- The root tag.
	- 0: List of nine tags, one for each hotbar slot. This is an ordered list, with the first child tag corresponding to the first slot in the hotbar.
		- 0An item in the inventory. For slots containing no items, this isminecraft:airwith aCountof zero.
			- Seeitem format.
		- 1–8See above.
	- 1–8: See above.
	- DataVersion: Thedata version.

Note that nine  List tags, 0–8, are created regardless of how many hotbars have been saved.

