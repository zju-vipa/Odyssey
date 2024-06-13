### Items
Armors
- Now can be visually customized with a variety of unique trims at thesmithing table.
- Purely visual with no gameplay benefits, and can only be applied tohelmets,chestplates,leggingsandboots.
	- All trim patterns are visually the same on an armor's item icon, but the color will still change based on the trim material.
	- The name of the trim pattern will be displayed on the item's tooltip.
- Armor trim has 2 properties: pattern and material.
	- Pattern: Defined by the smithing template used to apply the trim, and represents the visual pattern of the trim.
	- Material: Defined by what ingredient is used to apply the trim, and represents the color of the trim.
		- Available ingredients:
			- Amethyst Shard
			- Copper Ingot
			- Diamond
			- Emerald
			- Gold Ingot
			- Iron Ingot
			- Lapis Lazuli
			- Nether Quartz
			- Netherite Ingot
			- Redstone Dust

Map
- The color forblack terracottanow matchesJava Edition.

Shields
- Can now be combined with aBannerin a crafting menu to apply its pattern on it.
	- The banner is consumed on use.
	- A Shield can be combined with a Banner only if no pattern was previously applied.



### Mobs
Elder guardian
- DropsTide Armor Trimupon death.

### Non-mob entities
- Experience Orbs now merge when spawned with the summon command.

### World generation
Ancient City
- Chests now containWard Armor TrimandSilence Armor Trim.

Bastion Remnant
- Chests now containNetherite UpgradeandSnout Armor Trim.

Desert Pyramid
- Chests now containDune Armor Trim.
- Now includes a new room filled withsandandsuspicious sand.
	- Some sand will appear exposed, and can be found at the same height asblue terracotta.
	- Suspicious sandis visible on the top layer of the newly added room.
- In the suspicious sand, the player can find:
	- Diamond
	- Emerald
	- Tnt
	- Gunpowder
	- Archer Pottery Sherd
	- Miner Pottery Sherd
	- Prize Pottery Sherd
	- Skull Pottery Sherd

Desert Well
- Now includes suspicious sand underwater.
- In the suspicious sand, the player can find:
	- Brick
	- Stick
	- Emerald
	- Suspicious Stew
	- Arms up Pottery Sherd
	- Brewer Pottery Sherd

End City
- Chests now containSpire Armor Trim.

Jungle Temple
- Chests now containWild Armor Trim.

Nether Fortress
- Chests now containRib Armor Trim.

Ocean Ruins (cold)
- Now includesuspicious gravelblocks.
- In the suspicious gravel, the player can find:
	- Emerald
	- Iron axe
	- Coal
	- Gold Nugget
	- Wheat
	- Wooden hoe
	- Blade Pottery Sherd
	- Explorer Pottery Sherd
	- Mourner Pottery Sherd
	- Plenty Pottery Sherd

Ocean Ruins (warm)
- Now includesuspicious sandblocks.
- In the suspicious sand, the player can find:
	- Wooden hoe
	- Emerald
	- Coal
	- Gold Nugget
	- Wheat
	- Angler Pottery Sherd
	- Shelter Pottery Sherd
	- Snort Pottery Sherd

Pillager Outpost
- Chests now containSentry Armor Trim.

Shipwreck
- Chests now containCoast Armor Trim.

Stronghold
- Chests now containEye Armor Trim.

Woodland mansion
- Chests now containVex Armor Trim.

### Gameplay
Effect
- Distinct green particles are now emitted by the player under effect of Hero of the Village status effect.

Smithing Table functionality
- Overhauled. It is now a workstation for physical equipment upgrades and modifications.
- Added a slot used by smithing templates to the left of the old 2 slots.
- Smithing templates define what type of upgrade that will be making to equipment.
	- It specifies both what type of items that can upgrade, and which ingredients are valid to customize the upgrade.
- Netherite equipment crafting now also requires a netherite upgrade smithing template.

General
- Fixed fall damage accumulating when player jumps on roofed Soul Sand Bubble Column

### General
Accessibility
- The four Creative Inventory tabs now have their names read out by text-to-speech.
- Screen reader now properly reads description in popping window after disabling “Require Encrypted Websockets” and “Allow mobile data for online play”.

