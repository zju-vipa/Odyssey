# Camera
The camera is a inanimate mob-like entity that is capable of capturing and storing images. In Minecraft Education, it works together with the portfolio item to create collections of photos.[1]

## Contents
- 1 Obtaining
- 2 Usage
- 3 Behavior
- 4 Sounds
	- 4.1 Generic
	- 4.2 Unique
- 5 Data values
	- 5.1 ID
	- 5.2 Entity data
- 6 Video
- 7 History
	- 7.1 Future
- 8 Issues
- 9 Trivia
- 10 Gallery
	- 10.1 Screenshots
	- 10.2 In other media
- 11 See also
- 12 References
- 13 External links

## Obtaining
The camera can be obtained in the Creative inventory in Education Edition. It can be obtained by either NBT editors, inventory editors, or glitches in Bedrock Edition.

To get the block form of the camera in Bedrock Edition using an NBT editor you need to set the item name of the block in the inventory slot (name: ) to item.camera, then you need to add a compound tag called Block and inside of that put the int tag version: 18040335 and the text tag name: minecraft:camera into the block compound tag. For the usable item / spawn egg form of the camera you just need to set the item name of the block in the inventory slot (name: ) to camera, you don't need to add the block compound for this form of the camera though. 

## Usage
Using a camera from one's inventory captures a first-person screenshot. It may also be placed, creating a camera entity that can track the user, and take pictures from the camera's perspective. Photos that are taken with the camera appear in the portfolio.

Close-up snapshots of an item on the ground can be taken by holding the Shift key while right-clicking.

Screenshots from camera can be inserted into book and quill.[1]

Photos that are taken with the camera block are stored in com.mojang/screenshots.

## Behavior
Camera on a boat
Cameras are mostly inanimate entities, but they occasionally move when falling and they move at the player's direction when they take a picture.

Cameras are classified as mobs in the game code, they obey gravity, allowing them to fall and having effects common to all other entities. Cameras can be affected by status effects. They can be killed by Harming and Decay splash/lingering potions, and they play the player death sound and fall to their side and disappear, droping no item. Cameras can't be leashed but they can ride on boats and minecarts.

Camera being harmed by poison effect
Cameras are harmed by fire, lava, and campfire damage but they never die from it. Cameras can be destroyed by any projectile used by the player, such as arrows, tridents, or snowballs. Cameras never drown and are invunerable to the void, cacti, falling blocks, to explosions or by firework rockets.

Wardens, withers, zoglins, goats, and vindicators named Johnny attack cameras, but the camera remains undamaged; pufferfish also inflate when an camera is nearby. Foxes don't sleep near cameras as well.

## Data values
### ID
| Camera | Identifier | Numeric ID | Form                         | Item ID[i 1] | Translation key  |
|--------|------------|------------|------------------------------|--------------|------------------|
| Block  | camera     | 242        | Block & Ungiveable Item[i 2] | item.camera  | tile.camera.name |
| Item   | camera     | 593        | Item                         | —            | item.camera.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Unavailable with /give command


| Camera | Identifier    | Numeric ID | Translation key           |
|--------|---------------|------------|---------------------------|
| Entity | tripod_camera | 62         | entity.tripod_camera.name |

### Entity data
See Bedrock Edition level format/Entity format.

## See also
- Portfolio
- Screenshot

