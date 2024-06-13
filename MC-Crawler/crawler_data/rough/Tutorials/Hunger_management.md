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

### Supernatural
Crafted with gold, these have a nourishment of 2.4.



** Enchanted golden apple **
Restores 
Advantages:
- Restore a lot of health and gives you an extra 16× 8for damage absorption.
- Cause temporary constant health regeneration that is not dependent on theplayer's hunger.
- Restore 9.6 saturation, considering their low hunger restoration.
- Give 2 minutes ofabsorptionIV,regenerationII‌[JE  only]/V‌[BE  only],resistanceandfire resistance.

Disadvantages:
- Very rare andnot renewableafter the1.9 Combat Update.
- Eating them takes a few seconds, whilesplash potions orlingering potions of Healing can be instantly applied bythrowingthem.
- Found only in structures (mineshaft,woodland mansion,desert pyramid,dungeon,bastion remnant,ruined portal,ancient city) chests.

** Golden apple **
Restore 
Advantages:
- Cause temporary constant health regeneration that is not dependent on the player'shunger.
	- The rate of regeneration is faster than the natural health regeneration inBedrock Editionand beforeJava Edition 1.9, making them useful in combat and emergency situations.
- Compared withpotions of regeneration, their effects are available without the need forbrewing, which is only possible by accessingthe Nether.
	- Not to mention that golden apples are stackable up to 64, but potions are not.
- Tree farmingcan provide a good supply ofapples.Tradingwith farmervillagers can also get them in quantity.
- Can be used to curezombie villagers. Ifgenerated structuresare turned off, this is the only way to obtain villagers and trade with them.
- Although they restore fewer hunger points, they grant 5 seconds ofregenerationII and 2 minutes ofabsorption, giving the player an extra 4.
- Restore 9.6 saturation, a large amount considering their low hunger restoration.
- They can be eaten while the hunger bar is full, which means the player can maintain a high level of saturation (and the natural regeneration it offers) without being only able to eat until the hunger bar starts draining.

Disadvantages:
- Require 8gold ingots to be crafted, meaning that they are too expensive to be an efficient food source inSurvival mode, unless with an efficient gold (zombified piglin) farm
- Eating them takes a few seconds, whilesplash potions orlingering potions of Healing can be instantly applied bythrowingthem.
- Finding them in structures (dungeon,mineshaft,igloo,stronghold,underwater ruins,desert pyramid,woodland mansion,ruined portal,bastion remnant) chests is rare and unreliable.

** Golden carrot **
Restore 
Advantages:
- Restore 14.4 saturation, the highest of any stackable food currently in the game.
- Can also be used to makepotions of night vision.
- Are cheaper thangolden apples. A golden carrot costs 8gold nuggets, but a golden apple costs 8gold ingots.
- Can bebought from farmer villagersin large quantities.

Disadvantages:
- Finding carrots can be difficult, as they are only found inpillager outpostandshipwreckchests, growing invillagefields, or dropped with an1⁄120chance fromzombies.
- Finding the golden carrot itself is also difficult, as they can be found inruined portalandbastion remnantchests.
- Though cheaper than golden apples, they still need gold nuggets to be crafted.
- The trading offer is 3 golden carrots for 3emeralds, which can be expensive, though the price can be lowered with zombification and curing, or theHero of the Villageeffect.

### Cooked food
These have a nourishment of 1.6 — the most nourishing of the ordinary foods.



** Steak and cooked porkchop **
Restores 
Advantages:
- They restore one of the highest amount of hunger and saturation (12.8 points) of any food in the game.
	- Two pieces regenerate 25.6 saturation, filling the saturation bar, so the player doesn't need to eat again for a long time.
- Can be found relatively early on, provided there arecows,mooshrooms and/orpigs nearby.
- Cows, mooshrooms and pigs can bebredto supply the player withraw beefandraw porkchops.
	- Cows, mooshrooms and hoglins also supply the player withleather.
- Hoglins are a source of porkchops inthe Nether.
	- Since hoglins are hostile mobs, theyrespawn quickly, making breeding unnecessary, enabling efficienthoglin farmsto be built.
- Raw beef and porkchops can be cooked quickly using acampfireorsoul campfirewhen away from a reliable source of food.
	- All these mobs can also be killed while on fire to get cooked meat directly.
