### Custom superflats
See also: Java Edition Custom Superflat

There is an NBT string in every level.dat file called "FlatWorldLayers", which when edited properly, can cause the respective world to generate custom layers. This is used when Custom Superflats created on Legacy Console Edition get converted over to Bedrock Edition.

Custom Superflats can, nevertheless, still be created without cheats through custom world folders.

### Single Biome world type
See also: Java Edition Single Biome

Similar to Custom Superflats, there is code in the game files for single biome worlds. It is fully functional but has many issues.

## Other
### Fifth giant tree taiga biome variants
The file biome_client.json contained a biome name that never existed in game.

"mega_taiga": {
      "water_surface_color": "#2d6d77",
      "water_fog_color": "#2d6d77"
    },
    "mega_spruce_taiga": {
      "water_surface_color": "#2d6d77",
      "water_fog_color": "#2d6d77"
    },
    "mega_taiga_mutated": {
      "water_surface_color": "#2d6d77",
      "water_fog_color": "#2d6d77"
    },
    "mega_spruce_taiga_mutated": {
      "water_surface_color": "#2d6d77",
      "water_fog_color": "#2d6d77"
    },
    "mega_taiga_hills": {
      "water_surface_color": "#286378",
      "water_fog_color": "#286378"
    },

Out of the five giant tree taiga biomes, only four can generate in the game while another one, mega_taiga_hills, appears only in this code, as that biome is not defined in the vanilla behavior pack in the biomes folder. Whether the biome is a dropped feature or not is unknown.

Colors:  #2d6d77  #286378

### World settings
level.dat contains several player abilities. Most of these are used in multiplayer, to determine who has what permissions. However, some are completely inaccessible without an NBT editor. With the exception of permissionsLevel, none of these settings can be altered in-game for the world itself, only for individual players. The flying changes in-game as players toggle flight mode, but cannot be altered manually without editing.

| Ability        | Description                                                                                                                     |
|----------------|---------------------------------------------------------------------------------------------------------------------------------|
| `instabuild`   | Whether the player can break blocks instantly. Normally true in Creative.                                                       |
| `invulnerable` | Whether the player is immune to damage. This immunity also affects`/kill`[needs testing]andthe void. Normally true in Creative. |
| `lightning`    | Depends if lightning appears in thunderstorms.                                                                                  |
| `flyspeed`     | The speed at which the player flies in Creative.[more information needed]                                                       |
| `walkspeed`    | The speed at which the player walks.[more information needed]                                                                   |

## Entities
### Armed zombie villager
The zombie villager was added, but it cannot spawn with armor equipped. However, armed zombie villagers are still spawnable via mob editing.
If a zombie villager is wearing armor, the helmet is struck through the head, the chestplate and leggings can be seen through holes in their clothes, while the boots look normal.

### Wither skeleton archer
If a wither skeleton is equipped with a bow, it uses it as a ranged weapon, and arrows shot are always set on fire regardless of what enchantment it has, or if it has an enchantment. However, wither skeleton archers cannot spawn naturally.

Minecraft Dungeons has wither skeleton archers.

### Wither jockey

Spiders spawned in the Nether have a 1% chance of spawning while being ridden by a skeleton, which has an 80% of being a wither skeleton and a 20% of a normal skeleton. However, since spiders cannot naturally spawn in the Nether, this mob is unused. Instead, it can be spawned using spider spawn eggs in Creative mode. Wither jockeys also have a cave spider variant. It can also be spawned with commands.

### Zombie horse
Zombie horses can be spawned only by using its spawn egg or /summon, as it cannot spawn naturally.

### 
These jockeys (see below) are unused since zombie horses cannot spawn naturally.

- Zombie horse jockey
	- Baby zombie riding zombie horse
- Husk zombie horse jockey
	- Baby husk riding zombie horse
- Zombie villager riding zombie horse jockey
	- Baby zombie villager riding zombie horse

### Baby trader llama
Trader llamas were added in beta 1.11.0.1, which at that time were breedable and could spawn a baby. However, as of beta 1.11.0.3, trader llamas no longer spawn naturally as babies since they are no longer breedable, causing the baby trader llama to become unused.

### Ravagers
Some Ravager with riders do not spawn naturally and must be summoned using /summon:

- Vindicatorriding Ravager
- Pillager Captainriding Ravager
- Vindicator Captainriding Ravager

### Agent

Main article: Agent
The agent was added in alpha 0.17.0.1, although it was hidden in the .apk file of the game. However, it is still used in conjunction with Code Connection.



### Camera
Main article: Camera

The camera was first found in the Pocket Edition v0.1.0 alpha .apk file, as of this version, the camera has functionality. 

As of v0.9.0, the camera entity was removed. Tommaso stated "It doesn't mean that it's dead forever, in fact, I have a lot of ideas for it! I think it will be back when have shaders, sharing and redstone."[3]

The camera was re-added in alpha v0.14.0, accessible only with inventory editors, but was removed again in alpha v0.16.0. However, the block can still be obtained in servers.

Cameras were added again in beta 1.8.0.8, but it requires mob editing to summon it or using an NBT editor to get its spawn egg. The camera can now be obtained using /give as of beta 1.12.0.2.

In beta 1.13.0.1, this item can be used by slide while using the item, the take picture sound can be heard and an explosion can be seen and a picture is saved to LocalState/screenshots folder on Windows 10 or /storage/emulated/0/screenshots folder on Android. However, Cameras are no longer obtainable using /give

As of beta 1.16.100.54, Cameras are once again obtainable using /give. It was reverted again in beta 1.16.100.58

### Old villager
See also: Villager/Before Village and Pillage

Old villagers, prior to the Village and Pillage update are still available in the game, but they are instantly converted into villager_v2 (new villagers).
Their spawn egg can be obtained only via /give spawn_egg 1 15. However, trying to spawn them with that spawn egg spawns an old villager who is instantly killed. A new villager then spawns and take its place.

Their trade tables were not removed, even though trading GUI has changed between Village and Pillage and prior updates.

