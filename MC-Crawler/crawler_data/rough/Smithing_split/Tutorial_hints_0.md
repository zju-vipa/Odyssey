# Tutorial hints
Tutorial hints (also know as game tips in Bedrock Edition) are tabs in the right-hand corner of the player's screen which show up when a player starts a world in Survival mode for the first time on a device. They are meant to guide new players who may not know the controls.

## Contents
- 1 Interface
	- 1.1 options.txt
- 2 List of hints
- 3 History
- 4 Issues
- 5 See also

## Interface
When a Survival world is generated for the first time on a device, the first tutorial hint appears: the movement hint. Each tutorial hint appears as a toast in the top right of the screen (much like new recipes and advancements). Each hint consists of the hint title, a description of how to complete it, and an image to describe it. Once the tutorial hint has been completed (for example, when the player harvests a tree's log), that tutorial hint disappears. After a certain amount of time, the next hint is shown automatically. Once the "craft wooden planks" hint is completed, tutorial hints never again appear in any world.

Tutorial hints are obtained by simply completing the task given. Each hint, minus the "Open your inventory" and the "Craft wooden planks" hint, have a progress bar that shows the player's progress on the current hint and fills up as it is being completed. For example, for the "Destroy the tree" hint, the progress bar begins emptying and starts filling up as the player harvests a log, so that when the log is destroyed, the bar is complete and the hint disappears.

In Creative mode, only the first two hints are displayed.

### options.txt
The gameplay stages of the tutorial is stored as tutorialStep: in the options.txt file in the game directory, except the Social Interactions hint, which is stored as joinedFirstServer:, so they are kept per device and per directory (you can set up more profiles with different game directories in the launcher options). After the last guide is shown, the value none is saved. Changing TutorialStep to this value (the game must be closed beforehand) prevents the instructions from appearing.

## List of hints
| Image | In-game title and description                                | Actual requirements (if different)                  | options.txt name    |
|-------|--------------------------------------------------------------|-----------------------------------------------------|---------------------|
|       | Move withForwards,Left,Backwards, andRight<br/>Jump withJump | Usemoveandjumpto move around.                       | `movement`          |
|       | Look around<br/>Use your mouse to turn                       |                                                     | `find_tree`         |
|       | Destroy the tree<br/>Hold downMine                           | Minealogblock until it breaks.                      | `punch_tree`        |
|       | Open your inventory<br/>PressInventory                       |                                                     | `open_inventory`    |
|       | Craft wooden planks<br/>The recipe book can help             | Put wood in acrafting tableor theinventorycrafting. | `craft_planks`      |
|       | Social Interactions<br/>PressSocial Interactionsto open      |                                                     | `joinedFirstServer` |


