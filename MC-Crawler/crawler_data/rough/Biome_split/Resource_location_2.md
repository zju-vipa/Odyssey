## Namespaces
|  | “ | This isn't a new concept, but I thought I should reiterate what a "namespace" is. Most things in the game has a namespace, so that if we add something and a mod (or map, or whatever) adds something, they're both different somethings. Whenever you're asked to name something, for example a loot table, you're expected to also provide what namespace that thing comes from. If you don't specify the namespace, we default to minecraft. This means that something and minecraft:something are the same thing. | „ |
|--|---|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
|  |   | — Dinnerbone on namespaces[4]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |   |

A namespace is a domain for content. It is to prevent potential content conflicts or unintentional overrides of objects of the same name.

For example, two data packs add two minigame mechanisms to Minecraft; both have a function named start. Without namespaces, these two functions would clash and the minigames would be broken. When they have different namespaces of minigame_one and minigame_two, the functions would become minigame_one:start and minigame_two:start, which no longer conflict.

### minecraft namespace
Minecraft reserves the minecraft namespace. When a namespace is not specified, a resource location falls back to minecraft‌[Java Edition  only]. As a result, the minecraft namespace should only be used by content creators when the content needs to overwrite or modify existing Minecraft data, such as adding a function to the minecraft:load function tag.

### Custom namespace
The namespace should be distinct for different projects or content creations (e.g. a data pack, a resource pack, a mod, backing data/resource packs for a custom map, etc.)

To prevent potential clashes, the namespace should be as specific as possible.

- Avoidalphabet soups. For example, a project named "nuclear craft" should not use the namespacenc, as this is too ambiguous.
- Avoid words that are too vague.battle_royalewould not be informative to look up as well, butplayer_name_battle_royalewould be much better.

In either case, these poorly chosen namespaces reduce the exposure of a project and bring difficulties for debugging when there are multiple content creations applied to the game.

### Other built-in namespaces

  

This feature is exclusive to  Java Edition. 


The vanilla Minecraft resource pack declares Realms-oriented language files in the realms namespace (located at assets/realms/lang/.json) and game-related language files in the minecraft namespace, even though translation keys are not resource locations. The realms jar itself also declares its en_us.json language file and its various textures in the realms namespace.

In the IDs of command argument types, a brigadier namespace also appears for command argument types that are native to Brigadier.


