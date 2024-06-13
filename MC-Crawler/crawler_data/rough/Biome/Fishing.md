# Fishing
Fishing is the use of a fishing rod to obtain items, usually fish.

## Contents
- 1 Catching fish
- 2 Junk and treasure
	- 2.1 Notes
- 3 Fishing rod durability
- 4 History
- 5 Issues
- 6 Trivia

## Catching fish
A fishing bobber in Bedrock Edition.
A newly obtained fishing rod with the enchantments Lure II, Unbreaking III and Luck of the Sea II.
To fish, the player must use a fishing rod to cast the line into a body of water. The player's position does not matter; the player can be in the water, underwater, sitting in a boat, or standing on adjacent land. The depth, size or origin (player-created or generated) of the body of water has no effect on the player's ability to fish in it, but some of these parameters may affect wait times and the possibility of catching treasure; see below.

Once the bobber hits water, the wait time is determined, and the player must wait for a random period between 5 and 30 seconds (100 to 600 ticks at 20 ticks per second) before the hook catches something. Small splashes can be seen around the bobber while it is in the water.

- Each level of theLureenchantment on a fishing rod subtracts 5 seconds from both the minimum and maximum wait time. If it causes the wait time to be less than 0, a new wait time is generated in the next tick.
- If the bobber is not directly exposed tosunormoonlight, the wait time is approximately doubled (each tick has a 50% chance of not decrementing the count). For direct exposure, allblocksabove the bobber must betransparentto sunlight, such asglassandcarpet. Blocks that diffusesky light(such asiceandleaves) negate direct exposure. The presence ofcloudsorrainfallhas no effect on direct exposure.
- If the bobber's block is being rained on, the wait time is reduced by approximately1⁄4(each tick has a 25% chance of counting down 2 instead of 1). The bobber must be located in abiomewhere it is currently raining and all blocks above it must not block movement (e.g.torch,tripwire).

After the wait period has passed, a trail of fishing particles appear, approaching the bobber in a serpentine path (provided that the Particles Video Setting is not set to Minimal). After 1 to 4 seconds the particles reach the bobber, the bobber dips below the surface, and the player has a approximately half a second‌[Bedrock Edition  only] or evenly-distributed one to two seconds‌[Java Edition  only] to reel in the line before the waiting time resets. Removing the bobber from water during this interval secures the caught item on the line.

Upon a successful reel-in:

- Araw cod,raw salmon,pufferfish,tropical fish, junk, or a treasure item appears (seejunk and treasurebelow), flies toward the player, and is added to the player's inventory. If the player'sinventoryis full, the item drops on the ground. While the item normally flies directly to the player's position, the item may hit blocks positioned between the bobber and the player, causing it to bounce off at an angle. Sudden player movement may also cause the item to miss the player entirely.
- The rod's durability is reduced by 1 point. This can vary depending on the circumstances; seebelow.
- Anexperience orbworth 1–6 experience points spawns at the position of the player. Consequently, aMending-enchantedfishing rodused only for fishing never wears out, repairing itself if damaged.

If the player wanders more than 32 blocks away from the bobber, or if the player stops holding the fishing rod, the bobber and fishing line disappear with no durability reduction to the rod.

The bobber floats up to the water's surface even if the fishing rod is used from underwater unless it hooks onto a mob such as squid or is obstructed by a block.

Fish mobs do not attempt to bite the fish hook and bobber, but can be hooked and reeled as with other mobs.

## Junk and treasure
The fishing rod can occasionally catch treasure or junk instead of fish. A fishing rod without the Luck of the Sea enchantment has an 85% chance of catching fish, a 10% chance of catching junk, and a 5% chance of catching treasure. Each level of the Luck of the Sea enchantment increases the chance of catching a treasure at the expense of reducing the chances of catching fish and junk. The Luck status effect grants the same benefit.

To catch items in the treasure category, the bobber must be in open water, defined as the 5×4×5 vicinity around the bobber resting on the water surface (2 blocks away horizontally, 2 blocks above the water surface, and 2 blocks deep). Each horizontal layer in this area must consist only of air and lily pads or water source blocks, waterlogged blocks without collision (such as signs, kelp, or coral fans), and bubble columns. These conditions are checked every tick to determine if the player is eligible to receive treasure from a fishing attempt. If the conditions are not met, only items in the fish and junk categories can be obtained from fishing.

