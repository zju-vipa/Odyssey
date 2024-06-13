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

