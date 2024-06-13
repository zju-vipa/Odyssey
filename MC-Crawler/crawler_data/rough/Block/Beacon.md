# Beacon
A beacon is a block that projects a beam skyward, and can provide beneficial status effects to players in a radius around it when placed on top of a solid pyramid base constructed from iron, gold, diamond, emerald or netherite blocks.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Crafting
- 2 Usage
	- 2.1 Activation
		- 2.1.1 Pyramids
	- 2.2 Beam
		- 2.2.1 Colors
	- 2.3 Powers
		- 2.3.1 Range
	- 2.4 Light source
	- 2.5 Piston interactivity
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block data
- 5 Achievements
- 6 Advancements
- 7 Video
- 8 History
- 9 Issues
- 10 Trivia
- 11 Gallery
	- 11.1 Renders
	- 11.2 Screenshots
	- 11.3 Development images
	- 11.4 In other media
- 12 References
- 13 See also

## Obtaining
### Breaking
A beacon can be mined successfully by hand or with any tool. When destroyed by an explosion, the block always drops as an item.

| Block    | Beacon              |
|----------|---------------------|
| Hardness | 3                   |
|          | Breakingtime (secs) |
| Default  | 4.5                 |

### Crafting
| Name   | Ingredients                          | Crafting recipe |
|--------|--------------------------------------|-----------------|
| Beacon | Glass+<br/>Nether Star+<br/>Obsidian |                 |

## Usage
When "activated", beacon blocks provide two unique functions: 

- A landmark beam reaching into the sky, which can be visible from far away.
- Powers, which give players status effects within a certain range.

Additionally, in Bedrock Edition beacons can also be waterlogged and conduct redstone power at the same time.

### Activation
The beacon base can be made of the different mineral blocks combined.
In order to activate a beacon, the beacon must meet the following requirements:

- Beacons require an unobstructed view of the sky.Transparentblocks (glass, water, etc.) and bedrock (the nether ceiling)  are allowed.
- The beacon is on top of a pyramid constructed fromiron blocks,gold blocks,emerald blocks,diamond blocks, and/ornetherite blocks.

#### Pyramids
For other pyramid structures, see Pyramid.

The four possible pyramid arrangements when using the beacon block. From left to right the pyramid structures decrease in complexity and strength.
Pyramids are the structures required to activate beacons. There are four possible pyramid heights. More pyramid levels make more powers available in a wider affected vicinity. The type of mineral block used to build the pyramid is entirely cosmetic and has no functional effect. Several different block types can be mixed without affecting functionality. If the pyramid is damaged so that the beacon deactivates, the previously-set powers resume their effects upon reactivation when the pyramid is repaired. This applies to piston-altered pyramids as well. 

| Level | Mineral blocks             | Materials                  | Layers                     |
|-------|----------------------------|----------------------------|----------------------------|
| 1     | 9                          | 81 (1 stack + 17 items)    | 3×3, beacon                |
| 2     | 34                         | 306 (4 stacks + 50 items)  | 5×5, 3×3, beacon           |
| 3     | 83 (1 stack + 19 blocks)   | 747 (11 stacks + 43 items) | 7×7, 5×5, 3×3, beacon      |
| 4     | 164 (2 stacks + 36 blocks) | 1476 (23 stacks + 4 items) | 9×9, 7×7, 5×5, 3×3, beacon |

This six-beacon pyramid provides all six effects from a single structure using the fewest mineral blocks possible.
Multiple beacons can make use of the same specific mineral blocks below them. Combined pyramids do not need to be symmetrical. The image to the right shows a 6-beacon (2 by 3) pyramid. It requires a total of 244 mineral blocks, with a base layer of 10 by 11.

| Level | Mineral blocks             | Materials                   | Layers                        |
|-------|----------------------------|-----------------------------|-------------------------------|
| 1     | 20                         | 180 (2 stacks + 52 items)   | 4×5, beacons                  |
| 2     | 62                         | 558 (8 stacks + 46 items)   | 6×7, 4×5, beacons             |
| 3     | 134 (2 stacks + 6 blocks)  | 1206 (18 stacks + 54 items) | 8×9, 6×7, 4×5, beacons        |
| 4     | 244 (3 stacks + 52 blocks) | 2196 (34 stacks + 20 items) | 10×11, 8×9, 6×7, 4×5, beacons |

### Beam
A vertical beam appears from a beacon if the beacon is activated, extending from the beacon block up to beyond the top of the world.

- InJava Edition, the beam is visible up to 256 blocks away.
- InBedrock Edition, the beam is visible up to 64 blocks away, regardless of how high the render distance is set.[1]

#### Colors
The color of the beam may be changed by placing blocks of stained glass or stained glass panes anywhere above the beacon block. The beam changes colors according to the colors of glass placed above it: the first block sets the beam color, while each additional block sets the color by averaging the red, green, and blue components of the current beam color and the block's color. The color values are the same as those for the corresponding dye. This also works using hardened stained glass and hardened stained glass panes.‌[Bedrock Edition and Minecraft Education  only] Stained glass panes have the same effect on the beam as stained glass blocks.

