# Respawn Anchor
The respawn anchor is a block that allows players to set their spawn point in the Nether.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Crafting
- 2 Usage
	- 2.1 Respawning
	- 2.2 Exploding
	- 2.3 Redstone component
	- 2.4 Mobs
	- 2.5 Note blocks
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 Advancements
- 6 History
- 7 Issues
- 8 Trivia
- 9 Gallery
	- 9.1 Screenshots
- 10 References

## Obtaining
### Breaking
Respawn anchors can be harvested with a diamond pickaxe or better. The respawn anchor keeps its current level of charges with the Pick Block option in Creative mode, and it is unique in the fact that this does not work on blocks with different states like the redstone lamp or daylight sensor.[1]

| Block     | Respawn Anchor        |
|-----------|-----------------------|
| Hardness  | 50                    |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 250                   |
| Wooden    | 125                   |
| Stone     | 62.5                  |
| Iron      | 41.7                  |
| Diamond   | 9.4                   |
| Netherite | 8.35                  |
| Golden    | 20.85                 |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Crafting
While the ingredients to craft a respawn anchor are all native to the Nether, they are also obtainable in the Overworld: glowstone can be obtained from trading with villagers or wandering trader, or crafted from glowstone dust dropped by witches; crying obsidian can be found in ruined portals.

| Ingredients                    | Crafting recipe |
|--------------------------------|-----------------|
| Crying Obsidian+<br/>Glowstone |                 |

## Usage
### Respawning
Tile priority in where the anchor looks to respawn the player (with 1 being the highest). The minimum area required to be valid is 1×2×1. Respawn attempts are made per column for layer1 and layer2, layer3 is used when attempts for all columns fail for layer1 and layer2; e.g. column1-layer2 has priority over column2-layer1, and column8-layer1 has priority over column1-layer3.
The respawn anchor is used to respawn in the Nether, even if the player leaves the Nether. Once the block is charged, it can be used to set the player's respawn location.

** Charging **
When crafted, a respawn anchor has no (zero) charge and can't yet be used until charged. Using a glowstone block (not glowstone dust) on it adds a charge. The anchor accepts up to 4 charges, and the charge level is indicated by a dial on the side of the block.

The first charge makes the respawn anchor glow with a light level of 3. Each glowstone after the first increases the light level by 4, up to a maximum of 15.

** Setting respawn **
To set the player's spawn location to the respawn anchor they must use it, just like one does with a bed. The anchor must at least have one charge, and it must be in the Nether. A confirmation appears when the player's respawn location is set. Other players can also set their spawn point to the same respawn anchor. Each respawn uses up one charge, even if used by another player.

Using a charged anchor overrides any other spawn location the player might have had, as with a bed. The respawn anchor does not serve as a backup spawn point to a missing or obstructed bed.

** Respawn upon player death **
Upon death, the player respawns next to the anchor, and it loses one charge. If a player's respawn anchor is destroyed, if its charges have been exhausted, or if the area around it is made unsuitable for respawning, a message appears saying "You have no home bed or charged Respawn Anchor, or it was obstructed", and the player respawns at the world spawn point. Returning through an end portal is not counted as a respawn against the charges.

A respawn anchor can be shared among several players. When shared, remaining charges are shared as well.
In Hardcore mode, the respawn anchor does not resurrect the player, but may still teleport them and consume charges.

### Exploding
If the player attempts to set their spawn at a charged respawn anchor in the Overworld, the End, or custom dimensions in which they are disabled, the block explodes (and is destroyed) similar to when a bed is used in the Nether or the End. The explosion has a power of 5 and sets fire to surrounding blocks.

### Redstone component
When charged, a redstone comparator gives a signal depending on the number of charges: 3 for one charge, 7 for two charges, 11 for three charges, 15 for four charges. An empty anchor gives a signal of 0.

The respawn anchor can also be charged with a dispenser.

The respawn anchor cannot be pushed by a piston. 

### Mobs
Hoglins run away from respawn anchors.

### Note blocks
Respawn anchors can be placed under note blocks to produce the "bass drum" sound.

## Data values
### ID
Java Edition:

| Name           | Identifier       | Form         | Block tags                              | Translation key                  |
|----------------|------------------|--------------|-----------------------------------------|----------------------------------|
| Respawn Anchor | `respawn_anchor` | Block & Item | `dragon_immune`<br/>`hoglin_repellents` | `block.minecraft.respawn_anchor` |

Bedrock Edition:

| Name           | Identifier       | Numeric ID | Form                       | Item ID[i 1]   | Translation key            |
|----------------|------------------|------------|----------------------------|----------------|----------------------------|
| Respawn Anchor | `respawn_anchor` | `527`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.respawn_anchor.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:

| Name    | Default value | Allowed values                      | Description                                   |
|---------|---------------|-------------------------------------|-----------------------------------------------|
| charges | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4` | How many charges the Respawn Anchor has left. |

Bedrock Edition:

| Name                  | Metadata Bits             | Default value | Allowed values                      | Values forMetadata Bits             | Description                                   |
|-----------------------|---------------------------|---------------|-------------------------------------|-------------------------------------|-----------------------------------------------|
| respawn_anchor_charge | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4` | How many charges the Respawn Anchor has left. |



