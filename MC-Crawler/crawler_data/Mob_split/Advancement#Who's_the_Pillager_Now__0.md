# Advancement
Advancements are a way to gradually guide new players into Minecraft and give them challenges to complete, similar to the basic system of achievements in Bedrock Edition.

## Contents
- 1 Obtaining
	- 1.1 Notifications
- 2 Interface
- 3 List of advancements
	- 3.1 Minecraft
	- 3.2 Nether
	- 3.3 The End
	- 3.4 Adventure
	- 3.5 Husbandry
- 4 JSON format
- 5 Sounds
- 6 History
- 7 Issues
- 8 Trivia
- 9 Gallery
	- 9.1 Screenshots
	- 9.2 Renders and diagrams
- 10 See also
- 11 References

## Obtaining
Advancements can be completed in any game mode, and are obtained and saved per world. Advancements can also be granted (and revoked) using the /advancement command.

Although advancements guide players logically through the game, they are independent of each other; an advancement can be completed without having completed the advancements "before" it. There are 110 (122‌[upcoming: JE 1.21]) advancements: 16 in the Minecraft tab, 24 in the Nether tab, 9 in The End tab, 35 (44‌[upcoming: JE 1.21]) in the Adventure tab, and 26 (29‌[upcoming: JE 1.21]) in the Husbandry tab.

### Notifications
When an advancement is obtained, a sliding toast notification appears in the top right corner. Each notification is accompanied by a chat message, if the game rule announceAdvancements is set to true (i.e. enabled). The color of the header text in the notification depends on the advancement; normal and goal advancements have yellow header text, while challenge advancements have pink header text. Completing a normal advancement causes the header text to display "Advancement Made!", completing a goal advancement results in a "Goal Reached!" header, and completing a challenge advancement shows "Challenge Complete!" In addition, music plays and experience is rewarded when completing most of these advancements.

Unlike the others, the five "root" advancements in each tab, each of which appears as the left-most advancement in its tab, and have the same name as its tab, do not cause a chat message or notification to appear.

## Interface
The advancement interface. The "Isn't It Iron Pick" advancement is selected.
The button to access the Advancements screen is found on the pause menu screen. The player can also open this screen by pressing L (this can be changed in the in-game options menu).

The advancement system involves several trees composed of advancements, each tree beginning with a root advancement from which several branches diverge. By clicking and dragging, the player can view different branches of an advancement tree. Each tree is categorized into different tabs (which are defined by the root advancements). Tabs are not visible if no advancements in the tab have been unlocked. There are five tabs in vanilla Minecraft:

- Minecraft: The heart and story of the game
- Nether: Bring summer clothes
- The End: Or the beginning?
- Adventure: Adventure, exploration, and combat
- Husbandry: The world is full of friends and food

Each tab has a different background with a repeating texture. Tabs only appear when at least one advancement in that tab has been made. Tabs are ordered left to right, based on when the first advancement in each tab was made.

Advancement icons display a header name and description when hovered over. The advancement descriptions have a unique color depending on the type of advancement with normal and goal advancements having green descriptions and challenge advancements having purple ones. As more advancements are unlocked, new ones become visible, with up to two advancements being displayed ahead of an unlocked one. Unlocked advancements show all of its direct parents advancements (the advancements between the root advancement of the tab and it), even those that have not been unlocked (but only show up to 2 advancements downstream of advancements already unlocked). Nine advancements, "How Did We Get Here?", "Voluntary Exile", "Hero of the Village", "Arbalistic", "You've Got a Friend in Me", "Smells Interesting", "Birthday Song", "Little Sniffs", and "Planting the Past" are hidden advancements, meaning that they cannot be viewed by the player until they have been unlocked, regardless of if its child advancement(s) (any advancement after it, including all branches), if any have been unlocked, which would normally display its parent advancements (as advancements can be unlocked and completed in any order).

If the player has not completed/unlocked any advancements, the interface shows a black background with white text reading "There doesn't seem to be anything here... :(".[1]

