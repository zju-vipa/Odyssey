# Vex
The vex is a small flying hostile mob wielding an iron sword, and is summoned only by evokers. It attacks by lunging at its target with its sword, and is capable of phasing through walls.

## Contents
- 1 Spawning
- 2 Drops
- 3 Behavior
- 4 Sounds
- 5 Data values
	- 5.1 ID
	- 5.2 Entity data
- 6 Achievements
- 7 Advancements
- 8 History
- 9 Issues
- 10 Trivia
- 11 Gallery
	- 11.1 Textures
		- 11.1.1 Old Model
	- 11.2 Screenshots
	- 11.3 In other media
- 12 References
- 13 External links

## Spawning
The vex spawns as part of an evoker's summoning attack: The evoker is surrounded by white particles and makes a magical, horn-like sound. Then, a group of three vexes appears near the evoker. The evoker can summon additional vexes even if some still remain alive from the last summoning.

The vex never spawns naturally, with the exception of evoker summoning, although it can be spawned using spawn eggs or via commands.

## Drops
In Java Edition, the vex's iron sword does not drop, because its main hand's HandDropChances is 0.  

In Bedrock Edition, the vex can drop its iron sword with random durability. This is not affected by the Looting enchantment.

5 is dropped when a vex is killed by a player or tamed wolf.

## Behavior
Vexes attack players, adult villagers, iron golems, and wandering traders if an evoker summoned them, and any other target as commanded by their summoning evoker (any mob that attacks the evoker accidentally or purposefully, or any mob that illagers naturally attack on sight). They still attack these mobs even when they do not have a weapon, and they deal the same damage. If it has no weapons, a mainhand-unarmed vex raises both of its hands when attacking; an unarmed vex can be spawned with this command /summon vex ~ ~ ~ {}. Vexes summoned by a monster spawner, spawn egg, or by the /summon command will only attack players unless provoked.

If any mob attacks a vex, any vexes in the area become hostile toward it. This includes "Johnny" vindicators that attack them, despite both being allied with the illagers.

Vexes are capable of flying through the air, and can freely pass through any block, including water and lava, without taking damage. Vexes can pass through bedrock, meaning it is possible for them to die in the Void. While vexes can pass through blocks easily, honey blocks seem to slow them down. Vexes also can be bounced back when pushed by a slime block.

While attacking, vexes glow red and lunge at their target. They often fly toward the back of their targets and attack from behind, making it difficult to block their attacks with a shield.

Vexes do not count toward the bossbar during a raid.

Vexes summoned by an evoker start taking damage after 30 to 119 seconds and eventually die.‌[Java Edition  only] Vexes summoned by a monster spawner, spawn egg, or by the /summon command don't take damage this way.

A vex does not despawn if it has a custom name or if it is in a block, minecart, or boat.

When idle, vexes wander within a 15×11×15 cuboid range centered on their evoker's position, unless summoned by a spawn egg or by the /summon command. This happens when the vexes killed the mob that their evoker commanded them to.

## Data values
### ID
Java Edition:

| Name | Identifier | Translation key        |
|------|------------|------------------------|
| Vex  | `vex`      | `entity.minecraft.vex` |

Bedrock Edition:

| Name | Identifier | Numeric ID | Translation key   |
|------|------------|------------|-------------------|
| Vex  | `vex`      | `105`      | `entity.vex.name` |

### Entity data
Vexes have entity data associated with them that contains various properties.

Java Edition:

Main article: Entity format
- Entity data
	- 
	- Tags common to all entities
	- 
	- Tags common to all mobs
	- BoundX: When a vex is idle, it wanders, selecting air blocks from within a 15×11×15 cuboid range centered at X,Y,Z =BoundX,BoundY,BoundZ.  This central spot is the location of the evoker when it summoned the vex, or if an evoker was not involved,BoundX,BoundYandBoundZdo not exist.
	- BoundY: SeeBoundX.
	- BoundZ: SeeBoundX.
	- LifeTicks: Ticks of life remaining, decreasing by 1 per tick. When it reaches zero, the vex starts taking damage andLifeTicksis set to 20.

Bedrock Edition:

SeeBedrock Edition level format/Entity format.

