# Durability
Durability is a property that affects tools, weapons, and armor. It represents the number of useful actions an item can perform and depletes upon item use. The bar starts at green, but as the durability decreases, the color gradually turns to yellow, then orange, and finally red. When the durability is empty, the item is about to become destroyed. Durability may be increased by combining two damaged items in the crafting grid or a grindstone, repairing them with materials in an anvil, or through the Mending enchantment.

## Contents
- 1 Interface
- 2 Armor durability
- 3 Tool & weapon durability
- 4 Sounds
- 5 History
- 6 See also
- 7 References

## Interface
"Unbreakable" redirects here.  For the enchantment that gives a chance for an item to avoid durability reduction when it is used, see Unbreaking.
The remaining durability of any item can be seen by looking at the item's durability bar on the bottom of the item icon in the inventory and action bar. Unused items do not display a durability bar. As the item's durability decreases, the bar's colored area shortens right to left, changing color from green to red and leaving an empty gray part. When the item has a small number of uses left, the durability bar is represented as empty, due to rounding to the nearest pixel 1-down, until the tool or armor is destroyed.

In Java Edition, the numeric durability of the player's items can be displayed in-game by pressing F3+H. This enables additional information in the tooltips for items in the player's inventory.

A weapon, tool or piece of armor picked up by a mob does not decrease in durability;[1] it remains the same as when the item was first picked up by the mob. However, a helmet worn by an undead mob in sunlight loses durability due to the helmet absorbing the mob's damage from burning.[2] In Java Edition, a crossbow wielded by a pillager or a piglin also loses durability and eventually breaks;[3] this is not the case in Bedrock Edition.[4]

Items with the Unbreakable tag do not deplete their durability or break when used. Their durability is not shown, even with advanced tooltips enabled, though it is retained in the NBT data. Such an item can be acquired using /give @s <item_name>{Unbreakable:1b}.‌[Java Edition  only]

Most items have the same durability in Java Edition as they do in Bedrock Edition, but due to a bug [5], items can be used one extra time in Bedrock Edition.

## Armor durability
Armor durability is based on the armor's type (head, torso, legs, feet) and material (leather, gold, chain mail, iron, diamond, and netherite). Any time the player takes damage that can be reduced by armor, each piece of armor they are wearing loses 1 durability for every 4 of incoming damage (rounded down, but never below 1). 

Armor can reduce damage from the following sources:

- Direct attacks frommobsand otherplayers
	- This includes Strength and Weakness status effects or extra damage from enchantments.
- Getting hit with anarrow,shulker bullet, throwntrident,egg,snowball,llama spit,fireball, orwither skull
	- This includes extra damage from enchantments.
