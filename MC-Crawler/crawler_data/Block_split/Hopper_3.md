### Block states
See also: Block states

Java Edition:

| Name    | Default value | Allowed values         | Description                                                                                                                         |
|---------|---------------|------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| enabled | true          | falsetrue              | True if hopper can move items to and from its inventory.When the hopper is being powered by redstone current, this is set to false. |
| facing  | down          | downeastnorthsouthwest | The direction the hopper's output points.The hopper pushes items into containers in this direction only.                            |

Bedrock Edition:

| Name             | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                                                                                                                                                                                                         |
|------------------|---------------|---------------|----------------|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing_direction | 0x10x20x4     | 0             | 01234          | 01234                   | The direction the hopper's output points.The hopper pushes items into containers in this direction only.0: Output facing down 1: (unused) 2: Output facing north 3: Output facing south 4: Output facing west 5: Output facing east |
| toggle_bit       | 0x8           | false         | falsetrue      | 01                      | 1 if hopper cannot move items to and from its inventory.When the hopper is being powered by redstone current, this is set to true.                                                                                                  |



### Block data
A hopper has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format


 Block entity data
Tags common to all block entities
Tags common to all objects that can be renamed
 Items: List of items in this container.
: An item, including the slot tag.
Tags common to all items
Tags common to all containers that can be locked
Tags common to all objects that use loot tables to produce items
 TransferCooldown: Time until the next transfer in game ticks, naturally between 1 and 8 or 0 if there is no transfer.

Bedrock Edition:

See Bedrock Edition level format/Block entity format.

