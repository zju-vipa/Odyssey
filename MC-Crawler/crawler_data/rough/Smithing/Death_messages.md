# Death messages
Death messages are messages sent in the chat to either all players or a specific player to announce the death of a player or pet. These messages communicate how the entity died, and some are intended to be humorous.

Upon the death of a player, a death message is broadcast to everyone on a server. Upon the death of a pet wolf, cat, or parrot the message is broadcast to the pet's owner in Java Edition or to all players in the world in Bedrock Edition.[1] In Bedrock Edition, death messages are also produced upon the death of a pet horse, donkey, mule, llama, or trader llama.[2]

In Java Edition, death messages are automatically recorded in the game's logs. The death of a villager or a renamed mob is recorded in the game's logs, but not broadcast in chat.

Death messages can be made not to appear in chat (and therefore broadcast to other players) with the game rule showDeathMessages. This also affects the notification of a pet's death.

## Contents
- 1 Java Edition
	- 1.1 Current
	- 1.2 Temporary
		- 1.2.1 3D Shareware v1.34
		- 1.2.2 23w13a_or_b
		- 1.2.3 24w14potato
	- 1.3 Removed
- 2 Bedrock Edition
- 3 History
- 4 Trivia
- 5 References

## Java Edition
### Current
** Cactus **
- <player> was pricked to death
	- Appears when the player is killed because they were touching a cactus.
- <player> walked into a cactus while trying to escape <player/mob>
	- Appears when the player is hurt by a player or mob, then killed by touching a cactus.

** Drowning **
- <player> drowned
	- Appears when the player runs out of air underwater and is killed from drowning damage.
	- Also appears in the game's log when a namedblaze,enderman,strider,snow golemorbeetakes lethal damage from being in water, and when a namedfish,squid,glow squidortadpoletakes lethal damage from being out of water.
- <player> drowned while trying to escape <player/mob>
	- Appears when the player is hurt by a player or mob then dies from drowning.
	- Also appears in the game's log when one of the aforementioned mobs is hurt by a player or mob, then dies from drowning.

** Drying out **
- <entity> died from dehydration
	- Appears in the game's log when a nameddolphinoraxolotldies to being out of water.
- <entity> died from dehydration while trying to escape <player/mob>
	- Appears in the game's log when one of the aforementioned mobs is hurt by a player or mob, then dies to being out of water.

** Elytra **
- <player> experienced kinetic energy
	- Appears when the player is killed by hitting a wall while flying with elytra on.
- <player> experienced kinetic energy while trying to escape <player/mob>
	- Appears when the player is hurt by a player or mob, then hits a wall while flying with elytra on.

** Explosions **
- <player> blew up
	- Appears when the player is killed byTNTactivated byredstonemechanisms,fire, dispensed out from adispenser, by anend crystaltriggered by a projectile shot by a dispenser or summoned with/summon, by aminecart with TNTthat wasn't triggered by a player or mob, or by the explosion of afireballorwither skullsummoned with/summon.
- <player> was blown up by <player/mob>
	- Appears when the player is killed by a mob that exploded (e.g.creeper), by TNT activated by a player or mob, either by usingflint and steelor afire chargeon the block or shooting it with anarrowthat is on fire, by the explosion of an end crystal triggered by a player or mob, by the explosion of a minecart with TNT triggered by a player shooting it with an arrow that is on fire, or by the explosion of a fireball or wither skull shot by a player or mob.
- <player> was blown up by <player/mob> using <item>
	- Appears in any of the cases for the previous death message, when the killer player or mob (if any) is holding a renamed item.
- <player> was killed by [Intentional Game Design]
	- Appears when the player is killed by abedexploding inthe Netherorthe End, or by a chargedrespawn anchorexploding in theOverworldorthe End.
	- Includes a click-event link toMCPE-28723.

** Falling **
- <player> hit the ground too hard
	- Appears when the player is killed by a less than 5 block fall,ender pearldamage, or falling while riding anentitythat died due to fall damage.
- <player> hit the ground too hard while trying to escape <player/mob>
	- Appears when the player is hurt by a player or mob then killed by either a fall from less than 5 blocks,ender pearldamage, or when riding anentitythat died due to fall damage.
- <player> fell from a high place
	- Appears when the player is killed by a greater than 5 block fall.
- <player> fell off a ladder
	- Appears when the player is killed by falling after being on aladder.
- <player> fell off some vines
	- Appears when the player is killed by falling after being on avine.
- <player> fell off some weeping vines
	- Appears when the player is killed by falling after being on aweeping vine.
- <player> fell off some twisting vines
	- Appears when the player is killed by falling after being on atwisting vine.
- <player> fell off scaffolding
	- Appears when the player is killed by falling after traversing up or down throughscaffolding.
		- If the player falls from scaffolding that doesn't have scaffolding below it, it just counts as a greater than 5 block fall ("fell from a high place").
- <player> fell while climbing
	- Appears when the player is killed by falling after being on a climbable block that is not one of the aforementioned ones.
		- Onlycave vinesfall into this category in the vanilla game,[3]however one can make more blocks climbable using data packs.
	- Also appears when the player falls from any climbable block, changes dimension before dying, and then dies to fall damage.
		- This assumes there being no climbable block in the exact same position in the dimension the player teleported to, as the climbable block the player fell from. For instance, if a player falls off a ladder at x=0, y=100, z=0 in the overworld and they teleport to the End before they die, it must be the case that the block at x=0, y=100, z=0 in the End is not climbable, for this death message to appear.
			- If that block is climbable, then the death message for that block appears instead. In this example, if the block at those coordinates in the End is a vine (instead of a ladder), the death message<player> fell off some vinesappears instead of<player> fell off a ladder.
- death.fell.accident.water
	- Appears when the player dies to fall damage in water, which is ordinarily impossible because water cancels all fall damage.
	- Currently replicable in1.13+ by taking fall damage on a waterlogged slab in a minecart, or by having a trident enchanted with an insanely high level ofRiptide, then trying to use it inside deep water bodies.
	- This death message is untranslated due toMC-195467.
		- Before 1.16, this message was translated as<player> fell out of the water.
- <player> was doomed to fall
	- Appears when the player takes any environmental damage (i.e. damage not caused by entities) other thanvoiddamage, then dies to a greater than 5 block fall.
- <player> was doomed to fall by <player/mob>
	- Appears when the player takes any damage caused by an entity, then dies to a greater than 5 block fall.
		- This includesallentities, including non-mob entities, which means that, apart from a player or mob, <player/mob> in this case can also be any of the following, if the entity does not have a player or mob as its owner (if shot by a dispenser or summoned with/summon): arrow, spectral arrow, trident, fireball, small fireball, firework rocket, primed TNT, minecart with TNT, falling block (appears as "Falling <block name>").
			- Lightning bolts would be included in the list if they didn't deal environmental damage.
			- Thrown snowballs, eggs and ender pearls could theoretically also be included in the list, but they currently don't deal damage.
			- Wither skulls could theoretically also be included in the list, but they deal environmental damage when they don't have an owner.
			- Shulker bullets, thrown splash potions of harming and area effect clouds could theoretically also be included in the list, but strangely, the death message for dying to fall damage after being hit by one of those entities if they don't have an owner is<player> was doomed to fall.
			- Llama spits could theoretically also be included in the list, but they do not deal damage when they don't have an owner.
