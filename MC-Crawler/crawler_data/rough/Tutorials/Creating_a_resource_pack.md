# Tutorials/Creating a resource pack
Resource packs allow users to include files that can modify or add custom textures, models, animations, music, sounds, user interfaces, and languages that change the way some things in Minecraft behave or look.

## Contents
- 1 Preface
	- 1.1 What NOT to do
- 2 Getting started
	- 2.1 Making a resource pack
	- 2.2 Tools
		- 2.2.1 File archiver
		- 2.2.2 Editor
		- 2.2.3 Audio editor
		- 2.2.4 Image editor/3D modeling tool
- 3 Creating a resource pack
	- 3.1 Creating the folder
	- 3.2 Creating a .MCMETA file
	- 3.3 Formatting pack.mcmeta
		- 3.3.1 "pack_format"
			- 3.3.1.1 "description"
			- 3.3.1.2 Correct syntax
	- 3.4 Testing your pack
		- 3.4.1 Troubleshooting
	- 3.5 Pack icon
- 4 Adding content
	- 4.1 Structuring the assets folder
		- 4.1.1 Adding a namespace folder
	- 4.2 Accessing the vanilla resources
	- 4.3 Modifying an entity's texture
		- 4.3.1 Finding the vanilla texture
			- 4.3.1.1 Pack hierarchy
	- 4.4 Modeling blocks and items
		- 4.4.1 Replacing a block
		- 4.4.2 Modeling the ladder - Blockbench
		- 4.4.3 Texturing the ladder - paint.net
		- 4.4.4 Finishing off
	- 4.5 Changing existing sounds or music
		- 4.5.1 Finding a sound's path
		- 4.5.2 Modifying the sound
		- 4.5.3 Testing your sound
	- 4.6 Adding new sounds or music
		- 4.6.1 Finding the sound path
		- 4.6.2 Adding the folders and sound in your resource pack
		- 4.6.3 Changing the sound event
		- 4.6.4 Testing your sound
	- 4.7 Adding languages
	- 4.8 Animation properties
	- 4.9 Texture properties
	- 4.10 Fonts
- 5 Testing your resource pack
- 6 Packaging resource packs with worlds
- 7 Server resource packs
- 8 References

## Preface
Resource packs allow users to include files that can modify or add custom textures, models, animations, music, sounds, user interfaces, and languages that change the way some things in Minecraft behave or look.

### What NOT to do
There are some things that you should NOT do when creating a resource pack / texture packs, which includes but is not limited to:

- Anything that violates theMinecraftEULA.
- Release files that allow users to play a release ofMinecraftwithout having purchased it from Mojang.
- Release the decompiled source code ofMinecraftin any way.

In any case, you should always follow the Terms and Conditions on the Mojang Studios website.

It is also suggested that you never extract game files to your desktop, as it can result in technical issues.

## Getting started
### Making a resource pack
Minecraft has a unique mechanic that allows for text and media files to be added to the game files that allow for everything from custom block textures and models to custom credits and sound events. This tutorial is meant to help with setting up the file systems in order to implement them. Since the files are essentially code, there are technical rules for how to format files and certain things may change from version to version. As such, what is written in this tutorial may not apply to every situation, but in the case where the difference is significant and specific, it provides a framework on the changes needed for different versions. 

This tutorial is geared toward the latest release of Minecraft, which is currently 1.20.4



{ 
  "pack": {
    "pack_format": 22,
    "name": "MyResourcePack",
    "description": "My Resource Pack"
  },
  "language": {
    "LANG_COUNTRY": {
      "name": "My Custom Language",
      "region": "Country/Region name",
      "bidirectional": false
    }
  }
}

### Tools
Creating custom files for Minecraft, whether in the forms of resource/data packs or mods, is somewhat technical and can be difficult. There are many rules that must be followed in order for add-ons to work correctly, most notably how the files are formatted. There are many tools that can help mitigate these issues, some of which are listed here.

#### File archiver
To access the base assets of Minecraft to edit textures, models, or sounds, a file archiver is needed. 7-Zip or WinRAR are suggested. MacOS has a built-in file archiver called "Archive Utility" that can be used, but if an alternative is wanted, The Unarchiver also works.

