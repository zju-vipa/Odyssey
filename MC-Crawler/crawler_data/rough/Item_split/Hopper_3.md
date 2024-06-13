### Block states
See also: Block states

Java Edition:

| Name    | Default value | Allowed values                                       | Description                                                                                                                              |
|---------|---------------|------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| enabled | `true`        | `false`<br/>`true`                                   | True if hopper can move items to and from its inventory.<br/>When the hopper is being powered by redstone current, this is set to false. |
| facing  | `down`        | `down`<br/>`east`<br/>`north`<br/>`south`<br/>`west` | The direction the hopper's output points.<br/>The hopper pushes items into containers in this direction only.                            |

Bedrock Edition:

| Name             | Metadata Bits             | Default value | Allowed values                      | Values forMetadata Bits             | Description                                                                                                                                                                                                                                                       |
|------------------|---------------------------|---------------|-------------------------------------|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing_direction | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4` | The direction the hopper's output points.<br/>The hopper pushes items into containers in this direction only.0: Output facing down<br/>1: (unused)<br/>2: Output facing north<br/>3: Output facing south<br/>4: Output facing west<br/>5: Output facing east<br/> |
| toggle_bit       | `0x8`                     | `false`       | `false`<br/>`true`                  | `0`<br/>`1`                         | 1 if hopper cannot move items to and from its inventory.<br/>When the hopper is being powered by redstone current, this is set to true.                                                                                                                           |



### Block data
A hopper has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format

- Block entity data
	- 
	- Tags common to all block entities
	- 
	- Tags common to all objects that can be renamed
	- Items: List of items in this container.
		- : An item, including the slot tag.
			- 
			- Tags common to all items
	- 
	- Tags common to all containers that can be locked
	- 
	- Tags common to all objects that use loot tables to produce items
	- TransferCooldown: Time until the next transfer ingame ticks, naturally between 1 and 8 or 0 if there is no transfer.

Bedrock Edition:

SeeBedrock Edition level format/Block entity format.

