### Charged creeper

Two creepers' explosion damage radius in the dirt. Comparison between a charged creeper's (left) and a normal creeper's (right). Notice that the charged creeper's explosion is much bigger than the normal creeper's explosion.
A charged creeper is a stronger version of the normal creeper. It appears when lightning hits a normal creeper. A charged creeper has 6 explosion power, twich that of a normal creeper. 

When a charged creeper explodes, it can cause certian mobs to drop their coresponding mob head, viz: zombies, creepers, piglins‌[Java Edition  only], skeletons, and wither skeletons.

A charged creeper can be summoned:

In Java Edition /summon creeper ~ ~ ~ {powered:1}

In Bedrock Edition /summon creeper ~ ~ ~ minecraft:become_charged

### Farming
Main article: Tutorials/Creeper farming
## Data values
### ID
Java Edition:

| Name    | Identifier | Translation key            |
|---------|------------|----------------------------|
| Creeper | `creeper`  | `entity.minecraft.creeper` |

Bedrock Edition:

| Name    | Identifier | Numeric ID | Translation key       |
|---------|------------|------------|-----------------------|
| Creeper | `creeper`  | `33`       | `entity.creeper.name` |

### Entity data
Creepers have entity data associated with them that contains various properties.

Java Edition:

Main article: Entity format
- Entity data
	- 
	- Tags common to all entities
	- 
	- Tags common to all mobs
	- ExplosionRadius: The radius of the explosion itself, default 3.
	- Fuse: States the initial value of the creeper's internal fuse timer (does not affect creepers that fall and explode upon impacting their victim). The internal fuse timer returns to this value if the creeper is no longer within attack range. Default 30.
	- ignited: 1 or 0 (true/false) - Whether the creeper has been ignited byflint and steel.
	- powered: 1 or 0 (true/false) - May not exist. True if the creeper is charged from being struck by lightning.

Bedrock Edition:

SeeBedrock Edition level format/Entity format.

