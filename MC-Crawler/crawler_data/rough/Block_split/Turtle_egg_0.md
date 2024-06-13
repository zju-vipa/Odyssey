# Turtle Egg
A turtle egg (in Java Edition) or sea turtle egg (in Bedrock Edition) is a block containing 1–4 eggs that each hatch into a baby turtle.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Post-generation
- 2 Trampling
- 3 Usage
	- 3.1 Placement
	- 3.2 Hatching
- 4 Sounds
	- 4.1 Generic
	- 4.2 Unique
- 5 Data values
	- 5.1 ID
	- 5.2 Block states
- 6 History
- 7 Issues
- 8 Trivia
- 9 Gallery
	- 9.1 Renders
	- 9.2 Screenshots
- 10 Notes
- 11 References

## Obtaining
### Breaking
A turtle egg drops as an item when mined using any tool[1] with the Silk Touch enchantment. If broken without the enchantment, pushed by a piston, or broken by a player or mob falling onto it, the egg breaks without dropping anything.

When mining a cluster of more than one turtle egg, the eggs break one at a time, instead of all at once. This is different from other clustered blocks, such as sea pickles or candles.

Breaking a cracked turtle egg with a Silk Touch tool resets the growth stage when the egg is placed on a different block.

| Block    | Turtle Egg          |
|----------|---------------------|
| Hardness | 0.5                 |
|          | Breakingtime (secs) |
| Default  | 0.75                |

### Post-generation
Main article: Turtle § Egg laying
When two turtles are bred with seagrass, one of them returns to its home beach, and after several seconds it lays a cluster of 1–4 eggs on the sand.

## Trampling
A zombie stomping on turtle eggs.
Two husks breaking turtle eggs by trampling on them.
Turtle eggs can be trampled by living entities (players, mobs, livestock, etc.) that fall onto or stand on top of them. Eggs in a cluster of eggs are trampled one at a time until no eggs remain.

Eggs can be trampled by a crouch-walking (or "sneaking") player. Though eggs cannot be trampled by non-living entities like arrows, they can be trampled by armor stands. When a falling block such as an anvil or sand block is dropped onto an egg, the falling block is dropped and turned into an item leaving the egg unharmed.

Zombies and their variants (husks, drowned, zombie villagers and zombified piglins) seek out and trample turtle eggs that have 2 blocks of air above them unless /gamerule mobGriefing is false. The range of detection is a 47×7×47‌[JE  only] or 11×5×11‌[BE  only] box centered on the block the mob is standing on. When a player in Survival or Adventure Game-mode is nearby (also includes iron golems and villagers), the zombie prefers to attack the player rather than trampling the turtle egg.

Unlike zombies and their variants, other mobs do not seek out turtle eggs to trample them. However, they can still break turtle eggs by accident. Any entity (even an anvil) falling onto an egg has a 1⁄3 chance of trampling the egg. Any entity standing on top of an egg has a 1⁄100 chance each game tick of trampling the egg.

Turtles cannot break turtle eggs, even when they are on top of them.

## Usage
### Placement
Up to 4 turtle eggs can be placed in a cluster on one block. Even though turtle eggs can be placed on any block, they only hatch on sand blocks. When adding more eggs to an existing cluster, they retain their hatching progress.

Turtle eggs do not require a supporting block below and unlike dragon eggs are not affected by gravity. Eggs are also capable of supporting lanterns hanging under them.[2]

### Hatching
Turtle eggs hatch on sand, red sand or suspicious sand. Eggs crack over time and hatch after cracking three times. Eggs hatch significantly faster at nighttime.

Turtle eggs have a 1/500 chance of cracking if they are randomly ticked during the day. However, if the in-game time is between 21600 and 22550 ticks (3:36 am and 4:33 am), then turtle eggs always crack when random ticked. This is a roughly 48-second window for the player. About 95% of eggs crack or hatch during this night-time window. On average, an egg hatches in 4-5 nights. 90% of eggs hatch in 7 nights or less.[3]

When a cluster of eggs hatches, all eggs hatch simultaneously.

Eggs do not progress toward hatching if the player is not within 128 blocks of horizontal distance of the chunk that the egg is located in. This is due to the egg's chunk not receiving random ticks.

## Data values
### ID
Java Edition:

| Name       | Identifier   | Form         | Translation key              |
|------------|--------------|--------------|------------------------------|
| Turtle Egg | `turtle_egg` | Block & Item | `block.minecraft.turtle_egg` |

Bedrock Edition:

| Name           | Identifier   | Numeric ID | Form                       | Item ID[i 1]   | Translation key        |
|----------------|--------------|------------|----------------------------|----------------|------------------------|
| Sea Turtle Egg | `turtle_egg` | `414`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.turtle_egg.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:

| Name  | Default value | Allowed values              | Description                                                                          |
|-------|---------------|-----------------------------|--------------------------------------------------------------------------------------|
| eggs  | `1`           | `1`<br/>`2`<br/>`3`<br/>`4` | Number of eggs.                                                                      |
| hatch | `0`           | `0`<br/>`1`<br/>`2`         | Determines how close an egg is to hatching; starts at 0 and is randomly incremented. |

Bedrock Edition:

| Name             | Metadata Bits   | Default value | Allowed values                                         | Values forMetadata Bits     | Description                                                                                  |
|------------------|-----------------|---------------|--------------------------------------------------------|-----------------------------|----------------------------------------------------------------------------------------------|
| turtle_egg_count | `0x1`<br/>`0x2` | `one_egg`     | `one_egg`<br/>`two_egg`<br/>`three_egg`<br/>`four_egg` | `0`<br/>`1`<br/>`2`<br/>`3` | Number of eggs.                                                                              |
| cracked_state    | `0x4`<br/>`0x8` | `no_cracks`   | `no_cracks`<br/>`cracked`<br/>`max_cracked`            | `0`<br/>`1`<br/>`2`         | Determines how close an egg is to hatching; starts at no cracks and is randomly incremented. |



## Notes