#### Editor
Making a resource pack involves creating JSON text files, which can be tricky to use and format correctly. Many File Editors assist with formatting these files and making sure proper syntax is used, as well as help organizing files in a project. Here are some suggestions:

- Notepad++- A very lightweight Text Editor. very easy to use
- Visual Studio Code– More complex Text Editor better suited for those who have experience with working in Text Editors.
- jsonformatter.org- an online JSON formatting

#### Audio editor
In order to add sound files, you must put it in the proper format (.ogg). While this can be done using one of numerous sites online, an audio editor program is suggested to allow customizing or trimming of audio files. Audacity is one of the most popular audio editors.

#### 
To add textures or custom models, it is suggested to use a modeling program that allows for a visual-based editing system. Like with audio conversion websites, there are many online tools, though a common recommended program is Blockbench. Most image editors suffice to modify textures, but it is recommended to use an editor that supports transparency such as paint.net or https://pixlr.com/ so that you may add transparent pixels to textures.

## Creating a resource pack
All the resources and instructions in a pack reside in the pack folder, which lives in the "resourcepacks" directory. You may wish to use an IDE to help keep track of the files within your resource pack if there are multiple.

In versions 1.11 and higher, all file names within a resource pack should use lowercase letters only.

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

### Accessing the vanilla resources
If you plan on editing multiple resources, or to help ease of access, you may want to save a copy of the vanilla resources in an accessible location in case some things rely on other files within the directory. To do this, you need to navigate to the vanilla resources file by opening the versions folder inside the .minecraft directory. You should see a list of numbered folders, which correspond to versions that you've loaded or used in the past. Open the folder corresponding to the version you want for your resource pack (in this tutorial it would be 1.20.4) and extract the JAR file located inside, which can be done by right clicking the file and selecting a file archiver from the "Open With" option. You may want to save this in an accessible location for future reference, as certain tasks such as modifying block models require textures in addition to the model files. If you do not have a program that can open .jar files simply change the extension from .jar to .zip.

### 
This section goes through the process of modifying a texture, using the creeper texture as an example.

#### Finding the vanilla texture
First, you need the vanilla resource to get the texture you want to edit. This is located in the extracted version folder that was created in the previous section. In the extracted folder, navigate to assets→minecraft→textures→entity→creeper where you can find creeper.png. Save a duplicate of this file somewhere accessible or keep the folder window open during the next few steps.

The creeper texture loaded in paint.net
Next you'll need to replicate the folder structure of the vanilla pack within your resource pack, which lets Minecraft know to use the texture. Since we are modifying a default texture, this is in the minecraft subfolder of our assets folder. Within the minecraft folder of your resource pack, do the following:

1. Insideminecraft, create a folder calledtextures.
2. Insidetextures, create a folder calledentity.
3. Insideentity, create a folder calledcreeper.
4. Copy the creeper texture from the vanilla resource pack into your newly createdcreeperfolder.

Now that you have the normal creeper texture placed in your resource pack, open it up in the image editor of your choice. It should look something like the image shown. 

Since texture files are very small, you may need to zoom in. 

** A quick note on textures **
If you've never seen a texture before, the above image might surprise you. A lot of textures look this way and are "wrapped" around a model, like wrapping paper around a present.

Color-coded Texture. Sections of the same color always face the same direction.
Now it's time to be creative! Edit the texture however you want. For simplicity, this example adds a headband. Note where the changes are and compare it to the color-coded texture above.

Creeper texture with a red headband.
Once you are happy with your texture, save the file as creeper.png. It is important that it is saved with the same name as the default asset or otherwise it cannot detect and load your texture.

Now you can load up Minecraft and spawn a creeper with your custom texture! If it doesn't show up, make sure that you've selected your resource pack.  If it still doesn't work, make sure you've named the file properly and placed it in the correct folder.

Here's the creeper with the new texture as it appears in-game.
##### Pack hierarchy
If you are playing with multiple resource packs loaded, there may be some textures that are in your pack that aren't being shown. This is because of the way resource packs are loaded in Minecraft. All selected resource pack files are loaded from the bottom up as they are shown in the selection menu, so if there is a resource pack that is loaded above yours, it may replace files that you've changed. This can cause various issues with using multiple themed resource packs that have differing textures, so make sure you have your resource pack at the top.

