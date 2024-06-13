## Data values
### ID
Java Edition:

| Name          | Identifier    | Form | Translation key                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|---------------|---------------|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Splash Potion | splash_potion | Item | item.minecraft.splash_potionitem.minecraft.splash_potion.effect.emptyitem.minecraft.splash_potion.effect.wateritem.minecraft.splash_potion.effect.mundaneitem.minecraft.splash_potion.effect.thickitem.minecraft.splash_potion.effect.awkwarditem.minecraft.splash_potion.effect.night_visionitem.minecraft.splash_potion.effect.invisibilityitem.minecraft.splash_potion.effect.leapingitem.minecraft.splash_potion.effect.fire_resistanceitem.minecraft.splash_potion.effect.swiftnessitem.minecraft.splash_potion.effect.slownessitem.minecraft.splash_potion.effect.water_breathingitem.minecraft.splash_potion.effect.healingitem.minecraft.splash_potion.effect.harmingitem.minecraft.splash_potion.effect.poisonitem.minecraft.splash_potion.effect.regenerationitem.minecraft.splash_potion.effect.strengthitem.minecraft.splash_potion.effect.weaknessitem.minecraft.splash_potion.effect.levitationitem.minecraft.splash_potion.effect.luckitem.minecraft.splash_potion.effect.turtle_masteritem.minecraft.splash_potion.effect.slow_falling |

Bedrock Edition:

| Name          | Identifier    | Numeric ID | Form | Translation key                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|---------------|---------------|------------|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Splash Potion | splash_potion | 561        | Item | potion.emptyPotion.splash.namepotion.mundane.splash.namepotion.mundane.extended.splash.namepotion.thick.splash.namepotion.awkward.splash.namepotion.nightVision.splash.namepotion.invisibility.splash.namepotion.jump.splash.namepotion.fireResistance.splash.namepotion.moveSpeed.splash.namepotion.moveSlowdown.splash.namepotion.heal.splash.namepotion.harm.splash.namepotion.poison.splash.namepotion.regeneration.splash.namepotion.damageBoost.splash.namepotion.weakness.splash.namepotion.wither.splash.namepotion.turtleMaster.splash.namepotion.slowFalling.splash.name |

### Item data

 tag: The item's tag tag.
 custom_potion_effects: The custom potion effects (status effects) this potion or tipped arrow has.
 One of these for each effect.
 id: The resource location of the effect.
 amplifier: The amplifier of the effect, with level I having value 0.  Negative levels are discussed here. Optional, and defaults to level I.
 duration: The duration of the effect in ticks.  Values 0 or lower are treated as 1.  Optional, and defaults to 1 tick.
 ambient: 1 or 0 (true/false) - whether or not this is an effect provided by a beacon and therefore should be less intrusive on the screen. Optional, and defaults to false.
 show_particles: 1 or 0 (true/false) - whether or not this effect produces particles. Optional, and defaults to true.
 show_icon: 1 or 0 (true/false) - true if effect icon is shown. false if no icon is shown.
 Potion: The name of the default potion effect. This name differs from the status effect name. For example, the value for an "Instant Health II" potion is "minecraft:strong_healing".  A potion or tipped arrow getting its effects from this tag is named with the proper effect. The default value is "minecraft:empty", which gives it the "Uncraftable" name.
 CustomPotionColor: The item uses this custom color, and area-of-effect clouds, arrows, and splash and lingering potions use it for their particle effects. This color does not extend, however, to the particles given off by entities who ultimately receive the effect. The numeric color codes are equal to the hex code of the color converted to a decimal number, or can alternatively be calculated from the Red, Green and Blue components using this formula: Red<<16 + Green<<8 + Blue. For positive values larger than 0x00FFFFFF, the top byte is ignored. All negative values produce white.

### Entity

Thrown splash potion




Hitbox size


Height: 0.25 blocksWidth: 0.25 blocks 




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

| Name          | Identifier | Translation key         |
|---------------|------------|-------------------------|
| Splash Potion | potion     | entity.minecraft.potion |

Bedrock Edition:

| Name          | Identifier    | Numeric ID | Translation key           |
|---------------|---------------|------------|---------------------------|
| Splash Potion | splash_potion | 86         | entity.splash_potion.name |

#### Entity data
See also: Chunk format and Potion data values

Splash potions when thrown have entity data that define various properties of the entity.


 Entity data
Tags common to all entities
Tags common to all projectiles
 Item: The item that was thrown. The entity renders as a lingering potion if the id is lingering_potion, otherwise it renders as a splash potion.
Tags common to all potion items

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

## See also
- Glass Bottle
- Lingering Potion
- Bottle o' Enchanting

## Notes

↑ Specifically its lower-north-west corner; the potion entity like most thrown entities is 0.25×0.25×0.25 blocks.



