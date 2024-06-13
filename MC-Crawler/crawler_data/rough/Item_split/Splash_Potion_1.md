## Data values
### ID
Java Edition:

| Name          | Identifier      | Form | Translation key                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|---------------|-----------------|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Splash Potion | `splash_potion` | Item | `item.minecraft.splash_potion`<br/>`item.minecraft.splash_potion.effect.empty`<br/>`item.minecraft.splash_potion.effect.water`<br/>`item.minecraft.splash_potion.effect.mundane`<br/>`item.minecraft.splash_potion.effect.thick`<br/>`item.minecraft.splash_potion.effect.awkward`<br/>`item.minecraft.splash_potion.effect.night_vision`<br/>`item.minecraft.splash_potion.effect.invisibility`<br/>`item.minecraft.splash_potion.effect.leaping`<br/>`item.minecraft.splash_potion.effect.fire_resistance`<br/>`item.minecraft.splash_potion.effect.swiftness`<br/>`item.minecraft.splash_potion.effect.slowness`<br/>`item.minecraft.splash_potion.effect.water_breathing`<br/>`item.minecraft.splash_potion.effect.healing`<br/>`item.minecraft.splash_potion.effect.harming`<br/>`item.minecraft.splash_potion.effect.poison`<br/>`item.minecraft.splash_potion.effect.regeneration`<br/>`item.minecraft.splash_potion.effect.strength`<br/>`item.minecraft.splash_potion.effect.weakness`<br/>`item.minecraft.splash_potion.effect.levitation`<br/>`item.minecraft.splash_potion.effect.luck`<br/>`item.minecraft.splash_potion.effect.turtle_master`<br/>`item.minecraft.splash_potion.effect.slow_falling` |

Bedrock Edition:

| Name          | Identifier      | Numeric ID | Form | Translation key                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|---------------|-----------------|------------|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Splash Potion | `splash_potion` | `561`      | Item | `potion.emptyPotion.splash.name`<br/>`potion.mundane.splash.name`<br/>`potion.mundane.extended.splash.name`<br/>`potion.thick.splash.name`<br/>`potion.awkward.splash.name`<br/>`potion.nightVision.splash.name`<br/>`potion.invisibility.splash.name`<br/>`potion.jump.splash.name`<br/>`potion.fireResistance.splash.name`<br/>`potion.moveSpeed.splash.name`<br/>`potion.moveSlowdown.splash.name`<br/>`potion.heal.splash.name`<br/>`potion.harm.splash.name`<br/>`potion.poison.splash.name`<br/>`potion.regeneration.splash.name`<br/>`potion.damageBoost.splash.name`<br/>`potion.weakness.splash.name`<br/>`potion.wither.splash.name`<br/>`potion.turtleMaster.splash.name`<br/>`potion.slowFalling.splash.name` |

### Item data
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

### Entity
| Hitbox size | Height: 0.25 blocksWidth: 0.25 blocks |
|-------------|---------------------------------------|

{
    "title": "Thrown splash potion",
    "rows": [
        {
            "field": "Height: 0.25 blocks<br>Width: 0.25 blocks",
            "label": "(link to Hitbox article, displayed as Hitbox size)"
        }
    ],
    "invimages": [],
    "images": []
}
#### ID
Java Edition:

| Name          | Identifier | Translation key           |
|---------------|------------|---------------------------|
| Splash Potion | `potion`   | `entity.minecraft.potion` |

Bedrock Edition:

| Name          | Identifier      | Numeric ID | Translation key             |
|---------------|-----------------|------------|-----------------------------|
| Splash Potion | `splash_potion` | `86`       | `entity.splash_potion.name` |

#### Entity data
See also: Chunk format and Potion data values

Splash potions when thrown have entity data that define various properties of the entity.

- Entity data
	- 
	- Tags common to all entities
	- 
	- Tags common to all projectiles
	- Item: The item that was thrown. The entity renders as a lingering potion if the id islingering_potion, otherwise it renders as a splash potion.
		- 
		- Tags common to all potion items

## Unused splash potions
Bedrock Edition has unused splash potion textures for several effects, along with their normal variants. These effects are: Absorption, Blindness, Haste, Health Boost, Hunger, Mining Fatigue, Nausea, Resistance, Saturation, and Levitation, as well as the Luck potion textures also present in Java Edition. These unused textures were added along with the other potion textures in Pocket Edition v0.12.1 alpha, except for the potion of Levitation, which was added in Pocket Edition 1.0.0. The textures were changed along with the other potion textures during the texture update in Bedrock Edition 1.10.0.

- Splash Potion of Absorption
- Splash Potion of Blindness
- Splash Potion of Haste
- Splash Potion of Health Boost
- Splash Potion of Hunger
- Splash Potion of Mining Fatigue
- Splash Potion of Nausea
- Splash Potion of Resistance
- Splash Potion of Saturation
- Splash Potion of Levitation

## Notes
1. ↑Specifically its lower-north-west corner; the potion entity like most thrown entities is 0.25×0.25×0.25 blocks.