- Cooked beef ‌[BE  only]and cooked porkchops areoffered by butcher villagersat reasonable prices.

Disadvantages:
- Their availability is dependent on the presence of animals within sight, which can be random and require extensive traveling depending on the biome the player spawns in.
- At least two animals of a type must be found to breed them for a reliable supply of meat.
- Breeding pigs requirescarrots,potatoes orbeetroots, which can be difficult to obtain, if there are novillages with carrot or potato farms nearby, orshipwrecks with supply chests, as they only very rarely drop fromzombies.
- Hoglins are hostile mobs that can cause massive damage, and they can only be hunted and bred inthe Nether, because in otherdimensionstheyzombify.

** Cooked mutton and cooked salmon **
Restores 
Advantages:
- Can be found relatively early on, provided there aresheep, and/orsalmonnearby.
- Restore 9.6 saturation.
	- Two pieces regenerate 19.2 saturation (equivalent to 20), filling the saturation bar completely.
- Breeding sheep also supplies the player withwool.
- Salmon spawn commonly inrivers andoceans in large schools, andrespawn relatively quicklywithout needing to breed them.
- Salmon can becaughtin any body of water with afishing rod.
- Raw mutton and raw salmon can be cooked quickly using acampfireorsoul campfirewhen away from a reliable source of food.
	- Sheep can also be killed while on fire to get cooked mutton directly.

Disadvantages:
- Their availability is dependent on the presence of animals within sight, which can be random and require extensive traveling depending on the biome the player spawns in.
- Similarly, to beef and pork, at least two sheep must be found to breed them for a reliable supply of mutton.
- Salmon cannot be bred, so the player has to hunt for them every time they need food, not to mention salmon are agile and hard to hit.
- Since salmon are aquatic mobs, it's almost impossible to kill them with fire to get cooked salmon directly, unless the player has aFire Aspectsword.

### Normal
These have a nourishment of 1.2 — the staple foods, cheap and fairly nourishing.



** Baked potato **
Restores 
Advantages:
- Restore 6 saturation.
- Restore a good amount of hunger and saturation.
- Potatoescan be farmed quickly and in large quantities, as each potato plant drops up to 4potatoes.

Disadvantages:
- Meats restore more hunger and saturation than baked potatoes.
- Finding the first potato can be difficult; they can be found only in structure chests,villages or as a rare drop fromzombies.

** Beetroot **
Restores 
Advantages:
- Beetroots can be used to breedpigs and can be crafted intored dye.
- No other actual advantages, though they can also be used for beetroot soup (see below).

Disadvantages:
- Beetroot seedscan be hard to find; they can be obtained fromvillagefarms, structure chests (snowy village,mineshaft,dungeon,end city,woodland mansion), andwandering traders.
- Beetrootgrows somewhat slower[verify]than other crops, and they only yield one beetroot for each plant.
- Individual beets have minimal food value, with only 1.2 saturation a piece.

** Beetroot soup **
Restores 
Advantages:
- Restores 7.2 saturation.
- It restores the same amount of hunger as sixbeetroots while taking only one-sixth as much time to eat.
- Uncrafted beetroot soup takes up less inventory space than uncraftedmushroom stew(up to 10 servings).

Disadvantages:
- Beetroot seedscan only be obtained fromvillagefarms, structure chests andwandering traders.
- Beetrootgrows somewhat slower[verify]than other crops, and they only yield one beetroot for each plant.
- Like other stews, beetroot soup does not stack when crafted.

** Bread **
Restores 
Advantages:
- Wheattakes little resources tofarmand maintain.
- Restore 6 saturation.
- One of the easiest foods to obtain early in the game.
- Pilesofhay bales commonly generate around plains, desert and savannavillages, which can easily be converted into an ample supply of bread.

Disadvantages:
- Wheat growing takes time, and threepiecesare required per bread loaf.
- Compared to 1-4carrots andpotatoes dropped from each plant, each wheat plant only yields a single piece of wheat.
- Bread requires acrafting tableto make.
- Meats restore more hunger and saturation than bread.

** Carrot **
Restores 
Advantages:
- Carrotsare easy to farm.
- Can be used to breedpigs andrabbits.