- <player> was doomed to fall by <player/mob> using <item>
	- Appears when the player takes any damage caused directly or indirectly by a player or mob holding a renamed item, then dies to a greater than 5 block fall.
- <player> was impaled on a stalagmite
	- Appears when the player falls on astalagmiteand dies.
- <player> was impaled on a stalagmite while fighting <player/mob>
	- Appears when the player is hurt by a player or mob, then falls on a stalagmite and dies.

** Falling blocks **
- <player> was squashed by a falling anvil
	- Appears when the player is killed by ananvilfalling on their head.
- <player> was squashed by a falling block
	- Appears when the player is killed by a falling block (other than an anvil or pointed dripstone) modified to inflict damage.
- <player> was skewered by a falling stalactite
	- Appears when the player is killed by a falling stalactite.

** Fire **
- <player> went up in flames
	- Appears when the player is killed because they were in afiresource block.
- <player> walked into fire while fighting <player/mob>
	- Appears when the player is hurt by a player or mob, then enters a fire source block.
- <player> burned to death
	- Appears when the player is killed because they were on fire, but not in a fire source block.
	- Also appears in the game's log when a namedsnow golemdies because of being in a hot biome.
- <player> was burned to a crisp while fighting <player/mob>
	- Appears when the player is hurt by a player or mob then killed because they were on fire.
	- Also appears in the game's log when a named snow golem is hurt by a player or mob, then dies to the heat in a hot biome.

** Firework rockets **
- <player> went off with a bang
	- Appears when the player is killed by the explosion of afirework rocket.
- <player> went off with a bang due to a firework fired from <item> by <player/mob>
	- Appears when the player is killed by the explosion of a firework rocket shot by a player or mob holding a renamed item.

** Lava **
- <player> tried to swim in lava
	- Appears when the player is killed because they were inlava.
- <player> tried to swim in lava to escape <player/mob>
	- Appears when the player is hurt by a player or mob, then enters lava and dies from it.

** Lightning **
- <player> was struck by lightning
	- Appears when the player is killed by alightningbolt.
- <player> was struck by lightning while fighting <player/mob>
	- Appears when the player is hurt by a player or mob, then killed by a lightning bolt.

** Magma block **
- <player> discovered the floor was lava
	- Appears when the player is killed because they were standing on amagma block.
- <player> walked into the danger zone due to <player/mob>
	- Appears when the player is hurt by a player or mob, then killed by magma block damage.

** Magic (Instant Damage / evoker fangs / guardian laser) **
- <player> was killed by magic
	- Appears when the player is killed by Instant Damage given with/effect, by an evoker fang summoned with/summonor by an arrow of harming shot from adispenseror summoned with/summon.
	- Also appears in the game's log when a named hostile mob dies to magic damage dealt by an activeconduit.
- <player> was killed by magic while trying to escape <player/mob>
	- Appears when the player is hurt by a player or mob then killed by Instant Damage or an evoker fang that didn't originate from a player or mob.
- <player> was killed by <player/mob> using magic
	- Appears when the player is killed by a potion or arrow of Harming shot by a player or mob, by an evoker fang summoned by an evoker or by the extra damage from a guardian's orelder guardian's laser.
		- If the player was killed by a splash potion of Harming shot from a dispenser or summoned with/summon, the death message is<player> was killed by Potion using magic.
		- If the player was killed by the cloud created by a lingering potion of Harming shot from a dispenser or summoned with/summon, the death message is<player> was killed by Area Effect Cloud using magic.
- <player> was killed by <player/mob> using <item>
	- Appears when the player is killed by one of the aforementioned ways but the player or mob is holding a renamed item during the player's death.

** Powder snow **
- <player> froze to death
	- Appears when the player is killed because they were in powder snow for too long.
- <player> was frozen to death by <player/mob>
	- Appears when the player is hurt by a player or mob, then dies from freezing damage.

** Players and mobs **
- <player> was slain by <player/mob>
	- Appears when the player is hurt by a player or mob and killed.
	- This death message is actually two different death messages:<player> was slain by <mob>and<player> was slain by <player>.
		- This means they can be customized completely independently of each other usingresource packs.
	- <player> was slain by <player>also appears when aparrotis fed acookie.
		- If the parrot was named, the message appears in the game's log. If it was tamed, the message is sent to its owner.
	- <player> was slain by <mob>also appears when the player is killed by ashulkerusing a shulker bullet, or allamausing its llama spit.
		- If the player was killed by a shulker bullet summoned with/summon, the death message is<player> was slain by Shulker Bullet. This doesn't work with llama spits, since they don't deal damage when they don't have an owner.
- <player> was slain by <player/mob> using <item>
	- Appears when the player is hurt by a player or mob holding a renamed item and killed.
	- This death message is actually two different death messages:<player> was slain by <mob> using <item>and<player> was slain by <player> using <item>.
		- This means they can be customized completely independently of each other using resource packs.
	- <player> was slain by <player> using <item>also appears when a parrot is fed a cookie by a player holding a named item in their main hand.
	- <player> was slain by <mob> using <item>also appears when the player is killed by ashulkerholding a renamed item using a shulker bullet, or allamaholding a renamed item using its llama spit.
- <player> was stung to death
	- Appears when the player is killed by abee.
- <player> was stung to death by <player/mob> using <item>
	- Appears when the player is killed by a bee that was holding a renamed item during the player's death.
- <player> was obliterated by a sonically-charged shriek
	- Appears when the player is killed by awardenusing its sonic boom.
- <player> was obliterated by a sonically-charged shriek while trying to escape <player/mob> wielding <item>
	- Appears when the player is killed by a warden holding a renamed item using its sonic boom.

** Projectiles **
- <player> was shot by <player/mob>
	- Appears when the player is killed by anarrowshot by a player or mob using aboworcrossbow.
	- When the player is killed by an arrow shot from a dispenser or summoned with/summon, the death message is<player> was shot by Arrow/Spectral Arrow.
- <player> was shot by <player/mob> using <item>
	- Appears when the player is killed by an arrow shot by a player or mob using a renamed bow or crossbow.
- <player> was pummeled by <player/mob>
	- Is coded to appear when the player is killed by asnowball,eggorender pearlshot by a player or mob. This is practically impossible, as these projectiles do not deal damage.
		- Blazestake damage from snowballs, which means that naming a blaze and killing it with snowballs sends this message to the game's log.
		- Because ofMC-72151, asnow golem's snowballs are able to hurt and killwolves,‌[until JE 1.20.5]after which the message would appear to the owner of the tamed wolf.
	- Theoretically, when the player is killed by a snowball or egg shot from a dispenser or summoned with/summon, or an ender pearl summoned with/summon, the death message is<player> was pummeled by Snowball/Thrown Egg/Thrown Ender Pearl.
- <player> was pummeled by <player/mob> using <item>
	- Is coded to appear when the player is killed by a snowball, egg or ender pearl shot by a player or mob that is holding a renamed item during the player's death. This is impossible, as these projectiles do not deal damage. However, as stated above, blazes take damage from snowballs, and snow golems can kill wolves, and if the killer in each case is holding a renamed item, this message appears instead.
- <player> was fireballed by <player/mob>
	- Appears when the player is killed by afireballshot by a player or mob.
	- When the player is killed by a fireball shot from a dispenser or summoned with/summon, the death message is<player> burned to death.
- <player> was fireballed by <player/mob> using <item>
	- Appears when the player is killed by a fireball shot by a player or mob that was holding a renamed item during the player's death.
