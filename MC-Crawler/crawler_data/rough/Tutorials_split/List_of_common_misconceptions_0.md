# List of common misconceptions
This page intends to collect and debunk several commonly-circulated falsehoods regarding game mechanics, blocks, items, and other elements of the Minecraft franchise.

## Contents
- 1 Game mechanics
- 2 Blocks
- 3 Items
- 4 Mobs
- 5 World
- 6 Development
- 7 Technical
- 8 Miscellaneous
- 9 Other media
- 10 References

## Game mechanics
Myth: Obsidian, bedrock, and other blocks normally considered "blast-resistant" can be blown up with large enough amounts of TNT.

- It is not possible to blow up blocks such asobsidianandbedrocksimply by using large amounts of TNT. A sufficiently large explosion power is needed to detonate these blocks, and TNT explosions have a strength of 5 regardless of how many TNT blocks explode within a given range or time.
	- Obsidianwasable to be blown up with TNT in versions beforeAlpha v1.0.14, however. BeforeInfdev 20100618, Obsidian had the same blast resistance as stone and would react as such. FromInfdev 20100618toAlpha v1.0.13_01, Obsidian had a higher blast resistance than stone, but still within the range that TNT can blow up. Alpha 1.0.14 made Obsidian completely TNT resistant.
	- The only way in vanilla Minecraft is using NBT tags to create a sufficient explosion for blowing up blast-resistant blocks.

Myth: Hardness is the same as blast resistance. 

- Hardness and blast resistance arenotthe same. For instance, cobblestone has a blast resistance of 6 and a hardness of 2.
- Hardnessdetermines the time it takes for a block to be broken bymining, andhas nothing to do with explosions.
	- Blocks with higher hardness takes longer to break than blocks with lower hardness, when using the same tool. For example,deepslatehas a hardness of 3, andstonehas a hardness of 1.5, thus deepslate takes longer to break than stone when using the same pickaxe.
	- Additionally, blocks that have different preferred tools but the same hardness takes the same amount of time to break when using their respective tools of the same tier. For example, logs and cobblestone both have a hardness of 2, which means breaking a log with aniron axeand mining a block of stone with aniron pickaxetakes exactly the same amount of time.
- Blast resistance determines the difficulty for a block to be broken in an explosion.
- Two blocks can have the same hardness but different blast resistance, and vice versa. For instance, planks and cobblestone have the same hardness of 2, but cobblestone (6) is much more blast resistant than planks (3).
- In addition, a block with a high hardness can have a lower blast resistance than that of another block with a lower hardness value; ore blocks are a notable example of this.[1]

Myth: In Java Edition, mobs spawn more frequently at lower altitudes.

- It is not the lower altitude that increases the spawn rates of farms built low in the world; instead, it's the lowertotal heightthat the game needs to check in order to spawn a mob. When the total height is lower, mob spawning checks are performed faster, and thus mobs spawn faster.
	- This is why it is recommended to remove the terrain on top of a slime-chunk-based slime farm, as that reduces the total height of the farm. If the myth were true, then removing the terrain on top would have made no difference.
	- This theory can be tested by creating a glass ceiling at world height limit above a mob farm. This decreases the rate of the farm, since the total height of the farm is increased.

Myth: Walking depletes hunger.

- Ever sinceJava Edition 1.11, normal walking does not increase hunger exhaustion at all.
	- However,jumpingstill increases hunger exhaustion. Therefore when hungry, the player should prevent unnecessary jumps, and walk upstairsorslabsif possible, as doing so doesn't deplete hunger.

Myth: Mobs drop more loot if a Looting sword is held in the off-hand.

- The truth is exactly the opposite. Looting can be applied only if the Looting sword is held in themain-hand.
	- Please note that this mechanic is marked as a bug (MC-3304) on Mojang's official bug tracker, meaning it can be fixed at some point.

Myth: Ore blocks drop more experience if mined using a Fortune pickaxe.

- Fortune increases only the yield of items; it does not affect the yield of experience.
	- Similarly, Looting does not affect the amount of experience dropped by mobs.

Myth: Chests, furnaces, shulker boxes, enchanting tables, some other interactive blocks, signs and beds are entities.