Disadvantages:
- Finding the first carrot can be hard, as it is found only invillages, structure chests, or rare drops fromzombies.
- Restores only 3.6 saturation.
- Meats andbaked potatoes restore more hunger and saturation than carrots.

** Cooked chicken **
Restores 
Advantages:
- Restores 7.2 saturation.
- Chickens are easier to find[verify]than most otherpassive mobs, and also layeggs and providefeathers.
- Chickens can be bred with any of several kinds ofseedsto breed, and the eggs make even those optional.
- Only a single chicken is needed to start a chicken farm; the eggs can be collected until more chickens spawn (which can then be bred as usual).
- Again thanks to the eggs, cooked chicken can befarmed completely automatically, compared to farming of other animals which needs the player to breed the animals.

Disadvantages:
- Other meats restore more hunger and saturation than cooked chicken.
- Eggs hatch into baby chickens, which need time to grow before they are able to lay more eggs, or can be killed for meat.

** Cooked cod **
Restores 
Advantages:
- Can befishedfrom any body of water, even underground or inthe End.
- Compared tosalmon,codis more commonly caught while fishing.
- Restore 6 saturation.
- Codcommonly spawn in mostoceanbiomes in large schools, andrespawn quicklywithout needing to breed them.

Disadvantages:
- Fishingtakes some time, making it slow to gather large amounts of fish.
- Findingcodmobs is also quite difficult, as they can only be found in regular, lukewarm and coldoceanbiomes.
- Other meats restore more hunger and saturation.

** Cooked rabbit **
Restores 
Advantages:
- Can be obtained relatively early on depending on the presence ofrabbits.  Rabbits can also be bred.
- Restore 6 saturation.
- Rabbits also supply the player withrabbit hideandrabbit's foot.
- Cooked rabbit can be purchased frombutcher villagers‌[Bedrock Edition  only].
- Can be used to craftrabbit stew.

Disadvantages:
- Other meats restore more hunger and saturation than cooked rabbit.
- Rabbits are relatively difficult to capture, kill and farm.

** Mushroom stew **
Restores 
Advantages:
- Can be a reliable food source ifmushrooms andmycelium,podzolornyliumcan be found.
- The recipe can be made in the 2×2 crafting menu.
- Restore 7.2 saturation.
- If possible, pressinguseon amooshroomwith abowlwill fill the bowl with stew.
- Huge mushrooms can be grown withbone mealonany dirt variantin dark places with enough place, and can be easily taken down with aniron axe.

Disadvantages:
- Like other stews, mushroom stew does not stack, so crafting a lot of stew at once takes up a lot of inventory space.
- A bowl of stew requires both types of mushrooms, which is bad news if you only have one type.
- Mycelium, podzol and nylium aren't easy to find, the first two found in rare biomes, the third only found inthe Nether.
	- Even if these blocks are found, the player can't obtain them withoutSilk Touch.
- Spreading based mushroom farmsare slow.
- Huge mushroom farmingrequiresbone meal, which is hard to obtain in large quantities in early game.

** Rabbit stew **
Restores 
Advantages:
- Can be purchased frombutcher villagers.
- Restore more hunger than most food in the game (only beaten bysuspicious stewwithSaturationeffect, or a wholecake).
- Restore 12 saturation.

Disadvantages:
- Like other stews, rabbit stew does not stack.
- A bowl of rabbit stew restores less hunger and saturation than all of its ingredients combined.
- Crafting rabbit stew requires a crafting table.   The bowl can be crafted easily (and is reusable), but each of the four other ingredients needs to be separately found and perhaps farmed.
- As with most other animals, two rabbits are required to start breeding them.

** Suspicious stew **
Restores *
Advantages:
- Flowers and mushrooms are easy to find.
- Restore 7.2 saturation.
- It's equivalent to amushroom stew, but with an extrastatus effectdepending on the flower used.  Even with the flower, it can still be crafted in the player's inventory.
- When crafted withblue orchidordandelion, suspicious stew grants the effectSaturationfor 7‌[JE  only]/6‌[BE  only]ticks (0.35/0.3 seconds), meaning an additional7 ()hunger and 14 saturation, for a total of13 ( × 6.5)hunger and 21.2 saturation.  While some of the saturation will likely be wasted, especially if the player was too hungry to begin with, the stew will at least raise the saturation to match the hunger gauge.
	- As long as the player has7 ()hunger, eating a single bowl of saturation suspicious stew will raise both hunger and saturation to full.
