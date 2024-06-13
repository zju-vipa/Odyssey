### Redstone component
For redstone to activate TNT, it must either lead directly to the TNT, or power an adjacent block.

### Crafting ingredient
| Name              | Ingredients       | Crafting recipe | Description                                      |
|-------------------|-------------------|-----------------|--------------------------------------------------|
| Minecart with TNT | TNT+<br/>Minecart |                 |                                                  |
| Underwater TNT    | Sodium+<br/>TNT   |                 | ‌[Bedrock Edition and Minecraft Education  only] |

## Data values
### ID
Java Edition:

| Name | Identifier | Form         | Block tags          | Translation key       |
|------|------------|--------------|---------------------|-----------------------|
| TNT  | `tnt`      | Block & Item | `enderman_holdable` | `block.minecraft.tnt` |

| Name       | Identifier | Translation key        |
|------------|------------|------------------------|
| Primed TNT | `tnt`      | `entity.minecraft.tnt` |

Bedrock Edition:

| Name | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key                                |
|------|------------|------------|----------------------------|----------------|------------------------------------------------|
| TNT  | `tnt`      | `46`       | Block & Giveable Item[i 2] | Identical[i 3] | `tile.tnt.name`<br/>`tile.underwater_tnt.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

| Name       | Identifier | Numeric ID | Translation key   |
|------------|------------|------------|-------------------|
| Primed TNT | `tnt`      | `65`       | `entity.tnt.name` |

### Block states
Java Edition:

| Name     | Default value | Allowed values | Description                                                                   |
|----------|---------------|----------------|-------------------------------------------------------------------------------|
| unstable | `false`       | `false`        | Hittingthe TNT block breaks it, dropping it as an item that can be picked up. |
|          |               | `true`         | Hittingthe TNT block causes it to ignite and then explode.                    |

Bedrock Edition:

| Name                 | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                                                   |
|----------------------|---------------|---------------|----------------|-------------------------|-------------------------------------------------------------------------------|
| allow_underwater_bit | `0x2`         | `false`       | `false`        | `0`                     | This is normal TNT.                                                           |
|                      |               |               | `true`         | `1`                     | This is Underwater TNT.                                                       |
| explode_bit          | `0x1`         | `false`       | `false`        | `0`                     | Hittingthe TNT block breaks it, dropping it as an item that can be picked up. |
|                      |               |               | `true`         | `1`                     | Hittingthe TNT block causes it to ignite and then explode.                    |



### Entity data
TNT has entity data associated with them that contain various properties of the entity.

Java Edition:

Main article: Entity format
- Dynamic block entity data
	- 
	- Tags common to all entities
	- Fusefuse: Ticks until explosion. Default is 0. If activated from a TNT block, the fuse duration is 80 ticks (4 seconds).
	- block_state: The block model to use.
		- Name: Theresource locationof the block.
		- Properties: Optional. Theblock statesof the block.
			- Name: The block state name and its value.

Bedrock Edition:

SeeBedrock Edition level format/Entity format.

