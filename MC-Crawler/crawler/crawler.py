
from pathlib import Path
import sys
import time
# sys.path.append(Path('./crawler.py').resolve().parent.parent)    
sys.path.append('..')
from bs4 import BeautifulSoup, NavigableString, Tag
from utils.request import get_html_content
from utils.markdown import to_md_table, to_header, to_list, LIST_TYPE
import random
class CONTENT_TYPE:
    TITLE = 'title'
    TEXT = 'text'
    TABLE = 'table'
    LIST = 'list'
    U_LIST = 'unordered_list'
    O_LIST = 'ordered_list'

class MC_BaiscCrawler:
    EXCLUDE_TOPICS = ['Achievements', 'Advancements', 'History', 'Issues', 'Trivia', 'Gallery', 'References', 'External links', 'Sounds', 'Video', 'Videos', 'See also', 'Fixes']
    H_NAMES = [f'h{i}' for i in range(8)]
    
    def __init__(self, urls: list[str], output_dir: Path):
        self.urls = urls
        self.output_dir = output_dir
        if not self.output_dir.exists():
            self.output_dir.mkdir()
        self.total = len(urls)
        self.success_num = 0
        self.failed_num = 0
        self.skip_num = 0
        self.failed_urls = []
    
    def crawl(self):
        for url in self.urls:
            print('crawling:', url)
            filename = url.split('/')[-1]+'.md'
            filepath = self.output_dir / filename
            if filepath.exists():
                print(f'{filename} exists. skip!')
                self.skip_num += 1
                print(f'processed {self.success_num+self.failed_num+self.skip_num} / {self.total}.')
                print()
                continue
            html_content = get_html_content(url)
            all_content = self.get_all_content(html_content)
            if all_content:
                self.success_num += 1
                self.write_to_file(all_content, filepath)
                print(f'crawl {url} success!')
            else:
                self.failed_num += 1
                self.failed_urls.append(url)
                print(f'crawl {url} failed!')
            print(f'processed {self.success_num+self.failed_num+self.skip_num} / {self.total}.')
            print()
            # sleep_time = random.uniform(1, 5)
            # print(f'sleep {sleep_time} seconds...')
            # time.sleep(sleep_time)
        print(f'crawl {self.success_num}/{self.total} success!')
        print(f'crawl {self.failed_num}/{self.total} failed!')
        print(f'skip {self.skip_num}/{self.total} files!')
        print()
        with open(self.output_dir/'failed_urls.txt', 'w') as f:
            for url in self.failed_urls:
                f.write(url+'\n')

    
    def filter_section(self, title: str):
        if title in self.EXCLUDE_TOPICS:
            return True
        return False


    def get_all_content(self, html_content: str)->list[dict]:
        all_content = []
        soup = BeautifulSoup(html_content, 'html.parser')
        h1 = soup.find('h1', recursive=True)
        # breakpoint()
        all_content.append(
            {
                'type': CONTENT_TYPE.TITLE,
                'level': 1,
                'content': h1.get_text()
            }
        )
        mw_parser_output = soup.find('div', {'class': 'mw-parser-output'})
        if mw_parser_output is None:
            return []
        # short description of this article
        first_p = mw_parser_output.find('p', recursive=False)
        if first_p:
            all_content.append(
                {
                    'type': CONTENT_TYPE.TEXT,
                    'content': first_p.get_text()
                }
            )
            # maybe there are many p tags
            # TODO: there still exists condition when p in the div tag, need to handle
            next_sib = first_p.find_next_sibling()
            while next_sib is not None and next_sib.name == 'p':
                all_content.append(
                    {
                        'type': CONTENT_TYPE.TEXT,
                        'content': next_sib.get_text()
                    }
                )
                next_sib = next_sib.find_next_sibling()
        # catalogs of this article
        toc = mw_parser_output.find('div', {'class': 'toc'})
        if toc:
            toc_title = toc.find('h2', {'id': 'mw-toc-heading'}, recursive=True)
            if toc_title:
                all_content.append(
                    {
                        'type': CONTENT_TYPE.TITLE,
                        'level': 2,
                        'content': toc_title.get_text()
                    }
                )
            ul = toc.find('ul')
            if ul:
                all_content.append(
                    {
                        'type': CONTENT_TYPE.LIST,
                        'list_type': LIST_TYPE.UL,
                        'content': self.convert_multilevel_toc(ul)
                    }
                )

        first_h2 = mw_parser_output.find('h2', recursive=False)
        # print(first_h2)
        next_sib = first_h2
        skip_section = False
        if first_h2:
            h_title = first_h2.find_all('span', recursive=False)[0].get_text()
            if self.filter_section(h_title):
                skip_section = True
                next_sib = next_sib.find_next_sibling()
                print(f'start skiping: {h_title}')
        if next_sib is None:
            next_sib = mw_parser_output.contents[0]
        while next_sib:
            for i, h_name in enumerate(self.H_NAMES):
                if next_sib.name == h_name:
                    level = i
                    h_title = next_sib.find_all('span', recursive=False)[0].get_text()
                    if level == 2:
                        if self.filter_section(h_title):
                            # next_sib = next_sib.find_next_sibling()
                            skip_section = True
                            # print(f'start skiping: {h_title}')
                            # continue
                        else:
                            skip_section = False
                            # print(f'stop skiping: {h_title}')
                    if not skip_section:
                        all_content.append(
                            {
                                'type': CONTENT_TYPE.TITLE,
                                'level': level,
                                'content': h_title
                            }
                        )
                    next_sib = next_sib.find_next_sibling()
                    continue
            if not skip_section:
                if next_sib.name == 'table':
                    # table embedded in table: https://minecraft.wiki/w/Note_Block Pitch
                    sub_tables = next_sib.find_all('table', recursive=True)
                    if sub_tables:
                        for sub_table in sub_tables:
                            table_content = self.get_table_content(sub_table)
                            all_content.append(
                                {
                                    'type': CONTENT_TYPE.TABLE,
                                    'content': table_content
                                }
                            )
                    else:
                        table_content = self.get_table_content(next_sib)
                        all_content.append(
                            {
                                'type': CONTENT_TYPE.TABLE,
                                'content': table_content
                            }
                        )
                elif next_sib.name in ['style']:
                    pass
                elif next_sib.name == 'ul':
                    all_content.append({
                        'type': CONTENT_TYPE.LIST,
                        'list_type': LIST_TYPE.UL,
                        'content': self.get_list_data(next_sib)
                    
                    })
                elif next_sib.name == 'ol':
                    all_content.append({
                        'type': CONTENT_TYPE.LIST,
                        'list_type': LIST_TYPE.OL,
                        'content': self.get_list_data(next_sib)
                    
                    })
                # https://minecraft.wiki/w/Redstone_circuits
                # so many dl dt dd tags, process simply
                elif next_sib.name == 'dl':
                    for content in next_sib.contents:
                        if content.name == 'dt':
                            all_content.append(
                                {
                                    'type': CONTENT_TYPE.TEXT,
                                    'content': '** '+content.get_text()+' **'
                                }
                            )
                        elif content.name == 'dd':
                            text = ''
                            for dd_content in content.contents:
                                if isinstance(dd_content, NavigableString):
                                    text += dd_content.strip()
                                elif isinstance(dd_content, Tag):
                                    # https://minecraft.wiki/w/Trading#Java_Edition_2
                                    if dd_content.name in ['ul', 'ol']:
                                        if text:
                                            all_content.append(
                                                {
                                                    'type': CONTENT_TYPE.TEXT,
                                                    'content': text
                                                }
                                            )
                                            text = ''
                                        all_content.append({
                                            'type': CONTENT_TYPE.LIST,
                                            'list_type': LIST_TYPE.UL if dd_content.name == 'ul' else LIST_TYPE.OL,
                                            'content': self.get_list_data(dd_content)
                                        
                                        })
                                    else:
                                        text += dd_content.get_text()
                            if text:
                                all_content.append(
                                    {
                                        'type': CONTENT_TYPE.TEXT,
                                        'content': text
                                    }
                                )
                                text = ''
                elif next_sib.name in ['pre', 'style']:
                    continue
                else:
                    # items Cherry_Boat
                    # TODO: clean
                    # uls in the div tag
                    # replicated content: https://minecraft.wiki/w/Enchanting
                    # so use recursive=False first. but for avoiding data lost, if recursive=False gets None, then use recursive=True
                    sub_uls = next_sib.find_all('ul', recursive=False)
                    if sub_uls is None:
                        sub_uls = next_sib.find_all('ul', recursive=True)
                    # https://minecraft.wiki/w/Trading Notes
                    sub_ols = next_sib.find_all('ol', recursive=False)
                    if sub_ols is None:
                        sub_ols = next_sib.find_all('ol', recursive=True)
                    # tables in the div tag
                    sub_tables = next_sib.find_all('table', recursive=False)
                    if sub_tables is None:
                        sub_tables = next_sib.find_all('table', recursive=True)
                    if sub_tables:
                        for sub_table in sub_tables:
                            table_content = self.get_table_content(sub_table)
                            all_content.append(
                                {
                                    'type': CONTENT_TYPE.TABLE,
                                    'content': table_content
                                }
                            )
                    elif sub_ols:
                        for ol in sub_ols:
                            all_content.append({
                                'type': CONTENT_TYPE.LIST,
                                'list_type': LIST_TYPE.OL,
                                'content': self.get_list_data(ol)
                            
                            })
                    elif sub_uls:
                        for ul in sub_uls:
                            all_content.append({
                                'type': CONTENT_TYPE.LIST,
                                'list_type': LIST_TYPE.UL,
                                'content': self.get_list_data(ul)
                            
                            })
                    else:
                        # assume all other content is text
                        all_content.append(
                            {
                                'type': CONTENT_TYPE.TEXT,
                                'content': next_sib.get_text()
                            }
                        )
            next_sib = next_sib.find_next_sibling()
        return all_content
    

    def get_col_row_span(self, td: Tag):
        try:
            colspan = int(td.get('colspan', 1))
        except ValueError as e:
            print(e)
            print(td)
            colspan = ''.join(filter(str.isdigit, td.get('colspan', 1)))
            colspan = int(colspan)
        try:
            rowspan = int(td.get('rowspan', 1))
        except ValueError as e:
            print(e)
            print(td)
            rowspan = ''.join(filter(str.isdigit, td.get('rowspan', 1)))
            rowspan = int(rowspan)
        return colspan, rowspan

    def get_table_content(self, table: Tag):
        rows, head_column_count = [], 0
        trs = table.find_all('tr', recursive=True)
        # get header
        row = []
        row_spans = []
        for child in trs[0].children:
            if child.name in ['td', 'th']:
                row.append(child.get_text().strip())
                colspan, rowspan = self.get_col_row_span(child)
                for _ in range(head_column_count, head_column_count+colspan):
                    row_spans.append(rowspan)
                head_column_count += colspan

                for _ in range(colspan-1):
                    row.append('')
        rows.append(row)

        header = rows[0]
        max_column_num = len(header)
        for tr in trs[1:]:
            row = []
            column_count = 0
            for child in tr.children:
                if child.name in ['th', 'td']:
                    while column_count < head_column_count and row_spans[column_count] > 1:
                        row_spans[column_count] -= 1
                        row.append('')
                        column_count += 1
                    # https://minecraft.wiki/w/Structure 页面奇怪的某行后面多了一个格子 Buried Treasure
                    if column_count < head_column_count:
                        colspan, rowspan = self.get_col_row_span(child)
                        max_range = min(head_column_count, column_count+colspan)
                        for i in range(column_count, max_range):
                            if rowspan > row_spans[i]:
                                row_spans[i] = rowspan

                        for _ in range(max_range - column_count - 1):
                            row.append('')

                        column_count = max_range

                    # <sup>1</sup>/<sub>3</sub> 
                    # integer text before fraction
                    int_text = ''
                    row_text = ''
                    fenzi = ''
                    fenmu = ''
                    divide_find = False
                    for content in child.contents:
                        if isinstance(content, NavigableString):
                            row_text += content.strip()
                            # unicode not ascii
                            if content.strip() in ['⁄', '/']:
                                divide_find = True
                                continue
                            int_text += content.strip()
                        elif isinstance(content, Tag):
                            # https://minecraft.wiki/w/Raiser_Armor_Trim#Smithing_ingredient Ingredients
                            if content.name in ['pre', 'style']:
                                continue
                            elif content.name in ['ul', 'ol']:
                                # https://minecraft.wiki/w/Trading list in the table
                                for li in content.find_all('li', recursive=True):
                                    row_text += li.get_text().strip()+'<br/>'
                            elif content.name == 'br':
                                row_text += '<br/>'
                            elif content.name == 'code':
                                row_text += '`'+content.get_text().strip()+'`'
                            elif content.name == 'sup':
                                fenzi = content.get_text().strip()
                                row_text += fenzi
                            elif content.name == 'sub':
                                fenmu = content.get_text().strip()
                                row_text += fenmu
                                if divide_find:
                                    row_text = '$'+int_text+'\\frac'+'{'+fenzi+'}'+'{'+fenmu+'}$'
                            else:
                                row_text += content.get_text().strip()
                    row.append(row_text)
            while column_count < head_column_count and row_spans[column_count] > 1:
                row.append('')
                row_spans[column_count] -= 1
                column_count += 1
            if max_column_num < len(row):
                max_column_num = len(row)
            rows.append(row)
        # there are some rows whose columns number are not same; sometimes some rows have one more column
        for row in rows:
            orig_len = len(row)
            for _ in range(max_column_num-orig_len):
                row.append('')
        return rows

    def get_list_data(self, l):
        sections = []
        lis = l.find_all('li', recursive=False)
        for li in lis:
            title = ''
            for content in li.contents:
                if isinstance(content, NavigableString):
                    title += content.strip()
                elif isinstance(content, Tag):
                    # sub lists exist, then extract it later
                    if content.name in ['ul', 'ol']:
                        break
                    else:
                        title += content.get_text().strip()
            section = {
                'title': title,
            }
            ul_2 = li.find('ul')
            if ul_2:
                section['sub_sections'] = self.get_list_data(ul_2)
                section['sub_sections_list_type'] = LIST_TYPE.UL
            else:
                ol_2 = li.find('ol')
                if ol_2:
                    section['sub_sections'] = self.get_list_data(ol_2)
                    section['sub_sections_list_type'] = LIST_TYPE.OL
            sections.append(section)
        return sections



    def convert_multilevel_toc(self, ul):
        sections = []
        lis = ul.find_all('li', recursive=False)
        for li in lis:
            section = {
                'title': li.a.get_text(),
            }
            ul_2 = li.find('ul')
            if ul_2:
                section['sub_sections'] = self.convert_multilevel_toc(ul_2)
                section['sub_sections_list_type'] = LIST_TYPE.UL
            sections.append(section)
        return sections

    def write_to_file(self, all_content: list[dict], filepath: Path):
        # filename = all_content[0]['content']+".md"
        with open(filepath, 'w') as f:
            for content in all_content:
                if content['type'] == CONTENT_TYPE.TITLE:
                    f.write(to_header(content['content'], content['level']))
                elif content['type'] == CONTENT_TYPE.TABLE:
                    f.write(to_md_table(content['content']))
                elif content['type'] == CONTENT_TYPE.TEXT:
                    f.write(content['content']+'\n')
                elif content['type'] == CONTENT_TYPE.LIST:
                    f.write(to_list(content['content'], list_type=content['list_type'])+'\n')


if __name__ == '__main__':
    urls = [
        # 'https://minecraft.wiki/w/Diamond_Hoe',
        'https://minecraft.wiki/w/Diamond',
        'https://minecraft.wiki/w/Diamond_Hoe'
    ]
    output_dir = Path('output')
    crawler = MC_BaiscCrawler(urls, output_dir)
    crawler.crawl()