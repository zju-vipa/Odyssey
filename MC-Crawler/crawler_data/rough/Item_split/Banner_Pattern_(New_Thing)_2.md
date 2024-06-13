#### All food restrictions
| Food item              | Food restriction proposal text    | Name of item when inedible               |
|------------------------|-----------------------------------|------------------------------------------|
| Air                    | rule.food_restriction.air_block   | rule.food_restriction.inedible.air_block |
| Apple                  | An Apple Party Diet               | Oak Tree Nut                             |
| Baked potato           | A Get Baked Diet                  | Baked Bump from the Dirt                 |
| Beetroot               | A Beeter Diet                     | Red Dirtbump                             |
| Beetroot soup          | A Soup Kitchen Diet               | Blood in a Bowl?                         |
| Bread                  | A Toasty Diet                     | Dried Porridge                           |
| Cake                   | A Birthday Diet                   | Lies                                     |
| Carrot                 | A Rabbit Diet                     | Rabbit Feed                              |
| Chorus fruit           | A Nomportation Diet               | Purple Alien Orb                         |
| Cooked chicken         | A Nugget Time Diet                | Burnt Bird                               |
| Cooked cod             | A Fish Without Chips Diet         | Ruined Sushi                             |
| Cooked mutton          | A Woolsome Diet                   | Disgusting Burnt Sheep Piece             |
| Cooked porkchop        | Bringing Home the Bacon Diet      | Charred Pig Part                         |
| Cooked rabbit          | A Bingo Diet                      | It Liked Jumping Around You Murderer     |
| Cooked salmon          | A River Diet                      | Slimy Fish Goop                          |
| Cookie                 | An Unhealthy Diet                 | Yucky Yellow Thing                       |
| Dried kelp             | A Weedy Food Diet                 | Dried But Somehow Also Slimy             |
| Enchanted golden apple | Michellin Level Expensive Diet    | Inedible Shining Blob                    |
| Glow berries           | An X-Ray Diet                     | Light Bulbs                              |
| Golden apple           | A Healthy Diet                    | Inedible Yellow Blob                     |
| Golden carrot          | Expensive Rabbit Food Diet        | Rabbit Food                              |
| Honey bottle           | A Sugar Drink Diet                | Too Much Sugar                           |
| Melon slice            | sliceddiet                        | Mostly Seeds                             |
| Mushroom stew          | Shrooms! Only Shrooms!            | Fungal Goop                              |
| Poisonous potato       | A Dubious Spud Diet               | Useless Knob                             |
| Potato                 | Unboiled, Unmashed, Unstewed Diet | Root Thing?                              |
| Pufferfish             | A Killer Diet                     | The Terror of the Deep                   |
| Pumpkin pie            | Mmmm, Pie. Pie! Only Pie!         | It's Not a Pie You Didn't Even Bake It   |
| Rabbit stew            | An Auto-Jump Diet                 | Who Stewed Roger Rabbit?                 |
| Raw beef               | A Cow Sushi Diet                  | Cut Cow                                  |
| Raw chicken            | A Salmonella Diet                 | Birdbits                                 |
| Raw cod                | A Fishy Diet                      | Slimy Water Thing                        |
| Raw mutton             | A Raw And Wooly Diet              | Sheet of Sheep                           |
| Raw porkchop           | A Pork Belly Diet                 | Piece of Pig                             |
| Raw rabbit             | Raw Jumpers Only                  | Bunneh :(                                |
| Raw salmon             | A Sushi Diet                      | Red Slimy Water Thing                    |
| Rotten flesh           | A Rotten Diet                     | Unhealthy Thing                          |
| Spider eye             | A Witching Diet                   | Arcachneous Orb                          |
| Steak                  | A Meat Lovers Diet                | Cremated Cow                             |
| Suspicious stew        | A Sus Diet                        | Sus                                      |
| Sweet berries          | A Sweet, Sweet Diet               | Stick Blobs                              |
| Tropical fish          | Only Eating Nemo                  | Nemo                                     |

### General
** Attribute **
- Added new attribute calledminecraft:generic.scale(Entity Scale).
- Controls the magnification of entity size. Defaults to 1.0.

** Capes **
- Added 6 new capes:

| Name                    | ID             | Texture |
|-------------------------|----------------|---------|
| Awesom caep             | `awesom`       |         |
| Blonk Cape              |                |         |
| No round shapes allowed | `no_circle`    |         |
| Nya, nya, nya, UwU!     | `nyan`         |         |
| Squid Cape              | `squid`        |         |
| Veterinarian Cape       | `veterinarian` |         |

- The blonk cape cannot be viewed in-game.

** Death messages **
- The following death messages have been added:
	- <player> experienced the dark side of the moon
		- Appears when the player runs out of breath and dies inthe Moondimension.
	- <player> was turned into gold
		- Appears when the player turns into gold by another player.

** Splashes **
- The original splash texts have been replaced with the following entries:
	- Exactly 181 rules to vote on!
	- Choose Your Own Adventure!
	- Choice Edition!
	- Democratic!
	- People's Choice!
	- Vote!
	- I Voted!
	- Picking and Choosing!
	- Freedom of Choice!
	- Make Your Voice Heard!
	- Choose Wisely!
	- As You Wish!
	- Community Choice!
	- Vote-Driven Development!
	- Mob Votes! Biome Votes! Food Votes! Moon Votes!
	- The Chosen Challenge!
	- To the Moon!
	- The Golden Vote!
	- Voted Game of the Year!
	- By Popular Vote!
	- A/B Voting!
	- Fair Votes Guaranteed!
	- Multiple Choice Gaming!
	- Vote With Your Gaming!
	- Game-Changing Votes!
	- Your Call!
	- You Decide!
	- I Demand a Recount!
	- Vox Populi, Vox Dei!
	- Machine Voting!
	- Online Voting!
	- Voting About Voting!
	- Can't Blame The Developers For Your Choices!
	- ✅
	- ❎

** Sounds **
- Added 4 new hidden kazoo-likesoundsthat play when voting forminecraft:the_joke.
	- sad1.ogg
	- sad2.ogg
	- sad3.ogg
	- sad4.ogg

** Toasts **
- Added a new toast notification that appears every few seconds when the player has not yet opened their voting screen, and a vote proposal has started. The notification title is "New proposal received!" in purple text, while the main message differs depending on how long has passed since the first notification appeared.
	- Opening the voting screen once prevents these toasts from ever appearing in the future, unlessoptions.txtis edited externally.
	- These toasts use a value called "urgency" which has four values:LOW,MEDIUM,CONCERNING,WHY_ARE_YOU_NOT_DOING_IT.
	- They start atLOWurgency, which lasts 2 minutes, change toMEDIUMfor 2 minutes, then toCONCERNINGfor 1 minute and finally toWHY_ARE_YOU_NOT_DOING_ITuntil the world is closed or the voting screen is opened.
	- The notification's main message changes depending on the level of urgency.
		- AtLOWurgency, toasts appear every 15 seconds, last 5 seconds each and can have the following messages:
			- Pressvto open voting screen
			- To open voting screen, pressv
			- New vote started, pressvto cast your vote
		- AtMEDIUMurgency, toasts appear every 10 seconds, last 3 seconds each and can have the following messages:
			- A new proposal is waiting for your vote, pressv
			- Others are having fun while you are not pressingv
			- Time to change some rules, pressv
			- You have new vote proposals to review, pressvto access!
		- AtCONCERNINGurgency, toasts appear every 5 seconds, last 2 seconds each and can have the following messages:
			- Ok, so the whole idea of this release is to vote, so pressv
			- Somebody wants to tell you what you can and can not do, pressvto prevent that
			- At this point you are probably just waiting to see what happens next. Fine! But you can avoid that by pressingv.
			- If you can't findv, it's probably on your keyboard
			- Not pressingvhas been proven less fun that pressingv
			- Do you want more phantoms? That's how you get more phantoms! Pressv
			- Please, just pressvand be done with it!
			- Hot votes in your area! Pressv
		- AtWHY_ARE_YOU_NOT_DOING_ITurgency, toasts appear every half a second, last 1 second each and can have the following messages:
			- PRESSvPRESSvPRESSvPRESSvPRESSvPRESSvPRESSvPRESSvPRESSvPRESSv
			- WHYYYYYYYYYYYYYYYYYYYYYYYYY NOv
			- DO YOU HAVE NO IDEA WHEREvIS!?
			- gfdgh bbtvsvtfgfsgb avjhrst ujs  t 452423 r
			- Pressvto open voting screen
			- AAAAAAAvAAAAAAA!
				- The red and blue parts of this message are obfuscated.

