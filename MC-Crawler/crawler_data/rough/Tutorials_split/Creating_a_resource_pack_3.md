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

