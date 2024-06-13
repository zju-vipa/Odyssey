### Fuel
Note blocks can be used as a fuel in furnaces, smelting 1.5 items per block.

## Data values
### ID
Java Edition:

| Name       | Identifier | Form         | Translation key            |
|------------|------------|--------------|----------------------------|
| Note Block | note_block | Block & Item | block.minecraft.note_block |

Bedrock Edition:

| Name       | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key     |
|------------|------------|------------|----------------------------|----------------|---------------------|
| Note Block | noteblock  | 25         | Block & Giveable Item[i 2] | Identical[i 3] | tile.noteblock.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


| Name         | Savegame ID |
|--------------|-------------|
| Block entity | Music       |

### Block states
See also: Block states

Java Edition:

| Name       | Default value | Allowed values                                                                                                                                                | Description                                    |
|------------|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| instrument | harp          | banjobasedrumbassbellbitchimecow_bellcreepercustom_headdidgeridoodragonfluteguitarharphatiron_xylophonepiglinplingskeletonsnarewither_skeletonxylophonezombie | The instrument of the note block.              |
| note       | 0             | 0123456789101112131415161718192021222324                                                                                                                      | The pitch of the note block                    |
| powered    | false         | falsetrue                                                                                                                                                     | True if the note block is currently activated. |



### Block data
In Bedrock Edition, a note block has a block entity associated with it that holds additional data about the block.

See Bedrock Edition level format/Block entity format.

## See also
- Tutorials/Redstone music
- Tutorials/Redstone music/Doorbell
- Jukebox
- Minecraft Note Block Studio– A music editor forMinecraft.


