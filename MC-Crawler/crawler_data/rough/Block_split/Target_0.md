# Target
A target is a block that produces a temporary redstone signal when hit by a projectile. Unlike most other conductive blocks, it also redirects adjacent redstone dust toward it.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
- 2 Usage
	- 2.1 Redstone component
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 Achievements
- 6 Advancements
- 7 History
- 8 Issues
- 9 Gallery
	- 9.1 Screenshots
	- 9.2 In other media
- 10 References
- 11 External links

## Obtaining
### Breaking
Targets can be mined using any tool or by hand, but a hoe is the fastest way to break it.

| Block     | Target                |
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

### Natural generation
A target can be found in ancient cities.

### Crafting
| Ingredients                 | Crafting recipe |
|-----------------------------|-----------------|
| Redstone Dust+<br/>Hay Bale |                 |

## Usage
Targets emit a redstone signal when hit by most projectiles. This includes arrows, tridents, eggs, snowballs, splash potions, fire charges fired by a dispenser, firework rockets, lingering potions, bottles o' enchanting, ender pearls, shulker bullets, flying players[1], and llama spit. The closer a projectile is to the center of the block, the stronger the redstone signal that is produced.

### Redstone component
Targets redirecting redstone toward themselves
When struck by most projectiles, the target emits redstone power for 4 redstone ticks (0.4 seconds). Arrows and tridents instead cause the target to emit power for 10 redstone ticks (1 second), similar to stone buttons. A target can be hit with any of the projectiles mentioned above.

The strength of the signal depends on how close the projectile is to the center of the block, from 1 to 15.

In Java Edition, the target also provides a block update when hit, meaning that an observer can detect if the target has been hit and has produced a redstone signal.[2]

When used as part of a redstone circuit, a target has the unique property that, though being an opaque block that is not a mechanism component, still can redirect adjacent redstone dust to point to itself.

## Data values
### ID
Java Edition:

| Name   | Identifier | Form         | Translation key          |
|--------|------------|--------------|--------------------------|
| Target | `target`   | Block & Item | `block.minecraft.target` |

Bedrock Edition:

| Name   | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key    |
|--------|------------|------------|----------------------------|----------------|--------------------|
| Target | `target`   | `494`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.target.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
Java Edition:

| Name  | Default value | Allowed values                                                                                                                    | Description                          |
|-------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| power | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | Redstone power output of the target. |




