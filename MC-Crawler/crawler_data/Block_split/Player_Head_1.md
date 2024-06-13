### Item data
Java Edition:

Main article: Item format
Player heads use item NBT to save the owner.


 tag: The item's tag tag.
 SkullOwner: The username of the player this is a skull of. This gets converted to the compound version on almost any action.
 SkullOwner: Different definition for the skull's owner.

 Id: UUID of owner, stored as four ints. Optional. Used to update the other tags when the chunk loads or the holder logs in, in case the owner's name has changed.
 Name: Username of owner. If missing or empty, the head appears as a Steve head. Otherwise, used to store or retrieve the downloaded skin in the cache. Need not be a valid player name, but must not be all spaces.
 Properties
 textures
: An individual texture.
 Value: A Base64-encoded JSON object.
 isPublic: Optional.
 signatureRequired
 profileId: Optional: The hexadecimal text form of the player's UUID, without hyphens.
 profileName: Optional: Player name.
 textures
 CAPE: Optional.
 url: URL of a player cape (64x32 PNG).
 SKIN
 url: URL of a player skin on textures.minecraft.net.
 metadata
 model: The model of the player skin. Can be "classic" or "slim".
 timestamp: Optional: Unix time in milliseconds.
 Signature: Optional.

Bedrock Edition:

In Bedrock Edition, heads have no additional item tag.
See Bedrock Edition level format/Item format.
### Block states
See also: Block states

Java Edition:
Floor

| Name     | Default value | Allowed values | Description                          |
|----------|---------------|----------------|--------------------------------------|
| rotation | 0             | 0              | The block is facing south.           |
|          |               | 1              | The block is facing south-southwest. |
|          |               | 2              | The block is facing southwest.       |
|          |               | 3              | The block is facing west-southwest.  |
|          |               | 4              | The block is facing west.            |
|          |               | 5              | The block is facing west-northwest.  |
|          |               | 6              | The block is facing northwest.       |
|          |               | 7              | The block is facing north-northwest. |
|          |               | 8              | The block is facing north.           |
|          |               | 9              | The block is facing north-northeast. |
|          |               | 10             | The block is facing northeast.       |
|          |               | 11             | The block is facing east-northeast.  |
|          |               | 12             | The block is facing east.            |
|          |               | 13             | The block is facing east-southeast.  |
|          |               | 14             | The block is facing southeast.       |
|          |               | 15             | The block is facing south-southeast. |

Wall

| Name   | Default value | Allowed values     | Description                                                                                      |
|--------|---------------|--------------------|--------------------------------------------------------------------------------------------------|
| facing | north         | eastnorthsouthwest | The direction the head is facing.Opposite from the direction a player is facing when placing it. |

Bedrock Edition:

| Name             | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                          |
|------------------|---------------|---------------|----------------|-------------------------|------------------------------------------------------|
| facing_direction | 0x10x20x4     | 0             | 1              | 1                       | On the floor (rotation is stored in the tile entity) |
|                  |               |               | 2              | 2                       | On a wall, facing north                              |
|                  |               |               | 3              | 3                       | On a wall, facing south                              |
|                  |               |               | 4              | 4                       | On a wall, facing east                               |
|                  |               |               | 5              | 5                       | On a wall, facing west                               |
|                  |               |               | 0              | 0                       | Unused                                               |



### Block data
A player head has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format


 Block entity data
Tags common to all block entities
 note_block_sound: Optional. The sound event this skull plays when played with a note block.
 ExtraType: Name of the player this is a skull of. This tag is converted to SkullOwner below upon loading the NBT. When loaded sets the name to the value and the UUID to null.
 SkullOwner: The definition of the skull's owner. When this is a player_head or player_wall_head, shows this player's skin; if missing, shows the head of the default Steve skin.

 Id: UUID of owner, stored as four ints. Optional. Used to update the other tags when the chunk loads or the holder logs in, in case the owner's name has changed.
 Name: Username of owner. If missing or empty, the head appears as a Steve head. Otherwise, used to store or retrieve the downloaded skin in the cache. Need not be a valid player name, but must not be all spaces.
 Properties
 textures
: An individual texture.
 Value: A Base64-encoded JSON object.
 isPublic: Optional.
 signatureRequired
 profileId: Optional: The hexadecimal text form of the player's UUID, without hyphens.
 profileName: Optional: Player name.
 textures
 CAPE: Optional.
 url: URL of a player cape (64x32 PNG).
 SKIN
 url: URL of a player skin on textures.minecraft.net.
 metadata
 model: The model of the player skin. Can be "classic" or "slim".
 timestamp: Optional: Unix time in milliseconds.
 Signature: Optional.

Bedrock Edition:

See Bedrock Edition level format/Block entity format.

