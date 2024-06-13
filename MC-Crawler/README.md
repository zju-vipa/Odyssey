# Minecraft Wiki Crawler

## Installation

We use python 3.11. We have tested on macOS and Ubuntu 20.04. You can follow the instructions below to run it.

### Install Requirements

```bash
pip install -r requirements.txt
```

## Get Started

You can just run `python main.py`.

In the `main.py`:

```python
if __name__ == '__main__':
    urls_dir = Path('crawler_data/rought_urls')
    base_url = 'https://minecraft.wiki'
    urls = [
        'https://minecraft.wiki/w/Mob',
        'https://minecraft.wiki/w/Block',
        'https://minecraft.wiki/w/Item',
        'https://minecraft.wiki/w/Tutorials',
        'https://minecraft.wiki/w/Biome',
        'https://minecraft.wiki/w/Smithing',
        'https://minecraft.wiki/w/Structure'
    ]
    url_crawl(base_url=base_url, urls=urls, output_dir=urls_dir, rough=True)
    crawl(urls_dir=urls_dir, output_dir=Path('crawler_data/rough'))
    
    content_dirs = [
        Path(path) for path in Path('crawler_data/rough').iterdir() if path.is_dir()
    ]
    print(content_dirs)
    split_content(content_dirs=content_dirs)
```

- `urls_dir`: This is the directory where the crawled url will be placed.

- `base_url`: Minecraft Wiki Url

- `urls`: There are 22 categories. You can select which categories to crawl by appending urls of categories to `urls`.

  ![image-20240524上午93305274](./images/image-20240524上午93305274.png)

- `url_crawl()`: Fisrt crawl all pages urls of your selected categories and save them to `urls_dir`

- `crawl()`: According to urls in `urls_dir`, crawl contents of all pages, including text, lists, tables.

- `split_content()`: It is used to split files whose word count exceeds the limit, splitting them in content blocks to ensure that the word count of each file after splitting does not exceed the limit as much as possible.

## TODO

- [ ] https://minecraft.wiki/w/Biome 

  - [ ] Binome name detail pages

- [ ] https://minecraft.wiki/w/Crafting

  - [ ] Hidden formula ingredient quantity information.

- [ ] https://minecraft.wiki/w/Smelting

  - [ ] the page uses an image to represent hunger, need to convert it to text `hunger`

- [ ] https://minecraft.wiki/w/Smithing 

  - [ ] Template, material detail links
  - [ ] upgrading recipe: need to convert images to text info 

- [ ] https://minecraft.wiki/w/Structure

  - [ ] detail links

  

