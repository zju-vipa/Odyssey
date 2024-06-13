# Thunderstorm
A thunderstorm is a somewhat uncommon and dangerous weather condition.

## Contents
- 1 Behavior
- 2 Effects
	- 2.1 Lightning
		- 2.1.1 Effects on mobs
		- 2.1.2 Lightning mechanics
		- 2.1.3 Thunder
		- 2.1.4 Lightning rods
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Entity data
- 5 Advancements
- 6 History
- 7 Issues
- 8 Trivia
- 9 Gallery
	- 9.1 Screenshots
- 10 References

## Behavior
Thunderstorms are an uncommon temporary, global occurrence[1] that can happen randomly at any time, within the Overworld. The exact type of precipitation during a thunderstorm varies depending on the temperature of the current biome, as well as the current altitude.

- While the clear counter is counting down, the weather is always clear. This counter is used only when the "/weather clear" command is issued, setting the counter to a value given by the player or 5 minutes (seeCommands/weather)
- The rain counter counts down to zero, and each time it reaches zero, the rain is toggled on or off. When the rain is turned on, the counter is reset to a value between 12,000-24,000 ticks (0.5-1 game days), and when the rain is turned off the counter is reset to a value of 12,000-180,000 ticks (0.5-7.5 game days).
- Like the rain counter, the thunder counter also toggles thunder on and off when it reaches zero, but clear weather overrides the "on" state. When thunder is turned on, the thunder counter is reset to 3,600-15,600 ticks (3-13 minutes), and when thunder is turned off the counter resets to 12,000-180,000 ticks (0.5-7.5 days).
- Thunder can occur in the game only when the rain and thunder states both happen to be "on" at the same time. The random combinations of the states toggled by the rain and thunder counters result in a 1.44% chance for a thunderstorm to occur, or an approximate average real-time duration of 9 hours between thunderstorms.
- The values in each range are uniformly distributed.

Thunderstorms can be skipped entirely with the use of a bed, regardless of the time of day.

## Effects
As with rain and snow, the sky is darkened and the sun, moon, and stars are no longer visible. Thunderstorms darken the world, causing the light level from the sky to visually decrease to 10. The clouds darken from white to dark gray, although clouds themselves do not precipitate or create lightning. While the sun is not visible during rain, the glow associated with sunrise and sunset is still visible.

Unlike during regular rainstorms or snowstorms, the light level from the sky is treated as if it were 0 for the purposes of hostile mob spawning, which allows hostile mobs to spawn at any time of the day.

### Lightning
Not to be confused with Lighting.



Lightning is a lethal element to thunderstorms. Lightning momentarily increases the sky light's brightness to slightly greater than full daylight.

The fire that a lightning bolt creates.
Lightning strikes randomly and creates fires (only on normal and hard difficulty) in a 2 block radius where it strikes. Such fires act normally, igniting all flammable materials, detonating TNT, and even activating nether portals. The lightning itself, however, is not destructive and does not destroy blocks. While most fires are extinguished by the rain, areas that block rain can allow the fire to spread, and any netherrack, magma blocks, soul sand, or soul soil lit by lightning is not extinguished by the rain.

Most entities struck by lightning are dealt 5 damage (sometimes twice in succession) and are set on fire, which may cause additional damage.

If the player is killed by a lightning strike, the death message appears: "<player> was struck by lightning". This message does not display if the player was killed by the fire created by a lightning bolt.

Lightning in Bedrock Edition changes color from white to orange at sunset, and appears brighter during the daytime.

Lightning may be manually summoned with the /summon lightning_bolt command. It is summoned as an entity, and it can be referred to by commands or selectors. 

A group of skeletal horsemen spawned during a thunderstorm.
Charged Creeper
A villager gets struck by lightning.
Lightning is also spawned when a trident enchanted with Channeling is thrown and strikes a mob or a lightning rod during a thunderstorm.

