# Composter
A composter is a block that converts some biological material into bone meal. It also serves as a farmer villager's job site block.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
- 2 Usage
	- 2.1 Composting
	- 2.2 Changing profession
	- 2.3 Redstone component
	- 2.4 Hoppers
	- 2.5 Fuel
	- 2.6 Note blocks
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Trivia
- 8 Gallery
	- 8.1 Renders
		- 8.1.1 Java Edition
		- 8.1.2 Bedrock Edition
	- 8.2 Screenshots
- 9 References
- 10 External links

## Obtaining
### Breaking
Composters can be broken using any tool, though an axe is the fastest. The composter does not retain the compost inside; instead, it drops empty.

| Block     | Composter             |
|-----------|-----------------------|
| Hardness  | 0.6                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 0.9                   |
| Wooden    | 0.45                  |
| Stone     | 0.25                  |
| Iron      | 0.15                  |
| Diamond   | 0.15                  |
| Netherite | 0.1                   |
| Golden    | 0.1                   |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
Composters generate in village farms. They can also generate in trail ruins.

### Crafting
| Ingredients    | Crafting recipe |
|----------------|-----------------|
| AnyWooden Slab |                 |

## Usage
Composters can be used to recycle a selection of food and plant items into bone meal. To do so, the player must use any of a selection of items on the composter. When an adjacent comparator is facing away from the composter, a comparator signal strength of up to 8 is emitted depending on the fullness of the block.

Composters appear to have an empty interior. As such, entities can enter and exit a composter through the top, but not the sides or bottom. The composter has a "floor", whose height depends on the fullness. When the composter is completely empty, this floor is slightly above the block below, and when it is completely full, there is a slight dip on top. In Bedrock Edition, when the composter’s fullness increases, any entities inside are pushed up accordingly.

### Composting
The composter can be filled with compost, which is done by adding compostable items to it. When successfully adding an item, a green particle () appears. The table below lists supported items, which have different levels of compost-ability. The higher the percentage of an item, the more likely it is for it to add another layer of compost. While the composter is empty, any compostable item can create the first layer of compost. Each layer of compost has a podzol-like appearance. When the composter reaches the 7th layer of compost, the compost changes appearance indicating that bone meal can be collected by using the composter a final time.

The following table shows the items that can be used in a composter, the percent chance for an item to add a level of compost, and the average number of items needed to fill a composter. Smaller pieces (individual pieces of wheat, melon slices, etc.) produce more compost than the blocks or other items that can be made from them. The exception is cookies, because each recipe produces 8 cookies, and together those give more than 3 times the compost.

Despite being plants, it is not possible to compost bamboo,[1] dead bushes,[2] poisonous potatoes[3] and chorus plant products.[4]. Meat and fish are also not compostable, unlike some other food items.

| Composting chance (per item)                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                                                                            |                           |                                             |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|---------------------------------------------|
| 30%                                                                                                                                                                                                                                                                                                                                                                   | 50%                                                                                                                                                                                          | 65%                                                                                                                                                                                                                                                                                                                                                       | 85%                                                                                                                                                                        | 100%                      |                                             |
|                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                                                                            |                           | Items                                       |
| Beetroot Seeds<br/>Dried Kelp<br/>Glow Berries<br/>Grass Block‌[BE  only]<br/>Hanging Roots<br/>Mangrove Propagule<br/>Mangrove Roots<br/>Kelp<br/>Leaves<br/>Melon Seeds<br/>Moss Carpet<br/>Pink Petals<br/>Pitcher Pod<br/>Pumpkin Seeds<br/>Saplings<br/>Seagrass<br/>Short Grass<br/>Small Dripleaf<br/>Sweet Berries<br/>Torchflower Seeds<br/>Wheat Seeds<br/> | Cactus<br/>Dried Kelp Block<br/>Flowering Azalea Leaves<br/>Glow Lichen<br/>Melon Slice<br/>Nether Sprouts<br/>Sugar Cane<br/>Tall Grass<br/>Twisting Vines<br/>Vines<br/>Weeping Vines<br/> | Apple<br/>Azalea<br/>Beetroot<br/>Big Dripleaf<br/>Carrot<br/>Cocoa Beans<br/>Fern<br/>Flowers<br/>Fungus<br/>Large Fern<br/>Lily Pad<br/>Melon<br/>Moss Block<br/>Mushrooms<br/>Mushroom Stem<br/>Nether Wart<br/>Potato<br/>Pumpkins<br/>Crimson Roots<br/>Warped Roots<br/>Sea Pickle<br/>Shroomlight<br/>Spore Blossom<br/>Wheat<br/>Wither Rose<br/> | Baked Potato<br/>Bread<br/>Cookie<br/>Flowering Azalea<br/>Hay Bale<br/>Mushroom Blocks<br/>Nether Wart Block<br/>Pitcher Plant<br/>Torchflower<br/>Warped Wart Block<br/> | Cake<br/>Pumpkin Pie<br/> |                                             |
|                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                                                                            |                           | Average number of items to complete compost |
| 23.33                                                                                                                                                                                                                                                                                                                                                                 | 14.00                                                                                                                                                                                        | 10.77                                                                                                                                                                                                                                                                                                                                                     | 8.24                                                                                                                                                                       | 7.00                      |                                             |
|                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                                                                            |                           | Average compost yield (per stack)           |
| 2.74                                                                                                                                                                                                                                                                                                                                                                  | 4.57                                                                                                                                                                                         | 5.94                                                                                                                                                                                                                                                                                                                                                      | 7.77                                                                                                                                                                       | 9.14                      |                                             |

