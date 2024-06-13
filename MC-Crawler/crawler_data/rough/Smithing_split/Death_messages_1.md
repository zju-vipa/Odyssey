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


