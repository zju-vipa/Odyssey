import sys
sys.path.append('..')
from bs4 import BeautifulSoup
from utils.request import get_html_content
from pathlib import Path

class URLCrawler:
    def __init__(self, base_url: str, urls: list[str], output_dir: Path):
        self.base_url = base_url
        self.urls = urls
        self.output_dir = output_dir
        if not output_dir.exists():
            output_dir.mkdir(exist_ok=True, parents=True)
    
    def crawl(self):
        for url in self.urls:
            filename = url.split('/')[-1]+'.txt'
            filepath = self.output_dir / filename
            if filepath.exists():
                print(f'{filename} exists. skip!')
                continue
            html_content = get_html_content(url)
            if url.split('/')[-1] == 'Mob':
                print('process Mob...')
                output_urls = self.extract_mob_urls(html_content)
            else:
                print('process others...')
                output_urls = self.extract_urls(html_content)
            self.write_to_file(output_urls, filepath)
    
    def rough_crawl(self):
        for url in self.urls:
            filename = url.split('/')[-1]+'.txt'
            filepath = self.output_dir / filename
            if filepath.exists():
                print(f'{filename} exists. skip!')
                continue
            html_content = get_html_content(url)
            output_urls = self.rought_extract_urls(html_content)
            self.write_to_file(output_urls, filepath)
    
    def rought_extract_urls(self, html_content: str):
        should_not_contain = [':', '?', 'Java_Edition', 'Pocket_Edition', 'Bedrock_Edition', 'Xbox_360_Edition', 'Wii_U_Edition', 'Xbox_One_Edition', 'Nintendo_Switch_Edition', 'Edition']
        urls = []
        soup = BeautifulSoup(html_content, 'html.parser')
        mw_parser_output = soup.find('div', {'class': 'mw-parser-output'})
        a_tags = mw_parser_output.find_all('a', recursive=True)
        for a_tag in a_tags:
            if 'title' in a_tag.attrs and 'href' in a_tag.attrs:
                url_path = a_tag['href']
                if not any([word in url_path for word in should_not_contain]):
                    if '#' in url_path:
                        url_path = url_path.split('#')[0]
                    url = self.base_url+url_path
                    if url not in urls:
                        urls.append(url)

        return urls

    
    def extract_mob_urls(self, html_content: str):
        urls = []
        soup = BeautifulSoup(html_content, 'html.parser')
        mw_parser_output = soup.find('div', {'class': 'mw-parser-output'})
        tables = mw_parser_output.find_all('table', recursive=True, attrs={'data-description': True})
        for table in tables:
            trs = table.find_all('tr', recursive=True)
            for tr in trs:
                tds = tr.find_all('td', recursive=False)
                for td in tds:
                    a_tags = td.find_all('a', recursive=True)
                    for a_tag in a_tags:
                        if 'title' in a_tag.attrs and 'href' in a_tag.attrs:
                            url_path = a_tag['href']
                            urls.append(self.base_url+url_path)
                            break
        return urls

    def extract_urls(self, html_content: str):
        urls = []
        soup = BeautifulSoup(html_content, 'html.parser')
        mw_parser_output = soup.find('div', {'class': 'mw-parser-output'})
        div_cols = mw_parser_output.find_all('div', lambda x: x and 'div-col' in x, recursive=True)
        for div_col in div_cols:
            lis = div_col.find_all('li', recursive=True)
            for li in lis:
                a_tags = li.find_all('a', recursive=True)
                for a_tag in a_tags:
                    if 'title' in a_tag.attrs and 'href' in a_tag.attrs:
                        url_path = a_tag['href']
                        urls.append(self.base_url+url_path)
                        break
        return urls
    
    def write_to_file(self, urls: list[str], filepath: Path):
        with open(filepath, 'w') as f:
            for url in urls:
                f.write(url+'\n')
        print(f'write to {filepath} done!')


if __name__ == '__main__':
    url_crawler = URLCrawler(
        base_url='https://minecraft.wiki',
        urls=[
            'https://minecraft.wiki/w/Mob',
            'https://minecraft.wiki/w/Block',
            'https://minecraft.wiki/w/Item',

        ],
        output_dir=Path('output/urls')
    )
    url_crawler.crawl()