### Modeling blocks and items
Main article: Model
Sometimes you may want to change one of the Minecraft models. To do so you need a file archiver to get the default model and texture along with a 3D modeling tool to edit the model. Blockbench works well in this case since it can export directly to the .json format needed for models. 

#### Replacing a block
Because the default ladder in Minecraft isn't 3D, you can replace it with your own model. First, get all the ladder's files into this resource pack:  

1. Open theMinecraftJAR file using a ZIP viewer of your choice.

- Navigate into theassets/minecraft/blockstatesfolder, then extractladder.jsontoTutorial_Resource_Pack/assets/minecraft/blockstates
- Navigate into theassets/minecraft/models/blockfolder, then extractladder.jsontoTutorial_Resource_Pack/assets/minecraft/models/block
- Navigate into theassets/minecraft/models/itemfolder, then extractladder.jsontoTutorial_Resource_Pack/assets/minecraft/models/item
- Lastly, navigate into theassets/minecraft/textures/blockfolder, then extractladder.pngtoTutorial_Resource_Pack/assets/minecraft/textures/block.

Now you can either edit the ladder.png using your preferred image editor, or you can edit it in your preferred modeling editor.

Note: If you are doing a basic "Just Simple Nonanimated Textures" resource pack, the .json files are unnecessary. Otherwise, if you are doing special features to change what the texture looks like when certain parameters are true or false, then the .json files would be necessary. For example, if you created a resource pack that makes grass blocks smooth, the .json files would prevent you from having dirt lines everywhere in your world that already uses code.    

#### Modeling the ladder - Blockbench
In modeling the ladder, we use Blockbench. Once you have opened the program, press Ctrl+O to open the model selection menu. After the open dialog has appeared, go to the location where you saved ladder.json and select .

You then should be facing a ladder that is on the south side of the box. 

- On the menu bar, go to"Edit -> Add Cube"to create a new block.
- Resize the model to a full-sized cube. Then, underTextureson the left panel right clickladder.png, then clickApply to Untextured Faces.
- In the top left, there is an image of the ladder, with a 1×1 highlighted region. Move this to change the texture to what you want it to be. Repeat until all sides of the block are as wanted.
- Go to"File -> Save Model"and save inresourcepacks/Tutorial_Resource_Pack/assets/minecraft/models/block/ladder.json(Replace"block"with"blocks"for 1.12 and below).

Now we have created a new model for the ladder block in Blockbench.

#### Texturing the ladder - paint.net
Go to getpaint.net and download paint.net for free.

- Open paint.net.
- Do Ctrl+O and go to .minecraft/textures/block/ladder.png and double click.
- Edit the Ladder however you want.
- When you're done, press the X button in the top right of the window. It opens a dialog if you changed anything and ask if you want to save your work. Press Save then okay twice. You don't need to change anything in the menus.

#### Finishing off
When you have completed the 3D model of the ladder and saved it, launch Minecraft, and test it out. Place a ladder on a wall, and you should see its replaced model.

### Changing existing sounds or music

  

This section is missing information about Changing subtitles of sounds, adding subtitles to existing sounds without them. 
Please expand the section to include this information. Further details may exist on the talk page.


Just like modifying the default textures or models, you can substitute custom sounds in place of the default ones. This example shows how to change the boss music in the ender dragon fight.

##### 
Similar to the custom texture and models, you'll first need to know the path of the sound you want to change.

1. Inside your.minecraftfolder, navigate toassets/indexes, which contains a list of numbered.jsonfiles.
2. Find the.jsonfile corresponding to yourMinecraftversion (e.g.1.19.json), and open it with a text editor or IDE.
3. In this file you can find all the sounds found inMinecraft. PressCTRL+Fto search for your sound.
	- For a list of filenames for music, you can checkMusic#List
4. Your sound path should look something like this:minecraft/sounds/music/game/end/boss.ogg

