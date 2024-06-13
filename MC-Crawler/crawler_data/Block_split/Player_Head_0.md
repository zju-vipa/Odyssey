# Player Head
A player head is a block modeled after the head of a player (Steve by default). Player heads cannot be obtained in Survival.

## Contents
- 1 Obtaining
	- 1.1 Breaking
- 2 Usage
	- 2.1 Decoration
	- 2.2 Wearing
	- 2.3 Dispensers
	- 2.4 Enchantments
- 3 Player skins
	- 3.1 Marc's Head Format
- 4 Sounds
	- 4.1 Generic
	- 4.2 Unique
- 5 Data values
	- 5.1 ID
	- 5.2 Metadata
	- 5.3 Item data
	- 5.4 Block states
	- 5.5 Block data
- 6 History
- 7 Issues
- 8 Trivia
- 9 Gallery
	- 9.1 Screenshots
	- 9.2 Development images
- 10 References

## Obtaining
### Breaking
A player head can be mined using any item,[1] and drops itself when broken.

| Block    | Player Head         |
|----------|---------------------|
| Hardness | 1                   |
|          | Breakingtime (secs) |
| Default  | 1.5                 |

If a player head is pushed by a piston or comes in contact with water or lava, it breaks off as an item.

When destroyed by an explosion, the player head always drops as an item.

## Usage
### Decoration
Player heads can be oriented in 16 different directions on top of a block, and 4 directions on the sides of blocks, similar to signs. They can be placed on top of, or beside each other by shift clicking.

### Wearing
The player can wear player heads, similarly to pumpkins or helmets. This overlays the second layer of the player's skin.

### Dispensers
A dispenser can equip a player head on a player, mob, or armor stand with an empty helmet slot, within the block the dispenser is facing.

### Enchantments
Player heads can receive the following enchantments, but only through an anvil.

| Name               | Max level | Method |
|--------------------|-----------|--------|
| Curse of Binding   | I         | Anvil  |
| Curse of Vanishing | I         | Anvil  |

## Player skins

  

This feature is exclusive to  Java Edition. 


Player heads can be given NBT data so that they appear with the skin of any Minecraft account. This means if a player knows that a specific account has a head that is desired to display, the NBT data can be edited to make it appear. Commonly, this kind of head is called a custom head.

The command to give the player a head with the skin of another player is /give @s minecraft:player_head{SkullOwner:"<PlayerName>"}.

Another command to give the player a head with another player's skin is /give @s minecraft:player_head{SkullOwner:{Id:"<PlayerUUID>",Properties:{textures:[{Value:"<SkinURL>"}]} } }. SkinURL is a string encoded in Base64 containing the URL of the player's skin.[2] A player head saves the skin of the player from the time it was created, meaning if the player changes their skin, the head still displays the original texture.[3]

Note that it is therefore necessary to be connected to the internet to load the texture of a skin, whatever the property used.
When they are loaded for the first time by the client, the skins textures are cached in .minecraft\assets\skins\(subfolders)\(files).
If the client does not have access to the internet when it first loads, the player's head displays a regular head (Steve's skin) which is also cached.
Afterward, even if the client reconnects to the internet, in order to display the skin correctly, it is necessary to clear the cache manually by deleting the recently created files in .minecraft\assets\skins\(subfolder), then restarting the game.

### 
Most of the MHF mob heads provided.

  

This feature is exclusive to  Java Edition. 


Marc Watson created a number of accounts with specific skins so map makers could use common player heads without the risk of someone changing their skins.[4] Nowadays, since heads do not update the skin if a player changes their skin, this is not something map-makers need to worry about, though these skins are still useful. These accounts have names in the format MHF_<name>, for example MHF_PigZombie is the name of a Minecraft user with a zombified piglin head. MHF stands for "Marc's Head Format".[5] There are also a few blocks and "bonus" heads, for more variety. These player heads have not been updated in compliance with the Texture Update, and are outdated.

Because these are names of player accounts, these player heads are obtained or placed using the minecraft:profile component, for instance: /give @s minecraft:player_head[profile={name:”MHF_<name>”}].

The following names/heads have been made available:[6]

Mobs

 MHF_Alex
 MHF_Blaze
 MHF_CaveSpider
 MHF_Chicken
 MHF_Cow
 MHF_Creeper
 MHF_Enderman
 MHF_Ghast
 MHF_Golem
 MHF_Herobrine
 MHF_LavaSlime
 MHF_MushroomCow
 MHF_Ocelot
 MHF_Pig
 MHF_PigZombie
 MHF_Sheep
 MHF_Skeleton
 MHF_Slime
 MHF_Spider
 MHF_Squid
 MHF_Steve
 MHF_Villager
 MHF_WSkeleton
 MHF_Zombie

Blocks

 MHF_Cactus
 MHF_Cake
 MHF_Chest
 MHF_CoconutB
 MHF_CoconutG
 MHF_Melon
 MHF_OakLog
 MHF_Present1
 MHF_Present2
 MHF_Pumpkin
 MHF_TNT
 MHF_TNT2

Bonus

 MHF_ArrowUp
 MHF_ArrowDown
 MHF_ArrowLeft
 MHF_ArrowRight
 MHF_Exclamation
 MHF_Question

## Data values
### ID
Java Edition:

| Name             | Identifier       | Form         | Translation key                  |
|------------------|------------------|--------------|----------------------------------|
| Player Head      | player_head      | Block & Item | block.minecraft.player_head      |
| Player Wall Head | player_wall_head | Block        | block.minecraft.player_wall_head |

Bedrock Edition:

| Head  | Identifier | Numeric ID | Form                         | Item ID[i 1] | Translation key      |
|-------|------------|------------|------------------------------|--------------|----------------------|
| Block | skull      | 144        | Block & Ungiveable Item[i 2] | item.skull   | —                    |
| Item  | skull      | 516        | Item                         | —            | item.skull.char.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Unavailable with /give command


| Name         | Savegame ID |
|--------------|-------------|
| Block entity | Skull       |

### Metadata
See also: Data values

In Bedrock Edition, player heads use the following data values:
For the item and for the tile entity, data values determine the skull type:

|  | DV | Description           |
|--|----|-----------------------|
|  | 0  | Skeleton Skull        |
|  | 1  | Wither Skeleton Skull |
|  | 2  | Zombie Head           |
|  | 3  | Head                  |
|  | 4  | Creeper Head          |
|  | 5  | Dragon Head           |

