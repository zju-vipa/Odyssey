# Lingering Potion
Lingering potions are variants of splash potions that can be thrown to leave clouds with status effects that linger on the ground in an area.

## Contents
- 1 Obtaining
	- 1.1 Brewing
- 2 Usage
	- 2.1 Creating area effect clouds
	- 2.2 Lingering water bottle
		- 2.2.1 Mud
	- 2.3 Crafting ingredient
	- 2.4 Filling cauldrons
	- 2.5 Uncraftable lingering potion
- 3 Custom effects
- 4 Sounds
- 5 Data values
	- 5.1 ID
	- 5.2 Item data
	- 5.3 Thrown potion
		- 5.3.1 ID
		- 5.3.2 Entity data
	- 5.4 Area effect cloud
		- 5.4.1 ID
		- 5.4.2 Entity data
- 6 Advancements
- 7 History
- 8 Issues
- 9 Trivia
- 10 Gallery
	- 10.1 Renders
	- 10.2 Screenshots
- 11 See also
- 12 References

## Obtaining
### Brewing
Main article: Brewing
| Ingredients                      | Brewing recipe |
|----------------------------------|----------------|
| Dragon's Breath+AnySplash Potion |                |

## Usage
### Creating area effect clouds
Lingering potions are thrown, like splash potions, by using them. On impact they explode, creating a cloud. The cloud is made of the potion particles corresponding to the potion that was thrown.  

The cloud starts with a radius of 3 blocks, decreasing to 0 over the course of 30 seconds. During the cloud's existence, any player or mob that walks into it after the first second gets the corresponding status effect; this decreases the radius by a 1⁄2 block immediately, reducing the cloud's lifespan by 5 seconds.

For effects with duration, the duration applied by the cloud is 1⁄4 that of the corresponding potion. For effects without duration such as healing or harming, the potency of the effect is 1⁄2 that of the corresponding potion.

The effect may be applied consecutively if the player or mob remains in the cloud. For example, a player throwing the Lingering Potion of Healing II straight down consumes the cloud within a few seconds while being healed 5 times for a total of 20 × 10 health. As far as healing is concerned, this makes the lingering potion much more powerful than the regular or splash potion, provided that the player is away from other mobs or players.

Lingering potions can also be thrown out of dispensers like splash potions.

### Lingering water bottle
Like the splash water bottle, a lingering water bottle puts out fire and damages endermen and blazes by 1. It creates no effect cloud.

#### Mud
Lingering water bottles can be used on dirt, coarse dirt, or rooted dirt to turn it into mud.

### Crafting ingredient
| Name         | Ingredients                    | Crafting recipe           | Description                                                                                                                                                                                                                                    |
|--------------|--------------------------------|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Tipped Arrow | Arrow+MatchingLingering Potion | 8888888888888888888888888 | Arrows of Decay are exclusive toBedrock Editionunless obtained viacommands. Arrows of Luck are exclusive toJava Edition. A custom potion obtained viacommandscannot craft arrows with the potion's custom name, lore, or theCustomPotionColor. |

### Filling cauldrons
In Bedrock Edition, using a lingering potion on a cauldron adds one level of that potion to the cauldron. Attempting to add a lingering potion to a cauldron with water, dyed water or a non-matching potion empties the cauldron and creates an explosion sound (but no actual explosion).

### Uncraftable lingering potion
In Java Edition, the uncraftable potion is a splash potion with no effect that is unobtainable in regular gameplay. It is also available in potion and splash potion forms, as well as for tipped arrows.

It can be obtained using the following command: /give @s minecraft:lingering_potion{Potion:"minecraft:empty"}. It is also obtained any time a potion has invalid or missing potion effect tags, and thus serves as a placeholder.

| Icon | Name                         |
|------|------------------------------|
|      | Uncraftable Lingering Potion |

## Custom effects
In Java Edition, lingering potions can be obtained with any status effect using /give and the tag CustomPotionEffects, which is an array of effects for the potion. See Item format#Potion Effects for more information, and status effect for a list of effects and IDs.

## Data values
### ID
Java Edition:

| Name             | Identifier       | Form | Translation key                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|------------------|------------------|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Lingering Potion | lingering_potion | Item | item.minecraft.lingering_potionitem.minecraft.lingering_potion.effect.emptyitem.minecraft.lingering_potion.effect.wateritem.minecraft.lingering_potion.effect.mundaneitem.minecraft.lingering_potion.effect.thickitem.minecraft.lingering_potion.effect.awkwarditem.minecraft.lingering_potion.effect.night_visionitem.minecraft.lingering_potion.effect.invisibilityitem.minecraft.lingering_potion.effect.leapingitem.minecraft.lingering_potion.effect.fire_resistanceitem.minecraft.lingering_potion.effect.swiftnessitem.minecraft.lingering_potion.effect.slownessitem.minecraft.lingering_potion.effect.water_breathingitem.minecraft.lingering_potion.effect.healingitem.minecraft.lingering_potion.effect.harmingitem.minecraft.lingering_potion.effect.poisonitem.minecraft.lingering_potion.effect.regenerationitem.minecraft.lingering_potion.effect.strengthitem.minecraft.lingering_potion.effect.weaknessitem.minecraft.lingering_potion.effect.levitationitem.minecraft.lingering_potion.effect.luckitem.minecraft.lingering_potion.effect.turtle_masteritem.minecraft.lingering_potion.effect.slow_falling |

