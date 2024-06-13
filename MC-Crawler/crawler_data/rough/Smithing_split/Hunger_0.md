# Hunger
Hunger is a player-specific feature of Minecraft that regulates player's certain abilities (health regeneration and the ability to sprint), the value of which is managed by the player's activity.

## Contents
- 1 Description
- 2 Mechanics
	- 2.1 Effects of hunger
	- 2.2 Exhaustion level increase
	- 2.3 Food level and saturation level restoration
- 3 Food poisoning
- 4 Achievements
- 5 Video
- 6 History
- 7 Issues
- 8 References

## Description
The player's hunger value is shown on the heads-up display in the form of a hunger bar (aka food bar), which is similar to the health bar. It is located above the hotbar, opposite to health bar and represented by ten ham shanks ( × 10). One half of a ham shank () represents one hunger point or half-unit of hunger, thus the full bar consists of twenty hunger points. It is replenished by eating food, and decreased by player's actions such as sprinting, digging or attacking.

Various levels of player's hunger control health regeneration (or depletion) and the ability to sprint. When hunger is at least 18 (), the player's health regenerates. If it falls to 6 (), the player loses the ability to sprint. If the hunger bar is at zero, the player's health depletes. The specific effects are described in the Effects of hunger section. The hunger value does not drain on Peaceful difficulty and regenerates if it is not at the maximum value.

An important aspect of hunger not shown on the hunger bar is called food saturation and controls the decreasing of the hunger value. It depends on what the player has eaten last. There is also a food exhaustion value that controls the decreasing of the food saturation level. How exactly they control the overall hunger value is described in more depth in the Mechanics section.

See also:  § Food poisoning

Certain foods have a chance of inflicting the Hunger effect on the player upon consumption, causing the player's food bar to deplete faster and turn a yellow-green color (). These foods are pufferfish, raw chicken (30% chance), and rotten flesh (80% chance). A husk can also give the player the Hunger effect upon being attacked by one.

## Mechanics
The hunger system utilizes four variables to control players' abilities, the values of which are stored in the player.dat format:

- foodLevel: The player's current hunger level, shown on the hunger bar. Its initial value onworldcreation or respawn is20 ( × 10).
- foodSaturationLevel: The player's current saturation level, which determines how fastfoodLeveldepletes and is controlled by the kinds of food the player has eaten. Its maximum value always equalsfoodLevel's value and decreases withfoodLevel. Its initial value on world creation or respawn is 5.
- foodTickTimer: This variable is used whenfoodLeveleither exceeds 17 (), or is at zero. It increases on everytick, and whenever it reaches 80 (4 seconds), it resets to zero and 1is added or deducted, depending on whether the player is saturated or starving. If the player has a full20 ( × 10),1⁄6of 1times the player'sfoodSaturationLevelis restored, up to a maximum of 1, whenfoodTickTimerreaches 10 (1⁄2second), andfoodTickTimeris reset to zero.
- foodExhaustionLevel: The player's current exhaustion level, which determines how fast thefoodSaturationLeveldepletes. Its value is increased by the player's actions (seeExhaustion level increasefor specific values). The initial value is zero. When it reaches a value of at least 4, the total value is decreased by 4 and one point is subtracted fromfoodSaturationLevel, orfoodLeveliffoodSaturationLevelis at zero.

The above variables can be queried in-game with the following command: /data get entity <player's name> <variable>‌[Java Edition  only].

As a visible sign that the saturation is used up, the hunger bar starts to shake or jitter periodically. When the saturation level is at zero, once the exhaustion value reaches 4, the total hunger value is decreased by 1 (). Eating food replenishes both hunger and saturation levels (see Food level and saturation level restoration for specific values), with the hunger level being replenished first, which also increases the maximum allowed saturation level. For example, if a golden carrot (giving 6 () and 14.4 saturation points) is eaten by a player whose hunger bar is at 9 () and saturation is below 1, its value increases to 15 (), and the golden carrot's saturation potential is fully used. However, if the hunger level is 8 (), its value increases to 14 () and only 14 saturation points are used.

### Effects of hunger
Various hunger levels lead to various effects on the player:

- When the hunger bar is at 20 () and there is any saturation left, health regenerates 1every1⁄2second.‌[Java Edition  only]
- When the hunger bar is at 18 () or more, health slowly regenerates 1every 4 seconds.
- When the hunger bar is at 17 () points or below, the player does not naturally regenerate health.
- If the hunger bar is at6 ()points or below, then the player cannot sprint.
- When the hunger bar is at0 (), the player's health depletes at a rate of 1every 4 seconds (this makessleepingimpossible). On Easydifficulty, the player's health stops dropping at 10, on Normal, it stops at 1, and on Hard, it keeps draining until either the player eats something or starves to death.Resistanceandarmordo not reduce starvation damage.[1]

Switching to Peaceful difficulty eliminates all penalties above, and rapidly restores the player's hunger bar and health.

### Exhaustion level increase
Any action not listed here does not increase exhaustion level. For example, normal walking doesn't increase exhaustion, and therefore does not decrease saturation or the food bar.

| Action                                                                                            | Exhaustionlevel increase | Units                                               |
|---------------------------------------------------------------------------------------------------|--------------------------|-----------------------------------------------------|
| Swimming                                                                                          | 0.01                     | per meter                                           |
| Breakinga block                                                                                   | 0.005                    | per block broken                                    |
| Sprinting                                                                                         | 0.1                      | per meter                                           |
| Jumping                                                                                           | 0.05                     | per jump                                            |
| Attacking anentity                                                                                | 0.1                      | per attack landed                                   |
| Takingdamagethat is normallyprotected by armor                                                    | 0.1                      | per distinct instance of damage being received      |
| Hunger                                                                                            | 0.005                    | per tick, per Hunger status effect level            |
| Jumping while sprinting                                                                           | 0.2                      | per jump                                            |
| Regenerating health by having× 9or higher and<br/>havinggamerule`naturalRegeneration`set to`true` | 6.0                      | per 1healed                                         |
| Hungerfromraw chickenorrotten flesh, or taking damage fromhusks.                                  | 3.0                      | full 0:30 duration of Hunger I, at 0.1 per second   |
| Hungerfrompufferfish                                                                              | 4.5                      | full 0:15 duration of Hunger III, at 0.3 per second |

