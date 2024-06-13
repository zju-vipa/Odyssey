### Light source
Enchanting tables emit a light level of 7.

### Standard Galactic Alphabet
Glyphs flowing from the bookshelves animation.
The arcane glyphs that float from bookshelves to the enchanting table and the cryptic runes in the enchanting table's interface are written in the Standard Galactic Alphabet, which is a simple alphabet substitution cipher used in the Commander Keen series of computer games.



The arcane glyphs cannot be seen if "particles" in the video settings is set to "minimal".

The cryptic runes seen in the interface are randomly constructed from the following list of words:

| the      | elder    | scrolls | klaatu   | berata    | niktu   |
|----------|----------|---------|----------|-----------|---------|
| xyzzy    | bless    | curse   | light    | darkness  | fire    |
| air      | earth    | water   | hot      | dry       | cold    |
| wet      | ignite   | snuff   | embiggen | twist     | shorten |
| stretch  | fiddle   | destroy | imbue    | galvanize | enchant |
| free     | limited  | range   | of       | towards   | inside  |
| sphere   | cube     | self    | other    | ball      | mental  |
| physical | grow     | shrink  | demon    | elemental | spirit  |
| animal   | creature | beast   | humanoid | undead    | fresh   |
| stale    |          |         |          |           |         |

Java Edition additionally may use the following words:‌[JE  only]

| phnglui  | mglwnafh | cthulhu  | rlyeh |
|----------|----------|----------|-------|
| wgahnagl | fhtagn   | baguette |       |

Three to five words are chosen from the list and appended to each other, then displayed in the Standard Galactic Alphabet. Although sometimes the words chosen accidentally refer to mobs like blazes and elder guardians, the words chosen are random and purely cosmetic; they have no relation to the enchantments to be applied to the item and are not saved on the enchanted item (meaning they say nothing about the spell's identity), and they are displayed only in the enchanting table. Only the cost and one of the enchantments are known.

### Custom name
By default, the GUI of an enchanting table is labeled "Enchant", but this name can be customized by naming the enchanting table in an anvil before placing it or by changing the CustomName tag using the /data command‌[Java Edition  only].

### Note blocks
Enchanting tables can be placed under note blocks to produce "bass drum" sounds.

### Piston interactivity
Enchanting tables cannot be pushed by pistons. They also cannot be pushed nor pulled by sticky pistons.

## Data values
### ID
Java Edition:

| Name             | Identifier         | Form         | Translation key                    |
|------------------|--------------------|--------------|------------------------------------|
| Enchanting Table | `enchanting_table` | Block & Item | `block.minecraft.enchanting_table` |

| Name         | Identifier         |
|--------------|--------------------|
| Block entity | `enchanting_table` |

Bedrock Edition:

| Name              | Identifier         | Numeric ID | Form                       | Item ID[i 1]   | Translation key              |
|-------------------|--------------------|------------|----------------------------|----------------|------------------------------|
| Enchantment Table | `enchanting_table` | `116`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.enchanting_table.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

| Name         | Savegame ID    |
|--------------|----------------|
| Block entity | `EnchantTable` |

### Block data
An enchanting table has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format

- Block entity data
	- 
	- Tags common to all block entities
	- 
	- CustomName: Optional. The name of this container in JSON text component, which appears in its GUI where the default name ordinarily appears.

Bedrock Edition:

SeeBedrock Edition level format/Block entity format.

