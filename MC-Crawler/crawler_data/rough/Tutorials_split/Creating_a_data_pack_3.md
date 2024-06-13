### Predicates
Main article: Predicate
Predicates are technical JSON files that represent the conditions for loot tables, /execute if predicate command, or predicate target selector argument.

To add predicates, first create a folder named predicates inside the namespace folder. Then, create a file named (predicate_name).json (You can't put spaces in the file name. Use lowercase letters in the file name). in this folder or in any of its subfolders. This will be your predicate file. Your predicate will be named in the game as (namespace):(name) or (namespace):(subfolder1)/(subfolder2)/.../(name) if the file is located in a subfolder.

### Dimensions
Main article: Custom dimension
Dimensions are JSON file used to specify all the dimensions a world contains.

To add dimensions, first create a folder named dimension inside the namespace folder. Then, create a file named (dimension_name).json (You can't put spaces in the file name. Use lowercase letters in the file name). in this folder. This will be your dimension file.

Custom dimensions can be accessed in game using /execute in (namespace):(dimension_name)

## Utilities

  


This list is incomplete; you can help by expanding it.


Many utilities have been created in order to make programming data packs easier. This is a reference list for utilities such as transpilers or syntax highlighting plugins. Please exercise caution when installing third-party programs onto your computer, as they are not actively monitored and may contain malware. 

| Name             | Hosting | Description                                                                                                                 | Link                                                        |
|------------------|---------|-----------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| Minecraft Script | GitHub  | A language based on JavaScript that can be compiled into a working data pack using a Node.js compiler.                      | https://mcscript.stevertus.com/                             |
| Minity           | GitHub  | Another scripting language that compiles into data packs using a Node.js compiler.                                          | https://github.com/minity-script/minity                     |
| TMS Transpiler   | GitHub  | A python tool that can assemble indented mcfunction code into valid files. Great if you don't want to learn a new language. | https://github.com/davidkowalk/advanced_minecraft_scripting |
| ObjD             | Pub     | A dart framework for creating data packs to minimize the repetitive work to be done.                                        | https://objd.stevertus.com/                                 |

Another option is to use a visual interface to create the framework or the content for your project.

| Name                             | Hosting                      | Description                                                              | Link                                                      |
|----------------------------------|------------------------------|--------------------------------------------------------------------------|-----------------------------------------------------------|
| Datapack Creator                 | Planet Minecraft             | An IDE for creating data packs with some useful tools                    | https://www.planetminecraft.com/mod/datapack-creator-ide/ |
| NBTData Pack Generator           | nbt-data.com                 | An online generator for a raw data pack framework without any functions. | https://www.nbt-data.com/datapack-generator               |
| Recipe Generator                 | thedestruc7i0n.ca            | An Online Generator to generate the JSON files required for crafting.    | https://crafting.thedestruc7i0n.ca/                       |
| Minecraft Tools Recipe Generator | minecraft.tools              | An Online Generator to generate the JSON files required for crafting.    | https://minecraft.tools/en/custom-crafting.php            |
| Minecraft Recipe Generator       | recipegeneratorminecraft.com | An Online Generator to create data packs for custom recipes.             | https://recipegeneratorminecraft.com                      |
| Misode's Data Pack Generator     | GitHub                       | JSON Generator for Minecraft Data Packs                                  | https://misode.github.io/                                 |
| MCStacker for MC 1.19            | mcstacker.net/               | A collection of command generators.                                      | https://mcstacker.net/                                    |
| Origin Creator                   | GitHub                       | A fully featured webtool for creating data packs.                        | https://www.mathgeniuszach.com/apps/origin-creator/       |
| MCreator                         | mcreator.net                 | A easy-to-use, fully featured graphical tool for creating data packs.    | https://mcreator.net/                                     |
| MCDatapacker                     | Github                       | An offline program to create and edit data packs                         | https://github.com/IoeCmcomc/MCDatapacker                 |

If you use a code editor, you may want to format your data pack files with syntax highlighting. Depending on your text editor extra steps may have to be taken to install it in your environment.

| IDE/Editor                     | Description                                                       | Link                                                                                  |
|--------------------------------|-------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| Visual Studio CodeSublime Text | Language grammars and syntax highlighting for mcfunction files.   | https://github.com/Arcensoth/language-mcfunction                                      |
| Notepad++                      | Syntax highlighting.                                              | https://pastebin.com/hbMiJ3YV                                                         |
| Visual Studio Code             | Heavy language features for JSON and mcfunction files.            | https://marketplace.visualstudio.com/items?itemName=SPGoding.datapack-language-server |
| IntelliJ IDEA                  | Allows connecting to an external IDE to do more optimized coding. | https://plugins.jetbrains.com/plugin/22587-minecraft-command-devkit                   |




