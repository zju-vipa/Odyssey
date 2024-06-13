# Llama Spit
Llama Spit is a projectile produced by llamas that deals a small amount of damage.

## Contents
- 1 Behavior
- 2 Sounds
- 3 Data values
	- 3.1 ID
	- 3.2 Entity data
- 4 History
- 5 Gallery
	- 5.1 Screenshots

## Behavior
Llama spit that hits an entity deals 1 damage. Despite the spit being a projectile, dying from llama spit still shows the death message "<player> was slain by trader llama/llama." In Bedrock, however, the death message is "<player> was spitballed by trader llama/llama".

The spit entity must belong to an entity to do damage, meaning that a spit entity summoned by commands does no damage unless its Owner NBT attribute matches the UUID of an entity in loaded chunks. 

In Bedrock Edition, llama spit can be deflected if hit by the player.

Llama spit can not pass through any blocks, including non-solid blocks (ex. signs, open fencegate & sugarcane); this even includes water. The spitting animation still shows the trajectory but the spit entity that does damage terminates on the non-solid block.

Llama spit can be blocked by a shield.

## Data values
### ID
Java Edition:

| Name       | Identifier   | Translation key               |
|------------|--------------|-------------------------------|
| Llama Spit | `llama_spit` | `entity.minecraft.llama_spit` |

Bedrock Edition:

| Name       | Identifier   | Numeric ID | Translation key          |
|------------|--------------|------------|--------------------------|
| Llama Spit | `llama_spit` | `102`      | `entity.llama_spit.name` |

### Entity data
Java Edition:

Main article: Entity format
Llama spit have entity data associated with them that contain various properties.

- Entity data
	- 
	- Tags common to all entities
	- 
	- Tags common to all projectiles

Bedrock Edition:

SeeBedrock Edition level format/Entity format.