- <player> was shot by a skull from <player/mob>
	- Appears when the player is killed by awither skullshot by a player or mob (only possible with thewither).
	- When the player is killed by a wither skull summoned with/summon, the death message is<player> was killed by magic.
- <player> was shot by a skull from <player/mob> using <item>
	- Appears when the player is killed by a wither skull shot by a player or mob that is holding a renamed item during the player's death.

** Starving **
- <player> starved to death
	- Appears when the player plays inHardorHardcoreand is killed by hunger damage because their hunger bar was at 0.
	- Also appears in the game's log when a namedvextakes damage after 30-119 seconds from when it was spawned and dies from it.
- <player> starved to death while fighting <player/mob>
	- Appears when the player plays inHardorHardcoreand is hurt by a player or mob, then killed by hunger damage.
	- Also appears in the game's log when a named vex dies to starvation after being hurt by a player or mob.

** Suffocation **
- <player> suffocated in a wall
	- Appears when the player is killed because they were inside of a non-transparent block.
- <player> suffocated in a wall while fighting <player/mob>
	- Appears when the player is hurt by a player or mob, then killed by suffocation damage.
- <player> was squished too much
	- Appears when the player is killed by themaxEntityCramminggamerule.
- <player> was squashed by <player/mob>
	- Appears when the player is hurt by a player or mob, then killed by themaxEntityCramminggamerule.
- <player> left the confines of this world
	- Appears when the player is killed because they were outside the world border.
- <player> left the confines of this world while fighting <player/mob>
	- Appears when the player is hurt by a player or mob then killed by world border damage.

** Sweet berry bushes **
- <player> was poked to death by a sweet berry bush
	- Appears when the player is killed because they were in a sweet berry bush.
- <player> was poked to death by a sweet berry bush while trying to escape <player/mob>
	- Appears when the player is hurt by a player or mob, then enters a sweet berry bush and dies from it.

** Thorns enchantment **
- <player> was killed while trying to hurt <player/mob>
	- Appears when the player is killed because they hurt aguardian,elder guardian, or a player or mob wearing armor enchanted withThorns.
- <player> was killed by <item> while trying to hurt <player/mob>
	- Appears when the player is killed because they hurt a guardian, elder guardian, or a player or mob wearing armor enchanted withThornsand holding a renamed item.

** Trident **
- <player> was impaled by <player/mob>
	- Appears when the player is killed by atridentshot by a player or mob.
	- When the player is killed by a trident shot from a dispenser‌[upcoming: JE Combat Tests]or summoned with/summon, the death message is<player> was impaled by Trident.
- <player> was impaled by <player/mob> with <item>
	- Appears when the player is killed by a trident shot by a player or mob that was holding a renamed item during the player's death.

** Void **
- <player> fell out of the world
	- Appears when the player is killed by being 64 blocks below the lowest point where blocks can be placed.
- <player> didn't want to live in the same world as <player/mob>
	- Appears when the player is hurt by a player or mob, then killed by the void.

** Wither effect **
- <player> withered away
	- Appears when the player is killed by theWitherstatus effect.
- <player> withered away while fighting <player/mob>
	- Appears when the player is hurt by a player or mob, then killed by the Wither status effect.

** Generic death **
- <player> died
	- Is coded to appear only when the player achieves a death that is not assigned to a damage type (magic,cactusetc.) or is assigned to thegenericdamage type. Currently replicable in1.17.1+ by naming a bee with a name tag, letting it sting a player, waiting for it to die and looking at the game's log.
- <player> died because of <player/mob>
	- Is coded to appear only when the player is hurt by a player or mob then achieves a death that is not assigned to a damage type or is assigned to thegenericdamage type. Currently replicable in1.17.1+ by naming a bee with a name tag, letting it sting a player, punching it while waiting for it to die naturally and looking at the game's log.
- <player> was killed
	- Appears when the player is killed using/kill.
- <player> was killed while fighting <player/mob>
	- Appears when the player is hurt by a player or mob, then killed using/kill.

** Crash prevention **
- <player> was killed by even more magic
	- Has a hover event, with textActually, message was too long to deliver fully. Sorry! Here's a stripped version: <message>
	- Appears when the regular death message is too large to send. This appears only on multiplayer servers and cannot appear in regular gameplay as it requires any variable of the death message (attacker, victim or item held) to exceed more than roughly 150,000 characters. It also cannot appear in chat, but only on the client side death screen message under the "You Died!" title.[4]

** Unsendable death messages **
The following table contains all death messages that can appear. Death messages in italic text are documented above, while messages in bold text can be achieved only with /damage, and thus are considered unsendable.
There are four types of context in which death messages can appear:

- The base environmental message, which appears when the damage is dealt without any entity being involved. Damage types whose base message contains the%2$svariable don't fill in any of the variables, resulting in the messages containing "%1$s" and "%2$s".
- The base entity message, which appears when the damage is dealt directly by a player or mob. The translation for this message is always the same as the base environmental message. Damage types whose base message contains the%2$svariable now fill in all variables, while base messages that don't contain that variable are completely indistinguishable from base environmental messages, though they are considered different messages and should not be confused with the base environmental messages.
- The.playermessage, which appears when the damage is dealt without any entity in mind, right after damage by a player or mob was dealt to the victim.
- The.itemmessage, which appears in place of the base entity message when the attacker was holding a renamed item during the victim's death.

The fall damage type shows a different set of messages if the height the victim fell from was greater than 5 blocks. Those messages are documented above.
The bad_respawn_point damage type is excluded from the table, as it shows the exact same death message in every context without changing any variables.

