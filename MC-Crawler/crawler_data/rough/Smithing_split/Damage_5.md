### Falling block
Falling block entities deal damage to players and mobs in the same block space where they land. The damage is dealt only on landing, and is not dealt to players and mobs that collide with falling block entities in mid-air.

A falling anvil deals 2 per block fallen after the first block (e.g., an anvil that falls 4 blocks deals 6 damage). A falling stalactite deals 6 per block fallen after the first block (e.g., a stalactite that falls 4 blocks deals 18 × 9 damage).

The damage is capped at 40 × 20, no matter how far the anvil or stalactite falls.

Helmets take twice as much durability damage as other armor pieces, but do not provide any special protection other than the normal armor damage reduction.[2]

If cheats are enabled, a falling block entity that deals damage can be summoned if its HurtEntities tag is set to true. The amount of damage dealt per block fallen can be customized via the FallHurtAmount tag, and the maximum damage dealt can be customized via the FallHurtMax tag.

### Thorns enchantment
When a player or mob deals melee or projectile damage to a player or mob that is wearing Thorns-enchanted armor, part of the damage is reflected back at the attacker. The amount varies with the enchantment level. (Level * 15% chance of inflicting 1–4 damage, or Level - 10 damage if level is over 10) however, thorns increases the amount of durability lost per hit on the enchanted armor.

### Suffocation
Suffocation occurs when a player or mob's eyeline is inside of certain blocks, receiving 1 damage every half-second. 

Blocks that are transparent or do not fill an entire block do not cause damage. This includes amethyst clusters, anvils, bamboo, banners, beds, bells, brewing stands, cakes, cauldrons, chains, chests, chorus flowers, chorus plants, cocoa beans, comparators, composters, daylight detectors, dragon eggs, enchanting tables, end portal frames, ender chests, fences, fence gates, flower pots, glass, grindstones, heads, honey blocks, hoppers, iron bars, leaves, lecterns, lightning rods, extended piston heads, repeaters, saplings, slabs that are not double, stairs, stonecutters, trapdoors, and walls. Despite being fully to partially transparent, barriers, beacons, ice, slime blocks, and monster spawner can cause suffocation. Dirt path and farmland can also cause suffocation, regardless of them not being full blocks.

The player's screen displays a darkened form of the block in which the player is suffocating. When the player is in third person, the view automatically switches to the first-person view.‌[Java Edition  only]

In Bedrock Edition, an oxygen bar is also present in the suffocation process. Water Breathing effects can prevent suffocation in Bedrock Edition.

The usual ways an entity can suffocate are:

- Sand,gravelorconcrete powderfalling into the space the entity occupies.
- Riding apig,boat, orminecartinto a one-block-high space.
- Riding ahorse,llama, orstriderinto a two-block-high space.
- Standing where atreejust grew from asapling, or where ahuge mushroomjust grew from amushroom.
- Standing where anend gatewayappeared after killing the dragon.
- Having a solid block pushed into the entity's head with apiston.
- Sleeping in abedsurrounded by blocks or having a solid block above it.‌[Bedrock Edition  only]
- Being teleported into a block or having one placed onto the entity viacommands(including/setblock,/fill, or/clone).
- When playing on a distant server, sometimes broken blocks can reappear due to lag, and if the player moves where the block respawned, it can provoke suffocation (for example, chopping down a tree by moving right below the trunk).
- When water and lava meet, and create acobblestone,stone, orobsidianblock on the entity's head.
- Standing a certain distance outside of theworld border, configurable with/worldborder damage buffer(default is 5 blocks).
- Summoning an entity inside a block throughspawn eggs, commands, or with agolemorwitherstructure lying down.
- Standing in 2 block deep water in snowy and cold biomes where the topmost layer of water freezes into ice
- Throwing anenderpearlin a way you end up inside a block you can suffocate in.

#### Entity cramming

  

This feature is exclusive to  Java Edition. 


In Java Edition, players and mobs take damage if too many entities are packed into the same block space. Specifically, the maxEntityCramming game rule defines the maximum number of entities that can be in a block without becoming crammed. Once the number of entities in the space of a single block exceeds this value, entity cramming occurs. When entity cramming occurs, a random selection of cram count = (entities in block) - maxEntityCramming living entities (players and mobs) become crammed. A living entity can be crammed by non-living entities, such as minecarts or armor stands, but not by block entities, such as item frames. The block space used for counting the number of entities is the axis and grid-aligned 1-meter cubic space containing the centers of the entities. An entity outside this space can collide with the entities within the space, but it can not become crammed by the entities within the space.

When crammed, a player or mob takes 6 suffocation damage every half-second, as long as that player or mob is pushing greater than that number of other entities. The default value for maxEntityCramming is 24 entities. This means that upto 24 entities can coexist in one block space without getting crammed.

If an entity is climbing, it does not count toward the number of entities in the block and does not contribute to cramming[3]. This means that climable blocks, such as ladders, vines, and scaffolding can prevent entity cramming. However, spiders and cave spiders are always counted toward the number of entities in the block when they are climbing. This can cause entities on climbable blocks to become crammed.

If a player is killed by entity cramming damage, the death message reads <player> was squished too much.

### Drowning
The oxygen bar.
A player who runs out of air underwater begins drowning, taking approximately 2 damage per second. Damage is taken when the air supply value reaches -20. Usually, the air supply value decreases each game tick. It resets to 0 after damaging. Respiration gives a chance for air supply to not decrease itself per game tick. Chance is x/(x + 1), where x is the level of enchantment.

When the game rule drowningDamage is set to false, the air supply of players deplete normally, but no drowning damage is inflicted when players run out of air.

Mobs can also drown, although most mobs that can drown attempt to swim upward. Normally, mobs can remain underwater for 15 seconds before their air supply fully depletes. They can remain underwater for 16 seconds before actually beginning to take damage.

- Asquid,glow squid,tadpole, or any kind offishsuffocates in air instead of drowning in water.
- Dolphinscan suffocate in air or drown in water and must be given access to both to survive.
- Aquatic mobs,undead mobs,iron golemsandfrogsare immune to drowning.
- Azombiedoes not take drowning damage; instead, it begins the process of converting to adrownedmob when continuously in water for 30 seconds.
- Similar to a zombie, ahuskdoes not take damage from drowning, but first converts into a zombie, which then converts to a drowned if it remains underwater.
- Piglins,piglin brutesandhoglinsdo not attempt to swim upward in water, and drown as a result.
	- Because these mobs normally zombify outside the Nether before they can start drowning, this can only happen if theirIsImmuneToZombificationtag set totrue, or that water is created in the Nether using commands.

When the player is no longer submerged in water or is in a bubble column, the air supply regenerates at a rate of 1 bubble every 0.2 seconds (4 game ticks). A Respiration helmet adds an additional on average 15 seconds duration underwater per enchantment level, and a turtle shell adds an additional 10 seconds. Water Breathing and Conduit Power regenerate the air supply. In Bedrock Edition, both effects affect squid and fish.

