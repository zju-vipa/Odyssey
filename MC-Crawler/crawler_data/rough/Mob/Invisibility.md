# Invisibility
Invisibility is a status effect that turns entities invisible.

## Contents
- 1 Effect
	- 1.1 Invisibility
	- 1.2 Mob detection radius
- 2 Immune mobs
- 3 Causes
- 4 Brewing
- 5 Notes
- 6 Data values
	- 6.1 ID
- 7 Advancements
- 8 History
- 9 Issues

## Effect
The visible parts of a decorated llama, an enderman, a saddled pig, a shulker, a charged creeper, and a spider.
The visible parts of an armored player.
### Invisibility
Invisibility causes the affected mob or player's model to disappear from the world. The effect does not, however, affect the player or mob's ability to interact with the world.

Certain features of entities are not affected by Invisibility:

- Armor(includinghorse armor)
- Helditems
- Entities set onfire
- Arrowsstuck inplayers‌[Java Edition  only]
- Particlesbeing emitted
- Ashulkerhead
- Allama'scarpetdecoration
- Asaddleif equipped on apigorstriderfor riding (saddles on other mobs are invisible)
- The aura of acharged creeper
- The eyes ofcave spiders,spiders,endermenandphantoms

### Mob detection radius
Mobs do not attack or sense the player until the player is a lot closer than normal.

- A player with noarmorcan be detected at 7% of the usual detection distance.
- Each piece of armor increases this by another 17.5% of the usual distance. Full armor thus results in a 70% detection range.
- After detecting the player, a mob continues to follow as if the player is visible.

The following methods of reducing mob detection can stack with Invisibility:

- Sneakingreduces the detection range to 80% of the usual.
- Wearing the correspondingmob headreduces the detection range ofskeletons,zombies,creepers, andpiglinsto 50% of usual, although mob head does count as an armor piece. Wearing a mob head with Invisibility effect results in a larger detection range compared to having just the effect.

## Immune mobs
Withers and ender dragons are immune to Invisibility.

## Causes
| Cause                                      | Potency | Length                              | Notes                                                                                                                           |
|--------------------------------------------|---------|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| Potion of Invisibility                     | I       | 3:00                                | Wandering Traders drink this potion when attacked by hostile mobs or when avoiding zombies andillagers.‌[Bedrock Edition  only] |
| Potion of Invisibility(extended)           | I       | 8:00                                | Wandering Traders drink this potion if the time is between 12000 and 18000.                                                     |
| Splash Potion of Invisibility              | I       | 3:00‌[JE  only]<br/>2:15‌[BE  only] |                                                                                                                                 |
| Splash Potion of Invisibility(extended)    | I       | 8:00‌[JE  only]<br/>6:00‌[BE  only] |                                                                                                                                 |
| Lingering Potion of Invisibility           | I       | 0:45                                |                                                                                                                                 |
| Lingering Potion of Invisibility(extended) | I       | 2:00                                |                                                                                                                                 |
| Arrow of Invisibility                      | I       | 0:22                                |                                                                                                                                 |
| Arrow of Invisibility(extended)            | I       | 1:00                                |                                                                                                                                 |
| Illusioner                                 | I       | 1:00                                | Applies only toillusioners when casting the invisibility spell.                                                                 |
| Spawning within the world                  | I       | ∞                                   | Applies only tospiders on Hard difficulty.‌[JE  only]                                                                           |

## Brewing
| Potion                      | Reagent, Base | Extended                               | Enhanced | Effects                                                                   |
|-----------------------------|---------------|----------------------------------------|----------|---------------------------------------------------------------------------|
| <br/>Potion of Invisibility |               | <br/>Potion of Invisibility (extended) | -        | Invisibility<br/>Grants invisibility (except for equipped or held items). |

## Notes
- Catsbehave as though the entity affected is visible.
- Players inSpectatormode see invisibleentitiesas translucent instead.
- Endermenhave a reduced provocation range if the player looking at them is invisible.
- Pillagerspoint their crossbows and look at invisible players instead of shooting them.
- Invisibility also prevents the rendering of entity hitboxes‌[JE  only]by pressingF3+B.
- Sculk sensorsandwardenscan still detect a player with Invisibility.
- The attack indicator‌[JE  only]still appears when facing an invisible entity.[1]

## Data values
### ID
This section is about the effect IDs.  For the IDs on potions, see Potion § Item data.  For for the IDs on tipped arrows, see Arrow § Metadata.
Java Edition:

| Name         | Identifier     | Numeric ID | Translation key                 |
|--------------|----------------|------------|---------------------------------|
| Invisibility | `invisibility` | `14`       | `effect.minecraft.invisibility` |

Bedrock Edition:

| Name         | Identifier     | Numeric ID | Translation key       |
|--------------|----------------|------------|-----------------------|
| Invisibility | `invisibility` | `14`       | `potion.invisibility` |

