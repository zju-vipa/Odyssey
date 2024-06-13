# Coarse Dirt
Coarse dirt is a variation of dirt on which grass block cannot spread.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Mob loot
	- 1.4 Crafting
- 2 Usage
	- 2.1 Mud
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
	- 5.1 Data history
- 6 Issues
- 7 Gallery
	- 7.1 Screenshots

## Obtaining
### Breaking
Coarse dirt drops itself as an item when mined using any tool or by hand, but a shovel is the quickest.

| Block     | Coarse Dirt           |
|-----------|-----------------------|
| Hardness  | 0.5                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 0.75                  |
| Wooden    | 0.4                   |
| Stone     | 0.2                   |
| Iron      | 0.15                  |
| Diamond   | 0.1                   |
| Netherite | 0.1                   |
| Golden    | 0.1                   |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


### Natural generation
Coarse dirt can be found as large patches in the windswept savanna, wooded badlands, and two variants of old growth taiga biomes.

It also generates in mushroom farm rooms in woodland mansions and in trail ruins.


### Mob loot
An enderman holding coarse dirt drops the block upon death.

### Crafting
| Name        | Ingredients | Crafting recipe |
|-------------|-------------|-----------------|
| Coarse Dirt | Dirt+Gravel | 4               |

## Usage
Coarse dirt has the ability to grow saplings, sugar canes, mushrooms, bamboo, flowers, and sweet berries, which can be planted directly under appropriate conditions.

Neither mycelium nor grass can spread onto coarse dirt.

Coarse dirt can be tilled using a hoe to become normal dirt. There must be an empty space above the coarse dirt for it to be tilled.

Using any type of shovel on coarse dirt turns it into a dirt path.

### Mud
Using a water bottle, splash water bottle or lingering water bottle converts the coarse dirt into mud.

## Data values
### ID
Java Edition:

| Name        | Identifier  | Form         | Block tags                                                                                                            | Translation key             |
|-------------|-------------|--------------|-----------------------------------------------------------------------------------------------------------------------|-----------------------------|
| Coarse Dirt | coarse_dirt | Block & Item | bamboo_plantable_onenderman_holdablemoss_replaceablelush_ground_replaceablemineable/shoveldirt#sniffer_diggable_block | block.minecraft.coarse_dirt |

Bedrock Edition:

| Name        | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key       |
|-------------|------------|------------|----------------------------|----------------|-----------------------|
| Coarse Dirt | dirt       | 3          | Block & Giveable Item[i 2] | Identical[i 3] | tile.dirt.coarse.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block states

In Bedrock Edition, dirt uses the following block states:

Bedrock Edition:

| Name      | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description |
|-----------|---------------|---------------|----------------|-------------------------|-------------|
| dirt_type | 0x1           | normal        | normal         | 0                       | Dirt        |
|           |               |               | coarse         | 1                       | Coarse Dirt |