| Category               | Chance in category[note 2] | Unenchantedchance | LotS 1 | LotS 2 | LotS 3 |
|------------------------|----------------------------|-------------------|--------|--------|--------|
| Fish                   | Weight                     | 85%               | 84.8%  | 84.7%  | 84.5%  |
| Raw cod                | 60%                        | 51.0%             | 50.9%  | 50.8%  | 50.7%  |
| Raw salmon             | 25%                        | 21.3%             | 21.2%  | 21.2%  | 21.1%  |
| Tropical fish          | 2%                         | 1.7%              | 1.7%   | 1.7%   | 1.7%   |
| Pufferfish             | 13%                        | 11.1%             | 11.0%  | 11.0%  | 11.0%  |
| Treasure               | Weight                     | 5%                | 7.1%   | 9.2%   | 11.3%  |
| Bow[note 3]            | $16.7% (\frac{1}{6}$)      | 0.8%              | 1.2%   | 1.5%   | 1.9%   |
| Enchanted book[note 4] | $16.7% (\frac{1}{6}$)      | 0.8%              | 1.2%   | 1.5%   | 1.9%   |
| Fishing rod[note 3]    | $16.7% (\frac{1}{6}$)      | 0.8%              | 1.2%   | 1.5%   | 1.9%   |
| Name tag               | $16.7% (\frac{1}{6}$)      | 0.8%              | 1.2%   | 1.5%   | 1.9%   |
| Nautilus shell         | $16.7% (\frac{1}{6}$)      | 0.8%              | 1.2%   | 1.5%   | 1.9%   |
| Saddle                 | $16.7% (\frac{1}{6}$)      | 0.8%              | 1.2%   | 1.5%   | 1.9%   |
| Junk                   | Weight                     | 10%               | 8.1%   | 6.1%   | 4.1%   |
| Lily Pad               | 17%                        | 1.7%              | 1.4%   | 1.0%   | 0.7%   |
| Bowl                   | 10%                        | 1.0%              | 0.8%   | 0.6%   | 0.4%   |
| Fishing rod[note 5]    | 2%                         | 0.2%              | 0.2%   | 0.1%   | 0.1%   |
| Leather                | 10%                        | 1.0%              | 0.8%   | 0.6%   | 0.4%   |
| Leather boots[note 5]  | 10%                        | 1.0%              | 0.8%   | 0.6%   | 0.4%   |
| Rotten flesh           | 10%                        | 1.0%              | 0.8%   | 0.6%   | 0.4%   |
| Stick                  | 5%                         | 0.5%              | 0.4%   | 0.3%   | 0.2%   |
| String                 | 5%                         | 0.5%              | 0.4%   | 0.3%   | 0.2%   |
| Water bottle           | 10%                        | 1.0%              | 0.8%   | 0.6%   | 0.4%   |
| Bone                   | 10%                        | 1.0%              | 0.8%   | 0.6%   | 0.4%   |
| Ink Sac(10)            | 1%                         | 0.1%              | 0.1%   | 0.1%   | 0.04%  |
| Tripwire Hook          | 10%                        | 1.0%              | 0.8%   | 0.6%   | 0.4%   |