- When crafted with anoxeye daisy, it gives 8‌[JE  only]/6‌[BE  only]seconds ofRegenerationinstead, which heals, making it all but essential when/gamerule naturalRegenerationis turned off.
- Suspicious stew can also be made byusinga flower and then abowlon abrown mooshroom.
- Suspicious stew can be purchased from farmer villagers.
- When crafted with anazure bluet, it gives 8 seconds ofBlindness, the only way to get this effect in survival mode, and is required for theHow Did We Get Here?advancement.

Disadvantages:
- Like all other stews, suspicious stew doesn't stack (though the ingredients do).
- Suspicious stew can have negative effects too (Blindness,Poison,Weakness, or evenWither).
	- Remembering the correct flower for the recipe is important.
	- Once a suspicious stew is crafted, there is no indication to the nature of its effect.  This also applies to stew purchased from villagers.
	- The above points make it risky to eat any suspicious stew that you didn't craft yourself, thus its name.

### Low
These have a nourishment of 0.6, these are useful for achieving a full bar of both hunger and saturation when the current hunger bar is almost empty, if eaten with foods of higher tier of nourishment.



** Apple **
Restores 
Advantages:
- Can be obtained very early whenoak leavesordark oak leavesare broken or decay.
- Can be crafted intogolden apples.
- Apprentice levelfarmer villagerscan trade them.
- Can be found inloot chests in many structures.

Disadvantages:
- Apples only drop from two types of leaves.
- Restore 2.4 saturation and few hunger points, making them worse than most other foods.
- Either breaking leaves to get them or finding avillagecan be difficult.

** Chorus Fruit **
Restores 
Advantages:
- Can be eaten even when the hunger bar is full, allowing you to further raise saturation.
- Once obtained from theouter end islands, cheap to farm.
- Can teleport the player to otherwise inaccessible locations, such as nearby unexplored caves or inside an enclosed structure.
- Can teleport a falling player to the ground, saving them from a fatal fall.

Disadvantages:
- The teleportation is random.
- Has a cooldown of 1 second before it can be eaten again.
- Only obtainable end-game.
- Chorus flowers have to be manually broken or shot with a projectile, which can be annoying.
- Restore 2.4 saturation.

** Dried kelp **
Restores 
Advantages:
- Found easily inoceans and lakes.
- Eaten 0.5 seconds faster than other foods.
- Can be turned intodried kelp blocks, a lasting fuel.

Disadvantages:
- Is only worth eating if you have large amounts, and is more useful in its block form where it can be used as fuel.
- You have to cook regularkelpto get it.
- Restore 0.6 saturation.

** Melon slice **
Restores 
Advantages
- Melon farmingis easy to automate.
- Eachmelon blockdrops 3-7 melon slices, so you can quickly get a lot in only one harvest.
- Melon slices can be crafted intoglistering melon slices, which can be used to make apotion of Healing.
- For food efficiency minded players, melon slices are almost never wasted on overfilling the hunger bar.
- Melon slices can be crafted intomelon seeds.
- Melon plant stems will stay productive indefinitely with no need to replant them.

Disadvantages
- Melon seedscan only be found in structurechests (mineshafts,dungeons, andwoodland mansions).
- Melonblocks are only found injungles, savannavillages andwoodland mansions.
- Melon stems grow slowly and don't instantly spawn melon blocks even when grown withbone meal.
- Only restore 1.2 saturation per slice, so a diet of melon slices needs frequent stops to eat.

** Poisonous potato **
Restores 
Advantages:
- Can be used on servers to show how muchpotato farming you have done (pun intended).
- They can be eaten to fulfill theA Balanced Dietadvancement.
- No additional advantages otherwise.

Disadvantages:
- Have a 60% chance to inflict thePoisoneffect.
- Rarely found in chests.
- Restore 1.2 saturation and few hunger points.
- Can't even becomposted.

** Potato **
Restores 
Advantages:
- Potatoes may be found in plenty invillagefarms; otherwise they are a rare drop from zombies.

Disadvantages:
- Potatoes are far less nourishing thanbaked potatoes.
- Restore 0.6 saturation and few hunger points.