| Damage type                                       | Base message (environmental)                           | Base message (by entities)                             | .player message                                                                            | .item message                                                                                              |
|---------------------------------------------------|--------------------------------------------------------|--------------------------------------------------------|--------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| `arrow`                                           | %1$s was shot by %2$s                                  | <player> was shot by <player/mob>                      | death.attack.arrow.player                                                                  | <player> was shot by <player/mob> using <item>                                                             |
| `cactus`                                          | <player> was pricked to death                          | <player> was pricked to death                          | <player> walked into a cactus while trying to escape <player/mob>                          | death.attack.cactus.item                                                                                   |
| `cramming`                                        | <player> was squished too much                         | <player> was squished too much                         | <player> was squashed by <player/mob>                                                      | death.attack.cramming.item                                                                                 |
| `dragon_breath`                                   | <player> was roasted in dragon's breath                | <player> was roasted in dragon's breath                | <player> was roasted in dragon's breath by <player/mob>                                    | death.attack.dragonBreath.item                                                                             |
| `drown`                                           | <player> drowned                                       | <player> drowned                                       | <player> drowned while trying to escape <player/mob>                                       | death.attack.drown.item                                                                                    |
| `dry_out`                                         | <player> died from dehydration                         | <player> died from dehydration                         | <player> died from dehydration while trying to escape <player/mob>                         | death.attack.dryout.item                                                                                   |
| `explosion`                                       | <player> blew up                                       | <player> blew up                                       | <player> was blown up by <player/mob>                                                      | death.attack.explosion.item                                                                                |
| `fall`                                            | <player> hit the ground too hard                       | <player> hit the ground too hard                       | <player> hit the ground too hard while trying to escape <player/mob>                       | death.attack.fall.item                                                                                     |
| `falling_anvil`                                   | <player> was squashed by a falling anvil               | <player> was squashed by a falling anvil               | <player> was squashed by a falling anvil while fighting <player/mob>                       | death.attack.anvil.item                                                                                    |
| `falling_block`                                   | <player> was squashed by a falling block               | <player> was squashed by a falling block               | <player> was squashed by a falling block while fighting <player/mob>                       | death.attack.fallingBlock.item                                                                             |
| `falling_stalactite`                              | <player> was skewered by a falling stalactite          | <player> was skewered by a falling stalactite          | <player> was skewered by a falling stalactite while fighting <player/mob>                  | death.attack.fallingStalactite.item                                                                        |
| `fireball`                                        | %1$s was fireballed by %2$s                            | <player> was fireballed by <player/mob>                | death.attack.fireball.item                                                                 | <player> was fireballed by <player/mob> using <item>                                                       |
| `fireworks`                                       | <player> went off with a bang                          | <player> went off with a bang                          | <player> went off with a bang while fighting <player/mob>                                  | <player> went off with a bang due to a firework fired from <item> by <player/mob>                          |
| `fly_into_wall`                                   | <player> experienced kinetic energy                    | <player> experienced kinetic energy                    | <player> experienced kinetic energy while trying to escape <player/mob>                    | death.attack.flyIntoWall.item                                                                              |
| `freeze`                                          | <player> froze to death                                | <player> froze to death                                | <player> was frozen to death by <player/mob>                                               | death.attack.freeze.item                                                                                   |
| `generic`                                         | <player> died                                          | <player> died                                          | <player> died because of <player/mob>                                                      | death.attack.generic.item                                                                                  |
| `generic_kill`                                    | <player> was killed                                    | <player> was killed                                    | <player> was killed while fighting <player/mob>                                            | death.attack.genericKill.item                                                                              |
| `hot_floor`                                       | <player> discovered the floor was lava                 | <player> discovered the floor was lava                 | <player> walked into the danger zone due to <player/mob>                                   | death.attack.hotFloor.item                                                                                 |
| `in_fire`                                         | <player> went up in flames                             | <player> went up in flames                             | <player> walked into fire while fighting <player/mob>                                      | death.attack.inFire.item                                                                                   |
| `in_wall`                                         | <player> suffocated in a wall                          | <player> suffocated in a wall                          | <player> suffocated in a wall while fighting <player/mob>                                  | death.attack.inWall.item                                                                                   |
| `indirect_magic`                                  | %1$s was killed by %2$s using magic                    | <player> was killed by <player/mob> using magic        | death.attack.indirectMagic.player                                                          | <player> was killed by <player/mob> using <item>                                                           |
| `lava`                                            | <player> tried to swim in lava                         | <player> tried to swim in lava                         | <player> tried to swim in lava to escape <player/mob>                                      | death.attack.lava.item                                                                                     |
| `lightning_bolt`                                  | <player> was struck by lightning                       | <player> was struck by lightning                       | <player> was struck by lightning while fighting <player/mob>                               | death.attack.lightningBolt.item                                                                            |
| `magic`                                           | <player> was killed by magic                           | <player> was killed by magic                           | <player> was killed by magic while trying to escape <player/mob>                           | death.attack.magic.item                                                                                    |
| `mob_attack`                                      | %1$s was slain by %2$s                                 | <player> was slain by <player/mob>                     | death.attack.mob.player                                                                    | <player> was slain by <player/mob> using <item>                                                            |
| `mob_attack_no_aggro`                             | %1$s was slain by %2$s                                 | <player> was slain by <player/mob>                     | death.attack.mob.player                                                                    | <player> was slain by <player/mob> using <item>                                                            |
| `mob_projectile`                                  | %1$s was slain by %2$s                                 | <player> was slain by <player/mob>                     | death.attack.mob.player                                                                    | <player> was slain by <player/mob> using <item>                                                            |
| `on_fire`                                         | <player> burned to death                               | <player> burned to death                               | <player> was burned to a crisp while fighting <player/mob>                                 | <player> was burned to a crisp while fighting <player/mob> wielding <item>                                 |
| `out_of_world`                                    | <player> fell out of the world                         | <player> fell out of the world                         | <player> didn't want to live in the same world as <player/mob>                             | death.attack.outOfWorld.item                                                                               |
| `outside_border`                                  | <player> left the confines of this world               | <player> left the confines of this world               | <player> left the confines of this world while fighting <player/mob>                       | death.attack.outsideBorder.item                                                                            |
| `player_attack`                                   | %1$s was slain by %2$s                                 | <player> was slain by <player/mob>                     | death.attack.player.player                                                                 | <player> was slain by <player/mob> using item                                                              |
| `player_explosion`                                | %1$s was blown up by %2$s                              | <player> was blown up by <player/mob>                  | death.attack.explosion.player.player                                                       | <player> was blown up by <player/mob> using <item>                                                         |
| `sonic_boom`                                      | <player> was obliterated by a sonically-charged shriek | <player> was obliterated by a sonically-charged shriek | <player> was obliterated by a sonically-charged shriek while trying to escape <player/mob> | <player> was obliterated by a sonically-charged shriek while trying to escape <player/mob> wielding <item> |
| `spit`‌[upcoming: JE 1.20.5]                      | %1$s was slain by %2$s                                 | <player> was slain by <player/mob>                     | death.attack.mob.player                                                                    | <player> was slain by <player/mob> using <item>                                                            |
| `stalagmite`                                      | <player> was impaled on a stalagmite                   | <player> was impaled on a stalagmite                   | <player> was impaled on a stalagmite while fighting <player/mob>                           | death.attack.stalagmite.item                                                                               |
| `starve`                                          | <player> starved to death                              | <player> starved to death                              | <player> starved to death while fighting <player/mob>                                      | death.attack.starve.item                                                                                   |
| `sting`                                           | <player> was stung to death                            | <player> was stung to death                            | <player> was stung to death by <player/mob>                                                | <player> was stung to death by <player/mob> using <item>                                                   |
| `sweet_berry_bush`                                | <player> was poked to death by a sweet berry bush      | <player> was poked to death by a sweet berry bush      | <player> was poked to death by a sweet berry bush while trying to escape <player/mob>      | death.attack.sweetBerryBush.item                                                                           |
| `thorns`                                          | %1$s was killed while trying to hurt %2$s              | <player> was killed while trying to hurt <player/mob>  | death.attack.thorns.player                                                                 | <player> was killed by <item> while trying to hurt <player/mob>                                            |
| `thrown`                                          | %1$s was pummeled by %2$s                              | <player> was pummeled by <player/mob>                  | death.attack.thrown.player                                                                 | <player> was pummeled by <player/mob> using <item>                                                         |
| `trident`                                         | %1$s was impaled by %2$s                               | <player> was impaled by <player/mob>                   | death.attack.trident.player                                                                | <player> was impaled by <player/mob> with <item>                                                           |
| `unattributed_fireball`                           | <player> burned to death                               | <player> burned to death                               | <player> was burned to a crisp while fighting <player/mob>                                 | <player> was burned to a crisp while fighting <player/mob> wielding <item>                                 |
| `wind_charge`[experimental]‌[upcoming: JE 1.20.5] | %1$s was slain by %2$s                                 | <player> was slain by <player/mob>                     | death.attack.mob.player                                                                    | <player> was slain by <player/mob> using <item>                                                            |
| `wither`                                          | <player> withered away                                 | <player> withered away                                 | <player> withered away while fighting <player/mob>                                         | death.attack.wither.item                                                                                   |
| `wither_skull`                                    | %1$s was shot by a skull from %2$s                     | <player> was shot by a skull from <player/mob>         | death.attack.witherSkull.player                                                            | <player> was shot by a skull from <player/mob> using <item>                                                |

