# Iron Bars
Iron bars are blocks that serve a similar purpose to glass panes, but made of iron ingots instead of glass.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
	- 1.4 Post-generation
- 2 Usage
	- 2.1 Placement
	- 2.2 Curing
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Trivia
- 8 Gallery
	- 8.1 Renders
	- 8.2 Screenshots
- 9 References

## Obtaining
### Breaking
Iron bars can be mined using any pickaxe. If mined without a pickaxe, it drops nothing.

| Block     | Iron Bars             |
|-----------|-----------------------|
| Hardness  | 5                     |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 25                    |
| Wooden    | 3.75                  |
| Stone     | 1.9                   |
| Iron      | 1.25                  |
| Diamond   | 0.95                  |
| Netherite | 0.85                  |
| Golden    | 0.65                  |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
Iron bars can be found in parts of strongholds, woodland mansions, desert and plains villages, igloo basements, ruined portals, and trail ruins.

In the End, 2 obsidian pillars have iron bars around their end crystals.

### Crafting
| Ingredients | Crafting recipe |
|-------------|-----------------|
| Iron Ingot  | 16              |

Iron bars are not a source of iron. Once crafted, iron bars cannot be smelted into iron nuggets or ingots.

### Post-generation
Iron bars regenerate on end pillars when the ender dragon is respawned.

## Usage
Iron bars used to create arrow slits.
As with glass panes and fences, iron bars can be used to create narrow slits when placed between a door and a solid block. Mobs can see through and attack through these gaps, and arrows may be shot through them. Also as with fences and glass panes, arrows cannot be shot through iron bars themselves.

Endermen seen through iron bars do not become angry. The ender dragon cannot destroy iron bars (some of the end crystals are protected by them), which makes them a useful material in the End.

### Placement
Iron bars can be placed in much the same way as fences or glass panes. If no solid block is adjacent to the bars, they have appearance of a slim, tall column. If something is placed next to iron bars, they appear either flat,  shaped,  shaped or  shaped, depending on the blocks surrounding it.

### Curing
Iron bars speed up the curing process of zombie villagers.

## Data values
### ID
Java Edition:

| Name      | Identifier  | Form         | Translation key             |
|-----------|-------------|--------------|-----------------------------|
| Iron Bars | `iron_bars` | Block & Item | `block.minecraft.iron_bars` |

Bedrock Edition:

| Name      | Identifier  | Numeric ID | Form                       | Item ID[i 1]   | Translation key       |
|-----------|-------------|------------|----------------------------|----------------|-----------------------|
| Iron Bars | `iron_bars` | `101`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.iron_bars.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:

| Name        | Default value | Allowed values     | Description                                                        |
|-------------|---------------|--------------------|--------------------------------------------------------------------|
| east        | `false`       | `false`<br/>`true` | When true, the iron bars extend from the center post to the east.  |
| north       | `false`       | `false`<br/>`true` | When true, the iron bars extend from the center post to the north. |
| south       | `false`       | `false`<br/>`true` | When true, the iron bars extend from the center post to the south. |
| waterlogged | `false`       | `false`<br/>`true` | Whether or not there's water in the same place as these iron bars. |
| west        | `false`       | `false`<br/>`true` | When true, the iron bars extend from the center post to the west.  |

