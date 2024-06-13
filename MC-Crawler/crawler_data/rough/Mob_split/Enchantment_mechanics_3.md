### Conflicting enchantments
Some enchantments conflict with other enchantments and thus both can't be enchanted into the same item, effectively taking down the possibility for one to get an overpowered weapon.

The rules for enchantment conflicts are:

- Every enchantment conflicts with itself. (The player can't get a tool with two copies of the Efficiency enchantment)
- All melee damage enchantments (Sharpness,Smite, andBane of Arthropods) conflict with each other. This does not includeImpaling.
- All protection enchantments (Protection,Blast Protection,Fire Protection,Projectile Protection) conflict with each other.
- Silk Touchconflicts withFortune,Looting, andLuck of the Sea, and vice versa. However, Fortune, Looting and Luck of the Sea, does not conflict with each other.
- Depth StriderandFrost Walkerconflict with each other.
- MendingandInfinityconflict with each other.
- Riptideconflicts withLoyaltyandChanneling, but Loyalty does not conflict with Channeling.
- MultishotandPiercingconflict with each other.

Conflicting enchantments may appear on an item with specially-crafted /give commands. The behavior of such items should not be relied upon, but in general:

- An item with multiple copies of the same enchantment uses the level of the first copy of that enchantment in the list.
- For armor with conflicting protection enchantments, all enchantments take effect individually.
- For weapons with conflicting damage enchantments, all enchantments take effect individually.
- For tools with both Silk Touch and Fortune, Silk Touch takes priority over Fortune on blocks affected by both enchantments. Fortune still applies to blocks such as crops that are not affected by Silk Touch.
- For bows with both Mending and Infinity, both enchantments work individually.
- For tridents with both Loyalty and Riptide, Riptide still functions normally but the trident can no longer be thrown by the player. However, tridents can still be thrown using dispensers.‌[Bedrock Edition  only]
- For crossbows with both Multishot and Piercing, both enchantments work individually.

A chart showing all possible enchantments on diamond tools.[needs updating]
## Enchanting seed
The enchantments that the enchanting table offers to a player do not usually change until the player enchants an item.
After each applied enchant, the player gets offered different enchantments for any type of enchantable item.

This is controlled by the enchanting seed XpSeed in the player data.

### Deterministic initial enchantment
This enchantment seed is initialized to 0 on world creation, and whenever the last enchantment seed was 0 on loading into a world it is re-rolled.[1]
Hence, when a new world is played until the player performs their first enchant without closing and re-joining the world in between, the offered enchantments are always the same.
They still depend on the enchanted item and the enchantment level.

These deterministic enchantments with the XpSeed equal to 0, colloquially know as first enchants, can be used to guarantee certain enchantments, e.g. a diamond sword enchanted with 3 lapis lazuli and 15 bookshelves always gets Unbreaking 3 and Looting 2.

Due to the fact that enchanting an item changes the enchanting seed, only one such first enchant can be chosen per world.


