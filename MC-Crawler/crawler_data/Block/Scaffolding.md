# Scaffolding
Scaffolding is a climbable semi-solid block that can be stood on without falling as well as be placed and broken easily. It is mainly used to make construction easier

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Chest loot
	- 1.3 Crafting
- 2 Usage
	- 2.1 Fuel
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
	- 4.3 Falling block entity
- 5 Achievements
- 6 History
- 7 Issues
- 8 Trivia
- 9 Gallery
	- 9.1 Screenshots
	- 9.2 In other media
- 10 References
- 11 External links

## Obtaining
### Breaking
Scaffolding is broken instantly, and no tools are required. Scaffolding requires support and drops as an item if it loses this support.

| Block    | Scaffolding         |
|----------|---------------------|
| Hardness | 0                   |
|          | Breakingtime (secs) |
| Default  | 0.05                |

### Chest loot
| Item        | Structure      | Container      | Quantity | Chance                         |
|-------------|----------------|----------------|----------|--------------------------------|
|             |                |                |          | Java EditionandBedrock Edition |
| Scaffolding | Trial Chambers | Corridor chest | 2–10     | 19.6%                          |

### Crafting
| Ingredients   | Crafting recipe |
|---------------|-----------------|
| Bamboo+String | 6               |

## Usage
A stack of scaffolding created by placing another scaffolding block on the side face of the bottom scaffolding block.
When the bottom block of scaffolding is destroyed, all scaffolding blocks above it break, similar to chorus plants and bamboo; this makes it easier for players to make temporary structures. 

The placement of scaffolding is different from any other blocks in the game.

In Java Edition, when holding scaffolding, the hitbox of scaffolding in the world is a full block.

- Pressinguseon the top face of the scaffolding adds the scaffolding to the horizontal side, depending on the horizontal direction the player is facing. When pressing use on the other faces of a scaffolding, the scaffolding is added on top of the highest scaffolding in that location, allowing the player to build the scaffolding structure higher on the ground.
- When the player's eyes are inside the scaffolding, the placement depends on the vertical rotation of the player's head. If facing more than 45 degrees down, pressing use adds the scaffolding to the horizontal side, depending on the horizontal rotation of the player. Otherwise, the scaffolding is added on top of the highest scaffolding in that location.
- Whilesneaking, pressing use on a face of the scaffolding places the new scaffolding on that face, just like placing a block on full blocks (dirt, stone, etc.).
- Whilesneakingand the player's eyes are inside the scaffolding, pressing use adds the scaffolding to the direction the player is facing.

In Bedrock Edition, the hitbox of scaffolding in the world is not a full block even when holding a scaffolding, so the player can hit/interact with other blocks through the scaffolding. But when being hit, the scaffolding's interaction box is a full block.

- When trying to place a scaffolding inside of another scaffolding, the scaffolding is added on top of the highest scaffolding in that location, allowing the player to build the scaffolding structure higher on the ground.
- When pressing use while hitting the scaffolding, a new scaffolding is placed on the interaction face, just like placing a block on full blocks (dirt, stone, etc.). There's an exception that trying to place a scaffolding on the bottom face of a scaffolding adds the new scaffolding on top of the highest scaffolding.
- When the player's eyes are inside the scaffolding, pressing use places a scaffolding to the direction the player is facing. There's an exception that trying to place a scaffolding on the bottom of the scaffolding adds the new scaffolding on top of the highest scaffolding.

The placing scaffolding may fall as a falling block if not adequately supported.

A diagram showing that scaffolding can be placed up to 6 blocks away from the base of support.
Scaffolding can be placed up to 6 blocks out from the base of support (i.e. scaffolding block on a solid block) that is targeted; any further scaffolding placed falls to the ground unless able to be supported by a different scaffolding block. Only one additional block can be placed after 6 blocks, even if more would be able to be placed.

Scaffolding has different collision detection. The player can climb up or down by jumping or sneaking respectively. in Java Edition, floating scaffoldings has solid bottom.

A scaffolding block can be moved by pistons, allowing them to be broken easily.

Scaffolding can be waterlogged.

In Bedrock Edition, scaffolding cannot be placed inside lava; if scaffolding is placed next to lava or fire, the scaffolding is destroyed. If it falls into lava or fire, it is destroyed immediately.