- Getting hit with aneggorsnowball
- Laser beam from aguardianorelder guardian
- Damage fromThornsenchantment (as well asguardian's spikes)
- Getting struck bylightning
- Getting hit by a fallinganvilorstalactite
- Touching a block offire,lava,magma block(does not damage netherite armor)
- Touching acactus, or moving insidesweet berry bush
- Explosions(includingfireworks, but deals more than one point of durability)
- Getting hit by or falling into apointed dripstone(excludes fall damage which ignores armor)

The following types of damage are not reduced by ordinary armor and have no effect on the armor's durability, but some enchantments protect against them:

- Ongoing damage from being onfire
- Suffocatinginside ablockor due to entity cramming (also includes theworld border)
- Drowninginwater(partially for turtle shells)
- Fall damage(includingender pearls)
- Colliding a block withelytra
- Magic (evoker fangs,dragon's breath,Poison,WitherandInstant Damagestatus effects)
- Being inside of apowder snowblock (except entities wearing leather armor, which prevents freezing damage)

The following types of damage are not reduced by ordinary armor, even with enchantments such as Protection:

- Falling into thevoidor/kill
- Starvation
- Warden's ranged sonic attacks

Values in the table below represent the number of points of durability damage this armor can take before it is destroyed.

Note that every time the player takes damage that armor is capable of reducing (see above), it counts as one point of durability damage for every worn armor piece. 

| Material     | Helmet | Chestplate | Leggings | Boots |
|--------------|--------|------------|----------|-------|
| Turtle shell | 275    | N/A        | N/A      | N/A   |
| Leather      | 55     | 80         | 75       | 65    |
| Golden       | 77     | 112        | 105      | 91    |
| Chainmail    | 165    | 240        | 225      | 195   |
| Iron         | 165    | 240        | 225      | 195   |
| Diamond      | 363    | 528        | 495      | 429   |
| Netherite    | 407    | 592        | 555      | 481   |

## 
Some tools are not block-breaking tools: this includes fishing rods, carrots on sticks, flint and steel, warped fungi on sticks, brushes, and elytra. Such tools are no better than bare fists at breaking blocks, but they do not take damage from doing so—they take damage by being used in their own various manners.

For block-breaking tools, a use is counted if a player completely breaks apart one block or hits a mob. If a block is partially broken, this is not counted as a full use. Additional uses can be counted with specific actions performed by the item (e.g. paving dirt by a shovel).

Weapons with durability take damage from attacks: either a melee hit (sword, trident) or a shot/throw (bow, crossbow and trident).

Items with an Unbreaking enchantment do not always lose durability when used; for a given enchantment level, the chance of losing durability is 1 in (1+level). Such items last on average an extra level times their original durability.

Some blocks, such as short grass and crops, break instantly with any tool or an empty hand. This is distinct from blocks which do not naturally break instantly being broken by a tool with high speed. For more information, see Breaking § Instant breaking and Breaking § Blocks by hardness.

Axes, pickaxes, and shovels:

- Breaking a block that naturally breaks instantly counts as0uses.
- Breaking other blocks counts as1use.
- Paving dirt-like block using a shovel to make adirt pathcounts as1use.
- Using an axe on alogorwoodtostripit counts as1use.
- Using an axe oncopper-related blocks, if they are waxed or oxidized, counts as1use.
- Hitting a mob (hostile, neutral or passive) counts as2uses.

Hoes:

- Breaking a block that naturally breaks instantly counts as0uses.
- Breaking other blocks counts as1use.
- Tilling dirt or grass counts as1use.
- Hitting a mob counts as1use.

Shears:

- Hitting a mob counts as0uses.
- Shearing a shearable mob counts as1use.
- Shearing abee nestorbeehivecounts as1use.
- Shearing the tip ofcave vines,kelp,weeping vinesortwisting vinescounts as1use (‌[Java Edition  only]).
- Breaking any block counts as1use.

Swords:

- Breaking a block that naturally breaks instantly counts as0uses.
- Hitting a mob counts as1use.
- Breaking other blocks counts as2uses.

Fishing rods:

- Breaking a block or hitting a mob counts as0uses.
- Casting the line and reeling it in empty counts as0uses.
- Reeling in an item counts as1use.
- Catching the bobber/hook on a block, then reeling it in, counts as2uses.
- Using the line to yank on an item counts as3uses.
- Using the line to yank on a mob counts as5uses.

Carrot on a stick:

- Breaking a block or hitting a mob counts as0uses.
- Using the boost counts as7uses inJava Editionor2uses inBedrock Edition.

Warped fungus on a stick:

- Breaking a block or hitting a mob counts as0uses.
- Using the boost counts as1use.

Flint and steel:

- Breaking a block or hitting a mob counts as0uses.
- Using it to set a block on fire or light a nether portal counts as1use.

Bows:

- Breaking a block or hitting a mob counts as0uses.
- Firing an arrow counts as1use.

Tridents:

- Breaking a block that naturally breaks instantly counts as0uses.
- Attacking a mob or throwing counts as1use.
- Breaking other blocks counts as2uses.

Elytra:

- Flying for one second counts as1use. The durability cannot go below1.

Shields:

- When the shield blocks an attack, it takes damage equal to the strength of the attack (rounded down) plus 1. Note: when the shield blocks an attack of 3or stronger, it takes durability damage equal to the strength of the attack rounded up.

Crossbows:

- Shooting an arrow counts as1use.
- Shooting three arrows (when enchanted withMultishot) counts as3uses.
- Shooting a firework rocket counts as3uses.
- Shooting three firework rockets (when enchanted with multishot) counts as 3×3 =9uses.

Sparklers and glow sticks‌[Bedrock Edition and Minecraft Education  only]:

- Durability gradually decreases while the item is active and held in hand.
- If the player has a lit sparkler in their inventory and goes into the water, the sparkler is destroyed immediately regardless of durability.

Brushes:

- Breaking a block or hitting a mob counts as0uses.
- Brushingsuspicious sandorsuspicious gravelcounts as1use.
- Brushing anarmadillo scuteoff anarmadillocounts as16uses.

Using a tool properly maximizes its durability. Assuming a player uses a tool appropriately, the following list shows the maximum durability for tools of each material type.

** Materials **
- Gold: 32 uses
- Wood: 59 uses
- Stone: 131 uses
- Iron: 250 uses
- Diamond: 1561 uses
- Netherite: 2031 uses

** Specific tools and weapons **
- Flint and steel: 64 uses
- Brush: 64 uses
- Fishing rod: 64 uses ‌[Java Edition  only]or 384 uses ‌[Bedrock Edition  only]
- Carrot on a stick: 25 uses
- Warped fungus on a stick: 100 uses
- Shears: 238 uses
- Shield: 336 uses
- Bow: 384 uses
- Trident: 250 uses
- Elytra: 432 uses
- Crossbow: 465 uses
- Sparkler‌[Bedrock Edition and Minecraft Education  only]: 100 uses
- Glow stick‌[Bedrock Edition and Minecraft Education  only]: 100 uses