There are also a few other death messages which are unsendable:

- <player> fell too far and was finished by <player/mob>
	- Appears when the player takes damage that isn't fall or void damage, falls at least 5 blocks then takes fall damage dealt directly by a player or mob, which is only possible through the use of/damage.
- <player> fell too far and was finished by <player/mob> using <item>
	- Appears in the same situation as the previous message but instead when the player or mob that deals the fall damage is holding a renamed item.

### Temporary
These death messages existed only in April Fools' versions of the game.

#### 3D Shareware v1.34
- <player> was too soft for this world
	- Appeared when the player was in Obligatory nightmare mode and was killed by the constant damage they took there.
- <player> was too soft for this world (<player/mob> helped)
	- Appeared when the player was in Obligatory nightmare mode, was hurt by a player or mob and was killed by the constant damage they took there.

#### 23w13a_or_b
- <player> experienced the dark side of the moon
	- Appeared when the player ran out of air on the moon and died of asphyxiation.
- death.attack.onMoon.player
	- Appeared when the player was hurt by a player or mob then died of asphyxiation on the moon.
		- As with all other damage types on the table above, this damage type (on_moon) also had the death messagedeath.attack.onMoon.item, which could only appear when using the/damagecommand.
- <player> was turned into gold
	- Appeared when the player was turned into gold by another player while the ruleminecraft:midas_touchwas approved.
		- The damage type that caused this death message was special, meaning it didn't have any variants of the death message and thus it appeared no matter what attacked the player before they died.

#### 24w14potato
- <player> held the hot potato for too long.
	- Appeared when the player held ahot potatofor too long.
- death.attack.potato_heat.player
	- Appeared when the player was hurt by a player or mob then died to the heat from holding a hot potato.
		- As with all other damage types on the table above, this damage type (potato_heat) also had the death messagedeath.attack.potato_heat.item, which could only appear when using the/damagecommand.
- <player> was killed by a bad-tempered potato
	- Appeared when the player stood on apotato batteryfor too long, or tried to hurt aMega Spudwhile it had its forcefield around it.
- death.attack.potato_magic.player
	- Appeared when the player was hurt by a player or mob then died to either a potato battery or a Mega Spud's forcefield.
		- As with all other damage types on the table above, this damage type (potato_magic) also had the death messagedeath.attack.potato_magic.item, which could only appear when using the/damagecommand.

### Removed
In Java Edition snapshots 13w02a through 13w04a, a complicated system existed to show death messages for when the player fell to their death or fell and was killed by something else.
There were two types of messages:

- "<player> <first>",
- "<player> <first> and <last>".

<first> could be:

- fell (off a ladder|off some vines|out of the water|from a high place)
- was (shot|pummeled|blown|fireballed|knocked) (off a ladder|off some vines|out of the water|from a high place)
- was (shot|pummeled|blown|fireballed|knocked) (off a ladder|off some vines|out of the water|from a high place) by <player/mob>

<last> could be:

- into a pool of lava
- fell out of the world
- into a patch of fire
- into a patch of cacti
- got finished off by <player/mob>
- got finished off by <player/mob> using <item>
- got finished off using <item>

There were 352 different death messages.
(416 in the en_US.lang file, because the verb "blown" existed twice.)


All fall death messages:

