# Enderman
An enderman is a tall neutral mob found in all three dimensions. Endermen normally ignore players but run to attack those that damage it or look directly at its face. Endermen teleport to avoid water (which harms them), sunlight, projectiles and some other damage sources, and they occasionally pick up certain blocks.

## Contents
- 1 Spawning
	- 1.1 Overworld
	- 1.2 Nether
	- 1.3 End
- 2 Drops
	- 2.1 On death
- 3 Behavior
	- 3.1 Teleportation
	- 3.2 Moving blocks
- 4 Sounds
- 5 Data values
	- 5.1 ID
	- 5.2 Entity data
- 6 Achievements
- 7 Advancements
- 8 Video
- 9 History
- 10 Issues
- 11 Trivia
- 12 Gallery
	- 12.1 Renders
	- 12.2 Screenshots
	- 12.3 In other media
- 13 References
- 14 External links

## Spawning
An enderman in the Overworld.
Endermen can spawn on any solid surface that has at least three empty spaces above, at the light level of 0 in the Overworld and the End, or a light level of 7  or less in the Nether. They are the only mobs that spawn naturally in all 3 dimensions.

### Overworld
Endermen spawn uncommonly in the Overworld, in all biomes except mushroom fields and deep dark. They often spawn in groups of two, and rarely in groups of three.

### Nether
Endermen spawn rarely in soul sand valleys, uncommonly in nether wastes and most commonly in warped forests.

### End
Endermen spawn commonly in groups of up to four, anywhere in the End dimension.

## Drops
### On death
| Item |             | Roll Chance | Quantity (Roll Chance) |           |            |             |
|------|-------------|-------------|------------------------|-----------|------------|-------------|
|      |             |             | Default                | Looting I | Looting II | Looting III |
|      | Ender Pearl | 100%        | 0–1                    | 0–2       | 0–3        | 0–4         |

- 5 when killed by a player or a tamedwolf.
- Any block being held (see§ Moving blocksfor more information)

## Behavior
An enderman can be provoked by a player or other mob attacking them. They can also be provoked by a player looking them in the eyes for 5 game ticks (1⁄4 second)[1] from up to 64 blocks away. Endermen open their mouths and begin to shake‌[Java Edition  only] angrily if provoked; they also make loud and lengthy sounds while being stared at. If the player continues to maintain eye contact, the enderman does not move, although it may teleport away. Once the player stops looking at the enderman, it runs toward the back of the player to attack, although it ceases if hit by another player or mob.[2] An aggravated enderman runs fast and often teleports to the location of a player or mob up to 32 blocks away (orthogonally). Endermen are not provoked by a player viewing it through a transparent block or while wearing a carved pumpkin.

An aggravated enderman pursues the player until it is either killed or distracted by external elements, such as rain or fire. They do not take damage from sunlight like undead mobs, but when at a sufficient light level under the sky during the day they teleport randomly, typically winding up in caves (although certain non-full blocks, such as soul sand and mud, also register as "dark" when the enderman is standing in them).

Endermen can be harmed by melee attacks, water, lava, fire, splash water bottles, or rain. They are not damaged when standing in a filled cauldron‌[Java Edition  only].[3] Endermen teleport away when they take damage from any of natural sources (1), continuing to do so until they find a safe location. They also teleport while taking damage from other sources, such as suffocation, Poison, or Wither. 

Ranged attacks are ineffective against endermen, as they teleport when hit by a projectile instead of taking damage. Endermen that are hit by projectiles do not become hostile.[4] Arrows‌[Java Edition  only] and tridents appear to bounce off an enderman who is unable to teleport. In Bedrock Edition, arrows go straight through endermen that are unable to teleport (but the effect still goes through if it's a tipped arrow).[needs in-game testing]. 

Endermen can step up one full block without having to jump.

Endermen are hostile to endermites within 64 blocks but are passive to other mobs unless provoked.

An enderman in a player's vicinity prevents the player from sleeping in a bed at night as if any hostile mob were nearby. If the player is already asleep in a bed, it is possible for an enderman to teleport on it and wake players by pushing them off.

The endermen's aggression range for being looked at is reduced when the player is sneaking, or under the Invisibility effect depending on the number of armor pieces currently worn. The detection range in blocks for invisible players is shown in the following table:

| Number of armor pieces | Sneaking | Normal |
|------------------------|----------|--------|
| 0                      | 3        | 4      |
| 1                      | 8        | 11     |
| 2                      | 17       | 22     |
| 3                      | 26       | 33     |
| 4                      | 35       | 44     |

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
