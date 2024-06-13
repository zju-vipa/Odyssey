#### Potions with mixed effects
| Icon | Name                                | Duration | Effect                  | Description                                                                                                        |
|------|-------------------------------------|----------|-------------------------|--------------------------------------------------------------------------------------------------------------------|
|      | Potion of the Turtle Master         | 0:20     | Slowness<br/>Resistance | Slows players and mobs by 60%, to about 2.25 blocks per second sprinting, and reduces their damage taken by 60%.   |
|      | Potion of the Turtle Master +<br/>  | 0:40     |                         |                                                                                                                    |
|      | Potion of the Turtle Master II<br/> | 0:20     |                         | Slows players and mobs by 90%, to about 0.5625 blocks per second sprinting, and reduces their damage taken by 80%. |

### Uncraftable potion
In Java Edition, the uncraftable potion is a potion with no effect that is unobtainable in regular gameplay.

It is also available in splash potion and lingering potion forms, as well as for tipped arrows.

It can be obtained using the following command: /give @s minecraft:potion{Potion:"minecraft:empty"}. It is also obtained any time a potion has invalid or missing potion effect tags, and thus serves as a placeholder.

| Icon | Name               | Effect    |
|------|--------------------|-----------|
|      | Uncraftable potion | No effect |

### Joke potions
#### Java Edition 15w14a
| Icon                                                                                                                                                                        | Name                | Duration | Effect  | Description                                                                                    |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|----------|---------|------------------------------------------------------------------------------------------------|
|                                                                                                                                                                             | Potion of Caring    | Instant  | Caring  | Changes the mob AI to move toward the nearest mob as if it were to attack it.                  |
|                                                                                                                                                                             | Potion of Caring    | Instant  | Caring  |                                                                                                |
|                                                                                                                                                                             | Potion of Caring II | Instant  |         |                                                                                                |
| Invicon Potion of Weakness Revision 1.png: Inventory sprite for Potion of Weakness Revision 1 in Minecraft as shown in-game with description: Potion of Weakness Revision 1 | Potion of Sharing   | 1:30     | Sharing | Drops items in a random amount of time, ranging from food to rare items likesaddlesordiamonds. |
|                                                                                                                                                                             | Potion of Sharing + | 4:00     |         |                                                                                                |

#### Java Edition 23w13a_or_b
Big is an effect that makes entities bigger. Big I multiplies the entity size by 1.5 times,[verify] while Big II multiplies it by 2 times. 

Small is an effect that makes entities smaller.

### Undead mobs
The effects given by Potions of Healing and Harming are opposite on undead mobs, which includes skeletons and zombies. Potions of Healing cause harm, and Harming heals them. In addition, undead mobs are not affected by Poison or Regeneration. 

In Bedrock Edition, hitting an undead mob with a Regeneration Potion always registers as Regeneration I, no matter the level of the used potion.

### Mud conversion
Using a water bottle, splash water bottle, or lingering water bottle on dirt, coarse dirt, or rooted dirt converts it into mud, returning a glass bottle with it. This process can be automated with a dispenser. 

### Filling cauldrons with potions
In Bedrock Edition, using a potion bottle on a cauldron empties the potion into it and fills the cauldron by 1⁄3 of its capacity. Using a glass bottle on a cauldron filled with a potion drains it by 1⁄3 and fills the bottle. A single cauldron can store up to three potions of the same type. Different potions cannot be combined in a cauldron, nor can they be mixed with any other substance. Arrows can be also tipped when used on a cauldron containing potion. A single portion of potion can tip 16 arrows at once.

## Custom effects
In Java Edition, potions can also be obtained with any status effect using /give and the tag CustomPotionEffects, which is an array of effects for the potion. See Item format#Potion Effects for more information, and status effect for a list of effects and IDs.

## Data values
### ID
Java Edition:

| Name   | Identifier | Form | Translation key                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|--------|------------|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Potion | `potion`   | Item | `item.minecraft.potion`<br/>`item.minecraft.potion.effect.empty`<br/>`item.minecraft.potion.effect.water`<br/>`item.minecraft.potion.effect.mundane`<br/>`item.minecraft.potion.effect.thick`<br/>`item.minecraft.potion.effect.awkward`<br/>`item.minecraft.potion.effect.night_vision`<br/>`item.minecraft.potion.effect.invisibility`<br/>`item.minecraft.potion.effect.leaping`<br/>`item.minecraft.potion.effect.fire_resistance`<br/>`item.minecraft.potion.effect.swiftness`<br/>`item.minecraft.potion.effect.slowness`<br/>`item.minecraft.potion.effect.water_breathing`<br/>`item.minecraft.potion.effect.healing`<br/>`item.minecraft.potion.effect.harming`<br/>`item.minecraft.potion.effect.poison`<br/>`item.minecraft.potion.effect.regeneration`<br/>`item.minecraft.potion.effect.strength`<br/>`item.minecraft.potion.effect.weakness`<br/>`item.minecraft.potion.effect.levitation`<br/>`item.minecraft.potion.effect.luck`<br/>`item.minecraft.potion.effect.turtle_master`<br/>`item.minecraft.potion.effect.slow_falling`<br/>`item.minecraft.potion.effect.infested`<br/>`item.minecraft.potion.effect.oozing`<br/>`item.minecraft.potion.effect.weaving`<br/>`item.minecraft.potion.effect.wind_charged` |

Bedrock Edition:

| Name   | Identifier | Numeric ID | Form | Translation key                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|--------|------------|------------|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Potion | `potion`   | `426`      | Item | `potion.emptyPotion.name`<br/>`potion.mundane.name`<br/>`potion.mundane.extended.name`<br/>`potion.thick.name`<br/>`potion.awkward.name`<br/>`potion.nightVision.name`<br/>`potion.invisibility.name`<br/>`potion.jump.name`<br/>`potion.fireResistance.name`<br/>`potion.moveSpeed.name`<br/>`potion.moveSlowdown.name`<br/>`potion.heal.name`<br/>`potion.harm.name`<br/>`potion.poison.name`<br/>`potion.regeneration.name`<br/>`potion.damageBoost.name`<br/>`potion.weakness.name`<br/>`potion.wither.name`<br/>`potion.turtleMaster.name`<br/>`potion.slowFalling.name` |

### Metadata
In Bedrock Edition, potions use the following item data values to indicate the kind of potion:

| Potion                      | Regular | Extended | Enhanced(Level II) |
|-----------------------------|---------|----------|--------------------|
| Water Bottle                | 0       | N/A      | N/A                |
| Mundane Potion              | 1       | 2        | N/A                |
| Thick Potion                | 3       | N/A      | N/A                |
| Awkward Potion              | 4       | N/A      | N/A                |
| Potion of Night Vision      | 5       | 6        | N/A                |
| Potion of Invisibility      | 7       | 8        | N/A                |
| Potion of Leaping           | 9       | 10       | 11                 |
| Potion of Fire Resistance   | 12      | 13       | N/A                |
| Potion of Swiftness         | 14      | 15       | 16                 |
| Potion of Slowness          | 17      | 18       | 42                 |
| Potion of Water Breathing   | 19      | 20       | N/A                |
| Potion of Healing           | 21      | N/A      | 22                 |
| Potion of Harming           | 23      | N/A      | 24                 |
| Potion of Poison            | 25      | 26       | 27                 |
| Potion of Regeneration      | 28      | 29       | 30                 |
| Potion of Strength          | 31      | 32       | 33                 |
| Potion of Weakness          | 34      | 35       | N/A                |
| Potion of Decay             | 36      | N/A      | N/A                |
| Potion of the Turtle Master | 37      | 38       | 39                 |
| Potion of Slow Falling      | 40      | 41       | N/A                |



### Item data
#### Java Edition
- tag: The item'stagtag.

