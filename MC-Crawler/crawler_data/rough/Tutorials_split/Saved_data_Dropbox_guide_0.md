# Tutorials/Saved data Dropbox guide
This tutorial explains how to migrate your saved games to Dropbox so you can play your levels on multiple computers. BE WARNED that you can only play on one computer at a time, and you must allow Dropbox to completely finish syncing before starting to play on a different computer.  If you do not, you risk losing your progress or possibly corrupting your save.

## Contents
- 1 Download and Install Dropbox
- 2 Move your Minecraft Saved Data to your Mega Folder
	- 2.1 Windows
		- 2.1.1 Alternate (command line) method
	- 2.2 macOS
		- 2.2.1 Alternate (command line) method
	- 2.3 Linux
		- 2.3.1 Alternate (command line) method
- 3 Create the Symbolic Links
	- 3.1 Windows
		- 3.1.1 Windows Vista, 7, 8, and 10
		- 3.1.2 Windows XP (after installing junction.exe)
	- 3.2 macOS
		- 3.2.1 Alternate (command line) method
	- 3.3 Linux
- 4 Note on Multiple Operating Systems
- 5 Alternate Method

## Download and Install Dropbox
The first step is to download Dropbox. Dropbox automatically syncs content to their servers and allows you to access it both online and through a client on your PC. Dropbox is cross-platform, plus available on the web and web-enabled smartphones.

Go to http://www.dropbox.com, register for a free account, download the application and install it. You automatically get 2GB for free.

Once you have installed Dropbox, you'll need to know where the Dropbox folder is:

- On Windows XP, the Dropbox folder is located inside the user's "My Documents" folder. The easiest way to reference this is using the environmental variables, as follows:"%HomeDrive%%HomePath%\My Documents\Dropbox". Because "My Documents" contains a space, the quotation marks are required.
- On Windows 7 and 8, the default Dropbox folder location isC:\Users\username\Dropbox. Use the environmental variables%HomeDrive%%HomePath%\Dropbox.
- On Windows 10, the Dropbox folder is labeled as its own item in the sidebar of the File Explorer window.
- On Linux, the default location is in the user's home folder. For example, in Ubuntu, that folder is located at ~/Dropbox
- On MacOS, it should also be in the user's home folder.

Whichever operating system you are using, Dropbox has very good documentation and can assist you in finding help: http://www.dropbox.com/help

## Move your Minecraft Saved Data to your Mega Folder
Next, we will need to make a copy of your Minecraft data on the Dropbox server and then rename the original.

### Windows
On Windows, your Minecraft data is saved in your application data (AppData) folder. You can access this by holding Windows+R or hitting Start > Run and then typing %AppData%\.minecraft in the box. If the folder doesn't open, click on the Tools menu on Windows Explorer, click the View tab, and under Advanced Settings, make sure "Show hidden files, folders and drives" is selected.

Copy all the files in this folder to your Dropbox folder. For organization sake, I usually create a subfolder inside my Dropbox folder and title it "Minecraft".

Once these files are done copying, navigate back up to your AppData folder, and rename the .minecraft folder to .minecraft2 (for files that begin with a "." such as ".minecraft" Windows may give an error message when renaming and refuse to rename. If this happens try to rename the file to ".minecraft2."; this will rename the file to ".minecraft2" without the previously typed period at the end of the title.)

This step ensures that you:

1. Have a backup of your files in case of a catastrophe, and
2. Allows us to make the symbolic link to the correct location in a later step.

#### 
xcopy /I /E %AppData%\.minecraft %HomeDrive%%HomePath%\Dropbox\Minecraft
cd %AppData%
rename .minecraft .minecraft2
Note: attempting to use rename %AppData%\.minecraft %AppData%\.minecraft2 will give the error The syntax of the command is incorrect., as should be: rename %AppData%\.minecraft .minecraft2 

### macOS
In macOS, the Minecraft data folder is located in your Username > Library > Application Support folder. You can get here quickly by opening Finder > Go > Go To Folder > type ~/Library/Application Support/minecraft. For future reference, it's best to make an alias for this folder and copy it to your desktop. NOTE: Mountain Lion hides the user's Library folder. Hold down the option key and see the Library item appear in the GO menu.

Now, copy the saves directory (~/Library/Application Support/minecraft/saves/) to your Dropbox's Minecraft folder (~/Dropbox/Minecraft/), unless you already have saves from Windows or Linux there.

#### 
mkdir ~/Dropbox/Minecraft/
cp -r ~/Library/Application\ Support/minecraft/saves ~/Dropbox/Minecraft/
mv ~/Library/Application\ Support/minecraft/saves ~/Library/Application\ Support/minecraft/saves.old

### Linux
In Linux, your Minecraft data folder is located in your user home folder. However, it may be hidden from view. If you are using a GUI, ensure that you choose View > Show Hidden Files.

Copy the contents of the .minecraft folder to your Dropbox folder. As mentioned above, I usually create a folder inside the Dropbox called "Minecraft".

Once the copy is complete, rename the .minecraft folder to .minecraft2

