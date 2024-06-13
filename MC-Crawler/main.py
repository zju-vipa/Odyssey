from crawler.crawler import MC_BaiscCrawler
from crawler.url_crawler import URLCrawler
from pathlib import Path
from utils.markdown import split_file

def url_crawl(base_url:str, urls: list[str], output_dir: Path, rough:bool = True):
    url_crawler = URLCrawler(
        base_url=base_url,
        urls=urls,
        output_dir=output_dir
    )
    # url_crawler.crawl()
    if rough:
        url_crawler.rough_crawl()
    else:
        url_crawler.crawl()

def crawl(urls_dir: Path, output_dir: Path):
    output_dir.mkdir(exist_ok=True, parents=True)
    for file in urls_dir.iterdir():
        if file.is_file():
            with open(file, 'r') as f:
                urls = f.readlines()
                urls = [url.strip() for url in urls]
                output_subdir = output_dir/ file.stem
                crawler = MC_BaiscCrawler(urls, output_subdir)
                crawler.crawl()
    
    pages_name = ['Mob', 'Block', 'Item', 'Tutorials', 'Trading', 'Brewing', 'Enchanting', 'Biome', 'Effect', 'Crafting', 'Smelting', 'Smithing', 'Structure', 'Redstone_circuits', 'Archaeology', ]
    other_pages = [
        {
            "urls": [f'https://minecraft.wiki/w/{name}'],
            "output_dir": output_dir/ name
        }
        for name in pages_name
    ]
    for page in other_pages:
        crawler = MC_BaiscCrawler(page['urls'], page['output_dir'])
        crawler.crawl()

def split_content(content_dirs: Path, word_count_limit=1000, word_count_thres=40):
    for content_dir in content_dirs:
        for content_file in content_dir.iterdir():
            if content_file.is_file():
                split_file(content_file, word_count_limit=word_count_limit, word_count_thres=word_count_thres)

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
    