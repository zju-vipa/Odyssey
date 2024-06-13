### Creating the folder
The first thing we need to do is create the folder that contains all the resource pack files. Create a folder on your desktop or another easily accessible location and name it Tutorial_Resource_Pack. This eventually becomes the name displayed in the resource pack menu.

### Creating a .MCMETA file
Within your resource pack folder, we need to create a pack.mcmeta file. This lets Minecraft know that the folder is a resource pack and contains useful information such as:

- The recommended version for the resource pack.
- The description displayed under the pack title in the selection menu.
- Preliminary information on any custom languages added in the resource pack.

To create this file, we need to create a text file within the folder and name it pack.mcmeta. Make sure the file extension is .mcmeta and not .txt or the pack may not be detected. When renaming you may get a warning that changing a file name extension could make the file unusable or may switch the program required to open it. You can still open this file in a text editor by right-clicking the file and selecting the "Open With" option. Note: You may need to select a program using your file browser.

### Formatting pack.mcmeta
Open pack.mcmeta in a text editor or IDE of your choice and type or copy+paste the following:

{
  "pack": {
    "pack_format": 22,
    "description": "Tutorial Resource Pack"
  }
}

#### 
The value of "pack_format" tells Minecraft what release the resource pack is designed for, and is different for certain versions. The following list what versions each value is associated with:

- 1for versions1.6.1–1.8.9
- 2for versions1.9–1.10.2
- 3for versions1.11–1.12.2
- 4for versions1.13–1.14.4
- 5for versions1.15–1.16.1
- 6for versions1.16.2–1.16.5
- 7for versions1.17.x
- 8for versions1.18.x
- 9for versions1.19–1.19.2
- 11for versions22w42a–22w44a
- 12for version1.19.3
- 13for version1.19.4
- 14for versions23w14a–23w16a
- 15for versions1.20-1.20.1
- 16for version23w31a
- 17for versions23w32a-23w35a
- 18for versions1.20.2-23w35a
- 19for version23w42a
- 20for versions23w43a-23w44a
- 21for versions23w45a-23w46a
- 22for version1.20.3-pre1-23w51b
- 24for version24w03a-24w04a
- 25for version24w05a-24w05b
- 26for version24w06a-24w07a
- 28for version24w09a-24w10a
- 29for version24w11a
- 30for version24w12a
- 31for version24w13aand onward
- 

Note: As more updates are released, values may be changed or added.

##### 
The text following "description" is displayed under the pack title in the selection menu, and must be put inside quotes "". If you wish to use special characters, you can enter the Unicode code for the character in the format \u####, where #### is the Unicode hex code for the character. Say you want to use the letter  ß, which has code U+00DF. Inside the description you would type \u00DF. Make sure that you are using the correct slash, or it may not work. A list of Unicode codes can be found here. Note: Only the characters 0000–FFFF (Basic Multilingual Plane) are supported.[citation needed]

##### Correct syntax
Be very careful not to forget quotation marks "", colons :, braces {}, or square brackets []. Missing one of these can lead to your resource pack not being detected by Minecraft. Make sure that your pack.mcmeta file matches the one shown above.

### Testing your pack
If your resource pack is formatted correctly, it should appear in the selection menu like this.
At this point, you can test if the pack is formatted correctly by putting it in the game! To do this you must place your resource pack folder in the Minecraft pack folder. You can access it by selecting "Options", then "Resource Packs", then "Open Pack Folder", or you can navigate to it from your file browser:

- For Windows, right click on the start button → run → type in %appdata% → .minecraft → resourcepacks
- For MacOS, go to Library → Application Support → minecraft → resourcepacks
- For Linux, go to ~/.minecraft/resourcepacks (/home/<username>/.minecraft/resourcepacks)

Once you have the folder open, you can drag your custom pack folder and drop it in.

If you have formatted the files correctly, you should see your resource pack appear in the menu.

#### Troubleshooting
If you don't see your pack in the list, make sure your pack.mcmeta file is correct and saved in the folder. Look for any missing braces {}, commas ,, colons :, quotation marks "", or square brackets []. Remember that for each open brace, quotation, or square bracket, you must have a closing brace, quotation, or square bracket.

### Pack icon
If an icon is not specified, a cobblestone icon appears next to the pack. If you want to use your own pack icon, you can place it inside your resource pack folder with the name pack.png. The file must be a PNG, and works with any square resolution, but a 128×128 pixel image renders the best.

## Adding content
### Structuring the assets folder
Now that you have your resource pack set up, you can start adding content to it. You add most files into a subfolder called assets. Simply create a new folder inside your resource pack folder named assets. This, pack.mcmeta, and pack.png should be the only files located directly in your parent resource pack folder. Any other resource files must be located somewhere in assets or they won't be read by Minecraft.

#### Adding a namespace folder
Next, inside your assets folder are your namespace folders. These help separate the files in your resource pack so that there is no confusion between which files are located where. If you plan on modifying or replacing vanilla resources, those files would go into the minecraft namespace folder. Custom additions should go in your own namespace folder, which for this tutorial is named custom. In the future, you should use a significant or unique namespace so that there isn't a possibility of other resource packs confusing which files belong where when multiple packs are loaded.

