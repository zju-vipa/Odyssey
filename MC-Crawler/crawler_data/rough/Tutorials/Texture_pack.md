# Texture pack
A texture pack was a collection of files that were used to change the in-game textures of blocks, items, mobs and the GUI. They were .zip files that had various PNG images in them and a text document named pack.txt. The native resolution of Minecraft's textures were 16×16 (measured pixels in block height and width). 32×32, 64×64, 128×128, 256×256, 512×512, and 1024×1024 textures were referred to as "HD".

In Java Edition 1.6.1, texture packs were replaced with resource packs, which provide more control over textures and other game features, such as music and text.

## Contents
- 1 Behavior
- 2 Folder structure
- 3 Contents
	- 3.1 pack.mcmeta
- 4 Installing a texture pack
	- 4.1 Installation tips
- 5 Converting texture packs to resource packs
- 6 History
- 7 Trivia
- 8 Gallery
- 9 See also

## Behavior
The default texture pack settings.
Texture packs can be placed in the folder texturepacks within the .minecraft folder. Each texture pack is either a .zip file within the texturepacks folder. Once in the folder, a texture pack can be added from the options.

Texture packs load their assets based on the order of the packs on the list. The bottom-most pack loads first, then each pack placed above it replaces assets of the same name with its assets.

## Folder structure
| (texture pack name) font.txt pack.png pack.txt particles.png achievement bg.png icons.png map.txt armor (texture).png art kz.png environment (texture).png font (texture).png gui (texture).png creative_inv (texture).png item (texture).png chests (texture).png lang (lang).lang languages.txt misc (texture).png mob (texture).png enderdragon (texture).png villager (texture).png textures blocks (texture).png items (texture).png title black.png credits.txt mclogo.png mojang.png splashes.txt win.txt bg (texture).png |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Contents
### pack.mcmeta
A texture pack is identified by Minecraft based on the presence of the folder of the root directory, which contain a text file called pack.mcmeta, which would contain a description of the texture pack which would appear in game.

The root directory also contains an optional image called pack.png, which shows as the thumbnail for the pack on the texture pack selection menu.

## Installing a texture pack
1. Download a texture pack. Most texture packs are inZIPfile format, but as long as it has the necessary files (pack.mcmeta),Minecraftrecognizes a folder as a texture pack. In-depth instructions on obtaining the files to make custom texture packs are located atTutorials/Custom texture packs. However this is not necessary, as of snapshot12w23a, for as long aspack.txtexists, it is recognized as a texture pack.
2. RunMinecraft. IfMinecraftis already running, make sure to leave the world.
3. ClickTexture PacksinOptions.
4. ClickOpen Texture Pack Folder; this opens the folder whereMinecraftstores all texture packs. If nothing happens, the folder must be found manually. Depending on the operating system it is located at:

Windows XP and above: %appdata%\.minecraft\texturepacks .
GNU/Linux: ~/.minecraft/texturepacks (this folder may be hidden in the Home folder).
macOS: ~/Library/Application Support/minecraft/texturepacks (this folder may be hidden).
1. Minecraftdoes not have to be closed when placing the texture pack in the opened folder.
2. In a few seconds the texture pack appears inMinecraft. Select it and click "Done". The texture pack is now applied. IfMinecraftdid not update, simply exit and reopen the texture packs screen.

### Installation tips
- Texture packs may redesign only some textures. So if the main menu looks the same after a pack is selected, it doesn't mean the pack is not working.
- Many texture packs may be installed and overlap each other. The texture pack list can be scrolled by dragging the scrollbars up or down.
- Minecraftmay lock the currently used texture pack (for example, if the pack contains custom textures for user interface), so the file can't be overwritten. If the pack needs to be updated, it may be necessary to temporarily switch to the default pack and then overwrite the file.
- To get an unzipped directory to show as a texture pack inMinecraft, that directory needs apack.txtfile in it. This, however, did not work prior to12w23a.
- Keep in mind that, if a texture pack is downloaded in ZIP form, it may contain another folder inside of it that has the texture pack's title, this is the actual texture pack. In this case, this folder must moved to the texture packs folder.
- If an older version ofMinecraft(1.2.5 for example) is being used and a texture pack for a newer version is installed, the texture pack still runs properly, and ignores the unused items or blocks.
- If an older texture pack is used in a more recent version ofMinecraft, then the newer blocks and items show a "missing texture" because the texture pack isn't made for newer versions.
- An editor is a great way to make a texture pack.

Current versions of Minecraft support higher resolutions of texture packs. Traditionally, textures in-game work on a 16×16 block. Bigger texture packs can go all the way up to 512×512 (32×, 64×, 128×, 256×) but require better hardware to play smoothly.

## Converting texture packs to resource packs
Converting texture packs can be done with Mojang's converter tool (called "texture ender"). Converting texture packs from before 1.5 is a two-step process, requiring a converter to convert it to 1.5 first (called the "unstitcher") then the converter from 1.5 to 1.6. Links to both Mojang files are below:

- Unstitcher[verify]
- TextureEnder

