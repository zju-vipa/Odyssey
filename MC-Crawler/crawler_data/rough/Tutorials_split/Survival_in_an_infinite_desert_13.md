#### Wandering traders
Using the emeralds from the villager trading, you can buy useful resources from the wandering trader. The best things are flowers, dyes, sugar cane, red sand, kelp, coral blocks, saplings, plants, podzol (for renewable dirt), slimeball, packed and blue ice, etc. Do not buy a nautilus shell because there is no heart of the sea to make a conduit.

#### Zombifying and curing
You can cure villagers multiple times if you want, to get the cheapest trades. This table shows the number of cures required to make all trades 1 emerald or 1 item.

| Villager      | # Cures |
|---------------|---------|
| Armorer       | 3       |
| Butcher       | 3       |
| Cartographer  | 5       |
| Cleric        | 7       |
| Farmer        | 6       |
| Fisherman     | 4       |
| Fletcher      | 7       |
| Leatherworker | 6       |
| Librarian     | 5       |
| Mason         | 4       |
| Shepherd      | 5       |
| Toolsmith     | 6       |
| Weaponsmith   | 5       |

### Other things you can do
#### Farms
Thanks to the wandering trader, villagers, the nether and end, there are many farms that can be created. Tree farms for overworld wood are possible, as long as you have some dirt. All crops are also farmable, including chorus fruit. You can build bartering farms, hoglin farms, fortress farms and gold farms in the nether, and enderman farms in the end. Lava is also renewable from dripstone and dripstone blocks. All flowers and dyes are renewable from wandering traders. Overworld mob farms are also possible. Chickens can spawn as a chicken jockey in the nether, allowing for chicken farms. However, grass blocks are unobtainable, making flower farms useless although flowers are renewable. Sweet berries are unobtainable. Turtle eggs are also unobtainable. Mobs that require specific biomes cannot be spawned, such as turtles, strays, guardians, overworld animals, and drowned. Things like scutes, prismarine, raw beef, steak, and tridents are unobtainable. Villagers allow for renewable diamond armor, enchanted books, bells, and many other things. Raids can produce totems of undying and hero of the village can produce clay blocks, making terracotta renewable. The wither can be killed for nether stars and beacons.

#### Challenges
- Build massive farms to produce all renewable items
- Build massive projects
- Conquer a bastion remnant
- Take on a raid
- Complete all possible advancements. (How did we get here, trident related advancements are impossible without cheats)
- Do the challenge in hardcore mode or ultra hardcore
- Respawn the ender dragon
- Get every possible obtainable item and block
- Build a netherite or diamond beacon
- Get a full set of max enchantments netherite armor and all tools.

## Structures other than villages
### Mineshafts
One possibility for obtaining planks in a desert biome with Structures would be to find a natural cave or ravine and then dig down (which would be quite slow without basic mining tools) and attempt to find an mineshaft which is a treasure trove of oak planks (but home to deadly cave spiders).

(Note that at the time of writing there is a bug in Java Edition[1] reported with the /locate Mineshaft command, so don't rely on that to find a mineshaft until the bug is fixed.)

### Dungeons
Dungeon chests contain useful items including ingots, seeds, and buckets. However, all of these things can probably be obtained more easily from a Village (directly or, in the case of a bucket, indirectly via iron ingots).

There are unfortunately no wooden planks or wooden logs available in a dungeon.

### Pillager outposts
As of 1.14 there is another way to find a wood source without obtaining saplings or trees, which is via pillager outpost. Pillager outposts generated above ground consist of a huge amount of dark oak logs and the watchtower floor is made of birch planks. However, trying to tear down all the planks is a difficult challenge as the player with early equipment (or none) can easily be killed by the pillagers guarding the outpost. If the pillager outpost generates with a trapped iron golem, you can free the golem. While the golem fights with the pillagers, you can collect wood. If you are lucky to find a single outpost with two or more trapped golems, you have more time to collect wood as more iron golems can survive longer in the outpost before killed by pillagers (due to the fact that pillagers spawn infinitely in and around the outposts).

An alternative tactic is to trap the illagers rather than kill them. This might (needs testing) prevent further Illager spawns, and thus would allow you to collect the wood without being attacked.

## Possibly helpful mods
### Hypothetical mods
The following mods, either individually or in combination, would reduce or eliminate the frustration level of endless desert survival:

- Crafting planks from anything else native to desert, for example from sticks, or sandstone, or lava (cooled!) or obsidian.
- Recycling planks by destroying existing wooden objects (village furniture).

### Addons
For Bedrock Edition, one can modify using behavior pack to edit desert.json in biome folder. Then edit the world_generation_rules.

Default code:

"minecraft:world_generation_rules": {
     "hills_transformation": "desert_hills",
     "mutate_transformation": "desert_mutated",
     "generate_for_climates": [
       [ "warm", 3 ]
     ]
   },

To make an endless desert, change it like this: 

"minecraft:world_generation_rules": { 
     "hills_transformation": "desert_hills",
     "mutate_transformation": "desert_mutated",
     "generate_for_climates": [
       ["medium", 99999999],
       ["warm", 99999999],
       ["cold", 99999999],
       ["frozen", 99999999],
       ["lukewarm", 99999999]
     ]
   }, 

This generates a world with almost endless desert biomes. However, the player usually spawns on little islands (far away from world center), if this happens just teleport to the coordinates 0,0 and start survival in an endless desert. Make sure you teleport higher than Y 60, as this could result in you suffocating.