Bedrock Edition:

| Name             | Identifier       | Numeric ID | Form | Translation key                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|------------------|------------------|------------|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Lingering Potion | lingering_potion | 562        | Item | potion.emptyPotion.linger.namepotion.mundane.linger.namepotion.mundane.extended.linger.namepotion.thick.linger.namepotion.awkward.linger.namepotion.nightVision.linger.namepotion.invisibility.linger.namepotion.jump.linger.namepotion.fireResistance.linger.namepotion.moveSpeed.linger.namepotion.moveSlowdown.linger.namepotion.heal.linger.namepotion.harm.linger.namepotion.poison.linger.namepotion.regeneration.linger.namepotion.damageBoost.linger.namepotion.weakness.linger.namepotion.wither.linger.namepotion.turtleMaster.linger.namepotion.slowFalling.linger.name |

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

### Thrown potion

Thrown lingering potion




Hitbox size


Height: 0.25 blocksWidth: 0.25 blocks 




{
    "title": "Thrown lingering potion",
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

| Name             | Identifier | Translation key         |
|------------------|------------|-------------------------|
| Lingering Potion | potion     | entity.minecraft.potion |

Bedrock Edition:

| Name             | Identifier       | Numeric ID | Translation key              |
|------------------|------------------|------------|------------------------------|
| Lingering Potion | lingering_potion | 101        | entity.lingering_potion.name |

#### Entity data
See also: Chunk format and Potion data values

Lingering potions when thrown have entity data that define various properties of the entity.


 Entity data
Tags common to all entities
Tags common to all projectiles
 Item: The item that was thrown. The entity renders as a lingering potion if the id is lingering_potion, otherwise it renders as a splash potion.
Tags common to all potion items

### Area effect cloud

Area Effect Cloud




Hitbox size


Height: 0.5 blocksWidth: Varies 




{
    "title": "Area Effect Cloud",
    "rows": [
        {
            "field": "Height: 0.5 blocks<br>Width: Varies",
            "label": "(link to Hitbox article, displayed as Hitbox size)"
        }
    ],
    "invimages": [],
    "images": [
        "Area Effect Cloud.png"
    ]
}
#### ID
Java Edition:

| Name              | Identifier        | Translation key                    |
|-------------------|-------------------|------------------------------------|
| Area Effect Cloud | area_effect_cloud | entity.minecraft.area_effect_cloud |

Bedrock Edition:

| Name              | Identifier        | Numeric ID | Translation key               |
|-------------------|-------------------|------------|-------------------------------|
| Area Effect Cloud | area_effect_cloud | 95         | entity.area_effect_cloud.name |

#### Entity data
See also: Chunk format

The cloud that is created when: lingering potions are thrown; creepers with potion effects explode; dragon fireballs hit the ground, is an entity, which has entity data that defines the properties of the entity.


 Entity data
Tags common to all entities
 Age: Age of the field. Increases by 1 every tick. When this is bigger than Duration + WaitTime the area effect cloud dissipates.
 Color: The color of the displayed particle. Uses the same format as the color tag from Display Properties.
 Duration: The maximum age of the field after WaitTime.
 DurationOnUse: The amount the duration of the field changes upon applying the effect.
 Effects: A list of the applied effects.
 An individual effect.
 Ambient: 1 or 0 (true/false) - whether or not this is an effect provided by a beacon and therefore should be less intrusive on the screen. Optional, and defaults to false. Due to a bug, it has no effect on splash potions.
 Amplifier: The amplifier of the effect, with level I having value 0.  Negative levels are discussed here. Optional, and defaults to level I.
 Duration: The duration of the effect in ticks.  Values 0 or lower are treated as 1.  Optional, and defaults to 1 tick.
 Id: The numeric ID of the effect.
 ShowIcon: 1 or 0 (true/false) - true if effect icon is shown. false if no icon is shown.
 ShowParticles: 1 or 0 (true/false) - whether or not this effect produces particles. Optional, and defaults to true. Due to a bug, it has no effect on splash potions.
 Owner: The UUID of the entity who created the cloud, stored as four ints.
 Particle: The particle displayed by the field. This is the exact same as used in the /particle command, including additional parameters used for particles, for example dust 1 0 0 1.
 Potion: The name of the default potion effect. See potion data values for valid IDs.
 Radius: The field's radius.
 RadiusOnUse: The amount the radius changes upon applying the effect. Normally negative.
 RadiusPerTick: The amount the radius changes per tick. Normally negative.
 ReapplicationDelay: The number of ticks before reapplying the effect.
 WaitTime: The time before deploying the field. The Radius is ignored, meaning that any specified effects is not applied and specified particles appear only at the center of the field, until Age hits this number.

## See also
- Glass Bottle
- Potion
- Splash Potion

