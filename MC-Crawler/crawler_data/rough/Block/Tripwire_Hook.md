# Tripwire Hook
A tripwire hook is a block used to create a tripwire circuit, which requires two hooks and a straight horizontal line of 1-40 string. Both hooks in a valid circuit emit a redstone signal and power their attached blocks while any of the string is being touched by an entity, or if any string is broken without using shears.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Chest loot
	- 1.4 Crafting
	- 1.5 Fishing
- 2 Usage
	- 2.1 Crafting ingredient
	- 2.2 Redstone component
	- 2.3 Trading
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 Video
- 6 History
- 7 Issues
- 8 Gallery
	- 8.1 Screenshots
- 9 References
- 10 External links

## Obtaining
### Breaking
Tripwire hooks can be broken instantly using any tool, or without a tool.

A tripwire hook is also removed and drops itself as an item if:

- its attachment block is moved, removed, or destroyed
- waterflows into its space inJava Edition
- apistontries to push it or moves a block into its space

A tripwire hook is destroyed without dropping itself as an item if lava flows into its space.

### Natural generation
Four tripwire hooks are generated naturally in each jungle temple.

### Chest loot
| Item          | Structure        | Container | Quantity | Chance                         |
|---------------|------------------|-----------|----------|--------------------------------|
|               |                  |           |          | Java EditionandBedrock Edition |
| Tripwire Hook | Pillager Outpost | Chest     | 1–3      | 30.5%                          |

### Crafting
| Ingredients                          | Crafting recipe |
|--------------------------------------|-----------------|
| Iron Ingot+<br/>Stick+<br/>AnyPlanks | 2               |

### Fishing
Tripwire hooks can be obtained as a "junk" item from fishing.

## Usage
Tripwire hooks can be used as crafting ingredients or as redstone circuit components.

### Crafting ingredient
| Name          | Ingredients                                          | Crafting recipe |
|---------------|------------------------------------------------------|-----------------|
| Crossbow      | Stick+<br/>Iron Ingot+<br/>String+<br/>Tripwire Hook |                 |
| Trapped Chest | Tripwire Hook+<br/>Chest                             |                 |

### Redstone component
See also: Redstone circuit

A tripwire hook can be used to detect mobs, items, and other entities over a large area.

** Placement **
To place a tripwire hook, use thePlace Blockcontrol.
In order to function correctly, a tripwire hook must be part of a "tripwire circuit": astraightline of blocks consisting of a block with a tripwire hook attached to it, a "tripwire line" (1 to 40 blocks oftripwire), and a second tripwire hook attached to another block, with both tripwire hooks facing the tripwire.
To place tripwire, use thePlace Blockcontrolwith astring. Tripwire in a valid tripwire circuit has a short hitbox (0.09375 or 3/32 blocks high, with the bottom 0.0625 or 1/16 blocks above the block below), while tripwire not in a valid tripwire circuit has a taller hitbox (0.5 blocks high, bottom not raised).
A tripwire hook in an invalid tripwire circuit appears "folded", while a tripwire hook in a valid tripwire circuit appears extended straight. Tripwire lines from separate tripwire circuits can be placed next to each other (in parallel), above each other, and even intersecting each other.
** Activation **
A tripwire hook in a valid tripwire circuit activates when certainentities(players, mobs, items, etc.) intersect the tripwire hook's tripwire line "hitbox" (butnotthe tripwire hook itself), and deactivates when all entities leave or are removed from the tripwire line.
Entities that cannot activate a tripwire circuit include thrownpotions, some arrows,fireworks, thrownender pearls, and throwneyes of ender.
A tripwire hook also activates for 5 redstone ticks (0.5 seconds, barring lag) when any of its tripwires are destroyed, except whenshearsare used to destroy the tripwire.
Breaking the tripwire hook, or breaking the block it is attached to, does not generate a pulse.
** Behavior **
The tripwire hooks and the blocks they are attached to provide power, but the tripwire does not.
While active, a tripwire hook appears to move downward and it:
- powers any adjacentredstone dusttopower level15, including beneath the tripwire hook
- powers any adjacentredstone comparatorsorredstone repeatersfacing away from the tripwire hook to power level 15
- strongly powers its attachment block to power level 15
- activates any adjacentmechanism components, including above or below, such aspistons,redstone lamps, etc.

Tripwire produces no power itself, but its state change can be detected with anobserver.
Although destroying tripwire with shears cannot activate a tripwire hook, it changes the tripwire hook's block state (its "attached" state fromtruetofalse), which can be detected with an observer.
### Trading
Master-level fletcher villagers have a 2⁄3 chance to buy 8 tripwire hooks for an emerald as part of their trades in Java Edition, and always offer the trade in Bedrock Edition.

## Data values
### ID
Java Edition:

| Name          | Identifier      | Form         | Translation key                 |
|---------------|-----------------|--------------|---------------------------------|
| Tripwire Hook | `tripwire_hook` | Block & Item | `block.minecraft.tripwire_hook` |

Bedrock Edition:

| Name          | Identifier      | Numeric ID | Form                       | Item ID[i 1]   | Translation key           |
|---------------|-----------------|------------|----------------------------|----------------|---------------------------|
| Tripwire Hook | `tripwire_hook` | `131`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.tripwire_hook.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:

| Name     | Default value | Allowed values                            | Description                                                                                                                                                            |
|----------|---------------|-------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| attached | `false`       | `false`<br/>`true`                        | True if the tripwire hook is connected to a valid tripwire circuit.                                                                                                    |
| facing   | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction in which the tripwire hook juts out from the block it is attached to.<br/>For example, a tripwire hook facing north is attached to a block to its south. |
| powered  | `false`       | `false`<br/>`true`                        | True if the tripwire hook is active.                                                                                                                                   |

Bedrock Edition:

| Name         | Metadata Bits   | Default value | Allowed values              | Values forMetadata Bits     | Description                                                                                                                                                                                                                                                                       |
|--------------|-----------------|---------------|-----------------------------|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| attached_bit | `0x4`           | `false`       | `false`<br/>`true`          | `0`<br/>`1`                 | True if the tripwire hook is connected to a valid tripwire circuit.                                                                                                                                                                                                               |
| direction    | `0x1`<br/>`0x2` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3` | `0`<br/>`1`<br/>`2`<br/>`3` | The direction in which the tripwire hook juts out from the block it is attached to.0: Tripwire hook on block side facing south<br/>1: Tripwire hook on block side facing west<br/>2: Tripwire hook on block side facing north<br/>3: Tripwire hook on block side facing east<br/> |
| powered_bit  | `0x8`           | `false`       | `false`<br/>`true`          | `0`<br/>`1`                 | True if the tripwire hook is active.                                                                                                                                                                                                                                              |



