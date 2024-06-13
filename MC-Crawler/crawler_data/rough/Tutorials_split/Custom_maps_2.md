### Compressing resources
If you are using a resource pack, the textures and sounds can add a hefty amount to the package size. Compressing them or making sure they do not have unnecessary high resolution can help lighten the load.

** Compressing textures **
A lot of textures can become very large without the benefit of improved quality. Some textures could be as large at 2048×2048 (almost 4K UHD) even if the player will never notice much difference. At most, textures should be 256×256 and they should not need to exceed this. Usually, textures can safely be in resolutions of 16×16, 32×32, or 64×64. Either way, try not to exceed 256×256, as this level of details is not easily be seen by the player. After finding an acceptable resolution, try using image compressors. These can sometimes reduce your file size by up to 90%, but may come at the cost of a loss of color depth (24-bit colors to 16-bit). This reduces the file size because there are not as many colors to store, but vibrant textures may become more "grainy", or "static-ey". If you still think there is data that can be shaved off, try removing all EXIF data from the image. Note that this will remove any copyright notes the image has (if any are present), and you may have to manually add credit (you should always give credit manually, but this is a legal matter).

** Compressing .ogg sounds **
Ogg Vorbis is meant to reduce filesize,[1] but sometimes just the format isn't enough. You can also reduce the bitrate of the audio or reduce amplitude and manually increase it with /playsound. You can also try mixing the track down to mono, meaning the audio will have 1 track, instead of 2. This can result in quality reduction if not done carefully. It is recommended to mix small sounds down to mono, as players won't have enough time to distinguish the stereo version from its mono counterpart.

### Removing region files
This is not recommended for most users as it can delete parts of your map. Be sure to make a backup before attempting this; you never know if something might go wrong.

Before you start, it is recommended to read up on chunks and region files. As a summary, chunks are 16×16 regions of a world, and region files are a 32×32 chunks. There are 1024 chunks, or 262144 blocks, in a region file.

Use Dinnerbone's Chunk Coordinate Finder and input coordinates of a block in every chunk in intervals of 16. For example, find the chunk file at chunk number 0, 0 and then at chunk number 0, 32. Make sure to find the blocks in positive and negative chunks, too. Once you have a full list of chunks that you want to keep, make a backup of your current world.  Once you've made your backup, delete any chunk files that are not in your list. For example, if your list contains the regions:

- 0, 0,
- 0, 1,
- 0, -1,
- 3, 4,

you would not delete r.0.0.mca, r.0.1.mca, r.0.-1.mca, and r.3.4.mca. Delete all other files that do not match. This will remove any regions that are unused which can greatly reduce the map's total file size.