Controls
- Fixed issues with keyboard navigation on some menu screens on iOS, iPadOS, and Android.

Sounds
- The sounds emitted by players and mobs stepping, falling, jumping, or landing on top of Sculk Sensors are now affected by the "Players" sound slider.

Stability & Performance
- Game no longer crashes when an item starts/stops being used if the item is not available

User interface
- Multiplayer toggle in the Create New World screen will now always gray out if the setting would have no effect.
- Respawning in VR no longer softlocks the player in the death screen.
- Text shadowboxes now have the correct opacity on interactable block screens.
- Updated the seed picker with a Cherry Grove biome option.



Title Screen
- Thepanoramawas changed to showcase acherry grovebiome.
- The panorama now rotates clockwise.

## Fixes
97 issues fixed
- MCPE-35202– Fireball is not correctly positioned when shot by ghast
- MCPE-39974– lava_cauldron can be placed via commands
- MCPE-41221– Off-hand Shield in third person view is upside down
- MCPE-62041– Lantern cannot be placed on the bottom of a grindstone
- MCPE-64745– Iron bars and glass panes do not connect with any kind of pistons
- MCPE-104717– Weeping vines cannot be placed underneath some blocks
- MCPE-116102– Some blocks should not support pointed dripstone
- MCPE-116145– Pointed dripstone cannot be placed on some blocks
- MCPE-118898– Moon Lighting Originates From The Opposite Angle Relative To The Moon At Night Underwater
- MCPE-122403– Glow berries (cave vines) cannot be placed underneath some blocks
- MCPE-122613– Glow lichen and sculk vein cannot be placed on some blocks
- MCPE-122624– Glow lichen and sculk vein doesn't need to be placed on some blocks
- MCPE-122634– Roots cannot be placed underneath some blocks
- MCPE-125931– Dead bushes cannot be placed on grass block
- MCPE-133778– Dyes and glow ink sacs are consumed when used on a sign with no text
- MCPE-141124– Inactive scroll buttons can still play scroll sounds
- MCPE-141154– Amethysts should not be placed on some blocks (vanilla parity)
- MCPE-147711– Arrows don't appear in the Character Creator while the Hide Controller Hints setting is on
- MCPE-152485– Falling or flying through floating water sometimes doesn't reset fall damage
- MCPE-152926– Door top and bottom textures flip incorrectly & illogically when opened and closed
- MCPE-153909– Filter "has_equipment" cannot test for an empty string ("") or air
- MCPE-156331– The title on the Behavior pack dialogue box is not capitalized correctly
- MCPE-156773– Weighted pressure plates always output signal strength 1 for 1/2 second before they output the correct signal strength
- MCPE-159261– Loading animation is to big when adding friend
- MCPE-159970– Command block menu missing command block texture (icon)
- MCPE-161096– Sugar cane generates in water
- MCPE-162455– "World upload failed" when I save and quit to the title screen
- MCPE-163328– Mobs sit too low on the raft
- MCPE-163337– Hanging signs allow more characters than on Java
- MCPE-163399– Greek Mythology Mashup / Items in Frames
- MCPE-163416– Bamboo fence gate are not flammable
- MCPE-163475– Can't see camel dash bar on mobile
- MCPE-163501– Camel neck appeared when it up and sniff the ground.
- MCPE-163554– Hanging Sign Sounds are Very Quiet
- MCPE-164246– Hanging nether and bamboo signs don't have new sounds
- MCPE-164249– Arrows and tridents get stuck shaking when shot at Hanging Signs
- MCPE-164424– "minecraft:boostable" component has no effect on speed
- MCPE-164632– Hanging signs placement is not like in Java
- MCPE-164677– Standing on top of some incomplete blocks as it converts to complete blocks causes the player to fall through or be pushed out of the block
- MCPE-164719– The camel's head looks high up disturbing the player's eyesight
- MCPE-165962– Some splashes are written without "!" in Bedrock
- MCPE-166505– Camels has an error text in action hint
- MCPE-166791– Black terracotta uses white terracotta map color
- MCPE-167045– Player collision box incorrect after returning to main menu from death screen
- MCPE-167064– Chicken Spawn Egg appears as Sea Turtle Spawn Egg with Sniffer experiment turned on
- MCPE-167163– When Suspicious Sand is dropped onto some blocks, it drops
- MCPE-167176– Torchflowers placed by the player do not have a random location in the block
- MCPE-167177– The hitbox of Torchflowers seeds is too big and not the same as in Java
- MCPE-167193– Sniffer digging doesn't have digging particles playing
- MCPE-167200– Torchflower seeds cannot be composted
- MCPE-167217– Using pick block function on torchflower crop gives torchflower seeds instead of the plant item
- MCPE-167220– Bees are not tempted by or attempt to pollinate Torchflowers
- MCPE-167263– Brush's durability are used up incorrectly
- MCPE-167264– Enchantments cannot be applied to the brush
- MCPE-167910– Sand doesn't generate in the bottom of desert well, and the amount of suspicious sand in desert well doesn't match Java Edition
- MCPE-167975– Chickens and parrots are not tempted by torchflower seeds
- MCPE-167977– Torchflowers cannot be used to craft suspicious stew
- MCPE-168041– Placement of blocks on a Decorated pot is not the same as in Java
- MCPE-168047– State of the hanging signs under the Decorated pot does not correspond to the Java
- MCPE-168055– State of the hanging signs under the Decorated pot does not correspond to the Java
- MCPE-168075– Cherry groves can generate regular flowers
- MCPE-168280– Unable to place blocks on interactable blocks when sneaking
- MCPE-168357– Potions and tipped arrow colors don't match the particles
- MCPE-168367– /inputpermission doesn't have description in the autocomplete
- MCPE-168387– Woodland mansion, wooden logs face the wrong way
- MCPE-168390– Black boxes around non full blocks in third person view
- MCPE-168409– BlockPermutation.matches() and blockPermutation.withProperty() methods do not work with custom blocks. Script API
- MCPE-168548– Interaction with the armor stand depends on whether the player is sneaking or not, and not on pressing the shift button
- MCPE-168558– Stars show up too early and appear black with RTX on
- MCPE-168717– Stone Block Slab Recipe Duplication Content Log Errors and they are NOT Dupes
- MCPE-168805– Some brushing sounds missing
- MCPE-168807– Interacting with a waxed sign / hanging sign doesn't play a sound
- MCPE-168817– Reloading the world causes signs and hanging signs to use incorrect texture in editing screen
- MCPE-168818– Sign editing screen ignores added effects
- MCPE-168829– Glitched tall grass block can generate inside or above pink petal flowers
- MCPE-168834– Decorated pot is missing top row of pixels
- MCPE-168836– Shelter Pottery Shard is missing a space in its name
- MCPE-168838– Interacting with editable signs when holding certain items can break the sign or trigger item-specific interactions
- MCPE-168856– The loot table for suspicious blocks generated in trail ruins has two identical entries for bricks
- MCPE-168869– Trail Ruins structure aren't completely buried underground
- MCPE-168894– Game crashes when enabling RTX while in a world
- MCPE-168908– Minecraft for ChromeOS cursor sensitivity
- MCPE-168921– Miner pottery shard cannot be obtained by brushing suspicious sand in desert pyramid
- MCPE-168934– Raiser and Wayfinder smithing template texture are offset by 1 Pixel
- MCPE-168999– Flight mode is disabled when flying under stairs
- MCPE-169038– Woodland mansion entrance uses smooth stone slabs
- MCPE-169141– You can't plant bamboo on suspicious gravel
- MCPE-169142– Can't plant bamboo, cactus, sugar cane and dead bush on suspicious sand
- MCPE-169304– Suspicious sand and gravel do not have assigned any tools
- MCPE-169348– Sculk vibration frequencies haven't been updated
- MCPE-169422– Pink petals always drop one when using silk touch tools, regardless of how many amounts of them
- MCPE-169423– Z-fighting occurs on the sniffers' heads and ears
- MCPE-169563– Sculk shriekers aren't muted/silenced when waterlogged
- MCPE-169567– Bees still make player eat sound
- MCPE-169607– Torchflowers cannot be used to feed brown mooshrooms
- MCPE-169760– Pottery shard names do not rename "Pottery Sherd" to match like Java Edition
- MCPE-170184– Trade Tables no longer support custom entity Spawn Eggs


