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