The icon frames of advancements can vary in appearance based on difficulty, and whether or not it was completed. A legend is provided below:

| Icon frame |            | Description |
|------------|------------|-------------|
|            | Incomplete | Completed   |
|            |            | Advancement |
|            |            | Goal        |
|            |            | Challenge   |

Extra advancements and tabs can be added and customized with the use of JSON files and data packs.

## List of advancements
### Minecraft
Advancement tree in the "Minecraft" tab

| Minecraft |      |                        |                                             |                      |                                                                                                                                                                                                                           |                            |
|-----------|------|------------------------|---------------------------------------------|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|
|           | Icon | Advancement            | In-game description                         | Parent               | Actual requirements (if different)                                                                                                                                                                                        | Resource location          |
|           |      | Minecraft              | The heart and story of the game             | —                    | Have acrafting tablein the inventory.                                                                                                                                                                                     | story/root                 |
|           |      | Stone Age              | Mine Stone with your new Pickaxe            | Minecraft            | Haveoneof these 3 stones in the#stone_tool_materialsitem tag:Cobblestone Blackstone Cobbled Deepslatein the inventory.                                                                                                    | story/mine_stone           |
|           |      | Getting an Upgrade     | Construct a better Pickaxe                  | Stone Age            | Have astone pickaxein the inventory.                                                                                                                                                                                      | story/upgrade_tools        |
|           |      | Acquire Hardware       | Smelt an Iron Ingot                         | Getting an Upgrade   | Have aniron ingotin the inventory.                                                                                                                                                                                        | story/smelt_iron           |
|           |      | Suit Up                | Protect yourself with a piece of iron armor | Acquire Hardware     | Have any type of ironarmorin the inventory.                                                                                                                                                                               | story/obtain_armor         |
|           |      | Hot Stuff              | Fill a Bucket with lava                     | Acquire Hardware     | Have alava bucketin the inventory.                                                                                                                                                                                        | story/lava_bucket          |
|           |      | Isn't It Iron Pick     | Upgrade your Pickaxe                        | Acquire Hardware     | Have aniron pickaxein the inventory.                                                                                                                                                                                      | story/iron_tools           |
|           |      | Not Today, Thank You   | Deflect a projectile with a Shield          | Suit Up              | Block any projectile with ashield.                                                                                                                                                                                        | story/deflect_arrow        |
|           |      | Ice Bucket Challenge   | Obtain a block of Obsidian                  | Hot Stuff            | Have a block ofobsidianin the inventory.                                                                                                                                                                                  | story/form_obsidian        |
|           |      | Diamonds!              | Acquire diamonds                            | Isn't It Iron Pick   | Have adiamondin the inventory.                                                                                                                                                                                            | story/mine_diamond         |
|           |      | We Need to Go Deeper   | Build, light and enter a Nether Portal      | Ice Bucket Challenge | Enterthe Netherdimension.                                                                                                                                                                                                 | story/enter_the_nether     |
|           |      | Cover Me with Diamonds | Diamond armor saves lives                   | Diamonds!            | Have any type of diamondarmorin the inventory.                                                                                                                                                                            | story/shiny_gear           |
|           |      | Enchanter              | Enchant an item at an Enchanting Table      | Diamonds!            | Insert an item in anenchanting table, then apply an enchantment.                                                                                                                                                          | story/enchant_item         |
|           |      | Zombie Doctor          | Weaken and then cure a Zombie Villager      | We Need to Go Deeper | Useagolden appleon azombie villagerunder theWeaknesseffect; the advancement is granted when the zombie villagerconverts into a villager.In multiplayer, only the player that feeds the golden apple gets the advancement. | story/cure_zombie_villager |
|           |      | Eye Spy                | Follow an Eye of Ender                      | We Need to Go Deeper | Enter astronghold.                                                                                                                                                                                                        | story/follow_ender_eye     |
|           |      | The End?               | Enter the End Portal                        | Eye Spy              | Enterthe Enddimension.                                                                                                                                                                                                    | story/enter_the_end        |