In Java Edition, scaffolding is not ignited by lava, and can be placed inside. It will be destroyed by fire.

Mobs don't spawn on scaffolding. In Bedrock Edition mobs can spawn inside of scaffolding if the block below the scaffolding is spawnable. In Java Edition very small mobs such as chickens can spawn in the empty space inside of a scaffolding block if the block below is spawnable.

Scaffolding resets the fall distance of players falling into it only while sneaking, and can be used to prevent fall damage. While in scaffolding, the speed of all mobs and players is decreased.

### Fuel
Scaffolding can be used as a fuel in furnaces, smelting 0.25 items per block.

## Data values
### ID
Java Edition:

| Name        | Identifier  | Form         | Block tags | Translation key             |
|-------------|-------------|--------------|------------|-----------------------------|
| Scaffolding | scaffolding | Block & Item | climbable  | block.minecraft.scaffolding |

Bedrock Edition:

| Name        | Identifier  | Numeric ID | Form                       | Item ID[i 1]   | Translation key       |
|-------------|-------------|------------|----------------------------|----------------|-----------------------|
| Scaffolding | scaffolding | 420        | Block & Giveable Item[i 2] | Identical[i 3] | tile.scaffolding.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block states

Java Edition:

| Name        | Default value | Allowed values | Description                                                                                         |
|-------------|---------------|----------------|-----------------------------------------------------------------------------------------------------|
| bottom      | false         | falsetrue      | If this scaffolding is floating.                                                                    |
| distance    | 7             | 01234567       | The distance from a center scaffolding horizontally. If it is 7, it becomes a falling block entity. |
| waterlogged | false         | falsetrue      | Whether or not there's water in the same place as this scaffolding.                                 |

Bedrock Edition:

| Name            | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                                                                         |
|-----------------|---------------|---------------|----------------|-------------------------|-----------------------------------------------------------------------------------------------------|
| stability       | 0x20x40x8     | 7             | 01234567       | 01234567                | The distance from a center scaffolding horizontally. If it is 7, it becomes a falling block entity. |
| stability_check | 0x1           | false         | falsetrue      | 01                      | If a scaffolding block has been checked for stability.[more information needed]                     |

### Falling block entity
Main article: Falling Block

Falling Block




Hitbox size


Height: 0.98 BlocksWidth: 0.98 Blocks 




{
    "title": "Falling Block",
    "rows": [
        {
            "field": "Height: 0.98 Blocks<br>Width: 0.98 Blocks",
            "label": "(link to Hitbox article, displayed as Hitbox size)"
        }
    ],
    "invimages": [],
    "images": []
}

 Dynamic block entity data
Tags common to all entities
 BlockState: The falling block represented by this entity.
 Name: The resource location of the block.
 Properties: Optional. The block states of the block.
 Name: The block state name and its value.
 CancelDrop: 1 or 0 (true/false) - true if the block should be destroyed instead of placed after landing on a solid block. When true, the block is not dropped as an item, even if the DropItem tag is set to true. However, if the entity is deleted due to its Time value being too high, this tag is ignored and an item is dropped depending on the DropItem tag. CancelDrop defaults to 1 for falling suspicious sand and suspicious gravel, and 0 for the other vanilla falling blocks and any summoned falling block.
 DropItem: 1 or 0 (true/false) – true if the block should drop as an item when it breaks. Any block that does not have an item form with the same ID as the block does not drop even if this is set.
 FallHurtAmount: Multiplied by the FallDistance to calculate the amount of damage to inflict. By default this value is 2 for anvils, and 6 for pointed dripstone.
 FallHurtMax: The maximum hit points of damage to inflict on entities that intersect this falling block. For vanilla falling blocks, always 40 × 20.
 HurtEntities: 1 or 0 (true/false) – true if the block should hurt entities it falls on. Defaults to 1 for anvils and pointed dripstone and to 0 for the other vanilla falling blocks and any summoned falling block.
 TileEntityData: Optional. The tags of the block entity for this block.
 Time: The number of ticks the entity has existed. When Time goes above 600, or above 100 while the block is at Y=-64 or is outside building height, the entity is deleted.