- 
	- custom_potion_effects: The custompotion effects(status effects) this potion or tipped arrow has.
		- One of these for each effect.
			- id: Theresource location of the effect.
			- amplifier: The amplifier of the effect, with level I having value 0.  Negative levels are discussedhere. Optional, and defaults to level I.
			- duration: The duration of the effect inticks.  Values 0 or lower are treated as 1.  Optional, and defaults to 1 tick.
			- ambient: 1 or 0 (true/false) - whether or not this is an effect provided by a beacon and therefore should be less intrusive on the screen. Optional, and defaults to false.
			- show_particles: 1 or 0 (true/false) - whether or not this effect produces particles. Optional, and defaults to true.
			- show_icon: 1 or 0 (true/false) - true if effect icon is shown. false if no icon is shown.
	- Potion: Thename of the default potion effect. This name differs from thestatus effectname. For example, the value for an "Instant Health II" potion is "minecraft:strong_healing".  A potion or tipped arrow getting its effects from this tag is named with the proper effect. The default value is "minecraft:empty", which gives it the "Uncraftable" name.
	- CustomPotionColor: The item uses this custom color, and area-of-effect clouds, arrows, and splash and lingering potions use it for their particle effects. This color does not extend, however, to the particles given off by entities who ultimately receive the effect. The numeric color codes are equal to the hex code of the color converted to a decimal number, or can alternatively be calculated from the Red, Green and Blue components using this formula:Red<<16 + Green<<8 + Blue. For positive values larger than 0x00FFFFFF, the top byte is ignored. All negative values produce white.

Normal potions use an NBT "Potion" tag to indicate the potion type. The values of the tag (to be prefixed with minecraft:) are:

| Potion                                         | Regular                   | Level II               | Extended +             |
|------------------------------------------------|---------------------------|------------------------|------------------------|
| Uncraftable potion                             | anything except the below | –                      | –                      |
| Water bottle                                   | `water`                   | –                      | –                      |
| Mundane potion                                 | `mundane`                 | –                      | –                      |
| Thick potion                                   | `thick`                   | –                      | –                      |
| Awkward potion                                 | `awkward`                 | –                      | –                      |
| Night Vision                                   | `night_vision`            | –                      | `long_night_vision`    |
| Invisibility                                   | `invisibility`            | –                      | `long_invisibility`    |
| Leaping                                        | `leaping`                 | `strong_leaping`       | `long_leaping`         |
| Fire Resistance                                | `fire_resistance`         | –                      | `long_fire_resistance` |
| Swiftness                                      | `swiftness`               | `strong_swiftness`     | `long_swiftness`       |
| Slowness                                       | `slowness`                | `strong_slowness`      | `long_slowness`        |
| Water Breathing                                | `water_breathing`         | –                      | `long_water_breathing` |
| Instant Health                                 | `healing`                 | `strong_healing`       | –                      |
| Harming                                        | `harming`                 | `strong_harming`       | –                      |
| Poison                                         | `poison`                  | `strong_poison`        | `long_poison`          |
| Regeneration                                   | `regeneration`            | `strong_regeneration`  | `long_regeneration`    |
| Strength                                       | `strength`                | `strong_strength`      | `long_strength`        |
| Weakness                                       | `weakness`                | –                      | `long_weakness`        |
| Luck                                           | `luck`                    | –                      | –                      |
| The Turtle Master                              | `turtle_master`           | `strong_turtle_master` | `long_turtle_master`   |
| Slow Falling                                   | `slow_falling`            | –                      | `long_slow_falling`    |
| Infestation ‌[upcoming: JE 1.21 & BE 1.21.0]   | `infested`                | –                      | –                      |
| Oozing ‌[upcoming: JE 1.21 & BE 1.21.0]        | `oozing`                  | –                      | –                      |
| Weaving ‌[upcoming: JE 1.21 & BE 1.21.0]       | `weaving`                 | –                      | –                      |
| Wind Charging ‌[upcoming: JE 1.21 & BE 1.21.0] | `wind_charged`            | –                      | –                      |

