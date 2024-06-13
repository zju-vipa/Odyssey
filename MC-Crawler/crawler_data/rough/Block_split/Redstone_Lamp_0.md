# Redstone Lamp
A redstone lamp is a solid block that produces light while it is receiving redstone power.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
- 2 Usage
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 Video
- 6 History
	- 6.1 Lit redstone lamp "item"
		- 6.1.1 Appearances
		- 6.1.2 Names
- 7 Issues
- 8 Trivia
- 9 Gallery
	- 9.1 Screenshots
- 10 Notes
- 11 References
- 12 External links

## Obtaining
### Breaking
A redstone lamp can be mined with any tool[1] or by hand, dropping itself as an item.

| Block    | Redstone Lamp       |
|----------|---------------------|
| Hardness | 0.3                 |
|          | Breakingtime (secs) |
| Default  | 0.45                |

### Natural generation
Redstone lamps generate naturally in ancient cities.

### Crafting
| Ingredients                  | Crafting recipe |
|------------------------------|-----------------|
| Redstone Dust+<br/>Glowstone |                 |

## Usage
A redstone lamp can be used to produce switchable light. 

Redstone lamps are redstone mechanisms and can be activated by:

- An adjacent activepower component, including above or below: for example, aredstone torch(except that a redstone torch does not activate a redstone lamp it is attached to), ablock of redstone, adaylight sensor, etc.
- An adjacentpowered block(for example, an opaque block with an active redstone torch under it), including above or below
- A poweredredstone comparatororredstone repeaterfacing the redstone lamp
- Adjacent poweredredstone dustconfigured to point at the redstone lamp (or on top of it) or directionless; a redstone lamp isnotactivated by adjacent powered redstone dust that is configured to point away from it.

A redstone lamp activates instantly, but takes 2 redstone ticks to turn off (4 game ticks, or 0.2 seconds barring lag) in Java Edition or 3 redstone ticks to turn off (6 game ticks, or 0.3 seconds barring lag) in Bedrock Edition.

An active redstone lamp produces block light 15. An inactive redstone lamp produces no light.

A redstone lamp acts like an opaque block; it blocks sky light, mobs suffocate in it, and it conducts redstone power. It also allows mobs to spawn on them while it is unlit.

## Data values
### ID
Java Edition:

| Name          | Identifier      | Form         | Translation key                 |
|---------------|-----------------|--------------|---------------------------------|
| Redstone Lamp | `redstone_lamp` | Block & Item | `block.minecraft.redstone_lamp` |

Bedrock Edition:

| Name              | Identifier          | Numeric ID | Form                         | Item ID[i 1]   | Translation key           |
|-------------------|---------------------|------------|------------------------------|----------------|---------------------------|
| Redstone Lamp     | `redstone_lamp`     | `123`      | Block & Giveable Item[i 2]   | Identical[i 3] | `tile.redstone_lamp.name` |
| Lit Redstone Lamp | `lit_redstone_lamp` | `124`      | Block & Ungiveable Item[i 4] | Identical[i 3] | —                         |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑ a bThe block's direct item form has the same id as the block.
4. ↑Unavailable with /give command

### Block states
See also: Block states

Java Edition:

| Name | Default value | Allowed values     | Description                  |
|------|---------------|--------------------|------------------------------|
| lit  | `false`       | `false`<br/>`true` | If the redstone lamp is lit. |



## Notes
1. ↑Only when lit, it diffuses sky light from above.