** Pumpkin pie **
Restores 
Advantages:
- Pumpkin pie has a high hunger restoration value. Good choice for restoring hunger points before eating something with more saturation.
- Can be crafted in the player's inventory, as long as one is carrying the ingredients (pumpkins,sugarandeggs).
- Restore 4.8 saturation.
- All ingredients required to craft pumpkin pie can be farmed automatically.

Disadvantages:
- Meats restore the same amount of hunger and far more saturation than pumpkin pie.
- Pumpkins (and their seeds) are relatively rare, so it may take some time and traveling before the player is able to establish apumpkin farm.
- Pumpkin plants are slow to grow a pumpkin and only yield one at a time per plant.

** Raw beef, raw porkchop, and raw rabbit **
Restores 
Advantages:
- Raw beef and raw porkchops are relatively quick to get.
- Unlikeraw chicken, these meats do not carry a chance of contractingfood poisoningwhen eaten.
- Cooking them gives their cooked versions.
- Cows andmooshrooms can drop up to 3 raw beef, andpigs andhoglins can drop up to 3 and 4 raw porkchops respectively.

Disadvantages:
- The availability of raw meat is dependent on the presence of animal mobs.
- Raw meat offers significantly less food value than cooked meat.
- Restore 1.8 saturation.
- Killing hoglins isn't the best option unless it's a Nether survival, because they are hostile and deal massive damage.

** Raw chicken and raw mutton **
Restores 
Advantages:
- Chickens are relatively easier to find[verify]in the world thanpigs orcows, andsheepare also easy to find.
- Chickens are easily killed, as they have only 4health, making obtaining raw chicken both time effective, and food/saturation effective.
- Supplies of raw chicken are easier to maintain, as chickens also dropeggs which can be hatched into chicks for mass production of raw chicken rather than being dependent onwheat seedsorwheatforbreeding.
- Sheepcan beshearedto getwool.
- Chicken farming can be automated, providing an easy way of collecting eggs, raw chicken andfeathers.

Disadvantages:
- Raw chicken has a 30% chance of giving the playerfood poisoning.
- Cooked chickenorcooked muttonrestores more hunger points and saturation.
- Both restore 1.2 saturation.

### Poor
With a nourishment value of 0.2, these foods will provide almost no saturation. They are basically snacks that will rarely ever overfill the saturation bar.



** Cake **
Restores  (slice),  (whole)
Advantages:
- Cake can be used repeatedly and can be shared by several players as a feast item.
- Can be used as a decoration block.
- Cake can be eaten instantly without any eating animation and without switching the currently selected item.
- Cake restores a lot of hunger when eaten as a whole.
- In a big server or a laggy world, you will eat cake very fast, while other foods will take a very long to eat.

Disadvantages:
- Cake requires several different items to craft:sugar,wheat, aneggand threemilk buckets. Not only is acrafting tableis required for the recipe, but the milk buckets are non-stackable.
- Once cake is placed, it cannot be retrieved. If the block below the cake is broken, the cake will disappear.
- Cakes need to be placed to be eaten, which means they cannot be eaten in places where one cannot build.
- If you only eat part of a cake, you'll have to come back to that exact spot to eat the rest of it later on.
- Is not stackable inJava Edition.
- Restores just 0.4 saturation per piece, or 2.8 as a whole.

** Cookie **
Restores 
Advantages
- Crafted from two pieces ofwheatand one item ofcocoa beans.
- The ingredients can be farmed in large quantities.
- 8 cookies are made each time.
- One batch of cookies restores 16 hunger and 3.2 saturation with only 2 pieces of wheat, much more efficient than bread.

Disadvantages
- When fed to aparrot, a cookie will kill the parrot instantly.
- Restores only 0.4 saturation apiece.

** Honey Bottle **
Restores 
Advantages:
- Removepoison.
- A player only needs to harvest it from abeehiveorbee nest.
- Can be eaten while the hunger bar is full.
- Compared tomilk bucketthat removes all effects and cannot be stacked, honey bottles can stack to 16 and only removesPoison.

Disadvantages:
- Restore 1.2 saturation.
- Harvesting honey in the wild can be hazardous, andhoney farmingcan be a tricky business.
- Can only stack up to 16, though larger amounts can be stored ashoney blocks.

