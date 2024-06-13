# Information block
Information block was a block that could be used by players in MinecraftEdu to write large amounts of text.

## Contents
- 1 Usage
	- 1.1 Text
	- 1.2 Interaction
	- 1.3 Configuration
		- 1.3.1 Teleport
		- 1.3.2 Editing
- 2 Data values
- 3 Gallery
- 4 History

## Usage
The GUI of an information block.
The information block could be placed and used by both student and teacher players. 

### Text
When placed or interacted with, the information block opened a unique text field window, similar to that of a book and quill. Text could be entered starting on any line of the text field, however each line is limited to only 35 characters. When a line is full, the current word is shifted to the next line. Text may also span over several pages.

When editing text, the player could copy and paste the full contents of the current page.

### Interaction
All players could interact with information blocks to view their contents regardless of their permission level. Whether or not a player could edit text contained in an information block was only possible when one of several conditions were met:

- The player is a teacher
- The information block had been placed by a player
- The information block had been configured to allow all players to edit it

### Configuration
Teacher players could alter certain behavior of the information block through a special configuration menu.

#### Teleport
When configured, players who stepped on top of the information block would be teleported a certain amount of blocks (up to 5) in a certain direction. They would also be presented with the text field automatically.

#### Editing
Teachers could choose whether to allow all players to edit the contents of an information block. For blocks placed by teachers, this defaulted to off. For students, it defaulted to on.

## Data values

ID of this block is 3722.
| Name              | Identifier           | Translation key                      |
|-------------------|----------------------|--------------------------------------|
| Information block | `blockDialogMessage` | `block.minecraft.blockDialogMessage` |