<player> fell off a ladder
<player> fell off some vines
<player> fell out of the water
<player> fell from a high place
<player> was shot off a ladder
<player> was shot off some vines
<player> was shot out of the water
<player> was shot from a high place
<player> was pummeled off a ladder
<player> was pummeled off some vines
<player> was pummeled out of the water
<player> was pummeled from a high place
<player> was blown off a ladder
<player> was blown off some vines
<player> was blown out of the water
<player> was blown from a high place
<player> was fireballed off a ladder
<player> was fireballed off some vines
<player> was fireballed out of the water
<player> was fireballed from a high place
<player> was knocked off a ladder
<player> was knocked off some vines
<player> was knocked out of the water
<player> was knocked from a high place
<player> was shot off a ladder by <player/mob>
<player> was shot off some vines by <player/mob>
<player> was shot out of the water by <player/mob>
<player> was shot from a high place by <player/mob>
<player> was pummeled off a ladder by <player/mob>
<player> was pummeled off some vines by <player/mob>
<player> was pummeled out of the water by <player/mob>
<player> was pummeled from a high place by <player/mob>
<player> was blown off a ladder by <player/mob>
<player> was blown off some vines by <player/mob>
<player> was blown out of the water by <player/mob>
<player> was blown from a high place by <player/mob>
<player> was fireballed off a ladder by <player/mob>
<player> was fireballed off some vines by <player/mob>
<player> was fireballed out of the water by <player/mob>
<player> was fireballed from a high place by <player/mob>
<player> was knocked off a ladder by <player/mob>
<player> was knocked off some vines by <player/mob>
<player> was knocked out of the water by <player/mob>
<player> was knocked from a high place by <player/mob>
<player> fell off a ladder and into a pool of lava
<player> fell off some vines and into a pool of lava
<player> fell out of the water and into a pool of lava
<player> fell from a high place and into a pool of lava
<player> was shot off a ladder and into a pool of lava
<player> was shot off some vines and into a pool of lava
<player> was shot out of the water and into a pool of lava
<player> was shot from a high place and into a pool of lava
<player> was pummeled off a ladder and into a pool of lava
<player> was pummeled off some vines and into a pool of lava
<player> was pummeled out of the water and into a pool of lava
<player> was pummeled from a high place and into a pool of lava
<player> was blown off a ladder and into a pool of lava
<player> was blown off some vines and into a pool of lava
<player> was blown out of the water and into a pool of lava
<player> was blown from a high place and into a pool of lava
<player> was fireballed off a ladder and into a pool of lava
<player> was fireballed off some vines and into a pool of lava
<player> was fireballed out of the water and into a pool of lava
<player> was fireballed from a high place and into a pool of lava
<player> was knocked off a ladder and into a pool of lava
<player> was knocked off some vines and into a pool of lava
<player> was knocked out of the water and into a pool of lava
<player> was knocked from a high place and into a pool of lava
<player> was shot off a ladder by <player/mob> and into a pool of lava
<player> was shot off some vines by <player/mob> and into a pool of lava
<player> was shot out of the water by <player/mob> and into a pool of lava
<player> was shot from a high place by <player/mob> and into a pool of lava
<player> was pummeled off a ladder by <player/mob> and into a pool of lava
<player> was pummeled off some vines by <player/mob> and into a pool of lava
<player> was pummeled out of the water by <player/mob> and into a pool of lava
<player> was pummeled from a high place by <player/mob> and into a pool of lava
<player> was blown off a ladder by <player/mob> and into a pool of lava
<player> was blown off some vines by <player/mob> and into a pool of lava
<player> was blown out of the water by <player/mob> and into a pool of lava
<player> was blown from a high place by <player/mob> and into a pool of lava
<player> was fireballed off a ladder by <player/mob> and into a pool of lava
<player> was fireballed off some vines by <player/mob> and into a pool of lava
<player> was fireballed out of the water by <player/mob> and into a pool of lava
<player> was fireballed from a high place by <player/mob> and into a pool of lava
<player> was knocked off a ladder by <player/mob> and into a pool of lava
<player> was knocked off some vines by <player/mob> and into a pool of lava
<player> was knocked out of the water by <player/mob> and into a pool of lava
<player> was knocked from a high place by <player/mob> and into a pool of lava
<player> fell off a ladder and fell out of the world
<player> fell off some vines and fell out of the world
<player> fell out of the water and fell out of the world
<player> fell from a high place and fell out of the world
<player> was shot off a ladder and fell out of the world
<player> was shot off some vines and fell out of the world
<player> was shot out of the water and fell out of the world
<player> was shot from a high place and fell out of the world
<player> was pummeled off a ladder and fell out of the world
<player> was pummeled off some vines and fell out of the world
<player> was pummeled out of the water and fell out of the world
<player> was pummeled from a high place and fell out of the world
<player> was blown off a ladder and fell out of the world
<player> was blown off some vines and fell out of the world
<player> was blown out of the water and fell out of the world
<player> was blown from a high place and fell out of the world
<player> was fireballed off a ladder and fell out of the world
<player> was fireballed off some vines and fell out of the world
<player> was fireballed out of the water and fell out of the world
<player> was fireballed from a high place and fell out of the world
<player> was knocked off a ladder and fell out of the world
<player> was knocked off some vines and fell out of the world
<player> was knocked out of the water and fell out of the world
<player> was knocked from a high place and fell out of the world
<player> was shot off a ladder by <player/mob> and fell out of the world
<player> was shot off some vines by <player/mob> and fell out of the world
<player> was shot out of the water by <player/mob> and fell out of the world
<player> was shot from a high place by <player/mob> and fell out of the world
<player> was pummeled off a ladder by <player/mob> and fell out of the world
<player> was pummeled off some vines by <player/mob> and fell out of the world
<player> was pummeled out of the water by <player/mob> and fell out of the world
<player> was pummeled from a high place by <player/mob> and fell out of the world
<player> was blown off a ladder by <player/mob> and fell out of the world
<player> was blown off some vines by <player/mob> and fell out of the world
<player> was blown out of the water by <player/mob> and fell out of the world
<player> was blown from a high place by <player/mob> and fell out of the world
<player> was fireballed off a ladder by <player/mob> and fell out of the world
<player> was fireballed off some vines by <player/mob> and fell out of the world
<player> was fireballed out of the water by <player/mob> and fell out of the world
<player> was fireballed from a high place by <player/mob> and fell out of the world
<player> was knocked off a ladder by <player/mob> and fell out of the world
<player> was knocked off some vines by <player/mob> and fell out of the world
<player> was knocked out of the water by <player/mob> and fell out of the world
<player> was knocked from a high place by <player/mob> and fell out of the world
<player> fell off a ladder and into a patch of fire
<player> fell off some vines and into a patch of fire
<player> fell out of the water and into a patch of fire
<player> fell from a high place and into a patch of fire
<player> was shot off a ladder and into a patch of fire
<player> was shot off some vines and into a patch of fire
<player> was shot out of the water and into a patch of fire
<player> was shot from a high place and into a patch of fire
<player> was pummeled off a ladder and into a patch of fire
<player> was pummeled off some vines and into a patch of fire
<player> was pummeled out of the water and into a patch of fire
<player> was pummeled from a high place and into a patch of fire
<player> was blown off a ladder and into a patch of fire
<player> was blown off some vines and into a patch of fire
<player> was blown out of the water and into a patch of fire
<player> was blown from a high place and into a patch of fire
<player> was fireballed off a ladder and into a patch of fire
<player> was fireballed off some vines and into a patch of fire
<player> was fireballed out of the water and into a patch of fire
<player> was fireballed from a high place and into a patch of fire
<player> was knocked off a ladder and into a patch of fire
<player> was knocked off some vines and into a patch of fire
<player> was knocked out of the water and into a patch of fire
<player> was knocked from a high place and into a patch of fire
<player> was shot off a ladder by <player/mob> and into a patch of fire
<player> was shot off some vines by <player/mob> and into a patch of fire
<player> was shot out of the water by <player/mob> and into a patch of fire
<player> was shot from a high place by <player/mob> and into a patch of fire
<player> was pummeled off a ladder by <player/mob> and into a patch of fire
<player> was pummeled off some vines by <player/mob> and into a patch of fire
<player> was pummeled out of the water by <player/mob> and into a patch of fire
<player> was pummeled from a high place by <player/mob> and into a patch of fire
<player> was blown off a ladder by <player/mob> and into a patch of fire
<player> was blown off some vines by <player/mob> and into a patch of fire
<player> was blown out of the water by <player/mob> and into a patch of fire
<player> was blown from a high place by <player/mob> and into a patch of fire
<player> was fireballed off a ladder by <player/mob> and into a patch of fire
<player> was fireballed off some vines by <player/mob> and into a patch of fire
<player> was fireballed out of the water by <player/mob> and into a patch of fire
<player> was fireballed from a high place by <player/mob> and into a patch of fire
<player> was knocked off a ladder by <player/mob> and into a patch of fire
<player> was knocked off some vines by <player/mob> and into a patch of fire
<player> was knocked out of the water by <player/mob> and into a patch of fire
<player> was knocked from a high place by <player/mob> and into a patch of fire
<player> fell off a ladder and into a patch of cacti
<player> fell off some vines and into a patch of cacti
<player> fell out of the water and into a patch of cacti
<player> fell from a high place and into a patch of cacti
<player> was shot off a ladder and into a patch of cacti
<player> was shot off some vines and into a patch of cacti
<player> was shot out of the water and into a patch of cacti
<player> was shot from a high place and into a patch of cacti
<player> was pummeled off a ladder and into a patch of cacti
<player> was pummeled off some vines and into a patch of cacti
<player> was pummeled out of the water and into a patch of cacti
<player> was pummeled from a high place and into a patch of cacti
<player> was blown off a ladder and into a patch of cacti
<player> was blown off some vines and into a patch of cacti
<player> was blown out of the water and into a patch of cacti
<player> was blown from a high place and into a patch of cacti
<player> was fireballed off a ladder and into a patch of cacti
<player> was fireballed off some vines and into a patch of cacti
<player> was fireballed out of the water and into a patch of cacti
<player> was fireballed from a high place and into a patch of cacti
<player> was knocked off a ladder and into a patch of cacti
<player> was knocked off some vines and into a patch of cacti
<player> was knocked out of the water and into a patch of cacti
<player> was knocked from a high place and into a patch of cacti
<player> was shot off a ladder by <player/mob> and into a patch of cacti
<player> was shot off some vines by <player/mob> and into a patch of cacti
<player> was shot out of the water by <player/mob> and into a patch of cacti
<player> was shot from a high place by <player/mob> and into a patch of cacti
<player> was pummeled off a ladder by <player/mob> and into a patch of cacti
<player> was pummeled off some vines by <player/mob> and into a patch of cacti
<player> was pummeled out of the water by <player/mob> and into a patch of cacti
<player> was pummeled from a high place by <player/mob> and into a patch of cacti
<player> was blown off a ladder by <player/mob> and into a patch of cacti
<player> was blown off some vines by <player/mob> and into a patch of cacti
<player> was blown out of the water by <player/mob> and into a patch of cacti
<player> was blown from a high place by <player/mob> and into a patch of cacti
<player> was fireballed off a ladder by <player/mob> and into a patch of cacti
<player> was fireballed off some vines by <player/mob> and into a patch of cacti
<player> was fireballed out of the water by <player/mob> and into a patch of cacti
<player> was fireballed from a high place by <player/mob> and into a patch of cacti
<player> was knocked off a ladder by <player/mob> and into a patch of cacti
<player> was knocked off some vines by <player/mob> and into a patch of cacti
<player> was knocked out of the water by <player/mob> and into a patch of cacti
<player> was knocked from a high place by <player/mob> and into a patch of cacti
<player> fell off a ladder and got finished off by <player/mob>
<player> fell off some vines and got finished off by <player/mob>
<player> fell out of the water and got finished off by <player/mob>
<player> fell from a high place and got finished off by <player/mob>
<player> was shot off a ladder and got finished off by <player/mob>
<player> was shot off some vines and got finished off by <player/mob>
<player> was shot out of the water and got finished off by <player/mob>
<player> was shot from a high place and got finished off by <player/mob>
<player> was pummeled off a ladder and got finished off by <player/mob>
<player> was pummeled off some vines and got finished off by <player/mob>
<player> was pummeled out of the water and got finished off by <player/mob>
<player> was pummeled from a high place and got finished off by <player/mob>
<player> was blown off a ladder and got finished off by <player/mob>
<player> was blown off some vines and got finished off by <player/mob>
<player> was blown out of the water and got finished off by <player/mob>
<player> was blown from a high place and got finished off by <player/mob>
<player> was fireballed off a ladder and got finished off by <player/mob>
<player> was fireballed off some vines and got finished off by <player/mob>
<player> was fireballed out of the water and got finished off by <player/mob>
<player> was fireballed from a high place and got finished off by <player/mob>
<player> was knocked off a ladder and got finished off by <player/mob>
<player> was knocked off some vines and got finished off by <player/mob>
<player> was knocked out of the water and got finished off by <player/mob>
<player> was knocked from a high place and got finished off by <player/mob>
<player> was shot off a ladder by <player/mob> and got finished off by <player/mob>
<player> was shot off some vines by <player/mob> and got finished off by <player/mob>
<player> was shot out of the water by <player/mob> and got finished off by <player/mob>
<player> was shot from a high place by <player/mob> and got finished off by <player/mob>
<player> was pummeled off a ladder by <player/mob> and got finished off by <player/mob>
<player> was pummeled off some vines by <player/mob> and got finished off by <player/mob>
<player> was pummeled out of the water by <player/mob> and got finished off by <player/mob>
<player> was pummeled from a high place by <player/mob> and got finished off by <player/mob>
<player> was blown off a ladder by <player/mob> and got finished off by <player/mob>
<player> was blown off some vines by <player/mob> and got finished off by <player/mob>
<player> was blown out of the water by <player/mob> and got finished off by <player/mob>
<player> was blown from a high place by <player/mob> and got finished off by <player/mob>
<player> was fireballed off a ladder by <player/mob> and got finished off by <player/mob>
<player> was fireballed off some vines by <player/mob> and got finished off by <player/mob>
<player> was fireballed out of the water by <player/mob> and got finished off by <player/mob>
<player> was fireballed from a high place by <player/mob> and got finished off by <player/mob>
<player> was knocked off a ladder by <player/mob> and got finished off by <player/mob>
<player> was knocked off some vines by <player/mob> and got finished off by <player/mob>
<player> was knocked out of the water by <player/mob> and got finished off by <player/mob>
<player> was knocked from a high place by <player/mob> and got finished off by <player/mob>
<player> fell off a ladder and got finished off by <player/mob> using <item>
<player> fell off some vines and got finished off by <player/mob> using <item>
<player> fell out of the water and got finished off by <player/mob> using <item>
<player> fell from a high place and got finished off by <player/mob> using <item>
<player> was shot off a ladder and got finished off by <player/mob> using <item>
<player> was shot off some vines and got finished off by <player/mob> using <item>
<player> was shot out of the water and got finished off by <player/mob> using <item>
<player> was shot from a high place and got finished off by <player/mob> using <item>
<player> was pummeled off a ladder and got finished off by <player/mob> using <item>
<player> was pummeled off some vines and got finished off by <player/mob> using <item>
<player> was pummeled out of the water and got finished off by <player/mob> using <item>
<player> was pummeled from a high place and got finished off by <player/mob> using <item>
<player> was blown off a ladder and got finished off by <player/mob> using <item>
<player> was blown off some vines and got finished off by <player/mob> using <item>
<player> was blown out of the water and got finished off by <player/mob> using <item>
<player> was blown from a high place and got finished off by <player/mob> using <item>
<player> was fireballed off a ladder and got finished off by <player/mob> using <item>
<player> was fireballed off some vines and got finished off by <player/mob> using <item>
<player> was fireballed out of the water and got finished off by <player/mob> using <item>
<player> was fireballed from a high place and got finished off by <player/mob> using <item>
<player> was knocked off a ladder and got finished off by <player/mob> using <item>
<player> was knocked off some vines and got finished off by <player/mob> using <item>
<player> was knocked out of the water and got finished off by <player/mob> using <item>
<player> was knocked from a high place and got finished off by <player/mob> using <item>
<player> was shot off a ladder by <player/mob> and got finished off by <player/mob> using <item>
<player> was shot off some vines by <player/mob> and got finished off by <player/mob> using <item>
<player> was shot out of the water by <player/mob> and got finished off by <player/mob> using <item>
<player> was shot from a high place by <player/mob> and got finished off by <player/mob> using <item>
<player> was pummeled off a ladder by <player/mob> and got finished off by <player/mob> using <item>
<player> was pummeled off some vines by <player/mob> and got finished off by <player/mob> using <item>
<player> was pummeled out of the water by <player/mob> and got finished off by <player/mob> using <item>
<player> was pummeled from a high place by <player/mob> and got finished off by <player/mob> using <item>
<player> was blown off a ladder by <player/mob> and got finished off by <player/mob> using <item>
<player> was blown off some vines by <player/mob> and got finished off by <player/mob> using <item>
<player> was blown out of the water by <player/mob> and got finished off by <player/mob> using <item>
<player> was blown from a high place by <player/mob> and got finished off by <player/mob> using <item>
<player> was fireballed off a ladder by <player/mob> and got finished off by <player/mob> using <item>
<player> was fireballed off some vines by <player/mob> and got finished off by <player/mob> using <item>
<player> was fireballed out of the water by <player/mob> and got finished off by <player/mob> using <item>
<player> was fireballed from a high place by <player/mob> and got finished off by <player/mob> using <item>
<player> was knocked off a ladder by <player/mob> and got finished off by <player/mob> using <item>
<player> was knocked off some vines by <player/mob> and got finished off by <player/mob> using <item>
<player> was knocked out of the water by <player/mob> and got finished off by <player/mob> using <item>
<player> was knocked from a high place by <player/mob> and got finished off by <player/mob> using <item>
<player> fell off a ladder and got finished off using <item>
<player> fell off some vines and got finished off using <item>
<player> fell out of the water and got finished off using <item>
<player> fell from a high place and got finished off using <item>
<player> was shot off a ladder and got finished off using <item>
<player> was shot off some vines and got finished off using <item>
<player> was shot out of the water and got finished off using <item>
<player> was shot from a high place and got finished off using <item>
<player> was pummeled off a ladder and got finished off using <item>
<player> was pummeled off some vines and got finished off using <item>
<player> was pummeled out of the water and got finished off using <item>
<player> was pummeled from a high place and got finished off using <item>
<player> was blown off a ladder and got finished off using <item>
<player> was blown off some vines and got finished off using <item>
<player> was blown out of the water and got finished off using <item>
<player> was blown from a high place and got finished off using <item>
<player> was fireballed off a ladder and got finished off using <item>
<player> was fireballed off some vines and got finished off using <item>
<player> was fireballed out of the water and got finished off using <item>
<player> was fireballed from a high place and got finished off using <item>
<player> was knocked off a ladder and got finished off using <item>
<player> was knocked off some vines and got finished off using <item>
<player> was knocked out of the water and got finished off using <item>
<player> was knocked from a high place and got finished off using <item>
<player> was shot off a ladder by <player/mob> and got finished off using <item>
<player> was shot off some vines by <player/mob> and got finished off using <item>
<player> was shot out of the water by <player/mob> and got finished off using <item>
<player> was shot from a high place by <player/mob> and got finished off using <item>
<player> was pummeled off a ladder by <player/mob> and got finished off using <item>
<player> was pummeled off some vines by <player/mob> and got finished off using <item>
<player> was pummeled out of the water by <player/mob> and got finished off using <item>
<player> was pummeled from a high place by <player/mob> and got finished off using <item>
<player> was blown off a ladder by <player/mob> and got finished off using <item>
<player> was blown off some vines by <player/mob> and got finished off using <item>
<player> was blown out of the water by <player/mob> and got finished off using <item>
<player> was blown from a high place by <player/mob> and got finished off using <item>
<player> was fireballed off a ladder by <player/mob> and got finished off using <item>
<player> was fireballed off some vines by <player/mob> and got finished off using <item>
<player> was fireballed out of the water by <player/mob> and got finished off using <item>
<player> was fireballed from a high place by <player/mob> and got finished off using <item>
<player> was knocked off a ladder by <player/mob> and got finished off using <item>
<player> was knocked off some vines by <player/mob> and got finished off using <item>
<player> was knocked out of the water by <player/mob> and got finished off using <item>
<player> was knocked from a high place by <player/mob> and got finished off using <item>


