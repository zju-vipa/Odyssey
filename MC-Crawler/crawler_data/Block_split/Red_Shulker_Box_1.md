### Block states
See also: Block states

Java Edition:

| Name   | Default value | Allowed values           | Description                                                                                                               |
|--------|---------------|--------------------------|---------------------------------------------------------------------------------------------------------------------------|
| facing | up            | downeastnorthsouthupwest | The direction the shulker box is pointing.The opposite from the direction the player faces while placing the shulker box. |



### Block data
A shulker box has a block entity associated with it that identifies its contents.

Java Edition:

See also: Block entity format


 Block entity data
Tags common to all block entities
Tags common to all objects that can be renamed
 Items: List of items in this container.
: An item, including the slot tag. Shulker box slots are numbered 0–26, 0 starts in the top left corner.
Tags common to all items
Tags common to all containers that can be locked
Tags common to all objects that use loot tables to produce items

Bedrock Edition:

See Bedrock Edition level format/Block entity format.
### Item data
Java Edition:

Main article: Item format
Shulker boxes, as items, use an NBT tag BlockEntityTag to indicate the contents and details of the box when it is placed.

The following NBT structure is provided to show how the BlockEntityTag tag is organized, and is not comprehensive above the tag tag. The full NBT for an item can be found here.


 Entity data
 Item: The item
 tag: Additional information about the item. This tag is optional for most items.
 BlockEntityTag: The details of the shulker box.
All block data, except tags common to all block entities.

Bedrock Edition:

See Bedrock Edition level format/Item format.

