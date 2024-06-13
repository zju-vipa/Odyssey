### MacOS
The Mac comes with a program called Archive Utility. First, open Finder and go to Finder>Library>Application Support>minecraft>bin. If the folder is not there, check Finder>(User)>Library>Application Support>minecraft>bin Find minecraft.jar and right-click (or control+left click) and click "Open With" and "Archive Utility". Archive Utility will create a new folder called "Minecraft". Notice that this is a new folder, and that minecraft.jar is still intact. You can therefore modify and delete the new folder without altering your minecraft.jar. Create a new folder on your desktop, and drag all the necessary files into it. Now you are ready to edit.

If using Archive Utility results in a file called Minecraft.jar.cpgz, try instead changing the file extension from .jar to .zip to achieve the desired effect.

### 
On GNU/Linux-based systems, the game archive is usually located at ~/.minecraft/bin/Minecraft.jar where "~" is the user's home folder, usually located in /home/. Many desktop GNU/Linux distributions come with graphical archiver utilities that integrate with the desktop environment. If the zip and unzip command-line programs are available, the files can be simply extracted to a folder on the desktop using the following command in the terminal:

unzip -d ~/Desktop/my_texture_pack ~/.minecraft/bin/minecraft.jar pack.png pack.txt particles.png terrain.png achievement/* armor/* art/* environment/* font/* gui/* item/* misc/* mob/* terrain/* title/*

## Editing textures
terrain.png in 13w01b, the last version to actually use this file.
The textures are in the Portable Network Graphics (PNG) format and can be edited with any image editing program that can handle the format including transparency. Many different programs support this, some free ones include Paint.net (Windows) (which even Notch uses), GIMP (Windows, Mac, Linux), Paintbrush (Mac), and many more. Edit each PNG file as desired and save them with 32-bit color depth to preserve transparency.

Although Microsoft Paint does not handle transparency, it can still be used to make/edit textures. If you open a PNG image in Windows XP, a window should pop up showing transparency as a white and gray checkered pattern [does not work Win7 - no options of this type available]. There is a tool located on the toolbar that should have a screen tip with 'Change to transparent' or something similar. Go into Microsoft Paint and create/edit your texture(s). Find a color not used in the texture, and fill in the white space with it. Then, select the area desired to copy and paste it onto the PNG image. Paste it onto your PNG image and make sure to cover it completely. Simply change your unwanted color to transparent using the tool mentioned earlier, and every last pixel of that color on the current document will be changed to transparent. Beware, make sure that you do not click the wrong color, as this may mess up all textures in the document.

## Packing and installation
Once you are done editing, create a zip file of the files modified (or, in Minecraft 1.3, you can use a folder with the files too), preserving all folder hierarchy. The root folder of the zip must have the files and folders listed below, or else they will not be changed. If you find that nothing changes when you select your texture pack, make sure that the files are in the root of the zip and not one folder in.

### Windows
Select all the files (edited or not) Then choose the 7-Zip or WinRAR option after right-clicking and select "Add to archive...". The archive will open, and you can name the file. Then hit "OK", and the program will make all the files into a zip archive. To put it into Minecraft, simply start the launcher, log in, and at the title screen go to the button "texture packs". In the lower-left, click the Open Folder button and drag your ZIP into the folder. Select your texture pack, and view it on your computer.

### Mac OS
Highlight all the files in your folder, right-click, and click "compress (#) items". A new file called "Archive.zip" should appear. Rename the file to your liking. Go to Finder>Library>Application Support>minecraft>Texture Packs, and drag your .zip in. Now you can use your texture pack by selecting the button "mods and texture packs" in the main menu of Minecraft, and clicking on your pack.

### 
Folder Layout
~/appdata/roaming/.minecraft/resourcepacks/MyPack/(assets etc.)

In Terminal, run this command...

cd ~/.minecraft/resourcepacks/ && zip -r MyPack.zip MyPack

...then launch Minecraft and enable the resource pack.


