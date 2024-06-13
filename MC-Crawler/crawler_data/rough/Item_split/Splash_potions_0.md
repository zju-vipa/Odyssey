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

