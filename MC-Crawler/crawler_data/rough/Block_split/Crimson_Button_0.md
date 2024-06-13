# Wooden Button
A wooden button is a variant of the button that produces a temporary redstone signal when pressed. Wooden buttons come in every variation of wood, and all of them are non-solid blocks. They are activated either by a player interacting with the button or when hit by an arrow or trident. They remain pressed for longer than a stone button.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
- 2 Usage
	- 2.1 Placement
	- 2.2 Redstone power
		- 2.2.1 Activation
		- 2.2.2 Behavior
	- 2.3 Fuel
- 3 Sounds
	- 3.1 Generic
		- 3.1.1 Normal wood
		- 3.1.2 Cherry wood
		- 3.1.3 Bamboo wood
		- 3.1.4 Nether wood
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Gallery
	- 6.1 Renders

## Obtaining
### Breaking
A wooden button is most easily broken with an axe. It drops itself as an item when broken using any tool.

| Block     | Wooden Button         |
|-----------|-----------------------|
| Hardness  | 0.5                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 0.75                  |
| Wooden    | 0.4                   |
| Stone     | 0.2                   |
| Iron      | 0.15                  |
| Diamond   | 0.1                   |
| Netherite | 0.1                   |
| Golden    | 0.1                   |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

A button is removed and drops as an item if:

- its attachment block is moved, removed, or destroyed.
- waterorlavaflows into its space.‌[Java Edition  only]
- apistontries to push it or moves a block into its space.

### Natural generation
Jungle buttons generate naturally on house walls in desert villages.

### Crafting
Buttons can be crafted from planks for a matching wood-type button.

| Ingredients    | Crafting recipe |
|----------------|-----------------|
| MatchingPlanks |                 |

## Usage
See also: Redstone circuit

### Placement
Buttons can be placed by using them on a surface.

They can be attached to the side, bottom and top of any full opaque block.

If placed on the top or bottom of a block, the button can face any direction.‌[Java Edition  only]

It can also be attached to the top of a fence in Bedrock Edition.

More information about placement on transparent blocks can be found at Opacity/Placement.

### Redstone power
A button can be used as a monostable redstone power source (it automatically deactivates shortly after being activated).

#### Activation
Buttons are usually in an inactive state, but can be temporarily activated by players using it. A wooden button can also be activated by a fired arrow or a thrown trident if its collision box touched the button.

Mobs cannot activate buttons directly, but arrows fired by skeletons or dispensers can activate wooden buttons.

#### Behavior
When activated, a wooden button remains active for 1.5 seconds (15 redstone ticks; 30 game ticks).
A wooden button activated by a fired arrow or a thrown trident remains active until the arrow or trident despawns (after 1 minute) or is picked up by a player.

While active, a button:

- powers any adjacentredstone dusttopower level15, including beneath the button
- powers any adjacentredstone comparatorsorredstone repeatersfacing away from the button to power level 15
- strongly powers its attachment block to power level 15
- activates any adjacentmechanism components, including above or below, such aspistons,redstone lamps, etc.

When a button changes state it provides a redstone update to all redstone components adjacent to itself (including above and below), and to all redstone components adjacent to its attachment block.

### Fuel
Overworld wooden buttons can be used as a fuel source in furnaces, smelting 0.5 items per button. Nether wood buttons (crimson and warped), cannot be used as fuel in a furnace.

## Data values
### ID
Java Edition:

| Name            | Identifier        | Form         | Block tags                                              | Item tags                                               | Translation key                   |
|-----------------|-------------------|--------------|---------------------------------------------------------|---------------------------------------------------------|-----------------------------------|
| Oak Button      | `oak_button`      | Block & Item | `buttons`<br/>`wooden_buttons`                          | `buttons`<br/>`wooden_buttons`                          | `block.minecraft.oak_button`      |
| Spruce Button   | `spruce_button`   | Block & Item | `buttons`<br/>`wooden_buttons`                          | `buttons`<br/>`wooden_buttons`                          | `block.minecraft.spruce_button`   |
| Birch Button    | `birch_button`    | Block & Item | `buttons`<br/>`wooden_buttons`                          | `buttons`<br/>`wooden_buttons`                          | `block.minecraft.birch_button`    |
| Jungle Button   | `jungle_button`   | Block & Item | `buttons`<br/>`wooden_buttons`                          | `buttons`<br/>`wooden_buttons`                          | `block.minecraft.jungle_button`   |
| Acacia Button   | `acacia_button`   | Block & Item | `buttons`<br/>`wooden_buttons`                          | `buttons`<br/>`wooden_buttons`                          | `block.minecraft.acacia_button`   |
| Dark Oak Button | `dark_oak_button` | Block & Item | `buttons`<br/>`wooden_buttons`                          | `buttons`<br/>`wooden_buttons`                          | `block.minecraft.dark_oak_button` |
| Mangrove Button | `mangrove_button` | Block & Item | `buttons`<br/>`wooden_buttons`                          | `buttons`<br/>`wooden_buttons`                          | `block.minecraft.mangrove_button` |
| Cherry Button   | `cherry_button`   | Block & Item | `buttons`<br/>`wooden_buttons`                          | `buttons`<br/>`wooden_buttons`                          | `block.minecraft.cherry_button`   |
| Bamboo Button   | `bamboo_button`   | Block & Item | `buttons`<br/>`wooden_buttons`                          | `buttons`<br/>`wooden_buttons`                          | `block.minecraft.bamboo_button`   |
| Crimson Button  | `crimson_button`  | Block & Item | `buttons`<br/>`non_flammable_wood`<br/>`wooden_buttons` | `buttons`<br/>`non_flammable_wood`<br/>`wooden_buttons` | `block.minecraft.crimson_button`  |
| Warped Button   | `warped_button`   | Block & Item | `buttons`<br/>`non_flammable_wood`<br/>`wooden_buttons` | `buttons`<br/>`non_flammable_wood`<br/>`wooden_buttons` | `block.minecraft.warped_button`   |

Bedrock Edition:

| Name            | Identifier        | Numeric ID | Form                       | Item ID[i 1]   | Translation key             |
|-----------------|-------------------|------------|----------------------------|----------------|-----------------------------|
| Oak Button      | `wooden_button`   | `143`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.wooden_button.name`   |
| Spruce Button   | `spruce_button`   | `399`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.spruce_button.name`   |
| Birch Button    | `birch_button`    | `396`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.birch_button.name`    |
| Jungle Button   | `jungle_button`   | `398`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.jungle_button.name`   |
| Acacia Button   | `acacia_button`   | `395`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.acacia_button.name`   |
| Dark Oak Button | `dark_oak_button` | `397`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.dark_oak_button.name` |
| Mangrove Button | `mangrove_button` | `-487`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.mangrove_button.name` |
| Cherry Button   | `cherry_button`   | `-530`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.cherry_button.name`   |
| Bamboo Button   | `bamboo_button`   | `-511`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.bamboo_button.name`   |
| Crimson Button  | `crimson_button`  | `515`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.crimson_button.name`  |
| Warped Button   | `warped_button`   | `516`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.warped_button.name`   |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑ a b c d e f g h i j kAvailable with /give command.
3. ↑ a b c d e f g h i j kThe block's direct item form has the same id as the block.

