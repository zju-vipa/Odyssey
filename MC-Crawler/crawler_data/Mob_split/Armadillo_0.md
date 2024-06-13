# Armadillo
An armadillo is a passive mob found in badlands and savannas. It rolls up in response to being hurt or being near undead mobs or players that are sprinting or mounted. While in this state, it takes less damage. It also repels spiders and cave spiders away from it. It is the only source of armadillo scutes, which the armadillo sheds over time, as well as when it is brushed.

## Contents
- 1 Spawning
- 2 Drops
	- 2.1 Breeding
	- 2.2 On death
	- 2.3 Brushing
- 3 Behavior
	- 3.1 Breeding
- 4 Sounds
- 5 Data values
	- 5.1 ID
	- 5.2 Entity data
- 6 Achievements
- 7 Advancements
- 8 Video
- 9 History
- 10 Issues
- 11 Trivia
- 12 Gallery
	- 12.1 Renders
		- 12.1.1 Before 24w03a/1.20.70.20
	- 12.2 Screenshots
	- 12.3 Development images
	- 12.4 Concept artwork
	- 12.5 In other media
		- 12.5.1 Mob vote artwork
- 13 External links
- 14 References

## Spawning
Armadillos spawn in groups of two to three in savannas, savanna plateaus, and windswept savannas and groups of one to two in badlands, eroded badlands, and wooded badlands.

## Drops
Armadillos drop 1 armadillo scute every 5–10 minutes, similar to the rate at which chickens lay eggs.

### Breeding
Upon successful breeding, 1–7 is dropped.

### On death
- 1–3experienceorbs if killed by a player or tamedwolf.

Killing an armadillo pup yields no items nor experience.

### Brushing
If a player or dispenser uses a brush on an armadillo, it drops:

- 1Armadillo Scute

An unenchanted brush has enough durability to obtain 4‌[JE  only] / 5‌[BE  only] armadillo scutes.

## Behavior
An armadillo can become startled and hide in its shell when it is hurt or when confronted by undead, players who are sprinting, players on a mount, or players in a vehicle. When an armadillo is rolled up it does not walk, cannot eat, and is not tempted by food. While rolled up, it takes a reduced amount of damage given by basedamage−12. The armadillo then continues to scan for threats in the area, occasionally "peeking out" of its shell to see if the threat is still near. If there are no threats detected for 3 seconds(60 ticks), it unrolls. It also instantly unrolls if it comes into contact with water or is attached to a lead. An armadillo does not roll up while fleeing, in water, in the air, or being led.

The distance an armadillo checks for threats is the size of the hitbox inflated by 7 blocks on the X and Z axes and 2 blocks on the Y axis.

Spiders and cave spiders run away from armadillos.

### Breeding
Armadillos follow players holding spider eyes within 10‌[JE  only] / 16‌[BE  only] blocks.

A player can breed armadillos by using spider eyes on two of them. Baby armadillos take 20 minutes to grow up into adults. Feeding a spider eye once can reduce growth time by 10%.

## Data values
### ID
Java Edition:

| Name      | Identifier | Translation key            |
|-----------|------------|----------------------------|
| Armadillo | armadillo  | entity.minecraft.armadillo |

Bedrock Edition:

| Name      | Identifier | Numeric ID | Translation key       |
|-----------|------------|------------|-----------------------|
| Armadillo | armadillo  | 142        | entity.armadillo.name |

### Entity data
Armadillos have entity data associated with them that contain various properties.

Java Edition:

Main article: Entity format

 Entity data
Additional fields for mobs that can breed
Tags common to all entities
Tags common to all mobs
 state: The name for the armadillo's current posture. state="idle" means the armadillo standing and not rolled up. state="unrolling" means the armadillo is unrolling[more information needed]. state="scared" means the armadillo feels threatened by a nearby mob or player, and has rolled up to protect itself. Any other string for state defaults to the same behavior as "idle".

Bedrock Edition:

See Bedrock Edition level format/Entity format.