##### Modifying the sound
1. Inside your resource pack folder, navigate toassets/minecraft.
2. Create a new folder namedsounds.
3. Now inside yoursoundsfolder, you need to create new folders depending on your sound's path. For example, if your path isminecraft/sounds/music/game/end/boss.ogg, you need to create the folderssounds/music/game/end.
4. In the last folder (in this example, it'send) you can put in your new sound file. Make sure you named the file to the file that you're replacing, or in this example,boss.ogg.
	- Note that this filemustbe a.oggfile. To convert your sound file to a.oggfile, you can use the free websiteOnline-Convert.com

##### Testing your sound
If everything went according to plan, you have now replaced a sound in Minecraft. To test it:

1. Make sure you have enabled your resource pack.
	- If you already hadMinecraftopen with your resource pack enabled, you can pressF3+Tto reload all resource packs.
2. Use the/playsoundcommand to play your sound. In our example, type:/playsound minecraft:music.dragon master @s

### Adding new sounds or music

  

This section is a work in progress. 
Please help expand and improve it. The talk page may contain suggestions.


In addition to modifying default sounds, you can add your own! In this example, a new player hurt sound can be added without replacing any of the current player hurt sounds.

##### Finding the sound path
In order to add a sound, you'll need to know where it should actually go by determining its path. Unlike replacing sounds, you should go straight to your resource pack folder and search in there.

1. Find and open your version's.jsonindex file (e.g1.19.json) from.minecraft/assets/indexes.
2. PressCTRL+Fto search for your sound path.
	- In this case, the location for the player hurt sounds looks like this:minecraft/sounds/damage/.

##### Adding the folders and sound in your resource pack
1. Going to your resource pack folder, navigate toTutorial_Resource_Pack/assets/minecraft.
2. Inside theminecraftfolder, create a folder namedsounds.
	- If you already have asoundsfolder from replacing a default sound, open that folder.
3. Within thesoundsfolder, create a folder that matches the directory of the sound you want to add. In this case, we are going to create a file calleddamage.
4. Add your sound here.
	- The soundmustbe a.oggfile. Like in the previous section, you may use the free websiteOnline-Convert.comor use Audacity as mentioned at the top of the page.
	- Also note the already existing files seen in your.jsonfile from above. In this case, five other hurt sounds exist within theminecraft/sounds/damage/folder, two for falling at different heights (fallbig.oggandfallsmall.ogg) and the other three are when the player actually gets hurt (hit1.ogg,hit2.ogg, andhit3.ogg) Since we want toadda fourth sound to the existing three hurt sounds, we cannot reuse those file names. For simplicity, name your soundhit4.ogg.

##### Changing the sound event
Because we are adding a sound, we must change the associated sound event in sounds.json.

1. Go back toassets/minecraftin your resource pack folder.
2. Create a text file namedsounds.json. Do make sure that the file extension is indeed.jsonand nothing else.
3. At your choice, paste the following template intosounds.json:

{
  "entity.player.hurt": {
    "sounds": [
      {
        "name": "damage/hit1"
      },
      {
        "name": "damage/hit2"
      },
      {
        "name": "damage/hit3"
      },
      {
        "name": "damage/hit4"
      }
    ],
    "subtitle": "Hurt"
  }
}

- The above code only applies to this example, which adds a new damage sound. If you are changing a different sound event, replaceentity.player.hurtwith the sound event listed in the vanillasounds.jsonfile.
- You can find out the id used byMinecraftfor each sound folder. By using/playsoundin-game, you can determine this id. In this case, using/playsound minecraft:entity.player.hurt master @sconfirms that the player's hurt sound is indeed classified asentity.player.hurt.
- Make sure the name fields are in lowercase characters only. The names of your files should be in lowercase as well. Otherwise, the resource pack may fail to use your new sounds.
- Thesubtitlefield dictates the text to display when the sound is played. It can either be a string of text, or can use a field defined in alangfile.[needs testing]
- In addition to these fields displayed, you may add more additional fields to thesounds.jsonfile to specify more parameters such asvolumeandpitch. A detailed list of additionalsounds.jsonfields can be foundhere.
- Correct.jsonformatting is required! Any missing bracket, comma, etc. causes the resource pack to fail.

##### Testing your sound
If there is an error anywhere in your sounds.json file, none of the sounds described in it appear in-game. If this happens, you should check the spelling and file paths.

If everything went according to plan, you have now added a sound to Minecraft. To test it:

1. Make sure you have enabled your resource pack.
	- If you already hadMinecraftopen with your resource pack enabled, you can pressF3+Tto reload all resource packs.
2. Use the/playsoundcommand once again to play your sound. In our example, type:/playsound minecraft:entity.player.hurt master @s. For this example, it likely requires multiple tries, as hurt sounds are chosen randomly.

### Adding languages
Main article: Resource pack § Language
You can add new languages to Minecraft using a resource pack. Assume your language code is 'LANG'[1] and country/region code is 'COUNTRY',[2] pack.mcmeta looks like:

** pack.mcmeta **
{
  "pack": {
    "pack_format": 22,
    "description": "Tutorial Resource Pack"
  },
  "language": {
    "LANG_COUNTRY": {
      "name": "Tutorial Language",
      "region": "COUNTRY/REGION NAME",
      "bidirectional": false
    }
  }
}

If you want your language to be right-to-left, set "bidirectional" to true.

Then, put LANG_COUNTRY.json in assets/minecraft/lang inside your resource pack. When you launch the game, choose your resource pack, open the Language selection screen, and your new language should be there.

** Notes **
The pack.mcmeta goes in the root folder of your resource pack, not in the assets/minecraft/lang folder. Also note that the above pack.mcmeta is the same file as the pack.mcmeta file that you have created a while ago.  As of 1.7-pre, you can choose multiple resource packs at once. If you want to use your new language and resource pack for before 1.7, you need to combine them manually because multiple resource packs could not be selected before the version.

### Animation properties
Main article: Resource pack § Animation
An example of an animation file is this:

** stone.png.mcmeta **
{
  "animation": {
    "interpolate": true,
    "width": 1,
    "height": 7,
    "frametime": 1,
    "frames": [
      {
        "index": 0,
        "time": 0
      },
      1, 2, 3, 4, 5, 6, 4, 2
    ]
  }
}

** Note **
All you really need to make a texture animated is the following code. By default, it makes each frame last only one tick:

** stone.png.mcmeta **
{
  "animation": {}
}

Save the file as the same name as the texture you want to be animated with an .mcmeta in the same folder as your texture.

### Texture properties
Main article: Resource Pack § Textures
An example of a texture property is this: 

** shadow.png.mcmeta **
{
  "texture": {
    "blur": false,
    "clamp": true
  }
}

### Fonts
Main article: Resource pack § Fonts
Character sizes in fonts are determined by the last line of pixels that contains pixels that contain a non-zero alpha. This allows additional padding to be added around characters by adding a color with an alpha level of 1, which Minecraft considers as part of the character.

## Testing your resource pack
- Launch the game
- Click onOptions
- Click onResource Packs
- Find "Tutorial_Resource_Pack" in the list on the left and click the arrow next to it
- ClickDone

If you decide you want to make some changes to your resource pack, edit your resource pack, go to resource packs in options, remove your pack from the active list and exit, go back, and reapply it. Alternatively, saving the texture to the resource pack and pressing F3 + T reloads the pack without the need to reload the default textures first.

## Packaging resource packs with worlds
For use in singleplayer worlds, you can package your resource pack as a ZIP file named resources.zip inside the world directory. This is then automatically used when playing the singleplayer world.

## Server resource packs
If you are the owner of a server, you may set it as the resource pack of your server. 

1. Make sure your pack format is a .zip-folder.
2. Upload the pack on a file hosting website, e.g.MCPacks.
3. Copy the download link of your pack. IMPORTANT: If you are using your own server or some other host then you have to make sure that you are using a direct download link. You also need to make sure to use a SSL certificate that is compatible with the shipped Java version 8 u51. (MC-143768)
4. Open the server.properties with a text editor.
5. Search for the lineresource-pack=.
6. Paste the download link after the equal sign.
7. Optional: Set therequire-resource-packproperty totrueto force people to use the resource pack.
8. Save your changes to the server-properties and restart your server.
9. Enjoy!

Servers can have an icon that appears in the Multiplayer list. 

1. Create a PNG image with a size of 64 by 64 pixels, transparency is supported.
2. Save (or rename) it toserver-icon.png.
3. Move it to the server's directory.
4. Restart the server.
5. Server icons should display next to the server name.

