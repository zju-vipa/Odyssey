# Tutorials/Hunger management
Hunger is a feature in Minecraft's survival mode, requiring the player to eat in order to survive. It does not affect the player in Spectator or Creative modes. On Peaceful difficulty, hunger drain is disabled. Hunger levels are represented by a meat bar (similar to a stamina bar) next to the health bar. As this bar drains away, various unpleasant things happen:

## Contents
- 1 Conserving energy
- 2 Effects of hunger
- 3 Food
	- 3.1 Supernatural
	- 3.2 Cooked food
	- 3.3 Normal
	- 3.4 Low
	- 3.5 Poor
- 4 Emergency measures
- 5 Video

## Conserving energy
Several techniques can reduce your need for food:

- The most important tip is to avoid taking damage. Natural health regeneration uses far more hunger points than almost anything else.  This includes all types of damage like combat, falls, fire, poison, drowning, etc.
	- Armor will sharply reduce damage taken from most causes. Full diamond and netherite armor reduce damage you incur up to 80%.
	- Using more powerful weapons also shorten fights by killing things faster, leaving them fewer chances to hit you.  Likewise, ranged weapons allow you kill most mobs from a safer distance.
	- Especially avoid poison. Common enemies with poison arecave spidersandwitches. If poisoned, cure it quickly otherwise the poison can take alotof health points.
- Avoid fighting when you can -- 60 blows either way costs as much as healing a point of damage.  Taking falling damage does count as a blow.
	- Avoiding monsters and using a bed at night are the main things here.
- Reducejumping. While mining, carry somecobblestoneorlogs, and, whenever possible, craft and placestairs,slabsorladders instead of jumping.  120 jumps cost as much as healing one point of damage.
- Avoidsprinting, as it rapidly depletes your hunger bar. Jumping while sprinting is especially energy consuming.  Sprinting 60 meters costs as much as healing one point of damage.
	- Jumping costs four times as much hunger if you arealsosprinting, so 30 sprint-jumps equal healing one point of damage.
- While crossing deep water, use aboat(or make bridges) instead of swimming, as the former is faster and does not deplete the hunger bar.  Swimming 600 meters costs as much as healing one hunger point.

## Effects of hunger
Main article: Hunger
There are three hunger variables you need to worry about: The visible hunger bar, and two hidden values which are called "saturation" and "exhaustion". Hunger and saturation range from 0 to 20 (hunger is shown as ), but saturation cannot exceed your hunger (for example, if you have 17 ( × 8.5) hunger, you can have at most 17 saturation). 

Exhaustion ranges from 0 to 4. As you move about, fight, mine, etc, exhaustion accumulates. In order, common activities that will exhaust you the most are: Healing damage (most of a food point per health point), a "sprint jump", sprinting any distance, attacking monsters or receiving damage (from any source), and jumping. 

More specific values can be found in the table:

| Action                                                                                                           | Exhaustionlevel increase | Units                                               |
|------------------------------------------------------------------------------------------------------------------|--------------------------|-----------------------------------------------------|
| Swimming                                                                                                         | 0.01                     | per meter                                           |
| Breakingablock                                                                                                   | 0.005                    | per block broken                                    |
| Sprinting                                                                                                        | 0.1                      | per meter                                           |
| Jumping                                                                                                          | 0.05                     | per jump                                            |
| Attacking anenemy                                                                                                | 0.1                      | per attack landed                                   |
| Takingdamagethat is normallyprotected by armor                                                                   | 0.1                      | per distinct instance of damage being received      |
| Hunger status effect(food poisoning)                                                                             | 0.1                      | per second, per Hunger status effect level          |
| Jumping while sprinting                                                                                          | 0.2                      | per jump                                            |
| Regenerating health by having at least 18 hunger (× 9) and<br/>having`/gamerule naturalRegeneration`set to`true` | 6.0                      | per 1healed                                         |
| Food poisoning fromraw chickenorrotten flesh, or taken damage fromhusks.                                         | 3.0                      | full 0:30 duration of Hunger I, at 0.1 per second   |
| Food poisoning frompufferfish                                                                                    | 4.5                      | full 0:15 duration of Hunger III, at 0.3 per second |

When exhaustion reaches 4, it resets to 0, and saturation decreases by 1. When saturation reaches 0, the hunger bar will start to visibly ripple, and hunger starts to drain away in place of saturation. As a result, a way to visualize saturation is to think of it as an "extra hunger bar" invisible above your hunger bar, that's reduced before hunger at the same speed.  

When your hunger drops below 18 ( × 9), you stop naturally healing. Then at 6 () or below, you will be unable to sprint. Also, when your hunger drops to 0 (), you start to take starvation damage. On Easy mode, starvation damage will not lower you below 10, while on Normal mode, it can reduce you to 1. On Hard mode, starvation can kill you. 

Eating is essential to keep your health up, but it is not always needed. On Easy and Normal modes, the health bar will stop decreasing before death. If you are careful and do not take any further damage, then you can continue playing normally. Obviously, this is much riskier in multiplayer servers with PvP (player vs player), as well as adventuring.

With the exception of golden apples, chorus fruits, honey bottles and suspicious stew, you cannot eat when your hunger is at max; when you do eat, each food item restores a specific amount of hunger and saturation. 

The following section will elaborate on the strategies on effective management of both hunger and saturation.

## Food
Main article: Food
Food is a specific type of item that can be eaten by pressing the "use" button, when your hunger bar is not at maximum. Food restores both the hunger bar and saturation. Different types of food fill different amounts of each. You can obtain food through crafting, trading, searching naturally generated chests, farming, and killing mobs. Many foods can be cooked (smelted) for better effect. Burning mobs (e.g. flint and steel) is an easier method to obtain meat without the need of cooking.

Food can be divided into five tiers, according to how much saturation they restore per hunger unit. They are known as nourishment values, and the saturation one gets from any food is defined as nourishment times hunger. Knowing this, there are roughly two ways to approach the issue of hunger and saturation. Players can either try to eat efficiently, meaning using as little food items as possible, or try to eat expediently, meaning to stave off hunger as fast as they can.

The efficiency approach requires the player to avoid wasting hunger or saturation. Meaning, never eat any food that would "overfill" the hunger bar, avoiding to waste saturation points by going over the limit (the hunger value after consuming the food). By doing this, one will use every piece of food to its maximum potential. However, one needs to use more time to tend to their hunger bar and remember the current saturation value. Therefore, this is ill-suited for healing in emergencies, and should probably be done when safe and/or low on foodstuff.

The expediency approach, on the other hand, doesn't mind wasting a bit of the food here and there: Eat the most filling and nourishing food until full, and be done with it. If food supply is not an issue, if the player requires imminent healing, or if the player simply wants to save time, then, this is an appealing option.

A few foods also have special effects, mostly bad. While the golden apple can heal you, other foods can poison you (losing hit points) or give you food poisoning (draining your hunger bar). For these, there is milk bucket, obtained by using a bucket on a cow. While milk doesn't restore hunger or saturation, it does remove any status effects that the player currently has, so use it carefully. Another option are honey bottles, which only remove poison, do have some food value and are stackable (up to 16).