** Pufferfish **
Restores 
Advantages:
- Being the only way to obtainnausea, eating pufferfish is needed to get the advancementHow Did We Get Here?.
- Used for brewing apotion of Water Breathing.

Disadvantages:
- Pufferfish inflictHunger,Poison, andNauseaeffects, drainingand keeping you down tofor 48 seconds.

** Raw cod and raw salmon **
Restores 
Advantages:
- Raw cod or salmon can be used to tamecats, trustocelots, or feeddolphins.
- Can be obtained byfishing, or by killingcod,salmon,guardians,elder guardians,polar bears, ordolphins.

Disadvantages:
- Raw fish is not nearly as nourishing as cooked fish.

** Rotten flesh **
Restores 
Advantages:
- Easily obtained, either when fighting zombies, or after they burn in the sun.
- Rotten flesh can be a good emergency food when no better food is available:  If many pieces are eaten at once, theHungereffect do not stack up, instead it will last only 30 seconds from the last piece eaten, and consume less hunger than granted by a single piece of rotten flesh.  Accordingly, eating multiple pieces of rotten flesh will still leave the playerlesshungry and perhaps allow some healing.
- Incombat, eating rotten flesh is a good way of keeping your hunger topped off so that your health keeps regenerating, without wasting better quality food.
- Rotten flesh can be used to feed and breedwolveswithout poisoning them.

Disadvantages:
- Has an 80% chance to triggerfood poisoning, depleting the hunger for thirty seconds.
- Only restores 0.8 saturation.
- Killingzombies for rotten flesh may be dangerous for unskilled players.

** Spider eye **
Restores 
Advantages:
- None, it is best to leave them in yourbrewinglab.
- The only reasonable use is to fulfill theA Balanced Dietadvancement.
- If no other food is available, remember that when eating many of them, the poison duration does not stack.

Disadvantages:
- They givePoisonfor 4 seconds.
- Restore 3.2 saturation.

** Sweet berries **
Restores 
Advantages:
- Are easily obtainable in large quantities while in aTaigabiome.
- Sweet berries can be used to trustfoxes.
- Sweet berry bushes can be used as defenses, and the berries can be harvested without affecting their defensive properties.

Disadvantages:
- The bush block causes damage to anything that enters its hitbox (exceptfoxes).

** Tropical Fish **
Restores 
Advantages:
- Can besold to fisherman villagersat a reasonable price.
- They can be eaten to fulfill theA Balanced Dietadvancement.

Disadvantages:
- Can only be rarely caught fromfishing.
- Thetropical fishmob can only be found in lush caves, mangrove swamps or in warm, lukewarm oceans and deep variants.‌[JE  only]
- Tropical fish restore little hunger and saturation.

## Emergency measures
If your hunger meter is dropping and you have no food in hand, there are a few emergency measures you can take, depending on available resources.

** Milk **
If you have a bucket and a cow, mooshroom or goat milk them. The milk will let you fill up onrotten flesh,raw chicken,spider eyes, orpoisonous potatoes, and then cure the illness.
** Fast crops **
If you have anypotatoesorcarrots, and somebone meal(craft 3 from oneskeletonbone, or get fromcomposter), you can make a hoe and till somedirtnear anywatersource, then plant your vegetables and use the bone meal to make them mature more quickly. It can take several pieces of bone meal to get a mature plant. Cooking the potatoes will make them much more filling. If you have the bone meal but no carrots or potatoes, you can destroy someshort grassnear a river or lake, make and use ahoe, then plantwheat seedsand use the bone meal to rapidly grow yourwheat. The same caveats as above apply to the use of bone meal.
** Doing nothing **
You won't lose hunger if you don't do anything (walking, mining, healing, etc.). InHardcoreespecially, this can be a necessary strategy while waiting for crops or baby animals to grow.
** Death **
A last-ditch measure: If you're close to yourbedor spawn point, stuff yourinventoryandarmorinto achestor two … thendie. OnHard mode, you can just wait to die of starvation, otherwise, good methods are drowning, jumping off cliffs, or droppinggravelorsandon yourself. You will respawn with full health and hunger bars, and can then reclaim your stuff. Naturally, this method doesn't apply in hardcore. Note that this isn't a totally free solution: you lose most of yourexperience.