## Bedrock Edition
- <player> was slain by Arrow
	- Appears when the player is killed by an arrow shot from a dispenser or summoned with/summon.
- <player> was shot by <player/mob>
	- Appears when the player is killed by an arrow shot by a player or mob.
- <player> was pricked to death
	- Appears when the player is killed because they were touching a cactus.
- <player> drowned
	- Appears when the player runs out of air underwater and is killed from drowning damage.
- <player> experienced kinetic energy
	- Appears when the player is killed by hitting a wall while flying with elytra on.
- <player> blew up
	- Appears when the player is killed by anend crystal, abedexploding inthe Netherorthe End, or by a chargedrespawn anchorexploding in theOverworldorthe End.
- <player> was blown up by Block of TNT
	- Appears when the player is killed by TNT activated byredstonemechanisms, fire, or dispensed out from adispenser.
- <player> was blown up by <player/mob>
	- Appears when the player is killed by an entity that exploded, or by TNT activated by a player or mob.
- <player> was poked to death by a sweet berry bush
	- Appears when the player is killed because they were in a sweet berry bush.
- <player> hit the ground too hard
	- Appears when the player is killed by a less than 5 block fall,ender pearldamage, or falling while riding anentitythat died due to fall damage.
- <player> fell from a high place
	- Appears when the player is killed by a greater than 5 block fall.
