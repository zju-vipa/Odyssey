# Splash Potion
Splash potions are a variant of potions that can be thrown.

## Contents
- 1 Obtaining
	- 1.1 Natural generation
	- 1.2 Brewing
	- 1.3 Bartering
	- 1.4 Filling bottles
- 2 Usage
	- 2.1 Brewing
	- 2.2 Using
	- 2.3 Splash water bottles
		- 2.3.1 Mud
	- 2.4 Filling cauldrons
	- 2.5 Uncraftable splash potion
- 3 Custom effects
- 4 Sounds
- 5 Data values
	- 5.1 ID
	- 5.2 Item data
	- 5.3 Entity
		- 5.3.1 ID
		- 5.3.2 Entity data
- 6 Achievements
- 7 Advancements
- 8 Video
- 9 History
- 10 Issues
- 11 Trivia
- 12 Unused splash potions
- 13 Gallery
	- 13.1 Renders
	- 13.2 Screenshots
- 14 See also
- 15 Notes
- 16 References
- 17 External links

## Obtaining
### Natural generation
One splash potion of Weakness can be found in a brewing stand inside an igloo basement.

### Brewing
Main article: Brewing
| Ingredients              | Brewing recipe |
|--------------------------|----------------|
| Gunpowder+<br/>AnyPotion |                |

Splash potions are brewed by adding gunpowder to a normal potion, including uncraftable potions of luck‌[JE  only] and decay‌[BE  only].

### Bartering
Piglins have a 1.74% chance of bartering a splash potion of Fire Resistance when given a gold ingot.



### Filling bottles
Using a glass bottle on a cauldron that contains splash potion turns it into a bottle of that splash potion, this also removes 1⁄3 of the cauldron's content.‌[Bedrock Edition  only]

## Usage
### Brewing
| Ingredients                            | Brewing recipe |
|----------------------------------------|----------------|
| Dragon's breath+<br/>any splash potion |                |

Lingering potions are brewed by adding dragon's breath to a splash potion.

### Using
Splash potions are thrown by using them. On impact they explode, applying status effects to nearby entities. When thrown by the player, they have a range of 8 blocks if thrown at the best angle. The bottle is lost, unlike drinkable potions. Entities within an 8.25×8.25×4.25 cuboid centered on the thrown potion at impact and within 4 blocks euclidean distance of the thrown potion[n 1] at impact are affected.

In Bedrock Edition, splash potions' effects have only three-fourths of the duration of the drinkable form. In Java Edition, splash and drinkable forms have the same duration.

If the potion directly collides with an entity, the entity gets the full duration and potency of the effect. Otherwise, the farther away the entity is from the center of the impact, the lesser the imbued effect. For instant effects (i.e. Healing or Harming), the potency of the effect reduces linearly from 100% on a direct hit to 0% at 4 blocks' distance. For other effects, the potency is unchanged, but the duration decreases linearly on the same scale (rounded to the nearest 1⁄20 second), with no effect being applied if the duration would be 1 second or less.

### Splash water bottles
Splash water bottles have no effect on almost all entities, but they extinguish fire in the block hit and the four blocks horizontally surrounding it.

A splash water bottle deals 1 damage to endermen, striders, snow golems, and blazes; however, endermen have a chance of teleporting away if hit with one.

Splash water bottles can extinguish a burning entity.

#### Mud
Splash water bottles can be used on dirt, coarse dirt, or rooted dirt to turn it into mud.

### Filling cauldrons
In Bedrock Edition, using a splash potion on a cauldron adds one level of that potion to the cauldron. Attempting to add a splash potion to a cauldron with water, dyed water or a non-matching potion empties the cauldron and creates an explosion sound (but no actual explosion).

### Uncraftable splash potion
In Java Edition, the uncraftable potion is a splash potion with no effect that is unobtainable in regular gameplay. It is also available in potion and lingering potion forms, as well as for tipped arrows.

It can be obtained in two distinct (though functionally identical) variants, using the following commands: /give @s minecraft:splash_potion{Potion:"minecraft:empty"} or /give @s minecraft:splash_potion. It is also obtained any time a potion has invalid or missing potion effect tags, and thus serves as a placeholder.

| Icon | Name                      |
|------|---------------------------|
|      | Uncraftable splash potion |

## Custom effects
In Java Edition, splash potions can be obtained with any status effect using /give and the tag CustomPotionEffects, which is an array of effects for the potion. See Item format#Potion Effects for more information, and status effect for a list of effects and IDs.

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

