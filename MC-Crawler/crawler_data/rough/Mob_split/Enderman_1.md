### Moving blocks
Unlike any other mobs, which cannot hold blocks except as items, endermen have a unique ability to pick up, carry and set down certain blocks. Every tick they have 1⁄20 (5%) chance to select random block in a 4×3×4 (xyz) region horizontally centered on the enderman and vertically encompassing it. If enderman can directly see this block and block is in allowed list, it will pick up this block. An enderman cannot pick up blocks in a completely flat area. Endermen drop the block they are holding upon death as an item, although they do not visually let go of the block when dying.[9][10] It does not despawn while holding a block. Endermen cannot place blocks onto bedrock or entities.

Endermen can pick up the following blocks:

- Cactus
- Clay
- Coarse Dirt
- Rooted Dirt
- Dirt
- Flowers (short)
- Fungi
- Crimson Roots
- Warped Roots
- Grass Block
- Gravel
- Melon
- Moss Block
- Mud
- Muddy Mangrove Roots
- Mushrooms
- Mycelium
- Nylium
- Podzol
- Pumpkins
- Red Sand
- Sand
- TNT

Data packs from Java Edition can change this list by modifying the minecraft:enderman_holdable block tag.

Behavior packs from Bedrock Edition can not modify these as the list is hard-coded behind the minecraft:behavior.enderman_take_block method. 

While carrying a block, every tick the enderman has 1⁄2000 (0.05%) chance to silently[11] place it in a 2×2×2 region horizontally centered on the enderman and vertically at the same level as the enderman itself if the target location is air with a non-air block beneath and the block is allowed to be placed at the target location.

Endermen cannot pick up or place down blocks if the game rule mobGriefing is set to false.

Endermen can randomly breach walls, bridge fences, break redstone circuitry, set off explosions and kill themselves if they place a block of TNT on a power source and even construct golems by removing or placing blocks.

Endermen can pick up or place down blocks even when angry.

In Java Edition, users can summon an enderman holding any block (including the ones not listed above) using the carriedBlockState NBT data. For example, to summon an enderman holding a grass block with no AI where the player is standing:

/summon minecraft:enderman ~ ~ ~ {NoAI:1,carriedBlockState:{Name:"grass_block"}}
Enderman summoned with custom block will be able to place it, even if block is not on allowed list. It can place any block, including technical blocks like end portal.

## Data values
### ID
Java Edition:

| Name     | Identifier | Translation key             |
|----------|------------|-----------------------------|
| Enderman | `enderman` | `entity.minecraft.enderman` |

Bedrock Edition:

| Name     | Identifier | Numeric ID | Translation key        |
|----------|------------|------------|------------------------|
| Enderman | `enderman` | `38`       | `entity.enderman.name` |

### Entity data
Endermen have entity data associated with them that contains various properties.

Java Edition:

Main article: Entity format
- Entity data
	- 
	- Additional fields for mobs that can become angry
	- 
	- Tags common to all entities
	- 
	- Tags common to all mobs
	- carriedBlockState: Optional. The block carried by the enderman.
		- Name: Theresource locationof the block.
		- Properties: Optional. Theblock statesof the block.
			- Name: The block state name and its value.

Bedrock Edition:

SeeBedrock Edition level format/Entity format.

