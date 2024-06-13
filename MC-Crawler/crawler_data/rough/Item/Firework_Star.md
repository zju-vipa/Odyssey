# Firework Star
Firework stars are items used to determine the color, effect, and shape of firework rockets.

## Contents
- 1 Obtaining
	- 1.1 Crafting
- 2 Usage
	- 2.1 Crafting ingredient
- 3 Effects
	- 3.1 Shape effects
	- 3.2 Additional effects
- 4 Sounds
- 5 Data values
	- 5.1 ID
	- 5.2 Item data
- 6 Video
- 7 History
- 8 Issues
- 9 Trivia
- 10 Gallery
	- 10.1 Screenshots

## Obtaining
In Survival mode, firework stars are obtainable only through crafting. In Creative mode, they can be found in the Creative inventory. Note that only the generic version can be found in it.

### Crafting
| Ingredients                                                  | Crafting recipe | Description                                                                                                                                                                                 |
|--------------------------------------------------------------|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Gunpowder+<br/>MatchingDye+<br/>Extra ingredients (optional) |                 | Up to eight dyes can be added.<br/>One head, gold nugget, feather, or fire charge can be added.<br/>Both the diamond and the glowstone dust can be added with any of the other ingredients. |
| MatchingFirework Star+<br/>AnyDye                            |                 | Adds a "fade to color" effect to the firework star, overwriting any existing fades.<br/>Up to eight dyes can be added.                                                                      |

| Ingredients                                                                                                                                                              | Crafting recipe | Description                                                                                                                                                                                                                                      |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Gunpowder+<br/>Bone Mealor<br/>Lapis Lazulior<br/>Cocoa Beansor<br/>Ink Sac+<br/>Heador<br/>Gold Nuggetor<br/>Featheror<br/>Fire Charge+<br/>Glowstone Dust+<br/>Diamond |                 | ‌[Bedrock Edition and Minecraft Education  only]<br/>Up to eight dyes can be added.<br/>One head, gold nugget, feather, or fire charge can be added.<br/>Both the diamond and the glowstone dust can be added with any of the other ingredients. |
| White Firework Staror<br/>Blue Firework Staror<br/>Brown Firework Staror<br/>Black Firework Star+<br/>Bone Mealor<br/>Lapis Lazulior<br/>Cocoa Beansor<br/>Ink Sac       |                 | ‌[Bedrock Edition and Minecraft Education  only]<br/>Adds a "fade to color" effect to the firework star, overwriting any existing fades.<br/>Up to eight dyes can be added.                                                                      |

## Usage
The only usage of firework stars is to create firework rockets.

### Crafting ingredient
| Name            | Ingredients                                | Crafting recipe | Description                                                                                                                                                                                                                                                                                                                                 |
|-----------------|--------------------------------------------|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Firework Rocket | AnyFirework Star+<br/>Paper+<br/>Gunpowder | 3               | Adding more gunpowder increases the duration of the rocket. Up to three gunpowder can be used. Up to five firework stars can also be used with three gunpowder. Up to seven firework stars can be used by using firework stars instead of additional gunpowder. All firework stars explode almost simultaneously when the rocket detonates. |

## Effects
### Shape effects
A firework star can have only one shape effect.

| Type | Ingredient  | Effect                                  | Sample animation |
|------|-------------|-----------------------------------------|------------------|
| 0    | None        | Small ball explosion (default)          |                  |
| 1    | Fire Charge | Large ball explosion and heavy sound.   |                  |
| 2    | Gold Nugget | Star-shaped explosion                   |                  |
| 3    | Head(any)   | Creeper-shaped (creeper face) explosion |                  |
| 4    | Feather     | Burst explosion                         |                  |

### Additional effects
In addition to the shape effects, any combination of these additional effects may be added to a firework star.

| Ingredient                 | Effect                                                  | Sample animation |
|----------------------------|---------------------------------------------------------|------------------|
| None                       | Default                                                 |                  |
| Glowstone Dust             | Twinkle (Crackle effect and sounds after the explosion) |                  |
| Diamond                    | Trail effect after the explosion                        |                  |
| Glowstone Dust<br/>Diamond | Twinkle + trail effect after the explosion              |                  |

## Data values
### ID
Java Edition:

| Name          | Identifier      | Form | Translation key                |
|---------------|-----------------|------|--------------------------------|
| Firework Star | `firework_star` | Item | `item.minecraft.firework_star` |

Bedrock Edition:

| Name          | Identifier      | Alias ID          | Numeric ID | Form | Translation key             |
|---------------|-----------------|-------------------|------------|------|-----------------------------|
| Firework Star | `firework_star` | `fireworkscharge` | `520`      | Item | `item.fireworksCharge.name` |

### Item data
Java Edition:

Main article: Item format
- tag: The item'stagtag.

- 
	- Explosion: The explosion effect contributed by this firework star.
		- 
		- Tags common to all firework explosion effects

Bedrock Edition:

SeeBedrock Edition level format/Item format.
