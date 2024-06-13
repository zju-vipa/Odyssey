### Knockback
When receiving damage from players, mobs, most projectiles, or explosions, players and mobs are also knocked back. The resulting disorientation and loss of control should not be underestimated, as it is possible to be knocked back over a cliff or into lava, both of which are potentially fatal.

A sprinting attack causes extra knockback. A thrown egg or snowball also causes knockback, despite not damaging most mobs. Players whoever do not receive knockback from a thrown egg or snowball. Entities riding another entity never receive any knockback when attacked. Iron golems, shulkers, agents, NPCs,  wardens, and the ender dragon also don't receive knockback, and certain other mobs have varying levels of knockback resistance. Each piece of netherite armor adds 10% knockback resistance to its wearer, giving 40% knockback resistance with a full set.

Knockback resistance reduces knockback by multiplying the velocity a mob receives from knockback. If the velocity the mob would have without any knockback resistance is v, and the mob has a knockback resistance of r%, then the mob's actual velocity is determined by the formula A=v×(1−r100).

## Natural damage
Besides mob attacks, players can take damage from several other sources.

### Lightning damage
Lightning striking on or near the player inflicts 5 damage, which can be reduced with armor. Natural lightning strikes on the player are rare and occur only during thunderstorms. Players and mobs that get hit by lightning are set on fire, which is quickly extinguished by the rain during a thunderstorm.

### Fall damage
All players and most mobs receive damage when falling from great heights.

Fall damage is calculated based on change in the Y coordinate of the entity's position, rather than the entity's velocity when hitting the ground. This means that fall damage is also not based on the distance fallen, since an mid-air entity on a lead can travel a lot of distance as it bobs up and down.

Fall damage is 1 for each block of change in Y after the third. Thus, falling 4 blocks causes 1 damage, 2 damage for 5 blocks, and so forth:

fall damage = max(0, -(change in Y) − 3)
- Note that the change in Y needs to be negative, because falling upward is not normally possible and never does any damage. If the fall damage would be less than or equal to 0, then the entity simply does not take damage.

While a 23-block fall should be fatal for a player at full health (23 - 3 = 20 × 10 of damage), due to the way the change in Y is calculated, a 23.5-block fall is required instead, because the last half-block of change in Y usually isn't added in when calculating fall damage. For certain heights, including 23-block falls, this discrepancy is enough to avoid an entire 1 of damage.

Therefore, without Feather Falling or relevant status effects, or immunity to fall damage, the minimum guaranteed lethal change in Y for any mob is:

fatal change in Y = -(health + 3.5)
#### Fall damage resistance
Unenchanted Armor does not reduce fall damage. However, some echantments do reduce fall damage: Feather Falling and Protection.

Some status effects reduce fall damage:

- Slow Falling- Negates all fall damage. If the effect wears off mid-air, the entity only takes damage for the height difference between where the effect ended and where the entity lands.
- Resistance

Every player is immune to fall damage when the game rule fallDamage is set to false. Players who can fly are not immune to fall damage, and take fall damage for the change in Y from where they stop flying to where they land.

Hostile mobs that are immune to fall damage:

- Blaze
- Breeze
- Chicken Jockey
- Ender Dragon
- Ghast
- Magma Cube
- Phantom
- Shulker
- Vex
- Wither

Passive mobs that are immune to fall damage:

- Allay
- Agent
- Bat
- Bee
- Cat
- Chicken
- Iron Golem
- NPC
- Ocelot
- Parrot
- Snow Golem

Other mobs with resistance to fall damage:

- These mobs take damage as if they fell only half the distance:
	- Camel
	- Donkey
	- Horse
	- Mule
	- Skeleton Horse
	- Zombie Horse
	- Llama

- This mob always takes 10less fall damage:
	- Goat

- This mob always takes 5less fall damage:
	- Frog

- This mob takes damage for 5 blocks less than it fell, and its fall damage is not affected byJump Boost:
	- Fox

##### Sound
For most solid blocks, if a player of mob falls onto the blocks and takes damage, a sound plays and is transmitted to the environment. No sound is played or transmitted if the entity doesn't take damage. Falling from a small height (4–7 blocks) plays a thud sound, and falling from a larger height (8 or more blocks) give a click or cracking sound.

#### Fall damage reduction
In some cases, falling damage can be avoided:

- Sneakingprevents a player from falling off a drop of one block or greater.
- Entering or being inwater(when not in a boat) resets the change in Y. This includes falling into the water of any depth, as long as the entity collides with the water before colliding with the ground.
- Colliding with acobwebresets the entity's change in Y.
- Being inlavareduces the change in Y by half a block eachgame tick.
- Flying usingelytrasuch that the vertical movement is upward, level or less than 0.5 blocks per game tick downward resets change in Y to 1 block.
- Moving into aladderorvine's area of effect resets the fall damage. This also applies totrapdoorsacting as a ladder.
	- Falling onto the top of a ladder does not reset the change in Y and counts as hitting the ground.
	- Horses are unaffected by ladders and vines, and so their change in Y is not reset.
	- Spidersclimbing a block count the block as a "ladder" for this purpose.
- An entity riding another entity does not accumulate any change in Y. However, when the ridden entity takes fall damage it damages all riders for the same change in Y.
- Aminecart's change in Y is reset when landing on rails.
- Boatsdo not accumulate any change in Y while in water deeper than 1 block.
- Teleporting due to a thrownender pearlresets the change in Y, however, the teleportation itself causes 5fall damage to players.
- Eating achorus fruitresets the change in Y.[1]
- Wearing armor that isenchantedwithFeather FallingorProtectionreduces fall damage based on the level of the enchantment.
- Having theJump Booststatus effect reduces the effective change in Y by 1 block per level, e.g. falling 5 blocks with Jump Boost II counts as having fallen only 3.
- Slime blocksnegate all fall damage, but bounce the entity into the air. Both of these facts do not apply to sneaking players. Holding jump when hitting the slime block negates fall damage and stops most of the bounce
- Hay balesandhoney blocksdecrease fall damage to 20% of normal.
- Beds decrease fall damage to 50% of normal and cause the entity to bounce into the air.
- Sweet berry bushesnegate all fall damage.
- Holding sneak while landing on at least a two-block-high stack ofscaffoldingnegates fall damage from any height. Only 1 scaffolding block is needed to negate damage from smaller heights.
- Slow falling status effect completely negates all fall damage but causes the entity to fall slowly.
- Enteringpowder snowwhile falling resets the change in Y.

