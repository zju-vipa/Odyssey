### Charged creeper

Two creepers' explosion damage radius in the dirt. Comparison between a charged creeper's (left) and a normal creeper's (right). Notice that the charged creeper's explosion is much bigger than the normal creeper's explosion.
A charged creeper is created only when lightning strikes within four blocks of a normal creeper. The lightning can be created in any way, including naturally, with the /summon command, by a trident with the Channeling enchantment, or attracted to a lightning rod. Charged creepers are distinguished from normal creepers by their blue aura surrounding them, and their explosion power is significantly increased.

In Java Edition, a charged creeper can be summoned with the following command: /summon creeper ~ ~ ~ {powered:1}.

In Bedrock Edition, a charged creeper can be summoned by: /summon creeper ~ ~ ~ minecraft:become_charged.

Their countdown timers are the same as normal creepers, both in terms of range and time. With a power of 6, an explosion caused by a charged creeper is twice as powerful as the explosion caused by a creeper. Charged creepers' explosions are 50% more powerful than an explosion of TNT. How close the creeper was to the lightning strike does not affect the size or power of the explosion.

Charged creepers have the same entity ID as normal creepers. The only difference is that the value of the boolean powered tag is set to 1 (true).

In Java Edition, a charged creeper explosion that kills zombies, skeletons, wither skeletons, piglins, or other creepers causes one[2] of those mobs to drop its corresponding mob head. If multiple valid mobs are killed in the explosion, the one that drops a head is chosen at random. In Bedrock Edition, a charged creeper explosion that kills zombies, skeletons, wither skeletons, or other creepers causes all the killed mobs to drop their corresponding heads.[3]

A charged creeper does not drop its own head when it explodes, although any other charged creepers or creepers killed in the explosion drop a creeper head. Players and ender dragons do not drop their heads,[4] nor do mobs without corresponding mob heads, such as livestock animals.

### Farming
Main article: Tutorials/Creeper farming
## Data values
### ID
Java Edition:

| Name    | Identifier | Translation key          |
|---------|------------|--------------------------|
| Creeper | creeper    | entity.minecraft.creeper |

Bedrock Edition:

| Name    | Identifier | Numeric ID | Translation key     |
|---------|------------|------------|---------------------|
| Creeper | creeper    | 33         | entity.creeper.name |

### Entity data
Creepers have entity data associated with them that contains various properties.

Java Edition:

Main article: Entity format

 Entity data
Tags common to all entities
Tags common to all mobs
 ExplosionRadius: The radius of the explosion itself, default 3.
 Fuse: States the initial value of the creeper's internal fuse timer (does not affect creepers that fall and explode upon impacting their victim). The internal fuse timer returns to this value if the creeper is no longer within attack range. Default 30.
 ignited: 1 or 0 (true/false) - Whether the creeper has been ignited by flint and steel.
 powered: 1 or 0 (true/false) - May not exist. True if the creeper is charged from being struck by lightning.

Bedrock Edition:

See Bedrock Edition level format/Entity format.

