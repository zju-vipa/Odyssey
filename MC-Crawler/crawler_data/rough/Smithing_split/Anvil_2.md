## Creative mode
In creative mode, the anvil functions a little differently than other game modes:

- Any repair/enchant/rename operation may be done, regardless of the player's experience level. Incompatible enchantments are allowed as well (enchanting blocks etc.)
	- The experience cost is not taken from the player.
- The repair cost of toolsdoesstill increase.
	- It continues doubling with each repair, past the usual limit of 39 levels.
	- When it reaches the capacity of signed 32-bit integers, no repair cost is shown and the "product" item cannot be taken out of the anvil. Tools in this state also cannot be renamed or enchanted.
- Anvils are not damaged on use.

## Data values
### ID
Java Edition:

| Name          | Identifier      | Form         | Block tags | Item tags | Translation key                 |
|---------------|-----------------|--------------|------------|-----------|---------------------------------|
| Anvil         | `anvil`         | Block & Item | `anvil`    | `anvil`   | `block.minecraft.anvil`         |
| Chipped Anvil | `chipped_anvil` | Block & Item | `anvil`    | `anvil`   | `block.minecraft.chipped_anvil` |
| Damaged Anvil | `damaged_anvil` | Block & Item | `anvil`    | `anvil`   | `block.minecraft.damaged_anvil` |

Bedrock Edition:

| Name  | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key                                                                                  |
|-------|------------|------------|----------------------------|----------------|--------------------------------------------------------------------------------------------------|
| Anvil | `anvil`    | `145`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.anvil.intact.name`<br/>`tile.anvil.slightlyDamaged.name`<br/>`tile.anvil.veryDamaged.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:

| Name   | Default value | Allowed values                            | Description                                                                                                                                                                                                                                                                   |
|--------|---------------|-------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | An anvil pointing north or south is aligned with its long dimension pointing north–south.<br/>An anvil pointing east or west is aligned with its long dimension pointing east–west.<br/>This value is 90° clockwise from the direction a player faces while placing an anvil. |

Bedrock Edition:

| Name                         | Metadata Bits   | Default value | Allowed values                            | Values forMetadata Bits | Description                                                                                                                                                                                                                                                                   |
|------------------------------|-----------------|---------------|-------------------------------------------|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| damage                       | `0x4`<br/>`0x8` | `undamaged`   | `broken`                                  | `3`                     | Broken Anvil (inaccessible and unused, uses anvil base texture)                                                                                                                                                                                                               |
|                              |                 |               | `slightly_damaged`                        | `1`                     | Slightly Damaged Anvil.                                                                                                                                                                                                                                                       |
|                              |                 |               | `undamaged`                               | `0`                     | Anvil.                                                                                                                                                                                                                                                                        |
|                              |                 |               | `very_damaged`                            | `2`                     | Very Damaged Anvil.                                                                                                                                                                                                                                                           |
| minecraft:cardinal_direction | Not Supported   | `south`       | `east`<br/>`north`<br/>`south`<br/>`west` | `Unsupported`           | An anvil pointing north or south is aligned with its long dimension pointing north–south.<br/>An anvil pointing east or west is aligned with its long dimension pointing east–west.<br/>This value is 90° clockwise from the direction a player faces while placing an anvil. |



### Falling block entity
Main article: Falling Block
- Dynamic block entity data
	- 
		- 
		- Tags common to all entities
	- BlockState: The falling block represented by this entity.
		- Name: Theresource locationof the block.
		- Properties: Optional. Theblock statesof the block.
			- Name: The block state name and its value.
	- CancelDrop: 1 or 0 (true/false) - true if the block should be destroyed instead of placed after landing on a solid block. When true, the block is not dropped as an item, even if theDropItemtag is set to true. However, if the entity is deleted due to itsTimevalue being too high, this tag is ignored and an item is dropped depending on theDropItemtag.CancelDropdefaults to 1 for fallingsuspicious sandandsuspicious gravel, and 0 for the other vanilla falling blocks and any summoned falling block.
	- DropItem: 1 or 0 (true/false) – true if the block should drop as an item when it breaks. Any block that does not have an item formwith the same ID as the blockdoes not drop even if this is set.
	- FallHurtAmount: Multiplied by theFallDistanceto calculate the amount of damage to inflict. By default this value is 2for anvils, and 6for pointed dripstone.
	- FallHurtMax: The maximum hit points of damage to inflict on entities that intersect this falling block. For vanilla falling blocks, always 40× 20.
	- HurtEntities: 1 or 0 (true/false) – true if the block should hurt entities it falls on. Defaults to 1 foranvilsandpointed dripstoneand to 0 for the other vanilla falling blocks and any summoned falling block.
	- TileEntityData: Optional. The tags of the block entity for this block.
	- Time: The number of ticks the entity has existed. WhenTimegoes above 600, or above 100 while the block is at Y=-64 or is outside building height, the entity is deleted.


