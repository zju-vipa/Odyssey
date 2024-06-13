### Block data
A banner has a block entity associated with it that holds additional data about the block. 

Bedrock Edition:

SeeBedrock Edition level format/Block entity format.
Java Edition:

See also: Block entity format

- Block entity data
	- 
	- Tags common to all block entities
	- CustomName: Optional. The name of this banner in JSON text component, which is used for showing the banner on a map.
	- Patterns: List of all patterns applied to the banner.
		- : An individual pattern.
			- Color: Color of the section.
			- Pattern: The banner pattern code the color is applied to.


Pattern color
Main article: Banner/DV[edit]


Pattern
Main article: Banner/Patterns[edit]

### Item data
Java Edition:

Main article: Item format
Banners, as items, use an NBT tag BlockEntityTag to indicate the patterns and details when it is placed.

- Item: The item
	- tag: Additional information about the item. This tag is optional for most items.
		- BlockEntityTag: The details of the banner.
			- All block data, except tags common to all block entities.

Bedrock Edition:

SeeBedrock Edition level format/Item format.