| Category               | Chance in category[note 2]                   | Unenchantedchance                   | LotS 1                              | LotS 2                              | LotS 3                                |
|------------------------|----------------------------------------------|-------------------------------------|-------------------------------------|-------------------------------------|---------------------------------------|
| Fish[note 7]           | Weight                                       | 85%                                 | 84.8%                               | 84.7%                               | 84.5%                                 |
| Raw salmon             | 40%‌[BE  only]                               | 34.0%‌[BE  only]                    | 33.9%‌[BE  only]                    | 33.9%‌[BE  only]                    | 33.8%‌[BE  only]                      |
| Junk                   | Weight                                       | 10%                                 | 8.1%                                | 6.1%                                | 4.1%                                  |
| Lily Pad               | $14.2% ()‌15.5% (\frac{17}{110}$)‌[JE  only] | 1.4%‌[BE  only]<br/>1.5%‌[JE  only] | 1.1%‌[BE  only]<br/>1.2%‌[JE  only] | 0.9%                                | 0.6%                                  |
| Bamboo                 | $8.3% ()‌9.1% (\frac{10}{110}$)‌[JE  only]   | 0.8%‌[BE  only]<br/>0.9%‌[JE  only] | 0.7%                                | 0.5%‌[BE  only]<br/>0.6%‌[JE  only] | 0.3%‌[BE  only]<br/>0.4%‌[JE  only]   |
| Cocoa Beans‌[BE  only] | $8.3% (\frac{10}{120}$)                      | 0.8%                                | 0.7%                                | 0.5%                                | 0.3%                                  |
| Bowl                   | $8.3% ()‌9.1% (\frac{10}{110}$)‌[JE  only]   | 0.8%‌[BE  only]<br/>0.9%‌[JE  only] | 0.7%                                | 0.5%‌[BE  only]<br/>0.6%‌[JE  only] | 0.3%‌[BE  only]<br/>0.4%‌[JE  only]   |
| Fishing rod[note 5]    | $1.7% ()‌1.8% (\frac{2}{110}$)‌[JE  only]    | 0.2%                                | 0.2%                                | 0.1%                                | 0.1%                                  |
| Leather                | $8.3% ()‌9.1% (\frac{10}{110}$)‌[JE  only]   | 0.8%‌[BE  only]<br/>0.9%‌[JE  only] | 0.7%                                | 0.5%‌[BE  only]<br/>0.6%‌[JE  only] | 0.3%‌[BE  only]<br/>0.4%‌[JE  only]   |
| Leather Boots[note 5]  | $8.3% ()‌9.1% (\frac{10}{110}$)‌[JE  only]   | 0.8%‌[BE  only]<br/>0.9%‌[JE  only] | 0.7%                                | 0.5%‌[BE  only]<br/>0.6%‌[JE  only] | 0.3%‌[BE  only]<br/>0.4%‌[JE  only]   |
| Rotten Flesh           | $8.3% ()‌9.1% (\frac{10}{110}$)‌[JE  only]   | 0.8%‌[BE  only]<br/>0.9%‌[JE  only] | 0.7%                                | 0.5%‌[BE  only]<br/>0.6%‌[JE  only] | 0.3%‌[BE  only]<br/>0.4%‌[JE  only]   |
| Stick                  | $4.2% ()‌4.5% (\frac{5}{110}$)‌[JE  only]    | 0.4%‌[BE  only]<br/>0.5%‌[JE  only] | 0.3%‌[BE  only]<br/>0.4%‌[JE  only] | 0.3%                                | 0.2%                                  |
| String                 | $4.2% ()‌4.5% (\frac{5}{110}$)‌[JE  only]    | 0.4%‌[BE  only]<br/>0.5%‌[JE  only] | 0.3%‌[BE  only]<br/>0.4%‌[JE  only] | 0.3%                                | 0.2%                                  |
| Water Bottle           | $8.3% ()‌9.1% (\frac{10}{110}$)‌[JE  only]   | 0.8%‌[BE  only]<br/>0.9%‌[JE  only] | 0.7%                                | 0.5%‌[BE  only]<br/>0.6%‌[JE  only] | 0.3%‌[BE  only]<br/>0.4%‌[JE  only]   |
| Bone                   | $8.3% ()‌9.1% (\frac{10}{110}$)‌[JE  only]   | 0.8%‌[BE  only]<br/>0.9%‌[JE  only] | 0.7%                                | 0.5%‌[BE  only]<br/>0.6%‌[JE  only] | 0.3%‌[BE  only]<br/>0.4%‌[JE  only]   |
| Ink Sac(10)            | $0.8% ()‌0.9% (\frac{1}{110}$)‌[JE  only]    | 0.1%                                | 0.1%                                | 0.1%                                | 0.03%‌[BE  only]<br/>0.04%‌[JE  only] |
| Tripwire Hook          | $8.3% ()‌9.1% (\frac{10}{110}$)‌[JE  only]   | 0.8%‌[BE  only]<br/>0.9%‌[JE  only] | 0.7%                                | 0.5%‌[BE  only]<br/>0.6%‌[JE  only] | 0.3%‌[BE  only]<br/>0.4%‌[JE  only]   |

[note 3]

#### Notes
1. ↑ a bThe percentages in this table are in most places rounded for clarity.
2. ↑ a bThis does not vary depending on enchantments.
3. ↑ a b cBows and fishing rods caught from the Treasure category are enchanted at a random level between 22-30, but also badly damaged. Enchantment probabilities are the same as a level-30 enchantment on an enchanting table. These can also include treasure enchantments that are unavailable via an enchanting table.
4. ↑Enchantment probabilities are the same as a level-30 enchantment on an enchanting table, but the chance of multiple enchantments is not reduced. These can also include treasure enchantments that are unavailable via an enchanting table. However, the enchantments Swift Sneak and Soul Speed can not be obtained this way.
5. ↑ a b c dFishing rods and leather boots caught from the junk category are 10%–100% damaged, and always unenchanted.
6. ↑This table presents the loot possibilities that differ from the above table for a player fishing in one of the following biomes: jungle, sparse jungle, and bamboo jungle. Items listed in the above table but not the table below remain unchanged regardless of the biome in which the player is fishing.
The percentages for Unenchanted chance and Luck of the Sea of Junk item may be inaccurate.
7. ↑In Bedrock Edition, cod and salmon are the only fish that can be caught in jungle biomes and variants.

## Fishing rod durability
See also: Fishing Rod § Usage

The fishing rod has 64 units of durability in Java Edition and 384 units in Bedrock Edition. Each use costs 1 point, and the rod breaks when all durability is consumed. The number of uses can be increased if the Unbreaking or Mending enchantments are applied. 

- Reeling in while the bobber is in the air or in the water with nothing caught on it costs no durability.
- Reeling in and successfully catching fish, junk, or treasure costs 1 durability.
- Reeling in while the bobber is stuck in a solid block costs 2 durability.
- Reeling in a dropped item costs 3 durability.
- Reeling in an entity that is not a dropped item costs 5 durability.
- A fishing rod with theMendingenchantment has effectively infinite durability from incrementally repairing itself if used for fishing only, and the player isn't wearing damaged Mending armor or holding a damaged Mending item in the offhand.

The durability cost is subtracted on reel-in, rather than on hooking. Therefore, no penalty is levied for switching to another item or dropping the rod instead of reeling in.