- <player> was squashed by a falling anvil
	- Appears when the player is killed by an anvil falling on their head.
- <player> was squashed by a falling block
	- Appears when the player is killed by a falling block (other than an anvil) modified to inflict damage.
- <player> went up in flames
	- Appears when the player is killed because they were in a fire source block.
- <player> burned to death
	- Appears when the player is killed because they were on fire, but not in a fire source block.
- <player> went off with a bang
	- Appears when the player is killed by the explosion of a firework rocket.
- <player> tried to swim in lava
	- Appears when the player is killed because they were in lava.
- <player> was struck by lightning
	- Appears when the player is killed by a lightning bolt.
- <player> discovered floor was lava
	- Appears when the player is killed because they were standing on a magma block.
- <player> was killed by magic
	- Appears when the player is killed by a potion of Harming shot from a dispenser, by Instant Damage given with/effector by an evoker fang summoned with/summon.
- <player> was killed by <player/mob> using magic
	- Appears when the player is killed by a potion or arrow of Harming shot by a player or mob, or by an evoker fang summoned by an evoker.
- <player> was slain by <player/mob>
	- Appears when the player is hurt by a player or mob and killed.
	- This death message is actually two different death messages:<player> was slain by <mob>and<player> was slain by <player>.
- <player> was slain by <player> using <item>
	- Appears when the player is hurt by a player holding a renamed item and killed.
- <player> was slain by Small Fireball
	- Appears when the player is killed by a fireball shot from a dispenser.
- <player> starved to death
	- Appears when the player plays onHarddifficulty and is killed by hunger damage because their hunger bar was at 0.
- <player> suffocated in a wall
	- Appears when the player is killed because they were inside of a non-transparent block.
- <player> was killed trying to hurt <player/mob>
	- Appears when the player is killed because they hurt a guardian, elder guardian, or a player or mob wearing armor enchanted withThorns.
- <player> was impaled to death by <player/mob>
	- Appears when the player is killed by a trident shot by a player or mob, or from a dispenser or summoned with/summon.
- <player> fell out of the world
	- Appears when the player is killed by being more than 64 blocks below the bottom of the world.
- <player> withered away
	- Appears when the player is killed by the witherstatus effect.
- <player> died
	- Appears when the player is killed by/kill.
- <player> was fireballed by <player/mob>
	- Appears when the player is killed by a fireball shot by a player or mob.
- <player> was sniped by <player/mob>
	- Appears when the player is killed by a shulker bullet shot by ashulker
- <player> was spitballed by <player/mob>
	- Appears when the player is killed by a llama spit shot by allama.
- <player> froze to death
	- Appears when the player is killed because they were in powder snow for too long.
- <player> was skewered by a falling stalactite
	- Appears when the player is killed by falling stalactite.
- <player> was impaled on a stalagmite
	- Appears when the player falls on a stalagmite and dies.
- <player> was obliterated by a sonically-charged shriek whilst trying to escape <player/mob>
	- Appears when the player is killed by a warden using its sonic boom.

** Unused death messages **
NOTE: These death messages appear only in the en_US.lang file.

- <player> was shot by <player/mob> using <item>
- <player> walked into a cactus whilst trying to escape <player/mob>
- <player> drowned whilst trying to escape <player/mob>
- <player> was fireballed by <player/mob> using <item>
- <player> was killed by <player/mob> using <item>
- <player> walked into fire whilst fighting <player/mob>
- <player> tried to swim in lava to escape <player/mob>
- <player> walked on danger zone due to <player/mob>
- <player> was burnt to a crisp whilst fighting <player/mob>
- <player> was pummeled by <player/mob>
- <player> was pummeled by <player/mob> using <item>
- <player> was obliterated by a sonically-charged shriek
- <player> fell off a ladder
- <player> fell off some vines
- <player> fell out of the water
- <player> was doomed to fall
- <player> was doomed to fall by <player/mob>
- <player> was doomed to fall by <player/mob> using <item>
- <player> fell too far and was finished by <player/mob>
- <player> fell too far and was finished by <player/mob> using <item>
- <player> was poked to death by a sweet berry bush whilst trying to escape <player/mob>

