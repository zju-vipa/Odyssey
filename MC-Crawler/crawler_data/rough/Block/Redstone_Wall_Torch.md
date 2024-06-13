# Redstone Torch
A redstone torch is a non-solid block that produces a full-strength redstone signal on all sides adjacent to it, except for its attached block, and can power the block directly above it. It deactivates while the block it is attached to is powered.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
- 2 Usage
	- 2.1 Crafting ingredient
	- 2.2 Redstone component
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
	- 5.1 Unlit redstone torch "item"
		- 5.1.1 Names
- 6 Trivia
- 7 Issues
- 8 Gallery
	- 8.1 Renders
		- 8.1.1 Java Edition
		- 8.1.2 Bedrock Edition
	- 8.2 In other media
- 9 References

## Obtaining
In Java Edition, the inactive redstone torch cannot be obtained as an item. In Bedrock Edition, it can be obtained via inventory editing.

### Breaking
A redstone torch can be broken instantly using any tool, or without a tool, and drops itself as an item.

A redstone torch is removed and drops as an item if:

- its attachment block is moved, removed, or destroyed
- waterorlavaflows into its space
- apistonpushes it or moves a block into its space

### Natural generation
A single redstone torch is found inside each igloo. In ancient cities, multiple redstone torches can be found integrated into circuitry.

### Crafting
| Ingredients              | Crafting recipe |
|--------------------------|-----------------|
| Redstone Dust+<br/>Stick |                 |

## Usage
### Crafting ingredient
Redstone torches can be used to craft activator rails, redstone comparators, and redstone repeaters.

| Name                | Ingredients                                  | Crafting recipe |
|---------------------|----------------------------------------------|-----------------|
| Activator Rail      | Iron Ingot+<br/>Stick+<br/>Redstone Torch    | 6               |
| Redstone Comparator | Redstone Torch+<br/>Nether Quartz+<br/>Stone |                 |
| Redstone Repeater   | Redstone Torch+<br/>Redstone Dust+<br/>Stone |                 |

### Redstone component
See also: Redstone circuit

Redstone torches can be used to power blocks and transmission components such as redstone dust, activate mechanism components such as pistons, or invert redstone signals like a NOT Gate. 

** Placement **
See also: Opacity/Placement

Examples of redstone torch placement and behavior.
To place a redstone torch, use thePlace Blockcontrolwhile aiming at the surface to which the redstone torch should be attached.
A redstone torch can be attached to:
- thetoporsideof any full solidopaqueblock (stone, dirt, blocks of gold, etc.), including full-block mechanism components (command blocks,dispensers,droppers,note blocks, andredstone lamps)
- thetop onlyorside onlyof certain block. SeeOpacity/Placement.

Redstone torches cannot be attached to the bottoms of any blocks.
Attempting to attach a redstone torch to an invalid surface can cause it to "snap" to a valid surface adjacent to the same space. For example, if a fence is on the ground, attempting to attach a redstone torch to thesideof the fence causes the redstone torch to be attached to thetopof the ground next to the fence instead.
** Activation **
A redstone torch is active unless the block it is attached to is powered. Effectively, a redstone torchinvertsthe signal applied to its attachment block: power level 0 is changed to 15 and power levels 1 to 15 are changed to 0 (for an alternative that produces a greater range of output power levels, consider aredstone comparatorin subtraction mode).
Walls, fences, glass, slabs, hoppers, and stairs cannot be powered so redstone torches attached to them cannot be deactivated.
A redstone torch takes 1 redstone tick (2 game ticks, or 0.1 seconds barring lag) to change state and usually does not respond to 1-tick fluctuations of power.
** Behavior **
While active, a redstone torch:
- powers adjacentredstone dusttopower level15, including beneath the redstone torch if it is attached to the side of a block
- powers adjacentredstone comparatorsorredstone repeatersfacing away from the redstone torch to power level 15
- strongly powers a full solid opaqueblockabove the redstone torch to power level 15 (but not next to or below it)
- activates adjacentmechanism components, including above or below, such aspistons,redstone lamps, etc.
- produces "reddust"particles

A redstone torch never affects the block it is attached to, even if it is a mechanism component. For example, a redstone torch attached to a redstone lamp does not activate the lamp. It has to power something like redstone dust for the component to be powered.
A redstone torch experiences "burn-out" when it is forced to change state (by powering and de-powering the block it is attached to) more than eight times in 60 game ticks (three seconds, barring lag). After burning out, a redstone torch produces a "smoke"particleand a hiss similar to an extinguished fire, deactivates, and then ignores attempts to change its state until the number of state changes in the last 60 game ticks drops to fewer than eight—after that it re-activates when it receives a block update (an adjacent block changing its state) or aredstone updatethat would not normally deactivate the redstone torch. There is no limit on how often a single redstone torch can burn out.
## Data values
### ID
Java Edition:

| Name                | Identifier            | Form         | Block tags           | Translation key                       |
|---------------------|-----------------------|--------------|----------------------|---------------------------------------|
| Redstone Torch      | `redstone_torch`      | Block & Item | `wall_post_override` | `block.minecraft.redstone_torch`      |
| Redstone Wall Torch | `redstone_wall_torch` | Block        | None                 | `block.minecraft.redstone_wall_torch` |

Bedrock Edition:

| Name                 | Identifier             | Numeric ID | Form                         | Item ID[i 1]   | Translation key                  |
|----------------------|------------------------|------------|------------------------------|----------------|----------------------------------|
| Redstone Torch       | `redstone_torch`       | `76`       | Block & Giveable Item[i 2]   | Identical[i 3] | `tile.redstone_torch.name`       |
| Unlit Redstone Torch | `unlit_redstone_torch` | `75`       | Block & Ungiveable Item[i 4] | Identical[i 3] | `tile.unlit_redstone_torch.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑ a bThe block's direct item form has the same id as the block.
4. ↑Unavailable with /give command

### Block states
See also: Block states

Java Edition:
Floor:

| Name | Default value | Allowed values     | Description          |
|------|---------------|--------------------|----------------------|
| lit  | `true`        | `false`<br/>`true` | If the torch is lit. |

Wall:

| Name   | Default value | Allowed values                            | Description                                   |
|--------|---------------|-------------------------------------------|-----------------------------------------------|
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the top of the torch is facing. |
| lit    | `true`        | `false`<br/>`true`                        | If the torch is lit.                          |

Bedrock Edition:

| Name                   | Metadata Bits             | Default value | Allowed values                                      | Values forMetadata Bits             | Description                                                                                                                                  |
|------------------------|---------------------------|---------------|-----------------------------------------------------|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| torch_facing_direction | `0x1`<br/>`0x2`<br/>`0x4` | `west`        | `west`<br/>`east`<br/>`north`<br/>`south`<br/>`top` | `1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | The face of the block that the torch is attached to. If the torch is a wall torch, the top of the torch faces opposite to this direction.[1] |
|                        |                           |               | `unknown`                                           | `0`                                 | Unused                                                                                                                                       |

