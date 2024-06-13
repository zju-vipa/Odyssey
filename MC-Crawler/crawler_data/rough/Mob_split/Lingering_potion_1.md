### Thrown potion
| Hitbox size | Height: 0.25 blocksWidth: 0.25 blocks |
|-------------|---------------------------------------|

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

| Name             | Identifier | Translation key           |
|------------------|------------|---------------------------|
| Lingering Potion | `potion`   | `entity.minecraft.potion` |

Bedrock Edition:

| Name             | Identifier         | Numeric ID | Translation key                |
|------------------|--------------------|------------|--------------------------------|
| Lingering Potion | `lingering_potion` | `101`      | `entity.lingering_potion.name` |

#### Entity data
See also: Chunk format and Potion data values

Lingering potions when thrown have entity data that define various properties of the entity.

- Entity data
	- 
	- Tags common to all entities
	- 
	- Tags common to all projectiles
	- Item: The item that was thrown. The entity renders as a lingering potion if the id islingering_potion, otherwise it renders as a splash potion.
		- 
		- Tags common to all potion items

### Area effect cloud
| Hitbox size | Height: 0.5 blocksWidth: Varies |
|-------------|---------------------------------|

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

| Name              | Identifier          | Translation key                      |
|-------------------|---------------------|--------------------------------------|
| Area Effect Cloud | `area_effect_cloud` | `entity.minecraft.area_effect_cloud` |

Bedrock Edition:

| Name              | Identifier          | Numeric ID | Translation key                 |
|-------------------|---------------------|------------|---------------------------------|
| Area Effect Cloud | `area_effect_cloud` | `95`       | `entity.area_effect_cloud.name` |

#### Entity data
See also: Chunk format

The cloud that is created when: lingering potions are thrown; creepers with potion effects explode; dragon fireballs hit the ground, is an entity, which has entity data that defines the properties of the entity.

- Entity data
	- 
	- Tags common to all entities
	- Age: Age of the field. Increases by 1 every tick. When this is bigger thanDuration+WaitTimethe area effect cloud dissipates.
	- Color: The color of the displayed particle. Uses the same format as thecolortag fromDisplay Properties.
	- Duration: The maximum age of the field afterWaitTime.
	- DurationOnUse: The amount the duration of the field changes upon applying the effect.
	- Effects: A list of the appliedeffects.
		- An individual effect.
			- Ambient: 1 or 0 (true/false) - whether or not this is an effect provided by a beacon and therefore should be less intrusive on the screen. Optional, and defaults to false. Due to a bug, it has no effect on splash potions.
			- Amplifier: The amplifier of the effect, with level I having value 0.  Negative levels are discussedhere. Optional, and defaults to level I.
			- Duration: The duration of the effect inticks.  Values 0 or lower are treated as 1.  Optional, and defaults to 1 tick.
			- Id: Thenumeric ID of the effect.
			- ShowIcon: 1 or 0 (true/false) - true if effect icon is shown. false if no icon is shown.
			- ShowParticles: 1 or 0 (true/false) - whether or not this effect produces particles. Optional, and defaults to true. Due to a bug, it has no effect on splash potions.
	- Owner: TheUUIDof the entity who created the cloud, stored as four ints.
	- Particle: Theparticledisplayed by the field. This is the exact same as used in the/particlecommand, including additional parameters used for particles, for exampledust 1 0 0 1.
	- Potion: The name of the default potion effect. Seepotion data valuesfor valid IDs.
	- Radius: The field's radius.
	- RadiusOnUse: The amount the radius changes upon applying the effect. Normally negative.
	- RadiusPerTick: The amount the radius changes per tick. Normally negative.
	- ReapplicationDelay: The number of ticks before reapplying the effect.
	- WaitTime: The time before deploying the field. TheRadiusis ignored, meaning that any specified effects is not applied and specified particles appear only at the center of the field, untilAgehits this number.


