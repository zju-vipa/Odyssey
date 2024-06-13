# Fungus
A fungus is a mushroom-like block that generates in the Nether. There are two types of fungi: crimson and warped.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Mob loot
	- 1.4 Chest loot
	- 1.5 Post-generation
- 2 Usage
	- 2.1 Placement
	- 2.2 Growth
	- 2.3 Breeding
	- 2.4 Hoglins
	- 2.5 Crafting ingredient
	- 2.6 Composting
- 3 Sounds
- 4 Data values
	- 4.1 ID
- 5 History
- 6 Issues
- 7 See also
- 8 References

## Obtaining
### Breaking
A fungus can be mined instantly and always drops itself. Mining a flower pot containing a fungus drops both items separately.

| Block    | Fungi               |
|----------|---------------------|
| Hardness | 0                   |
|          | Breakingtime (secs) |
| Default  | 0.05                |

### Natural generation
Fungi naturally generate in the crimson and warped forest biomes, with each fungi most commonly generating in their respective biomes, and less frequently vice versa.


### Mob loot
An enderman holding a fungus drops the fungus upon death.

### Chest loot
| Item           | Structure       | Container           | Quantity | Chance                         |
|----------------|-----------------|---------------------|----------|--------------------------------|
|                |                 |                     |          | Java EditionandBedrock Edition |
| Crimson Fungus | Bastion Remnant | Hoglin stable chest | 2–7      | 22.8%                          |

### Post-generation
Applying bone meal to nylium causes fungi to appear nearby, similar to flowers on grass blocks. While fungi of both types and other Nether vegetation do generate this way, they are more likely to be the same type as the nylium.[1]

## Usage
### Placement
All of the blocks that fungi can be placed on.
Fungi may be placed on grass blocks, dirt, coarse dirt, podzol, farmland, rooted dirt, moss blocks, nylium, mycelium, soul soil, mud and muddy mangrove roots. Attempting to place it on any other block fails. Fungi requires a solid block underneath it, and pops off and drops itself if it is no longer supported.

Fungi can also be placed in flower pots.

### Growth
When bone meal is used on a fungus that is planted on matching nylium, it has a 40% chance to grow into its tall equivalent (similar to saplings and mushrooms). Crimson and warped fungi grow into crimson and warped huge fungi, respectively. The stem, shroomlight or wart blocks may replace certain blocks including slabs and torches.

### Breeding
Crimson fungus can be used to breed hoglins and keep them from despawning, but it does not stop the hoglin from attacking the player. Warped fungus can be used to breed striders and lead them around if crafted as a warped fungus on a stick.

### Hoglins
All hoglins, regardless of age, avoid and run up to 7 blocks away from warped fungus when it is placed on a block or inside of a flower pot‌[Java Edition  only][2]. Held warped fungi and warped fungi on sticks do not have this effect.

### Crafting ingredient
| Name                     | Ingredients                                             | Crafting recipe | Description                                                                                                                                                                               |
|--------------------------|---------------------------------------------------------|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Warped Fungus on a Stick | Fishing Rodor<br/>DamagedFishing Rod+<br/>Warped Fungus |                 | Crafting from a damaged fishing rod is available only inBedrock Edition.Java Editionrequires an unused fishing rod. The2×2 gridcan also be used for crafting instead of a crafting table. |

### Composting
Placing a fungus into a composter has a 65% chance of raising the compost level by 1.

## Data values
### ID
Java Edition:

| Name           | Identifier       | Form         | Block tags                                  | Translation key                  |
|----------------|------------------|--------------|---------------------------------------------|----------------------------------|
| Crimson Fungus | `crimson_fungus` | Block & Item | `enderman_holdable`                         | `block.minecraft.crimson_fungus` |
| Warped Fungus  | `warped_fungus`  | Block & Item | `enderman_holdable`<br/>`hoglin_repellents` | `block.minecraft.warped_fungus`  |

Bedrock Edition:

| Name           | Identifier       | Numeric ID | Form                       | Item ID[i 1]   | Translation key            |
|----------------|------------------|------------|----------------------------|----------------|----------------------------|
| Crimson Fungus | `crimson_fungus` | `483`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.crimson_fungus.name` |
| Warped Fungus  | `warped_fungus`  | `484`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.warped_fungus.name`  |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑ a bAvailable with /give command.
3. ↑ a bThe block's direct item form has the same id as the block.


