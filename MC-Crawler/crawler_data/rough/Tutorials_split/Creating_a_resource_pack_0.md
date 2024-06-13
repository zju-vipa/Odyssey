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