The resulting beam color can be found as C→=12n+1(c0→+∑i=1n2i−1ci→) where ci→ is the sequence of glass colors (c0→ corresponds to the lowest block and cn→ to the highest one).

Beacon beams cannot go through most blocks, but can go through bedrock (to allow beacons to be used in the Nether) and end portal frames.

Using just 15 colors of stained glass, It is possible to make all colors, for example; red + white stained glass above a beacon makes pink; in addition to this, the more white that is added, the lighter the color.

An interactive widget is being loaded. If this does not work for you, please reload the page or check if JavaScript is enabled.
### Powers
See also: Effect

The GUI shown when pressing use on the block.
Once the beacon is emitting a beam, it can then be fed one iron ingot, gold ingot, emerald, diamond, or netherite ingot to select the status effects given to players within range of the beacon. This is done through the beacon's GUI, displayed by pressing use while looking at the beacon block. It doesn't matter which of the items is fed into the beacon.

In the GUI, the player places the item to be fed in the empty slot and clicks an effect from the "Primary Power" section on the left. If the beacon is sitting on a 4-level pyramid, the "Secondary Power" section on the right also becomes active. The player can then choose either to turn on the Regeneration power in addition to the Primary Power or to raise the primary power to Level II. The user clicks the "Done" button (green checkmark), the item is consumed, and the power(s) become activated, with the outline of the effect on the HUD having a blue outline.‌[JE  only] To change the beacon's powers, this process must be followed again, consuming another ingot or gem.

If the pyramid is broken, effects deactivate or weaken depending on the level of the pyramid that is no longer complete. Upon restoration of the pyramid, the originally selected power returns without the need to spend another item.

The five primary powers are: 

- SpeedI: Increased movement speed.
- HasteI: Increased mining and attack speed.
- ResistanceI: Decreased nearly all incoming damage (2-level pyramid required).
- Jump BoostI: Increased jumping distance and height (2-level pyramid required).
- StrengthI: Increased melee damage (3-level pyramid required).

The secondary powers available with a 4-level pyramid are:

- RegenerationI: Regenerates health.
- Increasing the primary power to level II.

It is also possible to combine two different primary Level I powers:‌[Java Edition  only]

- select a primary power in the left panel
- select the Level II option in the right panel
- select the second desired power back in the left panel

Only one of the two powers appear to be selected, although both effects are active.[2]

Every four seconds, the selected powers are applied with a duration of 9 seconds, plus 2 seconds per pyramid level, to all players in range. Thus, when powers are changed or a player travels outside the area-of-effect, the powers persist for 5–9 seconds, or 13-17 seconds with a full pyramid.

#### Range
The beacon affects an area in the shape of a square column, which reaches downward and out to each side at a range determined by the size of the pyramid base (see table below), and upward a distance of that range + the height of this dimension blocks.

The effect duration from the beacon is also determined by the size of the pyramid base (9 + Pyramid size * 2).

The range of the beacon effect is limited by the simulation distance. As such, on simulation distance of 4 with a level 4 pyramid, the effect does not reach the chunks on the corners of the beacon range.

The distance from the player to the beacon block does not affect the intensity of the status effect.

| Pyramid size | Effect range(blocks) | Effect duration(seconds) |
|--------------|----------------------|--------------------------|
| 1 level      | 20                   | 11                       |
| 2 levels     | 30                   | 13                       |
| 3 levels     | 40                   | 15                       |
| 4 levels     | 50                   | 17                       |

### Light source
Beacon blocks can function as light sources, emitting a light level 15. Like other light sources, they melt snow and ice.

### Piston interactivity
Beacons cannot be pushed or pulled by pistons or sticky pistons.

## Data values
### ID
Java Edition:

| Name   | Identifier | Form         | Translation key          |
|--------|------------|--------------|--------------------------|
| Beacon | `beacon`   | Block & Item | `block.minecraft.beacon` |

| Name         | Identifier |
|--------------|------------|
| Block entity | `beacon`   |

Bedrock Edition:

| Name   | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key    |
|--------|------------|------------|----------------------------|----------------|--------------------|
| Beacon | `beacon`   | `138`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.beacon.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

| Name         | Savegame ID |
|--------------|-------------|
| Block entity | `Beacon`    |

### Block data
A beacon has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format

- Block entity data
	- 
	- Tags common to all block entities
	- CustomName: Optional. The name of this beacon in JSON text component, which appears when attempting to open it, while it is locked.
	- 
	- Lock: Optional. When not blank, prevents the container from being opened unless the opener is holding an item whose name matches this string.
	- primary_effect: Optional. The primary effect selected, seePotion effectsfor resource locations. Cannot be set to an effect that beacons do not normally use. Although Regeneration cannot normally be chosen as the primary effect, setting this value tominecraft:regenerationworks and even allows Regeneration II to be chosen as the secondary via the normal beacon GUI.
	- secondary_effect: Optional. The secondary effect selected, seePotion effectsfor resource locations. Cannot be set to an effect that beacons do not normally use. When set without a primary effect, does nothing. When set to the same as the primary, the effect is given at level 2 (the normally available behavior for 5 effects). When set to a different value than the primary (normally only Regeneration), gives the effect at level 1.

Bedrock Edition:

SeeBedrock Edition level format/Block entity format.