- These blocks useblock entities, which are extra data associated with a specific block (for instance, a chest's contents).
- Some of these blocks (chests, trapped chests, ender chests, shulker boxes, enchanting tables, beds, bells) also use block entities for rendering them or parts of them, making them blocks, but rendered as entities. This is also why they disappear in the distance.
- BetweenJava Edition Classic 0.24 SURVIVAL TESTand0.26 SURVIVAL TEST, signs were in fact being tested as entities. InJava Edition Infdev 20100607, they were reimplemented as blocks using the same model.
- Even though they look like blocks,item frames,‌[Java Edition  only]allboats, allminecarts,primed TNT,falling blocks,armor stands,end crystalsandcameras‌[Bedrock Edition and Minecraft Education  only]are still entities.

## Blocks
The missing model is a model, not a block, and is used only by blocks and items with corrupt or flawed model data.
Myth: A "missing texture block" exists in the game.

- There has never existed a central "missing texture block" or "purple error block" inMinecraft: Java Edition. While many blocks and items have used themissing textureat certain points, particularly thelocked chest, these were solely due to texture or model data being undefined for that particular block or item, There has never been a specific block ID reserved for error handling.
- Bedrock Edition does in fact have such a block, however it uses the "update!" texture instead of the iconic missing texture.

Myth: Sugar cane grows to four blocks tall on sand.

- The sugar cane growing code has no checks of the block they stand on. They grow up to three blocks tall. They often appear up to four blocks tall in world generation, which may have caused this rumor to spread, though this occurs on grass and dirt as well, not just sand.

Myth: Sugar cane grows faster on sand than on dirt.

- Sugar canedoes notgrow faster on sand than dirt. The rate of growth is solely based on therandom tickspeed, which has nothing to do with whether sand or dirt is underneath.

Myth: Petrified oak slabs existed in Alpha versions, according to their unofficial nickname, "alpha slabs".

- Petrified oak slabsfirst came into existence inJava Edition Beta 1.3and were craftable up to 1.2.5. The term "alpha slabs", which is commonly used to refer to these blocks, is a misnomer.

Myth: Water cannot exist in the Nether.

- Water can, in fact, be summoned in the Nether using the/setblockand/fillcommands, and once summoned in, it can continue to exist. There have also existed several unintended methods of bringing water into the dimension as well, which have since been patched. The Nether dimension does not forbid the existence of water; it just simply prevents the player from using awater bucket, stopsicefrom melting into water, and prohibits the existence ofwet spongesin placed form.
	- Water can also exist in acauldronin the Nether.

Myth: Torches can break falling sand because it is a non-solid block.

- This sentence is half-true.Falling blocksdrops initem formeven when they fall on solid blocks such assoul sand(MC-77079), and they do not break when they fall through a torch that's not at ground level (MC-3262).
- This is because when a falling block lands on a solid surface, it checks whether it can turn into a block at that location. If the location isoccupied(for example, by a torch), then it cannot become a block, and therefore drops as an item.
	- This is also why soul sand can break falling blocks: when a falling block entity lands on soul sand, it is technically "in" the soul sand, because the soul sand isless than a full block tall, and thus the falling block entity cannot turn into a block at that location (since it's occupied by the soul sand).
- Therefore, it is more accurate to say thatfalling sand can be broken by a torch on top of a solid block, because the torch occupies the space and prevents the falling sand from turning into a block.

Myth: Beacons don't work in the Nether. 

- Beacons, in fact, do work in the Nether; their beams can pass through bedrock. The reason they normally don't work in the Nether is because there are other solid blocks (mostlynetherrack) in the way. If the player removes all the non-bedrock blocks above the beacon, then it can activate normally.
	- Back when beacons were added inJava Edition 1.4.2, their beams actually couldn't go through bedrock; it wasn't untilJava Edition 1.8.2that their beams could go through bedrock, allowing them to be used in the Nether.

Myth: Mycelium prevents all mobs other than mooshroom from spawning.

- It is themushroom fieldsbiome itself that prevents other mobs from spawning there. Hostile mobs can spawn on mycelium in other biomes just like they do on any other solid block.
	- Also, mycelium outside of mushroom fields biomes does not spawn mooshrooms.

Myth: Putting a torch on a monster spawner seals the monster spawner.

- It is thelight levelfrom the torch that prevents the monster spawner from spawning mobs. Therefore, the torch doesn't have to be placed on the spawner itself; it can be put either on the wall or the ground, as long as the entire spawning range of the monster spawner is covered, no mobs can spawn. Light sources other than torches can be used as well.
- Torches also don't necessarily work for monster spawners that have different light level requirements:silverfishandblazescan spawn at light level 11 or lower, so torches with a light level of 14 don't work as well;magma cubescan spawn at any light level, making torches completely useless against them.

Myth: reserved6 served as a placeholder for fire during earlier versions of Pocket Edition.

- In-game testing has confirmed that fire was not replaced by any other block at any point duringPocket Edition's history. Fire's spreading mechanics were simply disabled fromPocket Edition v0.3.3 alphatoPocket Edition v0.6.1 alpha.
- Examination of the save files forPocket Editionworlds from several different versions has also confirmed that reserved6 was a technical block used for referencing inventory slots in the player'shotbar.

