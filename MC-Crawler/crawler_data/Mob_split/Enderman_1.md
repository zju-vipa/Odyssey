### Teleportation
They play a sound exclusively at the teleportation destination.[5]

Each teleportation attempt chooses a random destination 32 blocks along each axis (i.e. a 64×64×64 cube centered on the current position). It then applies the following checks:

- As long as the selected block is not a made of amovement-blocking material, seek downwards. If the found block is waterlogged, the teleportation attempt fails.
- Starting again with the originally selected target, seek downwards as long as the block below is not a made of amovement-blocking material. The teleportation attempt succeeds if no liquid orsolid blocksprevent them from standing at the destination.

Thus, endermen need at least three non-solid blocks above the destination to successfully teleport, and do not teleport to waterlogged blocks unless the ceiling above is made of a non-waterlogged movement-blocking material.[6]

Blocks that have a large enough collision box but are not made of a movement-blocking material, such as carpet that is not above a block made of a movement-blocking material, snow layers 10 or more deep, and azalea, can be used to prevent teleportation. Endermen always teleport an integer Y distance, so an enderman at Y=70.0 cannot teleport onto a movement-blocking block covered by a single carpet, snow layers only 2 deep, or many other short blocks, while an enderman at Y=70.99 could teleport onto snow layers 8 or 9 deep.

Endermen always attempt to teleport upon taking damage. Most melee attacks are successful, but the enderman usually teleports a few blocks behind the player when hit, if there is space behind the player. Endermen can be attacked with projectiles if they are in a boat or minecart.‌[Java Edition  only] If all available blocks within teleport distance are removed or unavailable as a destination, it is possible to hit endermen in Java Edition with a projectile, although arrows may simply bounce off, dealing no damage.[7] When teleporting due to damage, it makes 64 attempts to teleport.   

In Java Edition, an enderman cannot teleport while it is in a minecart or boat, although in rain and water it attempts to do so, always teleporting back repeatedly until death. This does not occur in Bedrock Edition.[8]

### Moving blocks
Unlike any other mobs, which cannot hold blocks except as items, endermen have a unique ability to pick up, carry and set down certain blocks. They silently[9] pick up blocks in a 4×3×4 (xyz) region horizontally centered on the enderman and vertically encompassing it. An enderman cannot pick up blocks in a completely flat area. Endermen drop the block they are holding upon death as an item, although they do not visually let go of the block when dying.[10][11] It does not despawn while holding a block. Endermen cannot place blocks onto bedrock or entities.

Endermen can pick up the following blocks:


Cactus
Clay
Coarse Dirt
Rooted Dirt
Dirt
Flowers (short)
  Fungi
Crimson Roots
Warped Roots
Grass Block
Gravel
Melon
Moss Block
Mud
Muddy Mangrove Roots
Mushrooms
Mycelium
  Nylium
Podzol
  Pumpkins
Red Sand
Sand
TNT
Data packs from Java Edition can change this list by modifying the minecraft:enderman_holdable block tag.

Behavior packs from Bedrock Edition can not modify these as the list is hard-coded behind the minecraft:behavior.enderman_take_block method. 

While carrying a block, the enderman sometimes silently[12] places it in a 2×2×2 region horizontally centered on the enderman and vertically at the same level as the enderman itself if the target location is air with a non-air block beneath and the block is allowed to be placed at the target location.

Endermen cannot pick up or place down blocks if the game rule mobGriefing is set to false.

Endermen can randomly breach walls, bridge fences, break redstone circuitry, set off explosions and kill themselves if they place a block of TNT on a power source and even construct golems by removing or placing blocks.

Endermen can pick up or place down blocks even when angry.

In Java Edition, users can summon an enderman holding any block (including the ones not listed above) using the carriedBlockState NBT data. For example, to summon an enderman holding a grass block with no AI where the player is standing:

/summon minecraft:enderman ~ ~ ~ {NoAI:1,carriedBlockState:{Name:"grass_block"}}
## Data values
### ID
Java Edition:

| Name     | Identifier | Translation key           |
|----------|------------|---------------------------|
| Enderman | enderman   | entity.minecraft.enderman |

Bedrock Edition:

| Name     | Identifier | Numeric ID | Translation key      |
|----------|------------|------------|----------------------|
| Enderman | enderman   | 38         | entity.enderman.name |

### Entity data
Endermen have entity data associated with them that contains various properties.

Java Edition:

Main article: Entity format

 Entity data
Additional fields for mobs that can become angry
Tags common to all entities
Tags common to all mobs
 carriedBlockState: Optional. The block carried by the enderman.
 Name: The resource location of the block.
 Properties: Optional. The block states of the block.
 Name: The block state name and its value.

Bedrock Edition:

See Bedrock Edition level format/Entity format.

